"""Read-only conservative knowledge lookup. No world-truth/other-character payload.
Run: python canon/knowledge/query_knowledge.py --character CH003 --event EV0036
Historical incomparable acquisitions remain denied; event numbers are not timestamps.
"""
from pathlib import Path
import json,argparse
HERE=Path(__file__).resolve().parent
def load(name):return json.loads((HERE/name).read_text(encoding='utf-8-sig'))
def context():
 events={r['id']:r for r in json.loads((HERE.parent/'events/records.json').read_text(encoding='utf-8-sig'))}
 edges=load('_build2b4/history_partial_order.json')['edges']
 return events,edges
def ancestors(event,edges):
 result={event}
 while True:
  added={a for a,b in edges if b in result}
  if added<=result:return result
  result|=added
HISTORY={9,10,37,50,51,52,53,58,79,81,95,111,118,141,142,143,144,145,146,147,148,165,166,167,168,169,176,177,178,180,181,182,183,184,185,187,189}
DENY={'UNAWARE','UNKNOWN','MEMORY_LOSS','FORGOTTEN'}
def lookup(character,event,before=False):
 records=load('records.json');events,edges=context()
 if event not in events:raise ValueError('未定义Event；请先明确Canon节点，不能按日期猜。')
 if character not in {f'CH{i:03}' for i in range(1,71)}:raise ValueError('未定义Character ID')
 epoch=events[event].get('knowledge_epoch', 'HISTORY' if int(event[2:]) in HISTORY else 'CURRENT')
 cutoff=(min(a for a,b in events[event]['source_ranges'])-1 if before else max(b for a,b in events[event]['source_ranges'])) if epoch=='CURRENT' else None
 hist_before=ancestors(event,edges)
 if before:hist_before.discard(event)
 dead=character=='CH006' and (epoch=='CURRENT' or 'EV0182' in hist_before)
 result={'character':character,'event':event,'position':'BEFORE' if before else 'AFTER','epoch':epoch,'read_only':True,'default_deny':True,'status':'DECEASED_NO_NEW_KNOWLEDGE' if dead else 'SCOPED_LOOKUP','allowed':[],'denied_or_unresolved':[],'warnings':['这是Canon参照查询；未选择RP开局，未改变角色卡。','输出不含客观真值、其他主体记录或完整源段；仅返回本主体有据的限定内容。','历史偏序不全时宁缺勿补；群体成员身份必须单独证实，本工具不自动继承G/ORG知识。','暂时性推测只返回其发生节点；已过时的事件事实必须保持过去时，不作为世界当前态。']}
 if dead:
  result['warnings'].append('安雅已故；生前事实可供作者参考，禁止继续生成她在死后接收的信息。');return result
 for r in records:
  own=[s for s in r['states'] if s['subject']==character];eligible=[]
  for s in own:
   tm=s['acquisition'];anchor=tm.get('history_anchor',s['event'])
   if epoch=='HISTORY':okay=tm['epoch']=='HISTORY' and anchor in hist_before
   else:okay=tm['epoch']=='HISTORY' or (tm['epoch']=='CURRENT' and tm['point'] is not None and tm['point']<=cutoff)
   if s.get('validity')=='EVENT_LOCAL' and s['event']!=event:okay=False
   if s.get('validity')=='HISTORICAL_BELIEF_ONLY':okay=False
   # Exact retained content of Tian's orphanage memories is unproved. Do not reconstruct it from facts.
   if character=='CH031' and epoch=='CURRENT' and cutoff>=10216 and s['event'] in ['EV0025','EV0026','EV0031']:
    okay=False
    result['denied_or_unresolved'].append({'knowledge_id':r['id'],'transition':s['id'],'state':'UNKNOWN_RETENTION','reason':'EV0170记忆缺口后未证还保留这部分早期现场信息；须有新的实际获知证据，不能回填。'})
   if okay:eligible.append(s)
  if not eligible:continue
  # Current acquisitions have exact local order; history uses only explicit predecessor edges.
  current=[s for s in eligible if s['acquisition']['epoch']=='CURRENT']
  if current:
   latest=max(s['acquisition']['point'] for s in current);selected=[s for s in current if s['acquisition']['point']==latest]
  else:
   selected=[]
   for s in eligible:
    anchor=s['acquisition'].get('history_anchor',s['event'])
    later=any(anchor!=t['acquisition'].get('history_anchor',t['event']) and anchor in ancestors(t['acquisition'].get('history_anchor',t['event']),edges) for t in eligible)
    if not later:selected.append(s)
  # A single event can contain a correction; explicit sequence disambiguates it, never raw list order.
  if len({s['event'] for s in selected})==1 and len(selected)>1:
   top=max(s.get('within_event_sequence',0) for s in selected)
   if top:selected=[s for s in selected if s.get('within_event_sequence',0)==top]
  if len({s['to_state'] for s in selected})>1:
   result['denied_or_unresolved'].append({'knowledge_id':r['id'],'reason':'获取时点存在不可自动排定的多个认知状态，先核子段，不选最终真值替代。','transitions':[s['id'] for s in selected]});continue
  for s in selected:
   payload=dict(knowledge_id=r['id'],transition=s['id'],state=s['to_state'],content=s['known_content'],source=s['source'],acquired_event=s['event'],as_of=s['acquisition']['description'],share='NO_AUTOMATIC_SHARING',validity=s['validity'])
   if s['to_state'] in DENY:
    payload['reason']='本状态不提供该秘密的肯定知识；不得用客观层补齐。';result['denied_or_unresolved'].append(payload)
   else:
    if s['to_state'] in ['MISUNDERSTANDS','BELIEVES','SUSPECTS','HEARD','PARTIAL','DISBELIEVES']:payload['render_as']='只能表达此主体的当时说法/理解/否定，不能输出为客观真相。'
    if s['acquisition']['epoch']=='HISTORY':payload['render_as']='作为此人过去亲历或接收的限定内容；不可宣称当时状态延续为如今现状。'
    result['allowed'].append(payload)
 return result
if __name__=='__main__':
 parser=argparse.ArgumentParser();parser.add_argument('--character',required=True);parser.add_argument('--event',required=True);parser.add_argument('--before',action='store_true');a=parser.parse_args()
 print(json.dumps(lookup(a.character,a.event,a.before),ensure_ascii=False,indent=2))
