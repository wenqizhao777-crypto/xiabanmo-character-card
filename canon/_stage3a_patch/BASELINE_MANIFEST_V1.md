# CANON_BASELINE_V1｜冻结清单

**CANON_BASELINE_V1 = FROZEN**
冻结记录时间：2026-09-10T20:59:22+08:00。Stage 2C已完成。

冻结表示后续不得无记录改变Canon事实、阶段与知情壁垒；不是删除未知，也不是保证原著未写的结局。新证据可经正式变更日志和新版Manifest修订。

## 模块清单与稳定范围

|模块|范围/状态|入口|主文件SHA256|
|---|---|---|---|
|Source Policy|来源、证据A–F、权限|[00_source_policy.md](00_source_policy.md)|`0f89d55e939240bf236778683b09fb039eb5eeb72876cf5eb8aa252a658ea5dd`|
|Master Timeline|EV0001–EV0192；192|[01_master_timeline.md](01_master_timeline.md)|`dd46ecc789df9d354e3b88f57d9a1c825d6b46c9beebed3d7a86c1324570be31`|
|Event JSON|192，知识时间层显式；新增EV0190–0192|[events/records.json](events/records.json)|`e873cf0d34e4ab49e1e199fe9ec102c713d1bb49b11f3cf319b04fe5605382e7`|
|World Rules|WR001–WR014；14|[02_world_rules.md](02_world_rules.md)|`a93ac418254a27250636f4c52746f781ebf94e7b0f4412875e2c6b47a0e211d8`|
|Power System|PS001–PS038；38|[03_power_system.md](03_power_system.md)|`2c300d01395c10199f7ad12b79db15d654b715e729aee87b326f2b24f4a2f0d0`|
|Organizations|ORG001–ORG019；19|[04_organizations.md](04_organizations.md)|`58b85804dcd8dea815be68191db04cba39cb4da170899c499a90fc9544e5432a`|
|Locations|LOC001–LOC036；36|[05_locations.md](05_locations.md)|`864222e82fcce213829e91d01f1ee7442a3ad0a833131a0255473d53693a0ca8`|
|Characters|CH001–CH070；70；A10/B26/C32/D2|[characters/records.json](characters/records.json)|`3c121e09f5a7b9acd34b7503053b2bdf7b65e40e4b1c20a0b4fe2713da3d245d`|
|Relationships|REL001–REL172；172／583阶段／36家庭分层|[relationships/records.json](relationships/records.json)|`470f678162bdfd1ded8e03c96eefd7c8554658b1331a983256bb5811977a144f`|
|Knowledge|K001–K235；235／365获取／20披露|[knowledge/records.json](knowledge/records.json)|`97617ee0df80e4b0ec28baef2fbc53b97ee43560e4a98491c82c3c6d9e6564f0`|
|Unresolved|WQ001–040、CQ001–008、RQ001–007|[UNRESOLVED.md](UNRESOLVED.md)|`bae720195245ced28c635f75ed3323e1264552b90212eace34d39c0a6912041b`|
|Inference Guardrails|主观/推断/未知与Canon/IF限制|[INFERENCE_GUARDRAILS.md](INFERENCE_GUARDRAILS.md)|`9e648804c1e99a11c3e307bc05c17d5fabcc833e6556c703ee78400ce6880a8c`|
|Snapshot Regression|60组合＋原38快照|[SNAPSHOT_REGRESSION.md](SNAPSHOT_REGRESSION.md)|`22d2b7836e78b2bf7e2053f6e3d86bbd4b863e63bc3a39cbfbf29590dba5eb45`|
|Query Tests|55实际查询PASS|[CANON_QUERY_TESTS.md](CANON_QUERY_TESTS.md)|`27576bcb213e9f23378fa0495c6366ad6176a8dfeb7f11a4d8d3e9f230f70ab0`|
|Review Queue|CR001–CR036；全部有结论|[STAGE2C_REVIEW_QUEUE.md](STAGE2C_REVIEW_QUEUE.md)|`df87002ce6aaec85e26ab1b7d27c318be9113aa849c512a8cf6ac3650a4e53f9`|
|Changelog|CC001–CC1013；完整前后像另存JSON|[CHANGELOG_STAGE2C.md](CHANGELOG_STAGE2C.md)|`3a321b646356d4e8b723affef7e1a11dab217652b405b277986bf1c6fb7b5c15`|
|Final Review|Stage2C完成；不进入下游|[STAGE2C_FINAL_REVIEW.md](STAGE2C_FINAL_REVIEW.md)|`471d4f645e02d6760e696f945c462019c25f577991d04727f912bced8aa6b430`|
|Stage 2A Check|历史完成检查，不当当前计数|[BUILD_CHECK.md](BUILD_CHECK.md)|`29d37188d84a5ba13e5ffe2951cacd692cec6235ff070a0548fb543299b7b7cd`|
|Stage 2B1 Review|历史原件保留|[STAGE2B1_REVIEW.md](STAGE2B1_REVIEW.md)|`9ecf1c5381dbbdc64fb9098bc1f56f71bb42b1abd158f83ec629788b01e7afdb`|
|Stage 2B2 Review|历史原件保留|[STAGE2B2_REVIEW.md](STAGE2B2_REVIEW.md)|`088f99fe2fd9775e97f345e23b918f4385d161cd628ba64d781a400603990ec2`|
|Stage 2B3 Review|历史原件保留|[STAGE2B3_REVIEW.md](STAGE2B3_REVIEW.md)|`6d257dc227b7e0ea2be749e40d0a4223c03295096950bdbc3c33c0d296e5afe7`|
|Stage 2B4 Review|历史原件保留|[STAGE2B4_REVIEW.md](STAGE2B4_REVIEW.md)|`af3e225725ed4c564f0abd22519ecc07015b4795268bde398bd1aa158fe76344`|

人物全部70份、关系172份、知识235份正式Markdown档案及导航均纳入[机器文件哈希清单](_stage2c/baseline_manifest.json)，不只记录四个JSON。模块入口分别见[人物](characters/README.md)、[关系](relationships/README.md)、[认知](knowledge/README.md)。

## 未解与用户设计边界

WQ40、CQ8、RQ7为分层导航；人物99条未知/争议、关系1436未知维度、K33项重要未知。它们跨层重叠，不相加计算独立问题数。既有UNKNOWN/DISPUTED没有为冻结而升级。

新增USER_DECISION_REQUIRED：0；Canon冻结阻塞：0。原用户决定中5组后续设计细化仍待议，见[专表](USER_DECISIONS_PENDING_STAGE2C.md)和[人工决定原件](../audit/USER_DECISIONS.md)。具体RP开局未定；U006没有选定新骰子规则。

## 回归与输入安全

43组全量结构、引用、变更链、未知保存及安全检查PASS；55实际查询PASS；60组三层联合情境PASS；原38快照复核通过。最终重新运行结果见[检查JSON](_stage2c/check_result.json)及[冻结后哈希验证](_stage2c/manifest_verification.json)。

262个非Canon受保护文件逐一SHA256匹配；source/current/audit保持只读，final无写入。保护清单见[input_baseline.json](_stage2c/input_baseline.json)。

原著：`18819c3060f411fd8bbb24e859657d24a7628317aed18c9106831f73eb250fa2`。

旧卡：`3d6a1d85f42d0980aac7ce9ff62f0a94d51f3c5c3272c3eaedf39ef1b8bd517d`。

## 修改统计与可追溯性

公开模块与报告变动287文件（原有修订280、新建7）。1013条CC包含机械导航和整条新增记录，不是1013个事实错误；共涉及443个稳定ID，其中54个涉及非导航/时间层的事实或边界等修订。

[文件前后哈希](_stage2c/file_changes.json)、[逐字段完整前后像](_stage2c/changes.json)、[改动前原件ZIP](_stage2c/canon_before.zip)。EV旧189个ID保留，新增从0190追加；CH/REL/K原编号不重排。

## 哈希范围与复现边界

机器清单覆盖Canon正式文件、现行数据、历史Review和构建工作证据；缓存/pyc不纳入。为避免自指哈希循环，清单自身、本Markdown、file_changes.json、check_result.json、manifest_verification.json不纳入自身哈希；验证回执另记录两份Manifest的哈希。它们的角色与排除范围明确，不伪称文件能包含自己的固定哈希。

旧_build*与一次性integrate/amend脚本是历史工作，不可重跑回退当前事实。重复检查使用[_stage2c/regression.py](_stage2c/regression.py)、[_stage2c/validate.py](_stage2c/validate.py)和[_stage2c/finalize.py --verify](_stage2c/finalize.py)。重新生成报告会改变文档哈希，须作为新修订处理。

未运行SillyTavern宿主：此任务没有构建新卡或界面；未进入Claude人物建模、世界书重构或IF/Game Layer。后续只在用户明确授权后开始。
