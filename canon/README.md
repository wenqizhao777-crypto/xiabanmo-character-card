# Canon Reference｜CANON_BASELINE_V1.2

**CANON_BASELINE_V1.2 = FROZEN**  
冻结时间：2026-09-11T00:34:53+08:00。本版将已应用的 FUP-3A-001 纠错正式收口；本轮新增事实修订为 0。

- FUP-3A-001：**RESOLVED / REJECT_CAUSAL_INTERPRETATION**。
- Tier A Performance 已完成此前同步；CH002 及相关对照项经 Stage 3A.3 同步至本版纠错结果，本轮只读核验。
- V1（Stage 2C）与 V1.1（Stage 3A Patch）均保留为历史冻结版本。
- 当前无阻塞 Stage 3B 的 Canon Follow-up；下一阶段可以在用户另行授权后进入 **Stage 3B**。本轮不启动。

当前入口：[V1.2 Manifest](BASELINE_MANIFEST.md)、[冻结 Review](STAGE3A4_BASELINE_V1_2_FREEZE_REVIEW.md)、[FUP 核证](FUP3A001_REVIEW.md)、[Changelog](CHANGELOG_FUP3A001.md)、[Follow-up](STAGE3A_PATCH_FOLLOWUPS.md)。旧报告中的“未同步/未冻结 V1.2”按其记录时点理解，当前状态以本入口和 Manifest 为准。

|当前模块|稳定范围与数量|入口|
|---|---|---|
|来源规则|原著最高，A–F分级、事实/认知/推断分层|[Source Policy](00_source_policy.md)|
|事件|EV0001–EV0192，192；原189不重编号|[时间线](01_master_timeline.md)|
|世界层|WR001–014、PS001–038、ORG001–019、LOC001–036，共107|[世界](02_world_rules.md) / [力量](03_power_system.md) / [组织](04_organizations.md) / [地点](05_locations.md)|
|人物|CH001–CH070；A10/B26/C32/D2；原38快照；99条未知/争议索引|[人物](characters/README.md)|
|有向关系|REL001–REL172；583阶段、36家庭分层、1436未知维度|[关系](relationships/README.md)|
|知识|K001–K235；365获取节点、20披露边、207旧TEMP全部接续|[认知](knowledge/README.md)|
|Stage 2C 历史回归|60组三层联合情境＋原38快照；55项实际查询|[快照](SNAPSHOT_REGRESSION.md) / [查询](CANON_QUERY_TESTS.md)|

## 本版纠错范围

相对 V1.1，仅纳入已核证的 EV0067、K018-T005、K098 限定导航及其时间线/页面/Profile/Transition 镜像修订，原 Change ID 为 F3A2-001–025；版本收口条目为 **FZ3A4-001**。全部稳定 ID、两命题客观 truth、误解起止锚点不变；未新增人物心理机制。

身份 K018：小璐在 EV0067 为 UNAWARE→UNAWARE；不得预设先猜中再否定。恋爱误解按 K098.cross_references 在 CH002 / CURRENT / point≥14075 且未到 K098-T001 的窗口显式读取；到 EV0092 使用原纠正状态。生产查询器不自动联查，两个命题不可互换。

## 下游读取顺序与边界

1. 先读[来源规则](00_source_policy.md)和[用户决定](../audit/USER_DECISIONS.md)：原著决定事实，用户明确决定允许如何改编。
2. 读当前 Manifest、[未解导航](UNRESOLVED.md)、[推断限制](INFERENCE_GUARDRAILS.md)、[后续待议设计](USER_DECISIONS_PENDING_STAGE2C.md)。既有未知与用户设计事项不因冻结而消失。
3. 选择 Event 及前/后位置，再读人物阶段、世界层及两个方向的关系；不得套全书末态。
4. 按主体使用[知识库](knowledge/README.md)和[只读查询](knowledge/query_knowledge.py)，再按明确约定补读限定导航。群体知情、读者知识、别名同一均不自动授予人物。
5. 本次 FUP 心理因果结论为 REJECT；原因 UNKNOWN。不得从“未识破”推断逃避，也不得反向补成终生从未怀疑、永远不回避等人格事实。Performance 的总结不反向定义 Canon。

既有 CH005 妖精感知阶段、CH029→CH006 有向评价、CH010 信息边界等 V1.1 修订继续有效，见[历史 Patch Review](STAGE3A_CANON_PATCH_REVIEW.md)。原世界 107 条、38 个原 Snapshot 保留。WQ40/CQ8/RQ7、人物99条、关系1436未知维度及 K33项重要未知采用原口径，不能相加充当独立问题总数。70主体记录不等于已证70个互异自然人；CH044/CH069 同一性仍未定。

## 历史与复验

V1、V1.1 原件、完整可还原目录及机器清单入口见 [Manifest](BASELINE_MANIFEST.md)。Stage 1 连续阅读仍为 100%，1,641,637 字符；Stage 2C/3A/3A.2/3A.3 的旧报告和回执按历史保存，不重写成当轮现状。

只读验证 V1.2：`python -X utf8 canon/_stage3a4/verify_freeze.py`。不要用旧版本哈希要求当前文件回退；不要重跑旧构建器或一次性补丁脚本覆盖当前资料。冻结固定文件、事实和引用边界，不代表已完成世界书、角色卡、RP 宿主测试或用户设计裁决。
