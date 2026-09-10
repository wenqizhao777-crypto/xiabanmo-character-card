"""人物库结构/引用/只读边界检查；不声称自动证明文学语义。"""
import json,pathlib,re,hashlib,collections
from build import ROOT,OUT,EV,E
P=json.loads((OUT/'records.json').read_text(encoding='utf8'))
errors=[];warnings=[]
def need(ok,msg):
 if not ok:errors.append(msg)
seq=[x['id'] for x in P];need(seq==[f'CH{i:03}' for i in range(1,len(P)+1)],'CH重复/断号/顺序')
need(len({x['name'] for x in P})==len(P),'档案名重复')
need(json.loads((OUT/'_build2b2/dossiers.json').read_text(encoding='utf8'))==P,'源数据与records不同步')
snap_count=0;unknown=0;checks=0
for d in P:
 f=OUT/f'{d["id"]}_{d["name"]}.md';need(f.exists(),str(f)+' missing')
 t=f.read_text(encoding='utf8');unknown+=len(d['unknown'])
 for k in ['first','end','org','power','relations','knowledge','unknown','evidence']:need(bool(d.get(k)),d['id']+' empty '+k)
 for n in ([1,2,3,4,5,6,7,8,9,10,11,12,13] if d['tier'] in 'AB' else [1,2,9,10,12,13]):need(f'## {n}｜' in t,d['id']+' section '+str(n))
 for e in d['events']:need(e in EV,d['id']+' invalid '+e)
 for e in d['evidence']:need(e in E,d['id']+' invalid '+e)
 if d['tier']=='A':
  need(len(d.get('snapshots',[]))>=3,d['id']+' snapshots missing')
  for s in d['snapshots']:
   snap_count+=1
   need(all(s.get(k) for k in ['node','身份','所属','位置','能力','伤势','关系','认知','心理']),d['id']+' incomplete snapshot')
  need(bool(d.get('audit_issues')) and bool(d.get('audit_missing')),d['id']+' audit nav missing')
 for target in re.findall(r'\]\(([^)]+)\)',t):
  if target.startswith(('http:','https:')):continue
  target=target.strip('<>');base,sep,anchor=target.partition('#')
  base=re.sub(r':\d+$','',base)
  dest=(f.parent/base).resolve();need(dest.is_file(),str(f.name)+' missing link '+target);checks+=1
  if anchor and dest.is_file():
   dt=dest.read_text(encoding='utf-8-sig')
   # 既有文件采用显式锚点；审计E使用纯编号标题。
   need(f'id="{anchor}"' in dt or re.search(r'^#{1,6} '+re.escape(anchor)+r'\s*$',dt,re.M|re.I),str(f.name)+' invalid anchor '+target)
 # 只核验正文L定位界限；不会通过数字存在宣称语义已经正确。
 for a,b in re.findall(r'\[L(\d+)(?:–(\d+))?\]',t):need(1<=int(a)<=38825 and (not b or int(a)<=int(b)<=38825),d['id']+' source range')
old=(OUT/'_build2b2/legacy_readme.md').read_text(encoding='utf8')
now=(OUT/'README.md').read_text(encoding='utf8')
anchors=re.findall(r'id="(p_temp_\d+)"',old)
need(len(anchors)==164 and all(now.count('id="'+a+'"')==1 for a in anchors),'旧164锚点丢失/重复')
need((OUT/'LEGACY_P_TEMP_INDEX.md').read_text(encoding='utf8')==old,'历史导航内容变化')
maps=json.loads((OUT/'_build2b2/temp_mapping.json').read_text(encoding='utf8'))
need(len(maps)==164,'映射不齐')
for m in maps:
 for k in m['characters']:need(k in seq,'P映射未知 '+k)
alltext='\n'.join((OUT/f'{d["id"]}_{d["name"]}.md').read_text(encoding='utf8') for d in P)
defs={'CH':set(seq),'E':set(E),'EV':set(EV)}
for pre,f in [('PS','03_power_system.md'),('WR','02_world_rules.md'),('ORG','04_organizations.md'),('LOC','05_locations.md')]:
 defs[pre]=set(re.findall(r'## ('+pre+r'\d{3})', (ROOT/'canon'/f).read_text(encoding='utf8')))
for pre,valid in defs.items():
 for k in set(re.findall(r'(?<![A-Za-z_])'+pre+r'\d{3,4}\b',alltext)):need(k in valid,'未知引用 '+k)
# 重点已人工核验的事实回归，避免后续重新渲染把错误初稿带回来。
by={d['id']:json.dumps(d,ensure_ascii=False) for d in P}
for k,term in [('CH005','忆记'),('CH007','情热'),('CH004','左眼'),('CH012','L12646'),('CH021','本相重伤'),('CH029','浅粉色'),('CH052','L33910'),('CH067','死透')]:need(term in by[k],'关键修订遗失 '+k+':'+term)
base=json.loads((OUT/'_build2b2/input_baseline.json').read_text(encoding='utf8'))
allowed={'canon/README.md','canon/UNRESOLVED.md','canon/INFERENCE_GUARDRAILS.md'}
protected=[];changed=[]
for rel,sha in base.items():
 if rel.startswith('canon/characters/') or rel in allowed:continue
 f=ROOT/rel;actual=hashlib.sha256(f.read_bytes()).hexdigest() if f.is_file() else None
 protected.append({'path':rel,'sha256':actual,'unchanged':actual==sha})
 if actual!=sha:changed.append(rel)
need(not changed,'只读文件发生变化 '+str(changed))
unexpected=[]
for f in ROOT.rglob('*'):
 if not f.is_file():continue
 rel=f.relative_to(ROOT).as_posix()
 if rel not in base and not(rel.startswith('canon/characters/') or rel=='canon/STAGE2B2_REVIEW.md'):unexpected.append(rel)
need(not unexpected,'越界新文件 '+str(unexpected))
for rel in ['canon/UNRESOLVED.md','canon/INFERENCE_GUARDRAILS.md']:
 content=(ROOT/rel).read_bytes();marker=b'\n<!-- STAGE2B2_APPEND_BEGIN -->'
 original=content.split(marker)[0]
 need(hashlib.sha256(original).hexdigest()==base[rel],rel+'原有内容非增量改动')
result={'stage':'Stage 2B-2','status':'PASS' if not errors else 'FAIL','characters':len(P),'tiers':dict(collections.Counter(d['tier'] for d in P)),
 'full_or_standard':sum(d['tier'] in 'AB' for d in P),'brief_or_minimal':sum(d['tier'] in 'CD' for d in P),'snapshots':snap_count,'unknown_disputed_items':unknown,
 'legacy_anchors':164,'local_link_checks':checks,'protected_file_count':len(protected),'changed_protected':changed,'unexpected_new_files':unexpected,'errors':errors,'warnings':warnings,
 'semantic_boundary':'结构自动检查不代替原著语义；人工重点核验范围见STAGE2B2_REVIEW。',
 'protected_hashes':protected}
(OUT/'_build2b2/check_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='protected_hashes'},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
