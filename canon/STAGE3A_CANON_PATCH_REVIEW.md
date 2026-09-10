# Stage 3A｜四条 Canon 疑点受控复核

记录日期：2026-09-10（Asia/Shanghai）。当前交付状态由 [Baseline Manifest](BASELINE_MANIFEST.md) 和本文件末尾冻结汇总共同确定。

仅复核 CR-3A-001–004。原著是事实最高来源，[人工决定](../audit/USER_DECISIONS.md)决定允许的 IF 设计；[Performance Review](../performance/STAGE3A_REVIEW.md)是疑点来源，不是事实依据。没有重做 Stage 2C、重新全文审计、补全 UNKNOWN 或制作角色卡。

已读取当前来源规则、V1 Manifest、相关 Stage 2C 修订及四项涉及的 CH/K/REL/EV、快照与原著源窗。采用 code-quality-workflow 的局部受控修订流程；已读取 TavernWeave A0，用户附件已授权本批核证、最小修订、回归及冻结。执行前 V1 原机器清单 638 个文件哈希全部匹配；另保存本轮 933 个既有项目文件的哈希及完整旧 Canon 字节快照。历史数据见 [输入基线](_stage3a_patch/input_baseline.json)、[V1 原件 ZIP](_stage3a_patch/baseline_v1_canon.zip)。

## CR-3A-001｜红思与妖精感知时序

**结论：PARTIAL_ACCEPT；已做消歧。** 接受「退役表象不能抹去兽化受控期的实际感知」，不接受将「复原」直接解释为「恢复原封印魔力源及全部旧少女能力」。

- 原著依据：[L10619–10628](../source/下班，然后变成魔法少女_第1-282章.txt:10619)先交代退役者原魔力源封存及红的既往自述，再写林昀发现她目光跟随摩可。林昀的「从来没听说」是经验，不是穷尽世界机制的定律。[L10962–10989](../source/下班，然后变成魔法少女_第1-282章.txt:10962)把异常与兽化身体相接；[L11602–11627](../source/下班，然后变成魔法少女_第1-282章.txt:11602)直接写红给妮妮手机、糖饼并交流，发生在受控期。[L11678–11695](../source/下班，然后变成魔法少女_第1-282章.txt:11678)支持获救后恢复人形及感官，不能单独证明原封印力量全部归还。
- 既有 Canon：[CH005](characters/CH005_红思与.md) stages、S01、能力阶段；[EV0053 / EV0054](01_master_timeline.md#ev0053)，E160–E162；[REL056](relationships/REL056.md)；[K055](knowledge/K055.md)、[K056](knowledge/K056.md)、[K057](knowledge/K057.md)。S01 已明确当时能与妮妮交流，林昀至 EV0049 才发现异常；后续少女战力另接 EV0074 等节点。
- 修改：CH005 `stages` 的过宽否定收窄为常规退役与实际兽化状态分层；人物及 Knowledge 导航删除「复原后才首次能看听妖精」的误导，注明 EV0054 人形/感官与后来战力分别读取。修改前后见 P3A-001–005。
- 最小性：没有增加能力、完整感知机制或新恢复事件；S01、K055–057、EV0053/0054、REL056 原记录不变。兽化与感知异常已有证据，仍不把它形式化为两套已完整确证的独立系统。
- 下游：CH005 阶段读取、Knowledge Profile、Performance 能力时序。
- 局部回归：人物两处导航与 JSON 对照通过；全部原快照不变；相关 K/REL/EV 数据无变化；CH005 在 EV0017、EV0053、EV0054 的现有生产查询结果与 V1 相同。Performance 同步位置见下表。

## CR-3A-002｜紫钻对安雅的有向评价导航

**结论：ACCEPT；采用人物互链与矩阵导航，不新建 REL。**

- 原著依据：[L34287–34298](../source/下班，然后变成魔法少女_第1-282章.txt:34287)：现任紫钻向小璐说明与樱有公务接触、没有私交，回顾自己曾有的疑虑，也承认可能受到偏见影响。「有此评价/自述」有据，评价内容不等安雅确有阴谋。
- 既有 Canon：[CH006](characters/CH006_安雅.md) psych、[CH029](characters/CH029_现任紫钻.md) psych、[EV0135](01_master_timeline.md#ev0135)，E517；关系库未单建此方向。双方档案已有 D/E 的视角限制。
- 修改：两个人物 `relations` 与独立档案添加 **CH029→CH006** 同一方向的导航；[Relationship Matrix](relationships/RELATIONSHIP_MATRIX.md)添加「尚未单建 REL 的评价导航」。P3A-006–010。
- 最小性：此次材料足以使已有评价可被找到，无需增加长期亲疏、信任、义务、恋爱等维度。保留 D/E；不添加 CH006→CH029 的反向态度或知情，也不把「没有私交」写成二人从未接触。
- 下游：关系导航与 CH006 Performance 的 §8.6 引用；主体 CH029 的意见不能成为 CH006 自述。
- 局部回归：双人物及矩阵导航均可查到；172 个 REL / 583 阶段与 V1 完全一致，新增 REL 为 0；CH006 EV0158 的现有认知查询不变。

## CR-3A-003｜摩可的「传播节点」措辞

**结论：ACCEPT；仅收窄职责说明和权限导航。**

- 原著依据：[L751–778](../source/下班，然后变成魔法少女_第1-282章.txt:751)为摩可对来历、任命和联络行为的自述；[L4800–4828](../source/下班，然后变成魔法少女_第1-282章.txt:4800)为私下接触白静萱与招募说法；[L13787–13794](../source/下班，然后变成魔法少女_第1-282章.txt:13787)由白转述摩可谈到父亲/翠雀恋爱说。[L13935–13952](../source/下班，然后变成魔法少女_第1-282章.txt:13935)又区分谁向林昀说出误会，不能因为旁人先责怪摩可就确认所有传播边。
- 既有 Canon：[CH010](characters/CH010_摩可.md)、[K015](knowledge/K015.md)、[K226](knowledge/K226.md)；[EV0004](01_master_timeline.md#ev0004)、[EV0024](01_master_timeline.md#ev0024)、[EV0055](01_master_timeline.md#ev0055)。招募、解释、误会流转与 K018 身份秘密的授权是不同事情。
- 修改：Tier A reason 改为长期队友及招募、登记联络、术语解释、家庭关系误会的流转；明确 **未证获得 K018，不因 Tier A 或传播作用授予秘密**。人物/Knowledge Profile 同步说明 K226 仍 UNKNOWN。P3A-011–015。
- 最小性：Tier A 不变；不新增 K；不改变 K015/K226；「不持有」仅是当前无证不授予的调用边界，不能改写成原著已证明「永远不知道」或「任何情况下必须答错」。
- 下游：CH010 模型的权限设置、Tier 理由和秘密追问验收。
- 局部回归：K015/K226 完全保留；EV0004/0024/0055 均无变更；在 EV0004、EV0024、EV0055、EV0067、EV0158 查询 CH010 均不授予 K018；Profile 与人物导航一致。

## CR-3A-004｜K098恋爱误解来源导航

**结论：PARTIAL_ACCEPT；补充同一恋爱误解链的双向导航，不接受顺带加固「先猜同人、再主动否定」的强因果。**

- 原著依据：[L13835–13854](../source/下班，然后变成魔法少女_第1-282章.txt:13835)、[L13969–13983](../source/下班，然后变成魔法少女_第1-282章.txt:13969)明确当期小璐持有父亲/翠雀恋爱解释；[L20727–20751](../source/下班，然后变成魔法少女_第1-282章.txt:20727)中，L20746 是林昀听她陈述后的概括：她知道没有恋爱关系，但仍希望翠雀成为继母。保留转述层级，不伪作小璐逐字直言。
- 既有 Canon：[K018-T005](knowledge/K018.md) / EV0067 的内容含恋爱误解；[K098-T001](knowledge/K098.md) / EV0092 记录该误解被放下。K018 `DISBELIEVES` 否定「同一身份」，K098 `DISBELIEVES` 否定「正在恋爱」，两者不能按同名状态机械互换。
- 修改：K018/K098 JSON 新增 `cross_references`，双页、[CH002 Knowledge Profile](knowledge/by_character/CH002_knowledge.md)、[Transition 导航](knowledge/KNOWLEDGE_TRANSITIONS.md)接续同一主体和误解片段。来源锚点沿用 K018-T005 / L14075，纠正沿用 K098-T001 / L20884，不宣称锚点就是人物生命中首次产生想法的瞬间。P3A-016–021。
- 最小性：选择任务允许的「来源/双向导航」方案；原 truth、全部已有 states、获取时点、证据等级、事件和 ID 均不变，不新建 T 节点。更强的心理因果在本次关键源窗未直接核实，独立登记 [FUP-3A-001](STAGE3A_PATCH_FOLLOWUPS.md)，不静默修改旧判断。
- **查询边界：**生产 `query_knowledge.py` 未改。早期单独过滤 K098 的 states 仍无直接节点；调用者必须沿显式导航补读同主体、同阶段的 K018-T005，并且只读取「恋爱误解」片段。到 EV0092 采用 K098-T001 的原有纠正；不让来源片段覆盖后期状态。此补丁没有实现自动联查 API。
- 局部回归：使用真实生产查询提供阶段结果，再由测试侧按上述导航读取，不把测试辅助函数冒充新增生产能力。EV0003 后/EV0067 前不授予来源；EV0067 后、EV0078 后、EV0090 后、EV0092 前可导航来源；EV0092 后、EV0117 后优先直接纠正，共 8 个窗口通过。另验不能跨给 CH010。CH002 的 EV0067/EV0092 生产查询与 V1 完全一致。

## PERFORMANCE_SYNC_REQUIRED

Performance 全部保持只读，下表是后续同步清单，不代表已修复或已通过新的演绎验收。

|人物/范围|文件及段落|建议同步内容|
|---|---|---|
|CH005｜CR-3A-001|[Performance §7 L191](../performance/tier_a/CH005_红思与_performance.md:191)、[§17 L448](../performance/tier_a/CH005_红思与_performance.md:448)|去掉「复原后才重新能看听」造成的首次感知歧义；按受控交流、人形/感官获救、后续战力三个事实节点读，不补原封印力量全面恢复。|
|CH006｜CR-3A-002|[Performance §8.6 L218](../performance/tier_a/CH006_安雅_performance.md:218)|补 CH029→CH006 导航出处；保持紫钻的 D/E 评价方向和无反向授权。不是新增正式 REL。|
|CH010｜CR-3A-003|[Performance Tier L14](../performance/tier_a/CH010_摩可_performance.md:14)、[validation §C 第2行 L133](../performance/validation/CH010_validation.md:133)|同步收窄后的 reason；「未证获得」不能强化为客观上永远不知或必须答错。验收应禁止无证输出 K018，不强制演绎所有未知回应。|
|CH002｜CR-3A-004 / FUP-3A-001|[Performance L24](../performance/tier_a/CH002_林小璐_performance.md:24)，§6 L156、§8 L197、§9 L286–287、§17 L501；[validation A3 L35–41](../performance/validation/CH002_validation.md:35)|引用新误解来源导航和 EV0092 纠正；强心理因果需先核原证据，不能将本补丁当成已验证「自我否定式合理化」的证明。|

## 回归、修改范围与冻结汇总

具体逐项结果见 [局部回归 JSON](_stage3a_patch/regression_results.json)。检查包含旧记录逐字段对照、文本修改重放、稳定编号、跨文件导航、时间窗口、生产查询不变、V1 原件和只读输入哈希；不冒称重新跑完 Stage 2C 全量语义回归。

- 四条 Request：全部核证并处理。**ACCEPT 2、PARTIAL_ACCEPT 2、REJECT 0、KEEP_UNKNOWN 0、KEEP_DISPUTED 0。**
- 修改既有文件：**15**，其中人物/知识/关系导航及数据文件 **13**，版本入口 README / Manifest **2**。新建公开报告 **3**（本 Review、Changelog、Follow-ups）；工作脚本、前后像和冻结证据另存 `_stage3a_patch/`，不混入事实错误数。
- 新增稳定 EV/CH/K/REL/T：**0**；原 192 EV、70 CH、172 REL / 583 阶段、235 K / 365 获取节点、20 披露边、38 原快照均保留。
- 新 Follow-up：**1**，明确保留未知、后续复核；本轮四项受控修改无冻结阻塞。
- Performance Sync：**需要**；未修改 `performance/`，未进行新的模型演绎或宿主验收。
- 局部回归：**49 / 49 PASS**；290 个非 Canon 受保护文件哈希一致，无受保护目录新增文件。检查器发现并修正了自身对简档缺省字段及原矩阵特殊换行的处理；没有因此改写 Canon 事实。
- Baseline：**CANON_BASELINE_V1.1 = FROZEN**。V1 原件保留，最终哈希结果见 [冻结验证](_stage3a_patch/manifest_verification.json)。

完整前后像见 [Patch 日志](_stage3a_patch/patch_changes.json)；人读摘要见 [Changelog](CHANGELOG_STAGE3A_PATCH.md)。Stage 2C 的原 Review、CC001–CC1013 与机器清单保留为 V1 历史。
