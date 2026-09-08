"""续审15增量维护脚本；只写audit，源文件只读。执行前拒绝重复批次。"""
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
assert len(ev)==427 and max(int(x['id'][1:]) for x in issues if x['id'].startswith('C'))==114
cards={x['id']:x for x in read('card_entries.json')}
chap=read('chapter_index.json')
change={'session':'15','evidence_changes':[],'missing_changes':[],'new_evidence_ids':[],'new_issue_ids':[],'updated_existing_issue_ids':[],'new_missing_ids':[],'expanded_missing_ids':[]}
hist=read('judgment_changes.json')
def E(start,end,level,finding,quote=None):
 id=f'E{len(ev)+1:03}'; q=quote or next(n for n in range(start,end+1) if S[n-1].strip() and not S[n-1].startswith('#'))
 ev.append(dict(id=id,start=start,end=end,quote_line=q,level=level,finding=finding,session='15'));change['new_evidence_ids'].append(id)
def C(title,severity,kind,card,current,problem,evidence,level,accurate,impact,action):
 id=f'C{max(int(x["id"][1:]) for x in issues if x["id"].startswith("C"))+1:03}'
 issues.append(dict(id=id,title=title,severity=severity,kind=kind,card=card,current=current,problem=problem,evidence=evidence,level=level,accurate=accurate,impact=impact,action=action));change['new_issue_ids'].append(id)
def revise(id,addition,refs,reason,card=None,field='accurate'):
 x=next(x for x in issues if x['id']==id);before=copy.deepcopy(x)
 x[field]+=' 续审15：'+addition;x['evidence']+='；'+refs
 if card:x['card']=list(dict.fromkeys(x['card']+card))
 hist.append(dict(session='15',id=id,reason='2026-09-09；'+reason,before=before,after=copy.deepcopy(x)))
 change['updated_existing_issue_ids'].append(id)
def erevise(id,addition,reason):
 x=next(x for x in ev if x['id']==id);b=copy.deepcopy(x);x['finding']+=' 续审15回接：'+addition
 change['evidence_changes'].append(dict(session='15',record_type='evidence',id=id,reason=reason,before=b,after=copy.deepcopy(x)))
def M(category,title,refs,details,scope):
 id=f'M{len(missing)+1:03}';missing.append(dict(id=id,category=category,title=title,evidence=refs,details=details,scope=scope));change['new_missing_ids'].append(id)
def mrev(id,refs,details):
 x=next(x for x in missing if x['id']==id);b=copy.deepcopy(x);x['details']+=' 续审15：'+details;x['evidence']+=','+refs
 change['missing_changes'].append(dict(session='15',record_type='missing',id=id,reason='2026-09-09；卷二138—162连续新证补充时效与收录边界，旧判断保留并限定历史阶段。',before=b,after=copy.deepcopy(x)));change['expanded_missing_ids'].append(id)





E(28332,28389,'A（设施、行动、能力机制）／D（劝导与战术期待）','同日下午南工事区，大型组合防御/歼灭发射台/堡垒/雷区；单魔雷可破蛹壳，大片危险不等已实际杀半蜕。矢劝墨停止自责道歉循环以免未来配合变差，非已战场失职。握今右手指套遥握选对象、维持绝静、松后等时双倍变化；静躁魔、矢抽雷封特容再松。不是必须手接触实体。',28381)
E(28390,28444,'A（通报链及备战）／C（来源怀疑）／D（角色技能报告）','妖精感兽→指挥部魔镜通知辖区队长，封锁/疏散/解除局部限魔，5分钟后正常行动。矢一月连地底清剿，不解蛹何来；多数初卵少数蠖、初蛹罕见非绝无，来源尚未知不认幕后已证。墨自报叶级、七种基础术/四套预符，没讨蛹经验，矢判断可支援即出发。',28420)
E(28445,28551,'A（战况、限制与规则）／D（标准、解释）','到场从蛹判为约30米半蜕（蛹通常20米上限），研究院推荐3蕾5以上叶为常规标准非硬性法。墨连控周围空气出力不足，尝试手臂短停即被挣开；矢丝牵避，尺量具体肌肉—墙、口器—地、爪—头等距离，墙碎后惯性甩兽，非冻结所有运动且仍可绕定距点作弧。妮娜先只见结果再推因果。',28494)
E(28552,28604,'A（出力、破约束与规则逐步显现）／C（早期猜解）','尺控半蜕占近四成出力，余六成保留；魔身高耗可出汗泪以冷却/拟人，当前却不累先疑汗。兽脱被定表皮破束，丝接触前软化，先推变湿规则后由手融明示魔力化腐液，身体衣装均受侵，兽用自身壳身筑巢。不能先让旁观墨理解完整规则。',28555)
E(28605,28663,'A（筑巢、限度和协作）／C（限制尚未找全）','一般残兽安全隐蔽食足处筑，眼前为当场例外；矢首次见造巢。墨固定空气拖闭合，自身腿融且治疗魔也受侵；剪会付巨量且占出力，因自身流失敌增，黏液/魔力/巢穴/自控/操控全剪不动，改腐蚀抗性成功。自述必有限制未查清，不能把未知限制自行补造或当任意概念必剪。',28640)
E(28664,28714,'A（处决全操作与代价取舍）','抗性被剪兽受自伤但规则重启未死；矢测试丝仅3秒、墨范围扩大耗升濒竭。三织命同现，尺0兽体10丝，10无需现实单位；主动暂停抗性分离腾出出力后剪尺0—10距离，第二秒重合、第三秒展网杀兽而丝不再融。不能省暂停写持续永久去抗性，亦不把单丝阶段保留全部空间操作。',28695)
E(28715,28762,'A（战后恢复、互认）／D（坦白和自评）','讨伐上报后民治治安官组织重建/回流，居民送糖葫芦饰品。身体衣装已修回非整段返程仍腐烂；矢复盘轻敌并青春男因接触尴尬，非始终完美冷静。墨握封糖葫芦后承刚意识嫉妒，矢承过去躲避稍不快但出生入死抵芥蒂，以信队友解释冷静。既非全盘从未介意也非嫉妒当罪。',28751)
E(28763,28813,'A（复診、离开事实与转述行为）／D（医嘱和叛逃情报）／C（危险推断）','146明说治疗一周后复诊，准正常用全部现存能力但不准实验室繁开；不是2月15/16马上复诊。回叙14次晨15找墨空屋、无联系方式和管理消息，至今更疑其涉险不善。翠只问郁金香，谎说陵园想起而非承认偶遇；祖答已叛爪，墨行踪仍未供。',28768)
E(28814,28872,'A（认知推进和告知计划）／D（祖掌握及推断）','翠据郁金香叛逃确认墨团队爪痕，仍不理解动机；祖名单说首批除财政心腹城防最多，推大概率战争后遗，非完整原因已判。翠决定隐墨接触、传考核风险以护全部考生，但尚组织言辞被祖晚宴邀请打断，不是已完成警报提交。祖猜近日见郁，翠未确认。',28858)
E(28873,28923,'A（赴宴、服装接受与仪礼）／D（餐厅评价）','与复诊同日晚，祖选公主裙，翠原则仅避过暴露/阻行动，非厌所有女装；祖车睡未透客人，至登飞行厨房方解释兑现魔事权力交易。厨师自称王庭而祖疑吹，非已证假牌。十余人提裙后跪拜为效忠礼，尚非翠正式加冕。',28902)
E(28924,28975,'A（名号、身份传播和接受接权）／D（保密保证）','折鹤兰花牌13011；飞燕草字牌13314外事部长、迷迭香字牌13877宣传副部长、雪毬字14053、鹤望兰字13692，来客至少字牌不是皆花牌。祖承例外向本席泄矢回国、保证无外传仅其话。翠坚持非正式权杖，最终问可用权力相当接受，不是已经就任。',28933)
E(28977,29063,'A（权力结构解释和明确推举）／D（角色政治评判、投资说明）','两贵族副院长代女王对外、五花牌教选司执事且派系互卡；五派不按部门纯切。名义反馈/活动/报表/宣传/考标均他派可拦，研究院提名仅增成功率需人情；黄欠2紫1、红新增部门可换人情。贵族派不等直接女王，副院长顾四杖妥协。六面间谍贪污强花被捕故事是具体案例不泛化人人同罪。祖投资友好蓝杖替厌恶的权斗、翠问绿派动机答本院需杖，未此刻揭所有人旧军真心。',29025)
E(29064,29123,'A（翠态度及新信息接收）／D（权杖事务和调查往事口述）','翠仍拒有流放/复仇两外障，但第三价值拒绝已变愿掌权改变问题；明认条件解后主观愿任。权杖下属办杂仍本人重要决策，祖支持集体复仇不是强制独行。翠目标樱也含调查牺牲荼蘼；祖称调查院折巡查、抓并弄死烬侍得凶手已死结论，翠此时首次听行动过程；不能倒给此前已知完整调查。',29116)
E(29125,29174,'A（翠叙述行为）／D（历史回忆和战争价值判断）','153翠说获捕风捉影消息而女王恰召见，非闯宫；女王实际回答至少部分问题，有些奇怪有些沉默，细节未逐条讲，不是始终零解释。翠认战正当自保守平民、怕信念遭利用，向祖称差点权杖战死而祖否危险程度。女王随后邀誓任杖，翠怒拒认为死伤孩子更应得，完整战争真相仍没披露给读者或全席。',29158)
E(29176,29215,'A（方案提出与新知）／D（法规案例、线人情报）／C（敌行动预测）','折查旧例可立功抵制裁，鸽血红185年前获赦（原300年流放）、80年前上任；翠初知，非翠已可自动赦。女王观礼为此时内部确认，不倒改109可能。黑市入口/假证背靠魔事被容许，数批标红来源爪与黑烬但不能锁定个人，暗访学院区推等考；不等已锁全部人或最终行动布局。',29207)
E(29217,29264,'A（做账/灭口计划和翠疑问）／D（人员安全承诺）／C（全局幕后猜测）','折称设陷防护最小伤，祖说硬件损必须有；财政3亿缺口加诸院计划报15亿，非已发生实际损失。首谋活口会揭账故准备处死，其他可赦。翠串线却仍问交易起是否做局/白狼是否甘入/其他院参与，无从得知；不能把全棋局操作者全知定案。墨牺牲换好处只是翠设想尚未出卖或保证绝对安全。',29250)
E(29265,29303,'A（私下谈话和军礼）／D（个人担忧与效忠承诺）','宴后折单独与翠低声，以换零件船讲升迁异化，明确担心让翠失自我，若不任杖仍向她本人效忠愿从新目标；军礼祝长官。不是此前公开所有人都已宣布旧军传承，亦不是政客绝无真诚/完全无私。',29291)
E(29304,29362,'A（争执及知情变化）／D（祖监控边界及自辩）','同夜返程翠明赞同立功赎罪方向、需尊后辈并参与安保，真正恼被耍。祖此时给郁金香现号金蛇，线人多方推认；称见面从翠反应知、拉拢只推，不知如何知翠在卢。祖知叛逃原因一点却不完整、让翠查，城市利益自辩不自动正当性裁决。',29343)
E(29364,29420,'A（翠拟方案及返屋）／C（组织三分和优先判断）','同夜翠按有限知情分财政核心/战争淘汰/后来叛入三群，第一三坏第二疑为其假设，不能推组织客观三等道德名单。拟自己抓墨旧部留询问，黑烬交研究院，需调整考场/观礼/考生活动；明确后续可把方案交魔事与折共同完善，并非永远瞒魔事。旧屋新租客、回家裙未换引三人惊叹，非次日新见。',29399)
E(29421,29474,'A（告后辈危险和当场反应）／D（报考动机与预告）','返屋换裙后同夜告三人院高层聚餐、爪黑潜入和合作；退今年可次年跳级、女王可能特殊再观不绝无。小想当众表现不知自身SS、白明说为樱及父母复仇，翠劝杀非天职又不强迫放仇。白拿心之叶，尚不把叶级等已会全部术。',29435)
E(29475,29505,'A（新叶阶段、资源和经济分工）／D（典型周期及历史上限认识）','白当日独开叶，早上拒逛街未先告，五个月快且夏更快；普通种芽大半年一年、芽叶3/4年为常态不是硬时钟。回响经播种者换爱晶涨魔反哺魂需消虚浮、心蜜花园产助灵思不直接涨魂且可连续；芽叶3蛹、叶蕾20蛹或2半蜕所需兑换规模不是吞回响瞬升。月圆后摩可合法渠道、翠积存投喂后辈并花牌训练稳，玛也投柏安。安婚后持续追强花林养家、少回响作存款，其余资源；花后无路是彼时千年认识，不能驳282盛开实证。',29498)
E(29506,29568,'A（三人选择、未来计划正式告知）／C（实力展望）','白升叶只初具复仇基础，若未来数月补术/技巧加完整兽化才可抗当年麻雀，非今天已过字牌；小魔装不到两月仍可争实战，夏当场投降不等实际比输。三人皆坚持，白为仇、小践并肩承诺与不落后、夏独立同伴资格；翠尊其意，首次向全三明确今年或明年拟成魔事权杖并要保密，不是所有真相全告。',29567)
E(29569,29646,'A（五都分院、迎接及箱中潜入）／D（地方观感与寒暄）','五都对应五院；除调查/研究外另三院跨都设分院，卢办只签或送件、无侍者低实权，院长绣球地位不如本部部长。折一行已在卢数日才到办事处，借劳累要办公室。湿衣新员工撞鹤望兰箱，折止其责，关门后才开箱，翠屏息被撞咳腰；在场绿派才见，分院不见箱内故此章尚无折女传闻爆出。称上司蓝杖为追随者立场不正式就任。',29644)
assert ev[-1]['id']=='E450'
C('女王部分回答与正式接见被改成拒绝解释和闯宫','MAJOR','历史因果／认知来源',[106],'卡106事件十称翠闯入蔷薇宫质问，女王没有解释战争伤亡，只提出效忠加冕。','153翠明确女王恰接见自己，并说她回答了至少其中一部分，只是有些答案奇怪或某些问题沉默。摘要把有限回答变完全不答，也把召见变自行闯宫，删掉需要后验的认知裂缝。','E441','A（原文如此记述）／D（翠对往事的陈述）','保留捕风消息、召见、部分回答且奇怪、情绪性拒任的顺序；别将翠的战争正义判断等于已向读者公开战争全部内幕。','生成从未发生的闯宫行动，或将女王所有回应锁为沉默回避。','后续依原口述修摘要，并开放奇怪回答的迟到解释。')
C('将宴席中飞燕草等字牌误写为花牌','MODERATE','人物能力／任职等级',[106],'卡106事件九说折鹤兰领衔，飞燕草、迷迭香等花牌集体跪礼。','149仅折鹤兰是花牌13011；飞燕草13314、迷迭香13877等为字牌。部长职务不能替代认证等级。','E438','A','折为花牌，其余列明的四人字牌，所有来客至少字牌；未知者不一律花牌。','凭部门职位抬高战力或改变花牌稀缺性。','按个人明确编号等级记录，保留职位独立维度。')
C('将准备转达的考核警告写成已经向祖母绿提交','MODERATE','信息传播／行动状态',[106],'卡106事件八及幕末说只把考核人为袭击警告交祖，已透露必要险情。','147决定告安全信息但还在修辞就被宴会邀请打断；宴上先由折鹤兰主动报告潜入和计划。决定说不等实际说，祖猜近期见郁也不等获墨全部警告。','E435、E436、E442、E445','A（说话及打断顺序）／C（祖推断）','146只问郁旧人且用陵园想起作借口；147传警意图未在本场说出，154折给既掌握线索，157才更明示监控边界。','让祖因翠警报才布置防卫，或持有实际从未交出的消息来源。','后续拆分准备、实际告知、他方先掌握三种记录。')
C('留活口方案被写成对整个魔事院保密的私案','MODERATE','保密范围／合作行动',[107],'卡107事件三称翠建立瞒祖母绿、魔事院与后辈的私案。','158明确计划由自己抓旧部并调整安保部署，后续可交魔事院让折鹤兰等一起完善。她隐瞒旧友接触/细节，不等方案必须不让任何魔事院人员知道。','E445、E446','A（规划文本）','区分墨荷私交/情报来源、自己亲抓留活口的方案以及共同布防。此刻后者待交绿派，不是全院已知或永久瞒全院。','阻止原文合作流程，或把安全布置写成翠单人秘密修改。','后续按角色、派系和实际提交时间维护保密。')
M('能力','握今目标规模、对抗出力和持续占用的实际限制','E428,E430,E432,E433','138遥握可选对象不必实体接触，但140面对半蜕连周围空气都因范围/魔量出力不足而难控，手臂短停即反弹。143改控局部空气墙成功，144随液体绕墙需扩范围而占用增高、耗尽逼近。绝对静止描述的是成功施用的效果，不是无条件控制任何强者；这些失败与代价决定团队分工。','卡64完整机制段与106战役主干缺140直接压制失败的上限证据。106已有后续耗涨故不称整卡完全无代价；本项补机制边界，与M017阶段战技回接，不粗并身体损伤或其他魔装限制。')
revise('C021','106复诊/问郁被定2月15—16，但146明确治疗一周后，同日晚宴；15日仅回忆发现墨退房。107把158返屋定21日、159—161定22日，正文都承同一晚归程，不能为章节切换加日。162只说准备多日、已在卢好几日，24日尚无本章直接日期依据。106尺约束四成在142非141、114三形处决在144；107箱女谣言162尚没发生。','E430—E450','连续时间锚与首次发生逐章复核。',[106,107])
revise('C013','146祖答郁已爪后翠才确认墨团队；157祖明确郁现名金蛇；其关于初爪财政/旧军组成仍人物现有名单，需与末段墨创立史分期。145墨自我发现嫉妒、矢承躲避不快后因战友而释，是137误解的后补，非从始全无负面。','E434—E436、E445、E446','后期认知从推有联推进归属确认，保留前态。',[106,107])
revise('C038','146一周后复诊正式准全部现存能力、实验室禁繁开，稳定期临时限制结束；不会返已毁两件。143剪抗性仍持续占出力，144主动停止才腾余量，不是一次剪除永远零成本。','E432、E433、E435','后续治疗/实战明确持续性与阶段变化。',[106])
revise('C017','160千年历史与翠自身都认为花后无路，安不断强化未开华；这是当时认识，不得因该段旁白存在而继续用未写入正文否定282盛开。开华新阶段与总魔量仍可提升分开。','E448','原文早期绝对语言受到末段实证修正，记录时效。')
revise('C005','160补月圆后联系猫眼/祖使摩可从偷渡、名不副实转合规，回响可用渠道随之改变；未说冒妮偷职位或本人拒返理由。','E448','增合法渠道形成的因果与时效。')
revise('C019','160翠将积存回响投后辈、玛大成本投柏安，收集/贡献/奖励和二次赠与应区分。不能以最终击败者就推其他人绝不能获资源，但也不以赠与直接证明初始收集权相反。','E448','保留产权问题未证边界，同时补实际流转。',[28])
revise('C066','161三名后辈现在确已获拟任蓝杖与两院合作口径，不继续全员未知权杖计划；依然小白不知林身、三人未得墨私交/留活口细案。','E447、E449','公开节点新到，及时移除当期旧未知。',[107])
revise('C110','159白主动以樱和过去父母复仇，众人知其兽力和仇恨不等父母具体身份全揭；祭子知情旧证仍有效，本次新叶亦不等完整兽能力机制全公开。','E447—E449','政治知情和能力开华各自变化，防倒推。')
revise('S010','146只问郁，147欲警未发，149祖承向此席例外告矢身份，150翠初知五教选司；152首次得调查院抓烬侍/折巡查行动，154初得鸽血红赦史与线人潜入，157初得金蛇现号。159三人获危险与合作，161再得权杖意向；162箱内偷渡仅本席核心见，分院尚不知。','E435—E450','实收、假说辞、计划和旁观接触严格分开。',[106,107])
revise('S011','145矢承躲避曾不快，修正137不怨教学但非全关系从无不快；146疑墨非善到147组织确认，不代表动机都明。154黑市标红识组织不锁个人，与157多方识出著名金蛇可以并存。158三群道德判断为翠分类猜测，非客观道德表。','E434—E446','认识升降和对象范围防冲突。',[106,107])
revise('R005','145墨口述其他队员以及妮娜夸队长处疑妮姆字误，保原不默改；154今天资格考核与当前离开考还有时段有词误疑点，不据今天把开考前移；162叙称顶头上司蓝杖是下属预认不证任命完成。','E434、E442、E450','字面矛盾不强制Canon补丁。')
erevise('E407','153翠口述补女王部分回答后提出加冕、被召见而非闯，见E441；119墨拒任丢面归责不是全部历史因果。','迟到解释接前转述，不同话者不同可知。')
erevise('E426','146复诊一周后准用现存全部能力见E435，仍不在实验室试繁开；此前或许修复导致实眠保留推测级，不扩大硬医疗因果。','新复诊边界更新。')
erevise('E427','138劝停止自责、145又承认过去躲避使少许不快；137不怨教学与后来承认关系芥蒂不同对象，不误判原著自相矛盾。','随后明确当事关系。')
knowledge='历史138—145：握今静雷→指挥部受妖精警报→蛹判断升级半蜕→墨控臂失败→矢尺约束/墨观察推理→变湿到魔化液规则→剪多概念失败→抗性暂分后主动停→三形处决→战友互认。现实146治疗一周后（13日治疗约20日），15日寻墨为空屋是回叙；147仅决定告警被打断，晚宴祖泄矢身份、字牌下属任职与正式杖分开。152翠愿上位但两外障，首次收调查旧案行动；153女王部分回答的口述不全揭真相；154线人不锁个人，157给郁=金蛇。158当夜拟共绿派完善活口案，159当夜告敌/合作，白当日叶；161再告权杖意向。162日期未点，分院只见箱受撞，核心关门后才见翠。'
for id,refs,detail in [
 ('M014','E429,E430,E434,E435,E436,E438,E439,E440,E441,E442,E445,E446,E447,E449,E450',knowledge),
 ('M015','E428,E429,E430,E432,E436,E439,E440,E441,E442,E443,E445,E446,E448','初蛹极罕非绝无；讨伐推荐非硬法。暴汗拟人有条件，规则限制未查明不能造；政治名单/意图/安全承诺分D/C，祖只知少数原因，幕后全局仍未知。花后无路为当前认识不抵末段。'),
 ('M017','E430,E431,E432,E433,E435,E448,E449','握今目标上限另M040；尺具体距离受支点强度，剪范围和魔量有限、停止持续抗性换出力，三形重合需完整织命。146稳定结束准能力，白当日叶但未新术完善，未来数月抗麻雀为预测。'),
 ('M019','E434,E436,E440,E444,E445,E446,E447,E449','墨嫉妒145自悟而矢保真不全客套；折低声个人效忠即不任杖仍愿随，政治算计与真情并存。翠从厌王庭避权转愿掌权改变，仍不愿牺牲旧友换利。三后辈报考各自动机，白复仇/小承诺竞技/夏独立，并非一心杀敌。'),
 ('M018','E428,E429,E434,E436,E438,E439,E440,E442,E443,E450','地方应急封锁/解禁/疏散/复建分工；5教选司和2副院长、按派不按部门纯分，人情互否。名义部门权和实际僵持、贵族派与女王副院长不同。回响药材资源补给制度卡28已有不新记全遗漏。除调研外3院跨都分院，低实权并不代表无机构。'),
 ('M036','E428,E430,E434,E436,E445,E446','墨过护歉疚到嫉妒自悟及战友认可，握今保糖葫芦是感情物件用途；翠知爪仍对其有回忆滤镜，决亲抓核真不等判她必清白。国度弃者和财政/后来加入区别是翠暂分类，末段创立史仍须校正。'),
 ('M016','E434,E440,E441,E444,E445,E446','亲历者在任期20年后的权力/复仇选择改变，不能锁从不想权；折怕人格异化、翠争旧英雄且不愿全盘代判。女王部分回答奇怪保开放，国度战争不纯为翠所述层次。'),
 ('M021','E428,E430,E431,E432,E433,E448','魔雷可破蛹壳，限制破坏术式不等所有普通武器都有效。爱晶增魔反哺需稳，心蜜助灵思非直接增魂，典型兑换与时段不是瞬升保证；卡28已有材料，不重复建M。'),
 ('M022','E435,E436,E438,E442,E445,E450','祖从有限问郁推见旧人、黑市入口被容许但非任意人都成功；149向内部例外泄身份也违早保证，NPC不能全知。在魔事院箱式潜入仅核心绿派看见，分院礼貌不是知真实身份。')]:mrev(id,refs,detail)
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
write('evidence_records.json',ev);write('issue_records.json',issues);write('missing_records.json',missing);write('judgment_changes.json',hist);write('session_15_changes.json',change)

ledger=read('reading_ledger.json');prev=copy.deepcopy(ledger['coverage']);start,end=28332,29646
ranges=[[1,end],[36130,38825]];chars=sum(len(S[n-1]) for lo,hi in ranges for n in range(lo,hi+1));lines=sum(hi-lo+1 for lo,hi in ranges)
assert chars-prev['continuous_semantic_chars']==sum(map(len,S[start-1:end]))
newcards=[107,165,166,169,171,176,177];ledger['card_entries_read']=sorted(set(ledger['card_entries_read']+newcards));ledger['card_entries_targeted']=sorted(set(ledger['card_entries_targeted'])-set(ledger['card_entries_read']))
cov=copy.deepcopy(prev);cov.update(continuous_semantic_chars=chars,continuous_semantic_char_percent=round(100*chars/1641637,2),continuous_semantic_lines=lines,continuous_semantic_line_percent=round(100*lines/38825,2),worldbook_full_bodies_read=len(ledger['card_entries_read']))
ledger['coverage']=cov;ledger['source_full_read_ranges']=ranges
session=dict(session='15',previous_next_line=start,new_source_range=[start,end],new_lines=end-start+1,new_chars=chars-prev['continuous_semantic_chars'],next_line=end+1,completed_chapters='卷二第138—162章',note='连续逐段完整显示并阅读；只检索标题规划边界不计正文。卡107后段不计源覆盖。保存校验后立即继续。',**{k:v for k,v in change.items() if k not in ['session','evidence_changes','missing_changes']},revised_evidence_ids=[x['id'] for x in change['evidence_changes']],new_full_card_body_ids=newcards,rechecked_full_card_body_ids=[28],rechecked_existing_card_sections=[2,20,22,47,16]);ledger['sessions'].append(session);write('reading_ledger.json',ledger)
nc=next(c for c in chap if c['start_line']==end+1);cp=read('resume_checkpoint.json')
scene='晚宴后翠愿筹上位并与魔事共同完善留活口案，三后辈新知蓝杖意向而未全知身份。162折带箱入卢安分院，仅绿派核心关门后见翠，撞箱者/分院尚未确认箱中人。'
pending=['从L29647卷二163续读；累计含独立末段不重计。','C013/M036：146已知墨是爪，157祖告郁=金蛇；翠仍不知其与旧友动机，拟亲抓核问，不能判清白。','C115/C014：女王曾部分回答，内容未全向读者展开；仍须迟到解释。','C038/M017/M040：146一周稳定期结束准全部能力；握今受对象魔量和出力约束，抗性剪曾主动停，不写永久免疫。','C066/C110/M014：161三后辈新知蓝杖计划，小白仍未知林翠同身；白父母秘密仍未知。','C021/C118：158至161是当晚，非卡逐日；162关门见箱中翠，女儿误会是否后文有据继续核；活口计划拟共同完善非瞒魔事。','C005/C017/C019/M021：160合法晶来源与魂稳/灵思区别，花牌上限当时认知不得覆写282；归属绝对化未证。','C009第三晶、C076气、C103袭考、C112门记录、M031苏间界及旧案/田记忆/交割/爱源朋友后续复核。','73.55%健康已PASS；约90%再检查后自动续读。卡100/143，余43；手机HTML未全审，宿主未运行。']
cp.update(next_source_start_line=end+1,next_source_end_hint=nc['end_line'],source_unread_main_range=[end+1,36129],next_source_chapter=nc['volume']+' '+nc['title'].lstrip('# '),last_completed_source_chapter='卷二第162章《我队长呢？》',last_read_line=end,session='15',cumulative_character_coverage=cov['continuous_semantic_char_percent'],cumulative_characters=chars,card_body_unread_ids=sorted(set(cards)-set(ledger['card_entries_read'])),integration_status='内部批次15已保存；一致性检查后立即续读，不等待用户',latest_scene=scene,pending_rechecks=pending);write('resume_checkpoint.json',cp)

cp['last_completed_source_chapter']=next(c['volume']+' '+c['title'].lstrip('# ') for c in chap if c['start_line']<=end<=c['end_line']);write('resume_checkpoint.json',cp)
pct=f'{cov["continuous_semantic_char_percent"]:.2f}';sev=Counter(x['severity'] for x in issues);ni=len(issues);nextlabel=f'L{end+1}／'+cp['next_source_chapter']
nav=f'> 续审15导航：唯一续读断点为 **{nextlabel}**，累计 **{pct}%（{chars}／1641637字符）**。先见[轻量续读索引](CONTINUE_STATE.md)；历史时点不能覆盖[现行断点](resume_checkpoint.json)。'
for n in ['00_card_structure.md','01_evidence_index.md','02_full_audit_report.md','03_missing_content.md','04_timeline_knowledge_risks.md','05_user_confirmation_required.md']:
 s=(A/n).read_text('utf-8');s=re.sub(r'^> 续审\d+导航：.*$',lambda m:nav,s,count=1,flags=re.M);mdwrite(n,s)
for n in ['README.md','02_full_audit_report.md']:
 s=(A/n).read_text('utf-8')
 for k,v in sev.items():s=re.sub(r'\|'+re.escape(k)+r'\|\d+\|',f'|{k}|{v}|',s,count=1)
 if n.startswith('02'):s=s.replace('当前137项＝114项C',f'当前{ni}项＝118项C',1).replace('累计记录137项',f'累计记录{ni}项',1).replace('不是137条',f'不是{ni}条',1)
 else:
  s=re.sub(r'^> 续审14已保存.*$',f'> 续审15已保存；自主任务继续。唯一下一断点 **{nextlabel}**，累计 **{pct}%（{chars}／1641637字符）**。先读[CONTINUE_STATE.md](CONTINUE_STATE.md)；校验后立即续读，约90%再健康检查。',s,count=1,flags=re.M)
  s=s.replace('累计完整语义阅读93条正文','累计完整语义阅读100条正文',1)
  s=re.sub(r'原著连续语义核验：L1–28331及L36130–38825，共[^。]+。',f'原著连续语义核验：L1–29646及L36130–38825，共{lines}/38825行（{cov["continuous_semantic_line_percent"]:.2f}%；按无换行字符{pct}%，{chars}/1641637字符）。',s,count=1)
  for a,b in [('**137项**',f'**{ni}项**'),('137项Canon',f'{ni}项Canon'),('另列39项','另列40项'),('源文L28332–36129','源文L29647–36129'),('：427组可回查证据','：450组可回查证据'),('：137项工作稿',f'：{ni}项工作稿'),('从现行断点L28332（卷二第138章《握今》）',f'从现行断点L29647（{cp["next_source_chapter"]}）')]:s=s.replace(a,b,1)
  s+='\n## 续审15｜握今战斗限制、权杖意向与政治信息链\n\n'+f'连续L28332—29646，卷二138—162，{session["new_lines"]}行/{session["new_chars"]}字符；累计{pct}%（{chars}/1641637）。下一{nextlabel}。新增E428—E450、C115—C118、M040，修订旧问题{len(change["updated_existing_issue_ids"])}项、证据{len(change["evidence_changes"])}项、遗漏{len(change["expanded_missing_ids"])}项。新读7条卡正文，累计100/143。\n\n女王部分回答与零解释、字牌与花牌、拟警报与已警报、拟共同完善与对魔事保密分别留证，不把政治当事人的估计升级全知。握今的目标限制与剪持续占出力单列差异，战后停止抗性不是永久免疫。前期花牌上限以当时认知解释，不推翻既读末段盛开。保存校验后立即继续。\n'
 mdwrite(n,s)
s=(A/'03_missing_content.md').read_text('utf-8').replace('M001—M039','M001—M040').replace('共39项','共40项').replace('L28332—36129','L29647—36129').replace('L28332–36129','L29647–36129');mdwrite('03_missing_content.md',s)
extra={'00_card_structure.md':'本批完整新读107/165/166/169/171/176/177，累计100/143；28全文复核，2/20/22/47/16相关段复核。未来摘要不计源文覆盖。','04_timeline_knowledge_risks.md':knowledge+'\n\n证据E428—E450；对应修订见session_15_changes.json和judgment_changes.json。','05_user_confirmation_required.md':'U001—U008不变；女王未公开的回答、后文可能的政治动机和握今未查明上限仍开放。不得借玩法授权把零回答、全花牌、已报警或瞒魔事的摘要错误变成原著事实。'}
for n,body in extra.items():mdwrite(n,(A/n).read_text('utf-8')+'\n## 续审15｜增量与阶段校正\n\n'+body+'\n')
oldnav=(A/'CONTINUE_STATE.md').read_text('utf-8');rules=oldnav[oldnav.index('## 续读规则'):oldnav.index('## 当前场景与开放索引')];footer=oldnav[oldnav.index('## 详细资料职责与读取条件'):].replace('[14补证留痕](session_14_changes.json)','[15补证留痕](session_15_changes.json)')
state=f'''# 续读接管索引｜第一阶段自主连续执行中

导航不替代详细证据与历史。正常完成条件为原著100%后通过最终第一阶段完整性检查；内部批次保存后立即续读，不能等待“继续”。

- **唯一下一断点：{nextlabel}**，章末提示L{nc['end_line']}。
- **累计字符{pct}%＝{chars:,}／1,641,637**；{lines}行。已读L1—29646及独立末段L36130—38825，未贯通。15新增L28332—29646，{session['new_lines']}行/{session['new_chars']}字符，卷二138—162。
- **E001—E450、C001—C118、M001—M040**；下一E451/C119/M041。主报告{ni}项＝C118＋有效S18＋R5；S018撤销占位勿用；U001—U008八组。
- 卡正文100/143，余43；手机/HTML未全审、宿主未运行。阶段IN_PROGRESS_NOT_COMPLETE。

'''+rules+'## 当前场景与开放索引\n\n'+scene+'\n\n'+''.join('- '+x+'\n' for x in pending[1:])+'\n**本批维护：** 73.55%健康已完成；本批完整性与输入哈希见report_validation.json。校验后立即续读。\n\n'+footer
mdwrite('CONTINUE_STATE.md',state)
v=read('report_validation.json');v.update(issue_count=ni,severity=dict(sev),evidence_count=len(ev),missing_count=len(missing),coverage=cov,next_source_start_line=end+1);v['session_15']={'status':'PENDING_VALIDATION','session':session};write('report_validation.json',v)
print(json.dumps(dict(coverage=cov,next_line=end+1,E=len(ev),C=118,M=len(missing)),ensure_ascii=False))
