# CANON_BASELINE_V1.1｜冻结清单

**CANON_BASELINE_V1.1 = FROZEN**
本轮记录时间：2026-09-10T23:11:14+08:00。四条 Stage 3A Canon Review Request 已核证；冻结仅在本轮局部回归通过后生效。

冻结固定当前可追溯事实、状态与导航边界，不代表未知已解决，不代表 Performance 已同步，不代表重做 Stage 2C 或完成 RP 宿主验收。

## 版本历史

- **V1：Stage 2C 冻结版**，原冻结时间 2026-09-10T20:59:22+08:00。
- **V1.1：Stage 3A 后受控 Canon Patch 版**；仅四项消歧/导航修订。ACCEPT 2 / PARTIAL_ACCEPT 2；无稳定 ID、已有 Knowledge 状态、truth 或等级变更。
- V1 原清单按原字节保存于 [BASELINE_MANIFEST_V1.md](_stage3a_patch/BASELINE_MANIFEST_V1.md)及 [baseline_v1_manifest.json](_stage3a_patch/baseline_v1_manifest.json)。前者是字节原件，内嵌相对链接仍按原目录解释；完整可还原目录上下文在 [V1 Canon ZIP](_stage3a_patch/baseline_v1_canon.zip)。原 [_stage2c/baseline_manifest.json](_stage2c/baseline_manifest.json)、Stage 2C Review/Changelog/检查证据均未覆盖。

## 当前模块与稳定范围

|模块|范围/状态|入口|主文件SHA256|
|---|---|---|---|
|Source Policy|来源、证据A–F、权限|[00_source_policy.md](00_source_policy.md)|`0f89d55e939240bf236778683b09fb039eb5eeb72876cf5eb8aa252a658ea5dd`|
|Master Timeline|EV0001–EV0192；192|[01_master_timeline.md](01_master_timeline.md)|`dd46ecc789df9d354e3b88f57d9a1c825d6b46c9beebed3d7a86c1324570be31`|
|Event JSON|192，知识时间层显式；新增EV0190–0192|[events/records.json](events/records.json)|`e873cf0d34e4ab49e1e199fe9ec102c713d1bb49b11f3cf319b04fe5605382e7`|
|World Rules|WR001–WR014；14|[02_world_rules.md](02_world_rules.md)|`a93ac418254a27250636f4c52746f781ebf94e7b0f4412875e2c6b47a0e211d8`|
|Power System|PS001–PS038；38|[03_power_system.md](03_power_system.md)|`2c300d01395c10199f7ad12b79db15d654b715e729aee87b326f2b24f4a2f0d0`|
|Organizations|ORG001–ORG019；19|[04_organizations.md](04_organizations.md)|`58b85804dcd8dea815be68191db04cba39cb4da170899c499a90fc9544e5432a`|
|Locations|LOC001–LOC036；36|[05_locations.md](05_locations.md)|`864222e82fcce213829e91d01f1ee7442a3ad0a833131a0255473d53693a0ca8`|
|Characters|CH001–CH070；70；A10/B26/C32/D2|[characters/records.json](characters/records.json)|`1ed702b611cd798212d4c850cb98b3fdb7d31ef7acb0faa9f03fd9acd6a8aad8`|
|Relationships|REL001–REL172；172／583阶段／36家庭分层|[relationships/records.json](relationships/records.json)|`470f678162bdfd1ded8e03c96eefd7c8554658b1331a983256bb5811977a144f`|
|Knowledge|K001–K235；235／365获取／20披露|[knowledge/records.json](knowledge/records.json)|`063dacf9b9c26f6839a1158c7558d8f6915de89d7b93f767eed04703733661c1`|
|Unresolved|WQ001–040、CQ001–008、RQ001–007|[UNRESOLVED.md](UNRESOLVED.md)|`bae720195245ced28c635f75ed3323e1264552b90212eace34d39c0a6912041b`|
|Inference Guardrails|主观/推断/未知与Canon/IF限制|[INFERENCE_GUARDRAILS.md](INFERENCE_GUARDRAILS.md)|`9e648804c1e99a11c3e307bc05c17d5fabcc833e6556c703ee78400ce6880a8c`|
|V1历史 Snapshot Regression|60组合＋原38快照|[SNAPSHOT_REGRESSION.md](SNAPSHOT_REGRESSION.md)|`22d2b7836e78b2bf7e2053f6e3d86bbd4b863e63bc3a39cbfbf29590dba5eb45`|
|V1历史 Query Tests|55实际查询PASS|[CANON_QUERY_TESTS.md](CANON_QUERY_TESTS.md)|`27576bcb213e9f23378fa0495c6366ad6176a8dfeb7f11a4d8d3e9f230f70ab0`|
|V1历史 Review Queue|CR001–CR036；全部有结论|[STAGE2C_REVIEW_QUEUE.md](STAGE2C_REVIEW_QUEUE.md)|`df87002ce6aaec85e26ab1b7d27c318be9113aa849c512a8cf6ac3650a4e53f9`|
|V1历史 Changelog|CC001–CC1013；完整前后像另存JSON|[CHANGELOG_STAGE2C.md](CHANGELOG_STAGE2C.md)|`3a321b646356d4e8b723affef7e1a11dab217652b405b277986bf1c6fb7b5c15`|
|V1历史 Final Review|Stage2C完成；不进入下游|[STAGE2C_FINAL_REVIEW.md](STAGE2C_FINAL_REVIEW.md)|`471d4f645e02d6760e696f945c462019c25f577991d04727f912bced8aa6b430`|
|Stage 2A Check|历史完成检查，不当当前计数|[BUILD_CHECK.md](BUILD_CHECK.md)|`29d37188d84a5ba13e5ffe2951cacd692cec6235ff070a0548fb543299b7b7cd`|
|Stage 2B1 Review|历史原件保留|[STAGE2B1_REVIEW.md](STAGE2B1_REVIEW.md)|`9ecf1c5381dbbdc64fb9098bc1f56f71bb42b1abd158f83ec629788b01e7afdb`|
|Stage 2B2 Review|历史原件保留|[STAGE2B2_REVIEW.md](STAGE2B2_REVIEW.md)|`088f99fe2fd9775e97f345e23b918f4385d161cd628ba64d781a400603990ec2`|
|Stage 2B3 Review|历史原件保留|[STAGE2B3_REVIEW.md](STAGE2B3_REVIEW.md)|`6d257dc227b7e0ea2be749e40d0a4223c03295096950bdbc3c33c0d296e5afe7`|
|Stage 2B4 Review|历史原件保留|[STAGE2B4_REVIEW.md](STAGE2B4_REVIEW.md)|`af3e225725ed4c564f0abd22519ecc07015b4795268bde398bd1aa158fe76344`|


人物 70、关系 172、知识 235 份正式档案及现行导航纳入 [V1.1 机器哈希清单](_stage3a_patch/baseline_v1_1_manifest.json)。原世界 107 条、38 快照、20 披露边保持原口径。旧 Stage 2C 报告只作为历史检查证据，上表有明确标记。

## 本轮 Patch 与回归

- [Patch Review](STAGE3A_CANON_PATCH_REVIEW.md)、[Changelog](CHANGELOG_STAGE3A_PATCH.md)、[逐字段前后像](_stage3a_patch/patch_changes.json)、[版本入口前后像](_stage3a_patch/version_changes.json)。
- 15 个既有文件变更：13 个局部数据/导航文件，2 个版本入口。新增公开报告 3 份；辅助证据单列于 [文件变化清单](_stage3a_patch/patch_file_changes.json)。稳定 ID 新增 0。
- [局部回归](_stage3a_patch/regression_results.json)：49 项检查，包含 8 个显式导航恢复窗口、8 个真实生产查询前后对照，以及编号/字段/镜像/输入保护。K098 补的是显式导航，**没有改造生产查询器使其自动联查**。
- 原事件/关系数据、所有既有知识状态/真值/等级/披露、人物 Tier/psych/原快照保持不变。旧 Stage 2C 的 43 组检查、55 项查询、60 组联合情境为 V1 历史结果，本轮不伪称重新执行。
- [冻结验证回执](_stage3a_patch/manifest_verification.json)独立核验当前文件哈希、两个 Manifest、V1 保存与只读输入。

## 未知、后续同步及用户边界

既有 WQ40/CQ8/RQ7、人物99条、关系1436维度、K33项重要未知的口径不变，不相加冒充独立问题数。原用户5组后续设计细则仍待议，见 [专表](USER_DECISIONS_PENDING_STAGE2C.md)。

新 [FUP-3A-001](STAGE3A_PATCH_FOLLOWUPS.md)仅登记 K018-T005 强因果证据链待复核；本轮保留原状态，不新增结论。四项受控修改没有冻结阻塞。**PERFORMANCE_SYNC_REQUIRED** 见 [Review 同步表](STAGE3A_CANON_PATCH_REVIEW.md#performance_sync_required)，未改写 Performance，也没有宣称下游已同步。

## 输入保护与哈希范围

本輪开始记录 933 个既有项目文件，其中 290 个非 Canon 文件逐一核对；source/current/audit/performance/final 均未改动，保护目录无新增文件。原 V1 638 项机器清单在修改前全部匹配；另外保留完整现有 Canon 字节快照，不以 V1 的旧哈希否定有日志的 V1.1 修改。

原著 SHA256：`18819c3060f411fd8bbb24e859657d24a7628317aed18c9106831f73eb250fa2`。

旧卡 SHA256：`3d6a1d85f42d0980aac7ce9ff62f0a94d51f3c5c3272c3eaedf39ef1b8bd517d`。

V1.1 机器清单覆盖 Canon 正式资料、历史原件和本轮脚本/前后像；缓存/pyc 排除。为避免自指循环，当前 Markdown Manifest、机器清单本身、局部检查回执、文件变化清单、冻结验证回执不进入自己的哈希范围；排除路径在机器清单逐项列明，验证回执另记两个当前 Manifest 和检查回执的哈希。

复核本补丁可运行 `python -X utf8 canon/_stage3a_patch/check_patch.py`；随后只读核验执行 `python -X utf8 canon/_stage3a_patch/finalize_patch.py --verify`。检查回执可更新，受冻结的正文不得无日志重建。不要重复运行一次性 `apply_patch.py`，不要重跑旧构建器覆盖当前数据。

未进入 Stage 3B、世界书重构、骰子/CG/好感系统；未修改角色卡或写入 final。后续只按新授权继续。
