# Stage 2B-3 构建与检查材料

本目录不是Canon权威。curation.py是逐方向人工整理，build.py只渲染relationships下文件；禁止把关键词命中当关系判定。正式记录见上级目录。

- input_baseline.json：本阶段写入前415个项目文件哈希；允许写入范围外逐一对比。
- curation_changes.json：原文复核后的初稿修改原因、前后值；不取代审计历史。
- character_scan.json：全部70条输入导航、建模与未单建决定。
- statistics.json：由最终正式数据计算的计数。
- check.py / check_result.json：编号、引用、阶段字段、方向、迁移及受保护文件校验。
- semantic_review.md：定点语义复核的证据、范围与剩余未知。

执行build.py会更新本阶段关系文件；不修改原TEMP_INDEX、人物、世界、事件、知识、source/current/audit。未涉及SillyTavern宿主测试。
