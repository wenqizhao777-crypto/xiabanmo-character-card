"""Version-only finalization. Never reruns the one-time factual navigation patch."""
from pathlib import Path
from datetime import datetime,timezone,timedelta
import json,hashlib,zipfile,re,subprocess,sys
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parents[2];C=P/'canon';B=C/'_stage3a_patch'
BASE=json.loads((B/'input_baseline.json').read_text(encoding='utf-8'))
Z=zipfile.ZipFile(B/'baseline_v1_canon.zip')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,s):p.write_text(s,encoding='utf-8')
def js(p,x):put(p,json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def original(path):return Z.read('canon/'+path).decode('utf-8-sig').replace('\r\n','\n')
def write_preserving(path,text):
 raw=Z.read('canon/'+path);newline='\r\n' if b'\r\n' in raw else '\n'
 (C/path).write_bytes((b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b'')+text.replace('\r\n','\n').replace('\n',newline).encode('utf-8'))

def version_docs(frozen):
 stamp=datetime.now(timezone(timedelta(hours=8))).isoformat(timespec='seconds')
 status='FROZEN' if frozen else 'PENDING_LOCAL_REGRESSION'
 readme=original('README.md').replace('# Canon Reference｜CANON_BASELINE_V1\n','# Canon Reference｜CANON_BASELINE_V1.1\n',1)
 readme=readme.replace('**Stage 2C：完成。CANON_BASELINE_V1 = FROZEN**',f'**Stage 3A 四项受控 Canon Patch：已核证。CANON_BASELINE_V1.1 = {status}**\n\nV1 是 Stage 2C 历史冻结版；V1.1 是 Stage 3A 后的局部消歧/导航修订版。当前先读 [Patch Review](STAGE3A_CANON_PATCH_REVIEW.md)、[Patch Changelog](CHANGELOG_STAGE3A_PATCH.md)和[当前 Manifest](BASELINE_MANIFEST.md)。既有稳定编号与知识状态不变。',1)
 readme=readme.replace('|回归|60组三层联合情境＋原38快照；55项实际查询|','|Stage 2C 历史回归|60组三层联合情境＋原38快照；55项实际查询|')
 readme=readme.replace('先读[基线清单]','Stage 2C 历史入口：[基线清单]',1)
 readme=readme.replace('5. 未来经授权才做心理/语言/行为建模与RP执行描述。','5. Stage 3A 已有 Performance 模型，本轮仅核证四条 Canon 疑点；后续模型同步或其他建模须另获授权。')
 readme=readme.replace('Stage 1全文阅读仍为100%，','以下为 Stage 2C 完成时的历史范围说明，保留追溯，不当作 Stage 3A 尚未发生：\n\nStage 1全文阅读仍为100%，',1)
 readme+='''\n## Stage 3A Patch 当前读取补充

- CH005：受控期已有妮妮交流；不要把人形/感官获救理解为首次妖精感知或取回全部原封印力量。
- CH029→CH006：新增 D/E 评价导航；不新建 REL、不推安雅的反向态度或阴谋。
- CH010：Tier A 与信息流转角色不授予 K018；K226 UNKNOWN 不等原著已证永远不知道。
- K098：EV0067–EV0092 的恋爱误解来源导航至 K018-T005；生产查询器不自动联查，需按同主体/时间补读限定片段。到 EV0092 使用 K098 的原纠正状态。
- [FUP-3A-001](STAGE3A_PATCH_FOLLOWUPS.md)保持开放；[PERFORMANCE_SYNC_REQUIRED](STAGE3A_CANON_PATCH_REVIEW.md#performance_sync_required)尚未执行。来源/当前卡/审计/Performance/final 本轮均未改动。
- 本轮局部检查见 [regression_results.json](_stage3a_patch/regression_results.json)。旧 Stage 2C 检查回执只证明 V1 历史，不用旧清单验证 V1.1 新哈希，也不要重跑历史构建器。

V1 原件、V1.1 当前哈希及验证方式统一见 [Manifest](BASELINE_MANIFEST.md)。本任务到此版本补丁为止，不进入 Stage 3B 或角色卡重构。
'''
 write_preserving('README.md',readme)
 old=original('BASELINE_MANIFEST.md')
 table=old[old.index('|模块|'):old.index('\n人物全部70份')]
 for match in list(re.finditer(r'\|\[([^\]]+)\]\(([^)]+)\)\|`([0-9a-f]{64})`\|',table)):
  table=table.replace(match.group(3),sha(C/match.group(2)))
 # These rows are retained historical validations, not rerun claims.
 table=table.replace('|Snapshot Regression|','|V1历史 Snapshot Regression|').replace('|Query Tests|','|V1历史 Query Tests|').replace('|Review Queue|','|V1历史 Review Queue|').replace('|Changelog|','|V1历史 Changelog|').replace('|Final Review|','|V1历史 Final Review|')
 manifest=f'''# CANON_BASELINE_V1.1｜冻结清单

**CANON_BASELINE_V1.1 = {status}**
本轮记录时间：{stamp}。四条 Stage 3A Canon Review Request 已核证；冻结仅在本轮局部回归通过后生效。

冻结固定当前可追溯事实、状态与导航边界，不代表未知已解决，不代表 Performance 已同步，不代表重做 Stage 2C 或完成 RP 宿主验收。

## 版本历史

- **V1：Stage 2C 冻结版**，原冻结时间 2026-09-10T20:59:22+08:00。
- **V1.1：Stage 3A 后受控 Canon Patch 版**；仅四项消歧/导航修订。ACCEPT 2 / PARTIAL_ACCEPT 2；无稳定 ID、已有 Knowledge 状态、truth 或等级变更。
- V1 原清单按原字节保存于 [BASELINE_MANIFEST_V1.md](_stage3a_patch/BASELINE_MANIFEST_V1.md)及 [baseline_v1_manifest.json](_stage3a_patch/baseline_v1_manifest.json)。前者是字节原件，内嵌相对链接仍按原目录解释；完整可还原目录上下文在 [V1 Canon ZIP](_stage3a_patch/baseline_v1_canon.zip)。原 [_stage2c/baseline_manifest.json](_stage2c/baseline_manifest.json)、Stage 2C Review/Changelog/检查证据均未覆盖。

## 当前模块与稳定范围

{table}

人物 70、关系 172、知识 235 份正式档案及现行导航纳入 [V1.1 机器哈希清单](_stage3a_patch/baseline_v1_1_manifest.json)。原世界 107 条、38 快照、20 披露边保持原口径。旧 Stage 2C 报告只作为历史检查证据，上表有明确标记。

## 本轮 Patch 与回归

- [Patch Review](STAGE3A_CANON_PATCH_REVIEW.md)、[Changelog](CHANGELOG_STAGE3A_PATCH.md)、[逐字段前后像](_stage3a_patch/patch_changes.json)、[版本入口前后像](_stage3a_patch/version_changes.json)。
- 15 个既有文件变更：13 个局部数据/导航文件，2 个版本入口。新增公开报告 3 份；辅助证据单列于 [文件变化清单](_stage3a_patch/patch_file_changes.json)。稳定 ID 新增 0。
- [局部回归](_stage3a_patch/regression_results.json)：49 项检查，包含 8 个显式导航恢复窗口、8 个真实生产查询前后对照，以及编号/字段/镜像/输入保护。K098 补的是显式导航，**没有改造生产查询器使其自动联查**。
- 原事件/关系数据、所有既有知识状态/真值/等级/披露、人物 Tier/psych/原快照保持不变。旧 Stage 2C 的 43 组检查、55 项查询、60 组联合情境为 V1 历史结果，本轮不伪称重新执行。
- [冻结验证回执](_stage3a_patch/manifest_verification.json)独立核验当前文件哈希、两个 Manifest、V1 保存与只读输入。

## 未知、后续同步及用户边界

既有 WQ40/CQ8/RQ7、人物99条、关系1436维度、K33项重要未知的口径不变，不相加冒充独立问题数。原用户5组后续设计细则仍待议，见 [专表](USER_DECISIONS_PENDING_STAGE2C.md)。

新 [FUP-3A-001](STAGE3A_PATCH_FOLLOWUPS.md)仅登记 K018-T005 强因果证据链待复核；本轮保留原状态，不新增结论。四项受控修改没有冻结阻塞。**PERFORMANCE_SYNC_REQUIRED** 见 [Review 同步表](STAGE3A_CANON_PATCH_REVIEW.md#performance_sync_required)，未改写 Performance，也没有宣称下游已同步。

## 输入保护与哈希范围

本輪开始记录 933 个既有项目文件，其中 290 个非 Canon 文件逐一核对；source/current/audit/performance/final 均未改动，保护目录无新增文件。原 V1 638 项机器清单在修改前全部匹配；另外保留完整现有 Canon 字节快照，不以 V1 的旧哈希否定有日志的 V1.1 修改。

原著 SHA256：`18819c3060f411fd8bbb24e859657d24a7628317aed18c9106831f73eb250fa2`。

旧卡 SHA256：`3d6a1d85f42d0980aac7ce9ff62f0a94d51f3c3272c3eaedf39ef1b8bd517d`。

V1.1 机器清单覆盖 Canon 正式资料、历史原件和本轮脚本/前后像；缓存/pyc 排除。为避免自指循环，当前 Markdown Manifest、机器清单本身、局部检查回执、文件变化清单、冻结验证回执不进入自己的哈希范围；排除路径在机器清单逐项列明，验证回执另记两个当前 Manifest 和检查回执的哈希。

复核本补丁可运行 `python -X utf8 canon/_stage3a_patch/check_patch.py`；随后只读核验执行 `python -X utf8 canon/_stage3a_patch/finalize_patch.py --verify`。检查回执可更新，受冻结的正文不得无日志重建。不要重复运行一次性 `apply_patch.py`，不要重跑旧构建器覆盖当前数据。

未进入 Stage 3B、世界书重构、骰子/CG/好感系统；未修改角色卡或写入 final。后续只按新授权继续。
'''
 # Copy exact input card hash from historical manifest, not a hand-transcribed digest.
 card=re.search(r'旧卡：`([0-9a-f]{64})`',old).group(1)
 manifest=re.sub(r'旧卡 SHA256：`[^`]+`',f'旧卡 SHA256：`{card}`',manifest)
 write_preserving('BASELINE_MANIFEST.md',manifest)
 js(B/'version_changes.json',[{'id':f'P3A-{22+i:03}','request':'CR-3A-001–004 / VERSION_ONLY','path':p,'before':original(p),'after':(C/p).read_text(encoding='utf-8-sig'),'facts_changed':False} for i,p in enumerate(['README.md','BASELINE_MANIFEST.md'])])

def file_changes():
 current={p.relative_to(P).as_posix():sha(p) for p in C.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.name!='patch_file_changes.json'}
 js(B/'patch_file_changes.json',{'modified':[{'path':p,'before':BASE[p],'after':h} for p,h in current.items() if p in BASE and BASE[p]!=h],'added':[{'path':p,'sha256':None if p in ['canon/_stage3a_patch/manifest_verification.json','canon/_stage3a_patch/regression_results.json'] else h,'kind':'PUBLIC_REPORT' if p in ['canon/STAGE3A_CANON_PATCH_REVIEW.md','canon/CHANGELOG_STAGE3A_PATCH.md','canon/STAGE3A_PATCH_FOLLOWUPS.md'] else 'PATCH_SUPPORT'} for p,h in current.items() if p not in BASE],'deleted':[p for p in BASE if p.startswith('canon/') and not (P/p).exists()],'note':'本文件自指排除；可重跑的检查/冻结验证回执不在此填固定哈希。完整稳定哈希见当前 Manifest，两个 Manifest 与局部检查回执哈希见最终验证回执。'})

EXCLUDE={'BASELINE_MANIFEST.md','_stage3a_patch/baseline_v1_1_manifest.json','_stage3a_patch/regression_results.json','_stage3a_patch/patch_file_changes.json','_stage3a_patch/manifest_verification.json'}
def freeze_manifest():
 files={p.relative_to(C).as_posix():sha(p) for p in C.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.relative_to(C).as_posix() not in EXCLUDE}
 js(B/'baseline_v1_1_manifest.json',{'version':'CANON_BASELINE_V1.1','status':'FROZEN','files':files,'excluded_self_or_dynamic':sorted(EXCLUDE),'history':'V1 preserved byte-exact; _stage2c documents are historical','counts':{'EV':192,'CH':70,'REL':172,'REL_stages':583,'K':235,'K_states':365,'new_stable_ids':0},'scope':'Four-request local patch only'})

def verify():
 m=json.loads((B/'baseline_v1_1_manifest.json').read_text(encoding='utf-8'))
 bad=[p for p,h in m['files'].items() if not (C/p).is_file() or sha(C/p)!=h]
 current={p.relative_to(C).as_posix() for p in C.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and p.relative_to(C).as_posix() not in EXCLUDE}
 extra=sorted(current-set(m['files']))
 protected=[p for p,h in BASE.items() if not p.startswith('canon/') and (not (P/p).is_file() or sha(P/p)!=h)]
 outside_new=[p.relative_to(P).as_posix() for p in P.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc' and not p.relative_to(P).as_posix().startswith('canon/') and p.relative_to(P).as_posix() not in BASE]
 historical=all(hashlib.sha256(Z.read(p)).hexdigest()==h for p,h in BASE.items() if p.startswith('canon/'))
 historical=historical and (B/'BASELINE_MANIFEST_V1.md').read_bytes()==Z.read('canon/BASELINE_MANIFEST.md') and (B/'baseline_v1_manifest.json').read_bytes()==Z.read('canon/_stage2c/baseline_manifest.json')
 text=(C/'BASELINE_MANIFEST.md').read_text(encoding='utf-8-sig')
 table_bad=[path for path,h in re.findall(r'\]\(([^)]+)\)\|`([0-9a-f]{64})`\|',text) if sha(C/path)!=h]
 regression=json.loads((B/'regression_results.json').read_text(encoding='utf-8'))
 state=all('CANON_BASELINE_V1.1 = FROZEN' in (C/p).read_text(encoding='utf-8-sig') for p in ['README.md','BASELINE_MANIFEST.md','STAGE3A_CANON_PATCH_REVIEW.md'])
 versions=json.loads((B/'version_changes.json').read_text(encoding='utf-8'))
 chain=all(x['before']==original(x['path']) and x['after']==(C/x['path']).read_text(encoding='utf-8-sig') for x in versions)
 ok=not bad and not extra and not protected and not outside_new and historical and not table_bad and regression['status']=='PASS' and state and chain
 out={'status':'PASS' if ok else 'FAIL','version':m['version'],'checked_files':len(m['files']),'mismatches':bad,'unlisted':extra,'protected_changes':protected,'new_outside_canon':outside_new,'V1_byte_exact':historical,'module_hash_errors':table_bad,'local_regression':regression['status'],'local_checks':len(regression['checks']),'version_consistency':state,'version_change_chain':chain,'markdown_manifest_sha256':sha(C/'BASELINE_MANIFEST.md'),'machine_manifest_sha256':sha(B/'baseline_v1_1_manifest.json'),'regression_receipt_sha256':sha(B/'regression_results.json'),'note':'Read-only on baseline content; only this verification receipt is written.'}
 js(B/'manifest_verification.json',out);print(json.dumps(out,ensure_ascii=False));return ok

if __name__=='__main__':
 if '--verify' in sys.argv:raise SystemExit(not verify())
 if '--prepare' in sys.argv:
  version_docs(False)
  for path in ['baseline_v1_1_manifest.json','manifest_verification.json']:
   if not (B/path).exists():js(B/path,{'status':'PENDING_LOCAL_REGRESSION'})
  file_changes();print('Prepared pending version documents; not frozen.');raise SystemExit(0)
 if '--freeze' not in sys.argv:raise SystemExit('Use --prepare, --freeze or --verify')
 pre=json.loads((B/'regression_results.json').read_text(encoding='utf-8'))
 assert pre['status']=='PASS','Cannot freeze before local checks pass'
 version_docs(True)
 f=C/'STAGE3A_CANON_PATCH_REVIEW.md';s=f.read_text(encoding='utf-8')
 s=s.replace('- 局部回归与冻结结果：**由本轮收尾写入下方最终回执；未经通过不冻结。**','- 局部回归：**49 / 49 PASS**；290 个非 Canon 受保护文件哈希一致，无受保护目录新增文件。检查器发现并修正了自身对简档缺省字段及原矩阵特殊换行的处理；没有因此改写 Canon 事实。\n- Baseline：**CANON_BASELINE_V1.1 = FROZEN**。V1 原件保留，最终哈希结果见 [冻结验证](_stage3a_patch/manifest_verification.json)。')
 put(f,s)
 result=subprocess.run([sys.executable,'-X','utf8',str(B/'check_patch.py')],cwd=P)
 if result.returncode:raise SystemExit('Final checks failed; do not deliver frozen status until fixed.')
 freeze_manifest();file_changes();raise SystemExit(not verify())
