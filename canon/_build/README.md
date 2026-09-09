# 构建过程区｜不是Canon事实来源

本目录保留追溯资料和可重复的结构检查。**初始候选、旧检查快照和脚本内临时文本可能含已修正结论，不可当作有效设定使用。**

现行事件应读[records.json](../events/records.json)和[Master Timeline](../01_master_timeline.md)，再回查原著。原著仍是事实权威。

- initial_candidates.json：158条初始候选，原样保留，已被后续拆分和修订；不是现行Canon。
- revisions.json：构建修订痕迹，与各事件证据和当前记录配合使用。
- review_packet_*.json：已使用的原文定位窗口。词组匹配只辅助定位，不是自动事实证明。
- readonly_baseline.json：任务开始时的受保护输入路径与哈希基线。
- temp_registry.json：稳定TEMP分配映射，不因展示排序改变编号。
- check_result.json、link_check.json：最近结构/输入/链接检查结果。
- navigation_crosscheck.json：审计证据与遗漏导航的当前交叉引用结果；不以引用数量代替原文支持。
- evidence_disposition.json及其他批次文件：过程快照，可能早于最终事件数量；不得据此覆盖当前状态。
- checkpoint.json：本轮交付状态。完成后无正文续读断点。

脚本用于追溯构建方法。不要无差别从头重跑：refine.py、finish.py等早期脚本会重建旧候选阶段。render.py从当前records生成文档，check.py检查结构与输入；修改前先理解它们的具体写入行为。这里的程序日志和旧草稿不提升事实证据等级。
