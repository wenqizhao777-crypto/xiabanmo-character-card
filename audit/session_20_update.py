"""续审20增量维护脚本；只写audit，源文件只读。执行前拒绝重复批次。"""
from pathlib import Path
import json, re, copy, hashlib
from collections import Counter

ROOT=Path(r'C:\Users\Administrator\Desktop\下班魔角色卡重构')
A=ROOT/'audit'
def read(n): return json.loads((A/n).read_text(encoding='utf-8'))
def write(n,v): (A/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def mdwrite(n,s): (A/n).write_text(s,encoding='utf-8')
S=(ROOT/'source/下班，然后变成魔法少女_第1-282章.txt').read_text(encoding='utf-8').splitlines()
ev=read('evidence_records.json'); issues=read('issue_records.json'); missing=read('missing_records.json')
assert len(ev)==535 and max(int(x['id'][1:]) for x in issues if x['id'].startswith('C'))==135
cards={x['id']:x for x in read('card_entries.json')}
chap=read('chapter_index.json')
change={'session':'20','evidence_changes':[],'missing_changes':[],'new_evidence_ids':[],'new_issue_ids':[],'updated_existing_issue_ids':[],'new_missing_ids':[],'expanded_missing_ids':[]}
hist=read('judgment_changes.json')
def E(start,end,level,finding,quote=None):
 id=f'E{len(ev)+1:03}'; q=quote or next(n for n in range(start,end+1) if S[n-1].strip() and not S[n-1].startswith('#'))
 ev.append(dict(id=id,start=start,end=end,quote_line=q,level=level,finding=finding,session='20'));change['new_evidence_ids'].append(id)
def C(title,severity,kind,card,current,problem,evidence,level,accurate,impact,action):
 id=f'C{max(int(x["id"][1:]) for x in issues if x["id"].startswith("C"))+1:03}'
 issues.append(dict(id=id,title=title,severity=severity,kind=kind,card=card,current=current,problem=problem,evidence=evidence,level=level,accurate=accurate,impact=impact,action=action));change['new_issue_ids'].append(id)
def revise(id,addition,refs,reason,card=None,field='accurate'):
 x=next(x for x in issues if x['id']==id);before=copy.deepcopy(x)
 x[field]+=' 续审20：'+addition;x['evidence']+='；'+refs
 if card:x['card']=list(dict.fromkeys(x['card']+card))
 hist.append(dict(session='20',id=id,reason='2026-09-09；'+reason,before=before,after=copy.deepcopy(x)))
 change['updated_existing_issue_ids'].append(id)
def erevise(id,addition,reason):
 x=next(x for x in ev if x['id']==id);b=copy.deepcopy(x);x['finding']+=' 续审20回接：'+addition
 change['evidence_changes'].append(dict(session='20',record_type='evidence',id=id,reason=reason,before=b,after=copy.deepcopy(x)))
def M(category,title,refs,details,scope):
 id=f'M{len(missing)+1:03}';missing.append(dict(id=id,category=category,title=title,evidence=refs,details=details,scope=scope));change['new_missing_ids'].append(id)
def mrev(id,refs,details):
 x=next(x for x in missing if x['id']==id);b=copy.deepcopy(x);x['details']+=' 续审20：'+details;x['evidence']+=','+refs
 change['missing_changes'].append(dict(session='20',record_type='missing',id=id,reason='2026-09-09；卷二260—269连续新证补充时效与收录边界，旧判断保留并限定历史阶段。',before=b,after=copy.deepcopy(x)));change['expanded_missing_ids'].append(id)










E(35330,35391,'A（行动/对答）；D/B（预感与任务猜测）','260金蛇换妆、符文开郊远山洞，安保从治安官变全魔少女、搜郊迫藏。褐鹈在糖果屋范围煮明日秘密武器，烟味争执使金熄。金自称三次不妙预感：二十年前、十二年前园丁端基地、现时；并非三次均已应验或精确预知机制。她抓到黑猫说“你的任务”带兽源、才逼近另任，仍未知刺女王；读者281已明不能倒灌260。')
E(35392,35441,'A（结算/会议）；D/B（未明动机）','261夺牌当夜公开582第一/277第三/629第五；582约六成牌四成奖，观礼占奖大头，纯牌第四。258追逐之后强风陷阱确实完成，借加风将追者吹飞引观众好评，夏由总第二返第一。翠夜备战忧遗漏，折建议开会，交核既有情报后按动机开放讨论；当时只恐袭/战争延续推测，并非已透悉兽源和刺王全谋。')
E(35442,35509,'A（历史调防/接触）；D（灾感）','262切1979夏末，西帕泰克堡失守/第三防线破，矢请求把妮姆等十岁者调内城低烈度护民，石先拒后许只限几人；不是矢擅调或全低龄免战。遇海蒂阿比梅尔郁金香，石女/后勤医疗、只是点头熟，称天使来自旁人；预感灾而非帕败之悲，矢当压力未正式警报。妮姆先失落后获承诺愿护市民，战后是否能回队当时未知。')
E(35510,35592,'A（战事/认知流）；D（保证/信念）','263另两名十岁调防，两日后敌至、进攻三日后援、半月普通军魔术使亡过万与魔少女伤亡逼千，拉锯一月渐优。矢队零伤亡靠全程监控魔装奇境但队外仍丧友；魔反复耗警线、精神疲，强于一般非花牌层。墨报告郁昏/重复警词并少信，矢也曾少信现战线好转以不会突然来安慰，随后爆炸隔十数秒魔镜回防通知；爆炸打断墨谢调妹，不是打断矢已说完的护队承诺。')
E(35593,35639,'A（报告接收/现场/能力）；B（先前演练推断）','264回防收到特殊A信标养分疑似、B小弱如野兽隐入吸A合C至蛹以上可合王蜕的分析，未直接全知最终羽。现场与数月前半蜕相同促矢墨判断或演练，非报告已明同场身份。矢让墨找妹、尺固定群兽留后援接手，再界门收回占用；蕾此时魔量不逊一般花、剪共同黏液概念救线，不是无限范围无成本。')
E(35640,35743,'A（代价/战况/观察）；D/B（新推断）','265蕾剪复数王蜕规则虚弱近坠，三花牌近二十花援；石称孩子非西所以没事/应疏散，后墨回面色证明另亲验妮姆安全。夜至天明与上午苦撑才捷报，非天亮前全收。兽魔近毒不利用、死王蜕不碎，矢后数见两黑影合才想C继续合并、喊外撤但不及；王消失、声音隔绝渐振翅震响、终羽出现。不是黑空间坠出羽，也不由此确立所有羽皆同法制成。')
E(35744,35859,'A（破防/救援/偷袭）；D/B（具体手段）','266织命剪裂/规则被巨大魔差破；羽多层防御、液化连己兽，1分蕾下失能2分花线破两花牌死3分撞碎界门。墨用魔装固定废墟挖矢、两人无力非不肯救。祖门内柱推羽、黑魔球叠术翠猜禁术不知数；顾幸存者收力，击败未杀拟捕，第二羽来祖预埋柱而首羽炮被空间吸；小人波被两羽遮迟察，黑线穿祖。众人只能见机制效果，非祖从始不知第二羽。')
E(35860,35959,'A（身份自报/动作/昙开）；D（伤情与可行性）','267男子自报蜂使徒/自称催化无能令羽停，不自动等现代蜂本人；祖拖话试修伤连辅助禁术不成不明言给众，分空间带三敌离。矢本相亦伤，墨不记昙开因叶只听故事：蕾以上可学、极低成功，石仅教少数有天赋可能送死者，矢已学非等花牌才能学。石认为本相近崩留后掩护、拒矢代死以命令撤，末托海蒂给矢墨但二人不知其死活；人走后独握宝石昙开，不在矢面前唱名。')
E(35960,36033,'A（会师/战斗/观察）；B（归因）；F（敌术全机制）','268昙开波灭，残军数十分钟后会护卫，王庭派花解释祖命令免误逃兵，非矢主谈。护卫见习叶/主力蕾，园丁后来且无妖精长；数千精锐对数万兽，矢墨双控高效但再枯；矢察残兽似妖精底色无暇研究。天空黑框两羽尸后祖坠再蜂出，祖击杀两羽由此强证，祖生死此刻未定、蜂仍伤且冷静而非毫发无伤；黑魔倾战场。')
E(36034,36129,'A（现象/昙开/握今/私心）；D/B（救法假说）；F（抹消机制）','269蜂残渣补兽侵蚀己方，吟词令冲者含熟悉花消失，去哪/死否/机制现场未知。矢无后悔仍悲愤不甘，选择剪昙、让墨后撤传别学傻瓜后句不知说出；曾学习有旁人制止不等首次安全可反复。魔装裂带魔量规则升、最后崩毁被叶墨握今静止，代价释放会加速、她余魔不长。矢只知争时，墨私有规避猜测怕假希望不说、望巨大黑猫伸手；本章尚无咬断明写，281才补断臂成果。英雄名望是事后叙述非当场所有人已熟姓名。')
C('石蒜的昙开教学被限定为花牌并移到旁观现场','MAJOR','能力门槛／信息时点',[111],'111事件八说石蒜教极少数有天赋的花牌，并当着矢面握宝石唱名。','267明确蕾以上可学，矢以蕾学成；墨叶只听不受教。人群撤离后石独处才发动，卡把教学资格、认证身份和见证时间混写。','E543、E544','A','开华蕾是学习下限、成功率极低；认证花牌非同一轴。矢听殿后决定而离开，后通过魔波知道昙开结束。','会禁止蕾期矢已有技能，或让矢看到仅叙述可见的临终动作。','分别记录学习条件、称号和目击/感知边界。')
revise('C011','260凶感三次是本人归纳且第三事态未终，不可写三次全应验；其过去医疗身份、灾前与矢点头之交经262实写。卡32性格段单写丧父与同卡多处石母冲突，仅石蒜母亲亡已证不能另造父亡。后271—275券契/奇境已明仍依E017—E019，不能用260未知覆盖后段。','E536、E538、E543','新读晚回忆回接身份与凶感时效，兼同卡父母称谓维护。',[32,111])
revise('C013','262矢主动调妮姆城内、263队零伤亡仍外友死，264看同型兽才推旧袭或演练，265墨亲见妹安全后归，267离城时再次不知海蒂生死。269墨怕虚假希望未告矢规避猜，伸手尚未写结果；281断臂/妹妹死/认证牌叙述才补全，不能改成先知必救或简单牺牲性人格。','E538—E545','贯通旧独立末段此前的战友承诺和救法未知，不静默用后知替前疑。',[111])
revise('C021','261才写258追逐后强风陷阱与582第一/277第三/629第五，262切史不是263；263爆炸打断墨谢调妹非矢宣言，265捷报在夜后天明上午非天亮前，266羽在界门撞碎而非仅濒失，267才蜂报号/祖分空间。111黑空间坠羽混268黑框返战。267石人走才唱，268撤军自己亲获昙开时间，不是援军会师后还全不知是否争时。所有10月2/3推算仍需服281立秋明示，未强排日历。','E537—E545','完整对照111逐事件，章节/昼夜/主体和见证链错序并入既有问题。',[110,111])
revise('C038','265剪共同规则本相虚弱而266魔差破规则剪裂、267矢自觉本相已伤、269再昙，故老伤与魔装损失有多次事件而非一场单因。石腿不可修是自称伤本相，祖伤辅禁亦未好，各自伤情不自动等同同一诅咒。','E541—E545','补战争内连续消耗与损伤来源，避免新战斗解释倒抹原旧伤。')
revise('S010','260金只听你的任务未知刺王；261翠仍以恐袭/战争猜动机；263墨转述预感与矢重新不忧→264报告/现场→265异常合流即时告警。266翠禁术推测、267祖伤修不成未明告；268祖坠当时生死不明而271祖现存已知，不等同归来方式明。269墨私规避猜不给矢，281结果后补。','E536—E545','最终贯通认知前因，仍分NPC未知与作者私叙。')
revise('S011','260三次凶感自称不是精预言；264报告特殊A疑似信标与现场相似推演练需证据标签；266祖招数叫禁术为翠猜而实际黑球/柱可记；267蜂催化与无法令停是其自述，268两羽死亡有现场迹象，269消散不明确死亡/空间转移。','E536、E540、E542—E545','战果与解释分层，全文末端未解不强行裁决。')
revise('R005','本段L35348褐鹈说女王老太婆后缺尾、L35407第一实不一般衔接异常、L35484及L36052半句截断继续保留，不补写或扩大为整章未读；原著覆盖100只指所给文件全部文本，不保证上游版本无漏字。','E536—E545','最终输入质量边界补记。')
mrev('M017','E540,E541,E542,E544','蕾矢魔量达到一般花、剪多王规则近坠/羽魔差破剪裂；祖顾残军收力、拟捕与实杀阶段分；常规魔法无法消化残兽魔力，攻击/控制有效与长期耗魔分别记。')
mrev('M040','E544,E545','268握今织命并用高效亦耗竭；269静止昙崩只暂缓不抹加速代价，墨的规避猜未说且281后揭断臂，不赋予叶墨免费冻结所有敌人与时间。')
mrev('M013','E538—E545','262—269是一段历史插叙，与270回现及280—281再次插史贯通；夏末、两日、三日、月战、夜/上午、撤军数十分钟为原明确粒度，卡10月2/3不据此算成Canon。')
mrev('M014','E536—E545','金蛇私感/黑猫另任、翠夜会议的动机未明、郁预感传播两人信度变化、妮姆/海蒂安全各时点、祖伤与墨救法隐心、羽尸与祖坠的不同认定，均按人按时间收录。')
mrev('M016','E538,E539,E543,E545','矢要求幼兵适岗而非放弃军责，石粗话照抚→拒代死托女，矢不甘选择昙而墨不愿假希望，战争创伤不能仅写无畏强者/冷漠复仇；承诺不等客观必然护全员。')
knowledge='最后缺口L35330—36129全文逐段读完：260暗任疑、261风陷阱/结算/动机会议，262—269历史防战、羽、祖受袭、石昙、矢昙/墨私猜；和已读270—282贯通。新增E536—E545，C136，旧问题修订7项。所给源文件全读，原著最终实际止282幻命织华发动；胜负机制仍未知。100%后立即最终核验，不进入二阶段。'
def links(s):return re.sub(r'\bE\d{3}\b',lambda m:f'[{m[0]}](01_evidence_index.md#{m[0].lower()})',s)
source_url=(ROOT/'source/下班，然后变成魔法少女_第1-282章.txt').as_posix()
def erender(x):
 c=next(c for c in chap if c['start_line']<=x['start']<=c['end_line'])
 return f'## {x["id"]}\n\n**定位：** {c["volume"]} {c["title"].lstrip("# ")}；[L{x["start"]}–{x["end"]}](<{source_url}:{x["start"]}>)。\n\n**证据等级：** {x["level"]}。\n\n**核验内容：** {x["finding"]}\n\n**附近原文定位片段（不代替整个区间）：**\n\n> {S[x.get("quote_line",x["start"])-1].strip()}\n\n'
def crender(x):
 loc='；'.join(f'[ID {i}｜{cards[i]["comment"]}](<{(A/"card_text"/f"entry_{i:03}.txt").as_posix()}>)' for i in x['card']) or '技术／源文位置见下方定位；[技术目录](technical)'
 pairs=[('严重程度',x['severity']),('问题类型',x['kind']),('角色卡位置',loc),('当前内容概述',x['current']),('发现的问题',x['problem']),('原著证据 / 定位',links(x['evidence'])),('证据等级',x['level']),('更准确的理解',x['accurate']),('可能造成的 RP 后果',x['impact']),('建议处理',x['action'])]
 return f'## [{x["id"]}] {x["title"]}\n\n'+''.join(f'**{k}：** {v}\n\n' for k,v in pairs)
def mrender(x):return f'### {x["id"]}｜{x["title"]}\n\n{x["details"]}\n\n**收录范围判断：** {x["scope"]}\n\n**证据：** {links(x["evidence"])}。\n\n'
for name,records,ids,renderer,pattern in [
 ('01_evidence_index.md',ev,change['new_evidence_ids']+[x['id'] for x in change['evidence_changes']],erender,r'(?ms)^## {id}\n.*?(?=^## |\Z)'),
 ('02_full_audit_report.md',issues,change['new_issue_ids']+change['updated_existing_issue_ids'],crender,r'(?ms)^## \[{id}\].*?(?=^## |\Z)'),
 ('03_missing_content.md',missing,change['expanded_missing_ids'],mrender,r'(?ms)^### {id}｜.*?(?=^#{{2,3}} |\Z)')]:
 s=(A/name).read_text(encoding='utf-8')
 for id in ids:
  x=next(x for x in records if x['id']==id);pat=pattern.format(id=id)
  if re.search(pat,s):s=re.sub(pat,lambda m:renderer(x),s,count=1)
  else:s+='\n'+renderer(x)
 mdwrite(name,s)
s=(A/'03_missing_content.md').read_text(encoding='utf-8')
for id in change['new_missing_ids']:
 x=next(x for x in missing if x['id']==id);header='## '+x['category']+'\n';assert header in s;s=s.replace(header,header+'\n'+mrender(x),1)
mdwrite('03_missing_content.md',s)
write('evidence_records.json',ev);write('issue_records.json',issues);write('missing_records.json',missing);write('judgment_changes.json',hist);write('session_20_changes.json',change)


CFG=dict(start=35330,end=36129,newcards=[],rechecked=[32,111,168],targeted=[110,47,64,89],chapters='卷二260—269，贯通既读270—282',note='最后800行连续语义阅读，合并既有尾段后所给源文件无未读缺口。',title='最终缺口贯通与战争因果回接',scene='正文读到269衔接既读270—282；文件真实结尾是282幻命织华唱名，机制和胜负未展开。',pending=['原著阅读100%已达，立即完成第一阶段最终完整性检查与技术静态范围收尾；不进入第二阶段。'],health='73.55/90.96两次健康PASS；进入最终验收',summary=knowledge,u_note='八组U继续保留：未改卡、未补原著缺字/IF，269不是原著截止，282之后未知仍未知。')
exec(compile((A/'batch_finalize.py').read_text('utf-8'),str(A/'batch_finalize.py'),'exec'))
exec(compile((A/'source_complete_state.py').read_text('utf-8'),str(A/'source_complete_state.py'),'exec'))
