from pathlib import Path
import ast,json,copy
P=Path.cwd();C=P/'canon';B=C/'_stage2c';ns=dict(P=P,C=C,B=B,json=json,copy=copy)
t=ast.parse((B/'integrate.py').read_text(encoding='utf-8-sig'));exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helper','exec'),ns)
read=ns['read'];dump=ns['dump'];queue=read('canon/_stage2c/review_queue.json');changes=read('canon/_stage2c/changes.json');K=read('canon/knowledge/records.json');Q={r['id']:r for r in K};ns.update(E={},H={},R={},Q=Q,queue=queue,changes=changes,evidence=read('audit/evidence_records.json'))
queue[32]['targets']=['PS004','PS017','WQ014','WQ020'];queue[32]['navigation_correction']='Stage 2C收尾：此前工作队列误指WQ003（认证任命），纠正为WQ014/WQ020；未改Canon结论。'
queue[33]['verification']='逐项对照既有未解记录及本轮变更前后；不声称无新源窗的事项做了新原文核证。'
q=ns['cr'](35,'Stage2C/查询粒度回归','同一Event内的提议与撤回必须标明查询粒度','ACCEPT',[[19586,19593],[19616,19637]],'撤回及听众反应明确；现有K090六个获取节点均为会后总结，不应声称已分别建模两次公布。事件前/后查询不可代替事件中段。',['K090','query_knowledge.py'])
ns['change'](q,'Knowledge','K090','boundary','EV0085跨提议至撤回；当前专属获取节点只登记撤回后的限定总结，不将整件事末态用于中段。不是国度统一资格制度；中段查询须按源行补核，不能从会后节点倒推。')
dump('canon/knowledge/records.json',K);dump('canon/_stage2c/review_queue.json',queue);dump('canon/_stage2c/changes.json',changes)
print(len(queue),len(changes))

