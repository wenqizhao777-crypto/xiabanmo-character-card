# Performance｜Tier A 人物可演绎模型层

**阶段状态：Stage 3A 完成。**
前置基线：`CANON_BASELINE_V1 = FROZEN`

---

## 这一层是什么

`performance/` 是 **Canon 的解释层与执行层**，不是事实层。

它把已冻结的原著事实、行为证据、关系阶段与知识边界，翻译成"这个人在原著没写过的新场景里会怎么判断、怎么说、说到哪一步、不做什么"。

**它不产生任何新的原著事实。** 凡需断言"原著里发生过 X"，回 `../canon/` 或 `../source/` 取，**不要引用本目录**。

**冲突规则：若本层任何一句解释与 Canon 冲突，改本层，不改 Canon。**

---

## 读取顺序

1. **[`00_performance_policy.md`](00_performance_policy.md)** —— 标记系统、稳定人格 vs 阶段状态、关系差分原则、Knowledge/Disclosure 执行、User 原则、亲密关系防快餐化、互动节奏、Novel Situation Protocol。**任何使用本目录的人先读这一份。**
2. 对应人物的 `tier_a/CHxxx_*_performance.md`
3. 对应人物的 `validation/CHxxx_validation.md`（知道模型在哪些场景被测过、哪些地方需要判断）
4. [`STAGE3A_REVIEW.md`](STAGE3A_REVIEW.md) —— 本阶段总结、Canon 疑点登记、下一阶段建议

---

## 目录结构

```text
performance/
├─ README.md                    本文件
├─ 00_performance_policy.md     解释层规则（必读）
├─ tier_a/                      10 份 Tier A 人物模型
├─ validation/                  10 份验证记录 ＋ 跨人物检查 ＋ Canon 冲突扫描
└─ STAGE3A_REVIEW.md            阶段 Review
```

---

## Tier A 进度表

|CH ID|人物|代号／别名|模型|验证|状态|
|---|---|---|---|---|---|
|CH001|林昀|矢车菊／翠雀／龙胆|[模型](tier_a/CH001_林昀_performance.md)|[验证](validation/CH001_validation.md)|✅ 完成|
|CH002|林小璐|白玫|[模型](tier_a/CH002_林小璐_performance.md)|[验证](validation/CH002_validation.md)|✅ 完成|
|CH003|夏凉|小锦|[模型](tier_a/CH003_夏凉_performance.md)|[验证](validation/CH003_validation.md)|✅ 完成|
|CH004|白静萱|薄雪／小萱|[模型](tier_a/CH004_白静萱_performance.md)|[验证](validation/CH004_validation.md)|✅ 完成|
|CH005|红思与|朝颜|[模型](tier_a/CH005_红思与_performance.md)|[验证](validation/CH005_validation.md)|✅ 完成|
|CH006|安雅|樱|[模型](tier_a/CH006_安雅_performance.md)|[验证](validation/CH006_validation.md)|✅ 完成（**证据稀薄，见下**）|
|CH007|麻生圆香|玛格丽特／玛丽|[模型](tier_a/CH007_麻生圆香_performance.md)|[验证](validation/CH007_validation.md)|✅ 完成|
|CH008|祖母绿|研究院首席／林小姐|[模型](tier_a/CH008_祖母绿_performance.md)|[验证](validation/CH008_validation.md)|✅ 完成|
|CH009|妮娜·克瑞吉欧斯|墨荷／黑猫|[模型](tier_a/CH009_妮娜·克瑞吉欧斯_performance.md)|[验证](validation/CH009_validation.md)|✅ 完成|
|CH010|摩可|方亭市播种者|[模型](tier_a/CH010_摩可_performance.md)|[验证](validation/CH010_validation.md)|✅ 完成|

**Tier A 名单由 `canon/characters/records.json` 的 `tier == "A"` 直接读取，未自行重选。**

---

## 每份模型的 17 节结构

1. 模型定位（含该人物的硬约束清单）
2. 核心人格结构（需求／恐惧／价值排序／自我认知／内外落差）
3. 内部矛盾
4. 决策模型（Priority 1–3、Hard Limits、Exception Conditions）
5. 情绪处理与表达
6. 心理防御与回避
7. 压力与极端状态
8. 关系差分模型
9. 认知与保密执行（七档 ＋ Disclosure 规律 ＋ 速查表）
10. 语言执行模型
11. 互动节奏与主动性（五档主动性）
12. 底线与边界
13. 高风险 OOC 模式
14. Anti-Flattening
15. Novel Situation Protocol（含分歧记录）
16. RP 执行摘要
17. 证据追踪（含 `INTERPRETIVE_MODEL` 可追溯性对照与 `UNKNOWN` 保留清单）

---

## 使用本层时最容易出错的六件事

1. **把 `INTERPRETIVE_MODEL` 当成设定。** 它只能进入"演绎指引"区，不能进入"设定"区。
2. **忽略阶段。** 每个人物有 3–5 个快照阶段，知识量差距极大（例：CH002 从 3 条到 44 条；CH007 从 0 条到 15 条）。低阶段起局时严禁注入高阶段信息。
3. **把关系当成对称的。** REL 是有向边。A→B 与 B→A 可以完全不同，且大量维度记为 `UNKNOWN`。
4. **把"知道"当成"愿意说"。** 每份模型的 §9 都把知识分成七档，其中"知道但通常不主动说"和"明确保密"是两回事。
5. **把语气写成平均值。** 各人物的语气差异是可量化的（叹号率从约 2% 到约 27%），长期生成会自然收敛，需要显式保留。
6. **把 `UNKNOWN` 填满。** 尤其是 CH006 安雅——她在原著中的真实形态是"一个巨大的空白 ＋ 几个确凿的动作"。**把空白填满，比把她写扁更糟。**

---

## 关于 CH006 安雅的特别说明

她是 Tier A 中证据最稀薄的一位，而**这不是资料整理的疏漏，是原著的实际状态**：

- 开篇前已死亡，当代只以别人的记忆存在；
- 知识档案只有 **2 条**已确认条目，其余六个分类**全部为空**；
- 死后快照可返回状态数为 **0**。

因此她的模型的主要价值**不在于它能演什么，而在于它拒绝演什么**——不复活、不托梦、不写遗言、不祝福、不用别人的追忆冒充她的人格。下游引用时请**保留其 §0 的整段说明**，而不只是保留结论。

---

## 验证覆盖

|测试类别|总项数|结果|
|---|---|---|
|Canon Scene Reconstruction|50|50 `PASS`|
|Novel Scene Generalization|30|30 `PASS`|
|Adversarial OOC|143|141 `HOLD`／2 `SOFT`／**0 `BREAK`**|

横向检查：[跨人物模板化检查](validation/CROSS_CHARACTER_CHECK.md)（10 项扫描全部通过）、[Canon 冲突扫描](validation/CANON_CONFLICT_AUDIT.md)（457 个 ID 引用，0 处无效）。

---

## 边界声明

- 本目录**只写 `performance/`**。`canon/`、`audit/`、`current/`、`source/`、`prototype/` 均未修改，`final/` 未写入。
- 本阶段**未**进入世界书重构、角色卡制作、骰子／CG／好感系统设计。
- 发现的 Canon 疑点**只登记**在 [`STAGE3A_REVIEW.md` §7](STAGE3A_REVIEW.md) 的 `CANON_REVIEW_REQUEST`（共 4 条），**未修改 Baseline**。
