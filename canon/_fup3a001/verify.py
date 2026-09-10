"""Local FUP-3A-001 regression. Writes only this directory/verification.json.
Cross-reference checks implement the documented manual navigation contract;
they do not claim automatic support in the unchanged production query engine.
"""
from pathlib import Path
import copy, hashlib, importlib.util, json, re, sys, zipfile
sys.dont_write_bytecode = True
ROOT=Path(__file__).resolve().parents[2]; CANON=ROOT/'canon'; HERE=Path(__file__).resolve().parent
checks=[]
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def norm(s): return s.replace('\r\n','\n').replace('\r','\n')
def check(name, okay, detail=None):
 checks.append(dict(check=name,status='PASS' if okay else 'FAIL',detail=detail))
def index(rs): return {r['id']:r for r in rs}
base=read(HERE/'input_hashes.json'); changes=read(HERE/'changes.json')
archive=zipfile.ZipFile(HERE/'before.zip')
def oldjson(p): return json.loads(archive.read('canon/'+p).decode('utf-8-sig'))
old_e=oldjson('events/records.json'); old_k=oldjson('knowledge/records.json')
e=read(CANON/'events/records.json'); k=read(CANON/'knowledge/records.json'); E=index(e); K=index(k)
OE=index(old_e); OK=index(old_k)
allowed={'canon/'+x['path'] for x in changes}
actual={p for p,h in base.items() if not (ROOT/p).is_file() or sha(ROOT/p)!=h}
check('existing-file-change-allowlist',actual==allowed,dict(changed=sorted(actual),allowed=sorted(allowed)))
check('old-byte-archive-authentic',all(hashlib.sha256(archive.read(p)).hexdigest()==base[p] for p in archive.namelist()))
protected={p:h for p,h in base.items() if p.split('/')[0] in ('source','current','audit','performance','final')}
check('protected-inputs-byte-identical',all((ROOT/p).is_file() and sha(ROOT/p)==h for p,h in protected.items()),dict(files=len(protected),by_directory={d:sum(p.startswith(d+'/') for p in protected) for d in ('source','current','audit','performance','final')}))
allnow={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and '.git' not in p.parts}
new=allnow-set(base)
check('no-new-files-outside-approved-canon-review',all(p in {'canon/FUP3A001_REVIEW.md','canon/CHANGELOG_FUP3A001.md'} or p.startswith('canon/_fup3a001/') for p in new),sorted(new))
check('sequential-local-patch-ids',[c['patch_id'] for c in changes]==[f'F3A2-{i:03}' for i in range(1,26)])
# Replay each recorded operation over exact prior bytes/JSON, ensuring every effective edit is logged.
replayed={}
for p in sorted(allowed):
 rel=p.removeprefix('canon/'); ops=[c for c in changes if c['path']==rel]
 obj=oldjson(rel) if p.endswith('.json') else norm(archive.read(p).decode('utf-8-sig'))
 for c in ops:
  field=c['field']
  if field=='text':
   check(c['patch_id']+'-unique-before',obj.count(c['before'])==1)
   obj=obj.replace(c['before'],c['after'],1)
  elif field=='append': obj=obj.rstrip()+'\n\n'+c['after'].rstrip()+'\n'
  else:
   if field=='state_record':
    r=next(r for r in obj if any(s['id']==c['record'] for s in r['states'])); j=next(j for j,s in enumerate(r['states']) if s['id']==c['record'])
    check(c['patch_id']+'-before',r['states'][j]==c['before']);r['states'][j]=copy.deepcopy(c['after'])
   else:
    r=next(r for r in obj if r['id']==c['record']);check(c['patch_id']+'-before',r[field]==c['before']);r[field]=copy.deepcopy(c['after'])
 expected=read(ROOT/p) if p.endswith('.json') else norm((ROOT/p).read_text(encoding='utf-8-sig'))
 check('full-log-replay:'+p,obj==expected)
check('event-count-and-stable-order',len(e)==192 and [x['id'] for x in e]==[x['id'] for x in old_e])
check('knowledge-count-and-stable-order',len(k)==235 and [x['id'] for x in k]==[x['id'] for x in old_k])
check('transition-ids-and-order', [s['id'] for r in k for s in r['states']]==[s['id'] for r in old_k for s in r['states']] and sum(len(r['states']) for r in k)==365)
check('all-knowledge-truth-and-top-grade-unchanged',all((r['truth'],r['grade'])==(OK[r['id']]['truth'],OK[r['id']]['grade']) for r in k))
check('all-other-events-unchanged',all(r==OE[r['id']] for r in e if r['id']!='EV0067'))
check('EV0067-only-two-fields', {a for a in E['EV0067'] if E['EV0067'][a]!=OE['EV0067'][a]}=={'later_informed','knowledge'})
check('EV0067-white-chain-unchanged',E['EV0067']['knowledge'][0]==OE['EV0067']['knowledge'][0])
check('EV0067-no-guessed-identity',E['EV0067']['knowledge'][1][2:4]==['UNKNOWN','UNKNOWN'])
check('all-other-knowledge-records-unchanged',all(r==OK[r['id']] for r in k if r['id'] not in {'K018','K098'}))
s=next(s for s in K['K018']['states'] if s['id']=='K018-T005'); os=next(v for v in OK['K018']['states'] if v['id']=='K018-T005')
check('K018-only-T005-content',all(K['K018'][f]==OK['K018'][f] for f in K['K018'] if f!='states') and all(t==next(v for v in OK['K018']['states'] if v['id']==t['id']) for t in K['K018']['states'] if t['id']!='K018-T005'))
allowed_state_fields={'from_state','to_state','known_content','source','observation','interpretation','knowledge_grade','certainty','correctness'}
check('T005-only-authorized-fields',{f for f in s if s[f]!=os[f]}<=allowed_state_fields)
check('T005-unaware-and-unmodified-time',s['from_state']==s['to_state']=='UNAWARE' and s['acquisition']==os['acquisition'] and s['acquisition']['point']==14075)
check('K098-only-navigation',all(K['K098'][f]==OK['K098'][f] for f in K['K098'] if f!='cross_references'))
t=K['K098']['states'][0]; nav=K['K098']['cross_references'][0]; onav=OK['K098']['cross_references'][0]
check('K098-correction-and-truth-unchanged',t==OK['K098']['states'][0] and t['id']=='K098-T001' and t['from_state']=='MISUNDERSTANDS' and t['to_state']=='DISBELIEVES' and t['acquisition']['point']==20884 and K['K098']['truth']==OK['K098']['truth'])
check('navigation-old-anchor-and-end-unchanged',all(nav[f]==onav[f] for f in ('kind','knowledge_id','transition_id','subject','event','point','valid_until_transition','source_ranges')))
check('navigation-explicit-subject-belief',nav['subject']=='CH002' and nav['kind']=='ORIGIN_NAVIGATION_ONLY' and bool(nav['known_content_fragment']))
charpaths=[p for p in base if p.startswith('canon/characters/')]
relpaths=[p for p in base if p.startswith('canon/relationships/')]
check('all-character-files-and-original-snapshots-unchanged',all(sha(ROOT/p)==base[p] for p in charpaths),len(charpaths))
check('all-directed-relationship-files-unchanged',all(sha(ROOT/p)==base[p] for p in relpaths),len(relpaths))
check('production-query-engine-unchanged',sha(CANON/'knowledge/query_knowledge.py')==base['canon/knowledge/query_knowledge.py'])
spec=importlib.util.spec_from_file_location('fup_query',CANON/'knowledge/query_knowledge.py');q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
original_load=q.load
snapshots={}
for ev in ('EV0003','EV0036','EV0050','EV0067','EV0078','EV0090','EV0092','EV0099','EV0117','EV0156','EV0158'):
 for before in (False,True):
  now=q.lookup('CH002',ev,before)
  q.load=lambda name: old_k if name=='records.json' else original_load(name)
  prev=q.lookup('CH002',ev,before);q.load=original_load
  check(f'query-no-identity-grant:{ev}:{before}',not any(x['knowledge_id']=='K018' for x in now['allowed']))
  def without_target(out):
   z=copy.deepcopy(out)
   for field in ('allowed','denied_or_unresolved'):z[field]=[x for x in z[field] if x.get('transition')!='K018-T005']
   return z
  check(f'query-only-controlled-delta:{ev}:{before}',without_target(now)==without_target(prev))
  if not before and ev in ('EV0003','EV0090','EV0099','EV0156'):snapshots[ev]=[len(now['allowed']),len(now['denied_or_unresolved'])]
check('profile-snapshot-query-counts',snapshots=={'EV0003':[3,0],'EV0090':[20,2],'EV0099':[26,2],'EV0156':[44,2]},snapshots)
profile=(CANON/'knowledge/by_character/CH002_knowledge.md').read_text(encoding='utf-8-sig')
check('profile-rendered-counts',all(re.search(r'EV'+ev[2:]+r'.*?返回'+str(a)+r'条状态，拦截/待核'+str(d)+r'条',profile) for ev,(a,d) in snapshots.items()))
# Use live query output for correction; early manual fragment comes solely from K098 nav.
def manual_projection(ch,ev,before=False):
 out=q.lookup(ch,ev,before)
 if ch!=nav['subject'] or out['epoch']!='CURRENT':return 'NONE'
 cutoff=min(a for a,b in E[ev]['source_ranges'])-1 if before else max(b for a,b in E[ev]['source_ranges'])
 actual=[v for v in out['allowed'] if v['knowledge_id']=='K098']
 if cutoff>=t['acquisition']['point']:
  return 'CORRECTION' if any(v['transition']=='K098-T001' and v['state']=='DISBELIEVES' for v in actual) else 'FAIL_NO_CORRECTION'
 if cutoff>=nav['point'] and nav['known_content_fragment']:return 'FRAGMENT'
 return 'NONE'
for ch,ev,before,expect in [('CH002','EV0003',False,'NONE'),('CH002','EV0067',True,'NONE'),('CH002','EV0067',False,'FRAGMENT'),('CH002','EV0078',False,'FRAGMENT'),('CH002','EV0090',False,'FRAGMENT'),('CH002','EV0092',True,'FRAGMENT'),('CH002','EV0092',False,'CORRECTION'),('CH002','EV0117',False,'CORRECTION'),('CH010','EV0067',False,'NONE'),('CH002','EV0050',False,'NONE')]:
 got=manual_projection(ch,ev,before);check(f'manual-navigation:{ch}:{ev}:{before}',got==expect,dict(expected=expect,actual=got))
check('query-does-not-auto-project-early-K098',not any(v['knowledge_id']=='K098' for v in q.lookup('CH002','EV0067')['allowed']))
for ch in ('CH001','CH003','CH010'):
 for ev in ('EV0036','EV0067','EV0092','EV0158'):
  now=q.lookup(ch,ev);q.load=lambda name: old_k if name=='records.json' else original_load(name)
  prev=q.lookup(ch,ev);q.load=original_load
  check(f'other-subject-query-identical:{ch}:{ev}',now==prev)
# Existing frozen manifest remains historical: account for expected patch deltas, not refreeze.
m=read(CANON/'_stage3a_patch/baseline_v1_1_manifest.json')
manifest_deltas={p for p,h in m['files'].items() if not (CANON/p).is_file() or sha(CANON/p)!=h}
check('historical-v1.1-machine-manifest-unchanged',sha(CANON/'_stage3a_patch/baseline_v1_1_manifest.json')==base['canon/_stage3a_patch/baseline_v1_1_manifest.json'])
check('v1.1-deltas-exactly-authorized',manifest_deltas=={p.removeprefix('canon/') for p in allowed if p.removeprefix('canon/') in m['files']},sorted(manifest_deltas))
for name in ('README.md','BASELINE_MANIFEST.md'):
 txt=(CANON/name).read_text(encoding='utf-8-sig');check('current-baseline-banner:'+name,'Stage 3A.2' in txt[:1400] and 'V1.2' in txt[:1400])
# Validate local file links in changed documents and new reports. Anchor resolution is not asserted.
link_errors=[];linkcount=0
for rel in sorted(allowed|{'canon/FUP3A001_REVIEW.md','canon/CHANGELOG_FUP3A001.md'}):
 if not rel.endswith('.md'):continue
 text=(ROOT/rel).read_text(encoding='utf-8-sig')
 for dest in re.findall(r'\]\(([^)]+)\)',text):
  dest=dest.strip().strip('<>')
  if dest.startswith(('http:','https:','#','app:')):continue
  dest=dest.split('#')[0]
  if not dest:continue
  dest=re.sub(r':\d+$','',dest);target=Path(dest) if Path(dest).is_absolute() else (ROOT/rel).parent/dest
  linkcount+=1
  if not target.is_file() and target.resolve() != (HERE/'verification.json').resolve():link_errors.append([rel,dest])
check('changed-report-local-file-links',not link_errors,dict(checked=linkcount,errors=link_errors))
# Source anchor checks supplement semantic review; they do not replace it.
source=ROOT/'source/下班，然后变成魔法少女_第1-282章.txt';sl=source.read_text(encoding='utf-8-sig').splitlines()
check('source-content-hash',sha(source)=='18819c3060f411fd8bbb24e859657d24a7628317aed18c9106831f73eb250fa2')
for a,b,words in [(4190,4196,['夏凉']),(4230,4255,['手机']),(7194,7198,['一个人']),(13780,13785,['因为我就是翠雀']),(13844,13854,['父亲']),(20800,20805,['恋爱'])]:
 piece='\n'.join(sl[a-1:b]);check(f'source-anchor:{a}-{b}',all(w in piece for w in words))
check('followup-resolved',(CANON/'STAGE3A_PATCH_FOLLOWUPS.md').read_text(encoding='utf-8-sig').count('REJECT_CAUSAL_INTERPRETATION')>=1 and 'RESOLVED' in (CANON/'STAGE3A_PATCH_FOLLOWUPS.md').read_text(encoding='utf-8-sig'))
check('review-formal-conclusion',all(w in (CANON/'FUP3A001_REVIEW.md').read_text(encoding='utf-8') for w in ('REJECT_CAUSAL_INTERPRETATION','APPLIED_MINIMAL_CORRECTION','PERFORMANCE_SYNC_REQUIRED = YES','RESOLVED')))
failed=[x for x in checks if x['status']=='FAIL']
result=dict(task='FUP-3A-001',date='2026-09-11',status='PASS' if not failed else 'FAIL',checks=checks,passed=len(checks)-len(failed),failed=len(failed),original_files=len(base),original_files_unchanged=len(base)-len(actual),modified_existing_files=sorted(actual),protected_files=len(protected),new_files=sorted(new),counts=dict(events=len(e),knowledge=len(k),transitions=sum(len(r['states']) for r in k)),snapshots=snapshots,historical_v1_1_expected_deltas=sorted(manifest_deltas),scope='Local static/data/query regression. Manual-navigation contract checked separately. No Performance edits, model generation, human acceptance or new baseline freeze.')
(HERE/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({a:result[a] for a in ('status','passed','failed','original_files','original_files_unchanged','protected_files','snapshots','historical_v1_1_expected_deltas')},ensure_ascii=False,indent=2))
for fail in failed: print(json.dumps(fail,ensure_ascii=False))
raise SystemExit(1 if failed else 0)
