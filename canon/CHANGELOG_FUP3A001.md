# Stage 3A.2｜FUP-3A-001 最小纠错 Changelog

## FZ3A4-001｜纳入 V1.2

记录时间：2026-09-11T00:34:53+08:00。**CANON_BASELINE_V1.2 = FROZEN**。

- 关联：FUP-3A-001，RESOLVED / REJECT_CAUSAL_INTERPRETATION；原逐字段变更 F3A2-001–025 全部保留。
- 修改前（V1.1）：EV0067 对小璐误记 SUSPECTED→REJECTED；K018-T005 误记 SUSPECTS→DISBELIEVES 与“先猜中再否定”；K098 仅有旧来源导航。
- 修改后（已在 Stage 3A.2 应用，本轮只冻结）：EV0067 UNKNOWN→UNKNOWN；K018-T005 UNAWARE→UNAWARE，保留有源恋爱误解；K098 显式限定片段与原起止导航。理由：电话验证主体混淆，原文不支持指定因果链；详见原 Review。
- 稳定 EV/K/Transition ID、全部命题 truth、获取时点不变；T005 D→A 只确认有直接证据的有限认知事实，未提升心理解释。
- Performance Sync：Stage 3A.3 **已完成并核对**；原 Stage 3A.2 局部回归 141 PASS 保留，本轮执行版本/内容/同步/哈希轻量核验。未重跑全量 Stage 2C 或模型生成。
- 本轮 Canon 事实/导航变更：**0**。仅4个现有版本/归档元数据文件更新，另建本版 Review、清单和核验材料。
- 原 Stage 3A.2 文本与 before/after 历史保留；下文“尚未同步/未冻结新版本”是当时状态。详见[冻结 Review](STAGE3A4_BASELINE_V1_2_FREEZE_REVIEW.md)与[Manifest](BASELINE_MANIFEST.md)。

---

复核/补丁启动：2026-09-10；收尾验证：2026-09-11（Asia/Shanghai）。结论：REJECT_CAUSAL_INTERPRETATION；Follow-up：RESOLVED。

这是当前工作副本的受控补丁，不是新的冻结版本。历史 V1.1 的原机器清单及旧 Changelog 均保留。仅本条错误状态及必要导航/展示同步；没有新增稳定 ID。

## 变更依据与影响

FEV02–03 证明电话验证/同人提问主体是夏凉；FEV05–09 证明小璐的恋爱误解，而未建立“先猜同人再否定”；FEV11–12 支持后来放下恋情而仍未识破身份。证据编号见 [Review](FUP3A001_REVIEW.md)。

K018-T005 的状态/第一人称内容纠错是事实记录层纠错；K098 恋爱片段及各页面是必要导航同步。D→A 仅确认明确内心所支持的未识破/恋爱误解，不确认心理防御模式。EV0092、K098-T001、两命题客观 truth、所有获取时点和 ID 均不变。

## 逐项变更

|Patch ID|文件|记录/字段|性质及前后记录|
|---|---|---|---|
|F3A2-001|[events/records.json](events/records.json)|EV0067 / later_informed|撤回未证的先猜同人/主动否定；保留未识破与恋爱误解；精确 before/after 见机器日志同号条目。|
|F3A2-002|[01_master_timeline.md](01_master_timeline.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-003|[events/records.json](events/records.json)|EV0067 / knowledge|撤回未证的先猜同人/主动否定；保留未识破与恋爱误解；精确 before/after 见机器日志同号条目。|
|F3A2-004|[01_master_timeline.md](01_master_timeline.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-005|[knowledge/records.json](knowledge/records.json)|K018-T005 / state_record|撤回未证的先猜同人/主动否定；保留未识破与恋爱误解；精确 before/after 见机器日志同号条目。|
|F3A2-006|[knowledge/records.json](knowledge/records.json)|K098 / cross_references|原有恋爱起点导航增限定片段，时点及结束转移不变；精确 before/after 见机器日志同号条目。|
|F3A2-007|[knowledge/K018.md](knowledge/K018.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-008|[knowledge/K018.md](knowledge/K018.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-009|[knowledge/K018.md](knowledge/K018.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-010|[knowledge/K018.md](knowledge/K018.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-011|[knowledge/K018.md](knowledge/K018.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-012|[knowledge/K018.md](knowledge/K018.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-013|[knowledge/K018.md](knowledge/K018.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-014|[knowledge/K098.md](knowledge/K098.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-015|[knowledge/by_character/CH002_knowledge.md](knowledge/by_character/CH002_knowledge.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-016|[knowledge/by_character/CH002_knowledge.md](knowledge/by_character/CH002_knowledge.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-017|[knowledge/by_character/CH002_knowledge.md](knowledge/by_character/CH002_knowledge.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-018|[knowledge/KNOWLEDGE_TRANSITIONS.md](knowledge/KNOWLEDGE_TRANSITIONS.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-019|[knowledge/KNOWLEDGE_TRANSITIONS.md](knowledge/KNOWLEDGE_TRANSITIONS.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-020|[knowledge/by_character/CH002_knowledge.md](knowledge/by_character/CH002_knowledge.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-021|[knowledge/by_character/CH002_knowledge.md](knowledge/by_character/CH002_knowledge.md)|页面 / text|文本/导航同步；精确 before/after 见机器日志同号条目。|
|F3A2-022|[STAGE3A_PATCH_FOLLOWUPS.md](STAGE3A_PATCH_FOLLOWUPS.md)|页面 / text|Follow-up 结案或当前未重新冻结状态说明；保留历史；精确 before/after 见机器日志同号条目。|
|F3A2-023|[STAGE3A_PATCH_FOLLOWUPS.md](STAGE3A_PATCH_FOLLOWUPS.md)|页面 / append|Follow-up 结案或当前未重新冻结状态说明；保留历史；精确 before/after 见机器日志同号条目。|
|F3A2-024|[README.md](README.md)|页面 / text|Follow-up 结案或当前未重新冻结状态说明；保留历史；精确 before/after 见机器日志同号条目。|
|F3A2-025|[BASELINE_MANIFEST.md](BASELINE_MANIFEST.md)|页面 / text|Follow-up 结案或当前未重新冻结状态说明；保留历史；精确 before/after 见机器日志同号条目。|

## 原判断、原因与回退材料

完整 before/after 与修订原因：[changes.json](_fup3a001/changes.json)（25 个操作，10 个既有文件）；修订前的原始文件字节：[before.zip](_fup3a001/before.zip)。运行前 951 个项目文件哈希：[input_hashes.json](_fup3a001/input_hashes.json)。这些材料保留旧判断与变更路径，不静默抹去历史。

audit E193、Stage 2A TEMP、旧建库脚本和以往冻结报告不改；它们属于被本条纠正的历史派生链。旧构建脚本不应直接重生成覆盖当前纠错。

## 验证与后续边界

局部回归 **141 PASS / 0 FAIL**；EV 192、K 235、Transition 365，编号、truth 与获取时间不变；原 951 文件中仅日志覆盖的 10 个 Canon 文件变化，其余 941 个不变。271 个只读输入文件全部哈希相同。真实查询与手动恋爱片段导航分别测试；原 CH002 Snapshot 未改。完整结果及首次检查脚本问题说明见 [Review 第7节](FUP3A001_REVIEW.md#7-局部回归与保护检查)和 [verification.json](_fup3a001/verification.json)。

Performance 文件全部只读；需按 Review 第6节同步并重跑 CH002 局部 Validation。没有新模型生成验收，也没有新基线冻结。
