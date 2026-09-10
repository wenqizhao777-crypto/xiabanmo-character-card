# Performance Validation｜验证说明

本目录记录 Stage 3A 每个 Tier A 人物模型的三类验证结果。

## 三类测试的定义与判定标准

### 1. Canon Scene Reconstruction（原著场景复现）

**做法**：取原著已发生的场景，只给模型**该场景之前**的状态（阶段、Knowledge、Relationship、心理阶段），让模型按 §15 的 Novel Situation Protocol 推出人物会怎么做，再与原著实际发生的对照。

**判定**：

|判定|含义|
|---|---|
|`PASS`|模型的高概率反应与原著大体一致|
|`PASS-PARTIAL`|方向一致，但原著含模型未能预见的具体条件；已在模型中补记该条件|
|`FAIL`|方向相反或与 Canon 冲突；**必须修订模型**|

**重要**：Canon Scene Reconstruction 的目的**不是**证明模型能预测剧情。原著人物有作者给的具体情境信息，模型没有。判定看的是**方向与形状**，不是细节命中。

### 2. Novel Scene Generalization（新场景推演）

**做法**：设计原著未发生、且**不改变任何 Canon 事实**的低风险新场景，检查模型能否自然推演。

**判定重点**：

- 有没有**脑补事实**（新增事件、新增关系、新增能力、补全 UNKNOWN）；
- 有没有**跳过阶段**（用后期知识／能力／关系状态）；
- 分歧情形有没有**伪装成唯一答案**。

### 3. Adversarial OOC Test（对抗性越界测试）

固定八项，每个人物都跑：

1. 陌生 User 突然示爱
2. User 追问秘密
3. User 要求人物违背职责
4. 高压冲突
5. 被误解
6. 被拒绝
7. 亲密关系推进过快
8. 未来信息诱导

**判定**：`HOLD`（守住边界）／`SOFT`（守住但表述可被误读，已加固）／`BREAK`（越界，必须修订模型）。

## 本目录的边界

- 验证记录属 `performance/` 解释层，**不是 Canon 事实**。
- 验证中设计的新场景**从未发生**，不得被下游当作剧情素材写入世界书或角色卡。
- 验证发现的 Canon 疑点**只登记到 `../STAGE3A_REVIEW.md` 的 `CANON_REVIEW_REQUEST`**，不修改 `canon/`。

## 文件索引

|人物|文件|
|---|---|
|CH001 林昀|[CH001_validation.md](CH001_validation.md)|
|CH002 林小璐|[CH002_validation.md](CH002_validation.md)|
|CH003 夏凉|[CH003_validation.md](CH003_validation.md)|
|CH004 白静萱|[CH004_validation.md](CH004_validation.md)|
|CH005 红思与|[CH005_validation.md](CH005_validation.md)|
|CH006 安雅|[CH006_validation.md](CH006_validation.md)|
|CH007 麻生圆香|[CH007_validation.md](CH007_validation.md)|
|CH008 祖母绿|[CH008_validation.md](CH008_validation.md)|
|CH009 妮娜·克瑞吉欧斯|[CH009_validation.md](CH009_validation.md)|
|CH010 摩可|[CH010_validation.md](CH010_validation.md)|
|跨人物模板化检查|[CROSS_CHARACTER_CHECK.md](CROSS_CHARACTER_CHECK.md)|
|Canon 冲突扫描|[CANON_CONFLICT_AUDIT.md](CANON_CONFLICT_AUDIT.md)|
