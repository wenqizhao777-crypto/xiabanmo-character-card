"""Read-only Stage 3A.4 verification. Prints JSON; never updates frozen artifacts."""
from pathlib import Path
import hashlib,json,zipfile,copy,re,sys,importlib.util
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[2];C=ROOT/'canon';H=Path(__file__).resolve().parent
checks=[]
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(name,ok,detail=None):checks.append(dict(name=name,status='PASS' if ok else 'FAIL',detail=detail))
def files(root):return {p.relative_to(root).as_posix():sha(p) for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and '.git' not in p.parts and p.suffix!='.pyc'}
base=j(H/'input_hashes.json');now=files(ROOT)
allowed={'canon/'+p for p in ('README.md','BASELINE_MANIFEST.md','STAGE3A_PATCH_FOLLOWUPS.md','CHANGELOG_FUP3A001.md')}
changed={p for p,h in base.items() if now.get(p)!=h};new=set(now)-set(base)
check('only-four-existing-metadata-files-change',changed==allowed,sorted(changed))
check('new-files-scope',all(p.startswith('canon/_stage3a4/') or p=='canon/STAGE3A4_BASELINE_V1_2_FREEZE_REVIEW.md' for p in new),sorted(new))
protected={p:h for p,h in base.items() if p.split('/')[0] in {'source','audit','current','performance','final'}}
protectednow={p:h for p,h in now.items() if p.split('/')[0] in {'source','audit','current','performance','final'}}
check('all-protected-files-and-paths-unchanged',protected==protectednow,{d:sum(p.startswith(d+'/') for p in protected) for d in ('source','audit','current','performance','final')})
check('all-other-existing-files-unchanged',all(now.get(p)==h for p,h in base.items() if p not in allowed))
archives=zipfile.ZipFile(H/'before_metadata.zip')
for rel in sorted(allowed):
 name=rel.removeprefix('canon/');check('pre-freeze-backup:'+name,hashlib.sha256(archives.read(name)).hexdigest()==base[rel])
 for appenddoc in ('STAGE3A_PATCH_FOLLOWUPS.md','CHANGELOG_FUP3A001.md'):
  if name==appenddoc:
   original=archives.read(name).decode('utf-8-sig').replace('\r\n','\n');body=original.split('\n',1)[1].lstrip('\n')
   check('historical-body-retained:'+name,body in (C/name).read_text(encoding='utf-8-sig'))
# Replay old FUP exact post-images for all seven factual/navigation files.
z=zipfile.ZipFile(C/'_fup3a001/before.zip');ops=j(C/'_fup3a001/changes.json')
factual={'01_master_timeline.md','events/records.json','knowledge/records.json','knowledge/K018.md','knowledge/K098.md','knowledge/by_character/CH002_knowledge.md','knowledge/KNOWLEDGE_TRANSITIONS.md'}
for rel in sorted(factual):
 data=z.read('canon/'+rel).decode('utf-8-sig')
 if rel.endswith('.json'):
  obj=json.loads(data)
  for op in [x for x in ops if x['path']==rel]:
   if op['field']=='state_record':
    rec=next(r for r in obj if any(s['id']==op['record'] for s in r['states']));n=next(n for n,s in enumerate(rec['states']) if s['id']==op['record']);assert rec['states'][n]==op['before'];rec['states'][n]=op['after']
   else:
    rec=next(r for r in obj if r['id']==op['record']);assert rec[op['field']]==op['before'];rec[op['field']]=op['after']
  same=obj==j(C/rel)
 else:
  obj=data.replace('\r\n','\n').replace('\r','\n')
  for op in [x for x in ops if x['path']==rel]:assert obj.count(op['before'])==1;obj=obj.replace(op['before'],op['after'],1)
  same=obj==(C/rel).read_text(encoding='utf-8-sig')
 check('exact-approved-FUP-postimage:'+rel,same)
# Validate archived V1.1 before comparing stable IDs/truth to it.
m11=j(C/'_stage3a_patch/baseline_v1_1_manifest.json');az=zipfile.ZipFile(H/'baseline_v1_1_canon.zip')
check('V1.1-archive-hashes',all(hashlib.sha256(az.read(p)).hexdigest()==h for p,h in m11['files'].items()),len(m11['files']))
check('V1.1-archive-complete-including-exclusions',set(az.namelist())==set(m11['files'])|set(m11['excluded_self_or_dynamic']),len(az.namelist()))
check('V1.1-original-markdown-manifest',az.read('BASELINE_MANIFEST.md')==(H/'BASELINE_MANIFEST_V1_1.md').read_bytes()==z.read('canon/BASELINE_MANIFEST.md'))
check('V1-and-V1.1-original-artifacts-preserved',all(now[p]==h for p,h in base.items() if p.startswith(('canon/_stage2c/','canon/_stage3a_patch/','canon/_fup3a001/'))))
oldk=json.loads(az.read('knowledge/records.json').decode('utf-8-sig'));olde=json.loads(az.read('events/records.json').decode('utf-8-sig'))
k=j(C/'knowledge/records.json');e=j(C/'events/records.json');K={r['id']:r for r in k};E={r['id']:r for r in e};OK={r['id']:r for r in oldk}
check('stable-event-ids',len(e)==192 and [r['id'] for r in e]==[r['id'] for r in olde])
check('stable-knowledge-ids',len(k)==235 and [r['id'] for r in k]==[r['id'] for r in oldk])
tids=[s['id'] for r in k for s in r['states']];oldids=[s['id'] for r in oldk for s in r['states']]
check('stable-transition-ids',len(tids)==len(set(tids))==365 and tids==oldids)
check('all-knowledge-truth-top-grade-unchanged',all((r['truth'],r['grade'])==(OK[r['id']]['truth'],OK[r['id']]['grade']) for r in k))
check('all-acquisition-points-unchanged',[s['acquisition'] for r in k for s in r['states']]==[s['acquisition'] for r in oldk for s in r['states']])
s=next(s for s in K['K018']['states'] if s['id']=='K018-T005');t=next(s for s in K['K098']['states'] if s['id']=='K098-T001');nav=K['K098']['cross_references'][0]
check('EV0067-state',E['EV0067']['knowledge'][1][2:4]==['UNKNOWN','UNKNOWN'])
check('K018-T005-state',s['from_state']==s['to_state']=='UNAWARE' and s['knowledge_grade']=='A' and s['correctness']=='UNKNOWN')
check('K098-window-and-navigation',nav['point']==14075 and nav['subject']=='CH002' and nav['valid_until_transition']=='K098-T001' and bool(nav['known_content_fragment']) and t['acquisition']['point']==20884 and t['to_state']=='DISBELIEVES')
check('K098-original-transitions-unchanged',K['K098']['states']==OK['K098']['states'])
check('EV0092-unchanged',E['EV0092']==next(r for r in olde if r['id']=='EV0092'))
# Small real lookup smoke check; manual navigation not portrayed as automatic.
sp=importlib.util.spec_from_file_location('freeze_query',C/'knowledge/query_knowledge.py');q=importlib.util.module_from_spec(sp);sp.loader.exec_module(q)
for ev,before in [('EV0067',True),('EV0067',False),('EV0092',True),('EV0092',False),('EV0158',False)]:
 data=q.lookup('CH002',ev,before);check('no-identity-grant:'+ev+':'+str(before),not any(x['knowledge_id']=='K018' for x in data['allowed']))
check('romance-correction-query',any(x['knowledge_id']=='K098' and x['state']=='DISBELIEVES' for x in q.lookup('CH002','EV0092')['allowed']))
check('early-K098-still-manual',not any(x['knowledge_id']=='K098' for x in q.lookup('CH002','EV0067')['allowed']))
# Sync content checks augment the recorded semantic review, not a claim of model execution.
perf=(ROOT/'performance/tier_a/CH002_林小璐_performance.md').read_text(encoding='utf-8-sig')
val=(ROOT/'performance/validation/CH002_validation.md').read_text(encoding='utf-8-sig')
sync=(ROOT/'performance/STAGE3A3_CH002_SYNC_REVIEW.md').read_text(encoding='utf-8-sig')
check('sync-final-conclusion',all(x in sync for x in ('REJECT_CAUSAL_INTERPRETATION','RESOLVED','本轮完成')))
check('sync-actual-state-and-navigation',all(x in perf for x in ('UNAWARE → UNAWARE','K098.cross_references','14075','UNKNOWN','E193','20／2','26／2','此处没有默认反应可用')))
check('rejected-mechanism-explicitly-deleted','已删除的第五条' in perf and '整条删除' in perf)
check('no-pending-mechanism-execution-tag',not re.search(r'INTERPRETIVE_MODEL[^\n]{0,35}待核|待核[^\n]{0,35}INTERPRETIVE_MODEL',perf))
A=val.split('## A.')[1].split('## B.')[0];B=val.split('## B.')[1].split('## C.')[0];D=val.split('## C.')[1].split('## D.')[0]
aheads=re.findall(r'^### (A\d[^｜]*)｜',A,re.M);bheads=re.findall(r'^### (B\d[^｜]*)｜',B,re.M);holds=re.findall(r'^\|(\d+)\|.*?`HOLD`\|$',D,re.M)
check('recorded-Canon-scenes-seven-all-pass',len(aheads)==7 and len(re.findall(r'\*\*判定：`PASS`',A))==7,aheads)
check('recorded-Novel-scenes-five-all-pass',len(bheads)==5 and len(re.findall(r'\*\*判定：`PASS`',B))==5,bheads)
check('recorded-OOC-fifteen-hold',holds==[str(i) for i in range(1,16)],holds)
check('old-OOC8-withdrawn','旧判据' in D and '已撤回' in D)
review=(C/'STAGE3A4_BASELINE_V1_2_FREEZE_REVIEW.md').read_text(encoding='utf-8-sig')
check('sync-count-discrepancy-disclosed','6/6' in review and '7项' in review and '7个既有文件' in review)
for rel in ('README.md','BASELINE_MANIFEST.md','CHANGELOG_FUP3A001.md','STAGE3A_PATCH_FOLLOWUPS.md','STAGE3A4_BASELINE_V1_2_FREEZE_REVIEW.md'):
 text=(C/rel).read_text(encoding='utf-8-sig');check('current-version-and-FUP:'+rel,all(x in text[:7000] for x in ('CANON_BASELINE_V1.2 = FROZEN','RESOLVED','REJECT_CAUSAL_INTERPRETATION')))
check('change-id-consistency',all('FZ3A4-001' in (C/r).read_text(encoding='utf-8-sig') for r in ('README.md','BASELINE_MANIFEST.md','CHANGELOG_FUP3A001.md','STAGE3A4_BASELINE_V1_2_FREEZE_REVIEW.md')))
m=j(H/'baseline_v1_2_manifest.json');excluded=set(m['excluded_self_or_dynamic']);canonnow=files(C)
check('V1.2-version-status',m['version']=='V1.2' and m['status']=='FROZEN')
check('manifest-coverage-no-omissions',set(m['files'])==set(canonnow)-excluded,dict(covered=len(m['files']),excluded=sorted(excluded)))
check('V1.2-file-hashes',all(canonnow.get(p)==h for p,h in m['files'].items()))
check('no-unlisted-exclusions',excluded=={'BASELINE_MANIFEST.md','_stage3a4/baseline_v1_2_manifest.json','_stage3a4/verification.json'})
links=[];errors=[]
for rel in [p.removeprefix('canon/') for p in allowed]+['STAGE3A4_BASELINE_V1_2_FREEZE_REVIEW.md']:
 text=(C/rel).read_text(encoding='utf-8-sig')
 for dest in re.findall(r'\]\(([^)]+)\)',text):
  dest=dest.strip().strip('<>').split('#')[0]
  if not dest or dest.startswith(('http:','https:')):continue
  dest=re.sub(r':\d+$','',dest);target=(C/rel).parent/dest;links.append([rel,dest])
  if not target.is_file() and target.resolve()!=(H/'verification.json').resolve():errors.append([rel,dest])
check('metadata-local-file-links',not errors,dict(count=len(links),errors=errors))
failed=[x for x in checks if x['status']=='FAIL']
res=dict(stage='Stage 3A.4',status='PASS' if not failed else 'FAIL',version='V1.2',baseline_state='FROZEN' if not failed else 'VERIFICATION_FAILED',fup='RESOLVED',conclusion='REJECT_CAUSAL_INTERPRETATION',checks=checks,passed=len(checks)-len(failed),failed=len(failed),input_files=len(base),unchanged_existing_files=len(base)-len(changed),changed_existing_files=sorted(changed),new_files=sorted(new),protected_files=len(protected),manifest_files=len(m['files']),hashes={'markdown_manifest':sha(C/'BASELINE_MANIFEST.md'),'machine_manifest':sha(H/'baseline_v1_2_manifest.json')},scope='Read-only freeze checks; recorded Performance cases reviewed, no fresh model/runtime execution; no full Stage2C rerun')
print(json.dumps(res,ensure_ascii=False,indent=2))
raise SystemExit(1 if failed else 0)
