# Stage 3A Canon Patch｜变更日志

日期：2026-09-10（Asia/Shanghai）。仅对应四条 CR；完整逐字段前后像见 [patch_changes.json](_stage3a_patch/patch_changes.json)，旧 Canon 字节见 [V1 ZIP](_stage3a_patch/baseline_v1_canon.zip)。本日志不替换 Stage 2C 的 CC001–CC1013。

P3A-001–021 是 13 个既有数据/导航文件的局部修改，并非 21 个事实错误；事实真值、既有知识状态、稳定编号均不变。P3A-022–023 是版本入口更新，不是 Canon 事实修订。所有回归明细见 [regression_results.json](_stage3a_patch/regression_results.json)，核证解释见 [Review](STAGE3A_CANON_PATCH_REVIEW.md)。

## P3A-001｜CR-3A-001

- 修改文件：[characters/records.json](characters/records.json)；记录/字段：`CH005 / stages`。
- 修改前：退役阶段笼统写看听妖精能力不能延续。
- 修改后：区分常规退役封存与兽化受控期已有交流。
- 核证依据：EV0053/0054、REL056、K055–057、CH005 S01；L10619–10628、10962–10989、11602–11627、11678–11695。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Knowledge Profile / CH005 Performance。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-002｜CR-3A-001

- 修改文件：[characters/records.json](characters/records.json)；记录/字段：`CH005 / knowledge`。
- 修改前：导航称复原后才能看听妖精。
- 修改后：受控交流、林昀后知、人形感官恢复与后续战力分层。
- 核证依据：EV0053/0054、REL056、K055–057、CH005 S01；L10619–10628、10962–10989、11602–11627、11678–11695。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Knowledge Profile / CH005 Performance。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-003｜CR-3A-001

- 修改文件：[characters/CH005_红思与.md](characters/CH005_红思与.md)；记录/字段：`正文 / exact_text`。
- 修改前：人物阶段表同样笼统否定感知延续。
- 修改后：镜像 JSON 阶段消歧。
- 核证依据：EV0053/0054、REL056、K055–057、CH005 S01；L10619–10628、10962–10989、11602–11627、11678–11695。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Knowledge Profile / CH005 Performance。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-004｜CR-3A-001

- 修改文件：[characters/CH005_红思与.md](characters/CH005_红思与.md)；记录/字段：`正文 / exact_text`。
- 修改前：人物 Knowledge 导航有首次感知歧义。
- 修改后：镜像 CH005 knowledge 的阶段限制。
- 核证依据：EV0053/0054、REL056、K055–057、CH005 S01；L10619–10628、10962–10989、11602–11627、11678–11695。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Knowledge Profile / CH005 Performance。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-005｜CR-3A-001

- 修改文件：[knowledge/by_character/CH005_knowledge.md](knowledge/by_character/CH005_knowledge.md)；记录/字段：`正文 / exact_text`。
- 修改前：按人知识页继承旧导航。
- 修改后：镜像 CH005 knowledge 的阶段限制。
- 核证依据：EV0053/0054、REL056、K055–057、CH005 S01；L10619–10628、10962–10989、11602–11627、11678–11695。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Knowledge Profile / CH005 Performance。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-006｜CR-3A-002

- 修改文件：[characters/records.json](characters/records.json)；记录/字段：`CH006 / relations`。
- 修改前：CH006 relations 缺少紫钻视角入口。
- 修改后：添加 CH029→CH006 的 D/E 公务接触及评价导航，不推反向。
- 核证依据：CH006/CH029 psych、EV0135（E517）；L34287–34298，D/E 不变。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Relationship Matrix / CH006 Performance。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-007｜CR-3A-002

- 修改文件：[characters/CH006_安雅.md](characters/CH006_安雅.md)；记录/字段：`正文 / exact_text`。
- 修改前：CH006 关系节缺少该入口。
- 修改后：添加同方向人物与源段链接。
- 核证依据：CH006/CH029 psych、EV0135（E517）；L34287–34298，D/E 不变。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Relationship Matrix / CH006 Performance。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-008｜CR-3A-002

- 修改文件：[characters/records.json](characters/records.json)；记录/字段：`CH029 / relations`。
- 修改前：CH029 relations 缺少对安雅评价入口。
- 修改后：添加 CH029→CH006 的 D/E 公务接触及评价导航，不推反向。
- 核证依据：CH006/CH029 psych、EV0135（E517）；L34287–34298，D/E 不变。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Relationship Matrix / CH006 Performance。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-009｜CR-3A-002

- 修改文件：[characters/CH029_现任紫钻.md](characters/CH029_现任紫钻.md)；记录/字段：`正文 / exact_text`。
- 修改前：CH029 关系节缺少该入口。
- 修改后：添加同方向人物与源段链接。
- 核证依据：CH006/CH029 psych、EV0135（E517）；L34287–34298，D/E 不变。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Relationship Matrix / CH006 Performance。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-010｜CR-3A-002

- 修改文件：[relationships/RELATIONSHIP_MATRIX.md](relationships/RELATIONSHIP_MATRIX.md)；记录/字段：`正文 / append_navigation`。
- 修改前：关系矩阵没有可发现入口。
- 修改后：追加尚未单建 REL 的评价导航；原矩阵正文原字节保留。
- 核证依据：CH006/CH029 psych、EV0135（E517）；L34287–34298，D/E 不变。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Relationship Matrix / CH006 Performance。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-011｜CR-3A-003

- 修改文件：[characters/records.json](characters/records.json)；记录/字段：`CH010 / reason`。
- 修改前：Tier A 理由为招募与身份误解核心传播节点。
- 修改后：收窄为招募、联络、术语和家庭误会流转；不授权 K018。
- 核证依据：K015、K226、EV0004/0024/0055；L751–778、4800–4828、13787–13794、13935–13952。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Knowledge Profile / CH010 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-012｜CR-3A-003

- 修改文件：[characters/CH010_摩可.md](characters/CH010_摩可.md)；记录/字段：`正文 / exact_text`。
- 修改前：人物正文继承宽泛 Tier 理由。
- 修改后：镜像收窄后的 reason，Tier A 不变。
- 核证依据：K015、K226、EV0004/0024/0055；L751–778、4800–4828、13787–13794、13935–13952。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Knowledge Profile / CH010 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-013｜CR-3A-003

- 修改文件：[characters/records.json](characters/records.json)；记录/字段：`CH010 / knowledge`。
- 修改前：知识导航未显式解释 K226 的未知边界。
- 修改后：注明 UNKNOWN 无证不授予，不反推永远不知道。
- 核证依据：K015、K226、EV0004/0024/0055；L751–778、4800–4828、13787–13794、13935–13952。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Knowledge Profile / CH010 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-014｜CR-3A-003

- 修改文件：[characters/CH010_摩可.md](characters/CH010_摩可.md)；记录/字段：`正文 / exact_text`。
- 修改前：人物 Knowledge 导航未写该限制。
- 修改后：镜像 K226 边界。
- 核证依据：K015、K226、EV0004/0024/0055；L751–778、4800–4828、13787–13794、13935–13952。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Knowledge Profile / CH010 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-015｜CR-3A-003

- 修改文件：[knowledge/by_character/CH010_knowledge.md](knowledge/by_character/CH010_knowledge.md)；记录/字段：`正文 / exact_text`。
- 修改前：按人知识页未写该限制。
- 修改后：镜像 K226 边界。
- 核证依据：K015、K226、EV0004/0024/0055；L751–778、4800–4828、13787–13794、13935–13952。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：人物 / Knowledge Profile / CH010 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-016｜CR-3A-004

- 修改文件：[knowledge/records.json](knowledge/records.json)；记录/字段：`K098 / cross_references`。
- 修改前：K098 没有可定位的误解来源字段。
- 修改后：追加指向 K018-T005 / CH002 / EV0067 的限定导航。
- 核证依据：K018-T005/EV0067、K098-T001/EV0092；L13835–13854、13969–13983、20727–20751；强因果另见 FUP-3A-001。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：Knowledge / CH002 Profile / Transition 导航 / CH002 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-017｜CR-3A-004

- 修改文件：[knowledge/records.json](knowledge/records.json)；记录/字段：`K018 / cross_references`。
- 修改前：K018 没有指向恋爱误解纠正的结构化导航。
- 修改后：追加指向 K098-T001 / EV0092 的交叉引用。
- 核证依据：K018-T005/EV0067、K098-T001/EV0092；L13835–13854、13969–13983、20727–20751；强因果另见 FUP-3A-001。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：Knowledge / CH002 Profile / Transition 导航 / CH002 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-018｜CR-3A-004

- 修改文件：[knowledge/K018.md](knowledge/K018.md)；记录/字段：`正文 / append_navigation`。
- 修改前：K018 正文未说明两个不同命题的接续。
- 修改后：追加来源、纠正、状态不能互换及强因果待核说明。
- 核证依据：K018-T005/EV0067、K098-T001/EV0092；L13835–13854、13969–13983、20727–20751；强因果另见 FUP-3A-001。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：Knowledge / CH002 Profile / Transition 导航 / CH002 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-019｜CR-3A-004

- 修改文件：[knowledge/K098.md](knowledge/K098.md)；记录/字段：`正文 / append_navigation`。
- 修改前：K098 正文早期来源入口缺失。
- 修改后：追加同一误解链与显式补读规则；无自动联查。
- 核证依据：K018-T005/EV0067、K098-T001/EV0092；L13835–13854、13969–13983、20727–20751；强因果另见 FUP-3A-001。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：Knowledge / CH002 Profile / Transition 导航 / CH002 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-020｜CR-3A-004

- 修改文件：[knowledge/by_character/CH002_knowledge.md](knowledge/by_character/CH002_knowledge.md)；记录/字段：`正文 / append_navigation`。
- 修改前：CH002 知识页缺少跨命题恢复导航。
- 修改后：追加 EV0067 来源与 EV0092 纠正及待核项入口。
- 核证依据：K018-T005/EV0067、K098-T001/EV0092；L13835–13854、13969–13983、20727–20751；强因果另见 FUP-3A-001。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：Knowledge / CH002 Profile / Transition 导航 / CH002 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-021｜CR-3A-004

- 修改文件：[knowledge/KNOWLEDGE_TRANSITIONS.md](knowledge/KNOWLEDGE_TRANSITIONS.md)；记录/字段：`正文 / append_navigation`。
- 修改前：Transition 导航未展示这段跨命题衔接。
- 修改后：追加非新节点说明；365 个原 T 节点保留。
- 核证依据：K018-T005/EV0067、K098-T001/EV0092；L13835–13854、13969–13983、20727–20751；强因果另见 FUP-3A-001。
- 是否改变事实：否；仅消歧/导航。原有真值、知识状态和证据等级不变。
- 受影响模块：Knowledge / CH002 Profile / Transition 导航 / CH002 Performance 与 validation。
- 回归：逐字段日志对照、文本重放、相关 ID/阶段及查询检查；最终通过状态统一见局部回归 JSON，不将导航测试冒充自动联查能力。

## P3A-022｜CR-3A-001–004 汇总：README 版本入口

- 修改文件：[README.md](README.md)。修改前：V1 / Stage 2C 为当前入口；修改后：指向 V1.1、四条 Patch、局部回归及同步/待核边界，Stage 2C 原完成说明标为历史。
- 核证依据：本轮四项 Review 与局部检查；不改变事实，属于版本导航；受影响模块：全库读取入口。回归：旧文件白名单、链接检查、版本一致性与冻结哈希。
- 完整前后像：[version_changes.json](_stage3a_patch/version_changes.json)。

## P3A-023｜CR-3A-001–004 汇总：Manifest 版本冻结

- 修改文件：[BASELINE_MANIFEST.md](BASELINE_MANIFEST.md)。修改前：V1 冻结范围与旧哈希；修改后：V1.1 当前哈希及本轮检查、完整 V1 历史入口。
- 核证依据：全部局部回归通过后才冻结；不改变事实，属于版本记录；受影响模块：冻结和后续变更门槛。回归：机器清单与 Markdown 模块哈希、V1 原件、受保护输入。
- V1 原 Manifest 已按原字节保存在 [_stage3a_patch/BASELINE_MANIFEST_V1.md](_stage3a_patch/BASELINE_MANIFEST_V1.md)，ZIP 同时保留原目录结构与链接上下文；原 `_stage2c/` 未覆盖。

## 本轮新增记录与交付边界

新增公开报告为本 Changelog、[Review](STAGE3A_CANON_PATCH_REVIEW.md)、[Follow-ups](STAGE3A_PATCH_FOLLOWUPS.md) 共 3 份，均不新增 Canon 事实。前后哈希与新增工作文件见 [patch_file_changes.json](_stage3a_patch/patch_file_changes.json)。备份、一次性 Patch 脚本、局部检查器、前后像和冻结回执位于 `_stage3a_patch/`；不可重复运行一次性写入脚本。

原关系矩阵含特殊换行，本补丁保留其原有正文的字节，只追加导航，没有顺手统一排版。source/current/audit/performance/final 全部未修改。新增稳定 ID 为 0；FUP-3A-001 保留待核；Performance 同步尚未执行。
