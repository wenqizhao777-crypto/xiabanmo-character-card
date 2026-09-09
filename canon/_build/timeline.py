from pathlib import Path
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[2]
CAN=ROOT/'canon'
SRC=ROOT/'source'/'下班，然后变成魔法少女_第1-282章.txt'
EV={x['id']:x for x in json.loads((ROOT/'audit'/'evidence_records.json').read_text(encoding='utf-8'))}
CH=json.loads((ROOT/'audit'/'chapter_index.json').read_text(encoding='utf-8'))
def add(rows,checkpoint):
 p=CAN/'events'/'records.json'; data=json.loads(p.read_text(encoding='utf-8'))
 for row in rows:
  # title, evidence IDs, time layer, tier, time, participants, before, occurrence, changes, knowledge edges, directed relationships, note
  title,refs,layer,tier,time,actors,before,occ,changes,know,rels,note=row
  eid=f'EV{len(data)+1:04d}'
  ids=refs.split(',');ranges=[[EV[x]['start'],EV[x]['end']] for x in ids]
  record=dict(id=eid,title=title,source_layer='NOVEL_TEXT',evidence_grade='A',status='CONFIRMED',audit_navigation=ids,source_ranges=ranges,time_layer=layer,time_tier=tier,time=time,participants=actors.split('、') if actors else [],witnesses='UNKNOWN：除发生字段明确写出的现场见闻外，不扩张目击名单。',later_informed='见知识传播；未列者UNKNOWN。',meaningfully_unaware='见知识传播与备注；不以名单缺席证明不知情。',before=before,occurrence=occ,direct_result=changes,long_term='仅沿关联事件跟踪；本项不另推未经证明的长期因果。',changes=changes,knowledge=know,relationships=rels,related_events=[],note=note,verification='AUDIT_LOCATED_SOURCE_RECHECK_PENDING')
  data.append(record)
 p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
 (CAN/'_build'/'checkpoint.json').write_text(json.dumps(dict(phase='TIMELINE_BUILDING',max_event_id=data[-1]['id'],next_source_line=checkpoint,unprocessed=f'L{checkpoint}—38825',note='候选节点已按原著状态组织，source_recheck_pending逐项回查后方可完成。'),ensure_ascii=False,indent=2),encoding='utf-8')
 print('saved',data[-len(rows)]['id'],data[-1]['id'],'next',checkpoint)

def add_text(text,checkpoint):
 rows=[]
 for line in text.strip().splitlines():
  if not line.strip():continue
  parts=line.split('|');assert len(parts)==12,(len(parts),line)
  title,refs,layer,tier,time,actors,before,occ,delta,k,rel,note=parts
  know=[]
  for edge in k.split(';'):
   if not edge:continue
   holder,topic,transition,via=edge.split('>');b,a=transition.split('→');know.append([holder,topic,b,a,via])
  relationships=[edge.split('>') for edge in rel.split(';') if edge]
  rows.append([title,refs,layer,tier,time,actors,before,occ,delta,know,relationships,note])
 add(rows,checkpoint)
