"""Stage 2C: source-verified local corrections. Run once against saved input baseline.
Historical builders are not invoked. Before-images remain in canon_before.zip.
"""
from pathlib import Path
import json,copy,re,hashlib,importlib.util
P=Path(__file__).resolve().parents[2]; C=P/'canon'; B=C/'_stage2c'
def read(p):return json.loads((P/p).read_text(encoding='utf-8-sig'))
def dump(p,x):(P/p).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
EV=read('canon/events/records.json'); CH=read('canon/characters/records.json'); REL=read('canon/relationships/records.json'); K=read('canon/knowledge/records.json')
E={r['id']:r for r in EV}; H={r['id']:r for r in CH}; R={r['id']:r for r in REL}; Q={r['id']:r for r in K}
evidence=read('audit/evidence_records.json'); queue=[]; changes=[]
def cr(n,origin,title,decision,ranges,reason,targets):
    q=dict(id=f'CR{n:03}',source=origin,title=title,decision=decision,source_ranges=ranges,
      audit_evidence=[e['id'] for e in evidence if any(e['start']<=b and a<=e['end'] for a,b in ranges)],
      verification='原文指定窗口已实际阅读；旧Review仅作待核建议',reason=reason,targets=targets,changes=[])
    queue.append(q);return q
def change(q,module,id,key,value):
    db={'Event':E,'Character':H,'Relationship':R,'Knowledge':Q}[module];rec=db[id]
    before=copy.deepcopy(rec.get(key));
    if before==value:return
    rec[key]=value; entry=dict(id=f'CC{len(changes)+1:03}',review=q['id'],module=module,record=id,field=key,before=before,after=copy.deepcopy(value),source_ranges=q['source_ranges'],reason=q['reason'])
    changes.append(entry);q['changes'].append(entry['id'])
def textchange(q,path,old,new):
    f=C/path;s=f.read_text(encoding='utf-8-sig');assert old in s,(path,old)
    if old==new:return
    f.write_text(s.replace(old,new),encoding='utf-8')
    entry=dict(id=f'CC{len(changes)+1:03}',review=q['id'],module='Document',record=path,field='exact_text',before=old,after=new,source_ranges=q['source_ranges'],reason=q['reason'])
    changes.append(entry);q['changes'].append(entry['id'])
def appendtext(q,path,text):
    f=C/path;s=f.read_text(encoding='utf-8-sig');textchange(q,path,s,s.rstrip()+'\n\n'+text+'\n')
def newevent(q,id,title,time,occ,result,ranges,actors,related):
    r=copy.deepcopy(E['EV0187']);r.update(id=id,title=title,time_layer='历史回溯',time_tier='T3',time=time,participants=actors,occurrence=occ,direct_result=result,changes=result,
      source_ranges=ranges,revealed_at=ranges,checked_anchors=ranges,review_context_ranges=ranges,audit_navigation=q['audit_evidence'],knowledge=[],relationships=[],knowledge_refs=[],relationship_refs=[],character_refs=[],related_events=related,
      witnesses='按所列直接叙述/当事人经历；读者后叙不授予旁人知情。',later_informed='未单列无证传播；后文回述与历史时点分开。',meaningfully_unaware='无证主体不默认知情。',before='见发生与历史限定；未给精确年份。',long_term=result,note=q['reason'],location='原文限定位置；精确地点不足保持UNKNOWN',verification='STAGE2C_SOURCE_VERIFIED',verification_scope='本条源窗逐行核证；CR/CC保留新增依据。')
    E[id]=r;EV.append(r);change(q,'Event',id,'integration_origin',q['id'])
q=cr(1,'STAGE2B1_REVIEW/S2A-R01','交易回撤与祖的干预不等整个时间循环','ACCEPT',[[36725,36735],[37193,37228]],'交易回撤明确；祖保留消耗、空间环路且干预过往交易，类别未解；金蛇的猜测不成为通用时间技能。',['EV0151','PS035'])
change(q,'Event','EV0151','title','金蛇交易回撤与祖母绿干预过往交易')
change(q,'Event','EV0151','occurrence','券契受抵押和规律限制，市集交易含未来五十年；金蛇回撤取回魔力，祖的消耗和空间环路仍在；祖出现在金蛇的过往交易记忆中并阻止再次回撤。')
change(q,'Event','EV0151','direct_result','能力：交易回撤被制约；金蛇认识到过往交易也受到祖的干预，但干预类别UNKNOWN。')
change(q,'Event','EV0151','changes',E['EV0151']['direct_result'])
q=cr(2,'STAGE2B1_REVIEW/S2A-R02','引离植物墙实验范围','ACCEPT',[[31794,31810]],'实见墙体稀疏/恢复；夏推理传送维持术式，明确现阶段不能传活人；不升任意实体穿墙。',['EV0126','PS029'])
change(q,'Event','EV0126','title','夏队撤退与引离干预术式维持的植物墙')
change(q,'Event','EV0126','direct_result','战术：三人脱离；能力：小镜令术式维持的植物墙稀疏，撤镜后恢复。传送维持术式是夏的解释，不证明任意物质或活人传送。')
change(q,'Event','EV0126','changes',E['EV0126']['direct_result'])
q=cr(3,'STAGE2B1_REVIEW/S2A-R03','郁金香骗局清算历史漏项','ACCEPT',[[36410,36424]],'阿比梅尔受财政院与民治院清算、革职及家族衰落有直接叙述；数百年前描述氏族地位，不等骗局发生年。',['EV0151','ORG016','EV0190'])
newevent(q,'EV0190','郁金香骗局清算与阿比梅尔衰落','海蒂出生之前；具体年份UNKNOWN','阿比梅尔成员参与炒作郁金香；泡沫破裂后财政院与民治院联手清算，涉事职员被革职送战场、商人受处罚，家族商业与政治影响衰落。','组织/经济：显赫氏族→被清算与衰落；不等全部后代有罪。',[[36410,36424]],['阿比梅尔家族','财政院','民治院'],['EV0151'])
change(q,'Event','EV0151','related_events',E['EV0151']['related_events']+['EV0190'])
q=cr(4,'STAGE2B1_REVIEW/S2A-R04','资格认证制度历史漏项','ACCEPT',[[33136,33144]],'初创由魔事院与研究院草拟，以保护为目的；后世测试与权义分化有据，具体创设年UNKNOWN。',['WR004','WR005','EV0132','EV0191'])
newevent(q,'EV0191','资格认证制度创设与后续扩展','早于当代考核；各次制度变更年份UNKNOWN','魔事院与研究院草拟资格制度控制讨伐风险；早期仅魔装及基础能力两项实战，后续白/字牌权义与测试分化，当代白牌有四门笔试及四项实战。','制度：讨伐保护资格→扩展权义荣誉及分化测试；评级不等开华。',[[33136,33144]],['魔事院','研究院','考试院'],['EV0132','EV0123'])
q=cr(5,'STAGE2B2_REVIEW/R001','木芙蓉错名','ACCEPT',[[33910,33915],[34010,34019]],'参赛者是木棉；木芙蓉仅旧表误字，不能新增实体或Canon别名。',['EV0134','CH052','P_TEMP_118'])
change(q,'Event','EV0134','participants',[v.replace('木芙蓉','木棉') for v in E['EV0134']['participants']])
q=cr(6,'STAGE2B2_REVIEW/R002','猫尾身份与柏安驻守名单','ACCEPT',[[6619,6620],[8685,8693],[8971,8977],[9806,9847]],'猫尾为调查院小队长，赴柏安查案后失踪获救；不属于柏安驻守编制。猫尾队和灯盏的失踪、恢复分别处理。',['ORG018','LOC007','CH021'])
for old,new in [('猫尾草等所在、与方亭队建立合作的驻守群体。','柏安市本地驻守及导师群体，与方亭队阶段性合作；猫尾为外来调查小队长。'),('猫尾队一度在异常巢穴中失踪后获救；玛格丽特与队员再与方亭队交流、留宿和参战。','柏安队共五人、常驻四人；灯盏追查失踪案后被囚获救。玛格丽特、灯盏、白蓟、木百合、含羞草分工活动；猫尾调查小队另属调查院，获救后回国治疗。'),('玛格丽特、猫尾草、灯盏等相关人；身份及当时指挥看事件。','玛格丽特及灯盏、白蓟、木百合、含羞草；具体阶段与职务按人物/事件，不把来访调查者纳入常驻编制。')]:textchange(q,'04_organizations.md',old,new)
textchange(q,'05_locations.md','猫尾草等驻守及失踪调查发生的城市。','柏安小队驻守、外来猫尾调查队失踪及救援发生的城市；来访不等常驻。')
q=cr(7,'STAGE2B2_REVIEW/R003','审计C011父亡过度否定','ACCEPT',[[36425,36432],[38253,38268]],'父亲在海蒂开始识字时死于残兽袭击；母亲石蒜后来战死，两次死亡分开。audit只读，Canon附纠正而不改C011历史。',['CH015','CH019','audit:C011'])
appendtext(q,'UNRESOLVED.md','## Stage 2C｜已核证的历史审计冲突\n\nCR007：audit C011的“仅母亡已证、不能另造父亡”限定不适用于最终正文。L36425–36432明写海蒂父亲早亡；L38253–38268确认母亲石蒜后来牺牲。CH015/CH019已有正确分层。审计原件只读保留；后续不得再用旧限定否定父亡。')
q=cr(8,'STAGE2B3_REVIEW/R001','女王谈话关系触发错挂','ACCEPT',[[37943,37960],[38190,38228]],'听身世、拒任和坚持男性身份属于EV0176；EV0146为破坏本相与转移伤者，不提前共享后续谈话。',['EV0146','EV0176','REL028','REL079','REL_TEMP_038'])
v=E['EV0146']['relationships'];change(q,'Event','EV0146','relationships',[]);change(q,'Event','EV0146','relationship_refs',[])
change(q,'Event','EV0176','relationships',E['EV0176']['relationships']+v);change(q,'Event','EV0176','relationship_refs',E['EV0176']['relationship_refs']+['REL_TEMP_038'])
q=cr(9,'STAGE2B3_REVIEW/R002','亡妻后父职回顾与少年战争混层','ACCEPT',[[12400,12412]],'父职/复仇矛盾是安雅死后至复出；支持窗口虽在少年能力回顾之后，不能套十五岁。',['EV0058','REL001','REL_TEMP_019','EV0192'])
newevent(q,'EV0192','安雅死后林昀在复仇与养育责任间挣扎','安雅死后至开篇复出；末句对当代救援回接','得知安雅死讯后，林昀自责并想复仇，又担心自己出事使女儿失依，尝试以普通父亲身份养育；女儿遇险后重新选择行动。','心理/行动：丧妻自责与责任冲突→复出守护；不表示十五岁已婚育。',[[12400,12412]],['林昀'],['EV0182','EV0001','EV0059'])
change(q,'Event','EV0058','relationships',[]);change(q,'Event','EV0058','relationship_refs',[])
change(q,'Event','EV0058','note',E['EV0058']['note']+' L12400–12412的亡妻后回顾独立为EV0192，非本事件少年时层。')
change(q,'Event','EV0192','relationships',[['林昀','林小璐','复仇冲动与避免女儿失依相牵制']]);change(q,'Event','EV0192','relationship_refs',['REL_TEMP_019'])
ss=copy.deepcopy(R['REL001']['stages']);ss[1]['event']='EV0192';ss[1]['story_phase']='安雅死后至复出前；由EV0058混合支持窗独立';change(q,'Relationship','REL001','stages',ss)
q=cr(10,'STAGE2B3_REVIEW/R003','江可错名','ACCEPT',[[14995,15025],[17688,17711]],'前座同学为江媛，同一友谊继续到演唱会；旧错字不是另一个角色。',['EV0072','CH050'])
change(q,'Event','EV0072','occurrence',E['EV0072']['occurrence'].replace('江可','江媛'))
q=cr(11,'STAGE2B3_REVIEW/R004','吴家姐妹共同受训互诺与法律说法','PARTIAL_ACCEPT',[[36961,36985],[36995,37024]],'共同受训半年及回家互诺有据；天牛否认法理为D，不提升司法事实，也不再说原著完全没有法理说法。',['CH026','CH027','EV0178','REL033','REL036'])
for id in ['CH026','CH027']:
    st=copy.deepcopy(H[id]['stages']);st.insert(1,['祭子共同受训','姐妹重聚、共同受训半年，食祭前互诺一起回家；后被分开安排','A：L36961–36985；天牛法理否认是D，非司法核证'])
    if id=='CH026':st[2][1]='导师天牛；食祭后与妹妹被分往不同城市，不抹共同受训期'
    change(q,'Character',id,'stages',st)
    change(q,'Character',id,'knowledge',H[id]['knowledge']+' 天牛在分派时对薄荷称两人无法理姐妹关系（D，L37012），不等妹妹当场也听到；法定手续仍未知。')
change(q,'Event','EV0178','occurrence','吴惜雨进入吴家；被带走后姐妹重聚，共同受训半年，食祭前互诺一起回家。食祭后天牛安排薄荷回家潜伏，称吴惜雨无法理姐妹身份且已被蜂带走；法理内容为天牛说法D。')
change(q,'Event','EV0178','direct_result','家庭/行动：共同养育→隔离后重聚受训→互诺回家→不同任务分派；未裁定司法身份。')
change(q,'Event','EV0178','changes',E['EV0178']['direct_result'])
q=cr(12,'STAGE2B3_REVIEW/R005','蜂带走箭不自动证明授课师承','KEEP_UNKNOWN',[[36995,37020]],'天牛明确自称薄荷老师，只说箭被蜂带走；收窄肯定式导师导航为C候选/D转述，不断言不是师生。',['CH027','CH044','REL123','REL124','RQ005'])
change(q,'Character','CH027','relations',H['CH027']['relations'].replace('CH044蜂导师','CH044蜂带走安排为天牛转述D，师承仅C候选'))
st=copy.deepcopy(H['CH027']['stages']);st[2][1]='天牛称已被蜂带走（D）；师承候选C，授课与具体职权UNKNOWN；后与薄荷在考试交集';change(q,'Character','CH027','stages',st)
change(q,'Character','CH044','relations',H['CH044']['relations'].replace('CH027导师','CH027被其带走为天牛转述D；师承候选C'))
for id in ['CH027','CH044']:change(q,'Character',id,'unknown',H[id]['unknown']+['蜂与箭的正式师生职责和具体授课未有独立确证；带走安排不能自动赋予训练成果或信任。'])
q=cr(13,'STAGE2B3_REVIEW/R006','白蓟私比批评与正式赛分期','PARTIAL_ACCEPT',[[19047,19095],[20333,20391]],'阳台上玛向小解释白蓟有错；不能仅靠此段证明白蓟同场听到。私比批评回接EV0084，正式赛及败后道歉保留后节点。',['EV0084','EV0089','REL020','REL083','REL_TEMP_028'])
change(q,'Event','EV0084','relationships',E['EV0084']['relationships']+[['玛格丽特','白蓟','对其私比挑衅作负面纪律判断；阳台说明的听者为小璐']])
change(q,'Event','EV0084','relationship_refs',E['EV0084']['relationship_refs']+['REL_TEMP_028'])
change(q,'Event','EV0089','relationships',[['玛格丽特','白蓟','观战与技术解释；私比批评已在EV0084，败后道歉接EV0090']])
q=cr(14,'STAGE2B4_REVIEW/R001','玛获安死讯与翠踪迹时点','ACCEPT',[[18678,18699],[12757,12778]],'安死亡消息由猫眼在葬礼前告玛；EV0083为当代回述。EV0061木先告翠巡查来访，不是演唱会初知全部。',['CH007','K187','K215'])
change(q,'Character','CH007','knowledge','安雅死讯在葬礼前已由金绿猫眼告知（L18678–18699）；EV0061由木百合得翠雀来访线索（L12757–12778），EV0082舞台/后台再重逢。苏胜紫去向按转述和末次联系；公众认识歌手不等认识巡查使。')
ss=copy.deepcopy(H['CH007']['snapshots']);ss[1]['认知']='已知安雅死讯，已听木百合描述翠雀巡查来访；本次当面互认尚未完成，不推全知方亭近况';change(q,'Character','CH007','snapshots',ss)
q=cr(15,'STAGE2B4_REVIEW/R002','黑猫亲子宣称提前与重复TEMP','ACCEPT',[[38595,38618]],'当场亲子宣称在EV0157，EV0155不可提前给黑猫；186/188历史入口保留映射，不再算两次传播。',['EV0155','EV0157','K185'])
change(q,'Event','EV0155','knowledge',[]);change(q,'Event','EV0155','knowledge_refs',[])
change(q,'Event','EV0157','knowledge_refs',list(dict.fromkeys(E['EV0157']['knowledge_refs']+['K_TEMP_186'])))
q=cr(16,'STAGE2B4_REVIEW/R003','妮妮厨房实际听者与妖精来源','ACCEPT',[[15428,15474]],'实际妮妮对翠雀说明，摩可并非本场听者；各自魔力源生自花园不等同一颗。K225还残留向它说明，亦需纠正。',['EV0163','REL053','K182','K225'])
change(q,'Event','EV0163','participants',['妮妮','翠雀'])
change(q,'Event','EV0163','occurrence','妮妮向翠雀说明昨夜获返国培训通知、预计当天动身；摩可正式任职文件及魔镜待送达。妮妮向翠解释二者各自魔力源诞生于花园、从小为伙伴，非血缘姐妹。')
change(q,'Event','EV0163','knowledge',[['翠雀','妮妮返国安排、摩可任职文件待递及园丁成长背景','SUSPECTED','PARTIALLY_CONFIRMED','妮妮厨房告知；不等摩可在场']])
ss=copy.deepcopy(R['REL053']['stages']);ss[-1]['claim']='A：妮妮向翠雀回述与摩可的伙伴经历和返国安排；D：各自魔力源来自花园，不是同一颗。本段不证明摩可听见。';ss[-1]['claim_metadata']={'text':ss[-1]['claim'],'grades':['A','D'],'statuses':['CONFIRMED','CHARACTER_BELIEF']};change(q,'Relationship','REL053','stages',ss)
ss=copy.deepcopy(Q['K225']['states']);ss[0]['known_content']='我与摩可在花园共同成长；这次向翠雀说明返国和职务安排。';ss[0]['disclosure_state']='PARTIALLY_DISCLOSED';change(q,'Knowledge','K225','states',ss)
q=cr(17,'STAGE2B4_REVIEW/R004','白对樱死亡认知提前','ACCEPT',[[6508,6543],[11900,11942]],'EV0032被告知樱离开而仍希望见面；EV0055听蛾才得死讯及小璐为樱之女。',['REL067','K034','K187'])
ss=copy.deepcopy(R['REL067']['stages']);ss[1]['claim']='A：向翠雀问樱，被谎称已离开方亭，仍希望再见；此时未获死讯。';ss[1]['claim_metadata']={'text':ss[1]['claim'],'grades':['A'],'statuses':['CONFIRMED']}
ss.append(dict(event='EV0055',claim='A：听蛾揭露樱死亡及小璐为其女儿，情绪激荡而冲击；不是此前已经知道。',sequence=3,source_ranges=[[11900,11942]],story_phase='当代月圆节蛾对质，昏迷之前',evidence_navigation=['E165'],claim_metadata={'text':'听蛾得樱死讯后冲击','grades':['A'],'statuses':['CONFIRMED']}));change(q,'Relationship','REL067','stages',ss)
change(q,'Relationship','REL067','stage_nodes',3);change(q,'Relationship','REL067','key_transition_count',2)
q=cr(18,'STAGE2B4_REVIEW/R005','夏听旧队故事不是历史组队时','ACCEPT',[[8420,8438]],'旧队事实历史发生；夏当代咖啡馆听闻。保留原TEMP入口但转正确获取事件。',['EV0037','EV0039','K037'])
v=E['EV0037']['knowledge'];change(q,'Event','EV0037','knowledge',[]);change(q,'Event','EV0037','knowledge_refs',[])
change(q,'Event','EV0039','knowledge',E['EV0039']['knowledge']+v);change(q,'Event','EV0039','knowledge_refs',E['EV0039']['knowledge_refs']+['K_TEMP_039'])
q=cr(19,'STAGE2B4_REVIEW/R006','白生日快照停在失效中间称谓','ACCEPT',[[17543,17568],[17596,17608]],'人物快照说明取事件结束，故必须接父母称谓恢复及拥抱，不能停在老师/叔叔；同一身份、血缘/法律未因此公开。',['CH004:S03','K073','K082'])
ss=copy.deepcopy(H['CH004']['snapshots']);ss[2]['关系']='事件结束已再次得到爸爸回应、重新拥抱翠雀叫妈妈；不等法律收养或知林翠同一';ss[2]['心理']='A由生日失落与困惑，经林解释和双方回应重新接受家庭联系';change(q,'Character','CH004','snapshots',ss)
q=cr(20,'STAGE2B4_REVIEW/R007','身份确认位置错误','ACCEPT',[[7131,7150]],'夏家房间外阳台，不是医院；私谈不产生医护目击名单。',['CH001:S02','CH003:S02','EV0036'])
for id in ['CH001','CH003']:
    ss=copy.deepcopy(H[id]['snapshots']);ss[1]['位置']='夏凉家阳台（L7141–7145），未单列稳定LOC';change(q,'Character',id,'snapshots',ss)
change(q,'Event','EV0036','location','夏凉家阳台；L7141–7145。')
q=cr(21,'STAGE2B4_REVIEW/R008','女儿确认父早知与获知渠道必须分层','PARTIAL_ACCEPT',[[4157,4178],[4299,4311]],'部分推翻旧Review及K017边界：L4176已说果然早知，不能将其全部降为线索；返程才明确电视日期与红补告的渠道。',['EV0019','EV0020','K017'])
change(q,'Event','EV0019','knowledge',[[('林小璐' if x[0]=='林小璐' else x[0]),('父亲在自己坦白前已知道少女身份；具体何时及渠道未明' if x[0]=='林小璐' else x[1]),x[2],x[3],('当面坦白与父亲回应，L4157–4178' if x[0]=='林小璐' else x[4])] for x in E['EV0019']['knowledge']])
change(q,'Event','EV0020','knowledge',E['EV0020']['knowledge']+[['林小璐','父亲从电视得知的时间及后来红的告知','PARTIALLY_CONFIRMED','CONFIRMED','返程明确问答L4299–4311']])
change(q,'Event','EV0020','knowledge_refs',list(dict.fromkeys(E['EV0020']['knowledge_refs']+['K_TEMP_019'])))
ss=copy.deepcopy(Q['K017']['states']);new=copy.deepcopy(ss[0]);new.update(id='K017-T002',event='EV0019',known_content='爸爸在我坦白前就知道我是魔法少女，具体何时和如何知道尚未解释。',source='坦白与父亲回应',observation='父亲指出隐瞒身份已久；自己回应果然早就知道',source_ranges=[[4157,4178]],evidence_navigation=['E077'])
new['acquisition'].update(event='EV0019',point=4178,description='纪念日遇袭出战前，父女坦白现场');ss[0]['from_state']='CONFIRMED';ss[0]['source']='返程父亲明确说明';ss[0]['observation']='返程问答';ss[0]['source_subjects']=['CH001'];ss.append(new)
change(q,'Knowledge','K017','states',ss);change(q,'Knowledge','K017','boundary','EV0019 L4176已确认父早知；EV0020才获电视时点及红补告的具体解释，两层不能压成同一获取。')
change(q,'Knowledge','K017','events',['EV0019','EV0020']);change(q,'Knowledge','K017','source_ranges',[[4157,4178],[4299,4311]]);change(q,'Knowledge','K017','evidence_navigation',['E077','E079']);change(q,'Knowledge','K017','first_documented_event','EV0019')
q=cr(22,'STAGE2B4_REVIEW/R009','苏去间界计划与传播重复空壳','ACCEPT',[[19364,19378]],'玛历史听计划，现代转述给林/红；到达与加入爪痕未知。现正式K092/K232分层可保留；203空壳保持退役映射，旧TEMP不复活。',['EV0086','EV0187','K092','K232'])
change(q,'Event','EV0187','participants',['苏胜紫','玛格丽特'])
change(q,'Event','EV0187','later_informed','玛在当代EV0086向林昀和红思与转述；二者并非历史末次通话参与者。')
q=cr(23,'Stage2C/Canon-IF回归','Guardrails误预定骰子与能力优先级','ACCEPT',[], 'USER_DECISIONS U006明确整体重做、细则后议，尚未选能力优先或奇迹方案；Canon只保存原著条件，不能把技能偏好当用户已裁决玩法。',['INFERENCE_GUARDRAILS.md','USER_DECISIONS:U006'])
textchange(q,'INFERENCE_GUARDRAILS.md','先依原著条件判断是否可能，再由以后游戏层处理可能范围内结果；不实现“高骰无视条件”。命运骰、CG、好感及OC默认均不写成本轮世界事实。','Canon保存原著能力条件与未知；U006尚未决定骰子和能力边界的具体优先规则，整体重做留待用户。不得把任何未来骰子、CG、好感或OC默认写成原著事实。')
q=cr(24,'Stage2C/新事件查询回归','新增历史Event不能按源码行号归当代','ACCEPT',[[36410,36424],[33136,33144],[12400,12412]],'查询器硬编码历史EV集合会漏新补历史；按事件显式knowledge_epoch识别，现有189行为不变，新节点不得把后文行号当今时。',['knowledge/query_knowledge.py','EV0190','EV0191','EV0192'])
hist={9,10,37,50,51,52,53,58,79,81,95,111,118,141,142,143,144,145,146,147,148,165,166,167,168,169,176,177,178,180,181,182,183,184,185,187,189,190,191,192}
for e in EV:change(q,'Event',e['id'],'knowledge_epoch','HISTORY' if int(e['id'][2:]) in hist else 'CURRENT')
textchange(q,'knowledge/query_knowledge.py',"epoch='HISTORY' if int(event[2:]) in HISTORY else 'CURRENT'","epoch=events[event].get('knowledge_epoch', 'HISTORY' if int(event[2:]) in HISTORY else 'CURRENT')")
# Current first-party annotations supersede TEMP suggestions without overwriting original TEMP text.
q=cr(25,'Stage2C/引用整合','正式Canon仍只指向旧TEMP与失效历史阶段说明','ACCEPT',[], '保留TEMP作为历史证据入口；新增正式K/REL/CH导航，不重建实体，不把关联当知情授权。旧构建脚本只作历史，禁止直接覆盖冻结库。',['Event','Character','Relationship','README','INFERENCE_GUARDRAILS'])
tm={x['temp']:x['formal_ids'] for x in read('canon/knowledge/temp_to_k.json')};rm={x['temp']:x['formal'] for x in read('canon/relationships/temp_to_rel.json')}
for e in EV:
    change(q,'Event',e['id'],'formal_knowledge_refs',sorted(set(k for t in e['knowledge_refs'] for k in tm[t])))
    change(q,'Event',e['id'],'formal_relationship_refs',sorted(set(k for t in e['relationship_refs'] for k in rm[t])))
for c in CH:
    change(q,'Character',c['id'],'formal_knowledge_refs',[k['id'] for k in K if any(s['subject']==c['id'] for s in k['states'])])
    change(q,'Character',c['id'],'formal_relationship_refs',[r['id'] for r in REL if c['id'] in [r['source'],r['target']]])
for r in REL:
    change(q,'Relationship',r['id'],'formal_knowledge_refs',sorted(set(k for t in r['knowledge_navigation'] for k in tm[t])))
q=cr(26,'Stage2C/Timeline-Knowledge阶段回归','妮妮获救事件混入未来返国时标','ACCEPT',[[13529,13592],[15428,15441]],'EV0066正文是获救后的基地生活，返国计划在EV0163；不能让早节点带未来离境状态。',['EV0066','REL053','REL054','CH010','CH011'])
change(q,'Event','EV0066','time','蛾死后获救并进入基地；尚未到EV0163返国计划')
for r in REL:
    ss=copy.deepcopy(r['stages']);dirty=False
    for s in ss:
        if s['event']=='EV0066' and '卷二25当日返国' in s['story_phase']:s['story_phase']='当代中段；蛾死后获救进入基地，返国计划在EV0163';dirty=True
    if dirty:change(q,'Relationship',r['id'],'stages',ss)
# Persist controlled records; per-field before/after is the authority for this change set.
dump('canon/events/records.json',EV);dump('canon/characters/records.json',CH);dump('canon/relationships/records.json',REL);dump('canon/knowledge/records.json',K)
dump('canon/_stage2c/review_queue.json',queue);dump('canon/_stage2c/changes.json',changes)
print('Saved',len(queue),'CR;',len(changes),'field changes;',len(EV),'events')
