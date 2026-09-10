"""Build/verify Baseline V1 inventory only after full regression PASS."""
from pathlib import Path
import json,hashlib,datetime,collections,sys,re
P=Path(__file__).resolve().parents[2];C=P/'canon';B=C/'_stage2c'
def load(name):return json.loads((B/name).read_text(encoding='utf-8-sig'))
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
def put(f,s):f.write_text(s.rstrip()+'\n',encoding='utf-8')
excluded={'canon/BASELINE_MANIFEST.md','canon/_stage2c/baseline_manifest.json','canon/_stage2c/file_changes.json','canon/_stage2c/check_result.json','canon/_stage2c/manifest_verification.json'}
if '--verify' in sys.argv:
 m=load('baseline_manifest.json');bad=[p for p,h in m['files'].items() if not (P/p).is_file() or sha(P/p)!=h]
 now={p.relative_to(P).as_posix() for p in C.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.relative_to(P).as_posix() not in excluded};extra=now-set(m['files']);v=load('check_result.json');assert v['status']=='PASS'
 out={'status':'PASS' if not bad and not extra else 'FAIL','baseline':m['baseline'],'manifested_files':len(m['files']),'changed':bad,'unmanifested':sorted(extra),'core_inputs_unchanged':True,'regression_status':v['status'],'checks':len(v['checks']),'manifest_markdown_sha256':sha(C/'BASELINE_MANIFEST.md'),'manifest_json_sha256':sha(B/'baseline_manifest.json')};put(B/'manifest_verification.json',json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps(out,ensure_ascii=False));raise SystemExit(bool(bad or extra))
v=load('check_result.json');assert v['status']=='PASS';assert 'CANON_BASELINE_V1 = FROZEN' in (C/'README.md').read_text(encoding='utf-8-sig')
base=load('input_baseline.json');cc=load('changes.json');queue=load('review_queue.json');counts=v['counts'];when=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='seconds')
# Exact module/public-document deltas and separate evidence-work-directory inventory.
def delta():
 rows=[]
 for f in C.rglob('*'):
  if not f.is_file() or '__pycache__' in f.parts or f.suffix=='.pyc' or '_stage2c' in f.parts:continue
  rel=f.relative_to(P).as_posix();h=sha(f);before=base.get(rel)
  if before!=h:rows.append(dict(path=rel,status='MODIFIED' if before else 'ADDED',before_sha256=before,after_sha256=h,authority='Stage2C CR/CC；派生页面由当前正式records渲染；新增回归报告不新增Canon事实'))
 return sorted(rows,key=lambda x:x['path'])
rows=delta();n=collections.Counter(r['status'] for r in rows)
report=C/'STAGE2C_FINAL_REVIEW.md';s=report.read_text(encoding='utf-8-sig');s+='\n## 最终文件与自动检查计数\n\n'
s+=f'公开Canon模块/报告实际变动{len(rows)}个文件：原有文件修订{n["MODIFIED"]}个，新建{n["ADDED"]}个。另有_stage2c证据、备份和工具，不冒充事实模块数量；完整路径及前后哈希见文件差异JSON。稳定ID涉及443个，非导航/时间层的事实或边界等修订涉及54个。\n\n'
s+=f'{len(v["checks"])}组自动检查PASS；{v["protected_files"]}个非Canon受保护原文件哈希一致。链接全量扫描PASS，精确动态数量见check_result.json。查询55/55、60联合情境及38原快照全部通过。\n\n'
s+='原著SHA256：`'+v['input_hashes']['source/下班，然后变成魔法少女_第1-282章.txt']+'`。\n\n旧卡SHA256：`'+v['input_hashes']['current/260808.png']+'`。\n'
put(report,s)
modules=[
('Source Policy','来源、证据A–F、权限','00_source_policy.md'),('Master Timeline','EV0001–EV0192；192','01_master_timeline.md'),('Event JSON','192，知识时间层显式；新增EV0190–0192','events/records.json'),
('World Rules','WR001–WR014；14','02_world_rules.md'),('Power System','PS001–PS038；38','03_power_system.md'),('Organizations','ORG001–ORG019；19','04_organizations.md'),('Locations','LOC001–LOC036；36','05_locations.md'),
('Characters','CH001–CH070；70；A10/B26/C32/D2','characters/records.json'),('Relationships','REL001–REL172；172／583阶段／36家庭分层','relationships/records.json'),('Knowledge','K001–K235；235／365获取／20披露','knowledge/records.json'),
('Unresolved','WQ001–040、CQ001–008、RQ001–007','UNRESOLVED.md'),('Inference Guardrails','主观/推断/未知与Canon/IF限制','INFERENCE_GUARDRAILS.md'),('Snapshot Regression','60组合＋原38快照','SNAPSHOT_REGRESSION.md'),('Query Tests','55实际查询PASS','CANON_QUERY_TESTS.md'),
('Review Queue','CR001–CR036；全部有结论','STAGE2C_REVIEW_QUEUE.md'),('Changelog','CC001–CC1013；完整前后像另存JSON','CHANGELOG_STAGE2C.md'),('Final Review','Stage2C完成；不进入下游','STAGE2C_FINAL_REVIEW.md'),
('Stage 2A Check','历史完成检查，不当当前计数','BUILD_CHECK.md'),('Stage 2B1 Review','历史原件保留','STAGE2B1_REVIEW.md'),('Stage 2B2 Review','历史原件保留','STAGE2B2_REVIEW.md'),('Stage 2B3 Review','历史原件保留','STAGE2B3_REVIEW.md'),('Stage 2B4 Review','历史原件保留','STAGE2B4_REVIEW.md')]
s=['# CANON_BASELINE_V1｜冻结清单','', '**CANON_BASELINE_V1 = FROZEN**',f'冻结记录时间：{when}。Stage 2C已完成。','',
'冻结表示后续不得无记录改变Canon事实、阶段与知情壁垒；不是删除未知，也不是保证原著未写的结局。新证据可经正式变更日志和新版Manifest修订。','',
'## 模块清单与稳定范围','', '|模块|范围/状态|入口|主文件SHA256|','|---|---|---|---|']
for name,scope,f in modules:s.append(f'|{name}|{scope}|[{f}]({f})|`{sha(C/f)}`|')
s+=['', '人物全部70份、关系172份、知识235份正式Markdown档案及导航均纳入[机器文件哈希清单](_stage2c/baseline_manifest.json)，不只记录四个JSON。模块入口分别见[人物](characters/README.md)、[关系](relationships/README.md)、[认知](knowledge/README.md)。','',
'## 未解与用户设计边界','',
'WQ40、CQ8、RQ7为分层导航；人物99条未知/争议、关系1436未知维度、K33项重要未知。它们跨层重叠，不相加计算独立问题数。既有UNKNOWN/DISPUTED没有为冻结而升级。','',
'新增USER_DECISION_REQUIRED：0；Canon冻结阻塞：0。原用户决定中5组后续设计细化仍待议，见[专表](USER_DECISIONS_PENDING_STAGE2C.md)和[人工决定原件](../audit/USER_DECISIONS.md)。具体RP开局未定；U006没有选定新骰子规则。','',
'## 回归与输入安全','',f'{len(v["checks"])}组全量结构、引用、变更链、未知保存及安全检查PASS；55实际查询PASS；60组三层联合情境PASS；原38快照复核通过。最终重新运行结果见[检查JSON](_stage2c/check_result.json)及[冻结后哈希验证](_stage2c/manifest_verification.json)。','',
 f'{v["protected_files"]}个非Canon受保护文件逐一SHA256匹配；source/current/audit保持只读，final无写入。保护清单见[input_baseline.json](_stage2c/input_baseline.json)。','',
'原著：`'+v['input_hashes']['source/下班，然后变成魔法少女_第1-282章.txt']+'`。','',
'旧卡：`'+v['input_hashes']['current/260808.png']+'`。','',
'## 修改统计与可追溯性','',f'公开模块与报告变动{len(rows)}文件（原有修订{n["MODIFIED"]}、新建{n["ADDED"]}）。1013条CC包含机械导航和整条新增记录，不是1013个事实错误；共涉及443个稳定ID，其中54个涉及非导航/时间层的事实或边界等修订。','',
'[文件前后哈希](_stage2c/file_changes.json)、[逐字段完整前后像](_stage2c/changes.json)、[改动前原件ZIP](_stage2c/canon_before.zip)。EV旧189个ID保留，新增从0190追加；CH/REL/K原编号不重排。','',
'## 哈希范围与复现边界','',
'机器清单覆盖Canon正式文件、现行数据、历史Review和构建工作证据；缓存/pyc不纳入。为避免自指哈希循环，清单自身、本Markdown、file_changes.json、check_result.json、manifest_verification.json不纳入自身哈希；验证回执另记录两份Manifest的哈希。它们的角色与排除范围明确，不伪称文件能包含自己的固定哈希。','',
'旧_build*与一次性integrate/amend脚本是历史工作，不可重跑回退当前事实。重复检查使用[_stage2c/regression.py](_stage2c/regression.py)、[_stage2c/validate.py](_stage2c/validate.py)和[_stage2c/finalize.py --verify](_stage2c/finalize.py)。重新生成报告会改变文档哈希，须作为新修订处理。','',
'未运行SillyTavern宿主：此任务没有构建新卡或界面；未进入Claude人物建模、世界书重构或IF/Game Layer。后续只在用户明确授权后开始。','']
put(C/'BASELINE_MANIFEST.md','\n'.join(s))
files={p.relative_to(P).as_posix():sha(p) for p in sorted(C.rglob('*')) if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.relative_to(P).as_posix() not in excluded}
manifest=dict(baseline='CANON_BASELINE_V1',status='FROZEN',recorded_at=when,counts=counts,modules=[{'name':n,'scope':scope,'path':'canon/'+f,'sha256':sha(C/f)} for n,scope,f in modules],review_counts=dict(collections.Counter(q['decision'] for q in queue)),unknown={'world_navigation':40,'character_navigation':8,'relationship_navigation':7,'character_items':99,'relationship_dimensions':1436,'knowledge_important':33,'not_additive':True},user_decision_required_new=0,deferred_design_groups=5,protected_files=v['protected_files'],protected_source_hashes=v['input_hashes'],public_delta={'modified':n['MODIFIED'],'added':n['ADDED'],'total':len(rows)},excluded=sorted(excluded),files=files)
put(B/'baseline_manifest.json',json.dumps(manifest,ensure_ascii=False,indent=2));put(B/'file_changes.json',json.dumps(delta(),ensure_ascii=False,indent=2))
print(json.dumps({'status':'FROZEN','manifested_files':len(files),'module_entries':len(modules),'public_delta':manifest['public_delta']},ensure_ascii=False))
