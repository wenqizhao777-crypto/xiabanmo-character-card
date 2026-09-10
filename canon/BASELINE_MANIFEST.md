# CANON_BASELINE_V1.2｜冻结清单

**CANON_BASELINE_V1.2 = FROZEN**  
冻结时间：2026-09-11T00:34:53+08:00。收口条目 **FZ3A4-001**；FUP-3A-001 = **RESOLVED / REJECT_CAUSAL_INTERPRETATION**。

## 版本历史

|版本|范围|历史保存|
|---|---|---|
|V1｜FROZEN|Stage 2C；2026-09-10T20:59:22+08:00|[原清单](_stage3a_patch/BASELINE_MANIFEST_V1.md)、[机器清单](_stage2c/baseline_manifest.json)、[完整历史 Canon ZIP](_stage3a_patch/baseline_v1_canon.zip)|
|V1.1｜FROZEN|Stage 3A Canon Review Patch；2026-09-10T23:11:14+08:00|[原清单字节副本](_stage3a4/BASELINE_MANIFEST_V1_1.md)、[原机器清单](_stage3a_patch/baseline_v1_1_manifest.json)、[完整历史 Canon ZIP](_stage3a4/baseline_v1_1_canon.zip)|
|V1.2｜FROZEN|FUP-3A-001 受控纠错收口版；2026-09-11T00:34:53+08:00|本文件、[本版机器清单](_stage3a4/baseline_v1_2_manifest.json)、[核验回执](_stage3a4/verification.json)|

V1.1 ZIP 按原机器清单逐项核验 654 个文件，并保留原 Manifest 及清单排除的4个当时记录，共659项；变化文件从 FUP 修订前原始字节还原，未把纠错后的工作副本冒充 V1.1。归档内原相对链接按 ZIP 根目录解释。冻结前（含 Stage 3A.2 状态横幅）的4个元数据原件另存 [before_metadata.zip](_stage3a4/before_metadata.zip)。旧版本均未覆盖。

## 相对 V1.1 的唯一事实/导航差异

已于 Stage 3A.2 完成，本轮不再次修改：

1. EV0067 撤回小璐“猜中再否定”的错误状态，同步时间线。
2. K018-T005 改为 UNAWARE→UNAWARE，保留当期分开看待两人及恋爱误解；truth 不变，knowledge_grade D→A 仅确认直接本人视角，correctness 为 UNKNOWN。
3. K098 既有来源导航增加恋爱片段，原起点14075与终止 K098-T001/20884 不变；不新建状态，不提供同一身份秘密，不自动联查。
4. 同步 K018/K098 页面、CH002 Knowledge Profile、Knowledge Transition 镜像。

对应7个事实/导航文件：`01_master_timeline.md`、`events/records.json`、`knowledge/records.json`、`knowledge/K018.md`、`knowledge/K098.md`、`knowledge/by_character/CH002_knowledge.md`、`knowledge/KNOWLEDGE_TRANSITIONS.md`。原变更条目 **F3A2-001–025**（包含该次元数据操作）；完整前后像见 [Changelog](CHANGELOG_FUP3A001.md)及[原机器日志](_fup3a001/changes.json)。本轮新增事实修订0，所有其他 Canon 事实不变。

## 当前模块与校验

稳定数量：EV192、CH70、REL172/583阶段、K235/365转移；世界层107条、原38快照、20披露边保持原口径。全部 EV/K/Transition ID 与原顺序不变；全部 Knowledge truth 和顶层 grade 不变。

|主文件|路径|SHA256|
|---|---|---|
|时间线|[01_master_timeline.md](01_master_timeline.md)|`ca71bcd9b6c6763d3acb92d512eccde20d637fe8b1d231e3cce9ba05727dd855`|
|Event|[events/records.json](events/records.json)|`2c3ae94c3ff078f559cd89d0a1db86b9559c5b8c18b4cf224b1124cd04be37e8`|
|Character|[characters/records.json](characters/records.json)|`1ed702b611cd798212d4c850cb98b3fdb7d31ef7acb0faa9f03fd9acd6a8aad8`|
|Relationship|[relationships/records.json](relationships/records.json)|`470f678162bdfd1ded8e03c96eefd7c8554658b1331a983256bb5811977a144f`|
|Knowledge|[knowledge/records.json](knowledge/records.json)|`161eb4f093b93c9b23f8908f8451cad52193b9eb0eb83f200a357432843c299a`|

所有纳入范围文件及 SHA256 见[机器清单](_stage3a4/baseline_v1_2_manifest.json)。覆盖当前 Canon 文件及保留的历史资料，排除缓存/pyc；为避免自指，Markdown Manifest、本版机器清单和本版核验回执不进入清单自己的哈希范围，排除列表在机器清单逐项记录。核验回执另存两个 Manifest 的哈希。

## 同步、未知与下一阶段

Tier A Performance 已与纠错后的 Canon 同步；本轮核对 [Stage 3A.3 Sync Review](../performance/STAGE3A3_CH002_SYNC_REVIEW.md)、CH002 实际模型/Validation、CH003 对照及跨人物检查。原被否决机制已删除、心理原因 UNKNOWN、Evidence Trace 已更新，无本项待核执行标签。原同步报告场景计数笔误及检查证据边界见[本版 Review](STAGE3A4_BASELINE_V1_2_FREEZE_REVIEW.md)。Performance 不进入 Canon 真值来源，本轮不改写。

当前无阻塞 Stage 3B 的 Canon Follow-up。WQ/CQ/RQ、其他未知与[用户待议设计](USER_DECISIONS_PENDING_STAGE2C.md)仍保留；User绑定/RP开局、IF范围、骰子细则不在本轮裁决。下一阶段可在另获授权后进入 Stage 3B，本轮到 Freeze 为止。

## 复验与历史解释

执行 `python -X utf8 canon/_stage3a4/verify_freeze.py`：只读核对本版清单、版本一致性、已核证内容、ID、同步材料及保护文件；不重写冻结数据或重新生成清单。核验结果写标准输出；落盘回执为冻结时原记录。

[FUP Review](FUP3A001_REVIEW.md)及其141项回归是 Stage 3A.2 当时证据；[Stage 3A Patch Review](STAGE3A_CANON_PATCH_REVIEW.md)与旧清单同理。不要重跑旧构建器、一次性补丁或旧版本冻结脚本覆盖本版。旧报告里的“未同步/未冻结 V1.2”不代表当前仍未完成。

本轮 source/audit/current/performance/final 保持只读；原著与旧卡哈希和全部冻结前文件哈希见[输入基线](_stage3a4/input_hashes.json)。未重新阅读原著、未重做 Stage 2C、未进入 Stage 3B 或最终制卡；无 RP 宿主验收声明。
