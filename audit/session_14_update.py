"""续审14增量维护脚本；只写audit，源文件只读。执行前拒绝重复批次。"""
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
assert len(ev)==402 and max(int(x['id'][1:]) for x in issues if x['id'].startswith('C'))==113
cards={x['id']:x for x in read('card_entries.json')}
chap=read('chapter_index.json')
change={'session':'14','evidence_changes':[],'missing_changes':[],'new_evidence_ids':[],'new_issue_ids':[],'updated_existing_issue_ids':[],'new_missing_ids':[],'expanded_missing_ids':[]}
hist=read('judgment_changes.json')
def E(start,end,level,finding,quote=None):
 id=f'E{len(ev)+1:03}'; q=quote or next(n for n in range(start,end+1) if S[n-1].strip() and not S[n-1].startswith('#'))
 ev.append(dict(id=id,start=start,end=end,quote_line=q,level=level,finding=finding,session='14'));change['new_evidence_ids'].append(id)
def C(title,severity,kind,card,current,problem,evidence,level,accurate,impact,action):
 id=f'C{max(int(x["id"][1:]) for x in issues if x["id"].startswith("C"))+1:03}'
 issues.append(dict(id=id,title=title,severity=severity,kind=kind,card=card,current=current,problem=problem,evidence=evidence,level=level,accurate=accurate,impact=impact,action=action));change['new_issue_ids'].append(id)
def revise(id,addition,refs,reason,card=None,field='accurate'):
 x=next(x for x in issues if x['id']==id);before=copy.deepcopy(x)
 x[field]+=' 续审14：'+addition;x['evidence']+='；'+refs
 if card:x['card']=list(dict.fromkeys(x['card']+card))
 hist.append(dict(session='14',id=id,reason='2026-09-09；'+reason,before=before,after=copy.deepcopy(x)))
 change['updated_existing_issue_ids'].append(id)
def erevise(id,addition,reason):
 x=next(x for x in ev if x['id']==id);b=copy.deepcopy(x);x['finding']+=' 续审14回接：'+addition
 change['evidence_changes'].append(dict(session='14',record_type='evidence',id=id,reason=reason,before=b,after=copy.deepcopy(x)))
def M(category,title,refs,details,scope):
 id=f'M{len(missing)+1:03}';missing.append(dict(id=id,category=category,title=title,evidence=refs,details=details,scope=scope));change['new_missing_ids'].append(id)
def mrev(id,refs,details):
 x=next(x for x in missing if x['id']==id);b=copy.deepcopy(x);x['details']+=' 续审14：'+details;x['evidence']+=','+refs
 change['missing_changes'].append(dict(session='14',record_type='missing',id=id,reason='2026-09-09；卷二115—137连续新证补充时效与收录边界，旧判断保留并限定历史阶段。',before=b,after=copy.deepcopy(x)));change['expanded_missing_ids'].append(id)




E(26742,26805,'A（购物、现场行为）／D（用途解释）／C（翠判断）','115翠只识墨部分特质而非看透；双方提前累计留两小时购物，墨认真比价批购发电机、建材/水管/农具，称经物质界城市运荒原缺水电朋友，刻意隐去身份，翠不追。餐厅算需37面包回本而不是已吃37，实际吃三并继续吃/打包。高档礼仪不熟不是一般生活全不能自理。',26757)
E(26806,26879,'A（礼制介绍及用餐动作）／D（墨的往事类比）／F（交换含义）','王庭贵族迎合女王甜味形成礼仪，但女王未要求效仿，社会阶层标记非强制法令。墨用黄油果酱刀压碎慕斯；翠教霜叶冷却、坚果微震等五专刀，取碎糕给自己、分好半块给墨。墨联想翠离开时交换尚未说全。翠未看电话人先离席；墨以炎页戳冷藏球损球断刀后装无事，不是敌袭。',26823)
E(26882,26910,'A（局务安排、田实绩和告白）','117林手机接红电话：建设局郊区项目有兽踪未见兽，特战部驻守，七日不见即要求项目停工、异策局改观察；精英田半日值守留时间讨低兽，玛已担几乎全城防。田现有数次单杀卵兽实绩。红公事后祝生日情人节并说心里全是你即挂断，翠稍心动后调节，非已经答应恋爱。',26891)
E(26911,27003,'A（两人实际行为与语义分歧）／D（幸福观）','翠误以墨一直等未动冷藏球，不知刚才破坏；墨想时光机仅自语，不是确有可用时机。少女食物分魔、此甜量无不良；翠补全幸福半答，失去一部分仍珍惜现有，不叫彻底不幸。墨反对残缺幸福，称讨论中自己得结论；翠尊重差异但说不懂复杂幸福，非全同意她后续手段。芭菲倒后翠因无魔区改手接，未能阻全部泼洒。',26939)
E(27004,27074,'A（支付和对话发生）／D（流放内幕、来源和归责）','餐费1170、损件加至1740，餐厅补偿后1590；券七年前发、过期三年，翠实垫1000并留车费。墨停车场说流放因拒任令王庭失面，翠认保密流放消息但提醒可能有别错；墨称先高层/播种者打听、15或16年前向樱核实且被告翠不见国度旧人。未把墨绝对无错评价升级完整流放因果。',27053)
E(27076,27111,'A（招揽、翠的复仇意向变化）／D（墨情报及技术承诺）','伤愈与女儿走正轨后翠开始考虑复仇预案，未即抛家追凶；墨称不知樱凶手，愿未来协助。墨说军团长教所有觉得会送死者昙开、自己也学会；团队收集三次含去年第三次，翠惊疑后让续说。恢复魔装为有研究院成员的团队承诺，形态能力可能不同，尚未实际修回。',27099)
E(27112,27147,'A（墨的真诚与翠犹豫）／D（家园制度）／C（组织及国度干预判断）','荒原安定点收被弃少女和无城收人类，罪犯更严限制，为墨描述；她真诚不等团队无罪。翠因梦想家不像爪痕将怀疑推旁，预判扩大会被叫停是当事推理。她质疑王庭而非所有国民，背负樱仇、孩子、方亭、祖盟约不敢再许无法完成承诺，回答要考虑。',27127)
E(27149,27221,'A（对话和信息边界）／D（经历、生日来源）／C（翠关系推断）','墨把未获答允归自己用餐闯祸，翠明确否认，原因是责任负担；翠询朋友而墨要求加入后才可交底。翠问是否与爪痕有联，沉默使她推有联系，不是获黑猫代号或确切组织名单。墨讲打工/物界上学为建设家园补知识，生日源昔日翠亲告不是调查。',27189)
E(27223,27354,'A（制礼及朋友互认）／D（节俗、玩笑评价）','122回退与用餐并行，白给三人都作写字巧克力，小恶作剧后见自己名字大喜；夏给三人宝石造型。夏明说小是队友朋友之喜欢，小先误听恋爱，白帮腔含前受欺负情绪；小承认朋友而非确无别友，江媛仍在。夏借胡闹教表达只有两人懂的心意，不把戏谑娇蛮/没朋友当客观全称。',27296)
E(27356,27412,'A（发礼与双手机知情）／D（谢礼传统二手解释）','翠返屋掩累，林手机此前已知巧克力但翠假装不知；先发13日路边买三盒，原为零食后决定留14礼。她解释国度促销/队友谢礼传统，最后明说旧队友所讲且有所怀疑，历史起源不得全A。白将说做蛋糕被小拦，此刻翠仍没知蛋糕。',27384)
E(27414,27467,'A（不同礼词与称呼、亲密变化）','白给翠母亲字样、给小请求用更喜欢交换一点父/老师关爱、给夏感谢并问能叫小凉。翠最初极端安抚下认母，现在被长期珍重打动真拥抱；小因读字放下抢夺仍嫉妒，非全部和解或敌意消失。白口头妈收老师，感翠身高变化错猜新鞋，没有得知手术。',27449)
E(27469,27551,'A（造型、试探与喂食）／C（翠起初猜测）','夏复现翠心之花、白更成熟心之芽与小芽的差异；额外夹层夏心之叶以试做/尊前辈掩饰，翠探查成分普通未见加料。夏期望翠吃产生私密联想，翠却以免孤立夏为由喂回；不能将动作写成翠吃掉或确认心意/真魔力补完。',27539)
E(27553,27648,'A（双向友谊与往昔记忆）／D（小的比喻）','小给白蝴蝶结糖果因共爱糖和适合发饰；给夏镜子不只魔装，还承认她晚两月却进步快使自己看见不足，谢同行。最初旁人猜荷包蛋/灌木/脸均错，不升设定；夏追小后获抱。翠回忆安苏高中在教室送巧克力引海王谣言，不能当实际滥情事实。',27625)
E(27650,27735,'A（回忆、当前礼物和情绪）／D（童话比喻）','安雅从共同成为少女一年后到婚前年年送，宝剑礼的救公主说辞遇林纠最初安救林；皇后清记忆是玩笑。小王冠由翠认出，夏白原不知；小称翠王子或公主最喜欢，仍不知父身。翠连起安佩剑与小王冠而落泪，只告往事，无身份揭露；小不是故意触伤或已知安礼细节。',27723)
E(27737,27793,'A（蛋糕消息传递与假急事）／C（翠最初误猜）','129翠原猜挑战甜品爱好；白为夏取不存在的手机被支来，透露父生日、视频寄送，翠望夏会意识递话。翠佯接急电、借工作急事出门，拒小留看蛋糕；当晚无真实新急务。白仍因他人没看称妈，后来小凉称谓已实际用。',27770)
E(27795,27836,'A（借车方案及首次见人）／C（路线风险估计）','翠因背景暴露/父女关系不能不接视频而找普通布景，祖研究所慢与店关门，选先借墨车。夜寒仅单衣、敲门用法沃符文。褐卷发少女不认识墨荷，翠凭看见金发认海蒂阿比梅尔=郁金香=石蒜女，非已经识金蛇/褐鹈两个代号。',27834)
E(27838,27895,'A（军医历史、当前行为）／C（识别和战斗推测）','郁金香旧天使名源医术/资源调度/温柔而非仅军长女，多人不知母女；翠只点头交且少伤未受治疗。郁未认伪龙胆、听墨荷警惕，翠看背手推准备变身非实际开战；褐欲说墨荷就是黑被拽住。翠困其变化暂不问，墨隔断阻偷听，接受冷静期借车披外套。',27868)
E(27897,27928,'A（车功能、解身与生理反应）／D（旅店解释）','车指纹/魔波双验证，录翠权限，猫雨刮/魔力点烟器与飞行档；出祖区先滑翔再禁区落地，不在禁区自由施大魔。宾馆满，出门30分钟小电话至；翠第一通暂不接、暗巷解男身明显恶心。界桥+两日少女适应已减轻，普通人即经桥也不适；后补三后辈首晚曾解身也经历适应期。',27927)
E(27930,28009,'A（通话和父职反省）／D（掩护同事说辞）','古典酒吧点低度银月春蝶第二视频接，谎称第一没听、男同事谈工顺便祝寿，不是真与同事赴宴。蛋糕37，王冠触愧怀恋而父礼带欣慰温暖。林反省因父不正经早逝、怕魔侧危险强压学习而疏女，安生前黏合；如今真向女说对不起非只为未接电话。',27995)
E(28010,28059,'A（父女部分和解及分糕）／D（蜡烛推销）','小承认父担心有理因翠救才安全，双方仍不够亲密难说肉麻话；蜡烛店称占星靠生日点，隔视频没烧。原拟整糕寄改三人分并为翠留，白建议给爸又收叔留块寄，此处无实际寄出。夏持手机三人祝，身份未曝光。',28016)
E(28061,28096,'A（回返、警告和决定）／D（危险口信）／C（翠分析）','林拒两女搭话并返巷变身，借外套已录常服、特绕巷防见；还车衣后墨才提醒考核有危险、最好不去/小心，未给具体袭击方案。翠觉得不止模拟大兽灾，玛信息也未验证，后辈先前拒退仍顾虑，决定再搜集后问祖，不是当场确定必安全或立刻退出。',28094)
E(28097,28129,'A（扫描实际作用及防护失效）／C/D（理论担忧）','翠记真出生非2月14，怕读心/历史回溯等高阶术；原文明言不擅术式，仍能隐呼吸/本相并放空。蜡烛扫描心率和魔活性，紧张反使其触发；不是占星认出实际生日，更没有破解林翠身份。高端魔术存在不等此廉价蜡烛具有。',28116)
E(28131,28189,'A（新共同认知与半真掩护）','小白只信翠和林生日巧同，夏已知而装惊讶。翠数次欲否真实生日被盖声，权衡后从善如流承认庆日；很多年没过半真半托词，非主动撒谎设随机生日。两次庆生同2月14终，小白仍未怀疑同身。',28165)
E(28190,28284,'A（当前睡眠与历史教学表现）／D（原因猜测、战术例题）','当前近凌晨实际入眠、近两日可少女沉睡，修复原因是或许而非又做一次术。梦中15岁矢教10岁种妮姆，魔力总量与每秒出力分开；飞行感知等占用需留闪避余量/隐藏上限反推敌人，不是总量越大瞬发无限。100/30/3.3及蕾5占4均教学假设非全族固定数值，500米感知为题设不是妮姆已实现。她乐观好学获平等认同又传播语录，矢承认新人解释不一定对。',28240)
E(28286,28331,'A（姐妹和教学接手因果）／D（妮娜自责）','妮娜半母保护、怕行贿和辜负期待而躲矢；妹乐观主动提问不反驳姐。表达差及过度心疼使姐教慢，妹自行整理问题请矢，逐渐改直接学；矢不怨认为妮娜已完成部分，妮娜却误认讨厌。排班强迫相见尚未巡检，不是队长正式惩罚撤职。',28323)
assert ev[-1]['id']=='E427'
C('把术式列为翠雀真正强项，抹平会用与擅长的区别','MODERATE','能力定位／相对专长',[47],'卡47称真正强项是出力管理、术式、近战经验和规则战。','134明确虽然翠雀并不擅长术式，仍为防生日识别使用数项保障；能熟练应用低阶术式与有战术经验，不等专精术式。卡把相邻专长并列会让这一局限消失。','E424','A','她会使用术式且能判断简单扫描，也熟悉高阶术存在；当前文本明确不擅长这一领域。不要把不擅长绝对化为完全不会术式。','生成万能术式专家、无代价开发高阶调查术，或反向误写完全不能用。','后续将会用的工具、理论见识、战术专长与术式短板分别保留。')
revise('C021','105事件三114段纳入115采购；餐厅到流放谈话为115—119，考核具体警告134才得，121返程尚未得警告。129对白昨天商店与131翠前天同来，和113当前/回叙及12入国存在相对日措辞张力，按明确14庆生日记录并挂R005，不自改源。','E403、E407、E410、E417、E419、E423','原文连续语义确认章节与消息先后。',[105])
revise('C006','133父以自己的身份反省严教/避魔造成疏远并道歉，小理解其担忧但仍不够亲密；王冠亲近与父蛋糕感受不同。卡105末把小仅作父母之外恩人会漏91已认母关系，128憧憬不自动取消该约定。','E416、E417、E421、E422','同日两身份关系补充，不把生日温情写成彻底和解。',[105])
revise('C013','119墨自述高层传言→15/16年前樱核流放，120自述团队知三次昙开及能修魔装，翠未确认技术。翠从减弱爪怀疑到121凭沉默推联系，131只认郁金香旧身份；听黑半字不等获黑猫代号。卡167/106仍将妮姆去向未明作为全局状态须沿末段修，历史137她活着上课不能倒灌结局。','E407—E410、E418、E419、E427','新增传播层与童年性格，不越阶段提前全部秘密。',[106,162,167])
revise('C084','134—135再明确实际出生日非14，蜡烛实际扫描魔活性误触。小白从不知翠生日变相信与林同日，夏装惊讶；翠接受庆日不等真实登记日已查明。','E421、E424、E425','后期机制强化日期类别而非推翻既有庆生日。',[105])
revise('C095','卡161卷一状态也写苏约九年前赴间界；同一错误回接本号，127旧巧克力高中记忆不提供九年失联依据。','E415','全读旧方亭组织条目发现重复错误载体。',[161])
revise('C038','136当前近两天可以实际入眠，叙述以或许修复解释，非新一轮手术已发生；仅睡眠新状态不解除再损死线。136训练数字为例题而非固定全族参数，持续占用与魔量不同。','E426','区分修复后的新表现、原因推测及通用战术。',[105,106])
revise('C069','132翠再次实际解除林身入酒吧，134重新变龙胆，外套录常服；不能把早期单向异常延伸至当前。两界生理不适不等男身已消失或无法变回。','E420、E423','新增实际往返对旧状态的直接校验。',[105])
revise('S010','115物资用途仅墨口径；119流放转述链与121组织沉默；131翠认海蒂旧人而对方未认龙胆，褐不懂墨荷且黑半字被打断；129白经夏安排递蛋糕计划，133两身份对话掩护；135小白知同日庆生不知同身。','E403、E407、E410、E417—E425','不同名字、消息和阶段不捆成统一全知。',[105,106])
revise('S011','翠120因梦想家描述减爪怀疑、121仅推有关联，墨121误把被缓拒归闯祸而翠纠正。白125把缩高错当新鞋，136回忆妮娜误觉被厌而矢并不怨。必须容许误解并保存获纠时点。','E409、E410、E413、E427','新场景印证应可怀疑和误认。',[105,106])
revise('R005','129白称昨天与店员商量、131翠称前天同来，与明确2/14当前及先前13日商店/同来语境有张力；不改原文或替角色自动记成真时间。126白包装先干花后假花亦仅保原字面；谢礼巧克力历史起源为翠转旧队友说法。','E412、E414、E417、E419','保留输入相对日/材质措辞和知识源边界。')
erevise('E383','132补普通人即经界桥仍可不适，翠先两日少女适应再解男身仍恶心，三后辈首晚解身有适应期见E420；此前少女一般免适应仅指魔力身，不推普通本体全免。','后文补生理形态边界。')
erevise('E402','115明确翠只懂墨一部分，墨觉得看透不能升级；后续幸福分歧/组织不知见E403/E406/E409/E410。','后文直接限定先前主观评价。')
knowledge='2/14：林电话获红局务及祝福→翠餐厅补幸福半答→墨停车场转述流放来源→车内说魔装/家园→翠减怀疑又因沉默推爪关联；未得身份名单。三女并行制礼，翠已从林手机知巧克力，返屋仍不知蛋糕。夏派白递话后翠假急电外出，借车识郁金香但不识金蛇/褐鹈，黑半字打断。林第二视频谈父女反省、未真正寄糕；还车后墨才警告考场，翠不确定。蜡烛低阶扫描误触，小白仅信同生日，夏佯惊。凌晨睡眠梦回战年教学/姐妹，非当前时间回退。'
for id,refs,detail in [
 ('M014','E407,E408,E410,E412,E413,E414,E417,E419,E422,E423,E425',knowledge),
 ('M015','E404,E406,E407,E409,E410,E412,E414,E424,E426,E427','礼制不等女王强迫，幸福观不裁真理；墨无错信念/修魔承诺、翠爪联系推理保层次。谢礼起源为旧友转述；术式数字题设不是固定能力参数；蜡烛不测生日，妮娜被厌纯误解。'),
 ('M019','E405,E406,E410,E411,E413,E414,E415,E416,E421,E422','红直白祝福没获恋爱回应；翠尊幸福差异且背责不愿轻许，墨误认失败原因获纠。小白夏互赠与嫉妒/友情并行，白用喜欢交换照顾、夏接受喂回；父王冠与蛋糕触情不同，父女承错仍不亲密，91认母不被当前憧憬抹掉。'),
 ('M021','E404,E412,E420,E424,E426','餐具冷却/震动及冷藏球需具体用法；物质身即经桥也有适应期，魔身与本体分开。出力是每秒上限非魔量，飞行感知持续占用，实战留余量、藏上限、反读敌占用；卡2/106已有主干不新建重复遗漏。'),
 ('M036','E403,E407,E408,E409,E410,E419','民生采购认真比价、餐费失算非全面无能；墨真信家园不等爪合法。翠承担太多需考虑而非因她表现笨拙拒绝；墨需翠先加入才交底，借车披衣与冷静期并存。'),
 ('M017','E413,E420,E423,E426','白感缩高但不知手术；翠男身再现并生理不适、可恢复龙胆常服；当前可以少女实际睡眠，修复为或许因，不是第二次手术记录。'),
 ('M020','E418,E419,E420','临时寻找电话背景受国度特色、夜营业、考场东侧客满、研究院层报耗时限制；借车飞行档滑翔后禁区落地，魔波录权可启动，不是可瞬移任意地。'),
 ('M016','E406,E409,E416,E426,E427','幸福守剩余观、复仇开始规划、王冠引泪不等完全治愈或完全绝望。妮姆乐观早慧/平等接纳与妮娜过护/误解分开，姐妹性格不因后续悲剧提前变成全沉默。'),
 ('M029','E420,E426','魔力身与解除本体跨界适应不同；睡眠由休眠改实眠是翠个体近期状态，原因以或许限定。'),
 ('M039','E403,E404,E407,E410,E412','物资远途采购、术式工具和实际知识学习互补；女王贵族甜品礼仪非女王强制，餐厅按损坏索赔并因失误补偿，优惠券有期限。社会经济机制已有此组，原卡105保餐饮主线不应记全遗漏。')]:mrev(id,refs,detail)
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
write('evidence_records.json',ev);write('issue_records.json',issues);write('missing_records.json',missing);write('judgment_changes.json',hist);write('session_14_changes.json',change)


ledger=read('reading_ledger.json');prev=copy.deepcopy(ledger['coverage']);start,end=26742,28331
ranges=[[1,end],[36130,38825]];chars=sum(len(S[n-1]) for lo,hi in ranges for n in range(lo,hi+1));lines=sum(hi-lo+1 for lo,hi in ranges)
assert chars-prev['continuous_semantic_chars']==sum(map(len,S[start-1:end]))
newcards=[106,143,154,158,161,162,167];ledger['card_entries_read']=sorted(set(ledger['card_entries_read']+newcards));ledger['card_entries_targeted']=sorted(set(ledger['card_entries_targeted'])-set(ledger['card_entries_read']))
cov=copy.deepcopy(prev);cov.update(continuous_semantic_chars=chars,continuous_semantic_char_percent=round(100*chars/1641637,2),continuous_semantic_lines=lines,continuous_semantic_line_percent=round(100*lines/38825,2),worldbook_full_bodies_read=len(ledger['card_entries_read']))
ledger['coverage']=cov;ledger['source_full_read_ranges']=ranges
session=dict(session='14',previous_next_line=start,new_source_range=[start,end],new_lines=end-start+1,new_chars=chars-prev['continuous_semantic_chars'],next_line=end+1,completed_chapters='卷二第115—137章',note='连续逐段完整显示并阅读；只检索标题规划边界不计正文。卡106后段不计源覆盖。保存校验后立即继续。',**{k:v for k,v in change.items() if k not in ['session','evidence_changes','missing_changes']},revised_evidence_ids=[x['id'] for x in change['evidence_changes']],new_full_card_body_ids=newcards,rechecked_full_card_body_ids=[22],rechecked_existing_card_sections=[2,3,47,64,105]);ledger['sessions'].append(session);write('reading_ledger.json',ledger)
nc=next(c for c in chap if c['start_line']==end+1);cp=read('resume_checkpoint.json')
scene='2月14双重生日结束，翠实际入眠。当前梦回1979矢车菊刚任队长的训练期：妮姆学习出力占用；137补教学从过护的妮娜逐渐转矢，妮娜误觉辜负被厌；下午排班将与矢巡工事，尚未展开。'
pending=['下一L28332卷二138《握今》；累计覆盖含独立末段，不重计。','C013/M036：翠120减爪怀疑、121由沉默推联系，131只认郁金香旧姓名、黑半字打断；134墨才警告考核，翠决定问祖未问。未得完整名单/黑猫代号，流放拒任归责仅墨说。','C038/C096/M017：13日已修补、丝奇境无痛但毁两件不返；14后可实眠，原因或许修复，不是再手术；再献祭男身消失为有条件专业警告。C114会用术式≠擅长。','C084/C066/M014：135小白新信翠与林同日生日，仍不知同身；夏装惊。蜡烛测魔活性非真出生日，真正日仍未知。132/134可解林再变龙胆，常服录借衣已还。','C006/M019：91认母不被王冠憧憬抹掉；133父女承错缓和仍不亲密。白给夏称小凉实际用，小白夏互赠与竞争并存。','M014/M015：137妮娜误觉被厌、矢不怨，教学接手因表达和过护非惩处；出力课堂数字全假设，不把妮姆500米感知写成已会。','C005摩可拒返原因；C009第三晶/祭子与白双偏移；C076气来源；C103袭考实验室计划；C112门记录未知；M031苏间界；樱案/田记忆/交割/爱之源朋友仍待后续。','73.55%健康已PASS；约90%再轻量检查，自动继续。卡93/143，余50；手机/HTML未全审、宿主未运行。']
cp.update(next_source_start_line=end+1,next_source_end_hint=nc['end_line'],source_unread_main_range=[end+1,36129],next_source_chapter=nc['volume']+' '+nc['title'].lstrip('# '),last_completed_source_chapter='卷二第137章《妮娜和妮姆》',last_read_line=end,session='14',cumulative_character_coverage=cov['continuous_semantic_char_percent'],cumulative_characters=chars,card_body_unread_ids=sorted(set(cards)-set(ledger['card_entries_read'])),integration_status='内部批次14已保存；一致性检查后立即续读，不等待用户',latest_scene=scene,pending_rechecks=pending);write('resume_checkpoint.json',cp)
pct=f'{cov["continuous_semantic_char_percent"]:.2f}';sev=Counter(x['severity'] for x in issues);ni=len(issues)
nav=f'> 续审14导航：唯一续读断点为 **L28332／卷二第138章《握今》**，累计 **{pct}%（{chars}／1641637字符）**。先见[轻量续读索引](CONTINUE_STATE.md)；历轮“本轮／当前／下一／尚未”按其历史时点解释，不能覆盖[现行断点](resume_checkpoint.json)。'
for n in ['00_card_structure.md','01_evidence_index.md','02_full_audit_report.md','03_missing_content.md','04_timeline_knowledge_risks.md','05_user_confirmation_required.md']:
 s=(A/n).read_text('utf-8');s=re.sub(r'^> 续审\d+导航：.*$',lambda m:nav,s,count=1,flags=re.M);mdwrite(n,s)
for n in ['README.md','02_full_audit_report.md']:
 s=(A/n).read_text('utf-8')
 for k,v in sev.items():s=re.sub(r'\|'+re.escape(k)+r'\|\d+\|',f'|{k}|{v}|',s,count=1)
 if n.startswith('02'):s=s.replace('当前136项＝113项C',f'当前{ni}项＝114项C',1).replace('累计记录136项',f'累计记录{ni}项',1).replace('不是136条',f'不是{ni}条',1)
 else:
  s=re.sub(r'^> 续审13已保存.*$',f'> 续审14已保存；自主任务继续。唯一下一断点 **L28332／卷二第138章《握今》**，累计 **{pct}%（{chars}／1641637字符）**。先读[CONTINUE_STATE.md](CONTINUE_STATE.md)；校验后立即续读，约90%再健康检查。',s,count=1,flags=re.M)
  s=s.replace('累计完整语义阅读86条正文','累计完整语义阅读93条正文',1)
  s=re.sub(r'原著连续语义核验：L1–26741及L36130–38825，共[^。]+。',f'原著连续语义核验：L1–28331及L36130–38825，共{lines}/38825行（{cov["continuous_semantic_line_percent"]:.2f}%；按无换行字符{pct}%，{chars}/1641637字符）。',s,count=1)
  s=s.replace('**136项**',f'**{ni}项**',1).replace('136项Canon',f'{ni}项Canon',1).replace('源文L26742–36129','源文L28332–36129',1).replace('：402组可回查证据','：427组可回查证据',1).replace('：136项工作稿',f'：{ni}项工作稿',1).replace('从现行断点L26742（卷二第115章《餐厅》）','从现行断点L28332（卷二第138章《握今》）',1)
  s+='\n## 续审14｜家园分歧、双重生日与姐妹教学\n\n'+f'连续L26742—28331（卷二115—137），1590行/{session["new_chars"]}字符；累计{pct}%（{chars}/1641637），下一L28332卷二138。新增E403—E427、C114；无新M，已有组按差异补充而非凑数。修订旧问题{len(change["updated_existing_issue_ids"])}项、证据2项、遗漏{len(change["expanded_missing_ids"])}项。世界书新读7条，累计93/143；源卡不改。\n\n维护有限认知：流放转述、家园真诚与爪关联、借车认旧人、夏递蛋糕计划、蜡烛扫描误会均区分来源。C114记录会用术式但不擅长，与卡47专长说矛盾；C095回接卡161九年失联。没有把旧梦当现实日序，亦无将牌面和技法例题当固定数值。73.55%检查已通过，本批保存后立即续读，不等用户。\n'
 mdwrite(n,s)
s=(A/'03_missing_content.md').read_text('utf-8').replace('L26742—36129','L28332—36129').replace('L26742–36129','L28332–36129');mdwrite('03_missing_content.md',s)
extra={'00_card_structure.md':'新全文106/143/154/158/161/162/167共7条，累计93/143；22全文复核，2/3/47/64/105相关段复核。106后段摘要不计原著覆盖。','04_timeline_knowledge_risks.md':knowledge+'\n\n证据E403—E427；本次时效回接C013/C084/C066/S010/S011/M014。119流放原因与15/16年前来源是墨自述，完整真相尚待后文；134蜡烛测心率或魔活跃，135同日生日信念不等真实出生或同身揭露。137教学由妮姆主动提问到矢接手，妮娜自责不是队長实际怨。','05_user_confirmation_required.md':'U001—U008不变；幸福观、邀约和技术承诺不由角色好感数替代。C114术式定位属文本差异，不以玩法授权掩盖。假生日蜡烛是源文低阶功能，不能设定为真实身份占星识别器；如新增此机制须隔离IF。'}
for n,body in extra.items():mdwrite(n,(A/n).read_text('utf-8')+'\n## 续审14｜增量与阶段校正\n\n'+body+'\n')
oldnav=(A/'CONTINUE_STATE.md').read_text('utf-8');rules=oldnav[oldnav.index('## 续读规则'):oldnav.index('## 当前场景与开放索引')];footer=oldnav[oldnav.index('## 详细资料职责与读取条件'):].replace('[13补证留痕](session_13_changes.json)','[14补证留痕](session_14_changes.json)')
state=f'''# 续读接管索引｜第一阶段自主连续执行中

导航不替代详细证据与历史。正常完成条件为原著100%后通过最终第一阶段完整性检查；内部批次保存后立即续读，不能等待“继续”。

- **唯一下一断点：L28332／卷二第138章《握今》**，章末提示L{nc['end_line']}。
- **累计字符{pct}%＝{chars:,}／1,641,637**；{lines}行。已读L1—28331及独立末段L36130—38825，未贯通。14新增L26742—28331，1590行/{session['new_chars']}字符，卷二115—137。
- **E001—E427、C001—C114、M001—M039**；下一E428/C115/M040。主报告{ni}项＝C114＋有效S18＋R5；S018撤销占位勿用；U001—U008八组。
- 卡正文93/143，余50；手机/HTML未全审、宿主未运行。阶段IN_PROGRESS_NOT_COMPLETE。

'''+rules+'## 当前场景与开放索引\n\n'+scene+'\n\n'+''.join('- '+x+'\n' for x in pending[1:])+'\n**本批维护：** 73.55%健康已完成；本批完整性与输入哈希见report_validation.json。校验后立即续读。\n\n'+footer
mdwrite('CONTINUE_STATE.md',state)
v=read('report_validation.json');v.update(issue_count=ni,severity=dict(sev),evidence_count=len(ev),missing_count=len(missing),coverage=cov,next_source_start_line=end+1);v['session_14']={'status':'PENDING_VALIDATION','session':session};write('report_validation.json',v)
print(json.dumps(dict(coverage=cov,next_line=end+1,E=len(ev),C=114,M=len(missing)),ensure_ascii=False))
