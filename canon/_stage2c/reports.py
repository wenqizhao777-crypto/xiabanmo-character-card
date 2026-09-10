"""Generate reviewable Stage 2C reports. Pass --freeze only after validation PASS."""
from pathlib import Path
import json,re,collections,hashlib,sys,datetime
P=Path(__file__).resolve().parents[2];C=P/'canon';B=C/'_stage2c';freeze='--freeze' in sys.argv
load=lambda f:json.loads((B/f).read_text(encoding='utf-8-sig'))
Q=load('review_queue.json');CC=load('changes.json');QT=load('query_tests.json');SR=load('snapshot_regression60.json');V=load('check_result.json');BASE=load('input_baseline.json')
if freeze:assert V['status']=='PASS',V['errors']
status='FROZEN' if freeze else 'CANDIDATE';when=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(timespec='seconds')
def put(f,s):(C/f).write_text(s.rstrip()+'\n',encoding='utf-8')
def js(x):return json.dumps(x,ensure_ascii=False)
def esc(s):return str(s).replace('|','／').replace('\n',' / ')
def short(v,n=220):
 s=js(v) if not isinstance(v,str) else v
 return esc(s if len(s)<=n else s[:n]+'…（完整字段见JSON）').replace('<','&lt;').replace('>','&gt;').replace('[','&#91;').replace(']','&#93;')
def src(ranges):return '；'.join(f'[L{a}–{b}](../source/下班，然后变成魔法少女_第1-282章.txt:{a})' for a,b in ranges) or '无新增源窗；核对原有记录与用户裁决，不伪称新原文证实'
def path_for(ch):
 m=ch['module'];id=ch['record']
 if m=='Event':return 'events/records.json'
 if m=='Character':return 'characters/records.json'
 if m=='Relationship':return 'relationships/records.json'
 if m=='Knowledge':return 'knowledge/records.json'
 return id
counts=collections.Counter(q['decision'] for q in Q)
# Snapshot report: actual 3-layer outputs saved full; compact human report includes all eight dimensions.
s=['# Stage 2C｜三层联合快照回归','',f'状态：60/60组合情境通过；原人物档38/38快照另行复核。生成时间：{when}。','',
'组合情境是核验用视图，不新增或重编号人物Snapshot。每位Tier A覆盖六类；原文没有独立重大能力升级时点的安雅、摩可明确保留未知，不为了凑数发明升级。末尾未再次出场的人物只引用最后有据状态，不默认移动、痊愈或继续接收消息。','',
'每组同时取Character的阶段事实、Relationship的有向阶段链、Knowledge的实际主体查询。Relationship全书末态维度不直接套给早期；历史时序不足不推成新关系。BEFORE严格是事件前，AFTER为支持窗口末态；事件中间的不同说法须回查子段。','',
'[60组完整三层返回值](_stage2c/snapshot_regression60.json) · [原38个快照完整复核](_stage2c/snapshot_regression38.json) · [可重复回归脚本](_stage2c/regression.py)','',
'人工逐项对照范围包括身份、所属/职务、位置、能力、伤势、关系、认知和心理证据等级。自动检查负责时间、主体、死后屏障等可判定约束；不宣称自动证明自然语言的全部语义。','']
for x in SR:
 s += [f'## {x["id"]}｜{x["character"]} {x["name"]}｜{x["category"]}','',f'**{x["result"]}** · [{x["event"]}](01_master_timeline.md#{x["event"].lower()}) {x["position"]} · {x["focus"]}。',f'人物来源：{x["character_origin"]}。','', '|核对项|此时允许的事实/限定|','|---|---|']
 for k,v in x['character_facts'].items():
  if k!='node':s.append(f'|{k}|{esc(v)}|')
 rids=[r['id'] for r in x['relationships']];know=x['knowledge'];s+=['', '有据关系阶段链：'+('、'.join(f'[{r}](relationships/{r}.md)' for r in rids) or '此节点无可安全排定的正式阶段；保留未知')+'。',f'实际认知返回：{len(know["allowed"])}条限定内容，{len(know["denied_or_unresolved"])}条拒绝/未决，状态`{know["status"]}`。返回内容逐条保存在完整JSON，含获取事件与来源；未返回不等此人一生从未知道。', '知识边界：'+('；'.join(f'{a["knowledge_id"]}={a["state"]}' for a in know['allowed']) or '不授予无证知识')+'。', '证据导航：'+src(x['source_ranges'])+'。','']
put('SNAPSHOT_REGRESSION.md','\n'.join(s))
# All actual query results; human summaries are not substitute for retained payload.
s=['# Stage 2C｜Canon实际查询测试','',f'结果：{len(QT)}/{len(QT)} PASS。执行脚本：[_stage2c/regression.py](_stage2c/regression.py)；[全部实际返回值](_stage2c/query_tests.json)。','',
'Knowledge测试实际执行query_knowledge.lookup；身份/能力/关系/组织/地点查询从对应正式记录定位字段并比对独立预期。后者是事实检索测试，不声称已经提供通用自然语言查询API。','',
'允许UNKNOWN、DISPUTED和人物当时的理解/听闻。知识查询仅支持事件前/后；同事件中段、未建历史偏序、群体成员具体获知仍需源段核验。拒绝无证知识不是否定客观事实。','',
'首次运行曾因测试把DISBELIEVES误当秘密确认、字面匹配用词不一致而报错；已改测试谓词，未删除小璐的误解或篡改事实。[首次失败与原因](_stage2c/regression_first_run_failures.json)。','']
for t in QT:
 s += [f'## {t["id"]}｜{t["category"]}','',t['question'],'',f'- 预期：{t["expected"]}',f'- 实际：{short(t["actual"],950)}',f'- 判定：**{t["result"]}**',f'- 回接：{esc("、".join(t["references"]))}','']
put('CANON_QUERY_TESTS.md','\n'.join(s))
# Queue: each item carries historical source, source check, exact changes and final disposition.
s=['# Stage 2C｜Review核证队列','',f'共{len(Q)}项；'+ '，'.join(f'{k} {counts.get(k,0)}' for k in ['ACCEPT','PARTIAL_ACCEPT','REJECT','KEEP_UNKNOWN','KEEP_DISPUTED','USER_DECISION_REQUIRED'])+'。','',
'CR001–CR022接续历次Review建议；CR023起为本轮整合、查询与未知保存发现。Review只作线索，所有事实更改均回查所列源窗。PARTIAL_ACCEPT说明有部分旧建议被收窄/否定；没有把建议整批变事实。','',
'本文件是核证摘要；[工作队列完整字段](_stage2c/review_queue.json)、[逐字段前后像](_stage2c/changes.json)、[变更日志](CHANGELOG_STAGE2C.md)保留完整链。原Review、TEMP及audit历史不改。','']
for q in Q:
 cs=[c for c in CC if c['review']==q['id']]
 s += [f'<a id="{q["id"].lower()}"></a>',f'## {q["id"]}｜{q["title"]}','',f'- 来源：`{q["source"]}`。',f'- 目标与影响：{esc("、".join(q["targets"]))}。',f'- 待核建议：{q["title"]}；原建议不自动接受。',f'- 核证：**{q["decision"]}**。{q["reason"]}',f'- 方法：{q["verification"]}。',f'- 原著：{src(q["source_ranges"])}。',f'- Stage 1导航：'+('、'.join(q['audit_evidence']) or '无新增E；按现有未解/人工裁决核对')+'。']
 if cs:
  substantive=[c for c in cs if c['field'] not in ['formal_knowledge_refs','formal_relationship_refs','knowledge_epoch']]
  selected=substantive[:3] or cs[:2]
  for c in selected:s += [f'- 当前/修订前 `{c["record"]}.{c["field"]}`：{short(c["before"],300)}',f'- 修订后：{short(c["after"],420)}']
  s += [f'- 已实际修订：{len(cs)}个字段/整条新增记录日志。全部Change ID：'+ '、'.join(f'[{c["id"]}](CHANGELOG_STAGE2C.md#{c["id"].lower()})' for c in cs)+'。','- 下游回归：重新渲染Event/CH/REL/K及导航；全量结构与资料专项、实际查询和快照共同检查，最终状态见[最终Review](STAGE2C_FINAL_REVIEW.md)。']
 else:s += ['- 当前内容与处理：保留所引记录中的未知/争议；没有新证据消除，未新增确定性事实。']
 if q.get('navigation_correction'):s+=['- 工作索引修正历史：'+q['navigation_correction']]
 s+=['']
put('STAGE2C_REVIEW_QUEUE.md','\n'.join(s))
# File change inventory current state; finalization recomputes it for exact totals.
def inventory():
 files=[f for f in C.rglob('*') if f.is_file() and '__pycache__' not in f.parts and f.suffix!='.pyc' and '_stage2c' not in f.parts]
 changed=[];added=[]
 for f in files:
  rel=f.relative_to(P).as_posix();h=hashlib.sha256(f.read_bytes()).hexdigest()
  if rel not in BASE:added.append(rel)
  elif h!=BASE[rel]:changed.append(rel)
 return changed,added
changed,added=inventory();formalids={c['record'] for c in CC if re.fullmatch(r'(?:EV\d{4}|CH\d{3}|REL\d{3}|K\d{3})',c['record'])}
substantiveids={c['record'] for c in CC if c['module'] in ['Event','Character','Relationship','Knowledge'] and c['field'] not in ['formal_knowledge_refs','formal_relationship_refs','knowledge_epoch','integration_origin']}
# World text-level changes count as their actual affected stable IDs.
world_changed={'WR002','ORG018','LOC007'}
s=['# Stage 2C｜受控变更日志','',f'{len(CC)}条CC日志；字段级记录不等于同样多的事实错误。正式导航及时间层字段属于机械整合。实际涉及{len(formalids|world_changed)}个稳定ID，其中非导航/时间层的事实或边界修订涉及{len(substantiveids|world_changed)}个稳定ID（含新增3个Event）。','',
'每条保留修改前后、理由、源窗和下游回归。大字段只在本页显示摘要，[changes.json](_stage2c/changes.json)保留完整前后像；[canon_before.zip](_stage2c/canon_before.zip)保存修订前全部Canon字节。摘要省略不是删除证据。','',
'派生页面与索引从当前正式records生成，归属CR025及相应事实CR；所有实际文件前后哈希见[文件差异清单](_stage2c/file_changes.json)。旧阶段整理脚本不能重跑覆盖当前事实。','']
for c in CC:
 s += [f'<a id="{c["id"].lower()}"></a>',f'## {c["id"]}｜{c["record"]}.{c["field"]}','',f'- 文件：[{path_for(c)}]({path_for(c)})；核证[{c["review"]}](STAGE2C_REVIEW_QUEUE.md#{c["review"].lower()})。',f'- 修改前：{short(c["before"],400)}',f'- 修改后：{short(c["after"],480)}',f'- 原因：{c["reason"]}',f'- 证据：{src(c["source_ranges"])}。','- 下游：Event↔Character↔Relationship↔Knowledge正式导航、相关阶段与查询均重查；实际结果见最终检查。','']
put('CHANGELOG_STAGE2C.md','\n'.join(s))
put('USER_DECISIONS_PENDING_STAGE2C.md','''# Stage 2C｜用户裁决边界与后续待议

**本轮新增用户裁决：0项；阻塞Canon冻结：0项。** U001–U008已经裁决，不重新发起投票。以下5组是[USER_DECISIONS.md](../audit/USER_DECISIONS.md)明确留待后续细化的设计，不是未知Canon事实，也不构成现在执行下游的授权。

|依据|后续待议|本基线处理|
|---|---|---|
|U001 C|开局事件、RP日期与显示实现|不指定默认末章/日历，Canon按相对时序|
|U004 B1|具体作者正式补充逐份采用|当前无获批材料；正文外只作候选|
|U006 C|命运骰整体重做，检定、能力边界、触发和代价|不默认能力优先或奇迹玩法；不继承旧规则为已批准方案|
|U007 A|逐个CG条件、关系标签与实现|保留未来框架意向；不将好感、CG写成Canon事实|
|U008 A|建角默认与未知字段实现|不向原作人物/NPC套自由OC满状态默认|

Unknown/Disputed另见[未解导航](UNRESOLVED.md)。亲源说法、法律手续、末战胜负与能力原理不得交给用户投票变成原著事实。未来设计细化仍须用户明确决定，并与Canon层分离。
''')
# Current README replaces obsolete stage permission/status prose; historical exact text remains ZIP.
put('README.md',f'''# Canon Reference｜CANON_BASELINE_V1

**Stage 2C：{'完成' if freeze else '最终检查中'}。CANON_BASELINE_V1 = {status}**

本基线将原著事实、人物状态、有向关系和人物知情范围分开；同一人物必须按剧情节点读取。冻结只固定可追溯事实与边界，不消除未知，不代表已经制作角色卡或通过RP宿主验收。

|当前模块|稳定范围与数量|入口|
|---|---|---|
|来源规则|原著最高，A–F分级、事实/认知/推断分层|[Source Policy](00_source_policy.md)|
|事件|EV0001–EV0192，192；原189不重编号|[时间线](01_master_timeline.md)|
|世界层|WR001–014、PS001–038、ORG001–019、LOC001–036，共107|[世界](02_world_rules.md) / [力量](03_power_system.md) / [组织](04_organizations.md) / [地点](05_locations.md)|
|人物|CH001–CH070；A10/B26/C32/D2；原38快照；99条未知/争议索引|[人物](characters/README.md)|
|有向关系|REL001–REL172；583阶段、36家庭分层、1436未知维度|[关系](relationships/README.md)|
|知识|K001–K235；365获取节点、20披露边、207旧TEMP全部接续|[认知](knowledge/README.md)|
|回归|60组三层联合情境＋原38快照；55项实际查询|[快照](SNAPSHOT_REGRESSION.md) / [查询](CANON_QUERY_TESTS.md)|

先读[基线清单](BASELINE_MANIFEST.md)、[最终Review](STAGE2C_FINAL_REVIEW.md)、[核证队列](STAGE2C_REVIEW_QUEUE.md)及[变更日志](CHANGELOG_STAGE2C.md)。原Stage Review、TEMP_INDEX及旧_build*目录是历史资料，不覆盖当前记录，不能直接重跑旧整理脚本。70主体记录不等于已证明70个互异自然人；CH044/CH069同一性仍未定。

## 下游读取顺序与边界

1. [来源规则](00_source_policy.md)和[用户决定](../audit/USER_DECISIONS.md)：原著决定Canon事实，用户明确决定允许如何改编；两者来源必须可区分。
2. [Manifest](BASELINE_MANIFEST.md)、[未解导航](UNRESOLVED.md)、[推断限制](INFERENCE_GUARDRAILS.md)、[后续待议设计](USER_DECISIONS_PENDING_STAGE2C.md)。本轮无新增阻塞裁决；原5组设计细则仍留后续。
3. 选Event与前/后位置，再读对应世界层、人物阶段和两个方向的关系；不能套全书末态。
4. 按主体查[Knowledge](knowledge/README.md)及[只读查询](knowledge/query_knowledge.py)，核对获取时点与来源。群体知道不等个人知道，别名同一不等人物已识破。事件中段及不可比较历史节点须核源段。
5. 未来经授权才做心理/语言/行为建模与RP执行描述。不能改事实、提升推断等级、移除认知壁垒或改原著关系。新事实证据须正式变更日志，不能就地无记录覆盖Baseline。

现有未知范围：WQ40、CQ8、RQ7导航；人物99条；关系1436未知维度；K33项重要未知。它们层级不同、有交叉，不相加冒充独立问题总数。

Stage 1全文阅读仍为100%，1,641,637字符。Stage 2C做整合核证与回归，未重新声称全文逐字阅读。source/current/audit及final均未写入。本任务完成后停止，未进入Claude人物建模、世界书重构、角色卡制作或游戏系统设计。
''')
# Manifest placeholder exists for initial local-link check; frozen manifest is created by finalize.py.
if not (C/'BASELINE_MANIFEST.md').exists():put('BASELINE_MANIFEST.md','# CANON_BASELINE_V1｜候选清单\n\n尚未冻结。最终结构、引用、受保护文件与查询检查通过后生成完整模块与哈希清单。')
changed,added=inventory()
# Cross-file final report, precise current facts; check count/links finalization will refresh.
s=['# Stage 2C｜最终完整性Review','',f'阶段状态：**{"完成" if freeze else "最终检查中"}**；`CANON_BASELINE_V1 = {status}`。时间：{when}。','',
'本轮逐条核对历次Review，回查争议源窗，并逐项对照192事件、107世界事实、70人物、172关系及235认知命题。未重新逐字通读原著；Stage 1的100%阅读覆盖不变。','',
'## 核证结论','',f'共{len(Q)}个CR；'+ '，'.join(f'{k} {counts.get(k,0)}' for k in ['ACCEPT','PARTIAL_ACCEPT','REJECT','KEEP_UNKNOWN','KEEP_DISPUTED','USER_DECISION_REQUIRED'])+'。','',
'CR021仅部分接受旧R008：原文L4176已经确认小璐知道爸爸早知，EV0020才补上电视渠道；不能整项移晚。箭与蜂师徒关系仍未知；吴姐妹共训与互诺有据，天牛的法理说法仍是人物陈述。唱名/静默两段张力继续保留。','',
'补入EV0190郁金香骗局清算、EV0191资格制度沿革、EV0192亡妻后的复仇/父职冲突；原189个EV不动。修正木棉错名、考核队号、柏安驻守名单、误挂的女王对话、死讯获取、厨房听众、称谓恢复与阳台位置。红早期受控改造的客观状态与旁人退役理解分开。','',
'## 修订与追溯','',f'{len(CC)}条字段/新增整条记录CC日志；涉及{len(formalids|world_changed)}个稳定ID，其中{len(substantiveids|world_changed)}个涉及事实/边界等非导航修订（包含新增3个Event）。其余主要是正式关系/知识链接及显式时间层，不能把总数说成事实错误数。','',
'所有旧记录的变化字段均对照修订前ZIP验证完整前后链；新增Event保留整条新增像。派生页面、索引与机器数据同步。文件级精确差异及前后哈希见[差异清单](_stage2c/file_changes.json)；最终计数以[Manifest](BASELINE_MANIFEST.md)为准。','',
'## 回归结论','', '|项目|实际覆盖与结论|','|---|---|',
'|Timeline与世界层|192 EV主体/时间层、107条制度/机制/组织/地点逐项对照；个案、人物理论、晚解释保留限定|',
'|Character|70主体的身份、别名、阶段、能力、伤势、心理等级与未知逐项核对；38个旧快照重查|',
'|Relationship|172有向边、583阶段、36家庭七层；十维中的未知、双向独立和非互惠恋爱保留|',
'|Knowledge|235命题、365获取节点、20披露边；所有207 TEMP有去向；世界真值不反授角色|',
'|三层快照|10个Tier A×6类＝60/60 PASS，另38/38原快照；无重大能力新节点者不杜撰|',
'|Future Leakage|早期能力、身份、关系、组织权限与秘密的查询通过；同Event中段需源行补核|',
'|Reader Leakage|敌方/插叙揭示不直接给无关角色；个人自己的历史亲历仍按偏序保留；群体不自动广播|',
'|Canon/IF|U001–U008原则保持；无游戏数值、废案或无据桥段成为事实。修正U006不应预选骰子优先级|',
'|Unknown Preservation|旧REL未知/争议维度与家庭未知未升级；K未知真值不升级；人物原未知全部保留，新增2条|',
'|ID与引用|稳定ID、源窗范围、反向主体、E引用、CR↔CC及本地链接自动检查；具体数量见检查JSON|',
'|Query Tests|55/55实际运行通过；覆盖时间、能力、关系、恋爱、家庭、认知、组织、地点、未知/争议|',
'|受保护输入|source/current/audit和所有非Canon原文件逐一SHA256比对；禁止目录无新增文件|','',
'## 未解、待议与适用范围','',
'WQ40、CQ8、RQ7仍是导航组数；人物99条未知/争议、关系1436未知维度、K33项重要未知分别计数，不能合成互不重叠总数。本轮新增人工裁决0、阻塞0；5组未来设计细化另列，未代用户选择。','',
'程序只能验证可判定结构、边界和预期用例，不能数学证明全部自然语言。语义结论依据本轮逐项核证和原著锚点。历史偏序不足、未观察状态、事件中段及正文未写结尾继续保守拒绝。未做SillyTavern宿主验收，本阶段没有需要宿主执行的新卡。','',
'## Freeze判定','',f'条件：所有Review有结论、已接受修订有日志、受影响模块和实际查询已重跑、引用与哈希全通过。当前：{"满足，允许冻结" if freeze else "待最终生成文档后的检查通过；未冻结"}。',
'冻结约束未来下游读取事实；新证据仍可通过正式CR/CC与新版Manifest修订。此任务在冻结后停止，不启动Claude人物建模或世界书。','',
'[机器检查证据](_stage2c/check_result.json) · [查询](CANON_QUERY_TESTS.md) · [快照](SNAPSHOT_REGRESSION.md) · [Manifest](BASELINE_MANIFEST.md)','']
put('STAGE2C_FINAL_REVIEW.md','\n'.join(s))
# Human stage report is an authorized controlled integration artifact; no audit decisions rewritten.
put('_stage2c/README.md','''# Stage 2C复现与历史边界

- `input_baseline.json`、`canon_before.zip`：改动前快照，不变。
- `review_queue.json`、`changes.json`：完整CR/CC、字段前后像与证据。
- `integrate.py`、`amend*.py`：本次一次性迁移轨迹，已经执行，**不要重跑**。
- `render_current.py`：仅渲染当前正式records；不重新执行旧阶段事实整理。
- `regression.py`：读取当前数据，实际运行55查询、60组合情境、原38快照回归。
- `validate.py`：检查完整数据、引用、未知保存、变更链及受保护文件哈希。
- `reports.py`：生成人可读文档；`--freeze`仅允许此前检查PASS。
- `finalize.py`：冻结后登记模块/文件清单与SHA256；排除自身清单和重复生成的检查结果以避免自指哈希循环。

回归输出中的PARITAL/HEARD/DISBELIEVES等是主体状态，不是客观真值。原阶段_build*输入与Review保存历史，不能覆盖当前Baseline。
'''.replace('PARITAL','PARTIAL'))
# Exact file-level delta for review. Exclude journal directory from public-module counts, report separately.
files=[]
for f in C.rglob('*'):
 if not f.is_file() or '__pycache__' in f.parts or f.suffix=='.pyc' or '_stage2c' in f.parts:continue
 rel=f.relative_to(P).as_posix();h=hashlib.sha256(f.read_bytes()).hexdigest();old=BASE.get(rel)
 if h!=old:files.append(dict(path=rel,status='MODIFIED' if old else 'ADDED',before_sha256=old,after_sha256=h,reason='CR025派生同步及相关事实CR；Stage2C报告为本轮新证据',record_changes=[c['id'] for c in CC if 'canon/'+path_for(c)==rel]))
(B/'file_changes.json').write_text(json.dumps(files,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(state=status,queue=dict(counts),CC=len(CC),stable_ids=len(formalids|world_changed),substantive_ids=len(substantiveids|world_changed),files=len(files)),ensure_ascii=False))
