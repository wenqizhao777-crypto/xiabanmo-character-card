# 当前角色卡结构地图

本文件仅记录 PNG 内嵌数据的静态解析结果，不运行卡片内代码。技术字段不能直接视为小说设定。

## 输入与载体

- 输入：`current/260808.png`（7,394,632 字节）。PNG 含 `chara` 与 `ccv3` 两个 Base64 JSON 块；解码后的对象完全一致，不能按两张不同卡重复计数。
- 规范自报：chara_card_v3 / 3.0。条目总数 143，正文总长度 224,224 字符（非 token）。
- 顶层兼容字段与 `data` 均存在。顶层人物描述、性格、场景、示例对话与作者评论为空；data 中系统提示、历史后指令、作者备注也为空。
- 名称：下班，然后成为魔法少女；主开场 `<开局声明>`；备用开场 `<开局>`。开场本身是 UI 占位符，不是原著事件。
- 8 个正则脚本、4 个 Tavern Helper 脚本，均为启用状态。

## 世界书配置

- 启用 142 条，禁用 1 条（ID 8 `[InitVar]`）。启用且 constant=true：56 条，共 37,777 字符。这里只说明候选常驻体积；实际注入仍受宿主预算、脚本、模板与上下文限制。
- 143 条的 secondary_keys 均为空。所有条目的递归相关配置一致：exclude_recursion=true、prevent_recursion=true、delay_until_recursion=false。不应声称本卡天然存在递归爆炸。
- 所有条目 probability=100、useProbability=true；group 为空、group_weight=100、ignore_budget=false；scan_depth、case_sensitive、match_whole_words 均为 null，具体继承宿主设置，不能假定命中方式。
- 113 条 extensions.position=0（顶层 position=before_char），30 条 extensions.position=4（顶层 position=after_char）。扩展值4涉及聊天深度注入语义，但未取得实际宿主版本，不据此宣称两个字段冲突。142 条 depth=4，ID15 depth=0。
- 条目数组索引不等于条目 ID；ID 有空缺并非自动构成损坏。

## 完整条目目录

|数组索引|ID|名称|字数|启用|常驻|主关键词|次关键词|位置：顶层/扩展|深度|顺序|
|---:|---:|---|---:|---|---|---|---|---|---:|---:|
|0|0|人物总览|1242|True|True|空|空|before_char/0|4|20|
|1|1|残兽与等级|267|True|True|空|空|before_char/0|4|25|
|2|2|魔法少女体系|606|True|True|空|空|before_char/0|4|15|
|3|3|魔术与符文|158|True|True|空|空|before_char/0|4|15|
|4|4|国度与政治|850|True|True|空|空|before_char/0|4|17|
|5|5|黑烬|306|True|True|空|空|before_char/0|4|15|
|6|6|其他|425|True|True|空|空|before_char/0|4|16|
|7|7|往事编年|1945|True|True|空|空|before_char/0|4|50|
|8|8|[InitVar]|767|False|True|空|空|before_char/0|4|100|
|9|9|变量快照|129|True|True|空|空|after_char/4|4|9990|
|10|10|[mvu_update]变量更新规则|2044|True|True|空|空|after_char/4|4|9991|
|11|11|[mvu_update]输出格式|673|True|True|空|空|before_char/0|4|9992|
|12|12|[mvu_plot]命运骰与检定|451|True|True|空|空|after_char/4|4|9993|
|13|13| [mvu_plot]叙事守则与开局初始化|531|True|True|空|空|after_char/4|4|9994|
|14|14|剧情·卷1幕01·重返战场|3212|True|False|卷1幕01、1999年5月、1999年6月|空|after_char/4|4|300|
|15|15|格式|3367|True|True|空|空|after_char/4|0|0|
|16|16|安雅|2594|True|False|安雅、樱|空|before_char/0|4|100|
|17|17|白静萱|3385|True|False|白静萱、薄雪、小萱|空|before_char/0|4|100|
|18|18|白狼|2266|True|False|白狼、前任紫钻|空|before_char/0|4|100|
|19|19|薄荷|2285|True|False|薄荷|空|before_char/0|4|100|
|20|20|魔法少女|583|True|True|空|空|before_char/0|4|20|
|21|21|残兽|566|True|False|残兽、兽之源、兽子、祭子、食祭|空|before_char/0|4|30|
|22|22|魔法少女的修炼方法|1140|True|True|空|空|before_char/0|4|30|
|23|23|认证牌|112|True|False|认证牌、白牌、字牌、花牌|空|before_char/0|4|30|
|24|24|开华|1092|True|True|空|空|before_char/0|4|30|
|25|25|灯盏|2630|True|False|灯盏|空|before_char/0|4|100|
|26|26|魔法少女变身步骤|921|True|True|空|空|before_char/0|4|30|
|27|27|起源与出现|808|True|True|空|空|before_char/0|4|30|
|28|28|回响(残兽核心/兑换物)|920|True|False|回响、核心、兑换物|空|before_char/0|4|30|
|29|29|鸽血红|1768|True|False|鸽血红、红宝石权杖|空|before_char/0|4|100|
|30|31|狗尾草|2115|True|False|狗尾草|空|before_char/0|4|100|
|31|32|金蛇|2464|True|False|金蛇、郁金香、海蒂、海蒂·阿比梅尔、海蒂.阿比梅尔|空|before_char/0|4|100|
|32|33|含羞草|2768|True|False|含羞草|空|before_char/0|4|100|
|33|34|褐鹈|1947|True|False|褐鹈|空|before_char/0|4|100|
|34|36|红思与|3356|True|False|红思与、朝颜|空|before_char/0|4|100|
|35|38|箭根薯|2040|True|False|箭根薯|空|before_char/0|4|100|
|36|40|金绿猫眼|2238|True|False|金绿猫眼|空|before_char/0|4|100|
|37|41|卷丹|1818|True|False|卷丹|空|before_char/0|4|100|
|38|43|土丁桂|2500|True|False|土丁桂、黎皎然|空|before_char/0|4|100|
|39|46|林小璐|3868|True|False|林小璐、小璐、璐璐、白玫|空|before_char/0|4|100|
|40|47|林昀|4567|True|False|林昀、翠雀、矢车菊、龙胆、老林|空|before_char/0|4|100|
|41|50|鸢|2569|True|False|鸢、唐菖蒲、陆红豆|空|before_char/0|4|100|
|42|53|玛格丽特|2753|True|False|玛格丽特、麻生圆香、麻生、圆香、玛丽|空|before_char/0|4|100|
|43|58|摩可|2388|True|False|摩可|空|before_char/0|4|100|
|44|59|摩丝|2743|True|False|摩丝、蛾|空|before_char/0|4|100|
|45|60|木百合|3023|True|False|木百合|空|before_char/0|4|100|
|46|64|黑猫|3319|True|False|黑猫、墨荷、妮娜、妮娜·克瑞吉欧斯、妮娜.克瑞吉欧斯、小荷、猫姐|空|before_char/0|4|100|
|47|66|女王|2174|True|False|女王|空|before_char/0|4|100|
|48|70|白蓟|2904|True|False|白蓟、邱云|空|before_char/0|4|100|
|49|72|山丹|1888|True|False|山丹|空|before_char/0|4|100|
|50|81|夏凉|3585|True|False|夏凉、小锦、小凉|空|before_char/0|4|100|
|51|88|紫钻|2201|True|False|紫钻、现任紫钻、钻石权杖|空|before_char/0|4|100|
|52|89|祖母绿|2807|True|False|祖母绿、绿宝石权杖、妖精仙人|空|before_char/0|4|100|
|53|91|剧情·卷1幕02·新队与下水道之歌|3219|True|False|卷1幕02、1999年6月|空|after_char/4|4|301|
|54|92|剧情·卷1幕03·异策局|3194|True|False|卷1幕03、1999年6月、1999年7月|空|after_char/4|4|302|
|55|93|剧情·卷1幕04·坦白与屏障|3194|True|False|卷1幕04、1999年7月、1999年8月|空|after_char/4|4|303|
|56|94|剧情·卷1幕05·黑烬黎明事变|3843|True|False|卷1幕05、1999年8月|空|after_char/4|4|304|
|57|95|剧情·卷1幕06·暑假与秘密基地|3645|True|False|卷1幕06、1999年8月、1999年9月、1999年10月|空|after_char/4|4|305|
|58|96|剧情·卷1幕07·柏安市巡查|3708|True|False|卷1幕07、1999年10月|空|after_char/4|4|306|
|59|97|剧情·卷1幕08·月圆节之变|3697|True|False|卷1幕08、1999年10月、1999年11月|空|after_char/4|4|307|
|60|98|剧情·卷2幕01·新局长与兽子|4597|True|False|卷2幕01、1999年11月|空|after_char/4|4|308|
|61|99|剧情·卷2幕02·鸢来袭|3625|True|False|卷2幕02、1999年11月、1999年12月|空|after_char/4|4|309|
|62|100|剧情·卷2幕03·演唱会与旧友|4091|True|False|卷2幕03、1999年12月|空|after_char/4|4|310|
|63|101|剧情·卷2幕04·备战与比试|4757|True|False|卷2幕04、1999年12月|空|after_char/4|4|311|
|64|102|剧情·卷2幕05·跨年·银屏山之战|4853|True|False|卷2幕05、1999年12月、2000年1月|空|after_char/4|4|312|
|65|103|剧情·卷2幕06·盟约与备考|4751|True|False|卷2幕06、2000年1月|空|after_char/4|4|313|
|66|104|剧情·卷2幕07·赴国度|3499|True|False|卷2幕07、2000年2月|空|after_char/4|4|314|
|67|105|剧情·卷2幕08·卢恩诺雷情人节|5934|True|False|卷2幕08、2000年2月|空|after_char/4|4|315|
|68|106|剧情·卷2幕09·旧梦与岔路|5533|True|False|卷2幕09、2000年2月|空|after_char/4|4|316|
|69|107|剧情·卷2幕10·魔事分院与笔试|5135|True|False|卷2幕10、2000年2月、2000年3月|空|after_char/4|4|317|
|70|108|剧情·卷2幕11·花园迷宫|5518|True|False|卷2幕11、2000年3月|空|after_char/4|4|318|
|71|109|剧情·卷2幕12·魔装考核|3560|True|False|卷2幕12、2000年3月|空|after_char/4|4|319|
|72|110|剧情·卷2幕13·云境夺牌战|3983|True|False|卷2幕13、2000年3月|空|after_char/4|4|320|
|73|111|剧情·卷2幕14·回忆·1979卢恩诺雷守卫战|3779|True|False|卷2幕14、2000年3月|空|after_char/4|4|321|
|74|112|原著时间|26|True|True|空|空|after_char/4|4|299|
|75|113|原著时间线2|10|True|True|空|空|after_char/4|4|330|
|76|114|柏安市|535|True|False|空|空|before_char/0|4|50|
|77|115|柏安市地下异策局|559|True|False|异策局|空|before_char/0|4|50|
|78|116|彩云湿地|485|True|False|彩云湿地|空|before_char/0|4|50|
|79|117|东华州域|477|True|True|东华州域|空|before_char/0|4|50|
|80|118|方亭市|545|True|True|空|空|before_char/0|4|50|
|81|119|方亭市第一福利院|502|True|False|福利院|空|before_char/0|4|50|
|82|120|方亭市下水道蛹兽巢穴|483|True|False|蛹兽巢穴、下水道|空|before_char/0|4|50|
|83|121|方亭小队秘密基地|446|True|True|空|空|before_char/0|4|50|
|84|122|翡翠书廊|523|True|True|翡翠书廊|空|before_char/0|4|50|
|85|123|花园|467|True|False|花园|空|before_char/0|4|50|
|86|124|荒原|487|True|False|荒原|空|before_char/0|4|50|
|87|125|纪念陵园|532|True|False|陵园|空|before_char/0|4|50|
|88|126|间界|471|True|True|间界|空|before_char/0|4|50|
|89|127|界门与界桥|511|True|True|空|空|before_char/0|4|50|
|90|128|黎星区|489|True|True|黎星区|空|before_char/0|4|50|
|91|129|临扬市|478|True|False|临扬市|空|before_char/0|4|50|
|92|130|卢恩诺雷|555|True|True|卢恩诺雷|空|before_char/0|4|50|
|93|131|卢恩诺雷魔事院分院|485|True|False|魔事院|空|before_char/0|4|50|
|94|132|珞明区|486|True|True|珞明区|空|before_char/0|4|50|
|95|133|魔法国度|493|True|True|空|空|before_char/0|4|50|
|96|134|魔法国度五都|488|True|True|空|空|before_char/0|4|100|
|97|135|蔷薇宫|473|True|False|蔷薇宫|空|before_char/0|4|50|
|98|136|湿地公园|482|True|False|公园|空|before_char/0|4|50|
|99|137|天都市|485|True|False|天都市|空|before_char/0|4|50|
|100|138|地区与势力总览|978|True|True|空|空|before_char/0|4|30|
|101|139|无魔力区|522|True|True|无魔力区|空|before_char/0|4|50|
|102|140|物质界|490|True|True|空|空|before_char/0|4|50|
|103|141|夕照区|489|True|True|夕照区|空|before_char/0|4|50|
|104|142|学院区|487|True|True|学院区|空|before_char/0|4|50|
|105|143|燕南市|477|True|False|燕南市|空|before_char/0|4|50|
|106|144|银廊|498|True|False|银廊|空|before_char/0|4|50|
|107|145|银廊后花园迷宫|489|True|False|后花园、迷宫|空|before_char/0|4|50|
|108|146|银屏山|472|True|False|银屏山|空|before_char/0|4|50|
|109|147|岳望市|471|True|False|岳望市|空|before_char/0|4|50|
|110|148|云境考场|526|True|False|云境、考场|空|before_char/0|4|50|
|111|149|爪痕荒原城堡|471|True|False|爪痕、荒原、城堡|空|before_char/0|4|50|
|112|150|祖母绿区|478|True|True|祖母绿区|空|before_char/0|4|50|
|113|151|地区概览|20|True|True|空|空|before_char/0|4|49|
|114|152|地区概览2|8|True|True|空|空|before_char/0|4|51|
|115|153|柏安市小队|470|True|False|柏安市、邱云、木百合、含羞草、播种者、灯盏|空|before_char/0|4|60|
|116|154|宝石权杖|476|True|True|宝石、权杖|空|before_char/0|4|60|
|117|155|财政院|483|True|True|财政|空|before_char/0|4|60|
|118|156|调查院|473|True|True|调查院|空|before_char/0|4|60|
|119|157|方亭市小队|468|True|True|空|空|before_char/0|4|60|
|120|158|国度军|483|True|False|国度军、国度|空|before_char/0|4|60|
|121|159|黑烬黎明|549|True|False|黑烬、黎明|空|before_char/0|4|60|
|122|160|间界联合军|516|True|False|间界、联合军|空|before_char/0|4|60|
|123|161|旧方亭市小队|471|True|True|空|空|before_char/0|4|60|
|124|162|卢恩诺雷城防军|526|True|False|卢恩诺雷、城防军|空|before_char/0|4|60|
|125|163|猫尾小队|490|True|False|猫尾|空|before_char/0|4|60|
|126|164|民治院|473|True|True|王庭、民治院|空|before_char/0|4|60|
|127|165|魔事院|478|True|True|魔事院|空|before_char/0|4|60|
|128|166|魔事院五派|483|True|False|魔事院|空|before_char/0|4|60|
|129|167|矢车菊小队|519|True|True|空|空|before_char/0|4|60|
|130|168|使徒|468|True|False|使徒、间界、黑烬、黎明|空|before_char/0|4|60|
|131|169|王庭|486|True|True|空|空|before_char/0|4|60|
|132|170|王庭护卫|530|True|False|王庭、护卫|空|before_char/0|4|60|
|133|171|研究院|475|True|True|空|空|before_char/0|4|60|
|134|172|异策局|501|True|True|异策局|空|before_char/0|4|60|
|135|173|异策局特殊作战部第三小队|480|True|False|异策局、李英伟|空|before_char/0|4|60|
|136|174|园丁|468|True|False|园丁、妖精、卫士|空|before_char/0|4|60|
|137|175|爪痕|472|True|False|爪痕、白狼|空|before_char/0|4|60|
|138|176|势力参考|18|True|True|空|空|before_char/0|4|59|
|139|177|势力参考2|8|True|True|空|空|before_char/0|4|61|
|140|178|剧情索引|1243|True|True|空|空|before_char/0|4|35|
|141|179|创作基调|2170|True|True|空|空|before_char/0|4|10|
|142|180|[mvu_update]羁绊与CG图鉴|2505|True|True|空|空|after_char/4|4|9995|

## 正则与展示层

|索引|脚本名|查找|promptOnly|markdownOnly|minDepth|用途线索|
|---:|---|---|---|---|---|---|
|0|魔法少女·开局标记出提示词|<开局>|True|False|None|替换长度 2|
|1|魔法少女·开局页渲染|<开局>|False|True|None|替换长度 76667|
|2|[美化][魔法少女]变量更新中|/<(update(?:variable)?)>(?!.*<\/\1>)\s*((?:(?!<\1>).)*)\s*$/gsi|False|True|None|替换长度 24644|
|3|[美化][魔法少女]完整变量更新|/<(update(?:variable)?)>\s*((?:(?!<\1>).)*)\s*<\/\1>/gsi|False|True|None|替换长度 24639|
|4|只发送最新3楼的变量更新|/<UpdateVariable>[\s\S]*?</UpdateVariable>/gm|True|False|6|替换长度 0|
|5|魔法少女·开局声明|<开局声明>|False|True|None|替换长度 12555|
|6|魔法少女·状态栏渲染|<StatusPlaceHolderImpl/>|False|True|None|替换长度 105711|
|7|魔法少女·正文美化|/<now_plot>([\s\S]*?)<\/now_plot>/gi|False|True|None|替换长度 77860|

正则配置全部 placement=[2]；未运行 UI，不断言渲染或替换必然成功。markdownOnly 的展示 HTML 不等于默认传给模型的正文。

## Tavern Helper 脚本

- [0] `mvu`：1,042 字符，enabled=True；审计副本 `technical/script_0.js`。
- [1] `zod`：4,437 字符，enabled=True；审计副本 `technical/script_1.js`。
- [2] `plot`：2,781 字符，enabled=True；审计副本 `technical/script_2.js`。
- [3] `手机`：743,791 字符，enabled=True；审计副本 `technical/script_3.js`。

## 数据流与审计分层

PNG → 卡片 data / character_book → 关键词及常驻候选 → Tavern Helper/模板/宿主处理 → 模型上下文；模型输出 → 变量更新、剧情定位、关系/CG规则 → 前端正则、手机、状态栏。

事实审计对象包括人物、世界、组织、地点、编年、剧情正文；技术审计对象包括初始化、变量持久化、剧情启停与正则；UI 本身的作者说明不自动判作 NPC 知識。只有确认进入生成提示或状态逻辑时，才判断信息泄漏。

本地图完成字段级盘点，不能替代全文内容核验；后续阅读与覆盖状态见 `reading_ledger.json`。

## 手机脚本内嵌的第二套资料（补充盘点）

script_3.js内嵌__mgCatalog，已以JSON解析器提取，未执行代码。包含75个人物档案、36个地区、23个势力、50个CG项目及10组别名。详见technical/phone_catalog.json。generatedFrom中的路径是卡片保存的历史构建标记，不代表当前目录有这些文件，也不具有Canon权威。

手机私聊等功能通过单独模型调用生成内容；其系统规则明示不得写入主线、MVU、好感或正文。当前数据会写入独立手机聊天状态。safeDossier按章节标题过滤人物资料，safePromptSnapshot读全局MVU快照，再做别名和长度处理。具体风险见S014–S016；不能把全部743791字符脚本计入主模型常驻token。

资料raw、sections与地图安全摘录可能保存同一实体的不同副本。已有原作人物不应仅因未出现在主世界书就计作整卡缺失；但手机内嵌资料也不保证正文模型可访问。

进一步运行验证尚未进行：未连接真实酒馆、未打开UI、未导入卡片、未执行任何远程依赖、未调用外部模型。全部字段解析完成不等于全部正文已核验。

## 续审02：正文覆盖增量（历史记录）

原卡结构、字段和提取副本未变。本轮另完整阅读ID91、ID92，累计48/143条正文；ID93仅前六事件定点比对，仍列未全文读。脚本、手机资料及HTML的原覆盖声明不变。本轮原著从L1286连续读至L4357；实时范围以reading_ledger.json为准。

## 续审03：正文覆盖增量

原始结构与提取副本未变。新增全文阅读ID93、94、95、119、121，累计53/143条正文；复查17、46、47、81等已读人物及3、5基础条目。当前源文连续已读L1—8658加既有L36130—38825，未以全文卡阅读替代源文核验。ID95超前到巡查的描述要从第111章继续对照；手机/HTML未全量审完、未运行宿主的声明不变。

## 续审04：正文覆盖增量

新增完整阅读ID33、60、70、96、97、114、172，累计60/143条；复查25、36、5、28。手机/HTML覆盖不变，未运行宿主。卡97的133章以后内容已读仅表示卡片阅读，不能计入原著已审范围。原著本轮L8659—11021连续已读，下一L11022；不改原始结构或提取副本。

## 续审05：正文覆盖增量

新增完整阅读ID53玛格丽特，累计61/143条；复查36、59、97。卡片所含卷二成长资料未借此计为原著已读。原著连续推进L11022—12944，卷一正文与附言均读完，下一卷二L12945。提取副本和技术资产未改，手机/HTML覆盖声明不变；未执行宿主。
