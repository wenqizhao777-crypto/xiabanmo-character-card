# Canon Reference

以原著事实为中心、独立于旧角色卡的世界状态参考。先读本页与[来源及状态规则](00_source_policy.md)，再按需要查事件和原文。

## 当前完成度

**本轮「Canon架构＋Source Policy＋覆盖全部已提供原著的Master Timeline」已完成。**

- 189个稳定事件：EV0001–EV0189，按故事阶段呈现，ID不表示年代顺序。
- 207个知识TEMP命题、49条有向关系TEMP，保留各事件的持有人、认知前后态与传播渠道。
- 覆盖提供文件起始至卷二第282章《琥珀》末尾：L1–L38825，去换行1,641,637字符。第一阶段全文连续语义阅读100%的状态保留；本轮是据此进行状态提取及重要原文锚点回查，不宣称又进行了一遍逐字全文阅读。
- 全局复核、结构引用及只读输入检查见[完成检查](BUILD_CHECK.md)。事件支持窗口和章节导航覆盖不等于将每句静态事实都收入百科。

## 权威顺序

1. 原著正文：Canon事实最高来源。
2. [USER_DECISIONS.md](../audit/USER_DECISIONS.md)：用户明确偏离或扩展Canon的最高设计依据；IF不能因此变成原著事实。
3. 最终审计资料：定位、修订与质检导航；重要事实回接原著。
4. 旧角色卡：仅用于理解历史问题，不作为本库事实底稿。

## 文件职责与读取路径

|文件/目录|职责与状态|
|---|---|
|[00_source_policy.md](00_source_policy.md)|来源层、A–F等级、事实与认知状态、时间精度、用户边界及修订规则；已完成|
|[01_master_timeline.md](01_master_timeline.md)|按故事阶段导航的世界状态时间轴及189个完整事件；本轮主交付|
|[events/records.json](events/records.json)|与时间轴同步的结构化事件记录；字段保留来源和TEMP映射|
|[events/STATE_CHAINS.md](events/STATE_CHAINS.md)|能力/伤势、身份/关系、信息传播、迟到解释与未决张力的跨事件复核索引|
|[events/SOURCE_COVERAGE.md](events/SOURCE_COVERAGE.md)|442个源文标题区间到事件支持窗口或未单列原因的导航；不是新的阅读覆盖率|
|[characters/README.md](characters/README.md)|关联人物名称与事件导航；完整人物档案尚未建立|
|[knowledge/TEMP_INDEX.md](knowledge/TEMP_INDEX.md)|K_TEMP_001–207及传播边；正式知识数据库尚未建立|
|[relationships/TEMP_INDEX.md](relationships/TEMP_INDEX.md)|REL_TEMP_001–049有向关系及阶段变化；正式关系数据库尚未建立|
|[02_world_rules.md](02_world_rules.md)|世界规则模块骨架，按事件导航；尚未全面填充|
|[03_power_system.md](03_power_system.md)|能力体系模块骨架；本轮只在事件内保留能力转换|
|[04_organizations.md](04_organizations.md)|组织模块骨架；完整组织百科尚未建立|
|[05_locations.md](05_locations.md)|地点模块骨架；完整地点百科尚未建立|
|[BUILD_CHECK.md](BUILD_CHECK.md)|本轮完成检查、范围及未决事项|
|[_build/README.md](_build/README.md)|构建过程、原始候选、修订痕迹、检查脚本与检查结果；不是Canon事实来源|

## 接管边界与后续计划

本轮仅写canon/；source/、current/、audit/保持只读，final/禁止写入。未修改角色卡，未选RP开局，未实施骰子、CG、好感或玩法重构。

本轮没有未处理的后续正文区间，也不保留继续阅读断点。后续需在用户明确指令下，按事件及TEMP引用逐步建立人物、知识、关系与02–05模块；不自动启动这些工作。

新增事件从EV0190开始，知识TEMP从K_TEMP_208、关系TEMP从REL_TEMP_050开始；先检查现有命题/方向，避免重复建号。排序或拆分时保留已有ID与修订映射。正式数据库须保存TEMP→正式ID映射。

原著末尾未展示的结局仍为UNKNOWN。不得以“本轮完成”推断全部悬念已解决，也不得将骨架视为完整百科。
