"""续审12增量维护脚本；只写audit，源文件只读。执行前拒绝重复批次。"""
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
assert len(ev)==347 and max(int(x['id'][1:]) for x in issues if x['id'].startswith('C'))==109
cards={x['id']:x for x in read('card_entries.json')}
chap=read('chapter_index.json')
change={'session':'12','evidence_changes':[],'missing_changes':[],'new_evidence_ids':[],'new_issue_ids':[],'updated_existing_issue_ids':[],'new_missing_ids':[],'expanded_missing_ids':[]}
hist=read('judgment_changes.json')
def E(start,end,level,finding,quote=None):
 id=f'E{len(ev)+1:03}'; q=quote or next(n for n in range(start,end+1) if S[n-1].strip() and not S[n-1].startswith('#'))
 ev.append(dict(id=id,start=start,end=end,quote_line=q,level=level,finding=finding,session='12'));change['new_evidence_ids'].append(id)
def C(title,severity,kind,card,current,problem,evidence,level,accurate,impact,action):
 id=f'C{max(int(x["id"][1:]) for x in issues if x["id"].startswith("C"))+1:03}'
 issues.append(dict(id=id,title=title,severity=severity,kind=kind,card=card,current=current,problem=problem,evidence=evidence,level=level,accurate=accurate,impact=impact,action=action));change['new_issue_ids'].append(id)
def revise(id,addition,refs,reason,card=None,field='accurate'):
 x=next(x for x in issues if x['id']==id);before=copy.deepcopy(x)
 x[field]+=' 续审12：'+addition;x['evidence']+='；'+refs
 if card:x['card']=list(dict.fromkeys(x['card']+card))
 hist.append(dict(session='12',id=id,reason='2026-09-09；'+reason,before=before,after=copy.deepcopy(x)))
 change['updated_existing_issue_ids'].append(id)
def erevise(id,addition,reason):
 x=next(x for x in ev if x['id']==id);b=copy.deepcopy(x);x['finding']+=' 续审12回接：'+addition
 change['evidence_changes'].append(dict(session='12',record_type='evidence',id=id,reason=reason,before=b,after=copy.deepcopy(x)))
def M(category,title,refs,details,scope):
 id=f'M{len(missing)+1:03}';missing.append(dict(id=id,category=category,title=title,evidence=refs,details=details,scope=scope));change['new_missing_ids'].append(id)
def mrev(id,refs,details):
 x=next(x for x in missing if x['id']==id);b=copy.deepcopy(x);x['details']+=' 续审12：'+details;x['evidence']+=','+refs
 change['missing_changes'].append(dict(session='12',record_type='missing',id=id,reason='2026-09-09；卷二74—89连续新证补充时效与收录边界，旧判断保留并限定历史阶段。',before=b,after=copy.deepcopy(x)));change['expanded_missing_ids'].append(id)


E(23013,23176,'A（归还、问答和承认监视）／D（备用身体功能与比例）','新年首日翠归还兽源。祖说劣化备用身体跟过银屏山战、采集数据并可能救援，不等实际施救；后列柏安与据点私事，承认偷看。温和派不足百分之一为她的估计，并承认研究院不是调查院、不能完整掌握每个成员档案；不扩成无所不知。',23159)
E(23013,23176,'A（新交易、回响交付和替身请求）／D（同盟报价与未来敌袭）','翠探讨深入同盟，祖自称自己的报价也代表猫眼，仍不是猫眼在场承诺。爪痕只作条件性备选、不等翠入伙；回响实际给付。翠要求让林和翠同时现身的装备，90仅见祖惊讶，92才解释成本不行；不杜撰两身份已有独立身体或家庭手续。',23171)
E(23177,23347,'A（假期日常与摩可角色变化）／D（人物感受）','91明确假期第五天、新年第四天。摩可有房却常睡小/夏房，白白日待卧室令其不便；前辈更懂教学、现人手已足，侦兽又为睡着仍有效的天性，它从无力感渐转享闲，不等从来无作用。小为翠早餐早起、白曾因翠要求提前退游戏；白蓟无意提母使小难过后道歉，关系不能只记争执。',23247)
E(23293,23347,'A（89私谈的回叙答复）／D（愿望和承诺）','91回接新年凌晨私谈：翠否认把小当樱替影，小也说独立喜欢翠而非混同安雅。翠唤璐璐、接受拥抱，承认迟早离开、不能保证等退役；若小独当一面可自行跟来，此前可撒娇。答复发生于89夜谈，不是91当日新一次告白；仍不知男身，永久相伴与退役节点未保证。',23333)
E(23348,23484,'A（替身限度、伪宝石交付及手续回述）／D（以后安排）','丝能造有外观触感的空壳，但不能精细动作或说话；翠未用其脱离孩子。祖制完美人偶成本过高，翠因伤也不能自由操纵。假心之宝石已交付，只伪波动而非真供魔/变身；龙胆资料部分将补，代号借研究保留却不在官方抽调名单。一年后让龙胆战死是计划，不是已经死亡或自动失效机制。',23473)
E(23485,23626,'A（考期与魔装现状）／D/C（导师建议和潜力预测）','93明说一月五日，三月三日卢恩诺雷认证、二月十日先出发。夏引离近半月提高反射和传送效率；改镜曲率聚散是建议、未来近免非规则攻击为翠展望，不是当前绝对能力。成长需反复强烈意愿与实训，不是任意许愿即得技能。',23517)
E(23485,23626,'A（天音四韵律、效果及底托变化）／D（训练设计）','天音三个月已掌四韵律：活化肢体、活化魔力、激发斗志、忘我。后两者分别可能无谋并加体魔耗、过度专注而忽略危险，既可强化己也可损敌。底托生握柄、边墨绿并趋锤为白愿望影响；翠拟分离盒与底托以保音乐辅助和近战风格，不是绝对禁近战或已完成所有武器形态。',23550)
E(23577,23626,'A（实际坦白范围和失真记忆）／D（修饰后故事与小的理解）','夏此前已私问确认，小因认母等事隔数日才问。白按翠准备口径明确坦白黑烬祭子、湖畔春天战斗与兽魔，隐去父母身份。白有战时记忆但失真为王道救人；翠修饰故事以维护其人的认同，不是完全失忆，也不能将该故事当客观战斗实况。小据此理解为兽方向偏移，仍未获全貌。',23594)
E(23627,23762,'A（王钥变形实测及自主选择）／C（其它晶石与根源猜测）','小最初不能复现护卫，翠先类比变化类；小提出浊化并实验成功，第二晶石亮、白杖成丝缠长枪。四晶所余两形与安雅继承仅翠私猜。小明确即翠退役也愿继续，因为自己喜欢少女身份；不再只靠依恋解释其职业选择。新年夜翠仅惊鸿一瞥不等全程见证小战斗。',23684)
E(23627,23762,'A（训练安排及任调权已获得的叙述）／D/C（制度方案与二次偏移假说）','翠给三天处理功课、一月九日起特训至二月十日，拟请假到三月中。祖提王庭/魔事院备案唯一残兽偏移者，翠因王庭不信、任调权已拿到及避免异样而拒；不是绝无备案路径。把白安排给玛试双重浊化/二次偏移仅训练假说，未实现。爪痕不属正常参试者且有抓捕义务，未明文禁考不能当合法通行证。',23727)
E(23763,23883,'A（红自学经历、课程和夏反应）／D（方法论与误判）','95才明确红教夏术式数学：红大学非理科、未入研究院，后来自学相关数学物理。她解释魔力不遵物理而外部作用可预测、数学可作工具；并非物理能无条件解释所有魔法。红把夏畏难误看成兴奋，夏勉强同意，未证一月学会全部理论。')
E(23763,23883,'A（丝线练习、家务轮换及争宠）／D（白对关系平等的理解）','小最初丝线实战多次割伤衣皮、险伤翠手，改翻花绳练对称、不死结、快速空间控制；数日能几轮但远未实战熟练。三旧重家务、六新加妖精轻家务轮换。小获撒娇权与白改由玛授课造成注意差异，白避爸爸却认为妈妈应可共有，仍不知男身；95仍记别人面前不能称妈妈。',23865)
E(23884,24060,'A（争执、被捕及局长身份获知）／D（拘捕报告和安全说辞）','96晚餐接95，次晨林男身任职，木潜档案被捕；她此时才知林为局长，先把遭遇猜成阴谋。跨城联系/王庭备案确有程序但通常避免麻烦，林只要求通知队友即可放人；不能把吓唬当已完成全部上报。章末止于问其私事，登王之门回答在97回述。',23991)
E(23939,23966,'A（黑烬清理范围与故意保留暗子）','黑烬明暗势力已清理，烬卫以上一个不留，但庭前烬及军前烬仍故意留几个暗子钓鱼。不能把清剿概括为全员物理清零，也不能把残留理解为局长完全不知。林正常男身办公再次否定永久不能解除变身。',23950)
E(24061,24246,'A（绿塔地理、档案关联与同行）／D（传闻及木经费来源）','绿塔1005米197层、下层商业办公、上层观光，顶层不向游客开放但局通行卡可入；同名体育场在远郊。木经费来自网络多跳关系所称大妖精、不是本人亲证权威。林学生时已听门传闻，局档案只见工程涉及门字；起因、位置、所谓王均未知，陪行有局长临时跨城联络权与私人好奇两面。',24133)
E(24165,24226,'A（自动书记物证、年份及持有变化）／F（门关联和含义）','顶层微魔来自维持平衡的温和结界，不等已失效纸回路仍运作。自动书记为国度廉价按指令记录用品：1955/56全零、1963波1共1、1964波0共1、1978震1共1、1979震0共1，止于1980。林记住后把原件给木，当时未解含义；记录确有，是否登王之门证据仍须98明确区分。',24194)
E(24227,24246,'A（木态度变化和正式道歉）／C（她的私下猜测）','林让木保留邂逅，词与翠的表达相似令木产生跟踪/关心等猜想，不是识破同一人。她感谢两次帮助并正式为误会道歉；该态度变化不能提前回填卷一刚相识期。')
E(24247,24282,'A（当天再议、承认未知与额外调查）／D（祖否认参与）／C（年代关联）','98当天下午接97登塔。祖说自己、研究院及相关朋友没有研究门，承认不是所有传闻都管。双方明确记录只能证明旧日有人调查东西，不能确认与登王之门有关；年代近安雅契约只促怀疑。祖接受调查资源流动不加价，不是新收一次研究费。',24266)
E(24283,24336,'A（假衣装录入与实际使用）／D（防护强度及未来活动要求）','假宝石此时录入蓝紫东华旗袍、挽髻发簪耳饰绣鞋等衣装，变身后秘密启动覆盖；脸身高体型不改。祖称防护稍强未经独立实战核验。可再录常服但此场没选好；须以龙胆在方亭留下活动痕迹是后续要求。不是已获真正第二本相或当场完成所有合法档案。',24306)
E(24337,24364,'A（照片、同伴反应与离开计划）','归据点新衣被拍后，柏安三人此时此前不见踪影、随后才上楼，不能写全员同步见证拍照。木有线索后与白蓟和解、接受下周离开；小提月底庙会送别，尚非98已举行或已有精确月日。',24348)
E(24365,24502,'A（同日课程、扶救与晶石波动）／C（王钥成长解释）','99夜承98当日照片。夏学习困难、翠给予碰拳安慰；小倒走楼梯摔时尚未变身，翠及时救。王钥一周本体未变、第三晶石有微弱波动，翠据此认为练习孵化新形态；先提出不适当教学/半成品两可能，不是最初已全知。小当前不知道安雅魔装战法，翠将来如何解释仍未定；并未觉醒第三形态。',24475)
E(24503,24603,'A（白夜访及玛告知风险的传播）／D（自我担心与保护承诺）','翠课后公务至午夜约一点睡，白因换导师缺相处而请求同睡；怕挤得翠难受先等其睡才靠近，翠接纳并放其头上肩。白明确风险是玛告诉的：考场可能被当爪痕/残兽；翠承诺自己在场、不让坏结局发生，不等外界必理解或未来安全已证明。妈妈称谓是既有关系强化，不是99才首次形成。',24567)
E(24604,24678,'A（100现场披露）／D（玛转述木家史与寄养谎言）','100庙会玛才向翠讲：木父母未婚乐队分手，父带娃后弃琴行，悔信以仍欠账吉他抵抚养费。老店主因身体退休、女儿灯盏经营，夫妇收养木故名义为灯盏妹妹；她仍信寄养后父会回。卡60已有大部核心身世，不称整项全缺；不添已见法律收养文书。玛复述谎言问题促翠反思，不能前移92或给木本人真相。',24668)
E(24712,24748,'A（公开地点的称呼与相处）','100公共小吃广场白两次自然称妈妈，翠接受汤圆和喂食、未纠正称谓。与95仍述只准私下的约定并存，说明角色约定不能被卡当作永不破例的公开场景硬禁；不据此宣布所有人知领养/父亲身份、也不开放兽子秘密。各旁观者逐渐到场不等都听到先前两句。',24717)
E(24604,24792,'A（庙会、地点与实际活动）／D（地方传说及许愿信仰）','檀香山为市内几十米土丘、白老庙传说纪念免费行医白姓医师；一月末庙会含舞龙、灯谜、套圈、灯展，摩可主持跨城相关活动有其播种者职责。翠刻意不显超常身体够不着谜条，非魔法身跳跃能力丧失。愿望不说的风俗不是神效规则，也未逐人披露所有愿望。',24776)
E(24793,24824,'A（物质界地貌、聚落与居民来源）／D（村民对庇护者理解）','远古变故造成海退地移与荒原，城市依国度防护；城堡周边草原村落却稳定有人。居民包括债务、犯罪、权贵冲突、事故、绝望及冒险者，不能统一写无辜难民或荒原绝无人。村民以为主人善良魔法少女是其认识，不等全知爪痕目的。卡124/149已有聚落与来源主干。')
E(24825,24885,'A（成员日常外观、照护和餐桌权序）／D/E（玩笑与互相评价）','褐鹈为有肉丰满而非胖的棕卷发少女，偷塞米种橘又拿锅威胁煮它，未实际吃妖精；金蛇长金双尾辫、烟管和补觉。黑猫学生服马尾金竖瞳，塞米称小荷并被其搂护；首领温和训互相欺负，与此前冷酷命令共存。鸢此刻有眼罩，但未交代具体何时如何伤眼；懒、投敌等嘲讽不当客观阵营变化。',24854)
E(24886,24907,'A（首领宣告、分工和计划）／D（线人核实口径及推测）','白狼称线人已考证兽源确在祖手、数日前秘密运至卢恩诺雷实验室；由69暂按真处理推进到自称核实，但转运未在本幕直接展示。她预计长期不移、不会告女王，拒向王庭泄露。黑猫点自己、褐鹈、金蛇，拟袭考场分流安保后抢兽源，尚未出发或成功；消息当场给在座成员，不全组织瞬时共享。',24890)
assert ev[-1]['id']=='E375'
C('将白静萱已坦白的祭子身份错误列为隐瞒项','MAJOR','认知范围／卡内矛盾',[17,103],'卡103第93章称只坦白残兽方向偏移、隐去祭子与父母真相；卡17另写小璐夏凉后来知道祭子层面。','源L23594明确已说黑烬祭子、湖畔战斗、残兽魔力，隐去的是父母身份。摘要把有限真相进一步删掉，且与人物卡自相矛盾。','E355','A（坦白范围）／D（修饰后的战斗故事）','夏先私问，小隔数日当众问；小夏知道祭子称谓与兽方向偏移，未知父母、人造细节。并非全队全社会得知。','RP会让小夏重复首次震惊、误判白还在隐瞒已告诉的内容。','后续按人物与时间修复知情边，不改成全盘公开。')
C('把私下称妈妈的约定绝对化为公开场景永不发生','MODERATE','关系状态／约束过强',[17,103],'卡17语言、当前关系及扮演约束把公开称妈妈列为禁止；卡103庙会省略实际称呼。','95有私下限制，但100在公共小吃广场白两次称妈妈，翠未纠正。卡将阶段约定写成覆盖后文真实行为的硬规则。','E359、E369、E371','A','保留早期约定及后文公共场景例外；例外不等正式解除约定，更不等周围人人知完整收养关系或林翠身份。','会阻止真实日常互动，或反向把例外扩大为全社会知情。','用阶段默认和已发生例外管理称呼；兽子保密另行控制。')
C('将绿塔未知门记录写成登王之门传闻得到物证','MODERATE','推断升级／摘要内冲突',[60,103],'卡103第97章称都市传言第一次获得物证，第98章与卡60又承认门是否真实未知。','物证是自动书记本身，不能确认其研究对象就是传闻之门；98明确把这种联系保留未知。所谓物证若不说明证明对象会升级结论。','E362、E363、E365','A（记录存在）／C（两者关联）／F（传闻真实性）','旧日有人研究某对象有实物记录；是否登王之门、与安雅的因果均未确认。年份相近只能提示后查。','NPC会据摘要宣布已找到传闻入口或提前认定安雅关联。','限定物证证明对象，保留卡60正确未知边界及未来补证入口。')
revise('C006','91回叙补全89认母答复：翠否认樱替影、承认迟早离开而许成熟后可跟来和此前可撒娇。94小又明确即翠退役仍因自己喜欢而继续；95新争宠表明承诺并未消除关怀分配矛盾。','E351、E356、E359','89答复未读已被后文填补，关系与独立动机有新证。')
revise('C009','94护卫复现需浊化实测，余晶及安雅继承仅翠猜；99第三晶微波支持正在孵化的解释，但未完成新形态，小仍不知道母亲魔装。魔装训练未见外形变化不等无进展。','E356、E368','能力逐阶段补充，保留尚未知根源，防旁白倒灌。')
revise('C021','91当下为新年第4天，认母答复回叙89夜；92并无木父故事，实际100才向翠讲。93课堂真坦白祭子另C110，94安排白训练、95才叙红教学；96末只问木目的，97才回叙门答案。97登塔→98当日下午衣装→99同日夜课不可拆成1月15/20/28三日。庙会只锚一月末，幕间只以上月任务失败作相对关系，不擅造日号。','E350、E351、E355、E357、E358、E360、E362、E365—E370、E372、E375','按实际事件和叙述位置拆开，修正本批卡103跨章与跨日混写。',[103])
revise('S003','91假期第5/新年第4天，不是卡1031月3；97/98/99当日连续不能被卡指定15/20/28号分离。93明确1月5、1月9训练、2月10出发和3月3考试可保留，源92上午接91、93午后却换日的张力另R005。','E350、E353、E357、E365、E368、E372','补直接日期和相对关系，不统一抹成所有日期都无据。',[103])
revise('C035','93揭天音四韵律及副作用（M038），翠拆盒/底托是避免整个魔装变纯锤并保留近战意愿，不能只解释为阻自残。白记得湖畔战但失真、翠修饰口径，不把主观救人故事替客观残虐。','E354、E355','能力发展和叙事认知补全，仍无按次扣本相的证明。',[17,103])
revise('C069','96再次男身日常办公。99说被迫维持变身须解释当期频繁失控和工作相处情境，不能据一句取消已展示的主动解除能力。','E360、E361、E368','新实际男身再次反证永久单向概括。')
revise('C087','92玛愿做东瀛午餐、久违无助理生活而放松，同时仍不喜束缚；翠清楚二人只适合挚友。95争宠建议并非专业，96让后辈自己解争执，100仍会教训木，并借她家事反问谎言保护。不得固化成永不干预或永远准确读心。','E352、E359、E360、E370','关系与教育方式多面性新证，不升级成互选恋爱或冷漠。')
revise('C090','90谈深入盟约、祖自称猫眼同价；92假宝石已给、登记还有待办，一年后龙胆战死仍方案，98衣装才录入。新衣照片的看见不等孩子已听疗伤、伪证、政治交换；柏安三人还晚到，不能以全员拍照同步机密。','E349、E352、E366、E367','合作从提议到分项落实，逐件分开已做与计划。',[103])
revise('C103','90兽源实际归祖；午餐幕间白狼自称经线人考证且数日前转运卢恩诺雷，知情口径已由69暂按真推进到自称确认，原69判断仍成立于当时。转运是其报告D，长期不移/不告女王是预测；黑猫三人抢夺只是新命令，未执行完成。','E348、E375','后文提供核实链及新持有地点报告，修正永久未核实的潜在残留。',[103])
revise('C056','96木在局长室才知道林的职位，97才正式道歉并认好人大叔，不能前移卷一相识阶段。100玛叙琴行夫妇收养与灯盏名义妹妹，木只认寄养；未展示具体法律登记，不从正式收养措辞外推手续。','E360、E364、E370','新日常与认知核验收窄阶段调用。',[60,103])
revise('R005','91新年第4天、92同日上午、93称午餐后却明确一月五日，保留日历转场张力，不以卡日期强行调和。100公共妈妈与95私下约定记实际例外，尚不足判源必然自相矛盾。幕间鸢眼罩原因未叙，亦不擅补银屏山某一招致伤。','E350—E353、E359、E371、E374','保留源文本身时序松动及未说明细节，不伪造唯一解释。')
knowledge='90祖承认旁观私事，仍自认档案不全；91回叙认母答复没有男身坦白。93夏已先私问、小此时才获祭子/战斗/兽魔，父母身份仍隐，战斗故事经过失真记忆和翠修饰。96木才知林局长、97道歉未识男翠；97原件给木林留记忆，98翠即告祖，私下保密约定不等信息永不传播。98新衣被拍时柏安三人晚到；99白由玛获考试风险、小尚不知安雅魔装。100翠才从玛知木父实情，木未知；公共妈称呼不等公开领养。午餐白狼称线人核实再向餐桌传新地点，其他成员不自动全知。'
revise('S010',knowledge,'E348—E375','本批逐人追踪实际获知节点，已说部分从未知移出但不外扩。',[103,60,17])
revise('S011','护卫启动经失败再试浊化、第三形态仍孵化；门记录存在与传闻有无分开。红把夏畏难误看兴奋、白记忆失真、木以气压耳痛联想到门排斥，均不能当客观机制。白狼转运消息为已核实的自述，未来安保判断仍预测。','E353—E356、E358、E362、E365、E368、E375','补认知阈值、失败试验与观察者错误，不升级推断。',[103])
erevise('E345','91回叙已补认母答复（E351）：拒替影、迟早离开、成熟可跟来、此前可撒娇；89当章未展开是历史叙述边界，不是当前仍无答复。','后文迟到解释解除旧待查。')
erevise('E305','午餐幕间自称经线人考证并报数日前转运（E375），由69暂按真进一步到首领称已核实；不倒推69当时已核实。','保留分期认知而修正当前开放口径。')
erevise('E341','93小获祭子、湖畔战和兽魔，父母身份隐，夏更早私问（E355）；87有限回答后来已补充，不再说小始终不知祭子。','新信息实际传播，但并非全部身世公开。')
M('能力','天音四韵律的双向效果、副作用与拆分成长','E354,E355,E357','除活化肢体/魔力，还有激发斗志与忘我：战意过深会无谋并加耗，专注过深会忽危险。这使辅助也可能对敌施负面，而不是纯恢复。底托握柄墨绿到锤的变化受白意愿影响，盒与底托分离为保辅助兼近战的教学方案；二次偏移尚为训练假说。','卡17及103已写八音盒、两种活化、拆底托，故不是天音名字缺失；遗漏新增韵律及条件对决策的影响。个体病因仍M023，不合并成同一治疗代价。')
mrev('M009','E348,E349,E365,E375','兽源归还、祖承认监视和知识不足并存。额外调查门资料不加费，政治报价代表猫眼仍祖口径；敌方报告兽源转运实验室非两组织已合作，金蛇只说近期未听利益交易。')
mrev('M014','E348,E351,E355,E360,E363,E365,E367,E368,E369,E370,E371,E375',knowledge)
mrev('M015','E353,E354,E355,E356,E358,E362,E365,E368,E375','王钥启动实验成功可确认当次条件，第三晶波动未等形态完成；翠猜安雅继承不给小。祖明确纸记录不证门，白狼报告核实不等读者亲见转运；她的未来预测仍D。')
mrev('M017','E353,E354,E356,E357,E358,E359,E368','夏反射/传送效率已提升，曲面聚散及花级预测仍未来。小丝线先失控险伤翠改翻花绳，数日能几轮不是熟练战法；王钥实际浊化开护卫，第三晶在孵化。白双浊化方案未完成；天音新增具体机制另M038。')
mrev('M018','E350,E357,E360,E361,E372','任调权94叙述已拿到，白备案有路径但翠拒。跨城失序少女可备案也常简处，林要通知队友即可放木；不是全部程序实际启动。黑烬高层清空仍故留低阶暗子钓鱼，摩可睡时侦兽天性与跨城庙会职责并存。')
mrev('M019','E351,E356,E359,E369,E370,E371','89认母答复由91回叙补全；小94说即前辈退役仍继续，95竞争因撒娇许可与授课分工发展。白99担心挤睡并听保护承诺，100公共称妈形成实际例外，不倒改95约定。木父寄养谎言100才讲翠，不能当木知道；卡60主干已收录，重点保留多方认知。')
mrev('M020','E362,E363,E364,E365,E372','补绿塔高度楼层、顶层封闭及局卡通行、同名体育场远郊，记录纸失效与结界微魔不是一个装置。檀香山城内土丘与银屏山不同；白老庙公共小吃/灯谜场中超常能力选择不用不等不能。门传闻关联保持未知。')
mrev('M022','E349,E352,E366,E367','丝线空壳不精细动作/说话，完美人偶预算不够；假宝石伪波动不供魔，龙胆不在官方抽调名单却借项目保号。92交宝石、98录衣装、常服待选、活动痕迹待做、一年战死是预案；外貌身体未改，不能等同独立身份真实生理。')
mrev('M023','E354,E355,E357,E369','小夏后来明确知道祭子称谓但父母隐；白战斗记忆非无而失真，保护人认同不等实际战况改写。玛实际告诉白国度风险节点在99回述；备案被拒与二次偏移实验仍须跟后文，不提前实现。')
mrev('M026','E358,E359','红非理科大学也未研究院进修，靠自学数学物理发展术式；解释外部物理模型的适用边界。她误读夏情绪显示教学能力仍有局限，不是全知导师；据点家务轮换不能全归一人。')
mrev('M027','E350,E352,E372','新年节目提前十二月录播、流向各城市的传统；鞭炮驱兽旧习经研究会刺激地下残兽而式微，不等所有烟花禁绝。庙会祈愿与免费医师地方传说按民俗/人物说法记录，不变客观神迹。')
mrev('M030','E352,E359,E360,E370','玛能做午餐且享无助理自理，仍喜欢自由；让柏安后辈自己解决争执不等放弃监护，庙会仍会敲木头教训。借木家史反问翠保护谎言，不替其断言唯一动机或所有建议专业。')
mrev('M036','E373,E374','物质界荒原聚落与早先间界故乡分开，来源异质而村民不知主人真组织；塞米种橘、黑猫餐桌搂护与首领家人说辞进一步展生活共同体，同时保留内部欺负和袭考场计划。卡124/149已有聚落主干，不再另建重复遗漏。')
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
write('evidence_records.json',ev);write('issue_records.json',issues);write('missing_records.json',missing);write('judgment_changes.json',hist);write('session_12_changes.json',change)


ledger=read('reading_ledger.json');prev=copy.deepcopy(ledger['coverage']);start,end=23013,24907
ranges=[[1,end],[36130,38825]];chars=sum(len(S[n-1]) for lo,hi in ranges for n in range(lo,hi+1));lines=sum(hi-lo+1 for lo,hi in ranges)
assert chars-prev['continuous_semantic_chars']==sum(map(len,S[start-1:end]))==83004
newcards=[118,124,140,149];ledger['card_entries_read']=sorted(set(ledger['card_entries_read']+newcards));ledger['card_entries_targeted']=sorted(set(ledger['card_entries_targeted']+[29])-set(ledger['card_entries_read']))
cov=copy.deepcopy(prev);cov.update(continuous_semantic_chars=chars,continuous_semantic_char_percent=round(100*chars/1641637,2),continuous_semantic_lines=lines,continuous_semantic_line_percent=round(100*lines/38825,2),worldbook_full_bodies_read=len(ledger['card_entries_read']))
ledger['coverage']=cov;ledger['source_full_read_ranges']=ranges
session=dict(session='12',previous_next_line=start,new_source_range=[start,end],new_lines=end-start+1,new_chars=chars-prev['continuous_semantic_chars'],next_line=end+1,completed_chapters='卷二第90—100章及幕间《爪痕的午餐》',note='连续全文显示后语义阅读，未以卡摘要代替；内部批次保存后立即继续。卡118/124/140/149全文新读。',**{k:v for k,v in change.items() if k not in ['session','evidence_changes','missing_changes']},revised_evidence_ids=[x['id'] for x in change['evidence_changes']],new_full_card_body_ids=newcards,rechecked_full_card_body_ids=[17,60,89],rechecked_existing_card_sections=[29,47,66,70,103])
ledger['sessions'].append(session);write('reading_ledger.json',ledger)
nc=next(c for c in chap if c['start_line']==end+1);cp=read('resume_checkpoint.json')
scene='庙会送别后接爪痕午餐幕间；白狼称线人已核兽源并转运卢恩诺雷，黑猫令自己/褐鹈/金蛇声东击西袭考场夺兽源，尚未执行。'
pending=['下一L24908卷二101《离开方亭》；已读L1—24907及独立末段L36130—38825，不重计。', 'C110/M014：白93已向小坦白祭子、湖畔战和兽魔，夏更早私问；父母身份仍隐，失真记忆和翠修饰口径不等战斗客观真相。', 'C006/M019：91回叙补89认母承诺，小不知男身；94即翠退役仍愿继续。95私下妈约定、100公共两次称妈并存C111，不等全面公开关系。', 'C009/M017/M038：94浊化开护卫、99第三晶微波但形态未完成；翠猜安雅继承，小尚不知母魔装。天音四韵律含双刃副作用，白二次偏移只是计划。', 'C090/M022：假宝石已交、98衣装已录；不能供魔、脸身不改，常服待选/活动待做/一年战死预案。孩子看照片不等知假身份或疗伤，柏安三人晚到。', 'C112/M020：绿塔纸真有旧记录，祖明确无法确认关联登王之门；安雅年份相近仅猜。木保原件、林记信息转告祖，木未识林翠也不知父亲遗弃。', 'C103/M009：90源归祖；午餐白狼称线人核实转运，其动机/不转移预测仍D，黑猫三人计划尚未执行。勿给所有敌我NPC全知。', '旧开放：C076气源/奇境、C096病因、苏去向M031、田记忆/妮妮交割/樱案/宝石游戏来源、M033返校计划；均按后文回接。', '当前卡全文75/143、余68；手机/HTML未全审、宿主未运行。任务须继续至全文100%及最终检查，约72—75%和90%自动健康检查。']
cp.update(next_source_start_line=end+1,next_source_end_hint=nc['end_line'],source_unread_main_range=[end+1,36129],next_source_chapter=nc['volume']+' '+nc['title'].lstrip('# '),last_completed_source_chapter='卷二幕间《爪痕的午餐》',last_read_line=end,session='12',cumulative_character_coverage=cov['continuous_semantic_char_percent'],cumulative_characters=chars,card_body_unread_ids=sorted(set(cards)-set(ledger['card_entries_read'])),integration_status='内部批次12已保存，继续自主执行至100%并最终完整性检查',latest_scene=scene,pending_rechecks=pending);write('resume_checkpoint.json',cp)
pct=f'{cov["continuous_semantic_char_percent"]:.2f}';sev=Counter(x['severity'] for x in issues);ni=len(issues)
nav=f'> 续审12导航：唯一续读断点为 **L24908／卷二第101章《离开方亭》**，累计 **{pct}%（{chars}／1641637字符）**。先见[轻量续读索引](CONTINUE_STATE.md)；历轮“本轮／当前／下一／尚未”按其历史时点解释，不能覆盖[现行断点](resume_checkpoint.json)。'
for n in ['00_card_structure.md','01_evidence_index.md','02_full_audit_report.md','03_missing_content.md','04_timeline_knowledge_risks.md','05_user_confirmation_required.md']:
 s=(A/n).read_text('utf-8');s=re.sub(r'^> 续审\d+导航：.*$',lambda m:nav,s,count=1,flags=re.M);mdwrite(n,s)
for n in ['README.md','02_full_audit_report.md']:
 s=(A/n).read_text('utf-8')
 for k,v in sev.items():s=re.sub(r'\|'+re.escape(k)+r'\|\d+\|',f'|{k}|{v}|',s,count=1)
 if n.startswith('02'):s=s.replace('当前132项＝109项C',f'当前{ni}项＝112项C',1).replace('累计记录132项',f'累计记录{ni}项',1).replace('不是132条',f'不是{ni}条',1)
 else:
  s=re.sub(r'^> 续审11已保存.*$',f'> 续审12已保存；自主连续任务仍在执行。唯一下一断点 **L24908／卷二第101章《离开方亭》**，累计 **{pct}%（{chars}／1641637字符）**。先读[CONTINUE_STATE.md](CONTINUE_STATE.md)；中期维护47.67%仍为历史快照。',s,count=1,flags=re.M)
  s=s.replace('累计完整语义阅读71条正文','累计完整语义阅读75条正文',1).replace('L1–23012及L36130–38825，共25708/38825行（66.22%；按无换行字符63.14%，1036517/1641637字符）',f'L1–24907及L36130–38825，共{lines}/38825行（{cov["continuous_semantic_line_percent"]:.2f}%；按无换行字符{pct}%，{chars}/1641637字符）',1)
  s=s.replace('**132项**',f'**{ni}项**',1).replace('132项Canon',f'{ni}项Canon',1).replace('另列37项','另列38项',1).replace('源文L23013–36129','源文L24908–36129',1).replace('：347组可回查证据','：375组可回查证据',1).replace('：132项工作稿',f'：{ni}项工作稿',1)
  s=s.replace('从源文L17121（卷二第41章《归家》）开始按卷逐章连续读取','从现行断点L24908（卷二第101章《离开方亭》）开始按卷逐章连续读取',1).replace('而非只验证现有105项','而非只验证已有问题',1)
  s+='\n## 续审12｜归还、成长课程、门记录与赴国前夕\n\n'+f'本批L23013—24907，卷二90—100及午餐幕间，1895行/83004字符；累计{pct}%（{chars}/1641637），下一L24908卷二101。新增E348—E375、C110—C112、M038；修订旧问题{len(change["updated_existing_issue_ids"])}项、证据3项、遗漏{len(change["expanded_missing_ids"])}项。四条城市/荒原世界书全文新增，累计75/143。\n\n白已坦白祭子、公开妈称例外、门物证的证明边界已修；认母答复回接89、白狼自称线人核实回接69，衣装/伪证/第三形态分开计划与完成。卡60已收录木身世、124/149已收聚落主干，不为新增量重复建遗漏。天音四韵律补M038。README后续优先级残留L17121/105项已作为纯导航错误修正，历史批次不改。完整before/after见judgment_changes.json及session_12_changes.json。保存后立即继续，72—75%健康检查尚未触发。\n'
 mdwrite(n,s)
s=(A/'03_missing_content.md').read_text('utf-8').replace('当前为M001—M037共37项','当前为M001—M038共38项',1).replace('L23013—36129','L24908—36129').replace('L23013–36129','L24908–36129');mdwrite('03_missing_content.md',s)
extra={'00_card_structure.md':'卡118/124/140/149全文新读，累计75/143；17/60/89全文复核，29/47/66/70/103按对应段核验。城市和城堡主干已有收录，不把局部摘要遗漏扩大到整卡无内容。手机/HTML未全审、宿主未运行。','04_timeline_knowledge_risks.md':knowledge+'\n\n时间：91新年第4天，回叙89答复；92同上午、93午后却1月5的源张力归R005。97/98/99同日，100才讲木父故事。1月9—2月10训练、3月3考试有直接日期，月底庙会无精确日号。王钥失败→浊化试成，第三晶微波未完形；门实物不证传闻；白狼已核实是自述，长期不移仍预测。证据E348—E375与C110—C112、相关旧C/S/R/M的完整改判见judgment_changes.json。','05_user_confirmation_required.md':'U001—U008仍八组。C110—C112为披露、称呼例外与推断等级修正，不需要用户替Canon投票；如有意采用祭子仍保密或公开妈妈永禁的IF，可未来纳既有U范围。木父故事归100、衣装和第三形态阶段有原文，不因重复摘要就称整段IF。保留既有用户边界，本自主任务不插入裁决等待。'}
for n,body in extra.items():mdwrite(n,(A/n).read_text('utf-8')+'\n## 续审12｜增量与阶段校正\n\n'+body+'\n')
oldnav=(A/'CONTINUE_STATE.md').read_text('utf-8');rules=oldnav[oldnav.index('## 续读规则'):oldnav.index('## 当前场景与开放索引')];footer=oldnav[oldnav.index('## 详细资料职责与读取条件'):].replace('[11补证留痕](session_11_changes.json)','[12补证留痕](session_12_changes.json)')
state=f'''# 续读接管索引｜第一阶段自主连续执行中

导航不替代详细证据与历史。正常完成条件为原著100%后通过最终第一阶段完整性检查；内部批次保存后立即续读，不能等待“继续”。

- **唯一下一断点：L24908／卷二第101章《离开方亭》**，章末提示L{nc['end_line']}。
- **累计字符{pct}%＝{chars:,}／1,641,637**；{lines}行。已读L1—24907及独立末段L36130—38825，未贯通。12新增L23013—24907，1895行/83004字符，卷二90—100及午餐幕间。
- **E001—E375、C001—C112、M001—M038**；下一E376/C113/M039。主报告{ni}项＝C112＋有效S18＋R5，S018撤销占位勿用；U001—U008八组。
- 卡正文75/143，余68；本批118/124/140/149全文新读，手机/HTML未全审、宿主未运行。阶段IN_PROGRESS_NOT_COMPLETE。

'''+rules+'## 当前场景与开放索引\n\n'+scene+'\n\n'+''.join('- '+x+'\n' for x in pending[1:])+'\n**本批维护：** README后续优先级旧L17121/105项修为现行导航并保留说明；源/卡与引用校验结果见report_validation.json。没有阶段完成或提前停止。\n\n'+footer
mdwrite('CONTINUE_STATE.md',state)
v=read('report_validation.json');v.update(issue_count=ni,severity=dict(sev),evidence_count=len(ev),missing_count=len(missing),coverage=cov,next_source_start_line=end+1);v['session_12']={'status':'PENDING_VALIDATION','session':session,'maintenance_notes':['README未标历史的优先级L17121/105项残留改为现行导航，保留修订说明。']};write('report_validation.json',v)
print(json.dumps(dict(coverage=cov,next_line=end+1,E=len(ev),C=112,M=len(missing)),ensure_ascii=False))
