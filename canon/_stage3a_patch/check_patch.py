"""Local four-request checks; writes only this patch's evidence. Does not rerun Stage2C builders."""
from pathlib import Path
import json,hashlib,zipfile,re,importlib.util,sys,collections,urllib.parse
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parents[2];C=P/'canon';B=C/'_stage3a_patch';BASE=json.loads((B/'input_baseline.json').read_text(encoding='utf-8'));Z=zipfile.ZipFile(B/'baseline_v1_canon.zip');checks=[]
def load(p):return json.loads((C/p).read_text(encoding='utf-8-sig'))
def old(p):return json.loads(Z.read('canon/'+p).decode('utf-8-sig'))
def ck(name,ok,detail=None):checks.append(dict(name=name,status='PASS' if ok else 'FAIL',detail=detail))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
D={m:load(m+'/records.json') for m in ['events','characters','relationships','knowledge']};O={m:old(m+'/records.json') for m in D};H={x['id']:x for x in D['characters']};K={x['id']:x for x in D['knowledge']};E={x['id']:x for x in D['events']};R={x['id']:x for x in D['relationships']}
for m in D:ck(m+'_ALL_STABLE_IDS_UNCHANGED',[x['id'] for x in D[m]]==[x['id'] for x in O[m]])
ck('NO_EVENT_OR_REL_FACT_MUTATION',D['events']==O['events'] and D['relationships']==O['relationships'])
ck('ALL_365_EXISTING_K_STATES_TRUTH_GRADES_PRESERVED',all(all(r[k]==o[k] for k in ['states','truth','grade','canon_status','disclosures']) for r,o in zip(D['knowledge'],O['knowledge'])))
ck('NO_NEW_K_OR_TRANSITION',len(K)==235 and sum(len(r['states']) for r in K.values())==365)
ck('NO_NEW_REL_OR_DIMENSION',len(R)==172 and sum(len(r['stages']) for r in R.values())==583 and D['relationships']==O['relationships'])
ck('ALL_CH_TIERS_PSYCH_SNAPSHOTS_PRESERVED',all(all(r.get(k)==o.get(k) for k in ['tier','psych','snapshots','unknown']) for r,o in zip(D['characters'],O['characters'])))
log=json.loads((B/'patch_changes.json').read_text(encoding='utf-8'));bad=[]
for m in ['characters','knowledge']:
 for r,o in zip(D[m],O[m]):
  for key in set(r)|set(o):
   if r.get(key)!=o.get(key):
    chain=[x for x in log if x.get('record')==r['id'] and x['field']==key]
    if not chain or chain[0]['before']!=o.get(key) or chain[-1]['after']!=r.get(key):bad.append([r['id'],key])
ck('EVERY_CHANGED_RECORD_FIELD_LOGGED',not bad,bad)
# Text changes replay from byte-preserved V1 source without broad formatting changes.
bad=[]
for path in {x['path'] for x in log if x['field'] in ['exact_text','append_navigation']}:
 s=Z.read('canon/'+path).decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
 for x in [x for x in log if x['path']==path]:
  if x['field']=='exact_text':
   if x['before'] not in s:bad.append(path+' missing before')
   s=s.replace(x['before'],x['after'])
  elif x['field']=='append_navigation':s=s.rstrip()+'\n\n'+x['after']+'\n'
 if s!=(C/path).read_text(encoding='utf-8-sig'):bad.append(path+' replay mismatch')
ck('TEXT_PATCH_REPLAY_EXACT',not bad,bad)
ck('CR001_RED_STAGES_DISAMBIGUATED','不等兽化受控期不能感知妖精' in H['CH005']['stages'][1][2] and '复原后才能看听妖精' not in H['CH005']['knowledge'])
for path in ['characters/CH005_红思与.md','knowledge/by_character/CH005_knowledge.md']:ck('CR001_MIRROR_'+path,H['CH005']['knowledge'] in (C/path).read_text(encoding='utf-8-sig'))
ck('CR001_EV0053_REL056_K055_K056_K057_UNCHANGED',all(K[id]==next(x for x in O['knowledge'] if x['id']==id) for id in ['K055','K056','K057']) and R['REL056']==next(x for x in O['relationships'] if x['id']=='REL056'))
ck('CR002_DIRECTIONAL_VIEW_ONLY',all('CH029→CH006' in H[id]['relations'] and 'D/E' in H[id]['relations'] and '不推其回向态度' in H[id]['relations'] for id in ['CH006','CH029']))
ck('CR002_DISCOVERABLE_IN_MATRIX','尚未单建REL的评价导航' in (C/'relationships/RELATIONSHIP_MATRIX.md').read_text(encoding='utf-8-sig'))
ck('CR003_REASON_NO_SECRET_GRANT',H['CH010']['tier']=='A' and '未证获得K018' in H['CH010']['reason'] and K['K226']['truth']=='UNKNOWN')
ck('CR003_K015_K226_UNCHANGED',all(K[id]==next(x for x in O['knowledge'] if x['id']==id) for id in ['K015','K226']))
origin=K['K098']['cross_references'][0];back=K['K018']['cross_references'][0]
ck('CR004_BIDIRECTIONAL_REFERENCE_RESOLVES',origin['knowledge_id']=='K018' and any(s['id']==origin['transition_id'] for s in K['K018']['states']) and back['knowledge_id']=='K098' and any(s['id']==back['transition_id'] for s in K['K098']['states']))
ck('CR004_ORIGIN_TIME_EQUALS_EXISTING_T005',origin['event']=='EV0067' and origin['point']==next(s for s in K['K018']['states'] if s['id']=='K018-T005')['acquisition']['point'])
# Actual current lookup, plus explicit consumer-followed cross-navigation (not a change to production query API).
sp=importlib.util.spec_from_file_location('q',C/'knowledge/query_knowledge.py');q=importlib.util.module_from_spec(sp);sp.loader.exec_module(q);real=q.load
q.load=lambda name:D['knowledge'] if name=='records.json' else real(name)
def sel(ch,ev,id,before=False):return [x for x in q.lookup(ch,ev,before)['allowed'] if x['knowledge_id']==id]
def nav(ev,before=False,ch='CH002'):
 direct=sel(ch,ev,'K098',before)
 if direct:return {'route':'DIRECT_EXISTING_STATE','source':direct,'interpretation':'DISBELIEVES否定恋爱；不确认同人'}
 src=sel(ch,ev,'K018',before)
 src=[x for x in src if x['transition']==origin['transition_id'] and ch==origin['subject']]
 return {'route':'EXPLICIT_CROSS_NAVIGATION' if src else 'NO_ELIGIBLE_ORIGIN','source':src,'interpretation':'只取恋爱误解片段，不复制K018的state到K098，不背书其他因果'}
queries=[]
for ev,bef,expected in [('EV0003',False,'NO_ELIGIBLE_ORIGIN'),('EV0067',True,'NO_ELIGIBLE_ORIGIN'),('EV0067',False,'EXPLICIT_CROSS_NAVIGATION'),('EV0078',False,'EXPLICIT_CROSS_NAVIGATION'),('EV0090',False,'EXPLICIT_CROSS_NAVIGATION'),('EV0092',True,'EXPLICIT_CROSS_NAVIGATION'),('EV0092',False,'DIRECT_EXISTING_STATE'),('EV0117',False,'DIRECT_EXISTING_STATE')]:
 out=nav(ev,bef);queries.append(dict(event=ev,before=bef,expected=expected,actual=out));ck('CR004_WINDOW_'+ev+('_BEFORE' if bef else '_AFTER'),out['route']==expected,out)
ck('CR004_NAV_DOES_NOT_GRANT_OTHER_CHARACTER',nav('EV0078',ch='CH010')['route']=='NO_ELIGIBLE_ORIGIN')
for ev in ['EV0004','EV0024','EV0055','EV0067','EV0158']:ck('CR003_NO_K018_'+ev,not sel('CH010',ev,'K018'))
# Existing query behavior remains exactly unchanged; don't hide implementation scope.
samples=[('CH005','EV0017'),('CH005','EV0053'),('CH005','EV0054'),('CH006','EV0158'),('CH010','EV0024'),('CH010','EV0055'),('CH002','EV0067'),('CH002','EV0092')];beforeafter=[]
for ch,ev in samples:
 q.load=lambda name:O['knowledge'] if name=='records.json' else real(name);b=q.lookup(ch,ev)
 q.load=lambda name:D['knowledge'] if name=='records.json' else real(name);a=q.lookup(ch,ev)
 beforeafter.append({'character':ch,'event':ev,'unchanged':a==b});ck('PRODUCTION_QUERY_UNCHANGED_'+ch+'_'+ev,a==b)
protected={p:h for p,h in BASE.items() if not p.startswith('canon/')};bad=[p for p,h in protected.items() if not (P/p).is_file() or sha(P/p)!=h];extra=[p.relative_to(P).as_posix() for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.relative_to(P).as_posix().startswith('canon/') and p.relative_to(P).as_posix() not in BASE];ck('SOURCE_CURRENT_AUDIT_PERFORMANCE_FINAL_UNCHANGED',not bad and not extra,{'files':len(protected),'changed':bad,'new':extra})
ck('V1_HISTORY_ARCHIVE_EXACT',all(hashlib.sha256(Z.read(p)).hexdigest()==h for p,h in BASE.items() if p.startswith('canon/')))
ck('STAGE2C_HISTORY_UNCHANGED',all((P/p).is_file() and sha(P/p)==h for p,h in BASE.items() if p.startswith('canon/_stage2c/') or p in ['canon/CHANGELOG_STAGE2C.md','canon/STAGE2C_FINAL_REVIEW.md','canon/STAGE2C_REVIEW_QUEUE.md']))
changed=[p for p,h in BASE.items() if p.startswith('canon/') and (not (P/p).is_file() or sha(P/p)!=h)];allowed={'canon/'+x['path'] for x in log}|{'canon/README.md','canon/BASELINE_MANIFEST.md'};ck('ONLY_ALLOWED_OLD_FILES_CHANGED',set(changed)<=allowed,{'modified':changed,'outside':sorted(set(changed)-allowed)})
ck('REQUIRED_PUBLIC_REPORTS_PRESENT',all((C/p).is_file() for p in ['STAGE3A_CANON_PATCH_REVIEW.md','CHANGELOG_STAGE3A_PATCH.md','STAGE3A_PATCH_FOLLOWUPS.md']))
# Local links only in current affected documents + new reports, not in copied historical V1 documents.
paths={C/x['path'] for x in log if x['path'].endswith('.md')}|{C/'README.md',C/'BASELINE_MANIFEST.md'}|set(C.glob('STAGE3A*.md'))|set(C.glob('CHANGELOG_STAGE3A*.md'));bad=[];links=0
for f in paths:
 if not f.exists():continue
 s=f.read_text(encoding='utf-8-sig')
 for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',s):
  part=urllib.parse.unquote(target.strip('<>').split('#',1)[0]);part=re.sub(r':\d+$','',part)
  if re.match(r'\w+://',part):continue
  dest=(f.parent/part).resolve() if part else f;links+=1
  if not dest.exists():bad.append([f.relative_to(C).as_posix(),target])
ck('CHANGED_DOCUMENT_LOCAL_LINKS',not bad,{'count':links,'bad':bad})
result={'status':'PASS' if all(x['status']=='PASS' for x in checks) else 'FAIL','checks':checks,'queries':queries,'production_query_unchanged':beforeafter,'protected_files':len(protected),'modified_old_files':changed,'counts':{'EV':192,'CH':70,'REL':172,'relationship_stages':583,'K':235,'knowledge_states':365,'new_stable_ids':0},'scope':'仅四条Patch局部回归；K098采用显式导航方案，未扩建生产查询器。未执行全文审计或Stage2C全量重建。'}
(B/'regression_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':result['status'],'checks':len(checks),'protected':len(protected),'failures':[x for x in checks if x['status']=='FAIL']},ensure_ascii=False));raise SystemExit(result['status']!='PASS')
