# Stage 3A.4｜Canon Baseline V1.2 冻结 Review

日期：2026-09-11（Asia/Shanghai）。**CANON_BASELINE_V1.2 = FROZEN**。FUP-3A-001 = **RESOLVED / REJECT_CAUSAL_INTERPRETATION**。本轮新增事实修订 **0**。

## 1. Freeze 前状态与授权范围

V1.1 为历史冻结版；当前工作副本已经包含 Stage 3A.2 的受控纠错，Stage 3A.3 已同步 Performance，但尚未冻结 V1.2。用户本次附件明确授权版本收口、必要元数据更新、轻量核验与冻结，不授权新的心理解释、Performance 修改或 Stage 3B。

沿 code-quality-workflow 执行局部核验与版本收口；已读取 TavernWeave A0（路由 code-quality-workflow / ST-A0，snapshot 2026-08-18，无采用的设计候选）。结构决定 No Refactor，执行为局部元数据收口。写前已固定 961 个既有项目文件的哈希，保留4个待更新元数据原件；只要内容偏离已核证变更、保护文件改变或冻结核验失败，就不能以最终冻结成功交付。

## 2. FUP 与 Canon 当前工作副本

读取 [FUP 原核证](FUP3A001_REVIEW.md)、[原 Changelog](CHANGELOG_FUP3A001.md)、[Follow-up](STAGE3A_PATCH_FOLLOWUPS.md)、原 Stage 3A Patch Review 和 Manifest。通过 F3A2-001–025 的 before/after 从修订前字节完整重放：冻结开始时10个受影响文件全部等于核证后的结果，无需要再改 Canon 的实际不一致。因此本轮未读取新原著正文，只计算保护哈希。

|对象|核对结果|
|---|---|
|EV0067|CH002 的身份命题 UNKNOWN→UNKNOWN，不再记录猜中后否定；白静萱原信息链不变。|
|K018-T005|UNAWARE→UNAWARE；有源的恋爱误解与未识破边界保留。knowledge_grade=A 仅指限定本人视角，不给心理原因升格；correctness=UNKNOWN。|
|K018 / K098 truth|与历史 V1.1 相同；各自命题不可互换。|
|K098|仅原来源导航增加限定恋爱片段；CH002 / CURRENT、起点14075、终止 K098-T001/20884 不变。生产查询不自动联查。|
|EV0092 / K098-T001|原纠正记录完整不变；DISBELIEVES 针对恋情，不授予身份秘密。|
|人物/关系/原快照|全部保持冻结前字节；本轮未修改任何事实或导航文件。|
|心理解释|被否决模型不作为 Canon 心理事实。原 E193/TEMP/构建脚本和历史报告只保留追溯，不是新的独立证据。|

本版相对 V1.1 的事实/导航差异只有上次 FUP 涉及的7个文件，其余差异均为已记录的历史资料新增或本轮版本元数据。Stable EV192、CH70、REL172/583阶段、K235/365转移及 ID 次序不变。本轮未重跑旧构建器、Stage 2C 或原一次性补丁。

## 3. Performance 同步核对

已读取 [Stage 3A.3 Review](../performance/STAGE3A3_CH002_SYNC_REVIEW.md)，并核对实际 [CH002 模型](../performance/tier_a/CH002_林小璐_performance.md)相关段落、[CH002 Validation](../performance/validation/CH002_validation.md)正文、CH003 模型/Validation 的对照项和跨人物检查。

- 被否决的“先猜同人→主动否定→恋爱合理化”已从执行规则删除；现存字样是已删除说明、禁止项、旧判据撤回或对抗测试输入，不算在用机制。
- 原 §15 的默认次优解释与“真相可承受度”条件已删除，相关心理原因明确 UNKNOWN；不重新赋予另一种默认心理动机。
- K018-T005 状态、K098 显式补读规则、Profile 3/0、20/2、26/2、44/2 查询数和 E193 主体混淆的 Evidence Trace 已同步。
- `tier_a/`、`validation/` 中未见本 FUP 的待核执行标签；其他人物“拦截/待核”“供词待核”属于不同含义，不为清零误删。
- CH003 和跨人物对照已撤回对小璐“把真相关掉”的依赖。

**同步核对：完成（针对本 FUP 的机制删除、认知状态与证据引用）。** 本轮没有把 Performance 反向写入 Canon。

### 回归记录与统计差异

|类型|Stage 3A.3 汇总|实际 Validation 文档核对|本轮证据边界|
|---|---|---|---|
|Canon Scene|6/6 PASS|A1、A2、重设计A3、A4-new、A5-new、原A4、原A5，共 **7项，均 PASS**|汇总少算1项；本轮记录差异，不修改 Performance 原件，不把旧A3再算一次。|
|Novel Scene|5/5 PASS|B1、B2、B3、B4-new、B5-new，5项均 PASS|核对已保存的推演与判定。|
|Adversarial OOC|15/15 HOLD，0 BREAK|#1–15 均 HOLD，#8旧判据撤回，#13–15含专项诱导|HOLD 表示守住规则，不是失败或未完成。|

这些是 Stage 3A.3 文档所载的局部推演/验证记录；本轮只读复核了它们与当前规则的一致性，没有另行调用模型生成，没有独立原始运行日志可供本轮复现实验，不能扩大为已通过真实酒馆运行或人类验收。

另一个非阻塞统计笔误：Sync Review §8 汇总写“6个文件修改+1新建”，其逐项清单实际列7个既有文件（含给旧 Review 加历史横幅）及1个新文件。本轮按实际文件记录取证，不沿用少算的总数。

### 防止同步摘要反向扩大 Canon

Performance 的“不是一个回避真相的人”（Validation L256）、“没有这个经历”及“被蒙在鼓里”等概括，不作为本次冻结的新事实：本版只承认特定证据链不能建立先猜中再否定，未识破原因 UNKNOWN；不证明她终生从未有疑问，也不排除原文已证的遮掩/隔离行为。现行模型对本项有明确不泛化和 UNKNOWN 限定；这些措辞的下游读取边界记在此处，本轮不做 Performance 润色或创建新心理模型。

上述统计/措辞记录不改变 Canon 内容，也不构成本 FUP 的新 Canon 冻结阻塞；后续不得把这份冻结报告当成对全部 Performance 性格推断的全面审计认可。

## 4. Changelog 与版本历史

既有 F3A2-001–025 含精确修改前/后、理由和原字节，无须重建另一套事实变更。现于原 Changelog 前增 **FZ3A4-001**，记录归入 V1.2、同步完成、原回归通过、Stable ID/truth不变及本轮无新增事实修订。原正文完整保留，读者可以区分 Stage 3A.2 当时状态与 Stage 3A.4 当前状态。

V1 原清单、ZIP 和 Stage 2C 记录全不改。V1.1 从原654项机器清单和 FUP 修订前字节还原、逐项验证，并补入原 Markdown Manifest 和4个自指/动态排除项，共659项，存入 [V1.1 ZIP](_stage3a4/baseline_v1_1_canon.zip)。原 V1.1 机器清单未覆盖，原 Manifest 字节单列存档。不是把纠错后的工作副本另起名字当作旧版。

V1.2 当前 [Manifest](BASELINE_MANIFEST.md) 和 [README](README.md)已替换旧的当前状态入口；[Follow-up](STAGE3A_PATCH_FOLLOWUPS.md)新增本轮收口说明，历史 OPEN、原提问、证据链、未同步/未冻结声明均保留为历史。

## 5. 最终轻量检查

验证命令：`python -X utf8 canon/_stage3a4/verify_freeze.py`。结果见 [verification.json](_stage3a4/verification.json)。脚本复验只读数据、向标准输出报告，不更新冻结资料。

检查包括：当前版本/Follow-up/Change ID一致；7个事实/导航文件精确匹配原 FUP 后像；稳定 ID、truth、原时间窗口；真实知识查询的身份拦截与纠正节点；同步关键引用与所载场景结果；V1.1还原字节；V1.2清单的覆盖、漏项、哈希；只允许4个原元数据文件改变；所有其他既有文件及保护目录的内容与路径集合不变；新增文件只在允许的本版 Canon 归档范围。

冻结前961个文件中仅4个元数据文件变化，其余957个字节不变。source、audit、current、performance、final的文件数、SHA256和新增/删除情况在机器回执逐项核对。没有新增原著阅读、没有修改旧卡、没有写入final。

本版机器清单覆盖当前 Canon 与历史档案；3个自指相关文件（Markdown Manifest、机器清单自身、核验回执）明确排除，回执另记Manifest哈希。排除不是删除历史证据，也不将Performance作为Canon清单的事实层。

## 6. 阻塞项、最终状态与停止边界

- 新 Canon 阻塞项：**0（本次受控冻结检查范围内）**。
- FUP-3A-001：**RESOLVED / REJECT_CAUSAL_INTERPRETATION**。
- V1.2 Freeze 条件：**满足**；最终状态 **CANON_BASELINE_V1.2 = FROZEN**。
- Tier A Performance：已同步到该纠错结果；场景统计按上文原记录与实际条目区分。
- WQ/CQ/RQ等未解事实、User绑定与RP开局、IF需求、骰子细则继续保留；不因本次冻结自动裁决。
- 下一阶段可以在用户另行授权后进入 Stage 3B。本轮结束，不进入 Tier B Performance、最终世界书或角色卡制作。
