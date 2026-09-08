# 第一阶段全文审计报告

> 最终收尾导航：**全文连续语义阅读100.00%（1,641,637／1,641,637字符）**，L1—38825，无续读断点。**第一阶段全文审计：完成**；现行入口见[轻量索引](CONTINUE_STATE.md)。

本文件“续审/中期”段落及session文件均为按各自断点保留的历史快照，不是新的未读区间或现行指令；最终有效判断见问题条目末次修订，前后值和原因见judgment_changes.json及final_changes.json。
> 当前161项＝138项C＋18项有效S＋5项R；S018为已撤销候选，保留于withdrawn_candidates.json，不补号、不计有效问题。细分结论以当前问题条目及其修订记录为准。
> 原著已全部连续语义核验；当前收尾不表示所有卡片条目均正确，亦不将待证判断升级为事实。本阶段未改卡。

累计记录161项，其中包含潜在风险和需用户裁决事项，不是161条已经证实的Canon错误。普通错误、结构事实与运行风险分别标注。

|严重程度|数量|
|---|---:|
|CRITICAL|3|
|MAJOR|86|
|MODERATE|55|
|MINOR|2|
|POTENTIAL RISK|15|

## 阅读方式

条目ID对应PNG原始ID，不能使用数组索引替代。链接指向audit中的逐字提取副本；source/current仍只读。证据索引保留原著卷号与源文件行号。

所有“后续修正／补充”均为建议，本阶段未生成新版角色卡。存在USER_CONFIRMATION_REQUIRED不妨碍继续核验原著，只阻止擅自选择改写方案。

## [S001] 主线推进脚本与全部剧情条目名称不匹配

**严重程度：** CRITICAL

**问题类型：** 技术／时间状态

**角色卡位置：** [ID 10｜[mvu_update]变量更新规则](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_010.txt>)；[ID 14｜剧情·卷1幕01·重返战场](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_014.txt>)；[ID 178｜剧情索引](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_178.txt>)

**当前内容概述：** 脚本只匹配剧情·卷一幕NN；实际22条剧情条目使用剧情·卷1幕NN或卷2幕NN。

**发现的问题：** 静态逐名核对得到0/22匹配；即使变量更新事件成功触发，该循环也不会切换这些剧情条目。当前节点解析也只接受卷一。

**原著证据 / 定位：** technical/script_2.js:1–5、55–66；全部条目comment和enabled字段

**证据等级：** 技术直接证据；非Canon分级

**更准确的理解：** 名称、节点协议与卷号必须一致；目前不能依靠这个脚本隔离各幕。未在真实酒馆运行，不推定额外宿主兼容行为。

**可能造成的 RP 后果：** 未来剧情可能仍由关键词触发，当前幕也不保证正确启用；日志却可报告同步成功。

**建议处理：** 后续修正命名协议和卷二支持；以真实宿主导入、跳幕及切换聊天验证。

## [S002] 脚本找不到绑定世界书时会选择其他同名主题世界书

**严重程度：** POTENTIAL RISK

**问题类型：** 技术／作用范围

**角色卡位置：** 技术／源文位置见下方定位；[技术目录](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/technical>)

**当前内容概述：** 主绑定解析失败后，从全量世界书中选择首个名称含魔法少女的世界书。

**发现的问题：** 回退条件不是当前角色卡的稳定标识；且操作是更新世界书条目的enabled，非只读提示过滤。

**原著证据 / 定位：** technical/script_2.js:27–39、55–65

**证据等级：** 技术直接证据；实际误操作未验证

**更准确的理解：** 仅在回退被触发且有多个相似名称时风险成立；现有名称失配又会使部分更新无效，不能声称已经改坏其他卡。

**可能造成的 RP 后果：** 修复S001后，回退可能作用于错误世界书，或共享世界书影响其他聊天。

**建议处理：** 后续限定当前绑定和唯一标识，无法定位时明确失败；先做隔离宿主验证。

## [S003] 开局、时间总览与状态缺省提供三套当前日期

**严重程度：** CRITICAL

**问题类型：** 时间／初始化

**角色卡位置：** [ID 4｜国度与政治](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_004.txt>)；[ID 8｜[InitVar]](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_008.txt>)；[ID 13｜ [mvu_plot]叙事守则与开局初始化](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_013.txt>)；[ID 14｜剧情·卷1幕01·重返战场](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_014.txt>)；[ID 15｜格式](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_015.txt>)；[ID 91｜剧情·卷1幕02·新队与下水道之歌](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_091.txt>)；[ID 92｜剧情·卷1幕03·异策局](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_092.txt>)；[ID 93｜剧情·卷1幕04·坦白与屏障](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_093.txt>)；[ID 94｜剧情·卷1幕05·黑烬黎明事变](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_094.txt>)；[ID 95｜剧情·卷1幕06·暑假与秘密基地](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_095.txt>)；[ID 178｜剧情索引](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_178.txt>)；[ID 98｜剧情·卷2幕01·新局长与兽子](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_098.txt>)；[ID 89｜祖母绿](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_089.txt>)；[ID 173｜异策局特殊作战部第三小队](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_173.txt>)；[ID 99｜剧情·卷2幕02·鸢来袭](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_099.txt>)；[ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)；[ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)

**当前内容概述：** 国度政治当前2000；初始化与叙事守则1999初春；第一幕和格式示例1999年5月17日。

**发现的问题：** 这首先是卡内可直接确认的冲突；没有单一开局时间，也未明确IF开局与原作轴谁负责最终定时。 续读发现ID92事件十把第47章定为7月6日，而正文明确七月中旬；同章已特训近半月，不能又写成特训正式开始。ID91第16章6月9日与紧接电话出战第17章6月12日也缺少原文三天跳转。 ID95把出游生日固定为10月5日，而正文第99章约在开学第三个周末、第100章九月过半时将至；入住为开学第一个周末、第一次早餐为其后周一。精确月日仍须独立论证，不能自动由旧卡继承。

**原著证据 / 定位：** [E010](01_evidence_index.md#e010)、[E011](01_evidence_index.md#e011)；technical/script_1.js世界.日期；ID8禁用；[E045](01_evidence_index.md#e045)、[E063](01_evidence_index.md#e063)、[E070](01_evidence_index.md#e070)；源文L1344–1378、2815、3402–3412；[E102](01_evidence_index.md#e102)、[E106](01_evidence_index.md#e106)、[E111](01_evidence_index.md#e111)、[E113](01_evidence_index.md#e113)、[E114](01_evidence_index.md#e114) [E124](01_evidence_index.md#e124)、[E129](01_evidence_index.md#e129)、[E139](01_evidence_index.md#e139)—[E145](01_evidence_index.md#e145)；L8667、9062、9811、9860、9951–9964、10296。；[E182](01_evidence_index.md#e182)、[E184](01_evidence_index.md#e184)、[E185](01_evidence_index.md#e185)、[E189](01_evidence_index.md#e189)、[E192](01_evidence_index.md#e192)—[E195](01_evidence_index.md#e195)、[E202](01_evidence_index.md#e202)、[E208](01_evidence_index.md#e208)—[E210](01_evidence_index.md#e210)；[E213](01_evidence_index.md#e213)—[E216](01_evidence_index.md#e216)、[E219](01_evidence_index.md#e219)、[E231](01_evidence_index.md#e231)—[E240](01_evidence_index.md#e240)；[E245](01_evidence_index.md#e245)、[E248](01_evidence_index.md#e248)、[E250](01_evidence_index.md#e250)—[E261](01_evidence_index.md#e261)；[E266](01_evidence_index.md#e266)—[E287](01_evidence_index.md#e287)；[E290](01_evidence_index.md#e290)、[E291](01_evidence_index.md#e291)、[E303](01_evidence_index.md#e303)、[E307](01_evidence_index.md#e307)—[E314](01_evidence_index.md#e314)；[E350](01_evidence_index.md#e350)、[E353](01_evidence_index.md#e353)、[E357](01_evidence_index.md#e357)、[E365](01_evidence_index.md#e365)、[E368](01_evidence_index.md#e368)、[E372](01_evidence_index.md#e372)；[E376](01_evidence_index.md#e376)、[E378](01_evidence_index.md#e378)、[E382](01_evidence_index.md#e382)、[E387](01_evidence_index.md#e387)、[E392](01_evidence_index.md#e392)、[E393](01_evidence_index.md#e393)、[E401](01_evidence_index.md#e401)

**证据等级：** 技术直接证据＋A（原文明确年/月及相对日期）；具体未有依据的月日为F；自定日历仍可为IF

**更准确的理解：** 当前年和历史年应按场景区分；精确月日如为创作安排须标明，不能混作已核验Canon。 小璐生日五月五日及家长会16:30/16:40有直接依据，不应把所有具体时点都列为不可知。 忌日为周六且上周是纪念日、处暑夜、八月末、开学周次、九月过半均已记录；这些不能擅自强压成一张毫无张力的日历。 接讯至抵达在111为两天、115回顾为四天，保留两说。抵达翌日解决蛛、约一周善后、节前两日问讯、离开近半月/搬入一个半月可作相对锚；不可强定卡96的10月15—17连续战期。 续审06：卷二1明确十一月初、月圆节后两周；2就任首日，3午后数小时大会，4—6会后交易与当日返程。若沿卡自定11月9日作首日，便不能把大会/祖来访移至10日、车站移至11日。8是次日十点、9同日下午、11次日晚、12再次日上午；17月圆节后三周，20战后数小时并同日傍晚车中确认，21十一月中。卡98的11月17—19跨三日体验与21—22日体检不吻合这些关系。源文20又以半个月回顾月圆节，与17三周有松动，保留近似时间，不私造精准日历。 续审07：24章的11月28日是小璐所读活动维护预告，不自动等于现场当天；34章明说十二月初周末，35为数日后、37又两日工作日中午。38跟踪与39午餐同时，40当日下班；卡100把37—40分别列12月6—8即使标推算也破坏同日性。卡99的上午招待也应按26章正午报告及27接续处理。不强造新的精确月日表。 续审08：42明确12月11日工作日、白生日；林认定庆生日为2月14日，登记簿真实日未给，卡100的12月24日错误另C084。43写十二月中、夏前天晋叶，45约周六，46周六下午到场并延续至散场；不把卡推算12月12/14直接认证。玛最后告别是十三年前，并非与二十年前初识同一时点。 续审09：51演唱会后一小时离场，52接墓园、53归基地却有斜阳、54再晚餐；这里的过渡和日夜关系有张力，不硬定全属同晚或翌日。57周末已过的工作日与58早8点、59十分钟后相接，卡101周末与分拆12月18—20不能照搬。62先说今天上午/两天调整，夜访段又有近一周/好几天，保留文本约数或叙述省略的不确定性。50末今年考核、51答明年，也不私改源字。 续审10：64来客一周后、周日；69只年末，来方亭超过一月，73说接近两月可并存不硬改日期。70放假倒数第二天且后天跨年，71同餐接续，72跨年夜，73酒局半小时有余；精确12/26、12/30仍为卡历安排，65教术式为更早夜晚回忆。 续审12：91假期第5/新年第4天，不是卡1031月3；97/98/99当日连续不能被卡指定15/20/28号分离。93明确1月5、1月9训练、2月10出发和3月3考试可保留，源92上午接91、93午后却换日的张力另R005。 续审13：本批直接锚10日出发，11日燕南/专列、12日门/彩云湿地，13日治疗与三人报到并行，14日制礼赴约；卡104中段整体早一天且和本卡109互相错开。107治疗没有独立12日依据。

**可能造成的 RP 后果：** 角色职务、伤势、亲疏及已知秘密的阶段选择从第一回合就可能错位。

**建议处理：** USER_CONFIRMATION_REQUIRED：开局与日期设计交由用户裁决；其余先记录冲突。

## [S004] 卡片自称原文止于269章，实际输入有至282章正文

**严重程度：** CRITICAL

**问题类型：** 覆盖范围／Canon维护

**角色卡位置：** [ID 7｜往事编年](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_007.txt>)；[ID 111｜剧情·卷2幕14·回忆·1979卢恩诺雷守卫战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_111.txt>)；[ID 178｜剧情索引](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_178.txt>)

**当前内容概述：** ID111明确原文止于第269章，后续战斗胜负和所有身份真相未揭。

**发现的问题：** 源文270–282已提供大量新揭示；过期断点散布人物、能力、政治和认知条目。它不是单个遗漏，更会主动禁止正确事实。

**原著证据 / 定位：** [E011](01_evidence_index.md#e011)–[E040](01_evidence_index.md#e040)；源文L36130–38825；[E014](01_evidence_index.md#e014)、[E016](01_evidence_index.md#e016)、[E035](01_evidence_index.md#e035)、[E036](01_evidence_index.md#e036)、[E040](01_evidence_index.md#e040)

**证据等级：** A

**更准确的理解：** 可以保留269作为指定RP截止点，但不能声称用户提供的全文只有269；282末仍未决的胜负继续未知。 第一阶段收尾：完整语义核对手机后，妮姆能力/结局、蜂使徒现时战果、雪毬能力、羊踯躅受控与刺王偷听等仍有269式过期未知。282《琥珀》才是所给源文件结尾；这是输入范围，不是宣告作品全部悬念完结。

**可能造成的 RP 后果：** 能力被禁止、死亡及传承遭抹除、知情状态停滞；后期演绎持续错误。

**建议处理：** 修正覆盖范围标记；USER_CONFIRMATION_REQUIRED确认是否有意保留269玩法断点。

## [S005] 阶段说明存在，但常驻资料没有执行阶段裁剪

**严重程度：** MAJOR

**问题类型：** 时间／结构／认知

**角色卡位置：** [ID 0｜人物总览](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_000.txt>)；[ID 4｜国度与政治](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_004.txt>)；[ID 7｜往事编年](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_007.txt>)；[ID 47｜林昀](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_047.txt>)；[ID 121｜方亭小队秘密基地](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_121.txt>)；[ID 157｜方亭市小队](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_157.txt>)

**当前内容概述：** 多条常驻内容直接给现任职务、后期队伍和历史秘密；人物正文又把各阶段完整并列。

**发现的问题：** “按阶段调用”只是提示约束，不是证明实际只注入本阶段；S001又使幕切换失效。

**原著证据 / 定位：** 所有143条配置完整解析；56条启用常驻共37777字符；[E001](01_evidence_index.md#e001)、[E012](01_evidence_index.md#e012)、[E037](01_evidence_index.md#e037)给出真实知识变化实例

**证据等级：** 技术直接证据；泄漏结果属风险

**更准确的理解：** 后台允许保存完整资料，但模型收到的事实不应默认成为开局现状或全部NPC知识。字符数不是token数，实际预算由宿主决定。

**可能造成的 RP 后果：** 开局即出现局长林昀、后期基地或完整身份链，NPC提前熟悉与信任。

**建议处理：** 后续拆分静态身份、动态阶段、后台秘密；按事件与知情主体过滤。

## [S006] 柏安市条目启用但无普通关键词入口

**严重程度：** MODERATE

**问题类型：** 触发机制

**角色卡位置：** [ID 114｜柏安市](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_114.txt>)

**当前内容概述：** enabled=true，constant=false，keys与secondary_keys为空。

**发现的问题：** 在常规关键词激活路径中没有入口；是否有宿主手动激活或外部关联未提供。

**原著证据 / 定位：** ID114完整配置；该条不是常驻

**证据等级：** 技术直接证据

**更准确的理解：** 可确认常规入口缺失，不能武断断言任何环境永远无法注入。

**可能造成的 RP 后果：** 提到柏安市时可能只得到队伍、案件片段，缺少地区背景。

**建议处理：** 后续调整触发或明确外部激活接口；真实宿主验证。

## [S007] 通用词触发会带入跨地域或未来情报

**严重程度：** MODERATE

**问题类型：** 触发／视角

**角色卡位置：** [ID 115｜柏安市地下异策局](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_115.txt>)；[ID 119｜方亭市第一福利院](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_119.txt>)；[ID 123｜花园](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_123.txt>)；[ID 131｜卢恩诺雷魔事院分院](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_131.txt>)；[ID 136｜湿地公园](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_136.txt>)；[ID 158｜国度军](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_158.txt>)；[ID 160｜间界联合军](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_160.txt>)；[ID 173｜异策局特殊作战部第三小队](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_173.txt>)

**当前内容概述：** 异策局、福利院、花园、公园、国度、间界等普通类别词被用作专属条目关键词。

**发现的问题：** 常见场景用语可能拉入柏安地下异策局、特定湿地公园或组织资料；不是所有同名类别都指该实体。

**原著证据 / 定位：** 00_card_structure.md逐条keys；宿主scan_depth和whole_word设置继承未给出

**证据等级：** 技术直接证据；实际注入需宿主确认

**更准确的理解：** 风险与关键词扫描方式和上下文有关，不能仅凭宽词认定每次都误触发。

**可能造成的 RP 后果：** 地点混淆，局部场景受远方事件污染，预算被无关条目占用。

**建议处理：** 后续使用专名与组合条件，并测试别名召回和普通词误触发。

## [S008] 常驻与重复提示负担缺乏实测预算依据

**严重程度：** POTENTIAL RISK

**问题类型：** 结构／上下文预算

**角色卡位置：** [ID 0｜人物总览](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_000.txt>)；[ID 1｜残兽与等级](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_001.txt>)；[ID 2｜魔法少女体系](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_002.txt>)；[ID 3｜魔术与符文](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_003.txt>)；[ID 4｜国度与政治](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_004.txt>)；[ID 5｜黑烬](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_005.txt>)；[ID 6｜其他](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_006.txt>)；[ID 7｜往事编年](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_007.txt>)；[ID 20｜魔法少女](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_020.txt>)；[ID 21｜残兽](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_021.txt>)；[ID 22｜魔法少女的修炼方法](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_022.txt>)；[ID 24｜开华](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_024.txt>)

**当前内容概述：** 启用常驻56条共37777字符；多处重复等级、身份和阶段约束，单条人物又重复目标、行为、关系。

**发现的问题：** 可能稀释当前场景和关键证据，但当前没有宿主预算、模型分词器或实际注入日志，不能给出确定溢出token数。

**原著证据 / 定位：** 全条目字符统计、enabled/constant、ignore_budget=false；递归阻断配置均已解析

**证据等级：** 技术直接证据；影响待实测

**更准确的理解：** 不是条目ID有缺口或扩展position不同就算结构错误；也未发现递归爆炸证据。

**可能造成的 RP 后果：** 重复“禁止”压过行动信息；预算裁剪时重要边界可能未注入。

**建议处理：** 后续按事实唯一来源合并；保留有用行为指导，使用真实提示预览测预算。

## [S009] 龙胆伪装与变身状态被绑定成互斥条件

**严重程度：** MAJOR

**问题类型：** 身份／呈现协议

**角色卡位置：** [ID 15｜格式](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_015.txt>)；[ID 47｜林昀](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_047.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)

**当前内容概述：** ID15规定龙胆只用于未变身伪装，一变身必须改翠雀，解除伪装立即林昀。

**发现的问题：** 原著明确要求在变身后激活假宝石，使龙胆衣装覆盖原衣装；常服模式也只是伪造变身前后差异。ID15却把龙胆绑定为未变身，一变身必须显示翠雀，直接冲突。

**原著证据 / 定位：** [E041](01_evidence_index.md#e041)；源文L23455–23479；[E012](01_evidence_index.md#e012)；ID15 L102–117、178–181；[E379](01_evidence_index.md#e379)、[E382](01_evidence_index.md#e382)、[E389](01_evidence_index.md#e389)、[E402](01_evidence_index.md#e402)

**证据等级：** A＋卡内直接冲突

**更准确的理解：** 不应要求伪装中的魔法少女一使用变身外观就公开翠雀；也不应把解除龙胆伪装等同还原男性肉身。 续审13：103龙胆新人身份用准考证，104翠本已魔法身体再借假宝石更衣，不是从男身才可伪装。107分别拿真心之花与假心之芽。114新常服已购一套已穿，不能将旗袍永久锁死或脱衣装即还原男身。

**可能造成的 RP 后果：** 头像、气泡或transform标签可在正文尚保密时先暴露翠雀，并让模型误判肉身形态。

**建议处理：** 后续拆分本体、变身状态、对外身份和UI显示名；保留伪装不必播放变身动画的设计。

## [S010] 唯一真实状态快照没有对应的逐NPC知识记录

**严重程度：** MAJOR

**问题类型：** 认知／长期状态

**角色卡位置：** [ID 9｜变量快照](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_009.txt>)；[ID 10｜[mvu_update]变量更新规则](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_010.txt>)；[ID 13｜ [mvu_plot]叙事守则与开局初始化](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_013.txt>)；[ID 99｜剧情·卷2幕02·鸢来袭](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_099.txt>)；[ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)；[ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)；[ID 60｜木百合](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_060.txt>)；[ID 17｜白静萱](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_017.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)；[ID 106｜剧情·卷2幕09·旧梦与岔路](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_106.txt>)；[ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)；[ID 108｜剧情·卷2幕11·花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_108.txt>)；[ID 145｜银廊后花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_145.txt>)；[ID 112｜原著时间](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_112.txt>)；[ID 113｜原著时间线2](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_113.txt>)；[ID 138｜地区与势力总览](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_138.txt>)；[ID 151｜地区概览](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_151.txt>)；[ID 152｜地区概览2](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_152.txt>)

**当前内容概述：** stat_data被称作真实唯一基准；schema主要存世界、人物、关系、节点和事件。

**发现的问题：** 有世界事实和对user好感，却没有内置的“某人何时从谁得知哪部分、相信程度”结构；passthrough允许扩展不等于已实现。

**原著证据 / 定位：** technical/script_1.js完整schema；[E012](01_evidence_index.md#e012)、[E027](01_evidence_index.md#e027)、[E036](01_evidence_index.md#e036)、[E037](01_evidence_index.md#e037)；[E053](01_evidence_index.md#e053)、[E057](01_evidence_index.md#e057)、[E064](01_evidence_index.md#e064)、[E067](01_evidence_index.md#e067)、[E069](01_evidence_index.md#e069)、[E070](01_evidence_index.md#e070)、[E071](01_evidence_index.md#e071)、[E073](01_evidence_index.md#e073)、[E078](01_evidence_index.md#e078)、[E079](01_evidence_index.md#e079)；[E080](01_evidence_index.md#e080)、[E091](01_evidence_index.md#e091)、[E095](01_evidence_index.md#e095)、[E097](01_evidence_index.md#e097)、[E100](01_evidence_index.md#e100)—[E105](01_evidence_index.md#e105)、[E109](01_evidence_index.md#e109)、[E110](01_evidence_index.md#e110) [E124](01_evidence_index.md#e124)—[E129](01_evidence_index.md#e129)、[E132](01_evidence_index.md#e132)、[E141](01_evidence_index.md#e141)—[E152](01_evidence_index.md#e152)。；[E155](01_evidence_index.md#e155)、[E160](01_evidence_index.md#e160)、[E163](01_evidence_index.md#e163)、[E165](01_evidence_index.md#e165)、[E169](01_evidence_index.md#e169)、[E176](01_evidence_index.md#e176)、[E178](01_evidence_index.md#e178)—[E180](01_evidence_index.md#e180)；[E182](01_evidence_index.md#e182)、[E189](01_evidence_index.md#e189)、[E191](01_evidence_index.md#e191)—[E199](01_evidence_index.md#e199)、[E200](01_evidence_index.md#e200)、[E203](01_evidence_index.md#e203)—[E212](01_evidence_index.md#e212)；[E217](01_evidence_index.md#e217)—[E240](01_evidence_index.md#e240)；[E241](01_evidence_index.md#e241)—[E249](01_evidence_index.md#e249)、[E254](01_evidence_index.md#e254)—[E261](01_evidence_index.md#e261)；[E262](01_evidence_index.md#e262)—[E287](01_evidence_index.md#e287)；[E288](01_evidence_index.md#e288)—[E314](01_evidence_index.md#e314)；[E315](01_evidence_index.md#e315)—[E347](01_evidence_index.md#e347)；[E348](01_evidence_index.md#e348)—[E375](01_evidence_index.md#e375)；[E376](01_evidence_index.md#e376)—[E402](01_evidence_index.md#e402)；[E403](01_evidence_index.md#e403)、[E407](01_evidence_index.md#e407)、[E410](01_evidence_index.md#e410)、[E417](01_evidence_index.md#e417)—[E425](01_evidence_index.md#e425)；[E435](01_evidence_index.md#e435)—[E450](01_evidence_index.md#e450)；[E454](01_evidence_index.md#e454)、[E459](01_evidence_index.md#e459)、[E461](01_evidence_index.md#e461)、[E464](01_evidence_index.md#e464)、[E467](01_evidence_index.md#e467)、[E469](01_evidence_index.md#e469)；[E473](01_evidence_index.md#e473)、[E474](01_evidence_index.md#e474)、[E480](01_evidence_index.md#e480)、[E489](01_evidence_index.md#e489)、[E490](01_evidence_index.md#e490)、[E492](01_evidence_index.md#e492)；[E494](01_evidence_index.md#e494)—[E515](01_evidence_index.md#e515)；[E516](01_evidence_index.md#e516)—[E535](01_evidence_index.md#e535)；[E536](01_evidence_index.md#e536)—[E545](01_evidence_index.md#e545)

**证据等级：** 技术直接证据；源文对照A/C/D

**更准确的理解：** 世界真相、玩家知道、NPC知道必须独立。节点推进不能一次解锁所有人的知识。 荼蘼牺牲时林昀尚不知；总局档案不等于本地局员知情；夏凉身世暂不告小璐；红个人知道小锦不等于本地记录有；第59章夏凉知道手机持有关系不等于识破真身。 麻雀认出矢车菊但未分享；王腾飞确认关联却错认变身方向；翠雀从病历与薄雪本人分次补知、故意不告樱死讯；猫眼私谈排除红思与；夏凉第98章才获林昀同一人的承认，并未因此获得全部身世。 白蓟验牌知翠雀=矢车菊但不知男身；灯盏与猫尾掌握调查目标改变而调查院旧档未同步；薄雪已觉醒魔装却待当面报告；田胜记忆与既往救人经历不一致。林昀129才报新来电并只向群发一般警告，红132不能说幕后名，不能自动向所有人解锁后续秘密。 红高一才确认男身，妮妮只听巡查使称呼；白首次同时得知樱死和母女关系后昏迷，不能补听后续宝石解释。夏凉早知男身，小璐此时才拼旧号，卡97事件八的孩子们全不知男身应按人拆开。摩丝临死前才从两人私语推翠为小璐父，玛格间奏一才经木百合消息确认复出；间奏二任调请求与樱案信息只在猫眼私谈，不能共享给所有后辈。 续审06：公众只知摩丝下落不明/袭击定性与旧影像复出新闻；田有梦和绿色残片，17仍回忆不起福利院细节。白叫爸爸源于摩可→情侣、夏→安息、小璐→领养的拼接；夏知真身而打趣，白误把沉默当接受。研究所交易、白狼秘闻与20诊断只在祖与翠私谈，白在检查床沉睡；卡98幕末方亭队知道爪痕与兽源有关等不能无传播直接全队解锁。七的研究员口供翠未亲闻，白仅概括被否定父母。敌方误以为两暗子未被发现及翠仍蓝色花级；林实际留钓线，但到陶芳通讯查讯才知目标湖畔春天。小璐对牵牛只是熟悉感，蓝星博文也只是疑问，均非确认内幕。 续审07：鸢知道首领额外要白与矢，塞米25才听到；鸢28通过蓝线认矢，未见男身变身。红31给翠的繁开说明刻意不让鸢听，新人也未旁听；36才由来客听原花牌袭局和红救援，不能自动拥有其名号与完整魔装记录规则。白知湖畔，夏知林翠却35才听出白另有秘密；三新人赶援途中被通知回校，未亲历对战。38给林的短信未发送又删除，红拐研究所为旁白明确女孩不知道；40末仅小璐看见林与红，尚未展开问答。 续审08：41林从女儿推理才知误会源，小璐从林得局长职务但同时收到虚假编外履历，私自改猜翠爱安雅且未分享。42夏从翠获母称承诺，林从白补闻同曲与失盒并推虐杀因果；白未获男身确认。46翠现场确认玛，夏48才得翠肯定，两市学生经后台介绍才互识；小璐最后才认木。观众看到额吻并未知道旧友身份，红未在场。 续审09：玛经学生复出消息主动问猫眼；52仅知爪痕来人不知谁，60才知假考生治疗方案且初见失控，红较早已听祖说。51仅小听墓地耳语后转述木；53白蓟保护动机是推测，54翠才知私吵，56玛从翠补小停种。58/59红才认玛并知道演出；59林红才听苏间界消息。62后辈只听取消条件和翠陪行，不知假考生、治疗目的，夏问白天赋也只获敷衍。 续审10：翠/夏66先不识浊化，玛当场才讲；小早已学，白蓟由表现推玛教。64送白入学计划无人获告。69鸢从翠话和查残气作报告，白狼暂当真，物质界众人未听镜谈。71小向父倾诉且求不告翠，父翠同一人无需转告。72员工私传白叫爸爸未全局公开/法律收养，小从糖确认探访频率。73小收到公务借口短信，回门才见鸢，不预授战书和首领命令。 续审11：74鸢由小自报才知林有女儿、见变身才知少女；林与小同时听战书。75父通知队伍但小两队转告无具体过程，89补带夏白来。79小获耳语、除翠外众人首次见白兽形却未知成因；81鸢才见兽源借回。87含羞从误认假白到感魔/实验确认，规则经广播给另外两人；小问白只获非敌所为。88夏仍想小未来觉醒，未现场见王钥；回据点途中小才报告觉醒，89翠才私告玛白祭子。鸢计划的88内心、翠未用底牌、祝福未传声不能给全队作公开知识。 续审12：90祖承认旁观私事，仍自认档案不全；91回叙认母答复没有男身坦白。93夏已先私问、小此时才获祭子/战斗/兽魔，父母身份仍隐，战斗故事经过失真记忆和翠修饰。96木才知林局长、97道歉未识男翠；97原件给木林留记忆，98翠即告祖，私下保密约定不等信息永不传播。98新衣被拍时柏安三人晚到；99白由玛获考试风险、小尚不知安雅魔装。100翠才从玛知木父实情，木未知；公共妈称呼不等公开领养。午餐白狼称线人核实再向餐桌传新地点，其他成员不自动全知。 续审13：101真实成年证件过物质界港口；103三后辈已获秘密任务假号口径但非治疗政治，土丁桂见准考证误认10岁新人；104白被拦、小夏已过，白到达后转告。105翠以连接波动假说辞遮实历，三人相信。106夏性别方向误解仍未纠正，小没听私语；熟悉旅客未认。107研究院核心人员没见来客，108伤愈实效与献祭风险只有翠祖知道。109小向林手机报平安、翠自己首次听陵园，摘面具才认墨荷；110翠把队长称谓推社交礼节并保留幸福半答。111翠才确认106熟人，墨国度任务/义肢为自述。112收到红核实会议文件，孩子仅旁听尾部；113白先告小父生日、夏最后知计划。114巡警只得翠的有限解释，不知黑猫组织。 续审14：115物资用途仅墨口径；119流放转述链与121组织沉默；131翠认海蒂旧人而对方未认龙胆，褐不懂墨荷且黑半字被打断；129白经夏安排递蛋糕计划，133两身份对话掩护；135小白知同日庆生不知同身。 续审15：146只问郁，147欲警未发，149祖承向此席例外告矢身份，150翠初知五教选司；152首次得调查院抓烬侍/折巡查行动，154初得鸽血红赦史与线人潜入，157初得金蛇现号。159三人获危险与合作，161再得权杖意向；162箱内偷渡仅本席核心见，分院尚不知。 续审16：167箱误会仅分院员得女儿假说，不知矢/林；173夏单独获避嫌说明，小白不听。175粉丝才补动画剧情，翠不等熟知原作。182女王进门无翠，108所谓翠观察恐识破与这一场无据；187翠明确不知当届题目，不能由参与安保推所有答案。189观礼半分钟延迟、多屏选择、龙少入镜，只有祖会意而别人未看表情，不使贵宾全知。 续审17：194小谎称五人队掩翠龙同身；195小谎关注博客，薄故乡自述不是所有 NPC 先知。201密谈旁白身份不传翠，212白私语只小听；213走错北路只观礼知，月季报方亭才认矢关系；215小锦技法因公开观礼已传考生。 续审18：217—220暗示/耳语/电话/回叙分层；220签名实签翠雀且消波，非公开矢落款。225外考官只偏移、核心知关系不揭；227皇冠教选→王庭秘书→女王筛选链，229紫违规十分钟档案窗口破遮蔽；231小先只告翠、232白提前知但薄花不知、233王令、234公众方亭学生/樱死亡阴谋传播均不等知林。237花对龙要求转达矢致歉仍未知同身。 续审19：240门外禁止泄有用真话仍可透露樱母亲，紫241才部分认。250小白先以狗弱小描述识普通考生对口供，薄由相似逼近同身未确认；253口头混话+掌心丝字双通道避镜；255手机无信号只能本地录像需保护，257疑雕塑照片留置非实测确证。259翠不知道复仇结果不倒灌读者所见。 续审20：260金只听你的任务未知刺王；261翠仍以恐袭/战争猜动机；263墨转述预感与矢重新不忧→264报告/现场→265异常合流即时告警。266翠禁术推测、267祖伤修不成未明告；268祖坠当时生死不明而271祖现存已知，不等同归来方式明。269墨私规避猜不给矢，281结果后补。

**可能造成的 RP 后果：** NPC按快照获得他人秘密，或同一人跨昵称忘记已知事项。

**建议处理：** 后续建立按主体、内容、来源、时间和确定度的认知状态；此阶段只审计。

## [S011] 禁止不知道者知道秘密，容易连合理怀疑也一并禁止

**严重程度：** MODERATE

**问题类型：** 认知／RP可执行性

**角色卡位置：** [ID 13｜ [mvu_plot]叙事守则与开局初始化](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_013.txt>)；[ID 59｜摩丝](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_059.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)；[ID 106｜剧情·卷2幕09·旧梦与岔路](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_106.txt>)；[ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)

**当前内容概述：** 未揭示秘密时“知情者滴水不漏，不知情者根本不知道有秘密”；摩丝条目对所有场内人物作统一要求。

**发现的问题：** 人物可察觉异常、误解和试探，不等于已确认真相；知情者也不是永远不失言。统一量词会覆盖真正知情角色。 第136—137回忆直接展示红被摩丝暗算和长期受控、妮妮被囚；她们不能正常告发，不等于不知道施害者。ID59所谓幕08前所有场内人物都只能视摩丝为普通局长的全称限制不成立。

**原著证据 / 定位：** [E006](01_evidence_index.md#e006)、[E012](01_evidence_index.md#e012)、[E027](01_evidence_index.md#e027)、[E036](01_evidence_index.md#e036)；ID59的全体知情限制需按原剧情回查；[E045](01_evidence_index.md#e045)、[E068](01_evidence_index.md#e068)、[E073](01_evidence_index.md#e073)、[E074](01_evidence_index.md#e074)、[E075](01_evidence_index.md#e075)、[E077](01_evidence_index.md#e077)、[E078](01_evidence_index.md#e078)；[E095](01_evidence_index.md#e095)、[E097](01_evidence_index.md#e097)、[E108](01_evidence_index.md#e108)、[E109](01_evidence_index.md#e109)、[E110](01_evidence_index.md#e110) [E126](01_evidence_index.md#e126)—[E128](01_evidence_index.md#e128)、[E140](01_evidence_index.md#e140)、[E148](01_evidence_index.md#e148)—[E152](01_evidence_index.md#e152)。；[E158](01_evidence_index.md#e158)—[E160](01_evidence_index.md#e160)、[E176](01_evidence_index.md#e176)；[E183](01_evidence_index.md#e183)、[E192](01_evidence_index.md#e192)—[E195](01_evidence_index.md#e195)、[E203](01_evidence_index.md#e203)、[E212](01_evidence_index.md#e212)；[E216](01_evidence_index.md#e216)、[E220](01_evidence_index.md#e220)—[E222](01_evidence_index.md#e222)、[E232](01_evidence_index.md#e232)—[E235](01_evidence_index.md#e235)；[E244](01_evidence_index.md#e244)、[E247](01_evidence_index.md#e247)、[E253](01_evidence_index.md#e253)、[E256](01_evidence_index.md#e256)、[E258](01_evidence_index.md#e258)、[E260](01_evidence_index.md#e260)、[E261](01_evidence_index.md#e261)；[E262](01_evidence_index.md#e262)、[E269](01_evidence_index.md#e269)、[E271](01_evidence_index.md#e271)、[E276](01_evidence_index.md#e276)、[E279](01_evidence_index.md#e279)、[E281](01_evidence_index.md#e281)—[E287](01_evidence_index.md#e287)；[E293](01_evidence_index.md#e293)、[E297](01_evidence_index.md#e297)、[E299](01_evidence_index.md#e299)—[E301](01_evidence_index.md#e301)、[E305](01_evidence_index.md#e305)、[E308](01_evidence_index.md#e308)—[E314](01_evidence_index.md#e314)；[E315](01_evidence_index.md#e315)、[E326](01_evidence_index.md#e326)、[E335](01_evidence_index.md#e335)、[E340](01_evidence_index.md#e340)、[E345](01_evidence_index.md#e345)；[E353](01_evidence_index.md#e353)—[E356](01_evidence_index.md#e356)、[E358](01_evidence_index.md#e358)、[E362](01_evidence_index.md#e362)、[E365](01_evidence_index.md#e365)、[E368](01_evidence_index.md#e368)、[E375](01_evidence_index.md#e375)；[E380](01_evidence_index.md#e380)、[E383](01_evidence_index.md#e383)、[E384](01_evidence_index.md#e384)、[E386](01_evidence_index.md#e386)、[E393](01_evidence_index.md#e393)、[E395](01_evidence_index.md#e395)、[E399](01_evidence_index.md#e399)；[E409](01_evidence_index.md#e409)、[E410](01_evidence_index.md#e410)、[E413](01_evidence_index.md#e413)、[E427](01_evidence_index.md#e427)；[E434](01_evidence_index.md#e434)—[E446](01_evidence_index.md#e446)；[E453](01_evidence_index.md#e453)、[E457](01_evidence_index.md#e457)、[E458](01_evidence_index.md#e458)、[E462](01_evidence_index.md#e462)、[E463](01_evidence_index.md#e463)、[E466](01_evidence_index.md#e466)、[E468](01_evidence_index.md#e468)；[E476](01_evidence_index.md#e476)—[E480](01_evidence_index.md#e480)、[E485](01_evidence_index.md#e485)、[E490](01_evidence_index.md#e490)；[E499](01_evidence_index.md#e499)—[E515](01_evidence_index.md#e515)；[E519](01_evidence_index.md#e519)、[E525](01_evidence_index.md#e525)、[E531](01_evidence_index.md#e531)、[E533](01_evidence_index.md#e533)；[E536](01_evidence_index.md#e536)、[E540](01_evidence_index.md#e540)、[E542](01_evidence_index.md#e542)—[E545](01_evidence_index.md#e545)

**证据等级：** A（具体知情反例与实际行为）

**更准确的理解：** 保持秘密不应抹掉观察能力或阻断按证据成长；须允许不知道、怀疑、误信、部分确认并存。 小璐见父亲与红熟识后猜翠雀关照缘由；林昀因手机归属误猜跟踪主谋；夏凉通过挂断试验确认他持翠雀手机，仍可误猜两人关系。不能用秘密未揭示让上述正常推理全部失效。 夏凉最终承認旧线索并不足以确定，主动用第二次手机试验求证；翠雀没有继续强行抵赖。王腾飞的错认、院长的辨认和小璐对两人私交的猜疑亦应各自保留。 木百合发现魔力是对的，误以为大叔暗算是错的，蛛照片又只推翻部分嫌疑；白蓟可验牌。翠雀由红视线/摩可垃圾、电话、员工物件逐步修正判断，不因秘密未揭示而完全看不见异常。 红早有受害知识却受限失声/遗忘，可经未被禁止的见妮妮绕行；限制作用于表达与行动而非抹去所有知情。反过来摩丝虽掌握旧号和战伤，却直到临死才推知男身。 续审06：林用电话借口掩失控，田见蓝光未识真身；白主动说漏嘴、林自己口误爸爸、夏有意顺误会、小璐用真线索拼错恋爱。林早标两暗子可合理留作调查，不等于他们认为未被发现就客观未暴露。需独立记录看见、相信、知道和能说，保密不要求人物永远不会失言。 续审07：白反复叫妈而小璐仍按乌龙理解，35一句妈妈不让却透露隐瞒；夏知真身也会临场尴尬撒谎。鸢财政仲裁官旧职和亲如姐妹说辞有真有假，林须逐步查档和试探；保密不抹观察。小璐关于红与翠的猜疑不等确恋爱或胁迫。38闯红灯骑车人后来由残兽出现补明逃命，先前无礼印象不应固化为人物事实。 续审08：小璐由游戏玩笑猜翠爱安雅、木把有余力的小璐当耗竭、含羞草把脸熟询问想成搭讪；均是可错的个人解释。翠从同名怀疑、网照不确定到舞台眼眸确认；夏从旧照联想到48获肯定。公开喜欢与额吻在公众看来是偶像互动，不能自动授予爱情或秘密身份的确认。 续审09：翠对玛舞台动机的预期49被当面解释修正；小对白蓟礼貌背后不满有观察，但白蓟对为你好仅推断。玛笑可表达不满，56认自己安抚判断失误，不是永久精准识心。苏名单无名不能排除暗中加入，失联不等死亡。线结可看见，命运意义仅翠未出口联想；62不说治疗理由是怕徒增顾虑，不是认定孩子必泄密。 续审10：夏把反击类比残兽不等认定残兽底色；翠对模拟偏移先担心再听解释、对白魔仍未知。白蓟误听导师评价，小误解关照仅母亲遗泽，都不变客观原话。白狼可按未独立确认报告行动；林73一度稍信只是喝酒又保持警戒，卡102所谓立即意识不可能只问候过度确定。知道局长增加陌生不等知道男身；保密叮嘱也不能阻止员工私传。 续审11：鸢确认女儿身份之前可怀疑婚育借口；翠对掉势由疑到试验、84读者获解释不等九人同获机制；含羞认错小后感魔和逐步实验改判。小89把翠极端关切推为寻找樱影子，叙述显示不是这个原因，不能当认母后即知父身份。 续审12：护卫启动经失败再试浊化、第三形态仍孵化；门记录存在与传闻有无分开。红把夏畏难误看兴奋、白记忆失真、木以气压耳痛联想到门排斥，均不能当客观机制。白狼转运消息为已核实的自述，未来安保判断仍预测。 续审13：翠对界桥异常不坦白；土丁桂看十岁证不疑、又不识旧号，翠不懂她为何注视直到问答。墨荷忘认证牌和面具才形成初遇障碍，未证她有识破所有术的能力。女王观礼可能、全场识魔与培训效率传闻、温泉美容均分等级。 续审14：翠120因梦想家描述减爪怀疑、121仅推有关联，墨121误把被缓拒归闯祸而翠纠正。白125把缩高错当新鞋，136回忆妮娜误觉被厌而矢并不怨。必须容许误解并保存获纠时点。 续审15：145矢承躲避曾不快，修正137不怨教学但非全关系从无不快；146疑墨非善到147组织确认，不代表动机都明。154黑市标红识组织不锁个人，与157多方识出著名金蛇可以并存。158三群道德判断为翠分类猜测，非客观道德表。 续审16：小先信背串、171复问改外因、172供述才证混乱术购买链；夏对压分的猜测已自行保留心理阴暗替代，不能将其都作恶者。薄目光令小怀疑白暴露但未证；薄对无出口/前方谜题的推论直到广播只部分证实。民间榜、姐妹脑测、土可考字牌/战力5分钟仍需分类。 续审17：197狗由回声游戏误解改实验认知，198土猜巢穴后199广播部分证，200紫疑笑后213确认；单次认证阻金蛇不能推全防无漏洞，208兽干瘪小明言不知吸何物，不能因像吸血鬼断其物种或具体吸魔。 续审18：223花单件评级经验承少见例外→225白B-反例当面校正，不写永不可能；224考官推偏移不识兽，227祖遗传潜力理论与实际授职不同，228翠自信技术来源仍无实物链。229意外反转近零暴露估计、231母自省、237武器直觉仍只翠信几分。 续审19：243夏被云限制不等月季恶意已证；249危险区传言见人就打被翠主动纠正。255箭能雾中否凝符的推测被本人部分确认且用反向融入换状态突破，不能扩成她所有状态禁术；257箭多抢不同数为全考生交易做法，不据此单独断恶谋。 续审20：260三次凶感自称不是精预言；264报告特殊A疑似信标与现场相似推演练需证据标签；266祖招数叫禁术为翠猜而实际黑球/柱可记；267蜂催化与无法令停是其自述，268两羽死亡有现场迹象，269消散不明确死亡/空间转移。

**可能造成的 RP 后果：** NPC显得迟钝，线索调查被封死，角色无法通过正常互动获知秘密。

**建议处理：** 后续逐人记录知道、可说、可做和被禁止之事，避免以全场一刀切守秘；不在本阶段改卡。

## [S012] 短事件列表与旧变量块裁剪可能丢失长期因果

**严重程度：** POTENTIAL RISK

**问题类型：** 开放式复查／记忆漂移

**角色卡位置：** [ID 10｜[mvu_update]变量更新规则](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_010.txt>)

**当前内容概述：** 大事记最多8条，旧记录删除；正则4从minDepth=6裁剪UpdateVariable块。

**发现的问题：** 二者不必然造成数据丢失，但在无长期知识账本时，承诺、误解来源及IF分歧容易从可见上下文消失。

**原著证据 / 定位：** ID10事件规则；data.extensions.regex_scripts[4]；schema未提供知识账本

**证据等级：** 技术直接证据；运行后果未验证

**更准确的理解：** 变量快照可能保留结果，却未必保留谁亲见、谁仅听说和为何作出承诺。不能把minDepth=6简单换算成实测3楼。

**可能造成的 RP 后果：** 长期RP关系和秘密反复重置，模型用常驻原作结局补回用户已经改变的事件。

**建议处理：** 后续区分状态、不可丢历史因果和短摘要；回放长对话验证。

## [S013] schema把未知或未提供状态默认成健康满魔力

**严重程度：** POTENTIAL RISK

**问题类型：** 开放式复查／状态语义

**角色卡位置：** 技术／源文位置见下方定位；[技术目录](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/technical>)

**当前内容概述：** 人物.魔力默认100、伤势默认无伤、变身状态默认未变身，阶段无；枚举错误回退。

**发现的问题：** 字段缺失可能表示未观测，也可能表示初始健康；同一默认值抹去这一区别。

**原著证据 / 定位：** technical/script_1.js人物Schema、Num、EnumOr

**证据等级：** 技术直接证据；实际触发未验证

**更准确的理解：** 默认值作为建角机制可以合理，但不应替缺失的NPC观测直接作事实断言。

**可能造成的 RP 后果：** 不在场伤者被“治愈”、无信息人物变成满魔力，影响战力和救援因果。

**建议处理：** 后续区分unknown与真实数值，记录观测时间；USER_CONFIRMATION_REQUIRED确认游戏默认规则。

## [S014] 手机并非纯显示层，包含第二套资料和生成链路

**严重程度：** MAJOR

**问题类型：** 结构／资料版本／开放式复查

**角色卡位置：** 技术／源文位置见下方定位；[技术目录](technical)

**当前内容概述：** script_3.js内嵌75人物、36地区、23势力、50CG及10组别名，独立生成聊天、论坛等。

**发现的问题：** 世界书修改不会自动证明手机快照资料同步；其中妮姆仍标魔装未觉醒等，继承旧断点。遗漏判断若不计它也会夸大“整张卡完全没有”。

**原著证据 / 定位：** technical/phone_catalog.json；script_3.js:1482起、1018–1059、10180–10190；[E034](01_evidence_index.md#e034)–[E040](01_evidence_index.md#e040)；[E544](01_evidence_index.md#e544)、[E312](01_evidence_index.md#e312)、[E526](01_evidence_index.md#e526)—[E529](01_evidence_index.md#e529)

**证据等级：** 技术直接证据＋A

**更准确的理解：** 需分三层：世界书正文、手机资料、手机模型提示。内嵌raw字段不等于全部注入正文。 第一阶段收尾：75人物全部sections与raw对应内容、36地区/23势力（已读世界书相同段逐字校验＋不同段全文读取）、50CG及10别名键已完成内容审计。映射见technical/CATALOG_REVIEW.md。小璐手机养女为新增C138；同人物谎言主体为C137。未明段自身与已知段冲突也需修，如柏安队称灯盏能力未展开、花园是否小世界仍未知；不能把资料末段的保守措辞当更高权威。

**可能造成的 RP 后果：** 两个渠道同一NPC说出不同历史，手机继续使用已过时人设；重构漏改隐藏副本。

**建议处理：** 后续统一资料来源和版本；遗漏报告明确存放层，不删除手机玩法。

## [S015] 手机安全章节筛选仍会送入身份秘密和后期经历

**严重程度：** MAJOR

**问题类型：** 认知／开放式复查

**角色卡位置：** 技术／源文位置见下方定位；[技术目录](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/technical>)

**当前内容概述：** safeDossier以标题白名单保留性格核心、外貌特征等，再替换未公开别名。

**发现的问题：** 林昀外貌段直接包含成年男性、翠雀与龙胆形态；薄荷性格段包含兽子、倒戈。替换姓名不能消除这些语义事实，也未按当前阶段裁剪。

**原著证据 / 定位：** script_3.js:12582–12605、12608–12633；phone_catalog.profiles.林昀/薄荷.sections

**证据等级：** 技术直接证据；NPC实际说漏属风险

**更准确的理解：** 已有别名遮蔽、匿名联系人token和防剧透系统规则值得保留，但不是逐事实知情控制。

**可能造成的 RP 后果：** 手机模型可在不说出被遮蔽名字的情况下透露男性身份、兽子经历或未来关系。

**建议处理：** 后续按事实与知情主体筛选资料，不只按标题与名字；用未知身份联系人做提示预览验证。

## [S016] 手机将整个MVU快照交给每次生成，未按联系人过滤

**严重程度：** MAJOR

**问题类型：** 认知／信息传播

**角色卡位置：** 技术／源文位置见下方定位；[技术目录](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/technical>)

**当前内容概述：** readLatestSnapshot返回latest.stat_data；safePromptSnapshot递归处理整对象；buildPrompt置于只读世界状态。

**发现的问题：** 递归函数处理长度、循环和别名，不区分目标联系人对不在场人物、玩家背景和事件的知情权限。

**原著证据 / 定位：** script_3.js:9972–10003、12636–12675、12874–12885、1034–1038

**证据等级：** 技术直接证据；实际泄漏未实测

**更准确的理解：** 只读限制能阻止该链路写主线，不等于阻止模型读取秘密；别名遮蔽也不建立信息来源。

**可能造成的 RP 后果：** 远方联系人知道现场伤势、玩家未告知背景或他人秘密行动。

**建议处理：** 后续为生成对象创建所知快照；保留独立沙盒与聊天切换令牌保护。

## [S017] 远程依赖未固定版本，无法仅靠PNG复现行为

**严重程度：** POTENTIAL RISK

**问题类型：** 技术／可复现性

**角色卡位置：** 技术／源文位置见下方定位；[技术目录](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/technical>)

**当前内容概述：** MVU和zod工具从GitHub分支路径经CDN加载，失败切换另一CDN。

**发现的问题：** 相同PNG在未来时间可加载不同依赖；z、_、$及TavernHelper等宿主能力依赖未随输入提供。

**原著证据 / 定位：** technical/script_0.js、script_1.js；未执行远程脚本或网络请求

**证据等级：** 技术直接证据

**更准确的理解：** 这是复现边界，不能据此断言恶意、不可用或已经泄露数据；手机媒体清单存在固定commit，应区别处理。

**可能造成的 RP 后果：** 变量迁移或API行为变化造成难以回溯的状态差异。

**建议处理：** 后续记录依赖版本、宿主版本与导入检查；仅在隔离环境做运行验证。

## [C001] 刘观山被归入异策局工作人员与第三小队

**严重程度：** MAJOR

**问题类型：** 人物身份

**角色卡位置：** [ID 0](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_000.txt>)

**当前内容概述：** 刘观山、李英伟、穆本生：异策局工作人员与第三小队骨干。

**发现的问题：** 原著介绍刘观山是高升公司外务派遣主任，与林昀同级；总览合并分组改变了人物社会身份。

**原著证据 / 定位：** [E007](01_evidence_index.md#e007)；全文刘观山4次命中L890、896、899、5582，其中后者仍为公司语境；[E092](01_evidence_index.md#e092)（第77章完整续读）

**证据等级：** A

**更准确的理解：** 刘观山是林昀职场同事；同一句列举不能覆盖不同人的所属。手机资料也有独立刘观山档案，应与总览交叉校验。

**可能造成的 RP 后果：** NPC拥有不应有的局内权限和战斗职责，办公室关系变成机构同僚关系。

**建议处理：** 后续修正总览分组；核对所有简写人物总览与长档案。

## [C002] 湿地公园残兽阶位错字形成不存在的蟹级

**严重程度：** MODERATE

**问题类型：** 专名／战力

**角色卡位置：** [ID 14｜剧情·卷1幕01·重返战场](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_014.txt>)

**当前内容概述：** 事件五称蟹级双头巨兽。

**发现的问题：** 原著该敌人为蠖阶；卡内等级总表也没有蟹级。

**原著证据 / 定位：** [E004](01_evidence_index.md#e004)，源文L642；同段后续等级复述L860附近

**证据等级：** A

**更准确的理解：** 使用原著卵、蠖、蛹等专有阶位；不因字形相近添加等级。

**可能造成的 RP 后果：** 模型将其当甲壳类独立等级或推错战力。

**建议处理：** 后续修正专名并扫描同类异体字；本次不改原卡。

## [C003] 匿名电话无法回拨被提前成当晚事实

**严重程度：** MAJOR

**问题类型：** 事件因果／时间

**角色卡位置：** [ID 14](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_014.txt>)

**当前内容概述：** 预警没有姓名、来源或可追踪回拨。

**发现的问题：** 当晚回拨能接通并给出湿地公园线索；次日再拨才不在服务范围。当前写法截断寻找女儿的情报来源。

**原著证据 / 定位：** [E003](01_evidence_index.md#e003)、[E006](01_evidence_index.md#e006)；源文L413–423、857附近；[E160](01_evidence_index.md#e160)

**证据等级：** A

**更准确的理解：** 区分不知来电者是谁、无法追查真实来源，与能否回拨取得新线索。 第137章红委托办卡并请妮妮以自身感应报警，补足第一通警告的来源链；这不改变当晚回拨能得新线索，也不让林昀在首章就认出来电者。

**可能造成的 RP 后果：** 林昀凭空定位公园，调查玩家尝试回拨会被错误拒绝。

**建议处理：** 后续修正事件先后与情报链。

## [C004] 将林小璐受困动机改成保护屏障外平民

**严重程度：** MAJOR

**问题类型：** 人物动机／事件

**角色卡位置：** [ID 14](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_014.txt>)

**当前内容概述：** 她明明害怕仍拒绝放弃屏障另一侧普通人。

**发现的问题：** 已读原段写她尝试撤退后被屏障拦住；此处增写平民与拒绝撤退，会抹去新人的恐惧和经验不足。

**原著证据 / 定位：** [E004](01_evidence_index.md#e004)；源文L549–557、597–642；[E084](01_evidence_index.md#e084)、[E098](01_evidence_index.md#e098)、[E102](01_evidence_index.md#e102)

**证据等级：** A（实际行动）；新增平民情节的Canon依据F

**更准确的理解：** 不能把被困结果反推成主动留守的英雄选择。若确为有意IF，应单独标识。 第64—66章仍有害怕熟人死亡及梦想困惑；第84—85章因院内老幼与伙伴主动坚持、第90章明确查仇保护愿望，属于成长后的选择，不推翻开篇撤退事实。

**可能造成的 RP 后果：** 过早完美化小璐，之后的撤退教学与成长缺少因果。

**建议处理：** USER_CONFIRMATION_REQUIRED确认是否有意改写；Canon基线应保留真实撤退尝试。

## [C005] 摩可的自述被改成冒充妮妮的承认

**严重程度：** MAJOR

**问题类型：** 身份／证据转述

**角色卡位置：** [ID 14｜剧情·卷1幕01·重返战场](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_014.txt>)；[ID 58｜摩可](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_058.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)

**当前内容概述：** 摩可承认冒充失踪前辈妮妮偷跑而来。

**发现的问题：** 实际对话讲上月偷跑来投奔妮妮，随后莫名收到播种者任命。是否合格、经验不足，与冒用妮妮身份是不同指控。

**原著证据 / 定位：** [E005](01_evidence_index.md#e005)、[E044](01_evidence_index.md#e044)、[E059](01_evidence_index.md#e059)、[E068](01_evidence_index.md#e068)、[E074](01_evidence_index.md#e074)；源文L751–778、1311–1313、2386–2388、3284、3865–3868；[E086](01_evidence_index.md#e086)、[E091](01_evidence_index.md#e091)、[E095](01_evidence_index.md#e095)、[E104](01_evidence_index.md#e104)；[E160](01_evidence_index.md#e160)；[E190](01_evidence_index.md#e190)；[E218](01_evidence_index.md#e218)；[E379](01_evidence_index.md#e379)；[E448](01_evidence_index.md#e448)

**证据等级：** D（摩可的自述），A（确实说了什么）

**更准确的理解：** 摩可自述偷跑投奔妮妮后获任命；第33章他城转交的国度回复确认有摩可登记。履历空白和能力不足不等于冒用妮妮姓名。追踪在招募后数天设置，仅粗定位，后来保留用于保障新人安全。 第76章翠雀向两新人提供福利院地址，第81章战中感应定位失效，不表示她一开始预知袭击。第93章院长提示摩可藏秘密但尚未解释，不能据此改判冒名已经坐实。 妮妮两年前遭囚、受拔羽榨魔已由回忆展示；摩可获任命的幕后安排仍未解释。确认旧播种者失踪缘由，不能反推新任者冒用其姓名。 续审06：妮妮已濒死获救并在基地教摩可。她拒绝替任，援引国度任命不可违，并把自己的失职/待回国度交割与摩可当前职责分开。正式撤职手续尚未展示，幕后任命缘由仍未知。 续审07：妮妮25章说昨晚接国度通知、今天返国观察培训待再指派，正式文件与魔镜预期送给摩可，尚未收到。她解释同花园魔力源、后天灵性及园丁培育；妖精没有人类姐妹亲缘，摩可出生晚且特殊，大妖精长纵容细因不能说。任命幕后依旧未知，不将新信息误当诈骗坐实。 续审13：103明确摩可现在已是官方认证方亭播种者，却坚决拒返国而不解释；随行只是惯例无明文强制。仍不等偷身份、任命手续幕后与拒返原因已破案。 续审15：160补月圆后联系猫眼/祖使摩可从偷渡、名不副实转合规，回响可用渠道随之改变；未说冒妮偷职位或本人拒返理由。

**可能造成的 RP 后果：** 错误定性诈骗身份，改变翠雀调查方向和后续任命逻辑。

**建议处理：** 后续修正转述与事件时间；旧待定位事项已获得上述证据，不再列为完全未知。真实任命背景仍随连续阅读复查。 妮妮获释待查项已解决；其是否获知男身仍待后文，不能因她在基地就默认全知。

## [C006] 前辈身份修补亲情的明确动机被否定

**严重程度：** MAJOR

**问题类型：** 心理／关系

**角色卡位置：** [ID 14｜剧情·卷1幕01·重返战场](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_014.txt>)；[ID 47｜林昀](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_047.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)；[ID 109｜剧情·卷2幕12·魔装考核](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_109.txt>)

**当前内容概述：** 他没有借前辈身份修补亲情，只把热情导向训练。

**发现的问题：** 原著内心明确希望借此更多了解女儿、弥合沟壑；隐瞒还带有被女儿赞美打乱原计划的局促。

**原著证据 / 定位：** [E006](01_evidence_index.md#e006)、[E008](01_evidence_index.md#e008)；源文L816–875、970；[E057](01_evidence_index.md#e057)、[E058](01_evidence_index.md#e058)、[E061](01_evidence_index.md#e061)、[E063](01_evidence_index.md#e063)、[E079](01_evidence_index.md#e079)；[E084](01_evidence_index.md#e084)、[E109](01_evidence_index.md#e109)、[E110](01_evidence_index.md#e110)；[E173](01_evidence_index.md#e173)、[E177](01_evidence_index.md#e177)；[E242](01_evidence_index.md#e242)、[E248](01_evidence_index.md#e248)、[E249](01_evidence_index.md#e249)；[E307](01_evidence_index.md#e307)—[E312](01_evidence_index.md#e312)；[E317](01_evidence_index.md#e317)、[E345](01_evidence_index.md#e345)—[E347](01_evidence_index.md#e347)；[E351](01_evidence_index.md#e351)、[E356](01_evidence_index.md#e356)、[E359](01_evidence_index.md#e359)；[E416](01_evidence_index.md#e416)、[E417](01_evidence_index.md#e417)、[E421](01_evidence_index.md#e421)、[E422](01_evidence_index.md#e422)；[E455](01_evidence_index.md#e455)、[E457](01_evidence_index.md#e457)、[E458](01_evidence_index.md#e458)；[E493](01_evidence_index.md#e493)、[E503](01_evidence_index.md#e503)、[E507](01_evidence_index.md#e507)、[E513](01_evidence_index.md#e513)；[E516](01_evidence_index.md#e516)、[E518](01_evidence_index.md#e518)、[E528](01_evidence_index.md#e528)、[E529](01_evidence_index.md#e529)、[E535](01_evidence_index.md#e535)

**证据等级：** A

**更准确的理解：** 训练保护和亲情修补可以同时存在；他既有责任感，也有私心、困窘和暂缓坦白。 第30章拒绝再借女儿向局方代问，不等于此前或此后都不借双重身份；第39章仍因父亲身份难管课业而转用翠雀，第60章回顾绕弯与谎言代价。 夜谈仍把翠雀视为父女桥梁；被夏凉识破后承认是因难以坦率面对小璐才连她也隐瞒，感觉卸下重担。 林曾因复仇可能令女儿失依而压抑复出；终章又意识到替女儿承担一切、什么都不说也是傲慢。小璐尚不知父亲身份却主动接住染血手，促他回到关系之中；未完成身份坦白，更非亲情已无障碍。 续审08：41林继续用双身份解释去向，仍回避向女儿坦白；42对白一度准备说出男身却因她希望多一个人关心而止住。随后主动认爸爸、重申母称承诺，不再只是此前口误或沉默默认；仍未完成法律收养或身份公开。 续审10：70原拟翠在基地过节、父以值班缺席；71明确合宿也是拉开父女距离、减负面印象，反向又用父亲身份聆听对翠的依恋。知局长反增陌生，关系不是已完全恢复。卡102所写最初独自在局里跨年、父亲陪伴已非退而求其次不能取代原计划和后文真实不安。 续审11：89亲子冲突明确让翠意识到把父亲劝阻直接套在队长身份上的错误；小已打算向父道歉，真正要的是战绩与依恋获认可。翠随后确实肯定战绩，不可记成始终不肯。丧妻意义危机与想保护所有后辈并存，玛邀观烟花时也表达未来愿望；不是永远纯理性导师或已完成全部亲情修复。 续审12：91回叙补全89认母答复：翠否认樱替影、承认迟早离开而许成熟后可跟来和此前可撒娇。94小又明确即翠退役仍因自己喜欢而继续；95新争宠表明承诺并未消除关怀分配矛盾。 续审14：133父以自己的身份反省严教/避魔造成疏远并道歉，小理解其担忧但仍不够亲密；王冠亲近与父蛋糕感受不同。卡105末把小仅作父母之外恩人会漏91已认母关系，128憧憬不自动取消该约定。 续审16：168主动容许同床因家长角色与孩子怕离队，170不再用三十出头父亲训斥法，171信背书后抚慰；有意渐放权同时保亲情。170仅想若一科差1—2分求通融，未实际改成绩；172改公开补考让受影响者重试，不能把私心推想写成既成舞弊。 续审18：216询夏想研究意愿但推到考后防连坐；227关三后辈且先问白，231由独断藏档失败反思傲慢关心、问小是否愿降分，小想公开承期待获尊重与夸奖。不是始终专制或即时全坦白，隐父身份和王庭险仍在。237女儿被打哭不迁怒公平切磋者，亲情与成人责任同存。 续审19：240先问女要不要见紫，242不愿因自己扼其未来、小可宁不当仍留到考后再议；252不因败责而追问胜法，253分队给历练，259不再追夏过保。承诺无险仍非结果保证，成年关切与放手并进。

**可能造成的 RP 后果：** 林昀被改成始终理性克制的导师，父女线最重要的内在矛盾被消除。

**建议处理：** 后续修正动机，保留矛盾与犹豫。

## [C007] 回家场景漏掉敲门谈话与道歉，日期也被跨日处理

**严重程度：** MODERATE

**问题类型：** 事件遗漏／时间

**角色卡位置：** [ID 14｜剧情·卷1幕01·重返战场](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_014.txt>)；[ID 47｜林昀](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_047.txt>)

**当前内容概述：** 新闻后以女儿兴奋回房、没有敲门质问概括；ID47写次日确认身份。

**发现的问题：** 源文当晚十点看回放后确认，并敲门谈话和道歉。注意“没有敲门质问”本身不等于“完全没敲门”，此项主要是省略关键和解动作与跨日错序。

**原著证据 / 定位：** [E001](01_evidence_index.md#e001)；源文L163–270

**证据等级：** A

**更准确的理解：** 不是直播时全家共同观看；此夜已存在笨拙的主动沟通，不能仅用“冷战到底”概括。

**可能造成的 RP 后果：** 亲子关系比原著更僵硬，后续修复失去早期尝试。

**建议处理：** 后续补充事件并校正相对先后；精确月日另待用户裁决。

## [C008] 心之花的旧伤与灰尘被写成种类特征

**严重程度：** MODERATE

**问题类型：** 外貌／世界规则

**角色卡位置：** [ID 20｜魔法少女](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_020.txt>)

**当前内容概述：** 魔法少女专属宝石布满细碎纹理，常沾尘。

**发现的问题：** 这是林昀长期封存、带旧伤的具体宝石外观，不是所有魔法少女宝石共有性质。

**原著证据 / 定位：** [E002](01_evidence_index.md#e002)；源文L279–286；[E389](01_evidence_index.md#e389)、[E392](01_evidence_index.md#e392)

**证据等级：** A

**更准确的理解：** 一般属性与个体当前完损、保养状态应分开。 续审13：108宝石裂隙已修补、实际魔装无痛，仍有永久毁缺及新材料沉淀要求；不能以旧裂痕灰尘定义心之花，亦不把新补完等同从未受损。

**可能造成的 RP 后果：** 所有新人的宝石自带裂纹或尘土，伤势提示失去区分。

**建议处理：** 后续移动到林昀相应历史阶段，不作普遍规则。

## [C009] 祭子与兽子的定义互相冲突，小璐猜测被写成已定性

**严重程度：** MAJOR

**问题类型：** 力量体系／认知

**角色卡位置：** [ID 5｜黑烬](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_005.txt>)；[ID 21｜残兽](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_021.txt>)；[ID 46｜林小璐](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_046.txt>)；[ID 47｜林昀](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_047.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)；[ID 17｜白静萱](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_017.txt>)；[ID 19｜薄荷](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_019.txt>)；[ID 109｜剧情·卷2幕12·魔装考核](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_109.txt>)；[ID 159｜黑烬黎明](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_159.txt>)；[ID 168｜使徒](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_168.txt>)；[ID 110｜剧情·卷2幕13·云境夺牌战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_110.txt>)

**当前内容概述：** ID21写后天兽子受教育成为祭子，又祭子参加食祭成兽子，并称小璐唯一天生兽子。

**发现的问题：** 与ID5天生祭子及“小璐疑似第二祭子”的记录直接冲突；同一段先称兽子再成为祭子形成分类循环。当前核验不足以把小璐身份升级为确定。 ID5的“小璐疑似第二祭子仅翠雀独疑”也不成立：兵触三第85章先如此认定，翠雀/红思与第94章共同猜其偏移者。三者说的是相关但并不等价的分类，不能合并成同一客观定义。 卷二第20章的检查并未提供祭子到兽子的完整普适转换公式，不能用已读白的诊断替卡21循环定义补证明。

**原著证据 / 定位：** ID5与ID21对读；[E020](01_evidence_index.md#e020)、[E036](01_evidence_index.md#e036)；关于更早造圣实验的完整源文尚待复核；[E090](01_evidence_index.md#e090)、[E098](01_evidence_index.md#e098)、[E102](01_evidence_index.md#e102)、[E105](01_evidence_index.md#e105)、[E112](01_evidence_index.md#e112)；[E196](01_evidence_index.md#e196)、[E199](01_evidence_index.md#e199)、[E204](01_evidence_index.md#e204)、[E205](01_evidence_index.md#e205)、[E208](01_evidence_index.md#e208)；[E247](01_evidence_index.md#e247)、[E248](01_evidence_index.md#e248)；[E336](01_evidence_index.md#e336)、[E338](01_evidence_index.md#e338)—[E341](01_evidence_index.md#e341)、[E346](01_evidence_index.md#e346)；[E356](01_evidence_index.md#e356)、[E368](01_evidence_index.md#e368)；[E486](01_evidence_index.md#e486)、[E489](01_evidence_index.md#e489)；[E494](01_evidence_index.md#e494)—[E497](01_evidence_index.md#e497)、[E504](01_evidence_index.md#e504)；[E521](01_evidence_index.md#e521)、[E523](01_evidence_index.md#e523)、[E532](01_evidence_index.md#e532)

**证据等级：** 卡内直接证据；A（诊断修订与战场行为发生）／D（祖诊断及七情报）／C（旧袭因果、造圣关联推测）／F（三词完整定义及小璐终极分类）

**更准确的理解：** 祭子、兽子、自然资质与实验结果分别记述；被结界吸入或拥有特殊魔力只是证据，不自动证明唯一天生兽子。 第75章兵触三的过强灵魂魔力病因到第99章获叙述支持，但宗教意义与祭子/兽子全部定义未因此一并证实。小璐白色魔力发生是A，兵触三祭子认定为D，翠雀/红偏移者判断为C；兵触三拟报蛾但被杀，未完成汇报。 续审06：祖先称白天生偏兽，体检后明确改成残兽偏向魔法少女；应保留这条诊断修订链。七称白是实验兽子、弃婴和研究员带出的孩子为敌方说法，父母死因尤其含其明示未知后的推论。祖对造圣来源只知三词、无释义，翠此时仍不知道研究员细节；小璐终极分类也未因此确定。 续审08：20时翠未闻研究员细节的判断保留为历史；42白在车里讲父母、失盒和敌人哼同曲，林由此部分理解战场虐杀原因。听觉理由增强她相信敌方的心理因果，不足以证父母恶意或七的全部身世论。林对人的伦理定义也不替代物种/祭子分类核验。 续审11：85/86王钥初析及魔力性质变化已出现，但未验证唯一天生兽子或完整祭子分类。卡102所谓卷二85第二祭子回溯实际不存在（C108）；卷一85原推断仍D。89玛虽杀过祭子，自称不知道定义，这时才听翠说白是祭子，不能由经历自动升级百科知情。 续审12：94护卫复现需浊化实测，余晶及安雅继承仅翠猜；99第三晶微波支持正在孵化的解释，但未完成新形态，小仍不知道母亲魔装。魔装训练未见外形变化不等无进展。 续审17：212白仅以耳语报告两人的残兽感，小说爪痕获不确定/更像兽答，转三者有联系的怀疑；此前93已听白自述祭子，却不等懂完整身世或知道薄箭同类。未说完的209你也是不补成已被当面确认祭子。 续审18：217小白早闻祭子兽子与圣子计划但不懂全定义；218薄给人类不改身心以兽为源/食祭晋阶和封笼成兽子解释，仍区分敌方自述。小由薄言到白近距弱似错觉只获微波旁证；220翠才回接去年亲听两个祭子，曾想田但从没想小，此时才真疑女儿且隐瞒。白亲自感小并在场，卡17全局不知道小疑似祭子已失效。228祖用天生爪作类比不等白加入爪。 续审19：245薄称真魔装生物/伪态及底色偏移为族群解释，小问薄真装不得用；不能把白普通天音等同已确认真生物形态。247王钥基础回满有重复战斗机制而非仅首次析出，受一次/充能/滞魔约束；256白焰与衣装变化已出现，未证小从此确切新阶或授权。

**可能造成的 RP 后果：** NPC不经调查便确认小璐秘密；建角把天赋与仪式结果混为一谈。

**建议处理：** 后续拆分定义，回查相关全部章节；删除“唯一”前需Canon证据，不能反向编造另一分类。

## [C010] 薄荷上级和姐妹关系沿用错误或过期状态

**严重程度：** MAJOR

**问题类型：** 组织所属／人物关系

**角色卡位置：** [ID 19｜薄荷](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_019.txt>)；[ID 38｜箭根薯](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_038.txt>)；[ID 109｜剧情·卷2幕12·魔装考核](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_109.txt>)；[ID 159｜黑烬黎明](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_159.txt>)；[ID 110｜剧情·卷2幕13·云境夺牌战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_110.txt>)

**当前内容概述：** 薄荷原直属上级蜂；与箭根薯仅同为兽子有旧怨。

**发现的问题：** 后文明确薄荷导师天牛、箭根薯导师蜂；二人为吴晰晴、吴惜雨姐妹，共同收养和食祭经历决定其选择。不可将同场任务等同同一导师。

**原著证据 / 定位：** [E021](01_evidence_index.md#e021)–[E023](01_evidence_index.md#e023)；源文L36895–37162；[E481](01_evidence_index.md#e481)、[E486](01_evidence_index.md#e486)、[E489](01_evidence_index.md#e489)；[E494](01_evidence_index.md#e494)—[E497](01_evidence_index.md#e497)、[E504](01_evidence_index.md#e504)；[E521](01_evidence_index.md#e521)、[E526](01_evidence_index.md#e526)、[E533](01_evidence_index.md#e533)

**证据等级：** A

**更准确的理解：** 分导师、行动安排者与组织上层；同时保留姐妹争执、伤害、内疚和依恋。 续审17：203箭叫薄好姐妹、204薄示静止并称旧对手，209冲突、212暂拒在观礼场合谈后约饭；这些显示彼此有认知但小还没获同门、层级、契约全信息，不能把场面叫法当组织等级。 续审18：218/219薄自称不接此次任务，只知别兽第四场行动，自述和监护导师属进步派，不把全5人都认蜂直属同一任务；220主动放过要经事后查罪，若有恶非免责，227/228保薄有风险。薄的濒危摊牌由217误认→放波引箭→约饭翻车触发，不足证她早就长期深恨整个组织并专为逃脱来考试。 续审19：245箭亲口明薄不参与此次行动，与薄自述互证，卡19蜂派入五暗子整体化过强；257再次强调不同派松散并不知高调真因。250薄被脸相似引向本人想法而小打断，不能不带时段地说她从未联想到龙矢。

**可能造成的 RP 后果：** 把有共同家庭史的姐妹演成普通敌对同僚，薄荷一律逃命或箭根薯必然死战。

**建议处理：** 后续修正所属与关系阶段；新增后文共同作战状态。

## [C011] 金蛇能力被永久锁定为未知

**严重程度：** MAJOR

**问题类型：** 能力／限制

**角色卡位置：** [ID 32｜金蛇](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_032.txt>)；[ID 111｜剧情·卷2幕14·回忆·1979卢恩诺雷守卫战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_111.txt>)

**当前内容概述：** 魔装、奇境、医疗能力和兽化战法均未公开，能力不能超出三次凶感。

**发现的问题：** 273–278展示券契、郁金香市集、交易回撤与信用抵押限制；强行禁止这些能力会严重削弱人物。

**原著证据 / 定位：** [E017](01_evidence_index.md#e017)–[E019](01_evidence_index.md#e019)、[E024](01_evidence_index.md#e024)；源文L36410–37228；[E536](01_evidence_index.md#e536)、[E538](01_evidence_index.md#e538)、[E543](01_evidence_index.md#e543)

**证据等级：** A；祖母绿破局机制仍F

**更准确的理解：** 完整记录交易条件、风险、循环和对手破局；三次强烈应验不是能力一生只能发动三次的次数上限。 续审20：260凶感三次是本人归纳且第三事态未终，不可写三次全应验；其过去医疗身份、灾前与矢点头之交经262实写。卡32性格段单写丧父与同卡多处石母冲突，仅石蒜母亲亡已证不能另造父亡。后271—275券契/奇境已明仍依E017—E019，不能用260未知覆盖后段。

**可能造成的 RP 后果：** 金蛇无法执行原著已完成的交易战术，反而可能被随意写成预知系。

**建议处理：** 后续按阶段补充机制、代价及实战；别反向推成无限修改现实。

## [C012] 褐鹈的旧身份与被捕状态仍被列未知

**严重程度：** MAJOR

**问题类型：** 人物／事件状态

**角色卡位置：** [ID 34｜褐鹈](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_034.txt>)

**当前内容概述：** 旧身份、袭击结果未知，当前仍在据点熬制秘密武器。

**发现的问题：** 272章已捕获褐鹈，并给出木槿及民治院经历和秘密关押去向。

**原著证据 / 定位：** [E014](01_evidence_index.md#e014)、[E015](01_evidence_index.md#e015)；源文L36314–36352

**证据等级：** A；审讯威胁为D

**更准确的理解：** 旧状态在较早开局可成立，不能作为所有后期的永恒当前；糖果屋所有细则仍未必已明。

**可能造成的 RP 后果：** 已囚禁角色继续在外执行任务，知情者不知道抓捕结果。

**建议处理：** 后续新增捕获与保密处置阶段，区别监管机构。

## [C013] 黑猫最关键的丧亲、义肢和刺杀目标仍列未知

**严重程度：** MAJOR

**问题类型：** 人物经历／组织／动机

**角色卡位置：** [ID 64｜黑猫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_064.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)；[ID 106｜剧情·卷2幕09·旧梦与岔路](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_106.txt>)；[ID 162｜卢恩诺雷城防军](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_162.txt>)；[ID 167｜矢车菊小队](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_167.txt>)；[ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)；[ID 111｜剧情·卷2幕14·回忆·1979卢恩诺雷守卫战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_111.txt>)

**当前内容概述：** 妮姆下落、义肢来源、另一个使命均未揭晓；爪痕仅写现任副首领。

**发现的问题：** 279–282及281回忆明确妹妹牺牲、认证牌托付、义肢材料、刺杀女王与替换魔力底色方案；另说明早期爪痕由墨荷建立的历史。

**原著证据 / 定位：** [E028](01_evidence_index.md#e028)–[E029](01_evidence_index.md#e029)、[E033](01_evidence_index.md#e033)–[E037](01_evidence_index.md#e037)；[E333](01_evidence_index.md#e333)、[E334](01_evidence_index.md#e334)；[E391](01_evidence_index.md#e391)、[E395](01_evidence_index.md#e395)、[E396](01_evidence_index.md#e396)、[E399](01_evidence_index.md#e399)；[E407](01_evidence_index.md#e407)—[E410](01_evidence_index.md#e410)、[E418](01_evidence_index.md#e418)、[E419](01_evidence_index.md#e419)、[E427](01_evidence_index.md#e427)；[E434](01_evidence_index.md#e434)—[E436](01_evidence_index.md#e436)、[E445](01_evidence_index.md#e445)、[E446](01_evidence_index.md#e446)；[E480](01_evidence_index.md#e480)；[E538](01_evidence_index.md#e538)—[E545](01_evidence_index.md#e545)；[E334](01_evidence_index.md#e334)、[E395](01_evidence_index.md#e395)、[E545](01_evidence_index.md#e545)、[E033](01_evidence_index.md#e033)

**证据等级：** A；救济计划可行性及部分政治解释D

**更准确的理解：** 历史创始与现任副首领不矛盾，必须分别写时期；她的复仇、组织理想和对队长感情共同作用。 续审11：83先由塞米回忆补独臂少女救猫、共同旅行、拒强退与三日后兽化回返；叙述给黑猫称号但未给姓名、手别、义肢材料。卡64已有塞米关系和强退阶段，不能说整段缺失；旧末段关于身份/妹妹/义肢的已证资料仍须独立补齐，不能倒灌给83场内他人。 续审13：108明确妮娜14/妮姆10、同队因姐妹恳求及石蒜收回响；矢起初疑镀金后知真相转接纳。109摘皮质面具才认墨荷，110义肢妖精技术为其自述而翠存疑，111国度任务也只被翠暂信；不可让当前翠拥有读者已知黑猫全貌。旧末段关于妹妹/义肢等结果仍有效但不提前NPC知情。 续审14：119墨自述高层传言→15/16年前樱核流放，120自述团队知三次昙开及能修魔装，翠未确认技术。翠从减弱爪怀疑到121凭沉默推联系，131只认郁金香旧身份；听黑半字不等获黑猫代号。卡167/106仍将妮姆去向未明作为全局状态须沿末段修，历史137她活着上课不能倒灌结局。 续审15：146祖答郁已爪后翠才确认墨团队；157祖明确郁现名金蛇；其关于初爪财政/旧军组成仍人物现有名单，需与末段墨创立史分期。145墨自我发现嫉妒、矢承躲避不快后因战友而释，是137误解的后补，非从始全无负面。 续审17：201旁白明确猫姐即墨荷，这是读者身份确认；202旧友自承责任、限制无谓伤平民孩子、为免招矢全体敌，不是已知她一切任务或无条件反伤害誓言。翠未在该密谈，不得到蜂/蛾兽源交易。 续审20：262矢主动调妮姆城内、263队零伤亡仍外友死，264看同型兽才推旧袭或演练，265墨亲见妹安全后归，267离城时再次不知海蒂生死。269墨怕虚假希望未告矢规避猜，伸手尚未写结果；281断臂/妹妹死/认证牌叙述才补全，不能改成先知必救或简单牺牲性人格。 第一阶段收尾：手机妮娜/妮姆/塞米相关记录也须按阶段同步（见technical/CATALOG_REVIEW.md）。83已述塞米划伤本相导致永久失臂，281明确右侧；因果不是完全未知，但现场具体动作不可补成咬断。269伸手与281转述不让翠当时直接知道塞米全过程；人皮面具应守109皮质面具的材质边界，不推断人皮来源。

**可能造成的 RP 后果：** 丧亲动机被悬空，刺杀变成凭空转恶或单纯嫉妒女王。

**建议处理：** 后续补足阶段、事实与人物立场，保持“曾受害”不等于“现行为全正当”。

## [C014] 女王的寡言克制被固定成禁止长篇解释与亲昵

**严重程度：** MAJOR

**问题类型：** 人格标签化／阶段

**角色卡位置：** [ID 66｜女王](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_066.txt>)

**当前内容概述：** 不得给女王添加轻佻口癖、长篇解释或轻易表露情绪；蔷薇宫问答未完整展示。

**发现的问题：** 280章呈现长篇问答；282章对翠雀表现过度亲昵、挑衅黑猫，翠雀觉得异质与不适。旧约束会阻止已出现的表现。

**原著证据 / 定位：** [E031](01_evidence_index.md#e031)–[E032](01_evidence_index.md#e032)、[E037](01_evidence_index.md#e037)；源文L37924–38228、38595–38668；[E464](01_evidence_index.md#e464)、[E469](01_evidence_index.md#e469)；[E479](01_evidence_index.md#e479)、[E490](01_evidence_index.md#e490)；[E509](01_evidence_index.md#e509)、[E515](01_evidence_index.md#e515)

**证据等级：** A（言行与翠雀反应）；女王的解释D

**更准确的理解：** 公共仪式、1979私人谈话、2000与翠雀互动需分开；她声称学会爱不等于叙述保证真爱。 续审16：182仪式女王确实不语/无影，189高席只见朦胧身影；这能支持该公共阶段少言，不会撤销280—282私谈长篇与亲昵反例。阳光穿透原因尚未此处揭示；卡66对此不擅猜原因的约束可保留。 续审17：200紫疑女王嘴角可能错觉，213护卫听笑和考官裁决才确认该处女王笑且未制止；非明确出口法令，更不能以当时沉默抹去末段言语。 续审18：233女王经妖精转令紫验证并要求单列评级、当天SS公开；间接传令同样是明确意志但不等本人当众开口。239祖只从紫转来大概率判断，翠此时才获见女儿要求，不应把233读者情报早注祖翠。

**可能造成的 RP 后果：** 女王变成只会沉默发布旨意的模板；或另一极端被写成无条件慈母。

**建议处理：** 后续保留多场景差异和陈述归属，不替其政治理由背书。

## [C015] 狗尾草与土丁桂的部分身份认知停在揭露前

**严重程度：** MAJOR

**问题类型：** 认知更新

**角色卡位置：** [ID 31｜狗尾草](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_031.txt>)；[ID 43｜土丁桂](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_043.txt>)；[ID 47｜林昀](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_047.txt>)；[ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)；[ID 108｜剧情·卷2幕11·花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_108.txt>)；[ID 110｜剧情·卷2幕13·云境夺牌战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_110.txt>)

**当前内容概述：** 狗尾草、土丁桂仍不知道龙胆就是矢车菊；土丁桂以为是其女儿。

**发现的问题：** 270章翠雀亲口向两人揭示魔法少女身份链，271章描述反应；但未公开林昀男性本体。

**原著证据 / 定位：** [E012](01_evidence_index.md#e012)；源文L36205–36257；[E453](01_evidence_index.md#e453)、[E461](01_evidence_index.md#e461)、[E466](01_evidence_index.md#e466)、[E467](01_evidence_index.md#e467)；[E475](01_evidence_index.md#e475)、[E484](01_evidence_index.md#e484)、[E488](01_evidence_index.md#e488)、[E491](01_evidence_index.md#e491)；[E526](01_evidence_index.md#e526)、[E527](01_evidence_index.md#e527)、[E529](01_evidence_index.md#e529)、[E535](01_evidence_index.md#e535)

**证据等级：** A

**更准确的理解：** 拆为龙胆→翠雀、翠雀→矢车菊、翠雀→林昀等不同信息边。两人已知前两边，不能由此一并知道后一边。 续审16：166土见龙胆联想蓝星后自己当错觉；185/186摸头源于妹妹习惯并被提醒道歉，非识破暗号。176/177狗先知衣装再获龙胆代号/致敬前辈，尚未识矢；这些前期状态仍成立，270揭露后才失效。 续审17：196翠主动道谢破冰、207调节话题、211压力劝慰、214土请求姐姐；均在龙胆假身份下发展，土只是觉得像大人/讲话有价值，未识矢。最终揭露不倒灌这段亲近。 续审19：250小急编矢小孩→251土以自己严师/小姨家世解龙忧郁(误推)→253翠不否并丝线掌书任务预告→259土狗亲近赠牌仍女儿假说。270已读真身份告知才替换，旧卡43/31全局维持女儿应保前史改当前。

**可能造成的 RP 后果：** 后期仍重复同一个误会，或一次揭面导致全体考生知道父亲身份。

**建议处理：** 后续新增两位当事人的知识更新时间、来源与范围。

## [C016] 将末场考核无法叫停写成客观制度

**严重程度：** MAJOR

**问题类型：** 制度／事件

**角色卡位置：** [ID 4｜国度与政治](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_004.txt>)；[ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)

**当前内容概述：** 模拟大兽灾极度危险无法叫停。

**发现的问题：** 279章考核确实暂停并撤离考生；无法立即处理食祭结界与无法发布停考命令并不是一回事。

**原著证据 / 定位：** [E027](01_evidence_index.md#e027)、[E036](01_evidence_index.md#e036)；源文L37391–37414、38524–38525；[E272](01_evidence_index.md#e272)、[E273](01_evidence_index.md#e273)、[E286](01_evidence_index.md#e286)；[E452](01_evidence_index.md#e452)、[E454](01_evidence_index.md#e454)

**证据等级：** A

**更准确的理解：** 考试组织可中止，但敌方仪式和实战威胁可能继续；安全控制不是一个开关。 续审09：54玛称项目已投入、欲停恐需现钻石或贵族，不是任何人均无法停的客观制度；62撤销的是双方私定的比试禁考条件，亦非中止正式考核。早前末段已见真正停考，仍不把后期消息倒灌现在。 续审16：164常规7花牌强安保与女王怒火预测，使共同体选择须在其察觉前阻止；167已预演加搜查，仍有政治保密和获功需求。107所谓不能轻易中止须当计划成本，不升级成绝对无中止权限。

**可能造成的 RP 后果：** 组织拒绝本可发布的撤离命令，所有人被强制留考场。

**建议处理：** 后续区分考核状态、人员撤离和结界解除条件。

## [C017] 盛开被标作者未写入书中的设定，实际282已明示

**严重程度：** MODERATE

**问题类型：** 能力／元信息

**角色卡位置：** [ID 24｜开华](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_024.txt>)

**当前内容概述：** 注意按作者没有写入书中的设定，随后介绍盛开与大繁盛开。

**发现的问题：** 282章直接解释花级盛开、最高强化纪录、强花门槛与翠雀应用；旧出处标记失效。

**原著证据 / 定位：** [E038](01_evidence_index.md#e038)；源文L38684–38693；[E448](01_evidence_index.md#e448)

**证据等级：** A

**更准确的理解：** “最高纪录原能力两倍”不表示每个花级固定翻倍；盛开与完整繁开应区别。此前外部作者设定的来源仍未随文件提供。 续审15：160千年历史与翠自身都认为花后无路，安不断强化未开华；这是当时认识，不得因该段旁白存在而继续用未写入正文否定282盛开。开华新阶段与总魔量仍可提升分开。

**可能造成的 RP 后果：** 模型把正文事实当外部扩展，或任意给所有人统一倍率。

**建议处理：** 后续更换为本地原著证据并保留条件；外部出处作为待裁决来源。

## [C018] 黑猫心解与翠雀繁开名称缺失，未知边界需要重划

**严重程度：** MAJOR

**问题类型：** 能力／战绩

**角色卡位置：** [ID 47｜林昀](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_047.txt>)；[ID 64｜黑猫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_064.txt>)

**当前内容概述：** 沿用握今旧形态，未收录恨今难握及幻命织华。

**发现的问题：** 282章已有心解实战、时间错位推理、范围静止和繁开诱饵。文件止于幻命织华唱名，能力完整内容与胜负仍未知。

**原著证据 / 定位：** [E038](01_evidence_index.md#e038)–[E040](01_evidence_index.md#e040)；全文所有提取世界书与手机脚本中两名称均0命中

**证据等级：** A（名称与实战）；C/D（部分推理）；F（未展开内容）

**更准确的理解：** 不能同时犯“已知仍未知”和“名称已知所以机制全知”两种错误。魔力量约束部分由实战支持，具体普适上限仍未明。

**可能造成的 RP 后果：** 黑猫被削成只能抓住单物体；翠雀被凭空补出终局必胜能力。

**建议处理：** 后续补充已展示能力、推断标签与严格截止点。

## [C019] 回响归属从单场合理分配升级为绝对抢尾刀规则

**严重程度：** POTENTIAL RISK

**问题类型：** 世界规则／过度概括

**角色卡位置：** [ID 28｜回响(残兽核心/兑换物)](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_028.txt>)

**当前内容概述：** 只要不是最终击败者便不具备回响收集权。

**发现的问题：** 原著L701说明此次收取理所当然，没有在该句确立所有协作战斗的排他规则。全文相关场景核验后仍不能下定论说相反规则已证实，具体分配与普适所有权需分开。

**原著证据 / 定位：** 源文L697–703；E013的考核积分均分属于另一套规则，不能直接用来证明回响应均分；[E055](01_evidence_index.md#e055)、[E056](01_evidence_index.md#e056)、[E069](01_evidence_index.md#e069)、[E079](01_evidence_index.md#e079)（实操／用途，非所有权判例） [E130](01_evidence_index.md#e130)、[E150](01_evidence_index.md#e150)；L9133–9140。；[E448](01_evidence_index.md#e448)；[E448](01_evidence_index.md#e448)、[E545](01_evidence_index.md#e545)

**证据等级：** A（局部叙述）；绝对制度依据F

**更准确的理解：** 战利品、贡献奖励、考核积分分别核验；实际代为收取与法律所有权也不同。 第29章掌中取得回响并计划留给新人，第46章考虑部分补贴家用，第60章新人战后收取：这些补足用途与动作，不能自动升级成尾刀规则已被推翻。 第116章出现击杀后无回响的异常，原因尚未释明；该事实应另记产物/来源异常，不解决排他收取权的争议。 续审15：160翠将积存回响投后辈、玛大成本投柏安，收集/贡献/奖励和二次赠与应区分。不能以最终击败者就推其他人绝不能获资源，但也不以赠与直接证明初始收集权相反。 第一阶段收尾：所给源文现已完整读完；相关收取、馈赠、贡献和认证积分仍未确立普适排他尾刀所有权，也没有据此确立相反法条。维持POTENTIAL RISK／制度F；U005保留玩法选择，而非继续等本文件未读章节。

**可能造成的 RP 后果：** 团队鼓励抢最后一击，协作和救援因奖励规则被扭曲。

**建议处理：** 保持绝对制度未证；如有意作为游戏分配机制，见U005 USER_CONFIRMATION_REQUIRED。

## [C020] 首幕补写中家庭知情提前与具体撤退规约缺证（联络约定已获支持）

**严重程度：** MODERATE

**问题类型：** 人物选择／IF边界

**角色卡位置：** [ID 14｜剧情·卷1幕01·重返战场](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_014.txt>)；[ID 81｜夏凉](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_081.txt>)

**当前内容概述：** ID14把招募后写清撤退规约、翠雀已独知夏凉家庭真相放在首幕；联系方式、同地授课和留回响也在补充段中。

**发现的问题：** 第16章1346–1347明确回补招募后交换联系方式及隔日晚间同地点授课，应撤回对这两项本身的缺证判断。第29章2169及第46章3336支持把回响用于新人发展的意图，但不能证明首幕已有实际分配。逐一写下紧急撤退路线仍未获所读正文支持；夏凉家庭真相则到第41章才让翠雀惊讶获知、第44章才明确仅向她保密。旧场景与后期发展被提前拼接。

**原著证据 / 定位：** [E009](01_evidence_index.md#e009)、[E045](01_evidence_index.md#e045)、[E048](01_evidence_index.md#e048)、[E054](01_evidence_index.md#e054)、[E056](01_evidence_index.md#e056)、[E064](01_evidence_index.md#e064)、[E065](01_evidence_index.md#e065)、[E067](01_evidence_index.md#e067)、[E069](01_evidence_index.md#e069)；L1346–1347、1596–1598、2169、2985–2988、3224–3232、3336；[E045](01_evidence_index.md#e045)、[E064](01_evidence_index.md#e064)、[E067](01_evidence_index.md#e067)

**证据等级：** A（联系方式、授课、获知时点与内心）；具体写下的撤退规约出处F

**更准确的理解：** 逐项区分：交换联系方式/同地授课已有支持；留回响有后期意图依据；书面撤退路线经全文审计仍无对应原场景依据；家庭秘密不能倒灌招募阶段。第42—43章补充被需要与自救的长期动机，也不能删去第15章即时试探和选择过程。 第一阶段收尾：完整阅读结束后，具体逐人书写紧急撤退路线仍未获对应原场景依据；保留U003疑似补桥。已获支持的联系方式、授课和后期家事揭露不重新列为无源。

**可能造成的 RP 后果：** 若全盘认定补写，会误删原著后文回补；若全盘接受首幕补写，会让翠雀提前知道家事并改变夏凉后续倾诉意义。

**建议处理：** 保留C020编号并收窄范围。USER_CONFIRMATION_REQUIRED只覆盖仍疑似IF的具体规约/动机桥段；不再要求裁决正文已确认的联络行为。

## [R001] 命运骰的成功档位与不可逾越能力条件需明确边界

**严重程度：** POTENTIAL RISK

**问题类型：** 玩法／战力／IF

**角色卡位置：** [ID 12｜[mvu_plot]命运骰与检定](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_012.txt>)；[ID 179｜创作基调](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_179.txt>)

**当前内容概述：** 1d20固定成败档，伤势与阶段只修饰叙事，不改变档位；真实悬念才检定。

**发现的问题：** “存在真实悬念”有一定保护，但没有明确不可实施、必然失败与可检定目标的裁定过程；可能先让不可能行动掷骰，再反推成功理由。

**原著证据 / 定位：** ID12完整规则；ID179要求既定规则不临时失效；[E017](01_evidence_index.md#e017)–[E019](01_evidence_index.md#e019)、[E038](01_evidence_index.md#e038)–[E040](01_evidence_index.md#e040)展示条件的重要性

**证据等级：** 技术／玩法直接证据，非Canon错误

**更准确的理解：** 骰子是明确游戏机制，不应因原著没有而删除。需先决定行动可行范围，再确定骰子能改变的结果。

**可能造成的 RP 后果：** 低阶角色凭高骰突破硬限制，或真实无悬念动作因强制失败引出失实代价。

**建议处理：** USER_CONFIRMATION_REQUIRED：硬规则优先的检定，或明确标记可改写规则的奇迹玩法；不替用户选择。

## [R002] 好感与CG已有限制，但对不同关系类型和能力阶段约束不足

**严重程度：** POTENTIAL RISK

**问题类型：** User中心化／关系／玩法

**角色卡位置：** [ID 180｜[mvu_update]羁绊与CG图鉴](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_180.txt>)

**当前内容概述：** 0–200统一好感阶梯；50CG含约会、照护、共浴、引离传送。

**发现的问题：** 卡已明确不能机械覆盖实际关系、必须完成场景，故不能指控自动亲密；但同一数值不能表达信任、亲情、畏惧和恋爱差异，也未在每个CG另列能力阶段。

**原著证据 / 定位：** ID180 L3–13、41；ID179玩家不天然成为中心

**证据等级：** 玩法直接证据；结果风险待实测

**更准确的理解：** 这些是明确RP设计，不是原著遗漏。应保留角色选择与原有关系，亲密场景由实际情境成立，能力依阶段可用。

**可能造成的 RP 后果：** 为了达成解锁场景安排没有动机的约会，或提前使用引离高阶功能。

**建议处理：** USER_CONFIRMATION_REQUIRED确认玩法与Canon边界；后续检验同样好感下不同关系、拒绝情境与未觉醒角色。

## [R003] 注入资料混有章节、原著断点和外部作品说明

**严重程度：** POTENTIAL RISK

**问题类型：** 元信息／视角污染

**角色卡位置：** [ID 24｜开华](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_024.txt>)；[ID 27｜起源与出现](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_027.txt>)；[ID 111｜剧情·卷2幕14·回忆·1979卢恩诺雷守卫战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_111.txt>)；[ID 178｜剧情索引](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_178.txt>)

**当前内容概述：** 原文、断更、章节编号、作者未写入设定、neta结城友奈满开等进入世界书content。

**发现的问题：** 这些不是仅存作者备注；条目启用时有进入模型上下文的通道。模型需要后台定位信息不等于NPC应说出小说章节。

**原著证据 / 定位：** 各条目content与启用配置；ID178章节索引、ID24外部作品说明

**证据等级：** 技术直接证据；实际台词污染未实测

**更准确的理解：** 章节引用可保留在审计和后台索引，RP层需标明仅后台用途；外部作者资料不是本任务的Canon证据。

**可能造成的 RP 后果：** NPC提及作者安排或断更，旁白按后续章节提前宣布命运。

**建议处理：** 后续移动后台元数据并保留可追溯定位；外部设定USER_CONFIRMATION_REQUIRED。

## [R004] 土丁桂外貌段落有明显未完句

**严重程度：** MINOR

**问题类型：** 文本完整性

**角色卡位置：** [ID 43｜土丁桂](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_043.txt>)

**当前内容概述：** 灰白色长发平时半扎双马尾，考核。实际正文在“考核”后换到魔法／战斗形态。

**发现的问题：** 导出内容在描述中途断开，后续字段直接接续；并不是JSON解析失败。

**原著证据 / 定位：** ID43外貌段L5–6；technical/phone_catalog中相应角色档案可供后续版本对照，但仍非Canon

**证据等级：** 卡面直接证据；缺失文字内容F

**更准确的理解：** 只能确认句子残缺，不自行猜出发色、衣装或考核前后的缺失描述。

**可能造成的 RP 后果：** 生成时把残句强行补成未经核验的细节。

**建议处理：** 后续回原著补证或改为完整已知陈述，不凭另一个旧卡副本自动修复。

## [R005] 原著输入部分句段疑似残缺，需要保留上游质量边界

**严重程度：** POTENTIAL RISK

**问题类型：** 开放式复查／证据完整性

**角色卡位置：** 技术／源文位置见下方定位；[技术目录](technical)

**当前内容概述：** 源文个别行在抓、为什、说明蜂对自己的等片段处中断。

**发现的问题：** 没有U+FFFD不代表全文内容绝对完整；须区分排版截句、作者留白与抓取丢字。282章思维中的■有明确剧情功能，不能视作乱码自动清洗。

**原著证据 / 定位：** 源文L36924、36950、37458；E039所含■的上下文；L4459、5796、6040、6108；第77章L5589王滕飞/L5596王腾飞字形变体 L9270独立冒号、L10397红思与处截断、L11005向着自己身后处疑似残句；E129所列L8667/9062两天与四天。；[E163](01_evidence_index.md#e163)；L11792对照E144—[E146](01_evidence_index.md#e146)；[E202](01_evidence_index.md#e202)、[E208](01_evidence_index.md#e208)；L14529、14901；[E213](01_evidence_index.md#e213)、[E225](01_evidence_index.md#e225)、[E229](01_evidence_index.md#e229)；[E252](01_evidence_index.md#e252)、[E256](01_evidence_index.md#e256)；L17724、L17985；[E265](01_evidence_index.md#e265)、[E270](01_evidence_index.md#e270)、[E273](01_evidence_index.md#e273)、[E277](01_evidence_index.md#e277)、[E279](01_evidence_index.md#e279)、[E286](01_evidence_index.md#e286)、[E287](01_evidence_index.md#e287)；L18536、L18833、L19618、L19673；[E319](01_evidence_index.md#e319)、[E323](01_evidence_index.md#e323)、[E326](01_evidence_index.md#e326)、[E336](01_evidence_index.md#e336)、[E342](01_evidence_index.md#e342)、[E345](01_evidence_index.md#e345)；[E350](01_evidence_index.md#e350)—[E353](01_evidence_index.md#e353)、[E359](01_evidence_index.md#e359)、[E371](01_evidence_index.md#e371)、[E374](01_evidence_index.md#e374)；[E379](01_evidence_index.md#e379)、[E399](01_evidence_index.md#e399)、[E402](01_evidence_index.md#e402)；[E412](01_evidence_index.md#e412)、[E414](01_evidence_index.md#e414)、[E417](01_evidence_index.md#e417)、[E419](01_evidence_index.md#e419)；[E434](01_evidence_index.md#e434)、[E442](01_evidence_index.md#e442)、[E450](01_evidence_index.md#e450)；[E452](01_evidence_index.md#e452)、[E457](01_evidence_index.md#e457)、[E469](01_evidence_index.md#e469)；源文L31126—31166；[E536](01_evidence_index.md#e536)—[E545](01_evidence_index.md#e545)

**证据等级：** A（文件文本形态）；成因F

**更准确的理解：** source仍是唯一最高来源；缺口应如实标记，不能引入网络版本私自补成Canon。 中段未完句与王滕飞/王腾飞变体须在引用时保留；不自动据字形生成两个总经理。 人物字形与排版残句不自动代表新设定，时间冲突独立登记。作者附记L10331谈目录重置属于发布说明，不能据此断言本地输入缺文的原因。 138章说未等翠回来魔装就用于战场，但127—129已写其作为林昀归家，而白也早与他相见；这里可能按魔法身份分别理解，也可能是叙述时序松动，原因未知，不私改。卷末作者讲砍推理暗线属于创作说明，不证明本地缺字成因，更不能恢复已废弃的红叛徒草案。 续审06：17明写月圆节后三周，20同次战后数小时却在回忆摩丝话时称半个月以后；可能约数/叙述松动，成因未明。无需反向据卡11月20—22修正原文，也不把第17章无副题自动认作缺章。 续审07：L15205附近夏凉重复、L16068附近尴尬重复以及L16280亿海百记字形需保留源文引用。结合31正式忆海百记及连续同一战斗，不据单次异写发明另一个繁开；具体排印或抓取成因仍未知，不改source。 续审08：L17724弃车而亡与正在逃跑语境不合，列疑似用字问题而不记路人死亡；L17985麻生原香与连续麻生圆香语境相接，不据单次异写另造角色。成因仍未知且source不改；体高与身长数值是不同维度，不误报残兽尺寸冲突。 续审09：50末今年考核、51开头明年；51离演出一小时、53入住走廊有斜阳；62同章两天调整与夜访近一周、好几天等时间词保留。它们可能含约数/省略或字误，成因未定，不据卡日期替换。L19316时间时间、L19685谢谢你的安心亦仅记录字形疑点，不改原著或造新设定。 续审11：76 L21353报心解百武成势，78 L21541解释原繁开百武乘势、新心解百势成武；因此撤回阅读76时的临时卡名错误候选，未分配C号，保留源文自身用名不一。78另现赤鸢，85只有章号无副题，89 L22793及L22822有残句，均不擅自补字。79除翠无人见白兽形与88夏认为翠等并不意外属于叙述和人物观感不同层，不直接判源矛盾。 续审12：91新年第4天、92同日上午、93称午餐后却明确一月五日，保留日历转场张力，不以卡日期强行调和。100公共妈妈与95私下约定记实际例外，尚不足判源必然自相矛盾。幕间鸢眼罩原因未叙，亦不擅补银屏山某一招致伤。 续审13：103申请的接过、109科普魔术使/魔法使混称、110消洱等字面疑点不改原著。111墨荷说队长没有留长发，与假衣装挽髻可并存为视觉表述，不推新剪发。114战争影响说辞明确是为解围所构且未必符合，不当医学诊断。 续审14：129白称昨天与店员商量、131翠称前天同来，与明确2/14当前及先前13日商店/同来语境有张力；不改原文或替角色自动记成真时间。126白包装先干花后假花亦仅保原字面；谢礼巧克力历史起源为翠转旧队友说法。 续审15：145墨口述其他队员以及妮娜夸队长处疑妮姆字误，保原不默改；154今天资格考核与当前离开考还有时段有词误疑点，不据今天把开考前移；162叙称顶头上司蓝杖是下属预认不证任命完成。 续审16：164段有跟腿，。一类排印，170小的发言舞台用他，189土身份说明以逗号收尾；只保上游字面，不编失去内容。31126—31166作者规划/废弃草案已完整阅读但非已成正文事实，尤其鸢原定聚餐、未来卷期和考核路线不作NPC知识。 续审20：本段L35348褐鹈说女王老太婆后缺尾、L35407第一实不一般衔接异常、L35484及L36052半句截断继续保留，不补写或扩大为整章未读；原著覆盖100只指所给文件全部文本，不保证上游版本无漏字。

**可能造成的 RP 后果：** 把缺字当设定、凭残句补全敌方计划，或误删表现能力效果的特殊字符。

**建议处理：** 进一步考据并在证据引用处注明缺口；本阶段不修原著文件。

## [S019] 开局标记替换引用不存在的捕获组

**严重程度：** POTENTIAL RISK

**问题类型：** 技术／开局提示

**角色卡位置：** 技术／源文位置见下方定位；[技术目录](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/technical>)

**当前内容概述：** 正则0查找<开局>，替换串为$1，查找式没有捕获组。

**发现的问题：** 标准JavaScript String.replace结果为字面量$1，并非清空开局标记。宿主如果直接采用该语义，就会把$1留在生成提示。

**原著证据 / 定位：** data.extensions.regex_scripts[0]；technical/static_verification.json

**证据等级：** 标准JavaScript静态验证；真实宿主未测试

**更准确的理解：** 其他已测变量与正文正则可以匹配，本项不能扩大成所有正则损坏。是否存在宿主额外处理需导入测试。

**可能造成的 RP 后果：** 备用开局标记未按脚本名所述清除，模型收到无意义占位文本。

**建议处理：** 后续核对替换意图并测试真实导入；本阶段不改配置。

## 开放式复查记录与撤销候选

本轮另从“长期保存后会发生什么”和“手机到底是显示还是另一条生成链路”出发复查，发现S012–S016、R005等问题。检查了隐藏资料副本、知识泄漏的语义而非姓名、默认值与未知状态的混淆。该复查不取代全文阅读结束后应做的最终开放式复查。

复核撤销：schema确实有10个顶层容器，先前11个的计数为审计工作笔记错误，未列为正式问题；JSON中的反斜杠表现不是正则双重转义损坏。ID缺号、两块PNG元数据重复、扩展position差别、所有递归阻断字段本身均不构成已证实缺陷。

未证实“所有剧情都被强制执行”：ID179明确允许玩家改变命运。其实际落实仍受S001、S005、S012影响；应测试IF分歧后旧原作状态会否覆盖新状态，不能仅凭剧情摘要存在就判强制命运。

## [C021] 剧情索引与正文的章节边界错位

**严重程度：** MODERATE

**问题类型：** 章节边界／时间定位

**角色卡位置：** [ID 91｜剧情·卷1幕02·新队与下水道之歌](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_091.txt>)；[ID 95｜剧情·卷1幕06·暑假与秘密基地](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_095.txt>)；[ID 96｜剧情·卷1幕07·柏安市巡查](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_096.txt>)；[ID 97｜剧情·卷1幕08·月圆节之变](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_097.txt>)；[ID 110｜剧情·卷2幕13·云境夺牌战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_110.txt>)；[ID 111｜剧情·卷2幕14·回忆·1979卢恩诺雷守卫战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_111.txt>)；[ID 178｜剧情索引](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_178.txt>)；[ID 98｜剧情·卷2幕01·新局长与兽子](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_098.txt>)；[ID 99｜剧情·卷2幕02·鸢来袭](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_099.txt>)；[ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)；[ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)；[ID 122｜翡翠书廊](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_122.txt>)；[ID 106｜剧情·卷2幕09·旧梦与岔路](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_106.txt>)；[ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)；[ID 108｜剧情·卷2幕11·花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_108.txt>)；[ID 29｜鸽血红](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_029.txt>)；[ID 66｜女王](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_066.txt>)；[ID 72｜山丹](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_072.txt>)；[ID 88｜紫钻](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_088.txt>)；[ID 109｜剧情·卷2幕12·魔装考核](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_109.txt>)；[ID 148｜云境考场](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_148.txt>)

**当前内容概述：** ID178把卷二262划入当代幕；ID91把本相课程标第27章、下水道主战标第28章。

**发现的问题：** 源文卷二262开头即标1979夏末；索引开始边界晚一章。270回当代、280—281再回历史，不能用单一章节连续段表示全部历史揭晓。 卷一第26章才是本相课程，第27章已进入下水道，第28章对抗蛹壳、第29章杰作与祭坛；ID91另编第26章日常桥段、把课程推到27，导致具体查证位置错位。 第06幕还把魔法少女日和旧队咖啡私谈并入第101—104章，实际为第106—109章；耳钉也从第110章生日夜前置进105—108章。 ID96把第114章验牌前置到112、把118灯盏口述的统计与仪式前置给113—114三新人，且把实际抵达翌日完成的巢穴行动延展成数日。第123章仅送别、收节日询问，实际返程和归家在127—129；ID97前两事件又把124—126提前写成林昀已归家。

**原著证据 / 定位：** [E042](01_evidence_index.md#e042)、[E011](01_evidence_index.md#e011)、[E030](01_evidence_index.md#e030)、[E033](01_evidence_index.md#e033)、[E040](01_evidence_index.md#e040)；[E054](01_evidence_index.md#e054)、[E055](01_evidence_index.md#e055)、[E056](01_evidence_index.md#e056)；chapter_index.json卷一26—29标题及行界；[E120](01_evidence_index.md#e120)—[E123](01_evidence_index.md#e123)；L8132、8325、8439、8624 [E124](01_evidence_index.md#e124)—[E145](01_evidence_index.md#e145)；L9811、9903、9956、10285、10342；卡96、97。；[E153](01_evidence_index.md#e153)—[E181](01_evidence_index.md#e181)；chapter_index.json卷一133至卷末；[E192](01_evidence_index.md#e192)—[E195](01_evidence_index.md#e195)、[E208](01_evidence_index.md#e208)—[E212](01_evidence_index.md#e212)；[E213](01_evidence_index.md#e213)—[E240](01_evidence_index.md#e240)；[E250](01_evidence_index.md#e250)—[E261](01_evidence_index.md#e261)；[E263](01_evidence_index.md#e263)—[E287](01_evidence_index.md#e287)；[E288](01_evidence_index.md#e288)—[E314](01_evidence_index.md#e314)；[E315](01_evidence_index.md#e315)—[E347](01_evidence_index.md#e347)；[E350](01_evidence_index.md#e350)、[E351](01_evidence_index.md#e351)、[E355](01_evidence_index.md#e355)、[E357](01_evidence_index.md#e357)、[E358](01_evidence_index.md#e358)、[E360](01_evidence_index.md#e360)、[E362](01_evidence_index.md#e362)、[E365](01_evidence_index.md#e365)—[E370](01_evidence_index.md#e370)、[E372](01_evidence_index.md#e372)、[E375](01_evidence_index.md#e375)；[E376](01_evidence_index.md#e376)、[E378](01_evidence_index.md#e378)、[E379](01_evidence_index.md#e379)、[E382](01_evidence_index.md#e382)、[E387](01_evidence_index.md#e387)—[E394](01_evidence_index.md#e394)、[E400](01_evidence_index.md#e400)—[E402](01_evidence_index.md#e402)；[E403](01_evidence_index.md#e403)、[E407](01_evidence_index.md#e407)、[E410](01_evidence_index.md#e410)、[E417](01_evidence_index.md#e417)、[E419](01_evidence_index.md#e419)、[E423](01_evidence_index.md#e423)；[E430](01_evidence_index.md#e430)—[E450](01_evidence_index.md#e450)；[E453](01_evidence_index.md#e453)—[E469](01_evidence_index.md#e469)；[E470](01_evidence_index.md#e470)—[E492](01_evidence_index.md#e492)；[E493](01_evidence_index.md#e493)—[E515](01_evidence_index.md#e515)；[E518](01_evidence_index.md#e518)—[E535](01_evidence_index.md#e535)；[E537](01_evidence_index.md#e537)—[E545](01_evidence_index.md#e545)

**证据等级：** A

**更准确的理解：** 分开实际事件时间、叙述所在章节和RP当前时间；一个章节归档错误不能让世界时钟直接回到1979。 卡97把133—136红旧事标132—134，把实际137妮妮段标135—136；142只到唤织命，城堡、概念裁切、剪碎与杀蛾在独立卷一终章L12364—12696。间奏二L12780—12883只到局长邀请，未到就任。作者附言也有独立标题，不能挤入142并驱动世界时间。 续审06：卡98事件八将第9章局长室叫爸爸与险些坦白混放到10—11章基地讨论之后；实际白先说漏嘴，次日晚才在基地转述。第12章是再翌日上午，不是下午。体检、车中确认母亲均在第20章同日，第21章已转校园，第22章是游戏历史与试玩；其事件十三标20—22并非整体范围错误，但摘要不得把已发生场景误排成另两日。第17章源标题无副题，保留原样。 续审07：卡99第24章家庭谈话接23同夜，不是新增一日；林接被捕报告在26章正午，27招待非上午；红破窗救援在29章末，30独战后31才繁开、后段才交复制剪。34新成员实际只有朝颜。37—38跟踪与39午餐并行，40为同日下班，不能被卡100拆成12月6、7、8日三天。章节错位与具体伪造内容分别见C074—C081。 续审08：43先写第三次约斗再回同日下午校园，44放学独巡、45同日晚归；翠先同意周六代巡后听歌手名字，46回述闻名后买票并提前巡逻带三后辈。47走廊只有熟悉感，48散场介绍后小璐才喊黏液洗澡，不是刚刚那场战斗。作者停更附言不能增加剧情两个月。 续审09：49报号在互认合作后，50小璐问为何知道名字而非先问父亲；51驾车者仍翠，到52墓园才男身。53球赛发起，55回述败因；54白蓟向翠道歉，55小先房内后受邀阳台，56阳台末只提学两手、57车中说已接受。58秘书已任数日；60才向玛披露计划、61才提留一年，62晚取消禁考后夜访夏。63以后未读。 续审10：63仅先教屏障，65回忆补同次夜课爆炸、当下构想成形；66才实际发射/防御/认输并开始小白对球、解释浊化，67白蓟旧史与二次浊化、68判胜和解及总分。卡101将全课定位63、整局结果放65，具体应拆事件发生时间与叙述位置；66桥外承诺另见C098。70/71家中谈话在跨年前，72/73才跨年夜局长室，73真来意未说完。 续审11：74仅午夜炸山及林推防护网，76才追加两小时与吸兽波；75未叙小通知两队，89回述只证带夏白来。77获救后寻三年、师父死才求契约，不是当场随后受测；78贯胸，79解释伤源险。81六人共同突围，82两人查塔四人追敌；84半杯、88才心解尽。85初析王钥、86解释护卫，不能整体始于86。卡102的干部死伤过半亦与78十去五不等。跨卷假回溯单列C108，终局提前见C107。 续审12：91当下为新年第4天，认母答复回叙89夜；92并无木父故事，实际100才向翠讲。93课堂真坦白祭子另C110，94安排白训练、95才叙红教学；96末只问木目的，97才回叙门答案。97登塔→98当日下午衣装→99同日夜课不可拆成1月15/20/28三日。庙会只锚一月末，幕间只以上月任务失败作相对关系，不擅造日号。 续审13：104把104—106到站/入境/住宿写2月11，实际101于10日出发、102次晨11日燕南、104又次日12日下午抵海站；107—108翌日疗伤为13日，与109另一边同日而非12日治疗后隔天。卡105把采购/制礼并在13夜需分113当天14日与13日回叙；14日下午买两套一套已穿，非仅一套。103摩可拒随行、104多份掩护文件不前置成101已给全后辈解释。 续审14：105事件三114段纳入115采购；餐厅到流放谈话为115—119，考核具体警告134才得，121返程尚未得警告。129对白昨天商店与131翠前天同来，和113当前/回叙及12入国存在相对日措辞张力，按明确14庆生日记录并挂R005，不自改源。 续审15：106复诊/问郁被定2月15—16，但146明确治疗一周后，同日晚宴；15日仅回忆发现墨退房。107把158返屋定21日、159—161定22日，正文都承同一晚归程，不能为章节切换加日。162只说准备多日、已在卢好几日，24日尚无本章直接日期依据。106尺约束四成在142非141、114三形处决在144；107箱女谣言162尚没发生。 续审16：167才回叙箱子被拿错、被分院员工拖回家、临编折女儿、魔镜联折领回和数日后传谣；107把162撞箱直接生成流言错因果。165/166是考前夜，167/168又考首日并回述半月，不按章逐日累加。四科两天、次日休息补考当日晚放榜、再翌日实战七天，1073/6放榜又3/6—8多天组队和1083/9实战的排序与原文连续日程不合。177邀队→178登记同早，183才规则、188广播首谜、189观众复盘，不能187全局早知。108cos名来源189观礼者传播并非183组队考生先叫。 续审17：190夏到场时马战仍进行、192才闻好味；194才落实集爆，196破冰主体277非629；199山首提传墙、206扩用，208才箭三分钟杀蛹非205即结果。211宣布582首出、213确认综合第一，214才277探索第一/本场综合第三、215庆功距约十小时且给一天休息。卡108/109不能把全部凑同一3/9傍晚或第三名当全程最终。 续审18：216续同餐→217明确一夜后中午休息日→220再短暂一天休后第二场；109把215与217都放同3/10且此前213定3/9傍晚不能随意凑。219未列名、220才四名及下一晨私疑；222薄先攀花而非花主动首招；224判偏移→225报告→226原S+检测→227截流→228末突报→229回叙紫违规→231同场40分钟→232当晚榜SS→233传令回叙；234才次日对战，非230—238同一第三日。239再休一天后3天2夜第三项。 续审19：242已翌日云境并回叙昨紫/旅馆，243风镜只计划、248才实作与第一夜统计；245吸魔发现→246术链→247第一夜解释，249第二午路队传闻、250回几小时前相遇、251数小时后翠追上、252私谈、253别队掌书。254找箭/误羊回叙并非250找人线；258已第三日最后半天且只追击开端，259翠未援，110提前具体强风陷阱尚无此证。 续审20：261才写258追逐后强风陷阱与582第一/277第三/629第五，262切史不是263；263爆炸打断墨谢调妹非矢宣言，265捷报在夜后天明上午非天亮前，266羽在界门撞碎而非仅濒失，267才蜂报号/祖分空间。111黑空间坠羽混268黑框返战。267石人走才唱，268撤军自己亲获昙开时间，不是援军会师后还全不知是否争时。所有10月2/3推算仍需服281立秋明示，未强排日历。

**可能造成的 RP 后果：** 按索引查证漏掉回忆首章，剧情幕选择错位，并把记忆发生年代写成当前场景。

**建议处理：** 后续修正章节映射；保持原著原始标题和带卷行号，精确月日另行裁决。

## [C022] 溶腔型一次死亡爆散被泛化为残兽常态

**严重程度：** MODERATE

**问题类型：** 能力机制／过度概括

**角色卡位置：** [ID 27](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_027.txt>)；[ID 91](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_091.txt>)

**当前内容概述：** ID27称残兽击败后常爆炸释放无杀伤力恶臭黏液；ID91先把喷口写作配合目标、后又称意外命中。

**发现的问题：** 第19章的爆散明确来自这只溶腔型的溶腔受损与体液压力失控，不是所有残兽的常见死后机制。原作两人计划打嘴，细小喷口并非通常可瞄准的弱点，命中它是意外。

**原著证据 / 定位：** [E047](01_evidence_index.md#e047)；L1493–1498、1515–1525、1534–1543

**证据等级：** A（类型、动作、因果）

**更准确的理解：** 只对该类型、该死亡条件记录爆散与失压黏液；计划目标和实际落点分别记录。ID91已提意外，不把整个结果全判错。

**可能造成的 RP 后果：** 普通残兽战会反复套恶臭爆炸，狭小喷口变成可靠万能弱点。

**建议处理：** 后续拆分物种说明与单场战斗结果，保留配合中仍有运气成分。


## [C023] 只有魔法少女攻击才能消灭残兽的排他断言缺少边界

**严重程度：** POTENTIAL RISK

**问题类型：** 世界规则／武力边界

**角色卡位置：** [ID 27｜起源与出现](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_027.txt>)

**当前内容概述：** 物理热武器难以奏效之后，直接断言只有魔法少女的魔力攻击能真正消灭残兽。

**发现的问题：** 第35章摩丝明确说局方数人或十数人搭配装备能勉强解决卵阶。虽是当事官员陈述而非本轮目击实战，却与卡的绝对排他结论形成待核张力；常规武器无效不推出魔术使及其专用装备永远无效。 续审06：林明说专用魔武使单人掌控者伤卵阶，资格审核后配发；第三队报抓两兽化者，随后三名装备者配合白的天音才抵蠖，一蛹四蠖仍迅速击溃队伍。异策局不能作战的无条件解释已不成立，但抓捕与抵挡不等于彻底击杀天然残兽，武装的魔力来源也不能凭这些段落穷尽。

**原著证据 / 定位：** [E060](01_evidence_index.md#e060)；L2493–2497；[E185](01_evidence_index.md#e185)、[E201](01_evidence_index.md#e201)、[E204](01_evidence_index.md#e204)；[E287](01_evidence_index.md#e287)

**证据等级：** A（武装配发与协作实战）／D（性能说明、抓捕报告、旧摩丝陈述）；绝对排他击杀边界仍待证

**更准确的理解：** 区分普通热武器、专用装备、魔术使和魔法少女，按阶位与条件查证。不能将局长每项自述无条件视为真。 当前可确认有装备、阶位、合力与少女辅助的分层边界；新武装战例不自动证明所有普通武器有效，也不据此反推卷一所有旧装备相同。 续审09：62后勤损耗报告需局长核实后向调查院申请维修补足，叙述再述魔术使单兵面对卵阶的能力；装备成本、维护链与战果级别不能省略。并非由此证实所有普通人/武器无条件彻杀全部残兽，保留潜在风险等级。

**可能造成的 RP 后果：** 异策局的作战能力被压成零，普通人协同或装备路线被错误封死。

**建议处理：** 继续沿正文寻找实际战例；现阶段保留潜在风险，不作反向无条件结论。 风险保留且旁证增强；继续查实际击杀及能源机制，不能把伤害、抓捕、击杀混为一件事。

## [C024] 没有目击记录被改写成两年没有实际袭击

**严重程度：** MODERATE

**问题类型：** 事实范围／调查推理

**角色卡位置：** [ID 91](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_091.txt>)

**当前内容概述：** ID91事件一称方亭市两年残兽袭击并非稀少而是完全为零。

**发现的问题：** 第16章为档案记载的目击为零，调查正围绕为什么如此展开。后文发现实际存在巢穴，不能把资料空白变成无事发生的客观历史。

**原著证据 / 定位：** [E043](01_evidence_index.md#e043)、[E055](01_evidence_index.md#e055)、[E056](01_evidence_index.md#e056)；L1292–1295、2044–2046

**证据等级：** A（记录与实探）；未记载期间具体活动F

**更准确的理解：** 在记录层写零；在事件层保留未记录、潜藏或被隐瞒的开放可能。

**可能造成的 RP 后果：** 调查假说被提前取消，后来证实的隐蔽活动显得凭空反转。

**建议处理：** 后续保留证据的限定语，事件与记录分开。


## [C025] 荼蘼葬礼回忆中的消息归属、死亡地点与知情状态被混写

**严重程度：** MAJOR

**问题类型：** 身份／信息传播／地点

**角色卡位置：** [ID 91](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_091.txt>)；[ID 95](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_095.txt>)

**当前内容概述：** ID91事件六称转交金绿猫眼警告、荼蘼被旧代号拒认、后来林昀得知她在海城战死。

**发现的问题：** 警告经自称金绿猫眼属官的人转交，其真实发信权威不能压成金绿猫眼直接传令。是林昀不愿再被称矢车菊并纠正称呼，不是拒认荼蘼。正文写她葬礼一年后在滨海市为保护情报牺牲，明确林昀尚不知情；本章没有后来已得知的事件。 第92章已明确实际获知节点；ID95称荼蘼为林昀的前辈也与第93章后辈名分相反。

**原著证据 / 定位：** [E053](01_evidence_index.md#e053)；L1920–1926、1948–1959；[E092](01_evidence_index.md#e092)、[E104](01_evidence_index.md#e104)；L5564、6720–6723、6735–6737

**证据等级：** A（死亡、关系及第92章通话获知）／D（早期警告转述与调查院消息归属）

**更准确的理解：** 保留实际传话链；死亡发生、读者获知、林昀何时获知是三层。海城不能当滨海市的已证别名。 本轮补确：林昀第92章在红思与离场的私谈中从金绿猫眼获悉荼蘼死讯；她是安雅队友而林昀名分上的后辈，未曾与他共同作战。第77章林昀内心接受警告来自金绿猫眼，故不宜再把该归属称完全无支持；实际发信路径仍按旧链保留。

**可能造成的 RP 后果：** NPC提前哀悼、找错地点或把间接警告当官方命令，并误演旧友不相认。

**建议处理：** 后续纠正地名、称谓及获知节点；保留早期消息转述链与后续得到确认的层级，不让第25章林昀提前知情。

## [C026] 小璐被提前赋予夏凉家事与母亲魔法身份

**严重程度：** MAJOR

**问题类型：** 认知状态／秘密时点

**角色卡位置：** [ID 92](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_092.txt>)；[ID 93](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_093.txt>)

**当前内容概述：** ID92事件八说小璐不愿夏凉借身世抢前辈；ID93事件三说小璐只知道翠雀是母亲旧队友、父亲旧识。

**发现的问题：** 第44章夏凉明确不愿告知小璐家事，翠雀尊重。第51章两新人只是听制度；第52—53章小璐才撞见父亲与红熟识并猜是否认识翠雀；直到第60章旧照才辨认母亲与翠雀。卡把不同阶段推断与秘密提前写成所知。

**原著证据 / 定位：** [E067](01_evidence_index.md#e067)、[E072](01_evidence_index.md#e072)、[E073](01_evidence_index.md#e073)、[E078](01_evidence_index.md#e078)、[E079](01_evidence_index.md#e079)；L3224–3232、3795–3826、4272–4273、4353–4356

**证据等级：** A（对话、内心、获知事件）

**更准确的理解：** 此阶段小璐不知道夏凉具体家庭遭遇；对父亲与翠雀关系是猜测。第59章手机事件夏凉也答应不转述给她。照片只给本次已见信息，后续第61章解释尚待读。

**可能造成的 RP 后果：** 人物会无来源谈家暴或母亲旧身份，后续倾诉与坦白失去作用。

**建议处理：** 后续按每个人与每项秘密保存状态及传播来源；不替人物决定公开家事。


## [C027] 剧情补写让不在场人物旁听并制造红思与约会演出

**严重程度：** MAJOR

**问题类型：** 事件主体／IF边界

**角色卡位置：** [ID 92](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_092.txt>)；[ID 93](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_093.txt>)

**当前内容概述：** ID92事件十林昀在门铃前收电脑、维持家长姿态；ID93写林昀在旁听红科普，又写红发现尾随故意演暧昧。

**发现的问题：** 第47—51章家中是两新人、摩可和来访红思与；林昀在第52章下班才于楼下遇红。第54—56章他独自为亡妻选礼、被两女孩与摩可跟踪，靠定位术式反跟发现她们，红没有到商场配合演约会。卡新增的在场者与动机改写了误会因果。

**原著证据 / 定位：** [E070](01_evidence_index.md#e070)、[E071](01_evidence_index.md#e071)、[E072](01_evidence_index.md#e072)、[E073](01_evidence_index.md#e073)、[E074](01_evidence_index.md#e074)、[E075](01_evidence_index.md#e075)；L3720–3763、3857–3881、3953–3966、4014–4027

**证据等级：** A（连续完整场景）；新增演出出处F

**更准确的理解：** 人物不在场不能凭旁白主题获得一手对白；跟踪是女儿对真实迹象的误解，不能写成红主动诱导的既成事件。

**可能造成的 RP 后果：** 林昀变成同时在公司与家中；红被赋予操弄家庭关系的行为，小璐的推理起因改变。

**建议处理：** USER_CONFIRMATION_REQUIRED：新增桥段若为有意IF需独立标明；原著线先记录可证过程，本阶段不改卡。


## [C028] 扣除翠雀后仍把队伍写成三名新人

**严重程度：** MODERATE

**问题类型：** 人数／队伍状态

**角色卡位置：** [ID 92](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_092.txt>)

**当前内容概述：** ID92事件三说林昀要求不计自己，宁愿让人以为方亭市有三个新人。

**发现的问题：** 第33章红思与说三个人是在把翠雀算入；林昀纠正别算我。此时只有白玫与小锦两新人，第57章更明说全市三名魔法少女围坐餐桌，包括林昀。

**原著证据 / 定位：** [E059](01_evidence_index.md#e059)、[E076](01_evidence_index.md#e076)；L2405–2407、4105

**证据等级：** A

**更准确的理解：** 本阶段总数三，除翠雀外新人二；尚未招募的第三新人不能自动生成。

**可能造成的 RP 后果：** 队伍人数、训练和后续招募需求错位。

**建议处理：** 后续按阶段纠正人数，并分实有队员与对外登记。


## [C029] 商场纪念日解释、手机响铃与战斗顺序被倒置

**严重程度：** MAJOR

**问题类型：** 时间线／事件因果

**角色卡位置：** [ID 93](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_093.txt>)

**当前内容概述：** ID93事件五写战后才承认纪念日；事件六写两新人杀兽后林昀在停车场因手机铃声露馅。

**发现的问题：** 第56章逛店前已说明十五周年；第58章餐厅坦白身份后，夏凉尚未出战便拨打翠雀；第59章在餐厅通过挂断核验。第60章才是两新人作战、翠雀暗看并回停车场变回本体。把手机放战后会改变为何他不能公开露面和红思与转告的原因。

**原著证据 / 定位：** [E075](01_evidence_index.md#e075)、[E077](01_evidence_index.md#e077)、[E078](01_evidence_index.md#e078)、[E079](01_evidence_index.md#e079)；L4017–4022、4193–4203、4230–4234、4286–4291

**证据等级：** A

**更准确的理解：** 纪念日澄清→共同购物午餐→疏散通知→两人坦白→手机试探→夏凉出战→暗中观战→停车场会合→回程照片。

**可能造成的 RP 后果：** NPC提前或延后掌握手机信息，战斗与伪装选择失去原因，同一幕地点切换错误。

**建议处理：** 后续按已读连续序列重校；不能用戏剧合理性代替源文。


## [C030] 纪念日项链材质被写成紫晶

**严重程度：** MINOR

**问题类型：** 物件／外观

**角色卡位置：** [ID 93](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_093.txt>)

**当前内容概述：** ID93事件五把纪念日礼物写成樱花形紫晶项链。

**发现的问题：** 第57章明确银链、芙蓉石即粉水晶的樱花形吊坠及金边，不是紫晶。

**原著证据 / 定位：** [E076](01_evidence_index.md#e076)；L4084–4088

**证据等级：** A

**更准确的理解：** 以明确物件说明为准；林昀最终选择理由是樱花意象。

**可能造成的 RP 后果：** 礼物颜色材质与后续回忆、展示不一致。

**建议处理：** 后续纠正材质，保留纪念意义。


## [C031] 下水道的敌方音波与己方构装声响被合成翠雀音爆攻击

**严重程度：** MODERATE

**问题类型：** 能力归属／表现解释

**角色卡位置：** [ID 91](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_091.txt>)

**当前内容概述：** ID91事件九称翠雀以丝线织成刀刃、护壁和音爆打破蛹壳。

**发现的问题：** 正文中音波攻击来自鱼形残兽，被丝线立方体挡下；丝线震鸣、蜂鸣是编织旋转的声音，最终斩杀靠镂空刀刃。该段没有把音爆列为翠雀的攻击手段。

**原著证据 / 定位：** [E056](01_evidence_index.md#e056)；L2147–2163；[E094](01_evidence_index.md#e094)、[E096](01_evidence_index.md#e096)；L5762、5960–5965

**证据等级：** A（本场动作与叙述）；独立音爆能力依据F

**更准确的理解：** 声音描写、对手技能与自身构装能力分开；不由战斗拟乐描写生成新技能。 第79章塞斯特斯拳击伴巨大音爆声是确有描写，故不能扩大成翠雀攻击从不发音爆；但这仍不支持第27—29章存在独立音爆破蛹技能。第82章回指下水道末击为同一格拉迪乌斯剑刃。

**可能造成的 RP 后果：** 翠雀无来源获得声波伤害手段，能力限制和对应战术被改变。

**建议处理：** 后续按本场实际动作修正；若额外技能为有意改编，纳入USER_CONFIRMATION_REQUIRED。

## 本轮连续阅读复核（续审02）

从原断点L1286逐行连续读至L4357（卷一16—60章），没有用关键词扫描替代正文。新增E043—E079、C022—C031；C005、C006、C019、C020、C021、S003、S010、S011保持原编号并修订。判断前后和理由见[judgment_changes.json](judgment_changes.json)。

C020中联系方式与同地授课已经后文回补，不再列作无依据补写；具体书面撤退规约仍待证。C019排他回响制度仍未确认，未因分配意图就宣布反证成功。本轮仅扩大已读范围的开放审查；最终全局开放式复查尚未进行。

## [C032] 夜谈摘要混入夏凉后期情绪与尚未发生的引离实战

**严重程度：** MAJOR

**问题类型：** 关系／成长时序

**角色卡位置：** [ID 93](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_093.txt>)

**当前内容概述：** 事件八写引离首次战场引兽，随后三次夜谈、夏凉害怕林昀偏爱女儿并说嫉妒。

**发现的问题：** 第62—63章是突破与测试，第64—66章沿途连续夜谈主体为小璐与翠雀；没有夏凉与林昀讨论父女偏爱或引离在此出战。夏凉第98章才确认父亲与前辈同一，不能提前套入其后亲情要求。

**原著证据 / 定位：** [E082](01_evidence_index.md#e082)—[E084](01_evidence_index.md#e084)、[E106](01_evidence_index.md#e106)、[E109](01_evidence_index.md#e109)、[E110](01_evidence_index.md#e110)；L4451、4542、4719–4759、7190–7228

**证据等级：** A（原场景与顺序）；新增桥段Canon依据F

**更准确的理解：** 区分一夜的情绪推进、后来的争宠与身份揭露；小璐并非要求立即复仇或退出。

**可能造成的 RP 后果：** 把不同角色的困惑和成长糅合，早期夏凉按未来秘密行动。

**建议处理：** USER_CONFIRMATION_REQUIRED：新增对白与战斗若有意IF应独立标识；原著基线按实际顺序记录。


## [C033] 屏障幕末新增摩可因怕丢脸而不报险的决定

**严重程度：** MAJOR

**问题类型：** 心理／信息传播

**角色卡位置：** [ID 93](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_093.txt>)

**当前内容概述：** 事件十补充摩可绕行试墙、判断更稳定、因招募夸口羞耻最终不报告。

**发现的问题：** 第68章结尾只有撞墙、触摸确认及完蛋了；此前私藏新人动机有依据，不能借此拼出发现屏障后的另一项决定。第72章其回院搜寻及受魔力干扰须据实际过程记录。

**原著证据 / 定位：** [E086](01_evidence_index.md#e086)、[E089](01_evidence_index.md#e089)；L4858–4875、5104–5106

**证据等级：** A（原动作）；追加判断及不报险动机F

**更准确的理解：** 可确认私藏招募，不能确认羞耻是危机通信受阻的原因。

**可能造成的 RP 后果：** 把摩可写成故意隐瞒可报告的生命危险，改变责任与救援因果。

**建议处理：** USER_CONFIRMATION_REQUIRED：疑似原创心理及动作另列，不能作为Canon内心。


## [C034] 薄雪变身、援军到达和兽之腑变身顺序被重排

**严重程度：** MAJOR

**问题类型：** 事件因果／首次能力

**角色卡位置：** [ID 94](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_094.txt>)

**当前内容概述：** 事件四先白玫小锦拖住敌人再薄雪变身；事件五第75章兵触三已化兽。

**发现的问题：** 薄雪第72—74章先变身回救田胜、打晕普通黑袍，第75章才遇兵触三并获两新人救援；第76章先倒叙两人到来，随后兵触三才用兽之腑。关于祭子病因的对话也在第75章，不能提前作她决定变身的已知事实。

**原著证据 / 定位：** [E089](01_evidence_index.md#e089)—[E091](01_evidence_index.md#e091)；L5140、5215、5225、5300–5308、5379、5544–5551

**证据等级：** A（实际顺序）／D（祭子说法）

**更准确的理解：** 她先因田胜救命和樱的回忆选择力量，并独立回救；两位队友后来介入。

**可能造成的 RP 后果：** 削弱白静萱的主动选择，NPC提前知祭子、把倒叙当新一轮行动。

**建议处理：** 后续依事件实际时间整理，同章倒叙要另标；本阶段不改卡。


## [C035] 给早期薄雪添加治愈消耗本相与牺牲式前排战术

**严重程度：** MAJOR

**问题类型：** 能力代价／行动主体

**角色卡位置：** [ID 17｜白静萱](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_017.txt>)；[ID 94｜剧情·卷1幕05·黑烬黎明事变](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_094.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)

**当前内容概述：** 第05幕事件七写薄雪主动吃爪击，每次治愈消耗本相，反复贴兽躯；末段白静萱接受薄雪治疗。

**发现的问题：** 原战薄雪初次输出尚不熟练，回救田胜后供魔力拆屏障；后续在地面治疗夏凉。以伤换伤风险到第94章训练才具体出现，且是冷静错误判断。没有本相按次消耗规则；白静萱与薄雪是同一人，不能成为彼此治疗的两个主体。

**原著证据 / 定位：** [E089](01_evidence_index.md#e089)—[E091](01_evidence_index.md#e091)、[E098](01_evidence_index.md#e098)、[E099](01_evidence_index.md#e099)、[E105](01_evidence_index.md#e105)、[E112](01_evidence_index.md#e112)；L5225、5271、6109、6329、6798–6815；[E326](01_evidence_index.md#e326)、[E341](01_evidence_index.md#e341)；[E354](01_evidence_index.md#e354)、[E355](01_evidence_index.md#e355)

**证据等级：** A（行动及后续测试）；添加消耗机制F

**更准确的理解：** 治愈性质可养护本相，但当前对翠雀旧伤无可感效果。田胜的被动受益不等于已掌握全套治疗术，情绪风险和资源代价也应分开。 续审11：79和87的白已主动释放兽形，出现救红、以腹承爪换攻眼及魔装支持持续战；这是后期真实战风，不再笼统否认全部搏命表现。但不能前置到卷一最初参战，更未证按治疗次数扣本相。小87才追问是否敌施手脚，白只给与此事无关的有限答复。 续审12：93揭天音四韵律及副作用（M038），翠拆盒/底托是避免整个魔装变纯锤并保留近战意愿，不能只解释为阻自残。白记得湖畔战但失真、翠修饰口径，不把主观救人故事替客观残虐。

**可能造成的 RP 后果：** 凭空削减生命核心、给新人后期战风，并生成身份分裂的重复角色。

**建议处理：** USER_CONFIRMATION_REQUIRED：新增代价和战术如为改编须标IF；Canon记录删去无依据推导。

## [C036] 兵触三最终被翠雀截杀，被误写成麻雀灭口

**严重程度：** MAJOR

**问题类型：** 关键事件／敌方合作因果

**角色卡位置：** [ID 94｜剧情·卷1幕05·黑烬黎明事变](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_094.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)

**当前内容概述：** 事件八称麻雀半空腰斩兵触三，阻断情报并掩盖爪痕黑烬交易。

**发现的问题：** 第85章翠雀赶往救援时直接贯穿逃跑兵触三；麻雀此前已被她击败禁魔。杀人主体与动机均被颠倒。

**原著证据 / 定位：** [E096](01_evidence_index.md#e096)、[E098](01_evidence_index.md#e098)、[E099](01_evidence_index.md#e099)；L5980–6001、6293–6318、6384；[E336](01_evidence_index.md#e336)、[E337](01_evidence_index.md#e337)

**证据等级：** A

**更准确的理解：** 兵触三拟向蛾报告双祭子，尚未完成；其自投翠雀飞行路线、误估叶级，导致被截杀。信息未传出不等于翠雀为灭口。 续审11：卡102又把相同金纹首领欲报蛾情节移至卷二85，并将击杀改成夏凉蓝冲击；实际卷二85无此回溯（C108）。原卷一85凶手翠雀及未传出报告的判断仍有效，不能因再写版本而变成夏或麻雀灭口。

**可能造成的 RP 后果：** 伪造爪痕内部清理/交易掩盖的支线，抹除主角救援行动。

**建议处理：** 后续纠正凶手和因果；有意另写灭口需USER_CONFIRMATION_REQUIRED。

## [C037] 麻雀被写成魔术使，写字楼地点被写成瑞明区

**严重程度：** MODERATE

**问题类型：** 身份／地点

**角色卡位置：** [ID 94](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_094.txt>)

**当前内容概述：** 事件九称爪痕魔术使麻雀，事件九和十一定位瑞明区。

**发现的问题：** 麻雀旧金铃是财政院字牌魔法少女，拥有魔装/半兽形；写字楼与其战场为珞明区。魔术使和魔法少女在此有不同施术与收押权限，不能当近义称呼。

**原著证据 / 定位：** [E093](01_evidence_index.md#e093)、[E096](01_evidence_index.md#e096)、[E100](01_evidence_index.md#e100)、[E103](01_evidence_index.md#e103)；L5655、5974、6390、6627

**证据等级：** A

**更准确的理解：** 麻雀为叛逃魔法少女；黑烬队众普通黑袍多为魔术使。珞明区与黎星区是两处战场。

**可能造成的 RP 后果：** 错用能力模板、媒介需求和司法权限；转移地图目标。

**建议处理：** 后续纠正条目身份与地名，并核对手机副本。


## [C038] 禁魔前置条件与旧伤的持续疼痛、加重风险须分开

**严重程度：** MAJOR

**问题类型：** 能力限制／战术

**角色卡位置：** [ID 3｜魔术与符文](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_003.txt>)；[ID 47｜林昀](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_047.txt>)；[ID 94｜剧情·卷1幕05·黑烬黎明事变](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_094.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)；[ID 106｜剧情·卷2幕09·旧梦与岔路](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_106.txt>)

**当前内容概述：** 事件九称透支本相连续杰作、每件均加重旧伤，禁魔限制麻雀媒介并逼她无法扩大屏障。

**发现的问题：** 原文先用线偶、盾与拳节约消耗/套话，后强行爆发，击败麻雀才禁魔；禁魔需先解除抵抗，并非战中任意封媒介。此前审计只强调爆发累积疼痛不够完整：终章明确如今翠雀用魔装战斗几乎一直魂痛；但未据此确立每件杰作必按次损耗本相。

**原著证据 / 定位：** [E094](01_evidence_index.md#e094)、[E096](01_evidence_index.md#e096)；L5980–5999 [E134](01_evidence_index.md#e134)—[E138](01_evidence_index.md#e138)、[E144](01_evidence_index.md#e144)；L9452–9460、9564、9731–9735、10305。；[E173](01_evidence_index.md#e173)、[E174](01_evidence_index.md#e174)；L12390、12485–12486；[E184](01_evidence_index.md#e184)、[E186](01_evidence_index.md#e186)、[E187](01_evidence_index.md#e187)、[E206](01_evidence_index.md#e206)；[E222](01_evidence_index.md#e222)—[E230](01_evidence_index.md#e230)；[E249](01_evidence_index.md#e249)、[E250](01_evidence_index.md#e250)；[E282](01_evidence_index.md#e282)—[E285](01_evidence_index.md#e285)；[E324](01_evidence_index.md#e324)—[E331](01_evidence_index.md#e331)、[E344](01_evidence_index.md#e344)；[E389](01_evidence_index.md#e389)、[E392](01_evidence_index.md#e392)、[E394](01_evidence_index.md#e394)；[E426](01_evidence_index.md#e426)；[E432](01_evidence_index.md#e432)、[E433](01_evidence_index.md#e433)、[E435](01_evidence_index.md#e435)；[E541](01_evidence_index.md#e541)—[E545](01_evidence_index.md#e545)

**证据等级：** A

**更准确的理解：** 分开四件事：旧损带来的用魔装持续魂痛；大量用魔加剧头痛并伤宝石；主动透支或用残剪撬动规则造成不可逆损坏；禁魔须解除目标抵抗。蛛受禁魔仍可另接兽腑不等于禁魔失效。精细用魔/格斗可减少消耗，但不能反称普通构装完全无痛。 续审06：伤后约叶级魔量、失控男转女，两周后仍约每日一次；大量加速飞行也触痛。祖解释奇境仍在但沉寂、残存力量可经康复成为新整体；方案不等于已修复，本相已透支部分仍不可回。不能将失控方向写成正常变身不可逆（另C069），也不能将每次用魔等同按件固定本相扣减。 续审07：翠尚未恢复奇境便用红复现剪分离气，需理解目标机制并付初始/维持魔量；永久大范围去残兽才需终章毁剪规模。红先说用自己的魔力，33章最后一剪又明确翠耗自身大半魔量，不能抽一句定成全程零自耗。复制剪约五分钟是红当期熟练度限制；剪消失后翠可用余魔维持分离数小时。分离本相与任意摧毁魔装不能互换。 续审08：43第三次切磋与前两场平手受不用更高能力、切磋性质与信息差制约，鸢基础格斗、魔量和力量占优。问伤势是否好些不是治愈证据。42结尾车内林化蓝线与翠在门前是遮掩两身份的线偶表现，具体切换未写，不扩成任意距离自主分身或无耗本体。 续审09：60失控再次现场发生，61丝线固定有小结但翠明确目前无使用障碍；她推副作用可能继续及本相影响，未出口的命运意象更非确证预言。不得把同伴建议稳定一年、翠拒等候或魔装打结写成已证按次损耗/本相侵蚀；具体差异见C096。 续审11：78贯胸时翠移源成功，79伤口侵蚀扩大并增修复魔耗，80仍因耗魔修躯负担魂痛；未伤源不等无险。81再借红复制剪和丝媒介剪气，88失魔致身体失支撑。新的伤害与消耗过程没有证明每件杰作固定扣本相，也没有因一次仍能战就证旧伤痊愈。 续审13：108术后实际丝与奇境试用无痛，繁开仅起手被阻止；祖要求7/10天稳定、保险至开考静养，两毁魔装仍不返。再献祭使林消失是本次专业警告，不等所有普通魔装使用按次损本相。109表情较自然也来自痛苦减轻。 续审14：136当前近两天可以实际入眠，叙述以或许修复解释，非新一轮手术已发生；仅睡眠新状态不解除再损死线。136训练数字为例题而非固定全族参数，持续占用与魔量不同。 续审15：146一周后复诊正式准全部现存能力、实验室禁繁开，稳定期临时限制结束；不会返已毁两件。143剪抗性仍持续占出力，144主动停止才腾余量，不是一次剪除永远零成本。 续审20：265剪共同规则本相虚弱而266魔差破规则剪裂、267矢自觉本相已伤、269再昙，故老伤与魔装损失有多次事件而非一场单因。石腿不可修是自称伤本相，祖伤辅禁亦未好，各自伤情不自动等同同一诅咒。

**可能造成的 RP 后果：** 任意先手封禁敌人，或让一切构装都损核心，消除真实战术取舍。

**建议处理：** 后续保留真实持续疼痛与按量风险，纠正禁魔时点；不增写每次杰作固定扣本相的机制，额外机制留USER_CONFIRMATION_REQUIRED。

## [C039] 麻雀内心回顾被写成被捕后的完整供词

**严重程度：** MAJOR

**问题类型：** 叙述视角／秘密传播

**角色卡位置：** [ID 94](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_094.txt>)

**当前内容概述：** 事件十称麻雀被禁魔后向林昀交代材料交易、跟踪及黑烬活动，樱案关联随口供公开。

**发现的问题：** 第81章主要是麻雀内心回顾且发生在胜负未决时。她未向翠雀完整供述，连黑烬在找什么都不知；认出矢车菊也未共享。第93章翠雀才从猫眼听黑烬背景及樱案关联。

**原著证据 / 定位：** [E095](01_evidence_index.md#e095)、[E096](01_evidence_index.md#e096)、[E104](01_evidence_index.md#e104)；L5845–5873、5882–5891、6727–6729

**证据等级：** A（叙述主体及对话）／D（院方结论）

**更准确的理解：** 读者所知、麻雀所知、盟方所知与翠雀所知四层分离；不把章标题黑烬黎明变成一份公开档案。

**可能造成的 RP 后果：** 翠雀与机构提前获得全部交易和跟踪细节，调查失去动机。

**建议处理：** 后续恢复叙述视角；未经证据传播的资料不解锁NPC知识。


## [C040] 第86章被替换成匿名预警回溯并新增事后封存剧情

**严重程度：** MAJOR

**问题类型：** 章序／原创桥段

**角色卡位置：** [ID 94](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_094.txt>)

**当前内容概述：** 事件十三写第86章回到5月26日重演首通电话，另写样本保护封存、小璐道谢和路径复盘等。

**发现的问题：** 第86章实际是翠雀到福利院误以为夏凉死去，获澄清后肯定新人，无匿名预警插叙。第84—85章亦无所写现场封存祭子推断以保护样本的审查行动。若有新增对白、病房和封存，需要单独来源。

**原著证据 / 定位：** [E098](01_evidence_index.md#e098)—[E100](01_evidence_index.md#e100)；源文L6320–6386；首通原定位E003

**证据等级：** A（本章内容）；新增封存/插叙依据F

**更准确的理解：** 保留误会暴露翠雀关心、对过度保护的反思与不同机构后续处理；不能用首卷已有电话情节填作新章。

**可能造成的 RP 后果：** 重复触发复出、覆盖已发生进度，NPC持有尚未收到的祭子情报。

**建议处理：** USER_CONFIRMATION_REQUIRED：确认这些是否有意IF；原文证据保持确定，不据摘要倒写原著。


## [C041] 福利院院长识别的形态被写成林昀本体

**严重程度：** MAJOR

**问题类型：** 身份认知

**角色卡位置：** [ID 95](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_095.txt>)

**当前内容概述：** 事件一称刘文琴从林昀神态行事认出矢车菊。

**发现的问题：** 第87章明确以翠雀面貌去见院长，她按旧新闻记忆辨认并获确认；这不是目击男性林昀并认出本体。叙述用林昀指人物本身不等于该形态在场。

**原著证据 / 定位：** [E100](01_evidence_index.md#e100)；L6402–6418

**证据等级：** A

**更准确的理解：** 院长知道翠雀=矢车菊及薄雪=白静萱，未因本段获知林昀=翠雀；心理暗示被暂缓便于谈话。

**可能造成的 RP 后果：** 把普通院长变成本体知情者，并错误扩大记忆处理对象。

**建议处理：** 后续明确场景形态与已知身份边。


## [C042] 扫墓中的偏移者内心猜测被写成父女讨论

**严重程度：** MAJOR

**问题类型：** 认知／内心转述

**角色卡位置：** [ID 95](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_095.txt>)

**当前内容概述：** 事件二写回家后父女讨论小璐银白爆发和祭子体质，再说林昀不告诉女儿。

**发现的问题：** 第90章偏移者判断是林昀据三人战后口述产生的内部猜测；没有回家后一同讨论。摘要自身也前句共享、后句隐瞒冲突。

**原著证据 / 定位：** [E102](01_evidence_index.md#e102)、[E105](01_evidence_index.md#e105)；L6556–6561、6584–6607

**证据等级：** A（视角）／C（推测）

**更准确的理解：** 当时林昀的推断未等于女儿知道；第94章红思与也参与猜测。女儿此处明确的是守护及追查目标。

**可能造成的 RP 后果：** 无传播途径便让小璐了解分类秘密，提前改变自我认同。

**建议处理：** 后续拆开可闻墓前对话与父亲内心，并按说话者保存信息。


## [C043] 夏凉身份揭露的地点、情绪与亲情回应被改写

**严重程度：** MAJOR

**问题类型：** 人物关系／视角

**角色卡位置：** [ID 95｜剧情·卷1幕06·暑假与秘密基地](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_095.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)；[ID 81｜夏凉](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_081.txt>)

**当前内容概述：** 事件六林家阳台、夏凉没有得意；事件七当夜答应生日出游，关系接近家人。

**发现的问题：** 实际在夏凉家阳台，她带小得意并主动求证，翠雀如释重负；最重要的亲情要求被严肃暂缓。封口费当夜被打断，后章才补完出游约定；不能把暂缓当已接纳义女或该夜承诺生日。

**原著证据 / 定位：** [E109](01_evidence_index.md#e109)—[E111](01_evidence_index.md#e111)；L7141、7171–7173、7198、7258–7278、7283–7290、7331–7334；[E377](01_evidence_index.md#e377)、[E387](01_evidence_index.md#e387)

**证据等级：** A（对话、内心及地点）／D（亲情解读）

**更准确的理解：** 夏凉珍视与小璐不同的专属关系，有真诚也有占有式喜悦；翠雀重视家庭责任，未轻诺身份转变。确认同一人不等于知道其性别本源或所有历史。 续审13：102夏公开温柔港湾策略并让翠真休息，回应先前翠教她表达用心；106仍以原女后男理解身份，纠正被打断。亲密、体贴、理解错误可以并存，不把只会操纵/完全理解任一端当固定性格。

**可能造成的 RP 后果：** 把复杂关系简化为立即圆满，丢失界限、试探和后续追问。

**建议处理：** 后续纠正地点与回应时点；新增问句与承诺如为改编进入USER_CONFIRMATION_REQUIRED。

## [C044] 秘密基地形成中的空间理由、邀请对象与先后错置

**严重程度：** MODERATE

**问题类型：** 地点／社会关系／日常因果

**角色卡位置：** [ID 95](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_095.txt>)；[ID 121](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_121.txt>)

**当前内容概述：** 第06幕写林家空间不足、孩子先画安全及撤退线再向林昀申请；入住后红才邀林昀任职。

**发现的问题：** 原文林家更大但有父亲、夏家更小；在夏凉家向翠雀提案，尚需讨论。红邀林昀作小锦联络人在参观交接时，早于周末入住；此处只是考虑，没有已经任职。ID121总体来源较准确，须防不同副本互相覆盖。

**原著证据 / 定位：** [E107](01_evidence_index.md#e107)、[E108](01_evidence_index.md#e108)、[E111](01_evidence_index.md#e111)；L6982–6985、7001、7064、7315–7346

**证据等级：** A；具体新增设计图依据F

**更准确的理解：** 区分提案、四人同意、院方背书、交接、邀职与入住，保留真实家庭约束而不是单一房间面积。

**可能造成的 RP 后果：** 普通父亲拥有未说明的魔法小队决策权限，工作状态提前变化。

**建议处理：** 后续统一副本；新增规划动作为IF候选并入USER_CONFIRMATION_REQUIRED。


## [C045] 夏凉没有坏习惯的绝对说法需要限定范围

**严重程度：** MODERATE

**问题类型：** 人物日常／标签范围

**角色卡位置：** [ID 81](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_081.txt>)

**当前内容概述：** 性格及第一阶段称与不良团体相处却没有坏习惯。

**发现的问题：** 第100章明确赖床到迟到前最后一秒，常迟到由小璐转述，翠雀也把作息问题当陋习；揭露后会以小动作干扰学习，第99章还上课玩手机。原句若意指不吸烟饮酒，应限定这些行为，不能泛化成生活学习全无坏习惯。

**原著证据 / 定位：** [E111](01_evidence_index.md#e111)、[E112](01_evidence_index.md#e112)、[E113](01_evidence_index.md#e113)；L7303–7305、7399–7413、7423–7425；[E116](01_evidence_index.md#e116)、[E118](01_evidence_index.md#e118)；L7825–7826、7838–7839

**证据等级：** A（具体行为）／D（同学迟到评价）；原卡坏习惯的拟定语义需澄清

**更准确的理解：** 保留热心、天赋与日常松懈并存，不由此把她反定性为道德恶劣或有未证实的不良嗜好。 第103—104章进一步证明她明确拒绝不合适打工，且对旧友留有恻隐；因此更应把“没有坏习惯”限为未染特定不良行为，而不是用本问题否定该拒绝事实。

**可能造成的 RP 后果：** 模型抹掉赖床、试探和课堂分心，人物趋于完美且丢失家庭磨合。

**建议处理：** 后续把绝对量词改成有范围的行为记录。

## [C046] 把白静萱近期独行行为固化为福利院长期孤僻性格

**严重程度：** MODERATE

**问题类型：** 人物性格／观察时期

**角色卡位置：** [ID 17](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_017.txt>)；[ID 119](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_119.txt>)

**当前内容概述：** 地点条目称先天病、失眼与孤僻性格令她长期被照护；人物初印象常抱书独行。

**发现的问题：** 第67章明确她原来喜欢热闹、与护工老人交谈，最近几天为了会摩可才抱书独行。安静懂事、孤独处境与孤僻性格不同；未被领养主要与身体负担相连，不能无证把性格列为原因。

**原著证据 / 定位：** [E085](01_evidence_index.md#e085)、[E086](01_evidence_index.md#e086)、[E100](01_evidence_index.md#e100)、[E101](01_evidence_index.md#e101)；L4783–4785、6446–6449、6494–6500

**证据等级：** A（行为变化）／E（他人担忧）

**更准确的理解：** 初登场观察可保留，但标明短期目的；她有好奇、感激、友情和沉稳的孩子气，不是持续拒绝与人交流。

**可能造成的 RP 后果：** 把可亲近的新人成无端疏离NPC，抹去摩可友情造成的日常变化。

**建议处理：** 后续拆开处境、外观印象、近期行为和性格动机。


## 续审03判断修订记录

本轮继续从L4358开始，旧问题ID保持不变。修订C021、C001、C004、C005、C006、C009、C025、C031、S003、S010、S011、R005；每项修订前后文本及原因保存在[judgment_changes.json](judgment_changes.json)。新增C032—C049；尚未完成全文。

## [C047] 夏凉讨回旧账的概括掩盖她明确拒绝报复的选择

**严重程度：** MODERATE

**问题类型：** 人物动机／关系发展

**角色卡位置：** [ID 81](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_081.txt>)；[ID 95](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_095.txt>)

**当前内容概述：** 人物关系称夏凉后来在电器街正面讨回旧账，剧情把街机只概括为替她讨公道。

**发现的问题：** 实际比试与私下惩戒由翠雀实施，夏凉暗示留一次机会，明确称不存在报复并已把旧友当陌生人。第104章又解释早期李雅晴善意与其轻生经历，不能仅保留天才反击的胜利模板。

**原著证据 / 定位：** [E116](01_evidence_index.md#e116)—[E118](01_evidence_index.md#e118)；L7890–7898、7924–7927、7960–7985

**证据等级：** A（行动与补叙）／D（夏凉价值判断）

**更准确的理解：** 她可以终止关系且不追求报复，也可希望伤害过自己的人改过；李雅晴自卑不等于无罪，道歉也不等于重归朋友。翠雀没有官方普通人处罚职位。

**可能造成的 RP 后果：** NPC被迫演复仇快意或自动复交，原著有意保留的善意、拒绝和边界消失。

**建议处理：** 后续补足当事人的主动选择与保护者行为，保留原作矛盾，不自动美化或谴责。


## [C048] 旧队留影把同一人的本名代号及第五成员混进四人照片

**严重程度：** MODERATE

**问题类型：** 身份别名／回忆传播

**角色卡位置：** [ID 95](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_095.txt>)

**当前内容概述：** 事件九称留影墙勾出樱、安雅、玛格丽特、兰香和红思与的旧队照片。

**发现的问题：** 樱就是安雅；第108章眼前照片明确四人，其中蓝发翠雀，红思与是在随后私人口述中作为第五人加入。若将所列五个名称当五个被拍者，会遗漏翠雀、重复安雅并提前加入红思与。

**原著证据 / 定位：** [E115](01_evidence_index.md#e115)、[E121](01_evidence_index.md#e121)；L7578–7580、8386–8388、8408–8420

**证据等级：** A（照片人数和叙述顺序）／D、E（旧友评价）

**更准确的理解：** 四人旧队与后来五人阶段分开，照片可观察内容和私下补述分开；咖啡老板只误认昔日顾客之女，未掌握魔法少女本体链。

**可能造成的 RP 后果：** 重复生成同一NPC、变造队伍组成，让旁听者看照片就获所有本名和历史。

**建议处理：** 后续统一别名和时期，照片只载实际可见信息。


## [C049] 生日会末的私密失踪通知被扩成全队出差部署

**严重程度：** MAJOR

**问题类型：** 知识时点／原创事件／能力物品

**角色卡位置：** [ID 95](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_095.txt>)

**当前内容概述：** 事件十一至十二把猫尾失踪、巡查决定、众人求同行、白板撤离分工、每人的备用心之种写在第109—110章；还约薄雪次日同上学。

**发现的问题：** 第110章孩子先睡、翠雀独自接讯，不能写当夜全队当场得知。第111章后续确有宣布离开、三新人一致请求同行、因安全拒绝，最终红思与日常辅导加翠雀远程检查。这些安排有据，但不在109—110章；白板、每人的备用心之种、备用联络器藏取等仍无本段依据。薄雪当期仍休学。

**原著证据 / 定位：** [E112](01_evidence_index.md#e112)、[E123](01_evidence_index.md#e123)、[E124](01_evidence_index.md#e124)；L7375–7379、8637–8657、8667–8683；ID95事件十一—十二

**证据等级：** A（实际通知、后续请求与训练安排）／F（无据额外道具、部署细节）

**更准确的理解：** 区分生日当夜私密通知与随后向三新人宣告任务。同行要求确实发生，不能继续当作纯原创；主要替代监护/教学者是红思与，辅以远程训练计划，不能改成只由夏凉看守。

**可能造成的 RP 后果：** 全员提前获得私密案件，休学孩子被安排上学，凭空产生可替换生命核心与完整撤退协议。

**建议处理：** 仅保留额外道具/桥段在USER_CONFIRMATION_REQUIRED；后续修正有据事件的章节位置与实际分工，不修改角色卡。


## 续审04修订记录

本轮新增C050—C061；修订8项旧问题：C049、C038、C019、C021、S003、S010、S011、R005。C049收窄为前置时点及无据物品，后续同行请求与红思与/远程辅导已有支持。完整前后判断和原因见[judgment_changes.json](judgment_changes.json)。新增证据29组，全文仍未读完。

## [C050] 没有回响被误写成没有回声的声学异常

**严重程度：** MAJOR

**问题类型：** 能力名词／事件因果

**角色卡位置：** [ID 96](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_096.txt>)

**当前内容概述：** 事件四称办公室残兽对声响与攻击反应像没有回声、空间吞掉脚步声。

**发现的问题：** 第116章实际是击杀后取不到作为残兽产物的回响，根本未给无回声能力；L9154反而明确走道回响脚步。卡片混淆同音近义词，改造了核心线索。

**原著证据 / 定位：** [E130](01_evidence_index.md#e130)；L9133–9140、9154；ID96事件四

**证据等级：** A

**更准确的理解：** 将无回响保留为超出翠雀既有知识的异常；后续员工兽化推理另记，尚未直接解释为何没有回响。

**可能造成的 RP 后果：** 把资源与生命来源谜题演成音效/声波术，调查与能力判断方向错误。

**建议处理：** 后续纠正名词；声学追加若为有意IF则列USER_CONFIRMATION_REQUIRED。

## [C051] 复制巢穴被追加按选择增生和拆墙扩张规则

**严重程度：** MAJOR

**问题类型：** 空间机制／无据推断

**角色卡位置：** [ID 96](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_096.txt>)

**当前内容概述：** 事件五称根据闯入者选择补出下一段、拆墙产生更多可复制结构，凭微小残留和物件校验找到核心。

**发现的问题：** 第117章解释多个已复制的一层空间，回到另一间同构办公室无尸血后确认；并无选择驱动增生或拆墙反馈。翠雀本拟向强魔力前进，却先发现微弱伤者，之后凭灯盏提灯导航才到核心。

**原著证据 / 定位：** [E131](01_evidence_index.md#e131)、[E133](01_evidence_index.md#e133)；L9214–9244、9247–9258、9402–9408

**证据等级：** A（实际机制及导航）／F（追加规则）

**更准确的理解：** 复制环境、不复制活物、空间拼接与一般粗糙模仿区分；不把侦查可操作性凭想象补成因果法则。

**可能造成的 RP 后果：** 错误禁止破墙、伪造解谜解法，抹除灯盏的独立导航贡献。

**建议处理：** 疑似IF的迷宫机制进入USER_CONFIRMATION_REQUIRED，未来重构前继续核验。

## [C052] 蛛网战脱困主体反置并追加提灯锁链破解

**严重程度：** MAJOR

**问题类型：** 战术因果／能力越界

**角色卡位置：** [ID 96](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_096.txt>)

**当前内容概述：** 事件九称灯盏脱锁后以提灯标记剩余蛛网找薄弱锁链，林昀精确击裂半蜕核心。

**发现的问题：** 被手臂、脚束缚并在破网后脱困的是翠雀；灯盏先受命去救猫尾、后轰翠雀头顶网。无再用提灯找弱链的动作，最终一击也未明说击裂核心。规则丝与实体网的区别比笼统锁链更关键。

**原著证据 / 定位：** [E137](01_evidence_index.md#e137)、[E138](01_evidence_index.md#e138)；L9747–9748、9754–9755、9765–9789、9798–9804

**证据等级：** A（战况）／F（追加动作）

**更准确的理解：** 翠雀冒险假说、丝线牵制、灯盏全力破网、翠雀解缚斩杀是实际链条；本人也避规则笼罩区，破网令其痛苦原因未明。

**可能造成的 RP 后果：** 让错误角色行动、增造提灯检测弱点能力，把未知原理变成万能胜法。

**建议处理：** 后续修正主体和步骤，未证实的招式/弱点定位作为IF候选，不擅自补全。

## [C053] 灯盏的调查口述被提前移交给柏安三新人

**严重程度：** MAJOR

**问题类型：** 信息传播／知识时点

**角色卡位置：** [ID 96](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_096.txt>)

**当前内容概述：** 事件三写三人组补齐提灯能力、失踪档案至少十一人/实际二十余人和仪式线索。

**发现的问题：** 第114章她们明确当时在上学，接触猫尾者主要灯盏；含羞草才提出找波利，后由波利补访问行程。118章才由灯盏告诉翠雀调查目标由爪痕转黑烬、失踪统计与仪式，119说明提灯。

**原著证据 / 定位：** [E128](01_evidence_index.md#e128)、[E129](01_evidence_index.md#e129)、[E132](01_evidence_index.md#e132)、[E133](01_evidence_index.md#e133)；L9017–9026、9300–9336、9404–9406

**证据等级：** A（转述链）／D（来源统计）

**更准确的理解：** 三人不具备完整档案不等于无用，白蓟组织、含羞草提供下一联系人、波利和灯盏分别补信息；约20以上不能强记准确22。

**可能造成的 RP 后果：** 提前跳过调查、使三新人全知、遗漏旧调查院资料未更新这一盲点。

**建议处理：** 后续按来源和获知时间分开保存；不让主线节点一次解锁整条链。

## [C054] 白蓟未知身份的统一断言覆盖她已读到的旧代号

**严重程度：** MODERATE

**问题类型：** 身份认知边界

**角色卡位置：** [ID 70](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_070.txt>)；[ID 96](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_096.txt>)

**当前内容概述：** 白蓟隐藏信息写不知道翠雀=矢车菊=林昀；剧情另写她看见矢车菊认证牌。

**发现的问题：** 第114章白蓟亲自验牌并读出矢车菊，翠雀用隐私结束话题，不等于否认旧牌为己。即使男性本体未知，翠雀与旧认证名的联系已有直接线索，不能用整条等式未知抹除。

**原著证据 / 定位：** [E128](01_evidence_index.md#e128)；L8937–8954；ID70隐藏信息、ID96事件二

**证据等级：** A（验牌及发言）／F（男性本体）

**更准确的理解：** 白蓟知道眼前翠雀出示属于矢车菊的认证牌；知道缘由、旧人生及林昀仍是另一组问题。含羞草/木百合是否完整听见、理解不能由同队自动继承。

**可能造成的 RP 后果：** 白蓟反复初闻旧号或线索失忆；反向修正过度又会使其知男身。

**建议处理：** 后续拆分知情边，不将不完整链写作全无或全知。

## [C055] 柏安善后被追加集体复盘与已完成的思想转变

**严重程度：** MODERATE

**问题类型：** 人物发展／原创场景

**角色卡位置：** [ID 96｜剧情·卷1幕07·柏安市巡查](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_096.txt>)；[ID 60｜木百合](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_060.txt>)

**当前内容概述：** 事件十写全队规则复盘、木百合区分冲动与证据，事件十一写队员系统分担与重组。

**发现的问题：** 第123章有后到调查队清剿、治疗、帮助琴行、告别演出，没写集体生存课。木百合见蛛照片仍嘴硬称有同伙、想追出城，后被灯盏叫停；不能当作当场完成反省。人物条目把大叔好人/请客道歉并入蛛案，也仍须后文核定真实时点。 间奏一后来确实承认抓错人，应结束此前一概嘴硬的状态；但她仍不知灯盏案情细节，不能自动升级为已掌握规则战全过程。

**原著证据 / 定位：** [E139](01_evidence_index.md#e139)、[E140](01_evidence_index.md#e140)；L9848–9854、9855–9868；ID96事件十—十一、ID60阶段二；[E178](01_evidence_index.md#e178)；[E252](01_evidence_index.md#e252)、[E253](01_evidence_index.md#e253)、[E261](01_evidence_index.md#e261)

**证据等级：** A（实际善后）／F（复盘、尚未读到的后期道歉时点）

**更准确的理解：** 保留舞台可靠、排练积极与判断幼稚并存。后续会成长不让此次事件自动治愈缺点；无据复盘不代表所有战后影响都不存在，偏头痛持续在127已有证。 间奏一向玛格承认抓错人、因而禁足是局部进步；仍记错翠雀名字，对灯盏失踪只知含糊解释。请客道歉具体情节尚未连续读到，仍留后查。 续审08：44木能迅速击杀蠖兽，但把仍有余力的小璐判断为苦战耗竭；战力可靠和观察判断有误并存。48认翠后畏缩、学生身份被介绍，不等此前疑点已全部解清。具体请客道歉尚未连续读到，后查项不提前关闭。

**可能造成的 RP 后果：** 强行人物成熟、角色弧提前完成，依作者方法论替换实际互动。

**建议处理：** 集体复盘与重组进入USER_CONFIRMATION_REQUIRED，后期道歉继续随原著核验。

## [C056] 柏安外观已知局部被遗漏，白蓟与小璐魔力色混淆

**严重程度：** MODERATE

**问题类型：** 外貌遗漏／不当未知

**角色卡位置：** [ID 60｜木百合](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_060.txt>)；[ID 70｜白蓟](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_070.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)

**当前内容概述：** 木百合及白蓟称更多变身细节未详，已知局部未录；卡70另写白蓟常态淡蓝魔力。

**发现的问题：** 完整服装确非全套明确，但112已有木百合层叠公主裙、浅金长卷发、分梳刘海与澄黄眸，113—114已有白蓟青发与披风。不能因未全描就丢掉这些已知局部或阻止采用。续审10第66—67章天青白蓟与浅蓝小璐同场对照，已不再是全部魔力色待核状态。

**原著证据 / 定位：** [E126](01_evidence_index.md#e126)—[E128](01_evidence_index.md#e128)；L8768、8773、8912、8924–8926；[E291](01_evidence_index.md#e291)、[E297](01_evidence_index.md#e297)、[E299](01_evidence_index.md#e299)、[E301](01_evidence_index.md#e301)；[E360](01_evidence_index.md#e360)、[E364](01_evidence_index.md#e364)、[E370](01_evidence_index.md#e370)

**证据等级：** A（已描局部）

**更准确的理解：** 外观按阶段逐项列已知与未知；缺乏完整设定图不等于没有服饰发色证据。 续审10：64含羞外貌与卡33相符，不算全缺；68白蓟人类黑发瘦削已录。66天青色明确为白蓟，浅蓝色是小璐；卡70写白蓟常态淡蓝色应复核修正，不能互换。 续审12：96木在局长室才知道林的职位，97才正式道歉并认好人大叔，不能前移卷一相识阶段。100玛叙琴行夫妇收养与灯盏名义妹妹，木只认寄养；未展示具体法律登记，不从正式收养措辞外推手续。

**可能造成的 RP 后果：** 同一角色早期视觉特征漂移，模型反复声称不存在已给描述。

**建议处理：** 后续补源文局部，不凭其推全套服装。

## [C057] 灯盏失踪与归队的关系主体被写反

**严重程度：** MODERATE

**问题类型：** 人物关系／事件主体

**角色卡位置：** [ID 25｜灯盏](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_025.txt>)；[ID 96｜剧情·卷1幕07·柏安市巡查](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_096.txt>)

**当前内容概述：** 灯盏条目写木百合失踪时最担心她；柏安剧情又称灯盏获救使她们暂时没有队长。

**发现的问题：** 本次失踪者为灯盏、焦急者为木百合；获救后灯盏恢复并与队友演出，白蓟是未来接班人，非队长再缺位。文字直接反转既定主体与结果。

**原著证据 / 定位：** [E128](01_evidence_index.md#e128)、[E140](01_evidence_index.md#e140)；L8971–8972、8994、9855–9888；[E370](01_evidence_index.md#e370)

**证据等级：** A

**更准确的理解：** 木百合担忧灯盏，灯盏归队后继续任队长并信任未来的白蓟；收养背景由后文E370补足，保留玛转述等级，不以卡内背景作事实权威。 第一阶段收尾：100章已由玛向翠转述木父弃置琴行、店主夫妇收养后木为灯盏名义妹妹的家史（D；E370）；不再是本审计未读背景。木本人仍信寄养父会回，不能将转述真相提前给她。

**可能造成的 RP 后果：** 生成不存在的失踪、重复任命新队长，破坏既定亲疏和领导关系。

**建议处理：** 后续纠正主宾及因果，不添加新危机补圆措辞。

## [C058] 节前基地家务与月圆节返家被合并成提前团聚

**严重程度：** MAJOR

**问题类型：** 时间地点／人物认知

**角色卡位置：** [ID 96](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_096.txt>)；[ID 97](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_097.txt>)

**当前内容概述：** ID96尾部称123已返家见三人、薄雪治愈被拒；ID97前两事件又写124—126林昀返家、摩可警戒和孩子据疲态备战。

**发现的问题：** 123仍柏安演出收讯；124—125在基地、翠雀离开近半月，红加班，林昀不在；127月圆节才返程，128进林家。白静萱此时首次见男性林昀。所谓孩子识旧伤、备用联络器收回、薄雪被拒治愈、节前全套备战，在这些原章未发生。

**原著证据 / 定位：** [E140](01_evidence_index.md#e140)—[E146](01_evidence_index.md#e146)；L9903、9956–9964、10141–10144、10285–10296、10413–10415

**证据等级：** A（实际场景与首次见面）／F（无据桥段）

**更准确的理解：** 节前普通家务未认识飞蛾危机；林昀返家后才私报调查结果及新来电，群中提醒安全。偏头痛持续本身有据，不能因桥段错误而否认伤痛。

**可能造成的 RP 后果：** 抹去白静萱第一次见林昀、消息未知与生活视角，创造全队提前接警。

**建议处理：** 后续修正时间地点；其余桥段列USER_CONFIRMATION_REQUIRED，不把未读后章当已否定。

## [C059] 匿名联络的同一来源被压成同一号码与固定三通

**严重程度：** MODERATE

**问题类型：** 通信链／证据粒度

**角色卡位置：** [ID 97](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_097.txt>)；[ID 36](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_036.txt>)

**当前内容概述：** ID97写五个月前神秘号码再次接通并以三通总结整个匿名线；ID36也写三通匿名电话。

**发现的问题：** 128明确旧号已空、新预警换号；129朝颜来电之外，130又回拨接通获很高/平时会去，爆响断线再拨关机。137回忆的是白玫遭袭当天中午办卡、求妮妮报警的过程，并非依卡所列三夜逐通交代；来源解开不抹去实际呼叫次数、号码变化或回拨。

**原著证据 / 定位：** [E144](01_evidence_index.md#e144)、[E145](01_evidence_index.md#e145)、[E148](01_evidence_index.md#e148)、[E149](01_evidence_index.md#e149)；L10338–10342、10643、10678–10705；[E159](01_evidence_index.md#e159)、[E160](01_evidence_index.md#e160)；L11602–11627；[E190](01_evidence_index.md#e190)

**证据等级：** A（通信及回忆过程）／F（各次呼叫未逐一重演的细节、妮妮是否知男身）

**更准确的理解：** 按具体发起方、号码、接通状态、听清内容记联络；一段预警可含未接、回拨、打回多个呼叫，不把来源同一等同号码相同。 现可确认红借妮妮自身感应向林警告的起源：办卡人只称认识的人，妮妮只获电话对方为巡查使的提示。不可顺势宣称她因此掌握林昀=翠雀，或全部电话只能说固定片段。 续审06已确认妮妮在蛾死后获救并恢复于基地；这只解决获释状态，不把此前号码变更抹掉，也不证明所有呼叫恰好三通或她已知林昀真身。

**可能造成的 RP 后果：** 错误号码追踪、缺失地址推理、提前赋予发话者身份与完整警告。

**建议处理：** 保留已揭示的红委妮妮警告源头和卷二7获救结果，逐次号码、呼叫状态仍按前文记录；后续只追妮妮是否知男身、补充供述及摩可任命缘由。

## [C060] 红思与味觉伏笔被固化为跨阶段稳定厨艺笑点

**严重程度：** MODERATE

**问题类型：** 性格与身体状态／伏笔回收

**角色卡位置：** [ID 36｜红思与](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_036.txt>)

**当前内容概述：** 语言及习惯写调味灾难属于稳定笑点、保留为日常缺点。

**发现的问题：** 125的味觉失调在132回接兽化处境，137救回后明确味觉等感官重新清晰反馈。把特殊身体阶段症状当永久稳定笑点会漏反转；续审07已读到恢复后厨艺改善的后辈评价，原先未见具体表现的判断现已收窄；仍不能倒填刚获救即善厨。

**原著证据 / 定位：** [E142](01_evidence_index.md#e142)、[E152](01_evidence_index.md#e152)；L10089–10098、10977–10986；[E161](01_evidence_index.md#e161)；L11679；[E232](01_evidence_index.md#e232)；[E278](01_evidence_index.md#e278)

**证据等级：** A（味觉叙事回接、评价发生）／D/E（小璐和夏凉对恢复后厨艺的评价）

**更准确的理解：** 保留表层喜剧及后期伤痛解释，按身体/认知阶段使用；一般烹饪技术与兽化味觉影响不同。 获救与味觉重新反馈已确认；厨艺技能与身体味觉应分别追踪。 续审07：卷二35章小璐明确说红做饭好吃了，夏回应终于克服障碍，已支持恢复后实际改善。这是两名后辈评价，不等同万能厨艺鉴定；仍不能倒填卷一137刚获救即立刻精通。原先恢复后表现全未知的待查项被新证据取代。 续审09：58红熟练做煮蛋、蔬菜粥、咖啡，晨咖啡是多年工作习惯。这是实际日常行为A，补强恢复后的生活能力，与35后辈好吃评价层次不同；仍不倒填刚醒即精通或消除一切普通烹饪失误。

**可能造成的 RP 后果：** 失去铺垫与后期解释，恢复后仍机械套用受困阶段症状。

**建议处理：** 后续按身体与技能阶段收录；已有恢复后改善评价，不再机械套稳定调味灾难，也不超出评价推出全能厨艺。

## [C061] 现场不能说的幕后身份被提前写成完整自白

**严重程度：** MAJOR

**问题类型：** 秘密身份／知情时点

**角色卡位置：** [ID 97](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_097.txt>)

**当前内容概述：** 事件四把摩丝姓名、1997年8月赴任首日被缝合写入129—131红思与现身的承认。

**发现的问题：** 131末背后声音、132红说不能讲幕后是谁；136回忆才向读者展示摩丝接见暗算，137继续展示两年受限与妮妮求救。这不是红在129—131当场承认全部；正文写返城头日见林、次日赴局，无1997年8月明文。140才在翠与摩丝对话中另获实验技术。

**原著证据 / 定位：** [E150](01_evidence_index.md#e150)—[E152](01_evidence_index.md#e152)；L10831–10861、10910–10928、10969–10980；[E157](01_evidence_index.md#e157)—[E160](01_evidence_index.md#e160)、[E167](01_evidence_index.md#e167)

**证据等级：** A（回忆揭示、现场对话差异）／D（技术口述）／F（额外精确年月与完整自白）

**更准确的理解：** 施害者、受控两年及求救源头已有原文支持，不再标整个过去未知；但须区分回忆供读者所知、红受限未说、翠后来当面质问所知。137红获救推翻无法恢复的绝对理解，获救本身也不是其此前可预知的事实。

**可能造成的 RP 后果：** 剧情强制揭露反派、让受限者轻易突破限制，抹去后续跨章揭示。

**建议处理：** 保留ID并收窄未知范围；后续纠正章界与叙述层，额外完整自白留USER_CONFIRMATION_REQUIRED。


## [C062] 把翠雀受伤退隐误写为因安雅订婚而退隐

**严重程度：** MAJOR

**问题类型：** 历史因果／关系

**角色卡位置：** [ID 97](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_097.txt>)；[ID 36](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_036.txt>)

**当前内容概述：** 卡97事件五称翠雀因安雅订婚退隐；卡36又把退隐、订婚并作红逃离的原因。

**发现的问题：** 135与终章明确翠因两次透支伤损、战力退化而隐退；135二十岁红才听订婚消息，136二十二毕业后才离城。卡97倒置退隐缘由；红一度支持前辈休养，逃离主要因无法维持与安雅的关系，不能把翠退隐本身写成直接伤害她的原因。

**原著证据 / 定位：** [E156](01_evidence_index.md#e156)、[E157](01_evidence_index.md#e157)、[E173](01_evidence_index.md#e173)

**证据等级：** A

**更准确的理解：** 分开十七岁翠伤退、二十岁红获知订婚、二十二岁红毕业离城，以及后续三十三岁回城；红与翠年龄不同，不拼成同一人的年份轴。

**可能造成的 RP 后果：** 扭曲两人抉择和安雅位置，把伤残归成恋爱变故。

**建议处理：** 后续纠正因果与相对年龄轴；精确日历仍归U001。

## [C063] 获救后的观察被补写成已经展示的逐层剖壳战斗

**严重程度：** MODERATE

**问题类型：** 场景细节／疑似原创

**角色卡位置：** [ID 97](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_097.txt>)

**当前内容概述：** 事件七写剪刀逐层剖开外壳、外壳反击；用不用再当安雅概括拒绝，称光柱立刻打断。

**发现的问题：** 137主要从红沉入黑暗切到被拉回后的观察：空蛾壳、裂剪、人形，未展示逐层剖割和反击过程。已有裂剪不能证明是这一次刚受损；终章补它早在花园战几废。拒绝尚有放不下过去、选择未来的完整答复；光柱132已出现。

**原著证据 / 定位：** [E151](01_evidence_index.md#e151)、[E161](01_evidence_index.md#e161)、[E162](01_evidence_index.md#e162)、[E173](01_evidence_index.md#e173)

**证据等级：** A（获救及答复）／F（新增操作与反击）

**更准确的理解：** 救回与剪刀有关有依据，但操作镜头缺口不能当原文动作实录；红自己未感知的过程也不自动为她所知。

**可能造成的 RP 后果：** 编造战斗和代价，遗漏明确拒绝理由并推迟警报。

**建议处理：** 后续区分结果、可推过程与可选IF；逐层反击列USER_CONFIRMATION_REQUIRED。

## [C064] 巨影规则在同命中整体失效的说法遮掉剪刀仍能被夺

**严重程度：** MAJOR

**问题类型：** 规则边界／战术

**角色卡位置：** [ID 59](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_059.txt>)；[ID 97](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_097.txt>)

**当前内容概述：** 摩丝条目两次写其规则在同命中失效；剧情称以内规则覆盖外规则、共享状态令队伍重组。

**发现的问题：** 终章实际夺魔仍生效，摩丝夺走了剪刀；不能影响的是由灵魂意志形成的奇境丝。她因剧痛且不能有效操作丢弃剪刀，翠拾回；并非同命全面关闭敌规则。源文未写共享生命状态使队伍恢复协作。

**原著证据 / 定位：** [E172](01_evidence_index.md#e172)、[E174](01_evidence_index.md#e174)、[E175](01_evidence_index.md#e175)

**证据等级：** A

**更准确的理解：** 区分魔力丝线/魔装剪刀与奇境丝线；同命连接诸生命、剪一卵之线的残兽概念向相连者传递，翠自己亦受规则约束。影子覆盖条件仍须遵守。

**可能造成的 RP 后果：** 把奇境变成无条件反制任何能力的领域，省掉规则试探与代价。

**建议处理：** 后续补作用对象、覆盖条件及夺剪反例；新增队伍协作桥段列USER_CONFIRMATION_REQUIRED。

## [C065] 把摩丝最后死因写成拳头处刑

**严重程度：** MAJOR

**问题类型：** 战果／能力状态

**角色卡位置：** [ID 97](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_097.txt>)

**当前内容概述：** 事件十一写蛾被剥回人形后林昀以拳头处刑。

**发现的问题：** 终章先以格斗泄愤，停手问樱案；摩丝说遗言并试图刺眼，翠以杰作贯头，再刺要害直至死。明确是杰作杀了她；拳头不构成原文最终死因。

**原著证据 / 定位：** [E176](01_evidence_index.md#e176)；L12635–12651

**证据等级：** A

**更准确的理解：** 保留殴打、问讯、遗言与突袭、杰作杀死的先后；剪刀失去仍能用丝线构成杰作。

**可能造成的 RP 后果：** 错误封死剩余能力，也改掉最后突袭与未完成审问的因果。

**建议处理：** 后续纠正死因和织命剩余形态；若保留拳杀则须明确IF。

## [C066] 剧情摘要把三新人统一写成不知道翠雀真身

**严重程度：** MAJOR

**问题类型：** 逐人知情／场景压缩

**角色卡位置：** [ID 97｜剧情·卷1幕08·月圆节之变](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_097.txt>)；[ID 98｜剧情·卷2幕01·新局长与兽子](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_098.txt>)；[ID 99｜剧情·卷2幕02·鸢来袭](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_099.txt>)；[ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)；[ID 81｜夏凉](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_081.txt>)；[ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)

**当前内容概述：** ID97事件八称孩子们不知道翠雀就是林昀；同段以小璐银白魔力灼伤蛾并救回薄雪概括救援。 续审06新增定位：ID98出场要点和幕末快照也写三人都/孩子们不知道林昀就是翠雀。 续审07：ID99幕末重复全体不知道，ID100事件一却保留夏凉已知。

**发现的问题：** 夏凉在第98章已获同一人的确认，此时不能与小璐、薄雪一起设为不知道男身；仅知道男身不表示她已知宝石代号的全部来历。救援方面，原文先摩可下去，后翠牵制时小璐与夏合救；摘要有省略，但单凭并字不足以判它明说小璐独救或银白魔力直接救人。 夏凉明知二者同一却顺势打趣后妈与母称，属于有意配合误会；小璐推错、白把不否认当接受，与夏并非同一知识状态。

**原著证据 / 定位：** [E109](01_evidence_index.md#e109)、[E166](01_evidence_index.md#e166)、[E169](01_evidence_index.md#e169)；源文L11964、12096、12099–12106；另见S010/C043；[E192](01_evidence_index.md#e192)—[E194](01_evidence_index.md#e194)；[E232](01_evidence_index.md#e232)—[E235](01_evidence_index.md#e235)；[E245](01_evidence_index.md#e245)、[E249](01_evidence_index.md#e249)、[E256](01_evidence_index.md#e256)、[E258](01_evidence_index.md#e258)、[E261](01_evidence_index.md#e261)；[E379](01_evidence_index.md#e379)、[E387](01_evidence_index.md#e387)、[E401](01_evidence_index.md#e401)；[E447](01_evidence_index.md#e447)、[E449](01_evidence_index.md#e449)；[E455](01_evidence_index.md#e455)、[E457](01_evidence_index.md#e457)、[E459](01_evidence_index.md#e459)

**证据等级：** A

**更准确的理解：** 三新人各有不同知识：夏早已知同一人，小璐此时拼旧号仍不知男身，白初闻樱死与母女关系后昏迷。能力攻击与稍后合救分别记录，但不把语义省略夸大成原卡明文断言。 同一错误沿用C066，累计涉及97、98；保持此前对救援并字的收窄，不重新宣称原卡明写小璐独救。 续审07：卡99出场要点及幕末孩子们不知道再次沿用同一错误，卡100事件一却已写夏不能说翠真实身份；原文37明确夏知道林翠同一并主动保密。夏35对白知湖畔经历惊讶，说明知真身不等拥有白的完整知识。小璐、白的误解照旧分列；不推翻此前对卡97合救省略的收窄。 续审08：42翠向夏说明母称承诺，夏新增该项知识而非获得白全经历。46翠先疑后现场确认歌手，47夏仍只称不确定，48翠明确答认识她时夏才得肯定；即使夏早知林翠，也不等预先知道全部旧队友。白仍没有得到男身确认，42父母双称是被回应的关系承诺。 续审13：卡104幕末三后辈不知昔日矢车菊又犯全称错误，夏早已知旧号；她103知龙胆掩护、106仍误解性别变向，两件事应分开。105只有夏懂生日双身份的描述可保留，不能因别处摘要错就抹掉。 续审15：161三名后辈现在确已获拟任蓝杖与两院合作口径，不继续全员未知权杖计划；依然小白不知林身、三人未得墨私交/留活口细案。 续审16：168翠准备未来逐步告秘密是计划；173再次亲口对夏区分她已知男身与小白不知，夏仍用能变男人的措辞，性别变向误解未明确纠正。不能把169/170三人已知龙胆参考误写成首次听所有身份。

**可能造成的 RP 后果：** 让夏凉丢失已确认的关键秘密，导致重复识破；压缩救援也容易遗漏同伴分工。

**建议处理：** 后续纠正全称知情状态，救援仅补主体与时间，不把未明说的独救设定强加给卡片。

## [C067] 卷一终局的局长邀请被提前写成已就任与公开会议

**严重程度：** MODERATE

**问题类型：** 身份任职／时间边界

**角色卡位置：** [ID 97｜剧情·卷1幕08·月圆节之变](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_097.txt>)

**当前内容概述：** 事件十四声称就任当日安排幸存者、未在公开会议说受害链，并以职位交接收卷。

**发现的问题：** 间奏二末只由金绿猫眼问对局长职位有兴趣否，卷一没有答应或交接会议。续审06已从卷二1—3确认战后休养两周到岗并在首日下午开公开大会，故不再将就任/开会本身列未知；差异收窄为卡97跨卷前置及其额外幸存者议程。三后辈任调权在卷一仍只见猫眼承诺，不能跟局长到岗自动合并。

**原著证据 / 定位：** [E179](01_evidence_index.md#e179)、[E180](01_evidence_index.md#e180)；L12824–12837、12875–12882；[E182](01_evidence_index.md#e182)—[E185](01_evidence_index.md#e185)；[E222](01_evidence_index.md#e222)

**证据等级：** A（邀请、卷二到岗大会与29章任调权落实）／F（卡97追加的会议议程）

**更准确的理解：** 按邀请、接受、任命、到岗区分阶段；卡97附加会议议程须按新证据继续区分。 续审06已确认林接受任职并在休养两周后到岗，首日中午通告、下午报告会。公开议程为内奸清理和武装配发，不是卡97那段幸存者安置/刻意不讲受害链的会议。实际就任与开会移出纯原创候选，只保留跨卷前置和额外会议细节。任命手续全过程未展示；三后辈任调权最终落实已由续审07第29章确认。 续审07：三名后辈任调权在29章已被叙述明确确认在翠手中，应由间奏二承诺推进为已落实；具体办理过程没有展示，不影响已获权这一事实。卡97把卷二到岗大会前置至卷一以及额外会议议程的问题保留，不能拿后续落实倒填卷末。

**可能造成的 RP 后果：** 提前赋予职位权力并使NPC得到尚未传播的任命信息。

**建议处理：** 后续按卷二实际情节收窄或加强判断；无据会议桥段列USER_CONFIRMATION_REQUIRED，不能断言全文从未发生。 任职已获正文支持，停止把它列为后续完全未知；C067保留阶段错置问题，U003范围相应收窄。

## [C068] 把摩丝的国度冷遇指控直接用作已确认生涯事实

**严重程度：** MODERATE

**问题类型：** 陈述来源／人物动机

**角色卡位置：** [ID 59](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_059.txt>)

**当前内容概述：** 性格与阶段一以女儿牺牲后未获国度应有重视作为确定的堕落背景。

**发现的问题：** 140追封、补贴、求助受拒等详情来自摩丝自述；141翠雀只以如果一切属实回应，并仅直接承认自身拒权杖和不满王庭。确有此控诉与其借此解释动机，不等于已独立验证每项制度事实。

**原著证据 / 定位：** [E168](01_evidence_index.md#e168)、[E169](01_evidence_index.md#e169)；L12070–12079、12111–12115

**证据等级：** A（她说了什么与翠回应）／D（具体控诉）

**更准确的理解：** 保留她对女儿的感情与以受害经历自我正当化的表现，同时将控诉标为其说法；不因此反向判她所有经历皆假。

**可能造成的 RP 后果：** 把敌方话术变成世界的唯一制度真相，令其他人无需证据就接受完整指控。

**建议处理：** 后续补来源标签与条件语气，继续寻旁证；这不是请用户投票决定Canon。

## [C069] 把单向失控变身写成变身从此只能单向

**严重程度：** MAJOR

**问题类型：** 能力机制／后遗症

**角色卡位置：** [ID 98｜剧情·卷2幕01·新局长与兽子](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_098.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)

**当前内容概述：** 事件二称魔装破损后变身从此只能单向发生。

**发现的问题：** 原文限制的是无预兆失控只见男转女，没有发生失控女转男；常规解除变身仍可进行。第18章林主动变少女追庄洋，又立即解除变身，是直接反例。

**原著证据 / 定位：** [E184](01_evidence_index.md#e184)、[E203](01_evidence_index.md#e203)；L13135—13148、14620—14623；[E220](01_evidence_index.md#e220)、[E221](01_evidence_index.md#e221)、[E237](01_evidence_index.md#e237)、[E238](01_evidence_index.md#e238)、[E240](01_evidence_index.md#e240)；[E277](01_evidence_index.md#e277)、[E282](01_evidence_index.md#e282)、[E283](01_evidence_index.md#e283)；[E360](01_evidence_index.md#e360)、[E361](01_evidence_index.md#e361)、[E368](01_evidence_index.md#e368)；[E420](01_evidence_index.md#e420)、[E423](01_evidence_index.md#e423)

**证据等级：** A

**更准确的理解：** 区分自动失控方向、主动变身、主动解除和魔力平复条件；初期数小时一次到两周后约一天一次是阶段性频率。 续审07：27章林先失控离席，28暂不能变回才查档，不能理解成任何时刻随意解除；40出研究所后仍正常恢复男性。红39章的变不回由本相变异及本体器官损伤解释，是另一人另一机制，不能并入林的永久单向限制。 续审09：57主动转林并换玛车掩身份，60局长室压不住魔力而转翠；玛曾听猫眼说、这次初亲见。翠称愈发失控是当前自述，仍不能外推男身必永久消失。主动变化、偶发失控、严重程度与治疗迫切原因分开。 续审12：96再次男身日常办公。99说被迫维持变身须解释当期频繁失控和工作相处情境，不能据一句取消已展示的主动解除能力。 续审14：132翠再次实际解除林身入酒吧，134重新变龙胆，外套录常服；不能把早期单向异常延伸至当前。两界生理不适不等男身已消失或无法变回。

**可能造成的 RP 后果：** 角色被错误锁死在少女状态，正常通勤与局长工作无法继续。

**建议处理：** 后续收窄为单向失控，额外不可逆机制若有意保留列USER_CONFIRMATION_REQUIRED。

## [C070] 把首次研究所体验拒绝写成已检查并得到结果

**严重程度：** MAJOR

**问题类型：** 事件结果／检查对象

**角色卡位置：** [ID 98｜剧情·卷2幕01·新局长与兽子](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_098.txt>)

**当前内容概述：** 事件九称祖安排翠体验残存魔装、检查底色与奇境反应，并据检查确认白的治愈与兽性非普通混合；同段写下午学习用品日常。

**发现的问题：** 第14章翠因隐私与数据用途质疑中止，第16章明确最终仍未接受产品试用。此访没有完成翠检查，更没对白体检；白首次实际体检是第20章湖畔春天战后。第12章实际次日上午用糖果打断清剿要求，所加学习用品和整个下午安排无此段依据。

**原著证据 / 定位：** [E195](01_evidence_index.md#e195)—[E199](01_evidence_index.md#e199)、[E201](01_evidence_index.md#e201)、[E208](01_evidence_index.md#e208)；[E236](01_evidence_index.md#e236)—[E240](01_evidence_index.md#e240)

**证据等级：** A（拒绝与实际体检时点）／F（额外日常桥段）

**更准确的理解：** 检查前专家解释、拟议体验、拒绝体验、战后对白完成检查是四个状态；20章还反转13章定义，不能前置其结果。 续审07：39章兽之源已交祖、交易完成，翠此时检查理疗已开始；40当次理疗完成且无需脱衣，叙述称此前要求脱衣纯谎言。首次14/16拒绝、20白体检、39后翠治疗三个对象/时间节点分开，不再泛称翠尚未接受任何治疗。23/24教辅款场景确实出现，但不是卡98第12章追加的下午学习用品安排。

**可能造成的 RP 后果：** 让人物依赖尚不存在的检查结果并跳过隐私争执与诊断修订。

**建议处理：** 纠正对象与完成状态；无据体验/学习用品桥段列USER_CONFIRMATION_REQUIRED，不用未来治疗倒填本次访问。

## [C071] 田胜的灾前报道和反复回味被改写为灾后入职与反复做梦

**严重程度：** MODERATE

**问题类型：** 人物履历／记忆状态

**角色卡位置：** [ID 98](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_098.txt>)；[ID 173](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_173.txt>)

**当前内容概述：** 卡98事件一写在工位反复梦见化蛾；173称田在月圆节灾后入职并编入第三队。

**发现的问题：** 卷二1明确赴总部报道入职当天就失去意识，灾后只是复苏与投入前线；工位是回味先前梦境、再次走神，不是展示多次重新做同一梦。两者不能改造成灾后新聘与周期性梦境症状。

**原著证据 / 定位：** [E182](01_evidence_index.md#e182)、[E183](01_evidence_index.md#e183)、[E189](01_evidence_index.md#e189)、[E202](01_evidence_index.md#e202)；L12962、12966、12975—12978、14527

**证据等级：** A（时序与叙述动作）／D（田对自身经历的解释）

**更准确的理解：** 入职报道→昏迷→恢复后前线；回味/回忆梦不等于重复入梦。实力提高为叙述事实，但飞蛾梦、绿色魔力与增长的机制仍未知，17他仍忆不起福利院具体细节。卡173因增长而能上前线的表述本身不另判为明确声称梦造成增长。

**可能造成的 RP 后果：** 错误追查反复施梦者，或抹去灾前在总部失踪这一经历。

**建议处理：** 后续按动作与时间修正；不把因果猜测、记忆恢复程度和入职手续混合。

## [C072] 白静萱早期的欲望迷失被统一解释成压抑情绪与怕麻烦人

**严重程度：** MAJOR

**问题类型：** 人物性格／跨阶段动机

**角色卡位置：** [ID 17](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_017.txt>)；[ID 98](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_098.txt>)

**当前内容概述：** 17称长期安静只是病弱失亲后学会不麻烦别人、情绪始终在内里累积；98虽提最初梦想但未保留欲望丧失与借用他人目标的层次。

**发现的问题：** 第17章连续叙述曾有音乐家梦想，失亲后从某时点失去欲望坐标，不知想要什么而观察和试套别人的梦想；安静因没有个人需求，非仅把强烈情绪忍住。第18章她高喊杀人却优先救人，第19章复仇模仿又与真切寻求认可并存。不能用单一休眠火山抹掉寻找自我的过程，也不能采敌人空壳辱骂判她永无感情。

**原著证据 / 定位：** [E191](01_evidence_index.md#e191)、[E202](01_evidence_index.md#e202)、[E204](01_evidence_index.md#e204)—[E209](01_evidence_index.md#e209)

**证据等级：** A（叙述轨迹、行为与选择）／D/E（七的否定性评价）

**更准确的理解：** 白有真实感激与向往，同时一度难识自己的欲望；模仿樱救人和翠惩敌产生冲突。第19战场接受母称、20醒后确认形成新联系，非一个抽象善恶直线性格即可概括。

**可能造成的 RP 后果：** RP把她永久写成压抑病娇或无情空壳，失去救人与复仇并存及重新建立自我的动机。

**建议处理：** 后续补欲望演变、物件与关系证据，保留既有感情，性格解释应服从当期叙述。

## [C073] 把真实袭局的佯攻写成局长遇袭假象

**严重程度：** MODERATE

**问题类型：** 敌方计划／实施方式

**角色卡位置：** [ID 98](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_098.txt>)

**当前内容概述：** 事件十一称残存暗子制造局长遇袭的假象以诱捕白静萱。

**发现的问题：** 第16章计划是调人实际佯攻，第18章假刘大春携兽之腑与术式媒介进入局长室，庄洋在门外接应，林在其发作前控制两人。假的是攻击重心和索要条件，不是凭假警报虚构一个完全未发生的袭击。

**原著证据 / 定位：** [E200](01_evidence_index.md#e200)、[E201](01_evidence_index.md#e201)、[E203](01_evidence_index.md#e203)

**证据等级：** A（计划和实际行动）

**更准确的理解：** 原计划以局长袭击调走少女主力、绑白后假索晶石与撤围，真实终点是带白穿荒原；实际遭林识破制止。敌人以为暗子未被发现，林早已标记，两方知识不可合并。

**可能造成的 RP 后果：** 略去刺客实际危险、林发现名册不符和两股魔力及追查通讯的推理。

**建议处理：** 后续用真实佯攻与主目标区分；若明确改成伪警报，则列USER_CONFIRMATION_REQUIRED。

## [C074] 把鸢与塞米的荒原任务会谈替换成已死兵蜂七重新布置行动

**严重程度：** MAJOR

**问题类型：** 事件主体／敌方命令链

**角色卡位置：** [ID 99｜剧情·卷2幕02·鸢来袭](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_099.txt>)

**当前内容概述：** 事件三标卷二25章，称黑烬据点中兵蜂七接白狼清单、安排暗子佯攻与五分钟缺口。

**发现的问题：** 25章实际为篝火旁鸢和塞米；七在19章已死。卡把16—19先前计划移来换主体，再把爪痕取源及带白、矢的额外任务接给七，改变生死、组织与命令传播。

**原著证据 / 定位：** [E200](01_evidence_index.md#e200)—[E207](01_evidence_index.md#e207)、[E217](01_evidence_index.md#e217)

**证据等级：** A（场景与七结局）／D（鸢受命说法）

**更准确的理解：** 主任务兽源，带白与矢的额外指令由鸢转述首领吩咐，副首领黑猫在场、塞米当时未听；塞米这只猫形妖精不是副首领黑猫。荒原没有本章据点会议或已死七复出。

**可能造成的 RP 后果：** 让死亡角色继续发令，并让敌人共享本未收到的任务，重复已结束袭击。

**建议处理：** 后续修正原著事件主体；若有意保留七存活与新据点计划，进入USER_CONFIRMATION_REQUIRED／U003。

## [C075] 唐菖蒲核查、失控与识破旧代号的顺序被倒置并附加交换口径

**严重程度：** MAJOR

**问题类型：** 身份识破／谈判知情

**角色卡位置：** [ID 99｜剧情·卷2幕02·鸢来袭](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_099.txt>)

**当前内容概述：** 事件六称先魔镜查档再失控变身，鸢凭波动和习惯认出并要求交源、白、矢才放行。

**发现的问题：** 林27末先失控离席，28变少女暂不能解除才查档；鸢闯入听兽源仍在问矢在哪，随后背后试攻逼蓝线才认出。25敌方内部带白任务并未在该次对翠谈判统一宣告为三项放行交换，不能越过传播链。

**原著证据 / 定位：** [E217](01_evidence_index.md#e217)、[E220](01_evidence_index.md#e220)—[E222](01_evidence_index.md#e222)

**证据等级：** A（动作顺序和实际对话）／D（谈判各方主张）

**更准确的理解：** 鸢在隐藏房间见翠并以蓝线认旧号，没有目睹林当面变身，尚不知男身。伤势被看出、治疗诱导与绑回计划分阶段出现；翠假动摇等援非真实投奔。

**可能造成的 RP 后果：** 向鸢泄露男身或让翠提前知道敌方要白的完整命令，改变拖延与拒绝逻辑。

**建议处理：** 后续依动作与消息接收时点纠正；无据三项放行条件列U003，不能当原著既成口供。

## [C076] 朝颜协战被压缩成直接借剪，混淆气与百武核心及持续消耗

**严重程度：** MAJOR

**问题类型：** 能力机制／战斗因果

**角色卡位置：** [ID 36｜红思与](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_036.txt>)；[ID 50｜鸢](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_050.txt>)；[ID 99｜剧情·卷2幕02·鸢来袭](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_099.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)

**当前内容概述：** 卡99事件七直接繁开借剪并称翠把剪交接过去、前后夹击；关键转折称去魔力化拆掉百武的气。卡36将五分钟直接作能力限时。

**发现的问题：** 原文红29先救、30—31先独战，五分钟复制物失败后才交剪给翠，方向不能反写；翠独持剪、红供魔维持，未给卡所述前后夹击场面。气为非魔力武道，百武核心为物理化，两次分离不同。32红说用她魔力不能抹掉33翠最后耗自身大半魔力。

**原著证据 / 定位：** [E222](01_evidence_index.md#e222)—[E230](01_evidence_index.md#e230)；[E322](01_evidence_index.md#e322)、[E330](01_evidence_index.md#e330)、[E344](01_evidence_index.md#e344)

**证据等级：** A（动作与叙述机制）／D（人物解释）

**更准确的理解：** 保留红本想独胜与临时改合作的动机；需理解机制才能分离。复制物约五分钟是当期不熟练，效果可由翠余魔维持数小时；不能泛化为剪失即效果失、气属于百武、必开奇境或无限重复复制。卡50武道背景和卡36所见所知限制本身可保留。 续审11：77回忆用魔力通窍/魔装/繁開研发武道，不推翻气本身非魔力却说明修行成果高度依赖少女力量。81红再复制剪、翠借丝剪气，88翠猜气有额外来源/用途及奇境增幅；只给此猜测C/D，不能把百武物理化、气、势、心解与奇境合成单能力。

**可能造成的 RP 后果：** 错误安排交武器和攻击分工，绕过试探获取机制的成本，永久锁定成长前限时。

**建议处理：** 后续分开忆记与繁开、复制持续与分离维持、气与物理化；新增战斗桥段若有意保留列U003。

## [C077] 把留城的敌人鸢写成正式新成员、同住并受书面队规约束

**严重程度：** MAJOR

**问题类型：** 组织成员／关系状态

**角色卡位置：** [ID 99｜剧情·卷2幕02·鸢来袭](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_099.txt>)

**当前内容概述：** 事件八称翠在基地同时介绍鸢和朝颜两名新旧成员、写下训练出勤出入与紧急中止条件，幕末有敌同住。

**发现的问题：** 34章基地只介绍朝颜，定位为非常驻、免日巡且手续之后谈。33鸢留城再挑战并未投诚或加入队伍；同城敌人不能变同住队员。24反省增加休息也未展示正式重新分配日程，卡将建议扩成制度结果。

**原著证据 / 定位：** [E215](01_evidence_index.md#e215)、[E230](01_evidence_index.md#e230)、[E231](01_evidence_index.md#e231)、[E236](01_evidence_index.md#e236)

**证据等级：** A

**更准确的理解：** 鸢是留城危险对手，39林私人救济附不杀人不毁公共设施要求；朝颜是加入方亭作重大支援的新成员，但不常驻基地、不承担一般巡逻，具体程序待办。

**可能造成的 RP 后果：** 默认敌人有基地访问和成员情报权限，生成原作未建立的团队信任与强制排班。

**建议处理：** 后续区分留城、获资助、受约束、入队与同住；额外同住及书面规则列U003待裁决。

## [C078] 妖精仙人的自称被误读为上一任播种者

**严重程度：** MAJOR

**问题类型：** 人物身份／句法转述

**角色卡位置：** [ID 99｜剧情·卷2幕02·鸢来袭](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_099.txt>)

**当前内容概述：** 事件十及出场要点把妖精仙人列为妮妮的朋友、方亭上一任播种者，并压缩培训交易。

**发现的问题：** 36原句我是方亭上一任播种者也就是妖精妮妮的朋友，上一任修饰妮妮；不能去掉句法关系改来客为前任。来客索翠个人物品作学费后被抛窗，未发生接受强化培训。

**原著证据 / 定位：** [E218](01_evidence_index.md#e218)、[E232](01_evidence_index.md#e232)、[E233](01_evidence_index.md#e233)

**证据等级：** A（原话、拒绝动作）／D（自称朋友等身份说辞）

**更准确的理解：** 按上下文是祖的圆球分身来访，孩子没有识出；前播种者为妮妮。来客提供部分袭局情报，但培训邀约被拒；其说明不能自动升级为全体认可的权威。

**可能造成的 RP 后果：** 凭空添加前任播种者履历，让孩子识破祖身份或默认接受可疑训练交易。

**建议处理：** 后续修正修饰对象、分开读者身份与孩子所知；如保留额外前任身份或拜师支线，列USER_CONFIRMATION_REQUIRED。

## [C079] 将第二次跟踪中未发送的情报和旁白行踪转成孩子的确认

**严重程度：** MAJOR

**问题类型：** 信息传播／视角

**角色卡位置：** [ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)

**当前内容概述：** 事件二写夏疏散而小璐和白击杀，之后三人追到商城、看见红临近异策局拐走并确认直接关系。

**发现的问题：** 38三人共同变身处理残兽，未给所述排他分工。短信写到途中中断、藏起、删掉，不能算通知送达。红拐研究所是旁白明确女孩不知道的事实，她们已丢目标，只计划晚下班再验证。

**原著证据 / 定位：** [E234](01_evidence_index.md#e234)、[E235](01_evidence_index.md#e235)、[E240](01_evidence_index.md#e240)；[E241](01_evidence_index.md#e241)—[E244](01_evidence_index.md#e244)

**证据等级：** A

**更准确的理解：** 把追踪失败、商场消磨时间与后续林红同来分开。至40章末小璐才看见二人，该历史时点未展开问答。 续审08：本条原截至40的尚未读质问现已推进：41夏白在基地转述目击让翠获讯，随后林在家向小璐承认局长职务并讲混有虚假编外履历的解释。小璐得知场地与局有关，不等亲眼跟踪到研究院；新的关系猜想见C083。38短信仍未送出、拐弯仍非女孩亲见。

**可能造成的 RP 后果：** 林凭不存在的短信预警，孩子获得没亲眼看见的路线与身份线索，跳过后续揭示。

**建议处理：** 后续保留已看见、推测、计划、发送成功的状态差别；具体改写路线和分工若有意保留列U003。

## [C080] 鸢后期赌博被前置到讨饭场景，并混入额外交易条款

**严重程度：** MAJOR

**问题类型：** 人物行为／交易条款

**角色卡位置：** [ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)；[ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)

**当前内容概述：** 卡100第39章塞米抱怨补助输彩票老虎机赌拳、搜身及三条底线/索白；卡101第69章也称三类都输钱。

**发现的问题：** 39实际贫困、私人食宿资助和不杀人不毁设施见旧证，未有赌博对话、搜身或第三条索白交涉。69才补出彩票老虎机耗钱，鸢却说上次赌拳小赚；不能把后期情节提前或三类统一输钱。塞米把钱称异策局给的，不因此推翻此前私人出资为正式公款补助。

**原著证据 / 定位：** [E219](01_evidence_index.md#e219)、[E230](01_evidence_index.md#e230)、[E236](01_evidence_index.md#e236)、[E237](01_evidence_index.md#e237)；[E303](01_evidence_index.md#e303)、[E313](01_evidence_index.md#e313)

**证据等级：** A（场景先后、资助与度假内心）／D（钱款称谓、输赢自述）／F（额外交涉）

**更准确的理解：** 撤回把赌博本身一概挂无据的理解：69赌博确有言行支持，73酒菜花光余款是鸢自述。仍保留39章节前置、赌拳输赢相反、搜身和索白协议无据的问题；其可变百武不能靠未发生搜身宣称全无武器。敌方获得帮助不等加入小队。

**可能造成的 RP 后果：** 前期穷困动机被后期挥霍覆盖，资金问责及白的人身交易被虚增，赌博种类的输赢也被改写。

**建议处理：** 赌博本身移出U003待证范围；错误前置和新增交涉如为有意改编保留USER_CONFIRMATION_REQUIRED，不改卡。

## [C081] 临时本体方案混入记忆复制和未经确认的时限与执行状态

**严重程度：** MAJOR

**问题类型：** 身体机制／实施状态

**角色卡位置：** [ID 36｜红思与](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_036.txt>)；[ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)；[ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)

**当前内容概述：** 卡100事件四把红写成入过渡空间须先变身者，用记忆复制16岁临时本体，称无灵魂且持续取决研究院稳定；并写已接受秘书假身份。 卡101事件六又称58为第一天就任。

**发现的问题：** 40被拦先变身的是林；临时本体由祖按本相制造，卡36外貌段亦这样写，与100记忆复制冲突。祖明确只能造无意识备用躯体，因此单写临时躯体无灵魂不能独立判错，也不能延伸为红人格无魂；真正无据的是用记忆复制及依研究院稳定决定时限。40场景中侄女、25岁天都调任仍为掩护方案，当章未展示上岗；续审09已在58确认复工，详下方分期。

**原著证据 / 定位：** [E237](01_evidence_index.md#e237)—[E240](01_evidence_index.md#e240)；[E278](01_evidence_index.md#e278)、[E279](01_evidence_index.md#e279)、[E287](01_evidence_index.md#e287)

**证据等级：** A（言行、提案与未展示执行）／D（祖的技术说明）／F（所加时限与执行细节）

**更准确的理解：** 红本体未愈拟休眠，以本相制造替身；她自愿保留16岁，改成年外貌费用本可交易覆盖。力量恢复、身体替换、临时躯体成品与秘书手续分开追；以40当章为限，不能凭未来卡摘要前置执行；后文实际状态如下。 续审09：40当时只是方案；58旁白已说明前些天治疗结束，以侄女身份由国度指派重新入职局长秘书，且数日掌握林8点到岗规律。59红称首席已治好、62筛文件实际减工作量，当前不能再写尚无上岗。卡101第一天就任仍错；制造过程、具体解除条件及额外时限仍未新增证明。

**可能造成的 RP 后果：** 让忆海百记复制自己和灵魂，错误限制生命周期，并让未办理的工作人员身份立刻生效。

**建议处理：** 后续依据实现过程再更新状态；记忆复制和额外时限列USER_CONFIRMATION_REQUIRED。保留无意识备用躯体的技术限制，不把卡未明说的无魂人格强加为其错误。

## [C082] 将红思与复归及临时本体机制一概冻结为未揭晓

**严重程度：** MODERATE

**问题类型：** 后期补充／未知范围

**角色卡位置：** [ID 36｜红思与](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_036.txt>)；[ID 99｜剧情·卷2幕02·鸢来袭](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_099.txt>)

**当前内容概述：** 卡36当前阶段称身份复归原理、临时本体与本相机制仍属未揭晓，卡99反复只说不解释复归。

**发现的问题：** 39—40已解释退役不足十年可恢复魔力源的条件、本相变异与器官损伤导致变不回、休眠本体和按本相造临时躯体的方案。具体恢复技术与完整机制仍未明，但不能把已有部分也永久封为悬念。

**原著证据 / 定位：** [E237](01_evidence_index.md#e237)—[E240](01_evidence_index.md#e240)；[E278](01_evidence_index.md#e278)、[E279](01_evidence_index.md#e279)

**证据等级：** A（说明发生、当前状态）／D（祖的机制说明）／F（完整技术与代价）

**更准确的理解：** 分开已经披露的条件、专家方案、已见力量恢复及尚未知具体手段。未重新获得国度终身资格不等没恢复魔法能力，制临时身体也不是力量复归的唯一同义表述。 续审09：58治疗结束与侄女秘书复工已出现，59本人引首席治好说法；读者已知恢复正常生活、少女外貌与任职结果，不能整体冻结未知。并未因此穷尽原本身体/备用身体的操作细节、回收魔力技术及全部长期限制。

**可能造成的 RP 后果：** NPC拒绝讨论已听过的说明、反复神秘化病因，把国度资格、力量、身体混成单一开关。

**建议处理：** 后续收窄未知范围而保留真正悬念，不凭局部解释宣称全部原理已解。

## [C083] 父职半坦白混入额外告知，并把小璐的新关系猜想换成另一条

**严重程度：** MAJOR

**问题类型：** 信息传播／误解内容

**角色卡位置：** [ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)

**当前内容概述：** 事件五称林已告知基地与研究院有关、红是新秘书，小璐转猜红喜欢翠雀爸爸，夏看出这层误会。

**发现的问题：** 41只坦白局长职务与异策局场地，同时用虚假编外履历掩空降；并未宣布红秘书任职或研究院关系。末尾明确是小璐猜翠雀喜欢安雅，没有向夏传播此猜想。

**原著证据 / 定位：** [E241](01_evidence_index.md#e241)—[E245](01_evidence_index.md#e245)

**证据等级：** A（对话、内心猜想与未传播的场景）／C（猜想的真实性）

**更准确的理解：** 真实职务、虚假履历、未告知事项与小璐私下误猜分别记录。小说没证明翠爱安雅以外的新恋爱关系；林否认恋人亦不抹掉红单方面感情。

**可能造成的 RP 后果：** 小璐获得机构秘密，夏回应未听过的猜想，父女悬念被替成无源关系。

**建议处理：** 后续按实际问答与逐人认知处理；额外披露或替换猜想若有意保留，列U003 USER_CONFIRMATION_REQUIRED。

## [C084] 生日日期误为12月24日，且忽略林主动认定的庆生日

**严重程度：** MODERATE

**问题类型：** 人物资料／关系意义

**角色卡位置：** [ID 47｜林昀](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_047.txt>)；[ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)；[ID 105｜剧情·卷2幕08·卢恩诺雷情人节](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_105.txt>)

**当前内容概述：** 卡100事件六称林把12月24日当生日；卡47称2月14日只是幼年编出的假生日、真实日未公开。

**发现的问题：** 42原文明确父亲为巧克力改称2月14日，成年林仍认定这一天是自己与父亲共度的生日。卡47保留真实登记日未知有据，但只是假的概括抹去了当下认定，且不应让读者误以为改日期由幼年林自己决定。

**原著证据 / 定位：** [E248](01_evidence_index.md#e248)；[E421](01_evidence_index.md#e421)、[E424](01_evidence_index.md#e424)、[E425](01_evidence_index.md#e425)

**证据等级：** A（当下认定与明确日期）／D（童年自述）／F（真正登记日）

**更准确的理解：** 区分未披露的登记生日、父亲改称的日期、林自己坚持的庆生日；2月14日可用于这段关系的庆生，不等客观出生日期已确定。 续审14：134—135再明确实际出生日非14，蜡烛实际扫描魔活性误触。小白从不知翠生日变相信与林同日，夏装惊讶；翠接受庆日不等真实登记日已查明。

**可能造成的 RP 后果：** RP拒绝为林按2月14日庆生，或用12月24日替换父亲巧克力故事。

**建议处理：** 后续纠正日期和改称主体，保留真实登记日未知；不要擅自补造出生日期。

## [C085] 静止八音盒被改成播放旋律，改变创伤回忆的触发链

**严重程度：** MAJOR

**问题类型：** 事件因果／心理触发

**角色卡位置：** [ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)

**当前内容概述：** 事件六写商店八音盒播放熟悉旋律，从而让白回忆父母与敌方话语。

**发现的问题：** 原盒没有上发条、静止无声，白只看相似物并拒绝新礼物；车中再主动回应问题讲旧盒。敌人哼同曲属于她解释为何相信敌方的往事，不能移到商店作当场声音刺激。

**原著证据 / 定位：** [E246](01_evidence_index.md#e246)、[E247](01_evidence_index.md#e247)

**证据等级：** A（静物与谈话顺序）／D（白的记忆、敌人说法）

**更准确的理解：** 分别保存相似物、旧物丢失、车中自发转述和往事哼曲；敌方曲子与旧盒相同增强她的信念来源，不证明对她身世的全套污名指控。

**可能造成的 RP 后果：** 模型凭任何音乐强行触发失控或心理反应，林提前获知完整研究员情报。

**建议处理：** 后续修正触发与转述时点；改成当场播放若有意保留，列U003 USER_CONFIRMATION_REQUIRED。

## [C086] 独巡援助被改作集体遭遇，并将魔装击杀写成术式

**严重程度：** MODERATE

**问题类型：** 战斗主体／能力类别

**角色卡位置：** [ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)

**当前内容概述：** 事件八写小璐一行巡查遭兽、金发少女用极快术式击杀。

**发现的问题：** 44小璐独巡，木到场支援；白摩可的眼镜少女目击是另处同日下午发生、45才对照。木明确唱名魔力构装析出与闪光小弹腿，以轮鞋魔装击杀，非术式。

**原著证据 / 定位：** [E252](01_evidence_index.md#e252)—[E254](01_evidence_index.md#e254)

**证据等级：** A（动作、析出、分头目击）／D（木判断小璐苦战）

**更准确的理解：** 保留分头见闻与晚上汇总；木错估小璐耗竭不能充作实力结论，小璐模拟屏障也不意味着已晋叶。

**可能造成的 RP 后果：** 全队获同一现场知识，木技能类别与小璐当期成长状态失真。

**建议处理：** 后续按真实主体现身和魔装表现处理；集体遭遇若有意保留，列U003 USER_CONFIRMATION_REQUIRED。

## [C087] 玛格丽特告别被前移七年，离队选择被压成单一旧怨

**严重程度：** MAJOR

**问题类型：** 人物动机／关系发展／回忆时间

**角色卡位置：** [ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)；[ID 53｜玛格丽特](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_053.txt>)

**当前内容概述：** 卡100事件九把告别称二十年前，歌声概括为把婚姻排除的旧怨唱给全场。卡53另有旧队情谊和自尊等人物描述。

**发现的问题：** 46明确最后告别定格十三年，林安已婚两年、小璐一岁多；同时写理性规划个人前途、对团体失落、祝福与友情。用婚恋败者的单一怨恨框架覆盖全段，会丢失自主选择。

**原著证据 / 定位：** [E256](01_evidence_index.md#e256)、[E257](01_evidence_index.md#e257)；[E262](01_evidence_index.md#e262)、[E263](01_evidence_index.md#e263)、[E267](01_evidence_index.md#e267)—[E269](01_evidence_index.md#e269)、[E276](01_evidence_index.md#e276)、[E285](01_evidence_index.md#e285)；[E301](01_evidence_index.md#e301)；[E328](01_evidence_index.md#e328)、[E346](01_evidence_index.md#e346)、[E347](01_evidence_index.md#e347)；[E352](01_evidence_index.md#e352)、[E359](01_evidence_index.md#e359)、[E360](01_evidence_index.md#e360)、[E370](01_evidence_index.md#e370)

**证据等级：** A（回忆、台词、相对时间）／D（玛自述）／E（林理解表情）

**更准确的理解：** 旧怨、不甘确有依据，你没选我原话与歌词回响也真实存在，不整段判虚构；但不能据此确定她仅为未被选作恋人离开或演唱会只为复仇。初识与离队分期。 续审09：49玛解释舞台邀请为重逢纪念、不愿辜负歌迷，并为估错翠感受致歉；52以专辑履行和安雅最后通话的旧约、61以为你效劳表达保护。非仅自恋或追恋复仇，也不能升级成她永不误判：56亲认自己把小璐当孩子哄，转而认真致歉。 续审10：她先按导师学生公事公办，不知白蓟依恋强度；翠分析后才意识到并抱着道歉。卡53含真实和解，不整体否定；但永不居高临下/总能准确理解后辈不能绝对执行。 续审11：80叙述情热早期受情绪支配会敌治我伤，她经管理情绪而由直口自夸辱骂转含蓄自夸/阴阳怪气；不能把早期直率原样锁到后期，也不把苏渣男化玩笑当恋爱事实。89对祭子及白的风险既有同情也有偏见警觉，仍会因友人自我燃尽而难过并邀其共看烟花。 续审12：92玛愿做东瀛午餐、久违无助理生活而放松，同时仍不喜束缚；翠清楚二人只适合挚友。95争宠建议并非专业，96让后辈自己解争执，100仍会教训木，并借她家事反问谎言保护。不得固化成永不干预或永远准确读心。

**可能造成的 RP 后果：** 把旧友归属感与职业选择简化为败恋报复，混淆小璐出生前后和旧队变迁。

**建议处理：** 后续保留多重动机及十三年锚点；单义恋爱路线如为设计另挂U007，额外改写挂U003 USER_CONFIRMATION_REQUIRED。

## [C088] 后台场景虚增红思与到场，并把工作人员制服当柏安队服

**严重程度：** MAJOR

**问题类型：** 场景人员／信息来源

**角色卡位置：** [ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)

**当前内容概述：** 事件十写三人穿黄色队服，红思与察觉队服和花牌不是演出道具；小璐在走廊直接认出刚清理残兽的人。

**发现的问题：** 46—48同行是翠与三后辈，未有红；黄色T恤明示工作人员制服。47小璐和木只觉得脸熟，48散场由翠介绍两市后小璐才喊黏液洗澡，残兽战发生在之前的放学日。

**原著证据 / 定位：** [E255](01_evidence_index.md#e255)、[E258](01_evidence_index.md#e258)、[E260](01_evidence_index.md#e260)、[E261](01_evidence_index.md#e261)；[E263](01_evidence_index.md#e263)、[E265](01_evidence_index.md#e265)、[E279](01_evidence_index.md#e279)

**证据等级：** A

**更准确的理解：** 分别记录舞台额吻、散场主动去后台、保安依玛指令放行、翠识柏安学生和各人逐步确认。额吻本在卡53，不报整卡全无；49吻手及正式派驻尚待读。 续审09：49吻手真实发生，50自报职衔及临时协商支援已证，旧条尚待读只指48时点。59红抗议大家去演出而自己双休日值班，直到办公室才知道玛归来，直接补强原未在现场；仍保持额吻/吻手分场，不因前面摘要错误否认后面真实礼节。

**可能造成的 RP 后果：** 红获得未在场的信息，演出服被当组织识别证据，提前关闭学生认人过程。

**建议处理：** 后续删改应按原场景人员与辨认顺序；若刻意让红同行或改队服，列U003 USER_CONFIRMATION_REQUIRED。

## [C089] 私定比试门槛被写成正式认证初试与取消资格权限

**严重程度：** MAJOR

**问题类型：** 制度权限／状态变更

**角色卡位置：** [ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)；[ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)

**当前内容概述：** 卡100事件十二称正式资格初试，输了明年资格将取消；卡101沿用输掉就没有资格。

**发现的问题：** 50只是玛提希望不参加，51明确她不是考官且翠质疑正当性；54两导师才共同暂定门槛，62又明确取消输赢约束。不是国度已设的正式初试或取消资格程序。

**原著证据 / 定位：** [E265](01_evidence_index.md#e265)、[E266](01_evidence_index.md#e266)、[E272](01_evidence_index.md#e272)、[E273](01_evidence_index.md#e273)、[E286](01_evidence_index.md#e286)；[E291](01_evidence_index.md#e291)、[E296](01_evidence_index.md#e296)、[E302](01_evidence_index.md#e302)；[E013](01_evidence_index.md#e013)、[E296](01_evidence_index.md#e296)、[E302](01_evidence_index.md#e302)

**证据等级：** A（约定及撤销）／D（初试比喻和消息）

**更准确的理解：** 保留提出→质疑→两导师同意→公开取消的顺序；正式比试仍保留但结果不限制是否参考。续审09仅读至62时只约未来抽签；现行赛制和结果由续审10补明如下，认证退出不因私人比试规则而获得普适制度证明。 续审10：64已实际抽签并由摩可宣读失能/出界/认输及专项规则，68方亭2比1；认输的现场规则不自动等于已宣读任意时点取消认证的制度。将旧句62时赛制待核视为历史状态，现由本补证更新。 第一阶段收尾：全文结束仍不把私比认输规则扩成认证任意退出制度；后期停考指令、被敌方结界阻挡与积分结算分属C016/M011/M041。旧完整制度待核仅是历史进度。

**可能造成的 RP 后果：** NPC把导师提议变不可撤销制度，或在取消后继续拒绝角色参考。

**建议处理：** 后续按权限与时点处理；若有意设官方初试则列U003 USER_CONFIRMATION_REQUIRED。

## [C090] 入国度知情与一年支援被前置，并附加旧队共同决策规则

**严重程度：** MAJOR

**问题类型：** 信息传播／合作承诺

**角色卡位置：** [ID 100｜剧情·卷2幕03·演唱会与旧友](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_100.txt>)；[ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)；[ID 53｜玛格丽特](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_053.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)

**当前内容概述：** 卡100第52及幕末已写留一年、玛知道假身份疗伤；卡101第61增加任何下一步必须同伴知情、不再个人决定生死的队规。

**发现的问题：** 52玛尚不知具体来袭者，60才惊讶地听入国度计划，61才提如有必要留一年请假。61坦白动机和愿意支援不等已经订立全队审批下一步的强制新规则。

**原著证据 / 定位：** [E269](01_evidence_index.md#e269)、[E282](01_evidence_index.md#e282)、[E285](01_evidence_index.md#e285)、[E286](01_evidence_index.md#e286)；[E349](01_evidence_index.md#e349)、[E352](01_evidence_index.md#e352)、[E366](01_evidence_index.md#e366)、[E367](01_evidence_index.md#e367)

**证据等级：** A（告知及提议）／D（条件承诺）／F（新增共同审批规则）

**更准确的理解：** 两人知情不同：红早从祖听过，玛60才知；49效劳在61被解释为真心，尚非52已经落实一年驻留。62后辈仍不知道伪装和治疗目的，当前阶段人物概览须按所选时点调用。 续审12：90谈深入盟约、祖自称猫眼同价；92假宝石已给、登记还有待办，一年后龙胆战死仍方案，98衣装才录入。新衣照片的看见不等孩子已听疗伤、伪证、政治交换；柏安三人还晚到，不能以全员拍照同步机密。

**可能造成的 RP 后果：** 玛提前阻拦未听到的计划，后辈共享秘密，强制队友批准每项行动。

**建议处理：** 后续按首次获知和承诺条件拆分；额外共同决定规则列U003 USER_CONFIRMATION_REQUIRED。

## [C091] 魔力球失败被追加为几乎维持不住变身

**严重程度：** MODERATE

**问题类型：** 战斗效果／能力解释

**角色卡位置：** [ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)

**当前内容概述：** 事件一写球接触后浊化打散，小璐整个人几乎无法维持变身。

**发现的问题：** 55魔力反馈令球两秒内崩，小璐呆站，主动解除变身是白蓟；66/67后文明确这次私比使用浊化，却没有补写小璐本体濒崩。66夏实际脱力解除变身是另一人另一场。

**原著证据 / 定位：** [E271](01_evidence_index.md#e271)、[E274](01_evidence_index.md#e274)—[E276](01_evidence_index.md#e276)；[E296](01_evidence_index.md#e296)—[E298](01_evidence_index.md#e298)

**证据等级：** A（球败、回述浊化与不同比赛结果）／C（55体验解释）／F（小璐濒解除）

**更准确的理解：** 浊化名称和实际使用已获后文支持，撤去名称本身待核状态；55小当时未知，66夏/翠也先不知，不能让读者晚得机制倒灌早期人物。球崩、感知反馈、本体维持仍分开。

**可能造成的 RP 后果：** 把专项失利扩为形体瓦解，战术代价和伤害阈值凭摘要新增。

**建议处理：** 保留C091主问题；技巧名称不列原创，额外濒失变身若要保留仍挂U003。

## [C092] 楼梯道歉对象被写反，导师提议又被改成学生失言

**严重程度：** MAJOR

**问题类型：** 关系修复／责任归属

**角色卡位置：** [ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)

**当前内容概述：** 事件二写白蓟楼梯向小璐道歉，玛解释自己措辞令学生把测实力误成决定资格。

**发现的问题：** 54楼梯受歉者是翠，白蓟说完离开，并未向小璐和解；玛只说弟子挑事已教训。50禁考希望本由玛提出、51自行比作初试；53白蓟区分老师原话和自己的保护动机推测，不能把条件源头转嫁学生。

**原著证据 / 定位：** [E265](01_evidence_index.md#e265)、[E266](01_evidence_index.md#e266)、[E271](01_evidence_index.md#e271)、[E273](01_evidence_index.md#e273)、[E286](01_evidence_index.md#e286)；[E298](01_evidence_index.md#e298)、[E301](01_evidence_index.md#e301)、[E302](01_evidence_index.md#e302)、[E308](01_evidence_index.md#e308)

**证据等级：** A（对象与原话归属）／D（白蓟动机推测）

**更准确的理解：** 白蓟私比挑衅与玛提出参考门槛是两项责任。62两学生仍不交谈，不能假设54已完成和解。 续审10：67知玛批评信息差与规则漏洞并命向方亭队歉；68师生关系获修复，71林回顾两学生比试后暂和解。62仍不交谈为历史，不继续当现状；暂和解不等54已向小道歉或两人挚友。

**可能造成的 RP 后果：** 提前抹掉矛盾，白蓟承担导师说过的限制，翠凭未发生的道歉推断双方关系。

**建议处理：** 后续修正接收者和责任来源；替代和解桥段列U003 USER_CONFIRMATION_REQUIRED。

## [C093] 教学提案章被扩成已实施的完整私课与保密协议

**严重程度：** MAJOR

**问题类型：** 事件阶段／教学内容

**角色卡位置：** [ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)

**当前内容概述：** 事件四把56放在训练场，写复述失败、脚步预兆训练、浊化说明和不向白蓟公开的约定。

**发现的问题：** 56阳台末仅提学两手、57确认接受；66小忆约三天学成浊化，67回忆与玛讨论过二次浊化，68翠观察基础控制、预判和动作进步。因此具体技巧与教学不再全未知，但不证明卡写的56训练场复述失败和订保密约定发生。

**原著证据 / 定位：** [E275](01_evidence_index.md#e275)—[E277](01_evidence_index.md#e277)、[E287](01_evidence_index.md#e287)；[E297](01_evidence_index.md#e297)、[E299](01_evidence_index.md#e299)、[E301](01_evidence_index.md#e301)、[E302](01_evidence_index.md#e302)

**证据等级：** A（学成、讨论与进步）／D（玛一般技术结论）／F（未见完整私课对白及保密协议）

**更准确的理解：** 提案→接受→实际学成→旁观者得知分期。白蓟赛前不知及玛赛前藏招不等双方签过所写保密协议；68玛视技巧半公开且传多人，不能造封闭传承。小未晋级、焦虑暂淡不等一次课程彻底治好。

**可能造成的 RP 后果：** 小璐提前掌握未教授技巧，NPC执行无源保密承诺，焦虑被一堂虚构课强行治好。

**建议处理：** 从U003撤去浊化教学本身和已证二次浊化讨论；保留56前置/增写课程细节及保密协议待裁决。

## [C094] “毫无天赋”的比较性概括可能被执行为资质全无

**严重程度：** POTENTIAL RISK

**问题类型：** 人物评价／措辞边界

**角色卡位置：** [ID 53｜玛格丽特](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_053.txt>)

**当前内容概述：** 人物条目反复以引号内毫无天赋、无天赋者概括玛，强调技巧成就。

**发现的问题：** 57旁白实际描述魔量不出众、能力普通、术式学习不好不坏；无天赋是玛相对旧队天才的自我说法。原卡引号也可能表达这种修辞，因此不判已经明说她全部资质为零，但执行时有字面化风险。

**原著证据 / 定位：** [E277](01_evidence_index.md#e277)；[E297](01_evidence_index.md#e297)、[E301](01_evidence_index.md#e301)

**证据等级：** A（普通资质和技艺花牌叙述）／D（自评）／F（角色卡实际执行是否字面化）

**更准确的理解：** 普通资质与坚持走向技艺极致不冲突。花牌为某领域极致追封，不能将她的谦贬句充作剥夺所有资质或低智能的机制。续审09时浊化创制细节尚未核；续审10已由下列新增证据补明。 续审10：玛称十几年牵头与同僚完善浊化，且曾教多人；技艺成就已有具体支持，不再待核名称。仍不将毫无天赋修辞判成卡已明说所有资质为零，具体研发时间和合作者见C102。

**可能造成的 RP 后果：** 人物的学习能力被错误压低，普通人的长期专研被改成无任何能力仍凭意志升级。

**建议处理：** 后续明确比较对象与修辞来源；保留作为语言特色的可能，不把所有无天赋措辞一概删除。

## [C095] 苏胜紫失联十二年的口径被改为九年及自行历年

**严重程度：** MODERATE

**问题类型：** 失踪时间／调查边界

**角色卡位置：** [ID 7｜往事编年](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_007.txt>)；[ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)；[ID 161｜旧方亭市小队](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_161.txt>)；[ID 126｜间界](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_126.txt>)

**当前内容概述：** 卡101事件六称九年前独入间界；卡7定1990—91，并说名单无名。

**发现的问题：** 59玛明称最后联系十二年前、恰为退役离方亭时；不是九年前。60排查无名只支持尚无证据，玛承认从不在物质界活动者可能查不出，不等已证明没有入爪痕。

**原著证据 / 定位：** [E280](01_evidence_index.md#e280)、[E281](01_evidence_index.md#e281)；[E415](01_evidence_index.md#e415)；[E280](01_evidence_index.md#e280)

**证据等级：** A（当前对话）／D（玛回忆与调查）／C（入爪痕猜测）

**更准确的理解：** 依来源保存十二年自述及满十年退役背景，若与别处年代产生张力另查，不用卡自行年份修源。林红此时才得去间界消息，暂假设安全、准备后去找而非已行动。 续审14：卡161卷一状态也写苏约九年前赴间界；同一错误回接本号，127旧巧克力高中记忆不提供九年失联依据。 续审18：新完整读卡126亦把苏离国写九年前，应与E280玛十二年前最后联系口径同修；保留最后联系/退役/说去间界而非独立确切抵达日。

**可能造成的 RP 后果：** 把未知失踪史补成确定时间表，或依据名单将可能性彻底排除。

**建议处理：** 后续修正摘要口径，保留可再核的相对年数；疑似自定历年挂U001，不擅定苏生死阵营。

## [C096] 丝线打结的推论被升级为本相受侵蚀与男身将消失的证明

**严重程度：** MAJOR

**问题类型：** 后遗症／推断升级

**角色卡位置：** [ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)

**当前内容概述：** 事件七及幕末称副作用已开始侵蚀/逼近本相，失控证明继续等可能令林身份彻底消失。

**发现的问题：** 60只是再次非自愿男转女，翠还明确单此不足以冒险；61线结目前不妨碍战斗，他推本相影响魔装且将来或出新副作用，命运不祥的联想没有说出口。没有给出本相已被侵蚀或男身必/将消失的验证。

**原著证据 / 定位：** [E283](01_evidence_index.md#e283)、[E284](01_evidence_index.md#e284)、[E285](01_evidence_index.md#e285)；[E389](01_evidence_index.md#e389)、[E392](01_evidence_index.md#e392)

**证据等级：** A（失控、结与无目前使用障碍）／D/C（风险分析）／F（最终病因及走向）

**更准确的理解：** 保留实际新症状、翠对未知的焦虑与抢回主动权动机；不把理由改成已证濒亡倒计时。复原技术承诺、毁魔装死亡风险与自动变身是不同命题。 续审13：107说明前置疗程已止魔溢，108修复后祖正式警告再献祭会使林昀消失；这一后来的有条件风险不反证63丝结当时已证明男身濒消。当前已能无痛施丝/奇境，稳定前不宜繁开，病因链与再损危险分开。

**可能造成的 RP 后果：** NPC依无证病理逼迫立即治疗，窥知未说出口的命运隐喻，提前锁死身体结局。

**建议处理：** 后续保持现象/自述/推论/未知分层；额外病理机制列U003 USER_CONFIRMATION_REQUIRED。

## [C097] 寻求祖母绿帮助的犹豫被改成明确拒绝研究院试验

**严重程度：** MAJOR

**问题类型：** 动机／选择状态

**角色卡位置：** [ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)

**当前内容概述：** 事件五写林明确反对把女儿交研究院试验，论证治疗不等安全制造觉醒。

**发现的问题：** 57玛只是建议找首席，林反而直觉可能得解；他犹豫因女儿与国度牵连、宝石权杖及自己本应蓝宝石的旧事，结论是会考虑、非万不得已先自己试。没有提出交研究院试验的具体方案或那段拒绝实验论证。

**原著证据 / 定位：** [E277](01_evidence_index.md#e277)

**证据等级：** A（内心与答话）／D（玛建议和评价）／C（可解决的直觉）

**更准确的理解：** 尚未决定求助，不等明确拒绝；保护过度、旧身份风险与专业能力未知并存，不能凭审计者价值判断代写育儿宣言。

**可能造成的 RP 后果：** 关闭本来仍开放的求助路线，或给祖增加当时未提出的实验要求。

**建议处理：** 后续保留犹豫与条件选择；拒绝实验桥段若为改编列U003 USER_CONFIRMATION_REQUIRED。

## [C098] 第66章比试被替换成桥上退役谈话与十年承诺

**严重程度：** MAJOR

**问题类型：** 原创场景／关系承诺

**角色卡位置：** [ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)

**当前内容概述：** 事件十三标66章桥面：小诉复仇恐惧想退役，翠承诺五年十年直到后辈退役、握手说相信你。

**发现的问题：** 66全文是夏爆炸对含羞、夏认输、小赛前紧张获场边鼓励、对球及浊化说明，没有离场上桥和所写长期承诺。68/71/72关系焦虑仍未解决，不能把关系保证和退役自由对白凭空完成。

**原著证据 / 定位：** [E295](01_evidence_index.md#e295)—[E297](01_evidence_index.md#e297)、[E302](01_evidence_index.md#e302)、[E308](01_evidence_index.md#e308)—[E312](01_evidence_index.md#e312)；[E295](01_evidence_index.md#e295)—[E297](01_evidence_index.md#e297)、[E308](01_evidence_index.md#e308)—[E312](01_evidence_index.md#e312)

**证据等级：** A（所标章节完整内容）／F（卡中具体十年承诺的对应原著依据）

**更准确的理解：** 保留真正的场边鼓励：展示进步和不足，不必拘泥胜负。审计只否定此处具体场景与承诺映射，不据此断言原著其他阶段从不讨论退役。 第一阶段收尾：源文100%后仍仅判定卡所标66章具体场景、十年承诺和前置的关系保证没有对应依据；不会以此否定原著其他阶段真实出现的退役讨论。未读后文的旧措辞停止作为当前状态。

**可能造成的 RP 后果：** NPC履行无源十年义务，小的依恋焦虑被提前解决且亲情弧改写。

**建议处理：** 具体桥段若有意增写列U003 USER_CONFIRMATION_REQUIRED；后续若有相似原情节回接本ID。

## [C099] 二次浊化操作者被写反，穿透命中被改成直接耗尽魔力

**严重程度：** MAJOR

**问题类型：** 行动主体／战斗因果

**角色卡位置：** [ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)

**当前内容概述：** 事件十四写白蓟尝试再次浊化、白魔恢复并直接耗尽她魔力。

**发现的问题：** 67二次操作的是林小璐，蓝焰先平复再褪白；白蓟只回忆自己曾尝试而当下继续攻击。68她先榨干魔力备防，白魔穿过后击中，不是证实吸魔效果。卡70相应能力段反而写对，构成同卡冲突。

**原著证据 / 定位：** [E299](01_evidence_index.md#e299)、[E300](01_evidence_index.md#e300)；卡70与101事件十四

**证据等级：** A（动作、先后及命中）／F（未证吸魔机制）

**更准确的理解：** 小主动复现白魔是一次成长；能穿当场术式/屏障/魔装与所有防御永远无效不同。不能从白蓟耗竭结果造抽蓝、按防御强度扣蓝或反浊化规则。

**可能造成的 RP 后果：** 攻防双方技能被互换，白魔增加原著未证的吸能能力。

**建议处理：** 后续按源文校正主体与因果；如有意设计吸魔规则另挂U003，当前不改卡。

## [C100] 白蓟对导师话语的误解被写成导师亲口否定期待

**严重程度：** MAJOR

**问题类型：** 人物认知／引语归属

**角色卡位置：** [ID 70｜白蓟](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_070.txt>)

**当前内容概述：** 阶段二称听见导师说不曾期待她获胜后哭。

**发现的问题：** 68玛实际说没有失望、并不责怪；白蓟哭着认为从未被期待，翠随后解释这些话听起来像我没看好。卡70把听者解读改成导师原话，而卡101写误以为，互相矛盾。

**原著证据 / 定位：** [E301](01_evidence_index.md#e301)

**证据等级：** A（实际台词与反应）／D/E（误解及翠解释）

**更准确的理解：** 玛忽略她的依恋是真的，后来真诚道歉也是真的；不能为强调伤害而添加导师蓄意贬低原话。

**可能造成的 RP 后果：** 师生误解被改成导师明确羞辱，道歉原因与人物性格变质。

**建议处理：** 保留误解→翠分析→玛意识到→抱歉的链；若保留改写对白列U003。

## [C101] 夏凉术式教学被追加只为此场使用一次的承诺

**严重程度：** MODERATE

**问题类型：** 选择范围／能力发展

**角色卡位置：** [ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)

**当前内容概述：** 事件十称夏以只为这场比试准备一次接受限制。

**发现的问题：** 63夏谈实用浅学与可能深入，65回忆承诺不丢修魔，66说明组合技建议及数日雏形；没有将术式研发或使用限制为一次比试的对白。

**原著证据 / 定位：** [E288](01_evidence_index.md#e288)、[E289](01_evidence_index.md#e289)、[E294](01_evidence_index.md#e294)—[E296](01_evidence_index.md#e296)

**证据等级：** A（选择与回忆对白）／D（教学提醒）

**更准确的理解：** 为眼前比试调整学序不等承诺比赛后放弃；爆炸首次当众使用也非终生一次性技能。翠对性价比/开华的教学意见不升级为术式一律禁止深研。

**可能造成的 RP 后果：** 后续成长被无源一次约束截断，混淆一次展示、禁忌一次性爆发和长期训练。

**建议处理：** 保留时间投入权衡，增写承诺列U003；不否定65已补出的真实爆炸课程。

## [C102] 浊化独创简称与早期阶段可能遮掉共同研发的时效

**严重程度：** POTENTIAL RISK

**问题类型：** 来源归属／阶段调用

**角色卡位置：** [ID 2｜魔法少女体系](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_002.txt>)；[ID 53｜玛格丽特](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_053.txt>)

**当前内容概述：** 卡2/53称麻生自创，53阶段一少年至1979后也写以死磕创造浊化。

**发现的问题：** 66玛说明十几年由她牵头和调查院同僚完善，翠原活跃期没见过；68玛视已教多人半公开。自创可以是牵头简称，不据此判卡明说无合作者；风险是早期阶段直接给成熟浊化或把技巧写成绝不外传。

**原著证据 / 定位：** [E297](01_evidence_index.md#e297)、[E301](01_evidence_index.md#e301)

**证据等级：** A（翠此前未知及当场获知）／D（玛研发/传播口径）／F（确切发明年份）

**更准确的理解：** 保留牵头、共同完善、成熟教学及各人学成的不同阶段；精确首创年份仍未知。一般二次无收益也留适用范围，不覆盖小的异常。

**可能造成的 RP 后果：** 早年NPC掌握后来才完善技巧，其他研究者贡献或传播历史被抹去。

**建议处理：** 继续核后文研发资料，仅标潜在阶段风险；不把简称本身一概判错。

## [C103] 白狼按真处理未核实的报告被升级为完全确认

**严重程度：** MODERATE

**问题类型：** 情报可信度／任务沿革

**角色卡位置：** [ID 101｜剧情·卷2幕04·备战与比试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_101.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)

**当前内容概述：** 69幕末写白狼知道兽源在祖手中，事件十五把抓翠与白称改令。

**发现的问题：** 69白狼追问是否借势骗人、具体转手运输，鸢承认没确认可靠性，只凭翠说及查无气息。白狼最后就当真的处理；抓人原已属任务，变化是兽源旁落后剩余目标及十万市民手段，非此前完全无抓人任务。

**原著证据 / 定位：** [E217](01_evidence_index.md#e217)、[E305](01_evidence_index.md#e305)；第25章旧任务见现有S010/M014；[E318](01_evidence_index.md#e318)、[E331](01_evidence_index.md#e331)、[E343](01_evidence_index.md#e343)、[E344](01_evidence_index.md#e344)；[E348](01_evidence_index.md#e348)、[E375](01_evidence_index.md#e375)

**证据等级：** A（报告和命令）／D（当事人确认程度）

**更准确的理解：** 读者据既有交易知道事实，不等白狼独立核实。她可以在假设可信时下令；鸢报告用真实局部掩盖度假，听者仍不知道真正拖延理由。 续审11：81翠已借回兽源当探测器，鸢当场见到才获新状态；不让白狼自动同步、不倒推69报告骗人。75改案及88完整内因显示鸢避免无谓屠杀、仍图掳人并保留向首领交代的策略；69低头领命保留为当期行为，现不能再说后续是否改案全未知。 续审12：90兽源实际归祖；午餐幕间白狼自称经线人考证且数日前转运卢恩诺雷，知情口径已由69暂按真推进到自称确认，原69判断仍成立于当时。转运是其报告D，长期不移/不告女王是预测；黑猫三人抢夺只是新命令，未执行完成。

**可能造成的 RP 后果：** 敌方无依据获全知，任务动机发生时间重写，后续侦查和欺瞒空间被提前取消。

**建议处理：** 后续区分收到/暂信/确认；命令已出口但尚未实行，不凭本段预判鸢后续选择。

## [C104] 把红思与的杯量误判写成玛格丽特确认翠雀生命极差

**严重程度：** MAJOR

**问题类型：** 能力读数／认知归属

**角色卡位置：** [ID 53｜玛格丽特](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_053.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)

**当前内容概述：** 卡53称玛从翠雀近底酒液判断其生命状态极差。

**发现的问题：** 80实际由红因杯浅而担心，并把自己超过半杯倒入；翠杯仅升一薄层，随后解释相对普通少女没那么糟。不同容量下的比例不能直接等同生命濒危，发判断的人也被换掉。

**原著证据 / 定位：** [E325](01_evidence_index.md#e325)、[E329](01_evidence_index.md#e329)

**证据等级：** A（倒杯与说明发生）／D/E（担忧和相对判断）

**更准确的理解：** 翠仍有真实伤势、耗魔与疼痛；应保留绝对魔量和自身剩余比例之别，不能由纠正过度担忧反判已痊愈。

**可能造成的 RP 后果：** NPC据错误血量读数强制濒死状态，误写玛的诊断可靠性。

**建议处理：** 后续分开可见读数、红误判、翠解释；只修审计不改卡。


## [C105] 情热繁开与奇境的叠加条件被合并成单一步骤

**严重程度：** MAJOR

**问题类型：** 能力机制／前置条件

**角色卡位置：** [ID 53｜玛格丽特](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_053.txt>)；[ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)

**当前内容概述：** 卡53称繁开酌情热醉会展开酒吧奇境，每个人本相映成杯；102也将领域直接归于繁开。

**发现的问题：** 80先繁开又同步展开奇境，81进一步明确繁开控制杯内情绪、配合奇境才把本相映射给他人。省略双层条件会把单独繁开当成自动全域他人状态控制。

**原著证据 / 定位：** [E328](01_evidence_index.md#e328)—[E330](01_evidence_index.md#e330)、[E344](01_evidence_index.md#e344)

**证据等级：** A（分次展开与实战）／D（规则解释）

**更准确的理解：** 无需敌人真饮酒亦可干预；情绪控制持续受目标魔量影响。屋顶被切破不等规则解除，88失魔后奇境消散是另一事件。

**可能造成的 RP 后果：** 任意场景开繁开即全场控制，忽略目标、持续与对抗条件。

**建议处理：** 第二阶段分别表述魔装、繁开、奇境和组合；本阶段不补未证规则名或极限。


## [C106] 鸢叛逃被简化成败给兽力后认可强者随行

**严重程度：** MAJOR

**问题类型：** 身份转变／多重动机

**角色卡位置：** [ID 50｜鸢](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_050.txt>)

**当前内容概述：** 卡50阶段一称败于紫钻暗用兽力，反而视作强者证明并随之叛逃。

**发现的问题：** 77—78写她仍想保身份研究、拒绝叛逃，紫钻决斗违规后又带看被迫退役者；她理解不同人的诉求，才参与大规模逃亡。仅败服强者替代研究中断之惧、同类处境与后续说服，取消了真实选择过程。

**原著证据 / 定位：** [E321](01_evidence_index.md#e321)—[E323](01_evidence_index.md#e323)

**证据等级：** A（回忆与行动）／D（诉求）

**更准确的理解：** 旧证中她自述白狼凭新力量击败自己有依据，不能反向全判虚构；新叙述使其成为动机之一而非充分因果。她仍对后来组织暴行负有参与责任。

**可能造成的 RP 后果：** 武痴被扁平化为只认强弱、对同类全无情感，也混淆早期家园与后期仇国派。

**建议处理：** 保留旧简述来源及新增回忆，分开决斗、参访、决定和后来派系变化；有意简化路线挂U003。


## [C107] 银屏山心解耗尽被提前到第81章并重复结算

**严重程度：** MAJOR

**问题类型：** 战斗状态／时间错序

**角色卡位置：** [ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)

**当前内容概述：** 事件十一标第81章，却写半杯直到分层消失、百势成武终于磨空；事件十五第88章又结算一次。

**发现的问题：** 81只首次掉层并让六新人突破；84仍半杯且战斗继续，88才分层消失、心解失效。把终局结果塞入81会让后续持续心解与当前状态矛盾。

**原著证据 / 定位：** [E331](01_evidence_index.md#e331)、[E335](01_evidence_index.md#e335)、[E343](01_evidence_index.md#e343)

**证据等级：** A

**更准确的理解：** 79怀疑→81试验受伤掉层→84叙述确认不可逆机制/半杯→88心解耗尽→另开奇境退走，按阶段写。六人共同突破后82才分流，不能只给夏白蓟突围功劳。

**可能造成的 RP 后果：** 敌人过早失去心解后又无因恢复，后续受伤、破塔和认输因果被重复触发。

**建议处理：** 修复分阶段索引和当前能力状态；历史问题保留，不合并删掉细微区别。


## [C108] 卷二第85章被不存在的第二祭子回溯替换

**严重程度：** MAJOR

**问题类型：** 跨卷串写／虚构场景

**角色卡位置：** [ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)

**当前内容概述：** 事件十三称卷二85插入湖畔春天金纹首领认第二祭子、被夏凉蓝冲击击杀的延迟回溯。

**发现的问题：** 连续全文显示该章实为含羞探索、小璐与塞米恶战及王钥首次析出，没有这段回溯。相近兵触三情节属于卷一85，且凶手是翠雀（C036），不能用旧事件跨卷移植为此处真实叙述。

**原著证据 / 定位：** [E336](01_evidence_index.md#e336)、[E337](01_evidence_index.md#e337)；[E098](01_evidence_index.md#e098)、[E099](01_evidence_index.md#e099)；C036

**证据等级：** A

**更准确的理解：** 区分事件原发生、文本真实回忆与卡片自行回顾；主动创作回顾可以是IF，但不能冒充原著章节。小璐身份仍未因此获客观定性。

**可能造成的 RP 后果：** 错误触发第二次敌情揭示、给夏添加击杀及知识，抹去王钥初次觉醒场景。

**建议处理：** 回接C021/C036/C009；有意保留回顾须列U003 USER_CONFIRMATION_REQUIRED，不静默改写源文。


## [C109] 间界妖精的受困处境被绝对化为无法离开故土

**严重程度：** MODERATE

**问题类型：** 世界规则／主观视角

**角色卡位置：** [ID 102｜剧情·卷2幕05·跨年·银屏山之战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_102.txt>)

**当前内容概述：** 事件十二概括间界贫瘠、妖精无法离开故土；并以塞米保持理智说明其间界来历。

**发现的问题：** 83一面写塞米自身无力离开，一面让大杰克说能带全族走却不愿。不能从个人困境建普世禁令；出生地与保留理智之间也未展示充分机制。

**原著证据 / 定位：** [E332](01_evidence_index.md#e332)—[E334](01_evidence_index.md#e334)

**证据等级：** A（回忆与言说发生）／D（大杰克可行性自述）／F（普适通行与理智机制）

**更准确的理解：** 保留个体能力、家园意愿和可行性自述，不反向断言妖精随时自由通行。塞米与黑猫的共同家园愿望具有具体关系来源，非仅白狼抽象口号。

**可能造成的 RP 后果：** 封死实际可有的迁移选择，把思想与能力限制作同一禁制，旁观者凭理智便全知籍贯。

**建议处理：** 收窄绝对规则并留开放机制；与M036关系补录交叉引用。


## [C110] 将白静萱已坦白的祭子身份错误列为隐瞒项

**严重程度：** MAJOR

**问题类型：** 认知范围／卡内矛盾

**角色卡位置：** [ID 17｜白静萱](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_017.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)

**当前内容概述：** 卡103第93章称只坦白残兽方向偏移、隐去祭子与父母真相；卡17另写小璐夏凉后来知道祭子层面。

**发现的问题：** 源L23594明确已说黑烬祭子、湖畔战斗、残兽魔力，隐去的是父母身份。摘要把有限真相进一步删掉，且与人物卡自相矛盾。

**原著证据 / 定位：** [E355](01_evidence_index.md#e355)；[E447](01_evidence_index.md#e447)—[E449](01_evidence_index.md#e449)

**证据等级：** A（坦白范围）／D（修饰后的战斗故事）

**更准确的理解：** 夏先私问，小隔数日当众问；小夏知道祭子称谓与兽方向偏移，未知父母、人造细节。并非全队全社会得知。 续审15：159白主动以樱和过去父母复仇，众人知其兽力和仇恨不等父母具体身份全揭；祭子知情旧证仍有效，本次新叶亦不等完整兽能力机制全公开。

**可能造成的 RP 后果：** RP会让小夏重复首次震惊、误判白还在隐瞒已告诉的内容。

**建议处理：** 后续按人物与时间修复知情边，不改成全盘公开。

## [C111] 把私下称妈妈的约定绝对化为公开场景永不发生

**严重程度：** MODERATE

**问题类型：** 关系状态／约束过强

**角色卡位置：** [ID 17｜白静萱](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_017.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)

**当前内容概述：** 卡17语言、当前关系及扮演约束把公开称妈妈列为禁止；卡103庙会省略实际称呼。

**发现的问题：** 95有私下限制，但100在公共小吃广场白两次称妈妈，翠未纠正。卡将阶段约定写成覆盖后文真实行为的硬规则。

**原著证据 / 定位：** [E359](01_evidence_index.md#e359)、[E369](01_evidence_index.md#e369)、[E371](01_evidence_index.md#e371)；[E376](01_evidence_index.md#e376)、[E377](01_evidence_index.md#e377)

**证据等级：** A

**更准确的理解：** 保留早期约定及后文公共场景例外；例外不等正式解除约定，更不等周围人人知完整收养关系或林翠身份。 续审13：101和102白又把妈收成老师，说明100公共例外未证明私下约定已正式废除；准确处理为有约定、有破例、有当场收口，不能反向固化为总能公开叫。

**可能造成的 RP 后果：** 会阻止真实日常互动，或反向把例外扩大为全社会知情。

**建议处理：** 用阶段默认和已发生例外管理称呼；兽子保密另行控制。

## [C112] 将绿塔未知门记录写成登王之门传闻得到物证

**严重程度：** MODERATE

**问题类型：** 推断升级／摘要内冲突

**角色卡位置：** [ID 60｜木百合](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_060.txt>)；[ID 103｜剧情·卷2幕06·盟约与备考](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_103.txt>)；[ID 4｜国度与政治](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_004.txt>)

**当前内容概述：** 卡103第97章称都市传言第一次获得物证，第98章与卡60又承认门是否真实未知。

**发现的问题：** 物证是自动书记本身，不能确认其研究对象就是传闻之门；98明确把这种联系保留未知。所谓物证若不说明证明对象会升级结论。

**原著证据 / 定位：** [E362](01_evidence_index.md#e362)、[E363](01_evidence_index.md#e363)、[E365](01_evidence_index.md#e365)；[E365](01_evidence_index.md#e365)

**证据等级：** A（记录存在）／C（两者关联）／F（传闻真实性）

**更准确的理解：** 旧日有人研究某对象有实物记录；是否登王之门、与安雅的因果均未确认。年份相近只能提示后查。 续审13：卡4又把自动书记年代写成与翠/安入道吻合的王权暗线，应沿98已明确的未知关联限定；线索相近不能升级因果或确证门。

**可能造成的 RP 后果：** NPC会据摘要宣布已找到传闻入口或提前认定安雅关联。

**建议处理：** 限定物证证明对象，保留卡60正确未知边界及未来补证入口。

## [C113] 彩云湿地住处分散概括遮掉四人同屋四床安排

**严重程度：** POTENTIAL RISK

**问题类型：** 空间概括歧义／调用风险

**角色卡位置：** [ID 116｜彩云湿地](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_116.txt>)；[ID 104｜剧情·卷2幕07·赴国度](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_104.txt>)

**当前内容概述：** 卡116称把分散的观景房作为赴考据点；卡104虽有四床同屋，地区常驻描述仍易给出多屋。

**发现的问题：** 卡116的分散房间措辞也可仅指旅馆整体布局，并未明确声称小队各住一屋；卡104又正确写四床同屋。因此不再裁为已确认空间事实错误，保留为常驻地域概括可能遮掉当期住法的调用风险。

**原著证据 / 定位：** [E386](01_evidence_index.md#e386)；[E455](01_evidence_index.md#e455)

**证据等级：** A（原著四床同屋）／C（卡措辞可能导致的调用风险）

**更准确的理解：** 旅馆各屋相隔，小队四人同屋；墨荷另屋几百米外。隐私术式可开启，不限夜间。 健康检查13修订：保留原先定位与当期同屋证据，但承认卡116可作非冲突解读；仅标潜在歧义，不要求将其改成确定错误。 续审16：168再明确四单床同屋到先后挤床、夏推拼床的改变，保持前期分散旅舍布局与小队同屋并存。新增证据加强同屋事实，但未证明116非冲突概括一定错，维持健康检查降级为潜在风险。

**可能造成的 RP 后果：** 会错误生成分房、跨屋走访、旁听条件与私谈距离。

**建议处理：** 后续区分酒店整体布局、当期房间分配及隐私状态。

## [C114] 把术式列为翠雀真正强项，抹平会用与擅长的区别

**严重程度：** MODERATE

**问题类型：** 能力定位／相对专长

**角色卡位置：** [ID 47｜林昀](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_047.txt>)

**当前内容概述：** 卡47称真正强项是出力管理、术式、近战经验和规则战。

**发现的问题：** 134明确虽然翠雀并不擅长术式，仍为防生日识别使用数项保障；能熟练应用低阶术式与有战术经验，不等专精术式。卡把相邻专长并列会让这一局限消失。

**原著证据 / 定位：** [E424](01_evidence_index.md#e424)

**证据等级：** A

**更准确的理解：** 她会使用术式且能判断简单扫描，也熟悉高阶术存在；当前文本明确不擅长这一领域。不要把不擅长绝对化为完全不会术式。

**可能造成的 RP 后果：** 生成万能术式专家、无代价开发高阶调查术，或反向误写完全不能用。

**建议处理：** 后续将会用的工具、理论见识、战术专长与术式短板分别保留。


## [C115] 女王部分回答与正式接见被改成拒绝解释和闯宫

**严重程度：** MAJOR

**问题类型：** 历史因果／认知来源

**角色卡位置：** [ID 106｜剧情·卷2幕09·旧梦与岔路](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_106.txt>)

**当前内容概述：** 卡106事件十称翠闯入蔷薇宫质问，女王没有解释战争伤亡，只提出效忠加冕。

**发现的问题：** 153翠明确女王恰接见自己，并说她回答了至少其中一部分，只是有些答案奇怪或某些问题沉默。摘要把有限回答变完全不答，也把召见变自行闯宫，删掉需要后验的认知裂缝。

**原著证据 / 定位：** [E441](01_evidence_index.md#e441)

**证据等级：** A（原文如此记述）／D（翠对往事的陈述）

**更准确的理解：** 保留捕风消息、召见、部分回答且奇怪、情绪性拒任的顺序；别将翠的战争正义判断等于已向读者公开战争全部内幕。

**可能造成的 RP 后果：** 生成从未发生的闯宫行动，或将女王所有回应锁为沉默回避。

**建议处理：** 后续依原口述修摘要，并开放奇怪回答的迟到解释。


## [C116] 将宴席中飞燕草等字牌误写为花牌

**严重程度：** MODERATE

**问题类型：** 人物能力／任职等级

**角色卡位置：** [ID 106｜剧情·卷2幕09·旧梦与岔路](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_106.txt>)

**当前内容概述：** 卡106事件九说折鹤兰领衔，飞燕草、迷迭香等花牌集体跪礼。

**发现的问题：** 149仅折鹤兰是花牌13011；飞燕草13314、迷迭香13877等为字牌。部长职务不能替代认证等级。

**原著证据 / 定位：** [E438](01_evidence_index.md#e438)

**证据等级：** A

**更准确的理解：** 折为花牌，其余列明的四人字牌，所有来客至少字牌；未知者不一律花牌。

**可能造成的 RP 后果：** 凭部门职位抬高战力或改变花牌稀缺性。

**建议处理：** 按个人明确编号等级记录，保留职位独立维度。


## [C117] 将准备转达的考核警告写成已经向祖母绿提交

**严重程度：** MODERATE

**问题类型：** 信息传播／行动状态

**角色卡位置：** [ID 106｜剧情·卷2幕09·旧梦与岔路](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_106.txt>)

**当前内容概述：** 卡106事件八及幕末说只把考核人为袭击警告交祖，已透露必要险情。

**发现的问题：** 147决定告安全信息但还在修辞就被宴会邀请打断；宴上先由折鹤兰主动报告潜入和计划。决定说不等实际说，祖猜近期见郁也不等获墨全部警告。

**原著证据 / 定位：** [E435](01_evidence_index.md#e435)、[E436](01_evidence_index.md#e436)、[E442](01_evidence_index.md#e442)、[E445](01_evidence_index.md#e445)

**证据等级：** A（说话及打断顺序）／C（祖推断）

**更准确的理解：** 146只问郁旧人且用陵园想起作借口；147传警意图未在本场说出，154折给既掌握线索，157才更明示监控边界。

**可能造成的 RP 后果：** 让祖因翠警报才布置防卫，或持有实际从未交出的消息来源。

**建议处理：** 后续拆分准备、实际告知、他方先掌握三种记录。


## [C118] 留活口方案被写成对整个魔事院保密的私案

**严重程度：** MODERATE

**问题类型：** 保密范围／合作行动

**角色卡位置：** [ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)；[ID 109｜剧情·卷2幕12·魔装考核](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_109.txt>)

**当前内容概述：** 卡107事件三称翠建立瞒祖母绿、魔事院与后辈的私案。

**发现的问题：** 158明确计划由自己抓旧部并调整安保部署，后续可交魔事院让折鹤兰等一起完善。她隐瞒旧友接触/细节，不等方案必须不让任何魔事院人员知道。

**原著证据 / 定位：** [E445](01_evidence_index.md#e445)、[E446](01_evidence_index.md#e446)；[E451](01_evidence_index.md#e451)、[E452](01_evidence_index.md#e452)、[E454](01_evidence_index.md#e454)；[E497](01_evidence_index.md#e497)、[E504](01_evidence_index.md#e504)

**证据等级：** A（规划文本）

**更准确的理解：** 区分墨荷私交/情报来源、自己亲抓留活口的方案以及共同布防。此刻后者待交绿派，不是全院已知或永久瞒全院。 续审16：163—164已真正向折及绿派提交、当面商讨，167已联研究/考试/调查完成实地预演版，不是仍待告知。翠明确承诺若有防务风险愿舍个人要求，折也愿先搜而放弃钓鱼获功。应只对未参与派系保密，不能全院保密或无条件纵容旧友。 续审18：220拿名单只是既有安保方案改进而非新建钓鱼局；228约晚上再调点位巡逻、翠要抓幕后且不妄救全部。名单真实性/薄清白须核，事后处置按罪；不能把调查计划写成已经全部核实或无限免罪。

**可能造成的 RP 后果：** 阻止原文合作流程，或把安全布置写成翠单人秘密修改。

**建议处理：** 后续按角色、派系和实际提交时间维护保密。

## [C119] 鸽血红已有现时发言却仍被写成没有清晰台词

**严重程度：** MODERATE

**问题类型：** 旧状态残留／语言

**角色卡位置：** [ID 29｜鸽血红](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_029.txt>)

**当前内容概述：** 卡29语言风格称现实时点没有清晰台词。

**发现的问题：** 182她向新紫说启程时刻已至、该去考场，已出现明确语气与劝止训斥的作用。

**原著证据 / 定位：** [E464](01_evidence_index.md#e464)

**证据等级：** A

**更准确的理解：** 可保留少言/不乱加口癖的约束；仅将无台词收窄为台词少，并记录此处从简古语到平实说明的切换。

**可能造成的 RP 后果：** 绝对未知会使已有言行消失。

**建议处理：** 按公共仪式时段采用实际台词，后续复核其他场景。


## [C120] 选择参加的补考被改成全员统一重考

**严重程度：** MODERATE

**问题类型：** 考试制度／资格与成绩

**角色卡位置：** [ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)

**当前内容概述：** 107事件九称翠推动全体统一补考。

**发现的问题：** 172规定自觉首日失常者可选；补考成绩唯一替换原分，不是全员强制，也不是取最高。

**原著证据 / 定位：** [E458](01_evidence_index.md#e458)、[E459](01_evidence_index.md#e459)

**证据等级：** A

**更准确的理解：** 小自选符文和算数两门；规则面向自觉受影响者，未把全部考生认作作弊或受害。

**可能造成的 RP 后果：** 改变选择权及成绩处理，可能让所有NPC无故重考。

**建议处理：** 保留自主报名、换题同难、仅计补考及公布时序。


## [C121] 聪明术购买链被提前改成小璐的考后回忆

**严重程度：** MAJOR

**问题类型：** 情报来源／动机猜测

**角色卡位置：** [ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)

**当前内容概述：** 107事件八称翠先查身体饮食接触、小回想社区兜售并知自己未购却遭公共波及。

**发现的问题：** 170只有群聊背串/稳心态，171餐厅通过复问才疑术式；完整卖术和购买链来自172排查受审者与叙述，不能归到小的前场回忆。袭击控制测试只是卡加推演，原段未证。

**原著证据 / 定位：** [E457](01_evidence_index.md#e457)、[E458](01_evidence_index.md#e458)

**证据等级：** A（来源序列）；D/B（各次解释）

**更准确的理解：** 自以背串→复问发现状态差异→翠夏疑术式/动机未定→次日抓人及供述；保持他人是否故意害人与未知卖者分离。

**可能造成的 RP 后果：** 提前透底消掉认知修正，给小不曾取得的线索。

**建议处理：** 回接实际来源，猜测另标，不增写体检和现场兜售目击。


## [C122] 随机第三队友被写成狗尾草介绍的候选人

**严重程度：** MODERATE

**问题类型：** 组队因果

**角色卡位置：** [ID 107｜剧情·卷2幕10·魔事分院与笔试](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_107.txt>)；[ID 108｜剧情·卷2幕11·花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_108.txt>)

**当前内容概述：** 107事件十一写狗介绍土丁桂为第三人候选；108同时又写随机分配。

**发现的问题：** 174/178规则第三随机；狗愿分到大腿，结果找到土才知成真，没有介绍候选过程。

**原著证据 / 定位：** [E460](01_evidence_index.md#e460)、[E462](01_evidence_index.md#e462)

**证据等级：** A

**更准确的理解：** 狗与龙互指定，再由考方随机分土；两人与土在汇合时才各自见到，既有一面之缘不等事前招募。

**可能造成的 RP 后果：** 把考试随机规则改成自由选人，并制造卡内互斥因果。

**建议处理：** 保留邀队与随机两步骤，避免用108正确摘要遮掉107错误。


## [C123] 无出口推理把夏凉与卷丹的发起作用写反

**严重程度：** MODERATE

**问题类型：** 行动主体／推理来源

**角色卡位置：** [ID 108｜剧情·卷2幕11·花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_108.txt>)

**当前内容概述：** 108事件二称卷丹先判断并由夏接受思路。

**发现的问题：** 185夏先画图提问与出题人视角，卷回应公平并提出反例，夏推暂不设出口，卷仍疑想多；不是卷主导夏接受。

**原著证据 / 定位：** [E466](01_evidence_index.md#e466)

**证据等级：** A（讨论流程）；B（未证假说）

**更准确的理解：** 三人认知不同：夏主导分析、卷推进和质疑、山未懂求复讲；不否定卷有实质贡献。

**可能造成的 RP 后果：** 削弱夏独立判断成长，并把讨论过程变成单人结论。

**建议处理：** 按每人贡献和证实阶段记录。


## [C124] 迷宫袭击规则被写成可通过袭击夺取积分

**严重程度：** MODERATE

**问题类型：** 积分机制／条件遗漏

**角色卡位置：** [ID 108｜剧情·卷2幕11·花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_108.txt>)；[ID 145｜银廊后花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_145.txt>)

**当前内容概述：** 108三明规概括考生可以袭击、夺取积分，并被指认则成绩转移；145也简成被指认就转。

**发现的问题：** 183只允许袭击/干扰；分数转移规定是受害者被淘汰后指认并核查，转给受害者。没有袭击者击倒人就拿其积分的规则，且不是任意被点名就处罚。

**原著证据 / 定位：** [E465](01_evidence_index.md#e465)；[E470](01_evidence_index.md#e470)、[E473](01_evidence_index.md#e473)、[E479](01_evidence_index.md#e479)

**证据等级：** A（公布规则）

**更准确的理解：** 允许竞争和偷袭≠授予击倒抢分；核验清晰锁人且受害淘汰后执行。其他场项目规则不得倒灌迷宫。 续审17：190醉露脸仍能淘汰马，200后补其被指认只伤个人当场、仍争团队与观礼分；个体零分不等所有成绩全清。194故意引爆他人陷阱致其间接破迷宫处罚，不等直接击倒抢分。

**可能造成的 RP 后果：** 诱导考生用不存在的掠分机制，或让随口指控自动扣分。

**建议处理：** 完整保存触发、核查、转移方向与本场边界。

## [C125] 引离佯攻撤离被省成身后镜面的真正攻击

**严重程度：** MODERATE

**问题类型：** 战术因果／能力机制

**角色卡位置：** [ID 108｜剧情·卷2幕11·花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_108.txt>)

**当前内容概述：** 108将193概括为身后镜完成真正攻击后带队撤退。

**发现的问题：** 背后镜仍为诱导，实际爆术最后出口在夏身边，目的是诱敌改屏障并用牵引撤走；没有命中醉的证据。

**原著证据 / 定位：** [E471](01_evidence_index.md#e471)、[E472](01_evidence_index.md#e472)

**证据等级：** A

**更准确的理解：** 保留双层前镜→反向背镜→夏旁出口→低耗牵引带三人撤的必要因果，不将最终镜位混作命中位置。

**可能造成的 RP 后果：** 使夏得到未发生的击伤、掩掉资源调度和牵引用途。

**建议处理：** 修正位置与目的；概述可简但不得倒转最后层。


## [C126] 三色地砖的规则和分工被改写

**严重程度：** MAJOR

**问题类型：** 谜题机制／行动主体

**角色卡位置：** [ID 108｜剧情·卷2幕11·花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_108.txt>)

**当前内容概述：** 108称沿不同颜色前进、踩错重置，小探路白确认。

**发现的问题：** 194目标连绿色路径；踩本格及四邻按红黄绿循环，前队进度可继承；小固定供魔、白薄解。

**原著证据 / 定位：** [E473](01_evidence_index.md#e473)

**证据等级：** A

**更准确的理解：** 这是邻格联动解题，不是按指定颜色逐人走的记忆关。

**可能造成的 RP 后果：** 生成错误机关和分工，无法复现真实协作。

**建议处理：** 替换错误机制并保留继承进度/固定供魔限制。


## [C127] 箭根薯的节省魔力合作被写成放弃灭口

**严重程度：** MAJOR

**问题类型：** 动机擅断／淘汰与杀人混淆

**角色卡位置：** [ID 108｜剧情·卷2幕11·花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_108.txt>)

**当前内容概述：** 108称箭本欲灭口，因为露脸且多名目击/监控而改合作。

**发现的问题：** 204她称已在被指认前淘汰先队，提合作为独打节点耗魔；没有此处杀人灭口意图及被逼改意的证据。

**原著证据 / 定位：** [E481](01_evidence_index.md#e481)、[E482](01_evidence_index.md#e482)

**证据等级：** A（提出合作）；D（自述）；F（未证杀人意图）

**更准确的理解：** 按敌意、淘汰竞争和合作分工记，不替人物增杀意；旁观监控是考试条件，不自动提供具体心理因果。

**可能造成的 RP 后果：** 把危险言行升级为未发生的杀人计划，误改人物关系。

**建议处理：** 删除无据动机归因的事实地位，若作为IF进入U边界。


## [C128] 夏凉用醉鱼草情报换图被写成出售穿墙底牌

**严重程度：** MAJOR

**问题类型：** 交易内容／信息传播

**角色卡位置：** [ID 108｜剧情·卷2幕11·花园迷宫](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_108.txt>)

**当前内容概述：** 108称210以穿墙情报换地图。

**发现的问题：** 实际以醉鱼草详细能力及不再告别人的承诺成交，目的仍保自己的底牌。

**原著证据 / 定位：** [E487](01_evidence_index.md#e487)、[E490](01_evidence_index.md#e490)、[E492](01_evidence_index.md#e492)

**证据等级：** A

**更准确的理解：** 场内交易对象获得醉能力情报；夏的引离到场外观礼传播才广为人知，不能提前给测绘队这项交换知识。

**可能造成的 RP 后果：** 倒转交易筹码和保密策略，制造错误知情名单。

**建议处理：** 分别记录交易、看见与事后公开三条链。


## [C129] 土丁桂请求改称姐姐被替换为考后继续并肩邀约

**严重程度：** MODERATE

**问题类型：** 关系事件／无据新增

**角色卡位置：** [ID 109｜剧情·卷2幕12·魔装考核](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_109.txt>)；[ID 43｜土丁桂](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_043.txt>)

**当前内容概述：** 109事件一将214末写成提出考后继续与新人才并肩。

**发现的问题：** 原末实际是能否改叫姐姐，没有此场考后长期结队邀约。

**原著证据 / 定位：** [E491](01_evidence_index.md#e491)

**证据等级：** A

**更准确的理解：** 肯定后的亲近以称呼请求表达；未来关系不得用未发生邀约填充。

**可能造成的 RP 后果：** 漏关键称谓发展并添未来约定。

**建议处理：** 保留称呼与临时队关系，长期承诺另待证。


## [C130] 薄荷对同党与未归化的先后判断写反

**严重程度：** MAJOR

**问题类型：** 认知阈值／旧信息抹除

**角色卡位置：** [ID 109｜剧情·卷2幕12·魔装考核](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_109.txt>)

**当前内容概述：** 109称薄一直以为两人是蛾留下的未归化祭子，小白坦白根本不知这些称呼。

**发现的问题：** 217她以为两人已属蛾/黑烬而先质疑装，确认不懂后才提未归化；原文明确小白早听过兽子祭子，也知圣子计划词系，缺的是完整定义。

**原著证据 / 定位：** [E494](01_evidence_index.md#e494)、[E495](01_evidence_index.md#e495)

**证据等级：** A（修正过程）；D（分类说法）

**更准确的理解：** 已闻名词≠掌握机制；薄同党假设→不懂/未归化→蛾根本未得手，保留各步及放波引箭的迟到因果。

**可能造成的 RP 后果：** 让薄在明知非同党前提下作不合理暗示，并抹已获知识。

**建议处理：** 拆开认词、定义、归属与能力性质，回接C009/C110。


## [C131] 木棉的武器直觉被变成小璐已听懂的客观败因

**严重程度：** MODERATE

**问题类型：** 战斗解释／认知归属

**角色卡位置：** [ID 109｜剧情·卷2幕12·魔装考核](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_109.txt>)

**当前内容概述：** 109称木五秒击败后小第一次听懂自己错在哪里：王钥被丝线束缚。

**发现的问题：** 236五秒只末次连段，前有实际击伤；237木是直觉说法、花类比非魔装读武器，翠心信几分，小仍埋脸哭未显示理解；238仍沮丧。

**原著证据 / 定位：** [E512](01_evidence_index.md#e512)、[E513](01_evidence_index.md#e513)、[E514](01_evidence_index.md#e514)；[E523](01_evidence_index.md#e523)、[E532](01_evidence_index.md#e532)

**证据等级：** A（战况）；D/E（直觉与解释）；F（是否已悟）

**更准确的理解：** 败战已定，原因包括系统对人训练差；魔装束缚是待后文实践检验的线索，由木提出、翠部分采纳。 续审19：247明说小连木战怎么输都没弄懂，进一步证237未悟；256才以既有技巧异常快融会、亲自说旧战法不圆满，故不是永远未理解。木的启发经翠部分接受→小败后思考→新战实践自证，仍不证明字面武器交流超能力。

**可能造成的 RP 后果：** 提前完成成长线、把他人理论写成本人掌握或客观机制。

**建议处理：** 区分整战和最后五秒，把认知成熟留给实际后文。

## [C132] 天音的传播、占用和声音干扰限制缺失

**严重程度：** MODERATE

**问题类型：** 能力限制遗漏

**角色卡位置：** [ID 17｜白静萱](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_017.txt>)；[ID 109｜剧情·卷2幕12·魔装考核](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_109.txt>)

**当前内容概述：** 17只写八音盒活化、B-与偏移口径；109偏重秘密通过，未给作用失效与多人代价。

**发现的问题：** 225直接解释音距衰减、人数增不降效果但占用升、杂声扰乱或覆盖即失效，微修本相不能救碎濒死；这些是战斗可执行的硬边界。

**原著证据 / 定位：** [E500](01_evidence_index.md#e500)、[E501](01_evidence_index.md#e501)

**证据等级：** A

**更准确的理解：** 把魔力治愈与天音音乐效果分开；人数不稀释并非不耗出力，无视声音干扰会夸大稳定度。

**可能造成的 RP 后果：** 造成无限多人全效、隔音照治或救濒死本相等超原表现。

**建议处理：** 收录检测阶段限制及早期锤柄回缩变化，不能倒灌尚未开发阶段。


## [C133] 紫钻会面把门外叮嘱与事后商量写成同室答复

**严重程度：** MAJOR

**问题类型：** 场景主体／信息来源

**角色卡位置：** [ID 110｜剧情·卷2幕13·云境夺牌战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_110.txt>)

**当前内容概述：** 110称祖在场见证并提醒小不泄母队长，翠未替女拒、说等考后小给答案。

**发现的问题：** 240翠只送到研究院门外且为避暴露不进，叮嘱者翠；241紫与小谈，242回叙小先拒紫、会后与翠私商由翠待考后找答案。

**原著证据 / 定位：** [E516](01_evidence_index.md#e516)—[E518](01_evidence_index.md#e518)

**证据等级：** A

**更准确的理解：** 祖在研究院把关不等描写其同室，翠不在紫面前替小发言；私商与会谈分别保存。

**可能造成的 RP 后果：** 让紫直接见龙/翠并听隐秘关系讨论，破后续行动依据。

**建议处理：** 按门外、休息室、旅馆三场景还原。


## [C134] 云境初期逃跑的主体被反转为629小队

**严重程度：** MODERATE

**问题类型：** 事件主体／策略

**角色卡位置：** [ID 110｜剧情·卷2幕13·云境夺牌战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_110.txt>)

**当前内容概述：** 110事件四称白玫队一路遇到队伍便撤。

**发现的问题：** 244是他队见SS主动撤，白玫白雪想追而薄阻止；保牌还是追人的争执由此产生。

**原著证据 / 定位：** [E520](01_evidence_index.md#e520)

**证据等级：** A

**更准确的理解：** 629主动探索，放走他队不等被逼不断逃。

**可能造成的 RP 后果：** 倒转实力威慑与争分分歧。

**建议处理：** 修正逃跑主体并保薄风险判断与分池差异。


## [C135] 云境第一夜12张C牌被记成12张叶级牌

**严重程度：** MODERATE

**问题类型：** 计分单位／阶段混用

**角色卡位置：** [ID 110｜剧情·卷2幕13·云境夺牌战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_110.txt>)

**当前内容概述：** 110事件八第一夜12张叶级、4B、1A。

**发现的问题：** 248明12C、4B、1A；认证评级不等开华级，不能从C认叶或把牌类改等级。

**原著证据 / 定位：** [E524](01_evidence_index.md#e524)

**证据等级：** A

**更准确的理解：** 保留编号评级的积分结构，不把持牌者开华混入。

**可能造成的 RP 后果：** 让夺牌记分与人物成长等级失配。

**建议处理：** 更正统计单位并与239规则联查。


## [C136] 石蒜的昙开教学被限定为花牌并移到旁观现场

**严重程度：** MAJOR

**问题类型：** 能力门槛／信息时点

**角色卡位置：** [ID 111｜剧情·卷2幕14·回忆·1979卢恩诺雷守卫战](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_111.txt>)

**当前内容概述：** 111事件八说石蒜教极少数有天赋的花牌，并当着矢面握宝石唱名。

**发现的问题：** 267明确蕾以上可学，矢以蕾学成；墨叶只听不受教。人群撤离后石独处才发动，卡把教学资格、认证身份和见证时间混写。

**原著证据 / 定位：** [E543](01_evidence_index.md#e543)、[E544](01_evidence_index.md#e544)

**证据等级：** A

**更准确的理解：** 开华蕾是学习下限、成功率极低；认证花牌非同一轴。矢听殿后决定而离开，后通过魔波知道昙开结束。

**可能造成的 RP 后果：** 会禁止蕾期矢已有技能，或让矢看到仅叙述可见的临终动作。

**建议处理：** 分别记录学习条件、称号和目击/感知边界。


## [C137] 小璐编造的亲子谎言被反写成她本人的信念

**严重程度：** MAJOR

**问题类型：** 认知主体／谎言传播

**角色卡位置：** [ID 46｜林小璐](<C:/Users/Administrator/Desktop/下班魔角色卡重构/audit/card_text/entry_046.txt>)

**当前内容概述：** ID46隐藏信息及phone_catalog.profiles.林小璐的隐藏真相段写“自行相信龙胆是矢车菊的小孩”；同条语言、关系段却写她为圆谎编造。

**发现的问题：** 250小璐当场编造给土狗听，252私下向翠解释并受训；253翠应付土狗并掌书预告任务。卡把编造者、相信或尚在追问的人混成同一认知主体，且与自身其他段落矛盾。

**原著证据 / 定位：** [E526](01_evidence_index.md#e526)、[E528](01_evidence_index.md#e528)、[E529](01_evidence_index.md#e529)；technical/phone_catalog.json profiles.林小璐.sections[隐藏真相与知情边界]

**证据等级：** A（编造、解释和逐人信息流）

**更准确的理解：** 小璐知道该亲子说法由自己编造；龙胆的魔法少女身份边与林昀男性本体边应分开。完整身份链未知不等每条边都未知。土狗的亲子疑问和掌书所知另依C015，不能迁给小璐。

**可能造成的 RP 后果：** NPC会忘记自己在说谎，追问虚构生育史并丢失掩护动机。

**建议处理：** 后续同步两份资料并按说谎者、听者和时点记录；不因修正这一信念就授予小璐男性本体知识。


## [C138] 手机将林小璐与林昀的亲生父女关系改为收养

**严重程度：** MAJOR

**问题类型：** 血缘关系／资料副本冲突

**角色卡位置：** 技术／源文位置见下方定位；[技术目录](technical)

**当前内容概述：** phone_catalog.profiles.林小璐的身份与关键关系写林昀养女/养父，profiles.林昀关键关系写自己的养女；世界书ID46则写亲生女儿。

**发现的问题：** 卷二72林内心明确“只有你是我亲生的”，92又在亲生血脉与魔装相似的思考中提及；没有原著的林小璐收养转变。手机副本把白静萱式家庭关系套入另一主体，不能以角色卡副本的亲生写法作为唯一证据。

**原著证据 / 定位：** [E312](01_evidence_index.md#e312)（L20854）；源文L23697—23701；technical/phone_catalog.json profiles.林小璐/林昀 的关键关系及身份与定位

**证据等级：** A（原著内心叙述中的既有父女关系）

**更准确的理解：** 在所给原著中小璐是林昀与安雅的亲生女儿；血缘事实不等小璐知道父亲的魔法少女身份。对夏凉和白静萱的家庭接纳分别记录，不以重亲情为由混淆血缘。

**可能造成的 RP 后果：** 同一玩家经正文和手机得到不同身世，父女和解与身份保密的基础被改写。

**建议处理：** 后续修正手机对应两人物及raw/sections同步关系；若有意更改血缘须列U003可选IF，不能作为原著秘密反转。

