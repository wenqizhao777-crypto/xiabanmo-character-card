from pathlib import Path
import json,copy
C=Path('canon');B=C/'_stage2c'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def put(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
Q=read(B/'review_queue.json');CC=read(B/'changes.json');RR=read(C/'relationships/records.json');r=RR[66];old=copy.deepcopy(r['stages'])
for s in r['stages']:s['claim_metadata']['text']=s['claim']
q=Q[16];entry=dict(id=f'CC{len(CC)+1:03}',review=q['id'],module='Relationship',record=r['id'],field='stages',before=old,after=copy.deepcopy(r['stages']),source_ranges=q['source_ranges'],reason='回归发现新增EV0055阶段的claim_metadata仍是旧短摘要；同步同一条已核证主张，等级不变。')
CC.append(entry);q['changes'].append(entry['id'])
put(C/'relationships/records.json',RR)
# New whole-record before/after, in addition to each logged field change.
for e in read(C/'events/records.json')[-3:]:
 q=next(x for x in Q if x['id']==e['integration_origin']);entry=dict(id=f'CC{len(CC)+1:03}',review=q['id'],module='Event',record=e['id'],field='__new_record__',before=None,after=e,source_ranges=q['source_ranges'],reason='补全新增稳定Event的整条新增前后像；编号追加且原189个不动。')
 CC.append(entry);q['changes'].append(entry['id'])
put(B/'review_queue.json',Q);put(B/'changes.json',CC)
print(len(Q),len(CC))
