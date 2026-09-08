"""第一阶段收尾增量维护脚本；只写audit，源文件只读。执行前拒绝重复批次。"""
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
assert len(ev)==545 and max(int(x['id'][1:]) for x in issues if x['id'].startswith('C'))==136
cards={x['id']:x for x in read('card_entries.json')}
chap=read('chapter_index.json')
change={'session':'final','evidence_changes':[],'missing_changes':[],'new_evidence_ids':[],'new_issue_ids':[],'updated_existing_issue_ids':[],'new_missing_ids':[],'expanded_missing_ids':[]}
hist=read('judgment_changes.json')
def E(start,end,level,finding,quote=None):
 id=f'E{len(ev)+1:03}'; q=quote or next(n for n in range(start,end+1) if S[n-1].strip() and not S[n-1].startswith('#'))
 ev.append(dict(id=id,start=start,end=end,quote_line=q,level=level,finding=finding,session='final'));change['new_evidence_ids'].append(id)
def C(title,severity,kind,card,current,problem,evidence,level,accurate,impact,action):
 id=f'C{max(int(x["id"][1:]) for x in issues if x["id"].startswith("C"))+1:03}'
 issues.append(dict(id=id,title=title,severity=severity,kind=kind,card=card,current=current,problem=problem,evidence=evidence,level=level,accurate=accurate,impact=impact,action=action));change['new_issue_ids'].append(id)
def revise(id,addition,refs,reason,card=None,field='accurate'):
 x=next(x for x in issues if x['id']==id);before=copy.deepcopy(x)
 x[field]+=' 第一阶段收尾：'+addition;x['evidence']+='；'+refs
 if card:x['card']=list(dict.fromkeys(x['card']+card))
 hist.append(dict(session='final',id=id,reason='2026-09-09；'+reason,before=before,after=copy.deepcopy(x)))
 change['updated_existing_issue_ids'].append(id)
def erevise(id,addition,reason):
 x=next(x for x in ev if x['id']==id);b=copy.deepcopy(x);x['finding']+=' 第一阶段收尾回接：'+addition
 change['evidence_changes'].append(dict(session='final',record_type='evidence',id=id,reason=reason,before=b,after=copy.deepcopy(x)))
def M(category,title,refs,details,scope):
 id=f'M{len(missing)+1:03}';missing.append(dict(id=id,category=category,title=title,evidence=refs,details=details,scope=scope));change['new_missing_ids'].append(id)
def mrev(id,refs,details):
 x=next(x for x in missing if x['id']==id);b=copy.deepcopy(x);x['details']+=' 第一阶段收尾：'+details;x['evidence']+=','+refs
 change['missing_changes'].append(dict(session='final',record_type='missing',id=id,reason='2026-09-09；卷二260—269连续新证补充时效与收录边界，旧判断保留并限定历史阶段。',before=b,after=copy.deepcopy(x)));change['expanded_missing_ids'].append(id)











C('小璐编造的亲子谎言被反写成她本人的信念','MAJOR','认知主体／谎言传播',[46],
  'ID46隐藏信息及phone_catalog.profiles.林小璐的隐藏真相段写“自行相信龙胆是矢车菊的小孩”；同条语言、关系段却写她为圆谎编造。',
  '250小璐当场编造给土狗听，252私下向翠解释并受训；253翠应付土狗并掌书预告任务。卡把编造者、相信或尚在追问的人混成同一认知主体，且与自身其他段落矛盾。',
  'E526、E528、E529；technical/phone_catalog.json profiles.林小璐.sections[隐藏真相与知情边界]', 'A（编造、解释和逐人信息流）',
  '小璐知道该亲子说法由自己编造；龙胆的魔法少女身份边与林昀男性本体边应分开。完整身份链未知不等每条边都未知。土狗的亲子疑问和掌书所知另依C015，不能迁给小璐。',
  'NPC会忘记自己在说谎，追问虚构生育史并丢失掩护动机。',
  '后续同步两份资料并按说谎者、听者和时点记录；不因修正这一信念就授予小璐男性本体知识。')
C('手机将林小璐与林昀的亲生父女关系改为收养','MAJOR','血缘关系／资料副本冲突',[],
  'phone_catalog.profiles.林小璐的身份与关键关系写林昀养女/养父，profiles.林昀关键关系写自己的养女；世界书ID46则写亲生女儿。',
  '卷二72林内心明确“只有你是我亲生的”，92又在亲生血脉与魔装相似的思考中提及；没有原著的林小璐收养转变。手机副本把白静萱式家庭关系套入另一主体，不能以角色卡副本的亲生写法作为唯一证据。',
  'E312（L20854）；源文L23697—23701；technical/phone_catalog.json profiles.林小璐/林昀 的关键关系及身份与定位',
  'A（原著内心叙述中的既有父女关系）',
  '在所给原著中小璐是林昀与安雅的亲生女儿；血缘事实不等小璐知道父亲的魔法少女身份。对夏凉和白静萱的家庭接纳分别记录，不以重亲情为由混淆血缘。',
  '同一玩家经正文和手机得到不同身世，父女和解与身份保密的基础被改写。',
  '后续修正手机对应两人物及raw/sections同步关系；若有意更改血缘须列U003可选IF，不能作为原著秘密反转。')
erevise('E312','本条L20854明确林昀不能向女儿解释“只有你是我亲生的”；收尾据此核对手机养女误写（C138），亲生关系为叙述中的既有事实，不把其育儿建议一并升为客观有效疗法。','2026-09-09；手机完整资料复核发现父女血缘副本冲突，回接既有范围不重复登记证据。')
revise('C019','所给源文现已完整读完；相关收取、馈赠、贡献和认证积分仍未确立普适排他尾刀所有权，也没有据此确立相反法条。维持POTENTIAL RISK／制度F；U005保留玩法选择，而非继续等本文件未读章节。','E448、E545','全文收尾，移除旧未完成阅读前提，保持绝对制度未证的等级。')
revise('C020','完整阅读结束后，具体逐人书写紧急撤退路线仍未获对应原场景依据；保留U003疑似补桥。已获支持的联系方式、授课和后期家事揭露不重新列为无源。','E045、E064、E067','消除旧待核阅进度，疑似IF不转成事实。')
revise('C057','100章已由玛向翠转述木父弃置琴行、店主夫妇收养后木为灯盏名义妹妹的家史（D；E370）；不再是本审计未读背景。木本人仍信寄养父会回，不能将转述真相提前给她。','E370','后文家史已核而本项残留未读句，明确现行知情边界。')
revise('C089','全文结束仍不把私比认输规则扩成认证任意退出制度；后期停考指令、被敌方结界阻挡与积分结算分属C016/M011/M041。旧完整制度待核仅是历史进度。','E013、E296、E302','分开私比、认证和敌袭阶段，并关闭本文件未读等待。')
revise('C098','源文100%后仍仅判定卡所标66章具体场景、十年承诺和前置的关系保证没有对应依据；不会以此否定原著其他阶段真实出现的退役讨论。未读后文的旧措辞停止作为当前状态。','E295—E297、E308—E312','全文完成后的结论范围维护，无源特定承诺不等禁止一切同题对白。')
revise('C013','手机妮娜/妮姆/塞米相关记录也须按阶段同步（见technical/CATALOG_REVIEW.md）。83已述塞米划伤本相导致永久失臂，281明确右侧；因果不是完全未知，但现场具体动作不可补成咬断。269伸手与281转述不让翠当时直接知道塞米全过程；人皮面具应守109皮质面具的材质边界，不推断人皮来源。','E334、E395、E545、E033','收尾将分章节伤情链回接，纠正可能把场面未详写误判为完全无因果的倾向。')
revise('S004','完整语义核对手机后，妮姆能力/结局、蜂使徒现时战果、雪毬能力、羊踯躅受控与刺王偷听等仍有269式过期未知。282《琥珀》才是所给源文件结尾；这是输入范围，不是宣告作品全部悬念完结。','E014、E016、E035、E036、E040','发现第二套资料的同源旧状态，保留旧问题编号不重复分裂。')
revise('S014','75人物全部sections与raw对应内容、36地区/23势力（已读世界书相同段逐字校验＋不同段全文读取）、50CG及10别名键已完成内容审计。映射见technical/CATALOG_REVIEW.md。小璐手机养女为新增C138；同人物谎言主体为C137。未明段自身与已知段冲突也需修，如柏安队称灯盏能力未展开、花园是否小世界仍未知；不能把资料末段的保守措辞当更高权威。','E544、E312、E526—E529','完整副本内容审计补充真实覆盖和重复错误导航，不将全目录自动注入提示。')
# 直接修正当前字段中失效的阅读状态；完整前值仍由judgment_changes保存。
for id,field,old,new in [
 ('C019','problem','目前未完成其他回响场景核验，不能下定论说相反规则已证实。','全文相关场景核验后仍不能下定论说相反规则已证实，具体分配与普适所有权需分开。'),
 ('C019','action','进一步考据；如为游戏分配机制，USER_CONFIRMATION_REQUIRED。','保持绝对制度未证；如有意作为游戏分配机制，见U005 USER_CONFIRMATION_REQUIRED。'),
 ('C020','accurate','书面撤退路线仍待核','书面撤退路线经全文审计仍无对应原场景依据'),
 ('C057','accurate','收养背景本轮未读，不以卡内背景作事实权威。','收养背景由后文E370补足，保留玛转述等级，不以卡内背景作事实权威。'),
 ('C089','accurate','认证退出的完整制度仍待核','认证退出不因私人比试规则而获得普适制度证明'),
 ('C098','accurate','不断言未读后文永不讨论退役','不据此断言原著其他阶段从不讨论退役'),
 ('C098','level','F（该场景之外后续是否有相似台词）','F（卡中具体十年承诺的对应原著依据）')]:
 x=next(x for x in issues if x['id']==id);b=copy.deepcopy(x);assert old in x[field];x[field]=x[field].replace(old,new)
 hist.append(dict(session='final',id=id,reason='2026-09-09；当前有效字段清理已失效的阅读进度表述，非删除历史判断。',before=b,after=copy.deepcopy(x)))
 if id not in change['updated_existing_issue_ids']:change['updated_existing_issue_ids'].append(id)
scopes={
'M017':'世界书和手机已有框架与多段实例；不足是散落条件和阶段连接未充分汇合，不能称整卡完全没有。',
'M018':'ID92有部分终身制背景、ID93有制度入门，手机亦含相关概括；收录需求是基础规则与实际运转的连接和个案边界，不重复算缺名词。',
'M021':'ID3有三要素/等级框架，ID94有田胜，手机田胜/魔术使也有部分成本；缺口是媒介寿命、代价及合作解障分工，非整卡全无媒介资料。',
'M023':'ID17和手机白静萱已有治疗与阶段框架；本项保留首次表现、验证路径和无法实现承诺。本相结构、兽子/祭子后补依本项details所列的后续证据，未解成因仍未知，不再等待本文件未读部分。',
'M027':'ID98及手机苏胜紫、林小璐等已有手游经历，不能称整卡全无游戏；不足在公共文化历史、题材限制、资本和信息源不确定性与传播过程，游戏设计者仍未确证。',
'M029':'卡100概括成年外貌、卡53/手机玛已有歌后身份；不足是升格时的程序与有限调整条件，不扩为日常任意改龄，也不混同红备用躯体。',
'M031':'卡0/7有失踪索引，卡53有旧友，手机苏胜紫已有角色资料，故不是全卡缺人；缺口在研究行为、拒绝权贵条件及自主性。拒邀理由为苏自述D、失联为玛消息，不推定当前阵营；九年误写见C095。',
'M033':'卡101/102和手机白静萱有文化学习、身世、亲情概括，未充分收录回校择校计划的私下讨论、条件与未实施状态。控兽仅翠期待，非客观疗法；与M023/M019互引，独立记录社会关系建立条件。',
'M037':'卡2、卡31及手机魔法少女/具体人物有评级术语和A-/SS等，不称全卡缺制度名；需补评估维度、可变性、潜力预测与技术假说限度，个人王钥战术仍M017。'
}
for id,scope in scopes.items():
 x=next(x for x in missing if x['id']==id);b=copy.deepcopy(x);x['scope']=scope
 change['missing_changes'].append(dict(session='final',record_type='missing',id=id,reason='2026-09-09；完整手机资料交叉审计后更新收录层级，保留原范围判断的前值。',before=b,after=copy.deepcopy(x)));change['expanded_missing_ids'].append(id)
exec((A/'batch_render_fragment.txt').read_text('utf-8').replace("session_12_changes.json","final_changes.json"))
print('final records saved',len(ev),len(issues),len(missing))
