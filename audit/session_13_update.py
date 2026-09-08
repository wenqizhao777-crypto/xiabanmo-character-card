"""续审13增量维护脚本；只写audit，源文件只读。执行前拒绝重复批次。"""
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
assert len(ev)==375 and max(int(x['id'][1:]) for x in issues if x['id'].startswith('C'))==112
cards={x['id']:x for x in read('card_entries.json')}
chap=read('chapter_index.json')
change={'session':'13','evidence_changes':[],'missing_changes':[],'new_evidence_ids':[],'new_issue_ids':[],'updated_existing_issue_ids':[],'new_missing_ids':[],'expanded_missing_ids':[]}
hist=read('judgment_changes.json')
def E(start,end,level,finding,quote=None):
 id=f'E{len(ev)+1:03}'; q=quote or next(n for n in range(start,end+1) if S[n-1].strip() and not S[n-1].startswith('#'))
 ev.append(dict(id=id,start=start,end=end,quote_line=q,level=level,finding=finding,session='13'));change['new_evidence_ids'].append(id)
def C(title,severity,kind,card,current,problem,evidence,level,accurate,impact,action):
 id=f'C{max(int(x["id"][1:]) for x in issues if x["id"].startswith("C"))+1:03}'
 issues.append(dict(id=id,title=title,severity=severity,kind=kind,card=card,current=current,problem=problem,evidence=evidence,level=level,accurate=accurate,impact=impact,action=action));change['new_issue_ids'].append(id)
def revise(id,addition,refs,reason,card=None,field='accurate'):
 x=next(x for x in issues if x['id']==id);before=copy.deepcopy(x)
 x[field]+=' 续审13：'+addition;x['evidence']+='；'+refs
 if card:x['card']=list(dict.fromkeys(x['card']+card))
 hist.append(dict(session='13',id=id,reason='2026-09-09；'+reason,before=before,after=copy.deepcopy(x)))
 change['updated_existing_issue_ids'].append(id)
def erevise(id,addition,reason):
 x=next(x for x in ev if x['id']==id);b=copy.deepcopy(x);x['finding']+=' 续审13回接：'+addition
 change['evidence_changes'].append(dict(session='13',record_type='evidence',id=id,reason=reason,before=b,after=copy.deepcopy(x)))
def M(category,title,refs,details,scope):
 id=f'M{len(missing)+1:03}';missing.append(dict(id=id,category=category,title=title,evidence=refs,details=details,scope=scope));change['new_missing_ids'].append(id)
def mrev(id,refs,details):
 x=next(x for x in missing if x['id']==id);b=copy.deepcopy(x);x['details']+=' 续审13：'+details;x['evidence']+=','+refs
 change['missing_changes'].append(dict(session='13',record_type='missing',id=id,reason='2026-09-09；卷二74—89连续新证补充时效与收录边界，旧判断保留并限定历史阶段。',before=b,after=copy.deepcopy(x)));change['expanded_missing_ids'].append(id)



E(24908,24999,'A（出发、身份核验、舱位与胜负）／D（行程预计）','2月10日9点出发，柏安三后辈已于一周前返城，玛红留守。林因局经费只批两间双床经济舱；港口真成年人证件通过，不是假宝石通行。夏飞行棋三胜获同舱，小一胜白二胜、翠一胜且加试卷为玩笑；翠要求守约不耍赖，不用任何战斗检定替代此局。次晨燕南、再下一日下午入国为计划，后文实到吻合。',24910)
E(25000,25130,'A（夏的主动照料、小白互助与学习进步）／D（策略与竞争宣言）','夏说明温柔港湾策略，明确让翠早睡且实际没有小动作，动机公开不等全无依恋。另一舱白几次没找到厕所，小带路并教西罗语；半年补习使小成绩跟上、语言较好，白外语从零但阅读助科学和东华语。互助与争宠可同时成立；小已知道翠筹备白重返校园。白再次把妈改老师，100公开例外不等约定解除。',25116)
E(25133,25153,'A（燕南实际抵达、车站和城市结构）','次晨即2月11日平安到燕南，巴士一小时余入市。中央都市面积常为普通城5—10倍、交通与科技更发达，优势源于专列停站。车站结界要求票与一定魔力作引路，不是普通人随意误入；获许可者可经商旅游进修/公务，如何满足普通人引路条件本段未说。',25147)
E(25154,25214,'A（证件核验和车内机制）／D（手续说明和摩可拒绝）','普通入国申请经异策局报民治院、通常月内答复、限时证离境回收；认证牌可通行、新人用准考证。翠已向三后辈说秘密任务藏身份，以龙胆新人入列。中转层票贴晶柱送往车厢、空间扩容近百节；68号欧培拉提供自助和借阅归还。播种者随行是惯例非明文义务，已获官方认证的摩可仍断拒返国且未解释。',25167)
E(25215,25303,'A（土丁桂初遇、外貌与伪年龄暴露）／C/D（潜力传闻和翠估计）','翠从他人谈话才知土丁桂名与抱队友意图，见其专注塑能术式书后离开；观景车才实际交谈。灰白半扎双马尾、白衬衫浅马甲深蓝裙，似混血非谱系确认。土见其像自己九岁妹妹而问，翠实际36快37，才翻证发现龙胆10岁，欲报16被读证打断。越幼越高潜力被原文称无据传闻，不能当规则。',25294)
E(25238,25254,'A（列车权限与旧队旅行记忆）／D（主厨传闻）','额外车厢按会员/认证牌分权限；潜修、实验、加固训练等不是新人免费全开，观景车为少数可见外景处。旧方亭四人初赴认证先向邻市求留守援助、向局求路费，安雅拉困倦翠来看景、苏将睡照拍成获奖作品，玛曾险被甩出窗。回忆不等当日全队在国度，亦非战争参军四人同行。')
E(25305,25417,'A（海路、守卫及放行）／D（通行警告与伪任务内容）','104次日下午即2月12日，海洋防卫难所以少沿海城而非海全消失。五界门各通不同都，材料畏惧说明与双生人形妖精守卫分开；近门对彼此面貌遮蔽后变身。小夏先过、白被要求例检但真实动机未明确，翠持祖正式印章的实验素材任务文件解围；另为小和夏准备证件不等本次三人都受同一检查。',25415)
E(25418,25444,'A（界桥适应与翠经历）／F（当次异象根源）','界桥除稳定通路外使普通人及掌魔不深者适应两界差异，免病变乃至肉体魔力化器官失能；少女通常不需此生理适应。翠独行见听别回来、旧记忆翻涌，撕碎阴影推门说我回来了。可记录体验与动作，尚不能将其定为守卫施咒、客观时空故障或具体幕后人命令。',25429)
E(25446,25525,'A（等待、借口、知识告知与手环）／D（翠对妖精的评价）','白先告小夏被拦后已放行；三人等近10分钟再5分钟，翠用空间连接波动解释迟到，原文明确不是实际原因。该故障作为一般现象确有国度预案。翠只告守卫人形妖精罕见、界门/王庭多见、很厉害。新人龙胆装作不懂手环；无魔力区才强制佩戴，抑流外放且警报，不是国度全域禁魔。',25479)
E(25526,25586,'A（四区和网络）／D（不具名效率统计）','卢恩诺雷常住数百万流动千万，四区分民生禁大多数术式、学院两名校、魔法侧浮岛、研究院限制区。正统教育效率倍增为不具名统计。城市有手机信号及物质界地图应用，网络原靠国度技术；小的童话想象被纠正，翠当时没听全，只误以为兴奋脱力。')
E(25588,25702,'A（互解术式、交通和住宿）／D（温泉美容传闻）','无魔力区不是实际无魔：全城互相理解术式仍工作，妖精语能被听懂。43号起飞点出禁区可自己飞；浮岛普通人可花钱乘空艇/用道具，非绝对禁止。彩云湿地房间虽散布，方亭四人实际住同一四床屋，隐私隔断可自行开启而非仅夜晚。温泉分男女妖精及内外浴，防误入术式；美容回流是翠明说听来的，不把感受当疗效证实。',25651)
E(25653,25794,'A（误认、隐瞒与认人未完成）／D（泡浴解释）','夏仍误以翠原本女性、用另一性别生活多年，翠欲纠被小插话打断；小未听私谈。翠闭眼为避嫌，感官代偿是临时借口；小相信不等客观魔术规则。继续服役永葆外貌不延寿，用来解释变前后相同仍为掩饰。去治疗是实际安排，翠基于数月帮助愿信祖却不能百分百排陷阱。出浴只感熟人被后辈打断，111才确认是墨荷。',25745)
E(25796,25911,'A（首次真身、盟约表达和并行研究）／D（年龄/好感玩笑及工作倍数）','书廊邀请学者不封闭于知识，外界未辟谣不等证实。核心成员因祖罕见妆发见客而担忧，未见客真容。祖与翠本次首次真身相见，影子游戏/好感点数是缓气氛和求认可；17岁百进制对话不能据算年龄，更不是真实好感系统。翠半真心半功利认可并求助后开私室，十余近二十玩偶视野支撑多地并行与数据转移，睡时重复工作不等任何科研全自动。',25889)
E(25912,25945,'A（治疗开始与材料操作）／D（专业原理与材料来源）','祖取真心之花、让翠躺床，前疗程已止魔溢、碎片贴合改善。取爱之源，称心之宝石原料、10毫升造一心之种，严格限制蔷薇宫/花园及少数魔事院话事人、研究申请难。其大量来源仅称朋友；修的是宝石而非开身体刀。困感让翠睡去，不是已见普通麻醉或全部失控原因最终解答。',25927)
E(25947,26008,'A（战时回忆框架与编制）／D/E（石蒜说辞和战友昵称）','十五岁矢车菊与樱主动参军，国度未强制物质界少女；玛苏因城防和播种者劝说留下，非四人同行。两军含少女/妖精、魔术使、普通军人或残兽，烈度升级后重组，矢樱分赴卢恩诺雷/多姆利亚队长任。石蒜疲惫花牌前线调任，三名10岁新兵因缺人分配；选矢为救人声望，保姆权杖是昵称不是真权杖。其军纪威望差不等无职责与善意。',25994)
E(26009,26079,'A（姐妹身世、行贿及接纳）／D（战力自许与错猜）','矢15岁领11队员；妮娜14、妮姆10。双亲死残兽，姐姐早当少女养妹、13获白牌，妹银廊三年刚契约月余。为同队妮娜把全部回响给石蒜，矢从权贵镀金猜测修正为被骗孩子，拒钱且指出危险任务需要能力，不收无谓赴死承诺；派其一月教妹，否则申请除名。墨荷姓名和队伍关系此回忆明示，非立刻治疗其右手。',26077)
E(26080,26138,'A（修复后实际试用和缩高）／D（稳定期与再损警告）','术后丝线无魂痛、奇境顺展，繁开只做到起手即被祖制止，未完成。毁掉两魔装不返，祖说修处需7/10天、保险等开考并静养，材料补缺不重雕，若再献祭林昀会消失。不能写完全恢复所有魔装、永久无风险或手术当场成功繁开。翠测身高再矮2cm，非所有身数据固定缩小。',26120)
E(26140,26190,'A（后辈报到与反应）／D（官方史说、观礼预测及学生猜测）','109与治疗同日，三人现场报到；女王可能观礼而非已到。官方说40年前战争、20年前战后及大兽灾导致两次缺席，上次60年前；临时抬难劝退为谣传。小猜女王识全部魔色后又为安慰白改口，夏指出观点不改事实；翠保证让白安心不等实际拥有免捕特权。',26157)
E(26193,26258,'A（城市防护、修轮椅、表情变化和通讯）／D（老人识人理由）','国度仍有残兽风险，但少女多且花园战后加巨物迟缓可疏建；无魔区370余小街区。翠帮修轮椅，老人凭眼神认少女是经验评价；治疗后能更自然表情，早期绷脸不宜永久化。林手机收到小报平安、回复加玫瑰，翠手机未被打扰；报到本可线上/术式远程，小坚持不用科技才亲去。随后为三人买巧克力。',26219)
E(26259,26361,'A（陵园初访、忘证及摘面具识人）／D（民俗来源）','气云糕为祭品传统促翠从店员首次听陵园并临时前往，不是已约墨荷。七像三少女一妖精三人，战争英雄公共叙事与翠恶心创伤记忆不同。门卫可收认证牌，少女忘记；她称队长，翠先有熟感但脸不符，摘皮质面具才认妮娜/墨荷、牌13251。面具原文只说皮质，不据卡64人皮扩具体来源。',26360)
E(26362,26426,'A（祭礼、外观与私谈行为）／D（义肢解释和幸福半答）／C（翠理解距离）','现代祭奠扫墓、致信、安魂诗，供品匣半月风蚀；女王七夜葬礼源头为据说。墨荷此刻琥珀圆眼、短马尾黑红学生装，与爪痕场金竖瞳分期；翠记右手本相曾斩，猫爪是妖精技术义肢为墨荷自述，翠有疑不深追。翠只答找到幸福半真，认为队长或为社交旧称、保持距离；这是其看法不等墨荷感情淡了。熟练祭礼支持多次悼念，不证20年每日连续到访。',26395)
E(26427,26453,'A（卡丁车送行与邀请）／D/C（双方观感）','墨荷以无普通汽车结构的微型魔导车送翠，翠碍于不伤期待接受，仍不舒服。墨荷邀明天下午已预约甜品店，不等翠当场已经答应；正式应允111。未把送行愿望等同两人感情全面修复。')
E(26454,26493,'A（国度生产结构与采购认知）／D（节庆与营销说法）','魔导工具/基础术式降低必要劳动，70%以上倾向个体经营，家庭作坊与个人时间使节假日不整齐；价值集中术式/集成技术/生产，再到传统产业，接触者以上可生产工具。甜品商家竞争以口味服务取胜，材料包配机器仍需投入不是无物质代价凭空万能。店员说巧克力可给喜欢者亦可谢朋友；小此前不关注、白只记有巧克力、夏未认真了解，三者不是一概完全没听过情人节。',26455)
E(26494,26563,'A（熟人确认、邀约应允与军礼失败）／D（伪任务口径）','翠核实106擦肩为墨荷、同住湿地几百米，墨荷称国度任务、翠按旧识经验觉未撒谎，不能升级她合法公务。墨荷不觉翠伪装有多大变化，没说明独特识破术。翠拒入屋避免同伴识出，因担心旧友且有真情才答次日用餐。蔷薇引航月守归途为旧军誓，翠能回话却举不起回礼，不等此刻把全部往事告知。',26552)
E(26564,26609,'A（远程职责、正式核件与承办新讯）／D（碎片转述）','红代管部分局务、每周通话互报，而翠仍远批非甩手。方亭因战绩/重建获五月州研讨会，原去年八月定临扬因黑烬灾转移；临扬/太余/新约遭重创，临扬两区毁及防网受损，不能只讲方亭获奖而漏灾害因果。绿塔仅候选。小吃酒心后黏人打断，两人约再谈；夏白隐藏采购，翠只猜另瞒事不知全计划。',26583)
E(26610,26680,'A（次日准备与前日采购回叙）／D/C（生日口径与小的推理）','113当前2月14，上午复习、翠离开后仅下午傍晚制礼。回叙13日白告诉小林生日明天、来源林自述；小串起糖和新年办公室，得知频繁联系但非确认法律已领养或父翠同一。她提蛋糕视频+寄送，白担心坏，店员确认国度有甜品冷链。夏最后获计划因知双身份而笑，尚未真的视频/寄出。',26673)
E(26681,26741,'A（购买两套常服、通讯及街头解围）／D/C（风险判断与解释）','114同2月14，翠两套小尺码衣一套已穿，以林手机问小礼物对象后安心，无早恋证据。提前一小时仍见墨被可疑举报，自己保持距离、获准靠近出证私谈，后说明以退伍少女性格受战影响解围且承认未必全符合。墨说看透她是反馈，非客观临床判定；治安官只得这份有限解释。',26734)
assert ev[-1]['id']=='E402'
C('彩云湿地住处分散概括遮掉四人同屋四床安排','MODERATE','空间状态／相处条件',[116,104],'卡116称把分散的观景房作为赴考据点；卡104虽有四床同屋，地区常驻描述仍易给出多屋。','106明确翠为避免舱位争夺专订同一间大景观房、四张单人床；旅馆整体房屋散布与小队实际住法不能混写。','E386','A','旅馆各屋相隔，小队四人同屋；墨荷另屋几百米外。隐私术式可开启，不限夜间。','会错误生成分房、跨屋走访、旁听条件与私谈距离。','后续区分酒店整体布局、当期房间分配及隐私状态。')
revise('C021','104把104—106到站/入境/住宿写2月11，实际101于10日出发、102次晨11日燕南、104又次日12日下午抵海站；107—108翌日疗伤为13日，与109另一边同日而非12日治疗后隔天。卡105把采购/制礼并在13夜需分113当天14日与13日回叙；14日下午买两套一套已穿，非仅一套。103摩可拒随行、104多份掩护文件不前置成101已给全后辈解释。','E376、E378、E379、E382、E387—E394、E400—E402','当前卡104/105连续日期与正文连续锚点交叉核验。',[104,105,122])
revise('S003','本批直接锚10日出发，11日燕南/专列、12日门/彩云湿地，13日治疗与三人报到并行，14日制礼赴约；卡104中段整体早一天且和本卡109互相错开。107治疗没有独立12日依据。','E376、E378、E382、E387、E392、E393、E401','按原著相对日序修正卡日期，不重排既有史段。',[104,105])
revise('C038','108术后实际丝与奇境试用无痛，繁开仅起手被阻止；祖要求7/10天稳定、保险至开考静养，两毁魔装仍不返。再献祭使林消失是本次专业警告，不等所有普通魔装使用按次损本相。109表情较自然也来自痛苦减轻。','E389、E392、E394','原先疼痛状态已失效，更新治疗后状态并保留稳定期风险。',[104])
revise('C008','108宝石裂隙已修补、实际魔装无痛，仍有永久毁缺及新材料沉淀要求；不能以旧裂痕灰尘定义心之花，亦不把新补完等同从未受损。','E389、E392','同物品完损状态随治疗改变。')
revise('C096','107说明前置疗程已止魔溢，108修复后祖正式警告再献祭会使林昀消失；这一后来的有条件风险不反证63丝结当时已证明男身濒消。当前已能无痛施丝/奇境，稳定前不宜繁开，病因链与再损危险分开。','E389、E392','后文加强条件性危害但推翻把其提前当已确诊的写法。',[104])
revise('C005','103明确摩可现在已是官方认证方亭播种者，却坚决拒返国而不解释；随行只是惯例无明文强制。仍不等偷身份、任命手续幕后与拒返原因已破案。','E379','新的拒返行为和合法现职并存，继续保留开放悬念。',[104])
revise('C013','108明确妮娜14/妮姆10、同队因姐妹恳求及石蒜收回响；矢起初疑镀金后知真相转接纳。109摘皮质面具才认墨荷，110义肢妖精技术为其自述而翠存疑，111国度任务也只被翠暂信；不可让当前翠拥有读者已知黑猫全貌。旧末段关于妹妹/义肢等结果仍有效但不提前NPC知情。','E391、E395、E396、E399','補全早期关系与重逢认知，保留后期结果的时效。',[104,105])
revise('C066','卡104幕末三后辈不知昔日矢车菊又犯全称错误，夏早已知旧号；她103知龙胆掩护、106仍误解性别变向，两件事应分开。105只有夏懂生日双身份的描述可保留，不能因别处摘要错就抹掉。','E379、E387、E401','相同知识全称错误回接旧ID并保留卡中正确差异。',[104,105,81])
revise('C043','102夏公开温柔港湾策略并让翠真休息，回应先前翠教她表达用心；106仍以原女后男理解身份，纠正被打断。亲密、体贴、理解错误可以并存，不把只会操纵/完全理解任一端当固定性格。','E377、E387','关系发展与剩余误解同步记录。',[104,81])
revise('S009','103龙胆新人身份用准考证，104翠本已魔法身体再借假宝石更衣，不是从男身才可伪装。107分别拿真心之花与假心之芽。114新常服已购一套已穿，不能将旗袍永久锁死或脱衣装即还原男身。','E379、E382、E389、E402','新实用阶段验证伪装与身体状态独立。',[104,105])
revise('C111','101和102白又把妈收成老师，说明100公共例外未证明私下约定已正式废除；准确处理为有约定、有破例、有当场收口，不能反向固化为总能公开叫。','E376、E377','紧随后文反向收窄本批前判断，不静默删除100例外。')
revise('C112','卡4又把自动书记年代写成与翠/安入道吻合的王权暗线，应沿98已明确的未知关联限定；线索相近不能升级因果或确证门。','E365','跨卡复核发现同一推断升级口径，回用旧号。',[4])
revise('R005','103申请的接过、109科普魔术使/魔法使混称、110消洱等字面疑点不改原著。111墨荷说队长没有留长发，与假衣装挽髻可并存为视觉表述，不推新剪发。114战争影响说辞明确是为解围所构且未必符合，不当医学诊断。','E379、E399、E402','新字形及观察层次保留，不升为Canon修补。')
knowledge='101真实成年证件过物质界港口；103三后辈已获秘密任务假号口径但非治疗政治，土丁桂见准考证误认10岁新人；104白被拦、小夏已过，白到达后转告。105翠以连接波动假说辞遮实历，三人相信。106夏性别方向误解仍未纠正，小没听私语；熟悉旅客未认。107研究院核心人员没见来客，108伤愈实效与献祭风险只有翠祖知道。109小向林手机报平安、翠自己首次听陵园，摘面具才认墨荷；110翠把队长称谓推社交礼节并保留幸福半答。111翠才确认106熟人，墨国度任务/义肢为自述。112收到红核实会议文件，孩子仅旁听尾部；113白先告小父生日、夏最后知计划。114巡警只得翠的有限解释，不知黑猫组织。'
revise('S010',knowledge,'E376—E402','全链按接收者实历记录，不用叙述全知替代。',[104,105])
revise('S011','翠对界桥异常不坦白；土丁桂看十岁证不疑、又不识旧号，翠不懂她为何注视直到问答。墨荷忘认证牌和面具才形成初遇障碍，未证她有识破所有术的能力。女王观礼可能、全场识魔与培训效率传闻、温泉美容均分等级。','E380、E383、E384、E386、E393、E395、E399','开放推理有真假与传播时点，保留可犯错的NPC。',[104,105])
erevise('E352','103已用龙胆准考证，104实际入境，114常服购置；衣装和证件方案部分落实见E379/E382/E402，不继续一概待办。','后续执行节点补齐，保留92当时状态。')
erevise('E372','101已明示柏安后辈一周前返城，106湿地入住之后111确认熟人；100祈愿不等未来安全已保证。','送别后实际去向有新证。')
M('世界规则','国度魔导生产、个体经营与技术价值链的社会基础','E398,E400,E401','标准术式和魔导工具大幅降低必要劳动，70%以上国民倾向个体经营、家庭作坊，使节日与工作时间个人化；价值集中术式创造、工具集成、生产能力。生产工具可由接触者以上魔术使从事，但创造新术/集成需要更高专业，材料包仍是投入，不能泛化无成本创造一切。甜品竞争、跨界冷链与异策局会议等把技术、商业、公共事务连起来。','已核卡4/6及130/139/150主要政治/分区/消费，缺少这条能生成职业与生活选择的生产结构；不是说国度商店或冷链词全部缺失。与M021术式成本、M027传媒及M018制度相互引用，不取代各自问题。')
mrev('M014','E376,E379,E380,E382,E384,E387,E389,E391,E392,E393,E395,E396,E399,E400,E401,E402',knowledge)
mrev('M015','E380,E383,E384,E386,E388,E392,E393,E396,E399,E402','年龄越幼潜力越大为无据传闻，土读伪证误认。空间故障与感官代偿是翠借口；女王会来只是可能，小/夏关于其能力纯猜。温泉美容据说、祖17百进制/好感点是玩笑。猫爪妖精义肢和国度任务为墨口径、翠觉得未说谎不自动证真。')
mrev('M017','E389,E392,E394','前置疗程魔溢停、108后丝奇境无痛，繁开起手被制止、稳固需数日至考核；两毁魔装不返，下一献祭风险为特定专业警告。身高再矮2厘米、表情能更自然，能力/身体/心理症状分项变动。')
mrev('M018','E376,E379,E385,E388,E390,E391,E393,E400','物质界港口未成年人需成年同行，魔法车站知少女不等同规则处处一致。播种者随考惯例非明禁，摩可拒返不证违规。银廊开华前3年、国度最低10岁是制度；战争下10岁征入不是常态。国度军少女纪律与普通士兵不同，白牌非主力的战时定位不当永恒通用上限。考试院属魔事/研究共辖、观礼未确认；方亭五月会议因临扬灾转承且绿塔候选。')
mrev('M019','E377,E387,E391,E396,E399,E401,E402','夏体贴策略公开，小帮白外语并容争宠。矢先误会权贵后拒钱接姐妹；110对墨保持边界、111因担忧和真情应邀，不等冷漠或即恢复亲密。父生日从白传小再夏，常往办公室的拼接不等小知领养/男翠；礼物尚未送。')
mrev('M020','E378,E381,E382,E385,E386,E395,E399','国度专列按票/牌权限服务，中转空间非任意传送。界门站台下车步行、湿地同屋四床、墨另屋几百米、隐私随需开启；陵园有身份或牌通行，翠临时从气云糕店得知非提前安排。')
mrev('M021','E383,E385,E386,E398','界桥为普通人/弱掌魔者提供世界适应，直穿可能病变/肉体魔力化；少女走手续通常无此生理需要。无魔区仍有全城互解与建筑术式。生产效率有资源/门槛，不把标准化工具等同人人无限造物。')
mrev('M022','E376,E378,E379,E382,E384,E389,E399,E402','物质界成年真证、入国民治许可/认证牌/准考证、界门祖任务特批、边检登记/手环四层分开；证件形式真实不等内容真实。龙胆作为新人从103起对外使用，旧熟人仍可看脸认。普通人进隐藏站魔力引路怎么满足未解释，不杜撰免门槛。')
mrev('M029','E387,E392,E396','长期少女青春不延寿，110国度成年18左右调整身体、物质界任满10年时调整，少数自愿保幼。翠是意外、墨为何未调未知；伤愈后又矮2cm及少痛能表情均个体阶段，不强改所有人。')
mrev('M033','E377,E401','102小已知白筹备回校，实际帮她补西罗语；白科学/东华语可借看书累积，外语从零。关系正建立、还没真正入学，不将计划已被小知道写成仍对全队保密。')
mrev('M031','E381','苏拍睡中翠的梦境之国爱丽丝照片并获摄影奖，新增专业外兴趣与四人旧旅行记忆；不等其当前间界去向已找到。')
mrev('M016','E383,E394,E395,E396,E399','界桥压迫体验、陵园厌恶战场气味与不能回军礼显示创伤的具体触发，勿纯荣耀英雄或永久无情。治疗后脸更自然不等心理痊愈；旧队称谓对翠为距离调节、对墨情感可能不同，暂不裁决全部。')
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
write('evidence_records.json',ev);write('issue_records.json',issues);write('missing_records.json',missing);write('judgment_changes.json',hist);write('session_13_changes.json',change)


ledger=read('reading_ledger.json');prev=copy.deepcopy(ledger['coverage']);start,end=24908,26741
ranges=[[1,end],[36130,38825]];chars=sum(len(S[n-1]) for lo,hi in ranges for n in range(lo,hi+1));lines=sum(hi-lo+1 for lo,hi in ranges)
assert chars-prev['continuous_semantic_chars']==sum(map(len,S[start-1:end]))
newcards=[104,105,116,122,125,127,130,139,142,144,150];ledger['card_entries_read']=sorted(set(ledger['card_entries_read']+newcards));ledger['card_entries_targeted']=sorted(set(ledger['card_entries_targeted'])-set(ledger['card_entries_read']))
cov=copy.deepcopy(prev);cov.update(continuous_semantic_chars=chars,continuous_semantic_char_percent=round(100*chars/1641637,2),continuous_semantic_lines=lines,continuous_semantic_line_percent=round(100*lines/38825,2),worldbook_full_bodies_read=len(ledger['card_entries_read']))
ledger['coverage']=cov;ledger['source_full_read_ranges']=ranges
session=dict(session='13',previous_next_line=start,new_source_range=[start,end],new_lines=end-start+1,new_chars=chars-prev['continuous_semantic_chars'],next_line=end+1,completed_chapters='卷二第101—114章',note='逐段完整显示后连续语义读；L25195—25199输出截断后专门补显，未留缺口。卡105后半摘要虽完整读，不算原著覆盖。内部健康检查后自动继续。',**{k:v for k,v in change.items() if k not in ['session','evidence_changes','missing_changes']},revised_evidence_ids=[x['id'] for x in change['evidence_changes']],new_full_card_body_ids=newcards,rechecked_full_card_body_ids=[4,6],rechecked_existing_card_sections=[43,47,64,81]);ledger['sessions'].append(session);write('reading_ledger.json',ledger)
nc=next(c for c in chap if c['start_line']==end+1);cp=read('resume_checkpoint.json')
scene='2月14日翠以新常服赴墨荷之约，先替被举报可疑的墨荷向治安官解围，解释她是战争退伍少女、性格或受影响；自承解释未必符合全现状，墨荷却感到仍被队长理解。用餐未开始。'
pending=['下一L26742卷二115《餐厅》；已读L1—26741及独立末段L36130—38825，不重计。','C038/C096/M017：108后宝石修补、丝奇境无痛；毁两魔装不返，繁开仅起手被阻、7/10天稳固保险等开考；再献祭林消失为祖有条件警告。身高再矮2cm，表情自然不等创伤痊愈。','C013/M014/M036：翠109摘面具才认妮娜=墨荷、111确认106熟人。妖精技术义肢和国度任务是墨口径，翠仍不知黑猫全貌；墨先认龙胆旧人不证特殊识破术。110幸福半答、111应约、军礼半抬，114退伍影响解释未必全真。','C005：103摩可合法现职却拒返国，理由未说，随行惯例非明文义务。C066：卡104又把夏已知矢车菊误入全员未知；106她性别变向误解仍未纠。','C090/S009/M022：假号准考证已用、边境实验素材真手续假内容、所有人另有备份；手环仅限无魔区，区内仍有互解术。四床同屋C113，墨另屋几百米。','C009/M038：第三晶尚未完形、天音四韵律双刃、白双偏移仍待后验。C110白祭子已说但父母隐，C111公开妈例外后101/102又收口。','C112：门记录不证传闻，卡4也有升级表述；木原件林记忆转祖。C103：首领称线人已核，三人袭考夺源仍计划，现场翠不全知。','M019/M033：小已知白回校筹备且帮助外语，未入学；113白告小林生日、夏最后知蛋糕/巧克力计划，尚未视频。父手机报平安与翠手机不扰分开。','M018/M039：五月研讨会因临扬灾改方亭、绿塔候选；国度个体经营与术式价值链补新遗漏。其余开放：气源C076、苏间界M031、樱案/田记忆/交割/游戏及爱之源朋友。','已到约72—75%窗口，本批保存后立即健康检查E/C/M/引用/修订/统计/冗余/时间认知/输入哈希，再自动接115；90%再检。卡86/143，手机/HTML未全审、宿主未运行。']
cp.update(next_source_start_line=end+1,next_source_end_hint=nc['end_line'],source_unread_main_range=[end+1,36129],next_source_chapter=nc['volume']+' '+nc['title'].lstrip('# '),last_completed_source_chapter='卷二第114章《碰面》',last_read_line=end,session='13',cumulative_character_coverage=cov['continuous_semantic_char_percent'],cumulative_characters=chars,card_body_unread_ids=sorted(set(cards)-set(ledger['card_entries_read'])),integration_status='内部批次13已保存，72—75%健康检查后立即继续，不等待用户',latest_scene=scene,pending_rechecks=pending);write('resume_checkpoint.json',cp)
pct=f'{cov["continuous_semantic_char_percent"]:.2f}';sev=Counter(x['severity'] for x in issues);ni=len(issues)
nav=f'> 续审13导航：唯一续读断点为 **L26742／卷二第115章《餐厅》**，累计 **{pct}%（{chars}／1641637字符）**。先见[轻量续读索引](CONTINUE_STATE.md)；历轮“本轮／当前／下一／尚未”按其历史时点解释，不能覆盖[现行断点](resume_checkpoint.json)。'
for n in ['00_card_structure.md','01_evidence_index.md','02_full_audit_report.md','03_missing_content.md','04_timeline_knowledge_risks.md','05_user_confirmation_required.md']:
 s=(A/n).read_text('utf-8');s=re.sub(r'^> 续审\d+导航：.*$',lambda m:nav,s,count=1,flags=re.M);mdwrite(n,s)
for n in ['README.md','02_full_audit_report.md']:
 s=(A/n).read_text('utf-8')
 for k,v in sev.items():s=re.sub(r'\|'+re.escape(k)+r'\|\d+\|',f'|{k}|{v}|',s,count=1)
 if n.startswith('02'):s=s.replace('当前135项＝112项C',f'当前{ni}项＝113项C',1).replace('累计记录135项',f'累计记录{ni}项',1).replace('不是135条',f'不是{ni}条',1)
 else:
  s=re.sub(r'^> 续审12已保存.*$',f'> 续审13已保存；自主任务继续。唯一下一断点 **L26742／卷二第115章《餐厅》**，累计 **{pct}%（{chars}／1641637字符）**。先读[CONTINUE_STATE.md](CONTINUE_STATE.md)；72—75%内部健康检查后立即续读。',s,count=1,flags=re.M)
  s=s.replace('累计完整语义阅读75条正文','累计完整语义阅读86条正文',1)
  s=re.sub(r'原著连续语义核验：L1–24907及L36130–38825，共[^。]+。',f'原著连续语义核验：L1–26741及L36130–38825，共{lines}/38825行（{cov["continuous_semantic_line_percent"]:.2f}%；按无换行字符{pct}%，{chars}/1641637字符）。',s,count=1)
  s=s.replace('**135项**',f'**{ni}项**',1).replace('135项Canon',f'{ni}项Canon',1).replace('另列38项','另列39项',1).replace('源文L24908–36129','源文L26742–36129',1).replace('：375组可回查证据','：402组可回查证据',1).replace('：135项工作稿',f'：{ni}项工作稿',1).replace('从现行断点L24908（卷二第101章《离开方亭》）','从现行断点L26742（卷二第115章《餐厅》）',1)
  s+='\n## 续审13｜入国、疗伤、墨荷重逢与节日前夕\n\n'+f'本批L24908—26741（卷二101—114），{end-start+1}行/{session["new_chars"]}字符；累计{pct}%（{chars}/1641637），下一L26742卷二115。新增E376—E402、C113、M039；修订旧问题{len(change["updated_existing_issue_ids"])}项、证据2项、遗漏{len(change["expanded_missing_ids"])}项。世界书11条新读，累计86/143。\n\n重点回接伤愈但毁物不返/需静养的能力状态、假身份制度与NPC知情、墨荷旧队关系和当前掩护、国度生产生活。卡104全员未知沿C066、日期整体早一日沿C021/S003；不为新增量重复建号。L25195—25199输出截断已补显示，不存在未读空洞。达到健康窗口，校验后自动继续115，不因保存或检查停止。\n'
 mdwrite(n,s)
s=(A/'03_missing_content.md').read_text('utf-8').replace('当前为M001—M038共38项','当前为M001—M039共39项',1).replace('L24908—36129','L26742—36129').replace('L24908–36129','L26742–36129');mdwrite('03_missing_content.md',s)
extra={'00_card_structure.md':'新增全文104/105及116/122/125/127/130/139/142/144/150共11条，累计86/143。4/6完整复核，43/47/64/81相关段复核。105后半未来摘要和地理条目的后段不计原著已读。','04_timeline_knowledge_risks.md':knowledge+'\n\n10日出发→11燕南→12界门/湿地→13治疗、报到、陵园、晚电话/采购→14制礼与赴约。108旧梦十五岁矢和姐妹编队属于1979历史，不能驱动当前时钟回退。109与108术后并行，不是隔日。墨荷右手自述、好感年龄玩笑、温泉美容、界桥借口均按证据层区分。证据E376—E402；当前伤愈状态回接C038/C096，知识C005/C013/C043/C066/S010/S011，空间C113、经济M039。','05_user_confirmation_required.md':'仍U001—U008。107好感点数是角色玩笑，不是为卡好感数值Canon背书；17百进制不是可据以确认祖真实年龄。真实治疗与冷链制度属原文，不能因魔法性当IF。卡中未知清理仍应按原著已揭信息，未读后文不预判。'}
for n,body in extra.items():mdwrite(n,(A/n).read_text('utf-8')+'\n## 续审13｜增量与阶段校正\n\n'+body+'\n')
oldnav=(A/'CONTINUE_STATE.md').read_text('utf-8');rules=oldnav[oldnav.index('## 续读规则'):oldnav.index('## 当前场景与开放索引')];footer=oldnav[oldnav.index('## 详细资料职责与读取条件'):].replace('[12补证留痕](session_12_changes.json)','[13补证留痕](session_13_changes.json)')
state=f'''# 续读接管索引｜第一阶段自主连续执行中

导航不替代详细证据与历史。正常完成条件为原著100%后通过最终第一阶段完整性检查；内部批次保存后立即续读，不能等待“继续”。

- **唯一下一断点：L26742／卷二第115章《餐厅》**，章末提示L{nc['end_line']}。
- **累计字符{pct}%＝{chars:,}／1,641,637**；{lines}行。已读L1—26741及独立末段L36130—38825，未贯通。13新增L24908—26741，1834行/{session['new_chars']}字符，卷二101—114。
- **E001—E402、C001—C113、M001—M039**；下一E403/C114/M040。主报告{ni}项＝C113＋有效S18＋R5；S018撤销占位勿用；U001—U008八组。
- 卡正文86/143，余57；手机/HTML未全审、宿主未运行。阶段IN_PROGRESS_NOT_COMPLETE。

'''+rules+'## 当前场景与开放索引\n\n'+scene+'\n\n'+''.join('- '+x+'\n' for x in pending[1:])+'\n**本批维护：** 输出截断的5行已补读；统计/源卡哈希及约72—75%健康结果见report_validation.json。内部检查后立即续读。\n\n'+footer
mdwrite('CONTINUE_STATE.md',state)
v=read('report_validation.json');v.update(issue_count=ni,severity=dict(sev),evidence_count=len(ev),missing_count=len(missing),coverage=cov,next_source_start_line=end+1);v['session_13']={'status':'PENDING_VALIDATION','session':session};write('report_validation.json',v)
print(json.dumps(dict(coverage=cov,next_line=end+1,E=len(ev),C=113,M=len(missing)),ensure_ascii=False))
