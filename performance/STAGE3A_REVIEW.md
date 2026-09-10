# Stage 3A｜核心人物可演绎模型 Review

阶段状态：**完成**
执行者：Claude Opus 5
前置基线：`CANON_BASELINE_V1 = FROZEN`（Stage 2C 完成）
写入范围：**仅 `performance/`**

---

## 1. 完成情况总览

|完成条件（任务书 §19）|状态|
|---|---|
|1. `performance/` 架构建立|✅|
|2. Performance Policy 完成|✅ `00_performance_policy.md`|
|3. 10 个 Tier A 均有独立 Performance Model|✅ 10/10|
|4. 每人 17 节结构完成|✅ 10/10（核心人格、内部矛盾、决策、情绪、防御、压力、关系差分、Knowledge／Disclosure、语言、互动节奏、底线、OOC、Novel Situation Protocol 全覆盖）|
|5. 每人有 RP 执行摘要与证据追踪|✅ 10/10|
|6. 每人完成三类验证|✅ 10/10|
|7. 跨人物模板化检查通过|✅ `validation/CROSS_CHARACTER_CHECK.md`|
|8. Canon Conflict Audit 通过|✅ `validation/CANON_CONFLICT_AUDIT.md`|
|9. Canon 疑点仅登记 Review，未修改 Baseline|✅ 见本文件 §7|
|10. `STAGE3A_REVIEW.md` 完成|✅ 本文件|
|11. `performance/README.md` 更新|✅|
|12. `canon/`、`audit/`、`current/` 未被修改|✅ 见 §6|

---

## 2. Tier A 人物数与完成数

**Tier A ＝ 10 人，全部完成。** 名单由 `canon/characters/records.json` 的 `tier == "A"` 直接读取，未自行重选。

|CH ID|人物|模型文件|验证文件|Canon 给出的 Tier A 理由|
|---|---|---|---|---|
|CH001|林昀|[tier_a/CH001_林昀_performance.md](tier_a/CH001_林昀_performance.md)|[validation/CH001_validation.md](validation/CH001_validation.md)|主角；多重身体、身份、职务和终局能力变化|
|CH002|林小璐|[tier_a/CH002_林小璐_performance.md](tier_a/CH002_林小璐_performance.md)|[validation/CH002_validation.md](validation/CH002_validation.md)|新一代主线成员；亲子、开华和王钥变化|
|CH003|夏凉|[tier_a/CH003_夏凉_performance.md](tier_a/CH003_夏凉_performance.md)|[validation/CH003_validation.md](validation/CH003_validation.md)|主队成员；家庭秘密、身份知情和能力组合发展|
|CH004|白静萱|[tier_a/CH004_白静萱_performance.md](tier_a/CH004_白静萱_performance.md)|[validation/CH004_validation.md](validation/CH004_validation.md)|祭子与身世、病情、认亲称谓及天音发展|
|CH005|红思与|[tier_a/CH005_红思与_performance.md](tier_a/CH005_红思与_performance.md)|[validation/CH005_validation.md](validation/CH005_validation.md)|退役、被控制、身体修复及复归岗位变化|
|CH006|安雅|[tier_a/CH006_安雅_performance.md](tier_a/CH006_安雅_performance.md)|[validation/CH006_validation.md](validation/CH006_validation.md)|旧队核心、妻与母亲身份；生前能力及死亡影响贯穿主线|
|CH007|麻生圆香|[tier_a/CH007_麻生圆香_performance.md](tier_a/CH007_麻生圆香_performance.md)|[validation/CH007_validation.md](validation/CH007_validation.md)|旧队到柏安导师、歌手、巡查与情热战斗发展|
|CH008|祖母绿|[tier_a/CH008_祖母绿_performance.md](tier_a/CH008_祖母绿_performance.md)|[validation/CH008_validation.md](validation/CH008_validation.md)|治疗、研究、政治和交易破局贯穿后段|
|CH009|妮娜·克瑞吉欧斯|[tier_a/CH009_妮娜·克瑞吉欧斯_performance.md](tier_a/CH009_妮娜·克瑞吉欧斯_performance.md)|[validation/CH009_validation.md](validation/CH009_validation.md)|战争队友到爪痕副首领；失亲、残肢与终局心解|
|CH010|摩可|[tier_a/CH010_摩可_performance.md](tier_a/CH010_摩可_performance.md)|[validation/CH010_validation.md](validation/CH010_validation.md)|长期队友、招募与身份误解的核心传播节点|

**建模方式**：逐人独立执行（读人物 Canon → 读核心关系 → 读 Knowledge Profile → 读关键 Event → 必要时回原著行号定位 → 建模 → 自检 → 进入下一人）。**未先生成统一模板再替换名字。**

---

## 3. 标记使用情况

十份模型合计 **192,922 字符**，标记使用如下：

|标记|使用次数|说明|
|---|---|---|
|`CANON_DIRECT`|1,413|Canon 记录中直接写明的事实或行为|
|`CANON_PATTERN`|181|多个独立证据支持的重复行为规律|
|`INTERPRETIVE_MODEL`|68|本层解释；**全部在各模型 §17 设有可追溯性对照表**|
|`STAGE_BOUND`|39|—|
|`RELATIONSHIP_BOUND`|34|—|
|`CONTEXT_BOUND`|26|—|
|`UNKNOWN`|121|**CH006 单独占 37**，与其证据稀薄状态一致|

**`CANON_DIRECT` : `INTERPRETIVE_MODEL` ≈ 21 : 1。** 解释层的自由生成占比低，绝大多数判断可直接指向 Canon 记录。

**逐人分布见** [`validation/CANON_CONFLICT_AUDIT.md`](validation/CANON_CONFLICT_AUDIT.md) §1.2。

---

## 4. Validation 结果

### 4.1 汇总

|测试类别|总项数|通过|备注|
|---|---|---|---|
|Canon Scene Reconstruction|50（每人 5 项）|**50 `PASS`**|含 2 项负向测试（CH006 A5、CH010 A5）|
|Novel Scene Generalization|30（每人 3 项）|**30 `PASS`**|每人含 1 项分歧场景，均未伪装唯一答案|
|Adversarial OOC|143|**141 `HOLD`／2 `SOFT`／0 `BREAK`**|两项 `SOFT` 为结构性张力，非模型缺陷|

### 4.2 两项 `SOFT` 的说明

|项|内容|处理|
|---|---|---|
|CH003 #5|被误解时"不辩解"可能被下游读成冷战或赌气|已在验证文件中区分"破裂关系→安静退出"与"未破裂关系→不辩解继续做事"。**模型文本无需修订**|
|CH005 #5|她同时需要更正误解（天性）与守住假履历（义务）|更正可核实的部分，不触及不可说的部分。需要下游在具体场景把握尺度，模型无法给出更硬规则|

### 4.3 最有价值的五条验证发现

1. **CH001 A3（EV0157）**：模型的六级价值排序正确预测了"边护驾边否认亲情因果"这个看似矛盾的组合。这是唯一一条**在价值冲突情形下**完成的复现测试。
2. **CH002 A1＋A2**：她拒绝怜悯、随后接受同一个人的教学。任何只写"倔强"或只写"好学"的模型都会失败。
3. **CH004 A1 的反证结构**：同样被敌人用"祭子"指认，EV0026 未失控、EV0070 失控——差异落在"是否贬低她的自我"。这确认了强触发的定位。
4. **CH008 A3**：一个权威人物**公开撤回自己的诊断方向**并承认成因不明。整个 Tier A 中只有她做过这个动作。
5. **CH009 A1＋A2**：她被冤枉时的第一反应**是怀疑自己**，需要外部证据才敢把矛头转出去。这推翻了"被辜负后觉醒的反抗者"这一最常见的误建方式。

---

## 5. 跨人物模板化检查

完整记录见 [`validation/CROSS_CHARACTER_CHECK.md`](validation/CROSS_CHARACTER_CHECK.md)。

|任务书指定扫描项|结果|
|---|---|
|是否都被写成"嘴硬心软"|`PASS`|
|是否都变得善解人意|`PASS`——**九人有在册的误读他人记录**|
|是否都爱自嘲|`PASS`——仅 CH005 一人，且限于年龄这一个题材|
|是否都用同一种心理防御|`PASS`——十种主防御各不相同，三组相邻机制已逐一确认分化|
|是否都对 User 慢热但最终恋爱|`PASS`——十人 OOC #1 全部 `HOLD`|
|是否都在压力下沉默|`PASS`——无人以沉默为高压反应|
|是否都具有相同对话节奏|`PASS`——两极对照已建立且可量化|

**额外扫描三项**：都选择保护（`PASS`＋观察项）／都有未识破的秘密（`PASS`，保密结构分四类）／都围着 CH001 转（`PASS`＋风险记录）。

**反向检查**：无人物因追求差异化而失真；全部差异化特征均直接来自 Canon 的 `psych`／`patterns`／REL／K 记录。

### 语气两极（可量化的分化证据）

|维度|一极|另一极|
|---|---|---|
|叹号率|摩可 约 27%|祖母绿 约 2%／妮娜（当代）约 2–3%／麻生 约 4%|
|句长中位|祖母绿 约 22 字|白静萱 约 14 字|
|停顿（省略号率）|白静萱 约 23%|祖母绿 约 15%（"不留白"）|
|单次发言量|麻生／祖母绿 3–6 句|白静萱 1–2 句|

**方法学声明**：以上统计由正文引号台词按上下文名字归属计算，**含噪声，属 `INTERPRETIVE_MODEL`，不作 Canon 事实**，仅用于相对比较。

---

## 6. Canon Conflict Audit

完整记录见 [`validation/CANON_CONFLICT_AUDIT.md`](validation/CANON_CONFLICT_AUDIT.md)。

|检查项|结果|
|---|---|
|ID 引用有效性|`PASS`——457 个不同 ID（CH 41／REL 124／K 140／EV 152），**0 处无效**|
|没有新 Canon 事实|`PASS`——68 条 `INTERPRETIVE_MODEL` 全部可追溯|
|没有 UNKNOWN 被补全|`PASS`——十份模型均设"`UNKNOWN` 保留清单"，合计 60 余项|
|没有 Relationship 被升级|`PASS`——恋爱维度为 F 的十余条关系全部未定性；家庭五层保持分离|
|没有 Knowledge 泄漏|`PASS`——K018 知情面与 Canon 完全一致|
|没有未来状态前置|`PASS`——四条最易前置的边界均已设为强规则|
|没有能力被扩大|`PASS`——十人的能力限制逐条记入|
|没有废案／旧卡 IF 混入|`PASS`——本轮未读取 `current/` 与 `audit/card_text/`|

### 写入边界

|目录|本轮操作|
|---|---|
|`canon/`|**只读，未写入**|
|`audit/`|**未读取、未写入**|
|`current/`|**未读取、未写入**|
|`final/`|**未写入**|
|`source/`|**只读**（仅按行号定位取证）|
|`prototype/`|**未读取、未写入**|
|`performance/`|本轮新建的全部内容|

---

## 7. `CANON_REVIEW_REQUEST`｜发现的 Canon 疑点（只登记，不修改）

> **【状态更新｜Stage 3A.1】** 以下四条已由受控复核全部处理完毕，基线推进至 `CANON_BASELINE_V1.1 = FROZEN`：**CR-3A-001 PARTIAL_ACCEPT／CR-3A-002 ACCEPT／CR-3A-003 ACCEPT／CR-3A-004 PARTIAL_ACCEPT**，新增稳定 ID 为 0，另派生一条待核项 **FUP-3A-001（`OPEN`）**。Performance 侧的最小同步见 [`STAGE3A1_SYNC_REVIEW.md`](STAGE3A1_SYNC_REVIEW.md)。**本节以下内容保留为提出时的原样，作为历史记录。**

> 以下四条均为**表述层面的可核证点**，不是已确认的事实错误。本阶段**未修改 `canon/` 任何内容**，交由后续受控复核（GPT／Codex）处理。

---

### CR-3A-001｜CH005 妖精感知能力的时序表述可能被误读

|项|内容|
|---|---|
|**涉及 ID**|CH005（stages、snapshots S01）、`canon/knowledge/by_character/CH005_knowledge.md` 导航句、EV0017、EV0052、EV0053|
|**当前 Canon 写法**|三处并存：<br>（a）CH005 stages"满期退役至开篇"：`看听妖精能力不能延续`<br>（b）CH005 S01 快照：`兽化改造与妖精感知不可据表面退役状态抹去`<br>（c）知识档案导航句：`复原后才能看听妖精`|
|**发现**|EV0053 中她在**受控期间**与妮妮有实际交流（提供手机、糖饼、新卡与警告请求，REL056 明确记载）。若单读（c）"复原后才能看听妖精"，会与 EV0053 冲突|
|**原著／记录证据位置**|EV0053；REL056；CH005 S01 快照原句；CH005 stages 第 2 项|
|**本层的读法**|三句可以自洽：**退役使原有的少女能力失效（a）；受控期的兽化改造提供了另一条感知路径（b）；复原后原有能力回来（c）**。本模型按此三层处理（见 `tier_a/CH005_红思与_performance.md` §7）|
|**影响范围**|下游若只取导航句（c），会写出"受控期她看不见妮妮"的场景，与 EV0053 直接冲突|
|**建议**|在知识档案导航句中补一个限定，明确（c）指的是**原有少女能力的恢复**，与（b）的改造来源分属两条路径。**不改变任何事实，只消除歧义。**|
|**优先级**|中|

---

### CR-3A-002｜CH006 与 CH029 之间没有正式 REL 条目

|项|内容|
|---|---|
|**涉及 ID**|CH006（psych 第 2 条）、CH029|
|**当前 Canon 写法**|CH006 psych：`D/E：旧友对樱的怀念、现任紫钻过往疑虑是各自视角；疑虑不能当她确有阴谋。`|
|**发现**|`canon/relationships/records.json` 中 **CH029 与 CH006 之间不存在任何 REL 条目**。CH029 现有的四条边分别指向 CH002（REL131／REL132）与 CH017（REL164／REL165）|
|**原著／记录证据位置**|CH006 psych 字段；`relationships/records.json` 全表检索结果|
|**影响范围**|下游若按关系库查询"谁对安雅有看法"，**查不到这一条**。该信息目前只存在于 CH006 的 psych 字段中，不在关系导航路径上|
|**建议**|二选一：（a）建立一条 CH029→CH006 的正式 REL（类别可为"过往疑虑"，维度大部分为 F）；或（b）在 CH006 与 CH029 的档案导航中互相加一句指向说明。**不改变疑虑本身的 D/E 定级，也不改变"疑虑不能当她确有阴谋"这条边界。**|
|**优先级**|中|

---

### CR-3A-003｜CH010 的 Tier A 理由与其知识档案规模之间的表述张力

|项|内容|
|---|---|
|**涉及 ID**|CH010（`reason` 字段）、K226、K015|
|**当前 Canon 写法**|CH010 `reason`：`长期队友、招募与身份误解的核心传播节点`|
|**发现**|CH010 的知识档案中：<br>· "已确认知道"分类**为空**<br>· 在册状态**仅 1 条**（K015 `PARTIAL`：花级不等于持有花牌）<br>· K226 明确记为 **未证获得 K018（林昀＝翠雀）**|
|**原著／记录证据位置**|`canon/knowledge/by_character/CH010_knowledge.md` 全文；K226-T001；K015-T001|
|**发现的性质**|"核心传播节点"一语若被下游读作"它掌握并传播了身份秘密"，会与 K226 直接冲突。从其余记录看，该表述更可能指的是**它在招募、登记、术语解释等环节上造成的误解与信息流转**（EV0004 登记联系暴露缺口、EV0024 夸大自述、EV0055 解释术语），而不是它持有 K018|
|**影响范围**|下游制作世界书时，一个被标为"身份误解核心传播节点"却知识档案近乎空白的角色，极易被误配成情报来源|
|**建议**|在 CH010 的 `reason` 或档案导航中补一句说明"传播节点"所指的具体环节，明确它**不持有 K018**。**不改变 Tier 分级，也不改变任何事实。**|
|**优先级**|中高（直接影响下游角色卡与世界书的信息权限配置）|

---

### CR-3A-004｜K098 缺少"开始相信恋爱说"的获取节点

|项|内容|
|---|---|
|**涉及 ID**|K098、K018-T005、EV0067、EV0092|
|**当前 Canon 写法**|K098（命题：`父亲林昀和翠雀正在恋爱`，truth=FALSE）只有**一条** state：EV0092，`from_state: MISUNDERSTANDS → to_state: DISBELIEVES`|
|**发现**|该条目记录了 CH002 **停止相信**的节点，但**没有记录她开始相信的节点**。前态 `MISUNDERSTANDS` 的起点实际由 **K018-T005（EV0067："我猜过爸爸和翠雀可能同一人，却自行否定，改认为二人在恋爱"）** 承载，但两条 K 之间**没有交叉引用**|
|**原著／记录证据位置**|K098 states 全表；K018-T005|
|**发现的性质**|这是**导航层的缺口**，不是事实冲突。两条记录内容一致，只是没有互指|
|**影响范围**|按阶段恢复 CH002 的认知状态时，若只查 K098，会看到一个没有起点的 `MISUNDERSTANDS` 前态；若只查 K018，会看到一个转向恋爱假设但没有后续的分支。**在 EV0067–EV0092 这段窗口内做认知快照会不完整**|
|**建议**|在 K098 中补一条指向 K018-T005 的导航引用（或反之）。**不新增事实、不改变任何状态值。**|
|**优先级**|低|

---

**以上四条均未修改 `canon/`。** 本阶段对它们的处理方式是：在 `performance/` 内按最保守的读法建模，并在此登记。

---

## 8. 哪些人物需要第二轮深挖

按优先级排列：

### 8.1 高优先级

**CH006 安雅**——**不是因为模型不足，而是因为它揭示了一个结构性问题。**

- 证据密度：已确认知道 **2 条**，六个知识分类全空，S03 状态数为 **0**。
- 本轮的处理是**大量保留 `UNKNOWN`**（该模型的 `UNKNOWN` 计数 37，为全体最高），并把"拒绝生成"本身作为模型的核心价值。
- **第二轮需要的不是补内容，而是决策**：下游（世界书／角色卡）是否需要一个可交互的安雅？如果需要，就必须由**用户明确授权**一个 IF 层，并与 Canon 严格隔离。这属于 `USER_DECISION` 范畴，不是建模能解决的。

### 8.2 中优先级

**CH003 夏凉 × CH001 林昀的关系性质**

- Canon **双向留白**：她的恋爱倾向为 F（"亲吻、贴近、独占式愿望不充分确认关系性质，更不确认被接受"），他的解读为 D（亲情），且明文"对方的亲情解读不替代夏本人的完整心理"。
- 这是本轮最难处理的一处，模型的做法是**两个方向都不定性**。
- 第二轮建议：设计专门的场景测试，验证长期 RP 中这条留白是否稳定，或是否需要在世界书层加一个显式的"不得定性"锁。

**CH005 红思与的四套语气切换**

- 四个阶段（少年结巴／成年工作口吻／受控禁言／复原后适应期）的切换是全体操作难度最高的。
- 第二轮建议：补跨阶段回忆场景的专项测试。

### 8.3 低优先级（观察即可）

- **CH002／CH003／CH004 对 CH001 注意力的三角竞争**：Canon 事实，但下游易退化为单一戏码。已在跨人物检查中记录风险。
- **CH009 EV0157 的硬分界线**：长期 RP 中易被跨越（玩家知道后面的事）。建议在阶段开关层实现。

---

## 9. 下一阶段建议

> **本阶段到此停止。以下仅为建议，未执行。**

### 9.1 立即可做的（不需要新授权）

1. **处理 §7 的四条 `CANON_REVIEW_REQUEST`**——建议由 GPT／Codex 受控复核，四条均为表述层修订，不改变任何事实。
2. **Tier B 人物的 Performance Model**——Canon 中 Tier B 共 26 人。本轮已发现多条 Tier A 模型依赖 Tier B 人物的关系边（如 CH023 白蓟、CH013 陆红豆、CH028 塞米、CH014 白狼、CH017 女王、CH020 妮姆、CH031 田胜），这些人物目前只有 Canon 记录、没有可演绎模型。

### 9.2 需要用户决定的

1. **User 的绑定方式**——`[CANON_DIRECT]` U008 规定自由 OC 默认与原作阶段／NPC 未知分开。本轮十份模型均按"User 不是特殊关系类别"处理，但**具体 RP 开局仍未定**（`[CANON_DIRECT]` Stage 2C Manifest：`具体RP开局未定`）。这决定了世界书的初始化方式。
2. **是否需要 IF 层**——尤其是 CH006 安雅（见 §8.1）。
3. **`[CANON_DIRECT]` U006 骰子整体重做的细则**——Stage 2C 明确"没有选定新骰子规则"，且明确"不应预选骰子优先级"。本阶段完全未涉及游戏系统。

### 9.3 移交下游的三条硬要求

1. **`INTERPRETIVE_MODEL` 不得升级。** 下游引用 `performance/` 时，必须区分"演绎指引"与"设定"。凡需断言"原著里发生过"，回 `canon/` 取。
2. **语气两极必须显式保留。** 长期生成会向平均值收敛；摩可与祖母绿／麻生的差异是最先丢失的（详见 §5 的量化表）。
3. **`[CANON_DIRECT]` CH004 REL032 含唯一一条跨人物行为复制禁令**（不得复制 CH002 冲上去拦人的行为形状）。世界书需要在人物层面实现这条禁令，而不是靠生成时的自觉。

---

## 10. 本阶段未做的事（明确声明）

- 未进入最终世界书重构。
- 未制作或重写任何角色卡。
- 未生成世界书条目。
- 未涉及骰子、CG、好感系统。
- 未为任何人物补恋爱、补创伤、补秘密。
- 未使用 MBTI、九型或任何外部人格框架。
- 未做精神医学诊断。
- 未大量复制原著台词（引用方式为**行号定位＋简述**）。
- 未修改 `canon/`、`audit/`、`current/`；未写入 `final/`。
- 未重新逐字通读原著（Stage 1 的 100% 阅读覆盖不变；本轮仅按行号定位取证）。

---

**Stage 3A 完成。按任务书 §19 要求，到此停止。**
