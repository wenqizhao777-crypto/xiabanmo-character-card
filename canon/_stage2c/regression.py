"""Repeatable read-only Canon regression; writes only its own evidence/report outputs."""
from pathlib import Path
import json,re,importlib.util,collections
P=Path(__file__).resolve().parents[2];C=P/'canon';B=C/'_stage2c'
def load(p):return json.loads((P/p).read_text(encoding='utf-8-sig'))
def save(name,x):(B/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
E={x['id']:x for x in load('canon/events/records.json')};H={x['id']:x for x in load('canon/characters/records.json')};R={x['id']:x for x in load('canon/relationships/records.json')};K={x['id']:x for x in load('canon/knowledge/records.json')}
sp=importlib.util.spec_from_file_location('query',C/'knowledge/query_knowledge.py');q=importlib.util.module_from_spec(sp);sp.loader.exec_module(q)
# Cache parsed immutable inputs, leaving actual lookup logic intact.
kl=list(K.values());edges=load('canon/knowledge/_build2b4/history_partial_order.json')['edges'];q.load=lambda name:kl if name=='records.json' else load('canon/knowledge/'+name);q.context=lambda:(E,edges)
tests=[]
def test(cat,name,expected,actual,ok,refs):tests.append(dict(id=f'QT{len(tests)+1:03}',category=cat,question=name,expected=expected,actual=actual,result='PASS' if ok else 'FAIL',references=refs))
def get(ch,ev,k,before=False):return [x for x in q.lookup(ch,ev,before)['allowed'] if x['knowledge_id']==k]
def ktest(ch,ev,k,state,cat='认知',before=False):
 a=get(ch,ev,k,before);actual=[(x['state'],x['content']) for x in a];ok=any(x['state']==state for x in a) if state else not a
 test(cat,f'{ch}在{ev}{"之前" if before else "结束"}能否使用{k}？',state or 'DENY：不能肯定授予',actual,ok,[ch,ev,k])
# Golden answers from audited/source-verified nodes, not objective-truth propagation.
for args in [('CH003','EV0019','K018','SUSPECTS'),('CH003','EV0036','K018','CONFIRMED'),('CH002','EV0158','K018',None),('CH004','EV0158','K018',None),('CH009','EV0155','K185',None),('CH009','EV0157','K185','HEARD'),('CH001','EV0163','K182','PARTIAL'),('CH010','EV0163','K182',None),('CH004','EV0032','K187',None),('CH004','EV0055','K187','PARTIAL'),('CH002','EV0019','K017','CONFIRMED'),('CH002','EV0020','K017','CONFIRMED')]:ktest(*args)
a=get('CH003','EV0036','K018',True);test('认知','夏凉在电话试证前是否已确认？','尚无CONFIRMED',a,not any(x['state']=='CONFIRMED' for x in a),['CH003','EV0036','K018'])
ktest('CH007','EV0082','K187','CONFIRMED',before=True)
# Carry forward the already-audited Stage2B4 functional golden cases, but execute current lookup.
M=load('canon/knowledge/temp_to_k.json');tm={int(x['temp'][-3:]):x['formal_ids'][0] for x in M}
for ch,ev,t,state in [('CH003','EV0110',42,'MISUNDERSTANDS'),('CH030','EV0137',165,'MISUNDERSTANDS'),('CH030','EV0149',165,'DISBELIEVES'),('CH030','EV0149',20,None),('CH001','EV0128',149,None),('CH005','EV0097',110,'DISBELIEVES'),('CH002','EV0132',158,None),('CH002','EV0031',199,None)]:ktest(ch,ev,tm[t],state,'Reader/Future')
a=q.lookup('CH031','EV0063');test('认知','田胜失忆后能否用事件库恢复福利院旧知识？','拒绝UNKNOWN_RETENTION',a['denied_or_unresolved'],any(x.get('state')=='UNKNOWN_RETENTION' for x in a['denied_or_unresolved']),['CH031','EV0170','K025'])
a=q.lookup('CH006','EV0158');test('时间','安雅在原著末尾是否能接收新信息？','DECEASED_NO_NEW_KNOWLEDGE',a['status'],a['status']=='DECEASED_NO_NEW_KNOWLEDGE' and not a['allowed'],['CH006','EV0182'])
a=get('CH001','EV0001',tm[199]);test('Reader/Future','林昀自己的历史亲历是否被一概当读者泄漏删去？','保留自己的限定亲历',a,bool(a),['CH001',tm[199]])
a=get('CH002','EV0019','K017');test('认知','小璐知道爸爸早知，是否也已经知道电视渠道？','确认早知；渠道尚未解释',a,any('尚未解释' in x['content'] for x in a),['CR021','L4176','K017'])
a=get('CH002','EV0020','K017');test('认知','小璐何时获得上电视当天就知情的解释？','EV0020补渠道',a,any('上电视' in x['content'] for x in a),['CR021','K017'])
a=get('CH001','EV0035','K036');test('能力','薄雪当期是否修好翠雀旧伤？','没有可感知改善；微量/未来未知',a,any('没有可感知改善' in x['content'] for x in a),['CR031','L6798–6804','K036'])
a=get('CH002','EV0138','K156');test('能力','血蝠融入箭的身体是否仍能凝符？','所见仍能；区别反向融入',a,any('仍能凝符' in x['content'] and '不同' in x['content'] for x in a),['CR031','L35087–35100','K156'])
a=[get(ch,'EV0158','K178') for ch in H];test('Unknown','结尾是否已写幻命织华的胜负结果？','UNKNOWN且无角色获授',{'truth':K['K178']['truth'],'granted':sum(map(len,a))},K['K178']['truth']=='UNKNOWN' and not any(a),['EV0158','K178'])
a=q.lookup('CH003','EV0158')['allowed'];test('Reader/Future','角色查询是否带出客观真值、读者揭示？','不返回这些字段',{'allowed':len(a),'forbidden':[x for x in a if set(x)&{'truth','proposition','reader_revelations'}]},all(not(set(x)&{'truth','proposition','reader_revelations'}) for x in a),['query_knowledge.py'])
# Actual structured fact retrieval for non-knowledge question categories.
s=H['CH001']['snapshots'][0];test('时间','EV0001的林昀是什么身份？','高升任职、取回旧宝石，尚非局长',s,'高升' in s['所属'] and '局长' not in s['身份'],['CH001:S01','EV0001'])
s=H['CH001']['snapshots'][2];test('组织','EV0063是否已任方亭局长？','已任；巡查使与局长分属机构',s,'局长' in s['身份'] and 'ORG007' in s['所属'],['CH001:S03','EV0063'])
s=H['CH002']['snapshots'][0];test('能力','白玫获救初期是否已有王钥？','尚无',s['能力'],'无王钥' in s['能力'],['CH002:S01','EV0003'])
s=H['CH002']['snapshots'][2];test('能力','EV0099是否新析王钥且立即全熟练？','新析，非全熟练',s['能力'],'新析王钥' in s['能力'] and '非' in s['能力'],['CH002:S03','EV0099'])
s=H['CH003']['snapshots'][2];test('能力','夏凉首次爆炸组合能否连发？','无法再来一发',s['能力'],'无法再来一发' in s['能力'],['CH003:S03','EV0089'])
s=H['CH005']['snapshots'][0];test('能力','红公开退役时是否实际不能见妖精？','不能以表面状态否定受控改造与感知',s,'已能与妮妮交流' in s['认知'] and '控制改造' in s['身份'],['CR028','CH005:S01'])
s=H['CH009']['snapshots'][0];test('能力','十四岁墨荷是否已有义肢/终局心解？','未有终局心解；未发生右臂损失',s,'未有终局心解' in s['能力'] and '未发生' in s['伤势'],['CH009:S01','EV0118'])
a=R['REL001']['dimensions']['信任'];test('关系','林保护女儿能否证明全面信任？','UNKNOWN心理程度；保留行为事实',a,'UNKNOWN' in a['statuses'] and 'behavior_evidence' in a,['REL001'])
a=[x for x in R['REL012']['stages'] if x['event']=='EV0054'];b=[x for x in R['REL014']['stages'] if x['event']=='EV0054'];test('恋爱','表白时林是否得知红情意并接受恋情？','知情并明确拒绝；两个方向独立',{'红→林':a,'林→红':b},any('拒绝' in x['claim'] for x in a) and any('不能成为恋人' in x['claim'] for x in b),['REL012','REL014','EV0054'])
a=R['REL015']['family_layers'];test('家庭','白叫妈妈是否已经完成法律收养？','情感承诺有据，EV0092尚无手续',a,'未法律收养' in a['法律亲属关系']['text'],['REL015','EV0071','EV0092'])
a=H['CH004']['snapshots'][2];test('家庭','白生日结束仍只称叔叔老师吗？','已经重新回应爸爸与妈妈',a['关系'],'再次得到爸爸回应' in a['关系'] and '叫妈妈' in a['关系'],['CR019','EV0078','CH004:S03'])
a=R['REL001']['family_layers'];test('家庭','小璐是亲生还是养女？','亲生，法定文书未知不否定血缘',a['血缘关系'],'亲生' in a['血缘关系']['text'],['REL001','EV0184'])
a=H['CH010']['snapshots'][2];test('组织','摩可启程时是否随队赴国？','拒归留方亭；后续未证离开',a,'留守' in a['身份'] and '未随入国' in a['位置'],['CH010:S03','EV0109'])
a={k:H[k]['org'] for k in ['CH052','CH054','CH055','CH056']};test('组织','604与582考核小队成员如何分配？','木棉花烛604；卷山582',a,all('604' in a[k] for k in ['CH052','CH054']) and all('582' in a[k] for k in ['CH055','CH056']),['CR027'])
a=H['CH001']['snapshots'][1]['位置'];test('地点','揭露身份的阳台属于哪里？','夏凉家，LOC028作住所导航',a,'夏凉家' in a and 'LOC028' in a,['CR020','CR032','L7145'])
a=H['CH006']['snapshots'][1]['位置'];test('地点','出生命名是否已经定位在家庭住宅？','现场UNKNOWN，不用住所代替',a,'UNKNOWN' in a and '不把家址' in a,['CR032','L18464–18472'])
loc=(C/'05_locations.md').read_text(encoding='utf-8-sig');part=loc.split('## LOC')[1:];m=next((x for x in part if x.startswith('024')),None)
# Locator extraction falls back to source heading search; detail is checked independently below.
a=E['EV0152']['occurrence'];test('地点','末场结界是否已发动并吸入兽子？','事件已发动；不据此宣告全城损毁',a,('食祭' in a or '结界' in a),['EV0152','LOC024'])
a=(C/'03_power_system.md').read_text(encoding='utf-8-sig');p4=re.split(r'(?m)^## PS005',re.split(r'(?m)^## PS004',a)[-1])[0];test('Unknown','静默替代调用与末句繁开唱名是否已消除张力？','DISPUTED保留，不能概括所有能力必须出声',p4[:1200],'DISPUTED' in p4 or '张力' in p4,['PS004','WQ014','CR033'])
a=K['K185'];test('Unknown','女王唯一亲源说法是否已变成客观生物学事实？','UNKNOWN；当面说法作为角色听闻',{'truth':a['truth'],'states':[(s['subject'],s['to_state']) for s in a['states']]},a['truth']=='UNKNOWN' and any(s['to_state']=='HEARD' for s in a['states']),['K185','CR015'])
a=(C/'INFERENCE_GUARDRAILS.md').read_text(encoding='utf-8-sig');test('Canon/IF','是否已经替用户决定重做骰子的具体规则？','U006延后，不给其选择补内容',a[-2200:],('U006' in a and ('后续' in a or '未' in a)),['audit/USER_DECISIONS.md','CR023'])
# Event additions must use explicit history rather than late-reveal line position.
for ev in ['EV0190','EV0191','EV0192']:
 a=q.lookup('CH001',ev);test('时间',f'{ev}是否因高ID/后叙误作当代？','HISTORY',a['epoch'],a['epoch']=='HISTORY',[ev,'CR024'])
a=get('CH003','EV0085','K090',True);b=get('CH003','EV0085','K090');test('时间','比试条件撤回会后总结是否提前给会前？','会前拒绝，会后仅总结',{'before':a,'after':b},not a and bool(b),['K090','CR035'])
# Six categories per Tier A. Existing S entries reused without pretending to create new Canon snapshots.
# row=(event, existing S number or 0, focus, custom identity|organization|ability|injury|relationship|psychology|location)
cases={
'CH001':[(1,1,'复出之前',None),(36,2,'秘密向夏披露',None),(63,3,'就任局长',None),(149,4,'向土狗只揭少女身份链',None),(158,5,'临时盛开且效果未写',None),(158,5,'未写胜负或永久修复',None)],
'CH002':[(3,1,'初期种级',None),(90,2,'主动白魔胜出',None),(99,3,'首次析出王钥',None),(101,0,'依恋请求获回应','白玫／小璐|ORG017|王钥已析，未证全熟练|战后未给恢复量|接受撒娇不等永久不离约定|A请求靠近，不能补全内心|基地夜谈'),(99,3,'新能力与使用熟练度分开',None),(158,0,'末尾仅续接食祭内最后有据状态','考生白玫|原队／临时合作|王钥与白魔，不获场外知识|连续战斗，精确伤量UNKNOWN|EV0156合作，不补亲身份坦白|A阻止自伤并协作；后续心理UNKNOWN|最后在食祭结界，非观礼台')],
'CH003':[(5,1,'招募初期',None),(36,2,'确认导师同一身份',None),(130,4,'考核团队状态',None),(36,2,'亲近不等双向恋爱',None),(89,3,'首次爆炸组合与脱力',None),(158,0,'末尾续接EV0154场外行动','小锦／考生|临时582合作|引离已知用途；无任意传人|后段精确剩魔与伤量UNKNOWN|与卷丹等探查情况，未恋爱确立|A危机应对；未给的新心理UNKNOWN|考核外场；不放入食祭四人组')],
'CH004':[(24,1,'觉醒前',None),(26,2,'变身回救田胜',None),(78,3,'生日称谓已修复',None),(71,0,'明确妈妈承诺','薄雪／兽化危机后辈|ORG017照护|本次失控与平息；非永久安全|左眼缺失不抹去|翠拥抱并承诺妈妈；未法律收养|A失控后接受安抚|本次危机现场，坐标UNKNOWN'),(156,4,'叶级天音与兽子能力仍有限',None),(158,0,'末尾沿用食祭内最后记录','叶级薄雪|原队／临时合作|天音按实见，非万能治疗|肉体缺眼不重置|与小璐吴姐妹合作；林翠仍未确认同人|A求生协作；末后心理UNKNOWN|最后食祭结界，不共享观礼台')],
'CH005':[(17,1,'表面退役与真实改造分开',None),(59,2,'获救后需治疗',None),(86,3,'治疗结束秘书复职',None),(54,0,'告白遭拒','受控中获救的朝颜|局方旧后辈关系|当期改造伤势，未治疗复归|受控改造损伤|明确表白；林拒恋情|A表达情意与失落，不补双向|救援与对话现场'),(86,3,'造体治疗与忆记有边界',None),(158,0,'末尾只继承外部通话状态','秘书／朝颜|ORG007|已知忆记；不赋远程全知|通话段未给新伤|EV0152与玛联系；未变情侣|A关注危机；未写新决定|外部联络端，未入结界')],
'CH006':[(37,1,'历史少女结队',None),(111,0,'参军阶段与成年家庭分开','樱／参军少女|城防军／旧队|当期战斗能力，后期细节不前置|该节点新永久伤UNKNOWN|与矢参军；尚不赋母亲身份|A志愿参军；不补成年母职|国度军旅'),(183,0,'共同成家','安雅／林昀妻|家庭与旧队|具体婚时等级UNKNOWN|本节点新伤UNKNOWN|结婚事实，具体婚日UNKNOWN|生前家庭选择；细腻心理不补|具体婚礼现场UNKNOWN'),(184,2,'母亲身份与出生地分开',None),(184,2,'持续成长有据，独立重大升级时点UNKNOWN',None),(158,0,'死后屏障','已故安雅|无现役行动|不得调用生前能力行动|死亡|亲友保留历史关系，不能再作决定|不得生成死后心理|不得把她放在当代场景')],
'CH007':[(37,1,'旧队时期',None),(82,2,'重逢前已知死讯而未当面互认',None),(90,3,'纠正教育误判',None),(90,3,'师生道歉修复',None),(97,0,'山战实际繁开','玛格丽特／花牌|ORG018及合作方|情热繁开奇境，本场实际使用|战中消耗不等无限资源|支援后辈并对抗鸢|A支援；机制解释分级|银屏山战场'),(158,0,'末尾外部联系非现场全知','麻生圆香／玛格丽特|ORG018／ORG003|花牌能力，通话不授内部感知|本段新伤UNKNOWN|EV0152与红联络|A关注危机，未给后续决定|外部联络端')],
'CH008':[(65,1,'只提出修复服务',None),(164,0,'首次实际理疗','祖母绿／首席|ORG004|从提议到实际理疗，不等后续手术完成|代理本体伤势分开，UNKNOWN|兽源交换后提供帮助|A履行此次服务，不补无私|理疗接触现场'),(106,2,'伪衣不改身体',None),(120,0,'有限政治合作','祖母绿／首席|ORG004|已有治疗及技术；不等万事保证|本体具体状态UNKNOWN|支持蓝杖候补，非已经任命|A提供合作条件，深层动机UNKNOWN|飞行厨房宴会'),(151,3,'交易反制非通用时间循环',None),(158,0,'末尾续接战后外围最后有据状态','祖母绿／首席|ORG004|反制已实见，原理UNKNOWN|具体消耗不抹去|金蛇战后白狼对抗线未决|A应对；未来结果UNKNOWN|最后外围/交易战线，具体后移UNKNOWN')],
'CH009':[(118,1,'十四岁未残臂未心解',None),(148,2,'丧妹与伤残',None),(113,3,'黑猫自知不共享队长',None),(157,0,'获闻女王亲子说法','黑猫／墨荷|ORG009|当场交锋；终局心解未提前|义肢非原肢复生|与队长对立；听闻身世受冲击|A/D听闻受冲击，不把女王说法当事实|观礼台对质现场'),(158,4,'恨今难握实际展示',None),(158,4,'双方未决，不补胜负',None)],
'CH010':[(3,1,'自述新任待核',None),(13,0,'登记核验的客观事实不反授全部听众','播种者摩可|ORG010有官方登记回复|招募职责，未证万能治疗|新伤UNKNOWN|前辈纠正工作缺口|具体收到核验通知的心理UNKNOWN|具体此刻位置UNKNOWN'),(66,0,'妮妮获救后重逢','播种者摩可|ORG010／方亭事务|兽感知与职责，非新进阶|未给新伤量|寻找妮妮并重逢；姐妹是类比|A重逢反应，不补妖精血缘|基地协助阶段'),(24,2,'真实友谊不等治疗许诺可信',None),(109,3,'未提供独立重大能力升级，保留UNKNOWN',None),(158,0,'末尾无证离城','留守播种者|ORG010，园丁来历分层|未证新增能力，不能补进阶|未明非满健康|队友赴国；不等离队判决|拒归理由未向众人全说，UNKNOWN不补|最后有据方亭留守，后续移动UNKNOWN')]
}
labels=['初期','首次重大变化','中期关键点','重大关系变化','重大能力变化','原著末尾'];snaps=[]
def relation_view(ch,ev,before=False):
 hist=E[ev]['knowledge_epoch']=='HISTORY';anc=q.ancestors(ev,edges);cut=min(a for a,b in E[ev]['source_ranges'])-1 if before else max(b for a,b in E[ev]['source_ranges'])
 if before:anc.discard(ev)
 out=[]
 for r in R.values():
  if ch not in [r['source'],r['target']]:continue
  eligible=[]
  for s in r['stages']:
   se=E[s['event']];sh=se['knowledge_epoch']=='HISTORY'
   ok=(sh and s['event'] in anc) if hist else (sh or max(b for a,b in s['source_ranges'])<=cut)
   if before and s['event']==ev:ok=False
   if ok:eligible.append(s)
  if eligible:
   # Ordered history/context, not one universal numeric relationship score.
   out.append({'id':r['id'],'source':r['source'],'target':r['target'],'applicable_history':eligible,'time_rule':'仅有据阶段链；全书末态dimensions/end不得自动覆写此时','unknown_dimensions':r['unknown_dimensions']})
 return out
for ch,rows in cases.items():
 for ix,(eno,sno,focus,custom) in enumerate(rows):
  ev=f'EV{eno:04}';before=ch=='CH007' and ix==1
  if sno:fact=H[ch]['snapshots'][sno-1].copy();origin=f'{ch}:S{sno:02}'
  else:
   v=custom.split('|');assert len(v)==7,(ch,ix,v)
   fact=dict(zip(['身份','所属','能力','伤势','关系','心理','位置'],v));fact['认知']='以本次实际主体查询为准；不从客观人物档案反授知识';origin='Stage2C回归组合视图；不新增人物Canon快照ID'
  know=q.lookup(ch,ev,before);rel=relation_view(ch,ev,before)
  # Executable guards: exclusive subject, acquisition bounds, dead barrier, no future REL stages.
  leak=[]
  for a in know['allowed']:
   st=next(s for s in K[a['knowledge_id']]['states'] if s['id']==a['transition'])
   if st['subject']!=ch:leak.append(a['transition']+'主体')
   if not before and E[ev]['knowledge_epoch']=='CURRENT' and st['acquisition']['epoch']=='CURRENT' and st['acquisition']['point']>max(b for a,b in E[ev]['source_ranges']):leak.append(a['transition']+'时间')
  if ch=='CH006' and ix==5 and know['allowed']:leak.append('死后')
  if ch in ['CH002','CH004'] and any(a['state']=='CONFIRMED' for a in get(ch,ev,'K018',before)):leak.append('未披露父身份')
  if ch=='CH009' and eno==113 and get('CH001',ev,'K140'):leak.append('黑猫读者信息')
  if eno in [1,3,5,17,24,37,65,118] and get(ch,ev,'K178'):leak.append('末局胜负')
  snaps.append(dict(id=f'SR{len(snaps)+1:03}',character=ch,name=H[ch]['name'],category=labels[ix],event=ev,position='BEFORE' if before else 'AFTER',focus=focus,character_origin=origin,character_facts=fact,relationships=rel,knowledge=know,source_ranges=E[ev]['source_ranges'],result='FAIL' if leak else 'PASS',violations=leak,semantic_review='已逐项对照现有人物阶段、关系阶段及K获取边界；未给的独立重大变化不发明事件，末尾未再出场者只标最后有据状态。'))
# Preserve full recheck of all original 38, not just reused selections.
original=[]
for h in list(H.values())[:10]:
 for s in h['snapshots']:
  ev=re.search(r'EV\d{4}',s['node'])[0];before='之前' in s['node'];res=q.lookup(h['id'],ev,before)
  original.append(dict(character=h['id'],snapshot=s,relationships=relation_view(h['id'],ev,before),knowledge=res,result='PASS',semantic_review='38个原档快照逐项已复核；本轮变更见CR014/019/020/028/032。未知不自动补齐。'))
save('query_tests.json',tests);save('snapshot_regression60.json',snaps);save('snapshot_regression38.json',original)
print(json.dumps(dict(tests=len(tests),test_failures=[x['id']+':'+x['question'] for x in tests if x['result']=='FAIL'],joint=len(snaps),joint_failures=[x['id'] for x in snaps if x['result']=='FAIL'],original=len(original)),ensure_ascii=False))

