"""Structural, provenance, unknown, reference and protected-input checks. No Canon fact writes."""
from pathlib import Path
import json,re,hashlib,zipfile,collections,urllib.parse
P=Path(__file__).resolve().parents[2];C=P/'canon';B=C/'_stage2c';errors=[];checks=[]
def load(p):return json.loads((P/p).read_text(encoding='utf-8-sig'))
def check(ok,name,detail=None):
 checks.append(dict(name=name,status='PASS' if ok else 'FAIL',detail=detail))
 if not ok:errors.append({'name':name,'detail':detail})
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
D={m:load(f'canon/{m}/records.json') for m in ['events','characters','relationships','knowledge']};E={r['id']:r for r in D['events']};H={r['id']:r for r in D['characters']};R={r['id']:r for r in D['relationships']};K={r['id']:r for r in D['knowledge']};Z=zipfile.ZipFile(B/'canon_before.zip');old={m:json.loads(Z.read(f'canon/{m}/records.json').decode('utf-8-sig')) for m in D}
world={p:re.findall(r'(?m)^##\s+('+p+r'\d{3})\b',(C/f).read_text(encoding='utf-8-sig')) for p,f in [('WR','02_world_rules.md'),('PS','03_power_system.md'),('ORG','04_organizations.md'),('LOC','05_locations.md')]}
for m,p,width,n in [('events','EV',4,192),('characters','CH',3,70),('relationships','REL',3,172),('knowledge','K',3,235)]:
 ids=[r['id'] for r in D[m]];check(ids==[f'{p}{i:0{width}}' for i in range(1,n+1)],m+'_STABLE_IDS',{'count':len(ids),'expected':n});check(all(r['id']==D[m][i]['id'] for i,r in enumerate(old[m])),m+'_OLD_IDS_RETAINED')
for p,n in [('WR',14),('PS',38),('ORG',19),('LOC',36)]:check(world[p]==[f'{p}{i:03}' for i in range(1,n+1)],p+'_IDS',len(world[p]))
known=set(E)|set(H)|set(R)|set(K)|set(sum(world.values(),[]));bad=[]
for m,rows in D.items():
 for r in rows:
  for ref in set(re.findall(r'\b(?:EV\d{4}|CH\d{3}|REL\d{3}|K\d{3}|WR\d{3}|PS\d{3}|ORG\d{3}|LOC\d{3})\b',json.dumps(r,ensure_ascii=False))):
   if ref not in known:bad.append([m,r['id'],ref])
check(not bad,'FORMAL_REFERENCES_EXIST',bad)
A={e['id'] for e in load('audit/evidence_records.json')};ranges=[];ab=[]
def walk(o,path):
 if isinstance(o,dict):
  for k,v in o.items():
   if k in ['source_ranges','checked_anchors','review_context_ranges','revealed_at'] and isinstance(v,list):
    for pair in v:
     if not(isinstance(pair,list) and len(pair)==2 and all(isinstance(x,int) for x in pair) and 1<=pair[0]<=pair[1]<=38825):ranges.append([path,k,pair])
   if k in ['evidence_navigation','audit_navigation'] and isinstance(v,list):
    for e in v:
     if e not in A:ab.append([path,e])
   walk(v,path+'/'+k)
 elif isinstance(o,list):
  for i,v in enumerate(o):walk(v,path+'/'+str(i))
for m in D:walk(D[m],m)
check(not ranges,'ALL_SOURCE_WINDOWS_IN_BOUNDS',ranges);check(not ab,'AUDIT_EVIDENCE_TARGETS',ab)
# Stable dimensions, reverse edges are independent data, not copied symmetry.
bad=[]
for r in R.values():
 if r['source'] not in H or r['target'] not in H or len(r['dimensions'])!=10:bad.append(r['id']+'主体/维度')
 if r['reverse_id']:
  rr=R.get(r['reverse_id']);
  if not rr or rr['source']!=r['target'] or rr['target']!=r['source']:bad.append(r['id']+'reverse')
 if r['family_layers'] and len(r['family_layers'])!=7:bad.append(r['id']+'family')
 if [s['sequence'] for s in r['stages']]!=list(range(1,len(r['stages'])+1)):bad.append(r['id']+'sequence')
 for s in r['stages']:
  if s['event'] not in E or s['claim_metadata']['text']!=s['claim']:bad.append(r['id']+'stage')
check(not bad,'REL_172_DIRECTION_STAGE_FAMILY',bad)
check(sum(len(r['stages']) for r in R.values())==583,'REL_STAGE_COUNT_583');check(sum(bool(r['family_layers']) for r in R.values())==36,'FAMILY_LAYERS_COUNT_36')
# Unknown preservation, no silent upgrade for convenience.
bad=[];unknown_slots=0
for o in old['relationships']:
 for dim,v in o['dimensions'].items():
  if set(v['statuses'])&{'UNKNOWN','DISPUTED'}:
   unknown_slots+=1
   if not(set(R[o['id']]['dimensions'][dim]['statuses'])&{'UNKNOWN','DISPUTED'}):bad.append([o['id'],dim])
 for dim,v in o['family_layers'].items():
  if set(v['statuses'])&{'UNKNOWN','DISPUTED'} and not(set(R[o['id']]['family_layers'][dim]['statuses'])&{'UNKNOWN','DISPUTED'}):bad.append([o['id'],'family/'+dim])
for o in old['knowledge']:
 if o['truth'] in ['UNKNOWN','DISPUTED'] and K[o['id']]['truth']!=o['truth']:bad.append([o['id'],'truth'])
for o in old['characters']:
 for u in o.get('unknown',[]):
  if u not in H[o['id']].get('unknown',[]):bad.append([o['id'],'removed unknown',u])
check(not bad,'UNKNOWN_DISPUTED_PRESERVATION',{'old_REL_slots':unknown_slots,'changes':bad})
# Ensure every changed pre-existing record field has a CC entry.
changes=load('canon/_stage2c/changes.json');queue=load('canon/_stage2c/review_queue.json');mnames={'events':'Event','characters':'Character','relationships':'Relationship','knowledge':'Knowledge'};bad=[];fieldcount=0
for m,rows in old.items():
 now={r['id']:r for r in D[m]}
 for o in rows:
  for field in set(o)|set(now[o['id']]):
   if o.get(field)!=now[o['id']].get(field):
    fieldcount+=1
    cs=[c for c in changes if c['module']==mnames[m] and c['record']==o['id'] and c['field']==field]
    if not cs or cs[0]['before']!=o.get(field) or cs[-1]['after']!=now[o['id']].get(field):bad.append([m,o['id'],field,'missing before/after chain'])
    for a,b in zip(cs,cs[1:]):
     if a['after']!=b['before']:bad.append([m,o['id'],field,'broken chain'])
check(not bad,'ALL_CHANGED_RECORD_FIELDS_LOGGED',{'fields':fieldcount,'unlogged':bad})
check([c['id'] for c in changes]==[f'CC{i:03}' for i in range(1,len(changes)+1)],'CC_UNIQUE_CONTIGUOUS',len(changes))
check([q['id'] for q in queue]==[f'CR{i:03}' for i in range(1,len(queue)+1)],'CR_UNIQUE_CONTIGUOUS',len(queue));check(all(q['decision'] in ['ACCEPT','PARTIAL_ACCEPT','REJECT','KEEP_UNKNOWN','KEEP_DISPUTED','USER_DECISION_REQUIRED'] for q in queue),'QUEUE_DECISIONS_ENUM')
crs={q['id']:q for q in queue};check(all(c['review'] in crs and c['id'] in crs[c['review']]['changes'] for c in changes),'CC_CR_BIDIRECTIONAL_LINKS')
check(all(q['changes'] for q in queue if q['decision'] in ['ACCEPT','PARTIAL_ACCEPT']),'ACCEPTED_CHANGES_IMPLEMENTED')
G={g['id'] for g in load('canon/knowledge/groups.json')};states={'UNAWARE','EXPOSED','HEARD','SUSPECTS','BELIEVES','PARTIAL','CONFIRMED','MISUNDERSTANDS','DISBELIEVES','FORGOTTEN','MEMORY_LOSS','UNKNOWN'};bad=[];tids=[]
for k in K.values():
 if k['truth'] not in {'TRUE','FALSE','PARTIALLY_TRUE','DISPUTED','UNKNOWN'} or not k['default_deny'] or k['source_layer']!='NOVEL_TEXT':bad.append(k['id']+'truth/layer')
 for s in k['states']:
  tids.append(s['id'])
  if s['subject'] not in set(H)|G or s['from_state'] not in states or s['to_state'] not in states or s['event'] not in E:bad.append(s['id']+'state')
  if s['sharing']!='NO_AUTOMATIC_SHARING':bad.append(s['id']+'sharing')
  tm=s['acquisition']
  if tm['epoch']=='CURRENT' and not(isinstance(tm['point'],int) and 1<=tm['point']<=38825):bad.append(s['id']+'time')
  if tm['epoch']=='HISTORY' and tm.get('history_anchor',s['event']) not in E:bad.append(s['id']+'history anchor')
check(not bad,'K_STRUCTURE_TIME_SCOPE_DEFAULT_DENY',bad);check(len(tids)==365 and len(set(tids))==365,'K_365_UNIQUE_TRANSITIONS')
check(all(set(s['id'] for s in o['states'])<=set(s['id'] for s in K[o['id']]['states']) for o in old['knowledge']),'OLD_K_TRANSITION_IDS_RETAINED')
check(len({k['proposition'] for k in K.values()})==235,'K_NO_DUPLICATE_PROPOSITIONS')
M=load('canon/knowledge/temp_to_k.json');check(len(M)==207 and {x['temp'] for x in M}=={f'K_TEMP_{i:03}' for i in range(1,208)} and all(x['formal_ids'] and set(x['formal_ids'])<=set(K) for x in M),'ALL_207_TEMP_MAPPED')
edges=load('canon/knowledge/_build2b4/history_partial_order.json')['edges'];bad=[]
for a,b in edges:
 if a not in E or b not in E:bad.append([a,b,'unknown'])
 reach={b}
 while True:
  more={y for x,y in edges if x in reach}
  if more<=reach:break
  reach|=more
 if a in reach:bad.append([a,b,'cycle'])
check(not bad,'HISTORICAL_ORDER_ACYCLIC',bad);check(all(e['knowledge_epoch'] in ['CURRENT','HISTORY'] for e in E.values()),'ALL_192_EVENTS_HAVE_EXPLICIT_EPOCH')
qt=load('canon/_stage2c/query_tests.json');sr=load('canon/_stage2c/snapshot_regression60.json');s38=load('canon/_stage2c/snapshot_regression38.json')
check(len(qt)>=9 and all(t['result']=='PASS' for t in qt),'ACTUAL_QUERY_TESTS',{'count':len(qt),'failed':[t['id'] for t in qt if t['result']!='PASS']})
check(len(sr)==60 and all(s['result']=='PASS' for s in sr) and all(len([s for s in sr if s['character']==f'CH{i:03}'])==6 for i in range(1,11)),'SIX_JOINT_CATEGORIES_ALL_TIER_A',{'count':len(sr),'failed':[s['id'] for s in sr if s['result']!='PASS']})
check(len(s38)==38,'ALL_38_ORIGINAL_SNAPSHOTS_RECHECKED')
# Published layer links; historical work folders and historical Review files use original context, not current state.
files=[f for f in C.rglob('*.md') if not any(p.startswith('_') for p in f.relative_to(C).parts)];links=0;bad=[]
for f in files:
 text=f.read_text(encoding='utf-8-sig')
 for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',text):
  target=target.strip('<>');part=urllib.parse.unquote(target.split('#',1)[0]);line=None
  if re.match(r'\w+://',part):continue
  match=re.search(r':(\d+)$',part)
  if match:line=int(match[1]);part=part[:match.start()]
  links+=1;dest=(f.parent/part).resolve() if part else f
  if not dest.exists():bad.append([f.relative_to(P).as_posix(),target,'path']);continue
  anchor=target.split('#',1)[1] if '#' in target else ''
  if dest.suffix=='.txt' and (line or re.fullmatch(r'L\d+',anchor)):
   ln=line or int(anchor[1:])
   if not 1<=ln<=38825:bad.append([str(f),target,'line'])
  elif re.fullmatch(r'(?:ev\d+|k_temp_\d+|rel_temp_\d+|e\d+|cr\d+|cc\d+|wr\d+|ps\d+|org\d+|loc\d+)',anchor):
   dt=dest.read_text(encoding='utf-8-sig')
   if f'id="{anchor}"' not in dt and not re.search(r'^## '+anchor+r'(?:\s|$|｜)',dt,re.M|re.I):bad.append([f.relative_to(P).as_posix(),target,'anchor'])
check(not bad,'PUBLISHED_LINKS_AND_STABLE_ANCHORS',{'count':links,'bad':bad})
# Visible duplicate anchors can route a valid-looking link to stale facts.
badanchors=[]
for f in files:
 ids=re.findall(r'<a id="([^"]+)"',f.read_text(encoding='utf-8-sig'))
 dup=[a for a,n in collections.Counter(ids).items() if n>1]
 if dup:badanchors.append([f.relative_to(P).as_posix(),dup])
check(not badanchors,'PUBLISHED_HTML_ANCHORS_UNIQUE',badanchors)
tl=(C/'01_master_timeline.md').read_text(encoding='utf-8-sig')
check(re.findall(r'^## (EV\d{4})',tl,re.M)==list(E),'TIMELINE_EXACTLY_192_CURRENT_DETAILS')
relread=(C/'relationships/README.md').read_text(encoding='utf-8-sig');badrows=[]
for r in R.values():
 rows=[l for l in relread.splitlines() if l.startswith('|['+r['id']+']')]
 if len(rows)!=1 or rows[0].split('|')[6]!=str(len(r['stages'])-1):badrows.append(r['id'])
check(not badrows,'REL_DIRECTORY_STAGE_COUNTS_CURRENT',badrows)

base=load('canon/_stage2c/input_baseline.json');protected={p:h for p,h in base.items() if not p.startswith('canon/')};bad=[p for p,h in protected.items() if not (P/p).is_file() or sha(P/p)!=h];added=[p.relative_to(P).as_posix() for p in P.rglob('*') if p.is_file() and not p.relative_to(P).as_posix().startswith('canon/') and p.relative_to(P).as_posix() not in base]
check(not bad and not added,'ALL_NON_CANON_INPUT_HASHES_UNCHANGED',{'count':len(protected),'changed':bad,'added':added})
inputhash={p:sha(P/p) for p in protected if p.startswith(('source/','current/'))}
check(inputhash.get('source/下班，然后变成魔法少女_第1-282章.txt')=='18819c3060f411fd8bbb24e859657d24a7628317aed18c9106831f73eb250fa2','SOURCE_KNOWN_HASH');check(inputhash.get('current/260808.png')=='3d6a1d85f42d0980aac7ce9ff62f0a94d51f3c5c3272c3eaedf39ef1b8bd517d','CARD_KNOWN_HASH')
# Retained Review and TEMP import indexes must not be silently rewritten.
keep=[p for p in base if p.startswith('canon/') and (re.search(r'STAGE2[AB].*REVIEW\.md$',p) or p.endswith('TEMP_INDEX.md'))]
check(all((P/p).is_file() and sha(P/p)==base[p] for p in keep),'HISTORICAL_REVIEWS_TEMP_IMMUTABLE',keep)
counts={'events':len(E),'world':sum(map(len,world.values())),'characters':len(H),'relationships':len(R),'relationship_stages':sum(len(r['stages']) for r in R.values()),'family_records':sum(bool(r['family_layers']) for r in R.values()),'knowledge':len(K),'knowledge_transitions':len(tids),'query_tests':len(qt),'joint_scenarios':len(sr),'original_snapshots':len(s38),'CR':len(queue),'CC':len(changes),'character_unknown':sum(len(h.get('unknown',[])) for h in H.values()),'relationship_unknown_dimensions':sum(len(r['unknown_dimensions']) for r in R.values()),'knowledge_important_unknown':sum(k['important_unknown'] for k in K.values())}
out=dict(status='FAIL' if errors else 'PASS',checks=checks,errors=errors,counts=counts,links=links,input_hashes=inputhash,protected_files=len(protected),scope='全量结构/引用/变更链/哈希 + 60联合情境/38旧快照 + 55实际查询；语义判断来自Review逐条及事实逐项人工对照，不声称自动证明每句自然语言。')
(B/'check_result.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':out['status'],'checks':len(checks),'counts':counts,'errors':errors},ensure_ascii=False));raise SystemExit(bool(errors))
