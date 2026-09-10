from pathlib import Path
import ast,json,copy,re
P=Path.cwd();C=P/'canon';B=C/'_stage2c';ns=dict(P=P,C=C,B=B,json=json,copy=copy)
t=ast.parse((B/'integrate.py').read_text(encoding='utf-8'));exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helper','exec'),ns)
read=ns['read'];dump=ns['dump'];queue=read('canon/_stage2c/review_queue.json');changes=read('canon/_stage2c/changes.json')
EV=read('canon/events/records.json');CH=read('canon/characters/records.json');REL=read('canon/relationships/records.json');K=read('canon/knowledge/records.json')
E={r['id']:r for r in EV};H={r['id']:r for r in CH};R={r['id']:r for r in REL};Q={r['id']:r for r in K}
ns.update(E=E,H=H,R=R,Q=Q,EV=EV,queue=queue,changes=changes,evidence=read('audit/evidence_records.json'))
cr=ns['cr'];ch=ns['change'];tc=ns['textchange']
q=cr(30,'Stage2C/引用和未知回归','导航文字错指与历史修订后的有效入口','ACCEPT',[[38298,38396],[11281,11378]],'妮姆原代号不是母名；性别身份知识引用是K018，少女代号链K033；旧Review/TEMP保留为历史而非当前结论。',['REL025','K085','K169','导航文档'])
ch(q,'Relationship','REL025','boundary',R['REL025']['boundary'].replace('母名翠雀','妮姆原代号翠雀'))
ch(q,'Knowledge','K085','boundary',Q['K085']['boundary'].replace('反向020','反向K018'))
ch(q,'Knowledge','K169','boundary',Q['K169']['boundary'].replace('另连035','另连K033'))
q=cr(31,'Stage2C/Knowledge实际返回值回归','被否定命题的限定认知文本仍复述肯定句','ACCEPT',[[6798,6804],[35087,35100]],'K036和K156状态PARTIAL没有表达命题已被否定；角色可用文本应写实际观察及解释范围，不能把FALSE命题原句当其当前相信内容。',['K036','K156'])
for id,content in [('K036','我暗中接引白的魔力试过旧伤，没有可感知改善；不排除过于微小的效果，也不判断她未来永远无效。'),('K156','血蝠融入箭的身体后，她仍能凝符；我先前把完整人形当必要条件的推断不完整。这与箭整个人融进血蝠的状态不同。')]:
 ss=copy.deepcopy(Q[id]['states']);ss[0]['known_content']=content;ss[0]['correctness']='CORRECT_WITHIN_SCOPE';ch(q,'Knowledge',id,'states',ss)
# World downstream of CR028.
q=queue[27];q['targets'].append('WR002')
tc(q,'02_world_rules.md','红思与早期退役状态看不见→月圆节前异常被用作调查线索；祖母绿玩偶的加强遮蔽另属技术案例。','红思与表面退役、被旁人视为不能见妖精；实际早已受控改造并能与妮妮对话。月圆节林昀才发现她看见摩可的异常（L10619–10628、L11560–11627）；发现时间不是能力获得时间。祖母绿玩偶的加强遮蔽另属技术案例。')
# Source-confirmed listener correction also applies reverse narrative.
ss=copy.deepcopy(R['REL054']['stages']);ss[-1]['claim']='A：向翠雀说明返国与后续工具安排，并请求照护摩可；D：回述各自魔力源生于花园、共同成长，不是同一颗源。本段不是向摩可传讯。';ss[-1]['claim_metadata']['text']=ss[-1]['claim'];ch(queue[15],'Relationship','REL054','stages',ss)
# History new node is temporally after Anya death, not after source publication.
p=C/'knowledge/_build2b4/history_partial_order.json';old=json.loads(p.read_text(encoding='utf-8-sig'));new=copy.deepcopy(old)
if ['EV0182','EV0192'] not in new['edges']:
 new['edges'].append(['EV0182','EV0192']);p.write_text(json.dumps(new,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 entry=dict(id=f'CC{len(changes)+1:03}',review='CR024',module='Navigation',record='knowledge/_build2b4/history_partial_order.json',field='edges',before=old['edges'],after=new['edges'],source_ranges=[[12400,12412]],reason='亡妻之后的明示偏序；不根据源行排序其他历史支线。');changes.append(entry);queue[23]['changes'].append(entry['id'])
for mod,rows in [('events',EV),('characters',CH),('relationships',REL),('knowledge',K)]:dump(f'canon/{mod}/records.json',rows)
dump('canon/_stage2c/review_queue.json',queue);dump('canon/_stage2c/changes.json',changes)
print(len(queue),len(changes))
