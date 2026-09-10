from pathlib import Path
import ast,json,copy,re
P=Path.cwd();C=P/'canon';B=C/'_stage2c'
ns=dict(P=P,C=C,B=B,json=json,copy=copy)
t=ast.parse((B/'integrate.py').read_text(encoding='utf-8'))
exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helpers','exec'),ns)
read=ns['read'];dump=ns['dump'];queue=read('canon/_stage2c/review_queue.json');changes=read('canon/_stage2c/changes.json')
EV=read('canon/events/records.json');CH=read('canon/characters/records.json');REL=read('canon/relationships/records.json');K=read('canon/knowledge/records.json')
E={r['id']:r for r in EV};H={r['id']:r for r in CH};R={r['id']:r for r in REL};Q={r['id']:r for r in K}
ns.update(E=E,H=H,R=R,Q=Q,EV=EV,queue=queue,changes=changes,evidence=read('audit/evidence_records.json'))
cr=ns['cr'];change=ns['change'];tc=ns['textchange']
q=cr(27,'Stage2C/人物组织回归','四个考生的临时小队编号错置','ACCEPT',[[31815,31829],[30455,30480],[32465,32473],[32529,32536],[30560,30574]],'木棉及花烛在604；卷丹山丹与小锦在582；薄荷白玫小白在629。考核组队不等永久组织身份。',['CH052','CH054','CH055','CH056'])
for id,old,new in [('CH052','582','604'),('CH054','582','604'),('CH055','629','582'),('CH056','629','582')]:change(q,'Character',id,'org',H[id]['org'].replace(old,new))
q=cr(28,'Stage2C/早期快照联合回归','红思与表面退役状态覆盖真实受控改造期','ACCEPT',[[3540,3548],[10619,10628],[11560,11627]],'早期不能见妖精是旁人依据她自述形成的解释。她开篇前已与妮妮对话，受控两年。林昀到月圆节才发现异常，不能把发现时间当能力获得时间。',['CH005:S01','K052','K054','K216'])
ss=copy.deepcopy(H['CH005']['snapshots']);ss[0].update(身份='公开为退役朝颜／局方职员；实际已受摩丝控制改造',能力='原认证及正常少女能力已退役；兽化改造与妖精感知不可据表面退役状态抹去，尚未后来的治疗复归',伤势='表面成年日常体；隐藏受控改造已存在，不等健康普通人',认知='本人受控且禁思禁言；已能与妮妮交流。旁人尚按其退役自述理解，林昀至EV0049才发现能见摩可的异常')
change(q,'Character','CH005','snapshots',ss)
q=cr(29,'Stage2C/人物战绩回归','墨荷战绩的目标及事件混写','ACCEPT',[[35744,35800],[36034,36090],[36116,36129]],'EV0143是羽破界门、墨荷救出矢并救伤者；EV0145是蜂来袭和矢昙开，握今暂缓崩毁。不得把两场敌手合写。',['CH009','EV0143','EV0145'])
change(q,'Character','CH009','abilities',H['CH009']['abilities'].replace('历史协同矢车菊攻击羽（EV0145）','羽破界门时救出矢车菊并协助抢救同伴（EV0143）；蜂来袭、矢昙开后用握今暂缓其本相崩毁（EV0145）'))
# Synchronize dependent witness, reader and historical navigation fields under existing CR.
for qid,id,key,value in [(8,'EV0146','participants',['林昀','妖精及伤者']),(8,'EV0146','character_refs',['P_TEMP_001','P_TEMP_130']),(15,'EV0155','later_informed','本事件未发生亲子宣称；黑猫后来在EV0157获知D称谓，不提前到本节点。'),(16,'EV0163','witnesses','妮妮与翠雀厨房对话；本段没有摩可在场证据。'),(16,'EV0163','later_informed','翠雀听妮妮讲返国计划和园丁成长经历；不默认再传播给摩可。'),(16,'EV0163','character_refs',['P_TEMP_045','P_TEMP_004']),(18,'EV0037','later_informed','夏凉在当代EV0039听翠雀回述；并非参与历史组队或在历史节点已知。'),(22,'EV0187','character_refs',['P_TEMP_028','P_TEMP_027'])]:change(queue[qid-1],'Event',id,key,value)
change(queue[17],'Character','CH003','patterns',[x.replace('EV0037','EV0039') for x in H['CH003']['patterns']])
change(queue[16],'Relationship','REL067','formal_knowledge_refs',sorted(set(R['REL067']['formal_knowledge_refs']+['K187'])))
# Source-subject correction of added K017 node.
ss=copy.deepcopy(Q['K017']['states']);ss[-1]['source_subjects']=['CH001'];change(queue[20],'Knowledge','K017','states',ss)
# Lossless metadata logs for formal TEMP mapping and history graph.
def jsonfix(path,edit,q):
 before=read('canon/'+path);after=copy.deepcopy(before);edit(after)
 if before==after:return
 dump('canon/'+path,after);entry=dict(id=f'CC{len(changes)+1:03}',review=q['id'],module='Navigation',record=path,field='json',before=before,after=after,source_ranges=q['source_ranges'],reason=q['reason']);changes.append(entry);q['changes'].append(entry['id'])
def fixmap(rows):
 for r in rows:
  if r['temp']=='K_TEMP_019':r['stage2c_note']='CR021：K017-T002在EV0019已确认父早知；T001在EV0020补具体电视时点。原始导入文本保留。'
jsonfix('knowledge/temp_to_k.json',fixmap,queue[20])
# Epoch formal navigation re-evaluate corrected event references.
tm={x['temp']:x['formal_ids'] for x in read('canon/knowledge/temp_to_k.json')};rm={x['temp']:x['formal'] for x in read('canon/relationships/temp_to_rel.json')}
for e in EV:
 change(queue[24],'Event',e['id'],'formal_knowledge_refs',sorted({k for t in e['knowledge_refs'] for k in tm[t]}));change(queue[24],'Event',e['id'],'formal_relationship_refs',sorted({k for t in e['relationship_refs'] for k in rm[t]}))
for mod,rows in [('events',EV),('characters',CH),('relationships',REL),('knowledge',K)]:dump(f'canon/{mod}/records.json',rows)
dump('canon/_stage2c/review_queue.json',queue);dump('canon/_stage2c/changes.json',changes)
print(len(queue),len(changes))
