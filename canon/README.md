# Canon Reference

以原著为最高事实来源。先查[来源规则](00_source_policy.md)，再按已选剧情节点读取人物、关系与世界状态。旧报告中“本轮”指各自历史阶段，不能覆盖这里的现行构建状态。

## 当前完成度

**Stage 2B-4｜Knowledge & Information Boundary Canon Construction：完成。**

- [认知数据库](knowledge/README.md)：K001–K235，235条可引用命题；客观真值、人物所信、获取时点和披露边分开。
- 207个原Knowledge TEMP全部处理，16条归并、1条空壳退役、22条拆分；得到213条正式命题，另新增22条。[映射](knowledge/TEMP_TO_K_MAP.md)保留全部旧入口和处理理由。
- 10份Tier A认知档案、364个认知状态节点、20条单独披露边；[窄矩阵](knowledge/KNOWLEDGE_MATRIX.md)、[Transitions](knowledge/KNOWLEDGE_TRANSITIONS.md)、[传播链](knowledge/DISCLOSURE_CHAINS.md)。
- **Default Deny**：未证明角色知道，就不授予私人、秘密、组织内部及非公开能力知识。Scope只说明传播范围，不是实际持有人名单。
- PUBLIC、COMMON、ORGANIZATION_INTERNAL、ROLE_RESTRICTED、PRIVATE、SECRET、HIGHLY_SECRET、UNKNOWN_SCOPE分别处理；公告有时间点，组织知道不等所有成员知道。
- [38个快照核对](knowledge/SNAPSHOT_CHECK.md)、[172条关系认知边界](knowledge/RELATIONSHIP_CROSSWALK.md)、[70人物导航扫描](knowledge/CHARACTER_SCAN.md)均完成；9组上游建议只登记[Review](STAGE2B4_REVIEW.md)。
- [恢复规则](knowledge/RESTORE_POLICY.md)和[只读查询](knowledge/query_knowledge.py)支持按CH/EV选择有限知情；不输出整库客观真相，不能代替复杂历史中间节点的证据判断。
- 未选RP开局，未赋User全知，未改卡、未建游戏系统、未写final。后续阶段等待用户指定。

## 已完成的前置阶段

|阶段|交付|
|---|---|
|Stage 1|所给原著L1–38825、1,641,637字符，连续语义审计100%；[人工裁决8/8](../audit/USER_DECISIONS.md)|
|Stage 2A|189个稳定Event、207个Knowledge TEMP、49个Relationship TEMP；[时间轴](01_master_timeline.md)、[原检查](BUILD_CHECK.md)|
|Stage 2B-1|WR14、PS38、ORG19、LOC36，合计107条世界事实；[检查](STAGE2B1_REVIEW.md)|
|Stage 2B-2|CH001–CH070，A10/B26/C32/D2；36份完整/标准与34份简档，38个核心快照、97条人物未知/争议；[人物入口](characters/README.md)、[检查](STAGE2B2_REVIEW.md)|
|Stage 2B-3|REL001–REL172，582关系阶段节点、36家庭分层记录；49旧TEMP映射至40方向、另增132；[关系入口](relationships/README.md)、[历史检查](STAGE2B3_REVIEW.md)|

70个CH是主体记录数，CH044/CH069同一性尚未裁明，不等已经证明70个互异自然人。Stage 2B-2的319指受保护文件哈希核验数，其本地链接核验为2876；关系阶段另有独立检查。

## 读取与权威顺序

1. 原著正文：Canon事实最高来源，任何已建模块发现冲突都应回查源行。
2. [USER_DECISIONS.md](../audit/USER_DECISIONS.md)：如何偏离或扩展Canon的人工设计依据，不能改称原著事实。
3. 第一阶段最终审计及末次修订：问题和证据导航，不用过时历史快照覆盖后证。
4. Stage 2A时间线、Stage 2B-1世界层、Stage 2B-2人物、Stage 2B-3关系：各司其职，短摘要不代替所属模块的证据限定。
5. 旧角色卡：仅作问题来源，不证明原著关系或机制。

## 文件职责

|入口|用途|
|---|---|
|[00_source_policy.md](00_source_policy.md)|来源层、A–F等级、事实/认知状态、时间精度与IF隔离；其阶段性建设描述保留历史|
|[01_master_timeline.md](01_master_timeline.md)|189个事件及偏序；EV号不是严格年代排序|
|[events/records.json](events/records.json)|结构化事件；相关知识与关系旧TEMP引用保持稳定|
|[events/STATE_CHAINS.md](events/STATE_CHAINS.md)|跨事件状态链及迟到解释|
|[events/SOURCE_COVERAGE.md](events/SOURCE_COVERAGE.md)|442个源文标题与事件支持窗口导航，不是新的阅读覆盖率|
|[02_world_rules.md](02_world_rules.md)|世界制度、公开性与阶段|
|[03_power_system.md](03_power_system.md)|机制、实绩、解释与限制|
|[04_organizations.md](04_organizations.md)|组织及职务，不代证私人关系|
|[05_locations.md](05_locations.md)|地点与阶段状态|
|[characters/README.md](characters/README.md)|70份人物主体档案；旧关系导航经正式TEMP映射接续|
|[relationships/README.md](relationships/README.md)|当前有向关系正式入口；十维、阶段、家庭七层、主观与未知|
|[relationships/TEMP_INDEX.md](relationships/TEMP_INDEX.md)|Stage 2A历史原件，含已登记粗分/错挂；请经正式映射使用|
|[relationships/TEMP_TO_REL_MAP.md](relationships/TEMP_TO_REL_MAP.md)|49条旧入口全部去向与修订依据|
|[knowledge/README.md](knowledge/README.md)|正式K命题、主体认知、取得阶段、披露和信息壁垒；与世界事实、人物身份、关系事实分别负责|
|[knowledge/TEMP_INDEX.md](knowledge/TEMP_INDEX.md)|207个历史入口原件；必须经TEMP_TO_K_MAP接到正式库，不按旧错误主体/节点调用|
|[UNRESOLVED.md](UNRESOLVED.md)|世界WQ、人物CQ及关系RQ的未解导航|
|[INFERENCE_GUARDRAILS.md](INFERENCE_GUARDRAILS.md)|限制从个案、旁观解释、别名或缺字段推断完整事实|
|[STAGE2B3_REVIEW.md](STAGE2B3_REVIEW.md)|Stage 2B-3历史检查与6组上游建议；不静默修旧库|
|[relationships/_build2b3/README.md](relationships/_build2b3/README.md)|输入哈希、人工整理修订、扫描及检查；不是更高Canon权威|
|[STAGE2B4_REVIEW.md](STAGE2B4_REVIEW.md)|认知阶段检查、9组上游修订建议及未决边界|

## 稳定ID与后续边界

新知识命题从K236追加，既有K001–K235不因排序变化重编号；拆分、归并或退役保留旧入口与修订依据。

新关系从REL173追加；更改排序不能重编号。同一Source/Target不要因别名重复建边；如确须拆分，保留旧号与迁移去向。CH、EV、WR/PS/ORG/LOC继续沿其所属模块规则；本阶段未新增这些号。

关系末态不是永久默认。必须选事件阶段后再处理家庭、婚恋、师生、敌对与认知；合作不自动信任，信任不自动依赖，拥抱/接吻/表白不自动双向恋爱。家庭称呼、个人认同、相互承诺、共住、社会公开、法律和血缘分别读取。

Knowledge TEMP仅为导航，事件参与者不自动获得整件事件的所有命题。CH别名合并不代表当事人知晓同一身份。正式认知库已完成本阶段构建；游戏好感、CG、命运骰和RP推进仍属于后续授权阶段。

本阶段source/current/audit、既有世界/事件/人物/关系和历史Review均只读；只在knowledge目录、此README、STAGE2B4_REVIEW范围内变动。UNRESOLVED与INFERENCE_GUARDRAILS本轮无需重复补写，保持原件。上游问题只登记，不静默改写。未涉及SillyTavern宿主运行测试，也不代替用户验收。

World负责世界事实；Character负责人物客观身份与阶段；Relationship负责有向关系事实；Knowledge负责谁何时凭什么知道多少。下一阶段可以按用户授权处理上游建议或继续其他数据库，不能自动开始人物润色、世界书改写或游戏实现。
