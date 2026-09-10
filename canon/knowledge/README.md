# Canon认知与信息壁垒数据库

**Stage 2B-4：完成。最终检查结果见 [Review](../STAGE2B4_REVIEW.md)。**
正式ID：K001–K235。207个TEMP均有处理去向；不更改原TEMP、Timeline、Character或Relationship。

本库分三件事：命题客观是否为真；谁在何时凭什么接触了多少；是否实际向另一个人披露。世界书有一条事实，不等角色或User能够读取。

## 先读哪里

- [恢复规则](RESTORE_POLICY.md)：如何按开局节点和主体选择可用信息，未知默认不授予。
- [TEMP迁移](TEMP_TO_K_MAP.md)：旧207条逐条去向、合并/拆分/空壳退役原因。
- [核心人物矩阵](KNOWLEDGE_MATRIX.md)、[认知变化索引](KNOWLEDGE_TRANSITIONS.md)、[披露链](DISCLOSURE_CHAINS.md)。
- [38个快照对照](SNAPSHOT_CHECK.md)、[172条关系边界对照](RELATIONSHIP_CROSSWALK.md)、[70人物扫描](CHARACTER_SCAN.md)。
- [结构化数据](records.json)、[只读查询](query_knowledge.py)、[群体定义](GROUP_SCOPE.md)。
- [本阶段统计](_build2b4/stats.json)、[检查结果](_build2b4/check_result.json)。

## Tier A入口

- [CH001 林昀](by_character/CH001_knowledge.md)
- [CH002 林小璐](by_character/CH002_knowledge.md)
- [CH003 夏凉](by_character/CH003_knowledge.md)
- [CH004 白静萱](by_character/CH004_knowledge.md)
- [CH005 红思与](by_character/CH005_knowledge.md)
- [CH006 安雅](by_character/CH006_knowledge.md)
- [CH007 麻生圆香](by_character/CH007_knowledge.md)
- [CH008 祖母绿](by_character/CH008_knowledge.md)
- [CH009 妮娜·克瑞吉欧斯](by_character/CH009_knowledge.md)
- [CH010 摩可](by_character/CH010_knowledge.md)

## 编号和状态规则

新增从下一K号追加；不得按字母、人物或年代重排ID。`Kxxx-Tnnn`只标某条中的获取/修正节点，节点号不代表故事时间。临时导入号继续保留在映射中。
`TRUE/FALSE/UNKNOWN`是命题真值；`CONFIRMED/PARTIAL/HEARD/SUSPECTS/MISUNDERSTANDS`等是主体状态。D口述可以证明“此人说过”，不能直接证明说法内容。
范围：PUBLIC、COMMON、ORGANIZATION_INTERNAL、ROLE_RESTRICTED、PRIVATE、SECRET、HIGHLY_SECRET、UNKNOWN_SCOPE。PRIVATE及以上敏感项没有证据便不授予；PUBLIC只是可接触，不是所有人已读。
上游有误只在Review登记。旧卡IF、原创坦白/会议、User全知与游戏规则均未采用。没有选择RP开局或进入下一阶段。

## 命题总目录

|ID/档案|明确命题|类型|客观真值|人物/组织导航|首见导航事件|私密/秘密|有阶段|错误认知|未决|
|---|---|---|---|---|---|---|---|---|---|
|[K001](K001.md)|白玫的日常身份是林小璐|秘密身份|TRUE|CH001,CH002|[EV0001](../01_master_timeline.md#ev0001)|True|True|False|False|
|[K002](K002.md)|当次受袭地点是湿地公园|地点|TRUE|CH001|[EV0002](../01_master_timeline.md#ev0002)|False|True|False|False|
|[K003](K003.md)|救援者使用翠雀代号|身份|TRUE|CH001,CH002|[EV0003](../01_master_timeline.md#ev0003)|False|True|False|False|
|[K004](K004.md)|摩可称自己偷跑后获播种者任命|组织成员|TRUE|CH001,CH010|[EV0004](../01_master_timeline.md#ev0004)|True|True|False|False|
|[K005](K005.md)|夏凉所见救援导师是魔法少女翠雀|身份|TRUE|CH001,CH003|[EV0005](../01_master_timeline.md#ev0005)|False|True|False|False|
|[K006](K006.md)|方亭下水道存在蛹巢|秘密地点|TRUE|CH001,CH005|[EV0006](../01_master_timeline.md#ev0006)|True|True|False|False|
|[K007](K007.md)|夏凉已经离家独居|私人秘密|TRUE|CH001,CH002,CH003|[EV0007](../01_master_timeline.md#ev0007)|True|True|False|False|
|[K008](K008.md)|林昀葬礼拥抱荼蘼意味着背弃安雅|动机认知|FALSE|CH001,CH003,CH006,CH040|[EV0008](../01_master_timeline.md#ev0008)|True|True|True|False|
|[K009](K009.md)|葬礼时有人经荼蘼劝林昀勿冲动追查|历史事件|TRUE|CH001,CH040|[EV0009](../01_master_timeline.md#ev0009)|True|True|False|False|
|[K010](K010.md)|荼蘼已在滨海断后牺牲|生死状态|TRUE|CH001,CH040|[EV0010](../01_master_timeline.md#ev0010)|False|True|False|True|
|[K011](K011.md)|摩可的播种者登记回复已经递达林昀|组织权限|TRUE|CH001,CH010|[EV0013](../01_master_timeline.md#ev0013)|True|True|False|False|
|[K012](K012.md)|爪痕与樱之死有因果关联|事件真相|UNKNOWN|CH001|[EV0013](../01_master_timeline.md#ev0013)|True|True|False|True|
|[K013](K013.md)|夏凉父亲已死且母亲因杀父入狱|私人秘密|TRUE|CH001,CH002,CH003|[EV0016](../01_master_timeline.md#ev0016)|True|True|False|False|
|[K014](K014.md)|红思与是已退役的朝颜|身份|TRUE|CH002,CH003,CH005|[EV0017](../01_master_timeline.md#ev0017)|False|True|False|False|
|[K015](K015.md)|花级不等于持有花牌|能力机制|TRUE|CH010,ORG002|[EV0017](../01_master_timeline.md#ev0017)|False|True|False|False|
|[K016](K016.md)|纪念日林昀外出是为与安雅的纪念日选礼|动机认知|TRUE|CH001,CH002,CH006|[EV0018](../01_master_timeline.md#ev0018)|True|True|False|False|
|[K017](K017.md)|林昀在女儿坦白前已经知道她是白玫|人际关系|TRUE|CH001,CH002|[EV0020](../01_master_timeline.md#ev0020)|True|True|False|False|
|[K018](K018.md)|林昀与翠雀是同一人|秘密身份|TRUE|CH001,CH002,CH003,CH004,CH005,CH006,CH007|[EV0189](../01_master_timeline.md#ev0189)|True|True|False|False|
|[K019](K019.md)|安雅曾与翠雀在旧方亭小队共同活动|人际关系|TRUE|CH001,CH002,CH003,CH006|[EV0020](../01_master_timeline.md#ev0020)|True|True|False|False|
|[K020](K020.md)|安雅的魔法少女身份是樱且持终身资格|身份|TRUE|CH002,CH003,CH006|[EV0021](../01_master_timeline.md#ev0021)|True|True|False|False|
|[K021](K021.md)|安雅死后遗体消散|历史事件|TRUE|CH006|[EV0021](../01_master_timeline.md#ev0021)|True|False|False|False|
|[K022](K022.md)|夏凉在EV0022晋升芽级|能力机制|TRUE|CH001,CH002,CH003|[EV0022](../01_master_timeline.md#ev0022)|False|True|False|False|
|[K023](K023.md)|摩可已向白静萱许诺变身能治病和复眼|人际关系|TRUE|CH004,CH010|[EV0024](../01_master_timeline.md#ev0024)|True|True|False|False|
|[K024](K024.md)|福利院黑袍人在寻找白静萱|战斗情报|TRUE|CH004|[EV0025](../01_master_timeline.md#ev0025)|True|True|False|False|
|[K025](K025.md)|白静萱已成为魔法少女薄雪|身份|TRUE|CH004,CH031|[EV0026](../01_master_timeline.md#ev0026)|True|True|False|False|
|[K026](K026.md)|薄雪的魔力在本次救援中具有疗伤效果|能力机制|TRUE|CH004|[EV0026](../01_master_timeline.md#ev0026)|False|True|False|False|
|[K027](K027.md)|救援少女之一使用翠雀代号|身份|TRUE|CH001,CH039|[EV0027](../01_master_timeline.md#ev0027)|False|True|False|False|
|[K028](K028.md)|麻雀袭击的蓝色少女是矢车菊|秘密身份|TRUE|CH001,CH036|[EV0028](../01_master_timeline.md#ev0028)|True|True|False|False|
|[K029](K029.md)|福利院的新人可能已陷危险|战斗情报|TRUE|CH001|[EV0029](../01_master_timeline.md#ev0029)|True|True|False|False|
|[K030](K030.md)|林昀与王腾飞认出的矢车菊存在同一身份关联|秘密身份|TRUE|CH001,CH047|[EV0030](../01_master_timeline.md#ev0030)|True|True|False|False|
|[K031](K031.md)|福利院新人合战击退了兵触三的进攻|战斗情报|TRUE|CH001,CH039|[EV0031](../01_master_timeline.md#ev0031)|False|True|False|False|
|[K032](K032.md)|樱曾经救过白静萱|历史事件|TRUE|CH001,CH004|[EV0032](../01_master_timeline.md#ev0032)|True|True|False|False|
|[K033](K033.md)|翠雀的旧代号是矢车菊|秘密身份|TRUE|CH001,CH002,CH003,CH012,CH013,CH030,CH032,CH035,CH036,CH039|[EV0028](../01_master_timeline.md#ev0028)|True|True|False|False|
|[K034](K034.md)|樱只是离开方亭，仍可与白静萱重逢|生死状态|FALSE|CH001,CH004|[EV0032](../01_master_timeline.md#ev0032)|True|True|True|False|
|[K035](K035.md)|樱案存在黑烬方面的调查线索|事件真相|TRUE|CH001|[EV0034](../01_master_timeline.md#ev0034)|True|True|False|False|
|[K036](K036.md)|薄雪的当期治疗能修好翠雀旧本相伤|能力限制|FALSE|CH001,CH004|[EV0035](../01_master_timeline.md#ev0035)|True|True|True|False|
|[K037](K037.md)|旧方亭队按林安、玛、苏、红逐步组成|历史事件|TRUE|CH003|[EV0039](../01_master_timeline.md#ev0039)|True|True|False|False|
|[K038](K038.md)|翠雀在生日出游时向夏凉表示双方是朋友伙伴|人际关系|TRUE|CH001,CH003|[EV0038](../01_master_timeline.md#ev0038)|True|True|False|False|
|[K039](K039.md)|林昀原本是女性，后来变成男性|秘密身份|FALSE|CH001,CH003|[EV0039](../01_master_timeline.md#ev0039)|True|True|True|False|
|[K040](K040.md)|猫尾调查队在柏安失踪|战斗情报|TRUE|CH001,CH021|[EV0040](../01_master_timeline.md#ev0040)|True|True|False|False|
|[K041](K041.md)|翠雀将暂离方亭赴柏安并安排留守教学|计划|TRUE|CH001,CH002,CH003,CH004|[EV0041](../01_master_timeline.md#ev0041)|False|True|False|False|
|[K042](K042.md)|白蓟验到翠雀出示的认证牌写着矢车菊|身份|TRUE|CH001,CH023|[EV0042](../01_master_timeline.md#ev0042)|False|True|False|False|
|[K043](K043.md)|木百合被林昀暗算、再获另一个人翠雀救助|事件真相|FALSE|CH001,CH024|[EV0042](../01_master_timeline.md#ev0042)|True|True|True|False|
|[K044](K044.md)|猫尾队从爪痕线转查黑烬且出现多起失踪|战斗情报|TRUE|CH001,CH021|[EV0043](../01_master_timeline.md#ev0043)|True|True|False|False|
|[K045](K045.md)|黑烬供词中有军、卫、侍等层级|组织存在|TRUE|CH001|[EV0044](../01_master_timeline.md#ev0044)|True|True|False|False|
|[K046](K046.md)|本次蛛巢的覆盖网影响缠绕拘束|能力机制|TRUE|CH001|[EV0045](../01_master_timeline.md#ev0045)|False|True|False|False|
|[K047](K047.md)|至少另四城出现类似异常线索|战斗情报|TRUE|CH001|[EV0046](../01_master_timeline.md#ev0046)|True|True|False|False|
|[K048](K048.md)|白静萱已经觉醒天音|能力机制|TRUE|CH001,CH004|[EV0047](../01_master_timeline.md#ev0047)|False|True|False|False|
|[K049](K049.md)|白静萱首次见到林昀的男性日常形态|身份|TRUE|CH001,CH004|[EV0048](../01_master_timeline.md#ev0048)|True|True|False|False|
|[K050](K050.md)|月圆节当晚林昀收到新的危险警告|战斗情报|TRUE|CH001,CH005|[EV0048](../01_master_timeline.md#ev0048)|True|True|False|False|
|[K051](K051.md)|局中部分残兽由职员被缝合而成|事件真相|TRUE|CH001|[EV0049](../01_master_timeline.md#ev0049)|True|True|False|False|
|[K052](K052.md)|红思与受控制而不能自由说出幕后信息|私人秘密|TRUE|CH001,CH005|[EV0049](../01_master_timeline.md#ev0049)|True|True|False|False|
|[K053](K053.md)|林昀与安雅准备订婚|家庭关系|TRUE|CH001,CH005,CH006|[EV0051](../01_master_timeline.md#ev0051)|True|True|False|False|
|[K054](K054.md)|红思与遭摩丝暗算并持续受控|事件真相|TRUE|CH005,CH012|[EV0052](../01_master_timeline.md#ev0052)|True|False|False|False|
|[K055](K055.md)|警告手机对应的接收者是一位巡查使|组织成员|TRUE|CH011|[EV0053](../01_master_timeline.md#ev0053)|True|True|False|False|
|[K056](K056.md)|匿名警告链由红交手机给妮妮而启动|事件真相|TRUE|CH005,CH011|[EV0053](../01_master_timeline.md#ev0053)|True|False|False|False|
|[K057](K057.md)|紅思与本次仍能被救回人形|伤势|TRUE|CH005|[EV0054](../01_master_timeline.md#ev0054)|True|True|False|False|
|[K058](K058.md)|摩丝的黑烬身份是蛾|秘密身份|TRUE|CH002,CH003,CH004,CH012|[EV0055](../01_master_timeline.md#ev0055)|True|True|False|False|
|[K059](K059.md)|蛾向白揭出樱死及小璐母女关系，白受到冲击|事件真相|TRUE|CH002,CH004|[EV0055](../01_master_timeline.md#ev0055)|True|True|False|False|
|[K060](K060.md)|摩丝使用嵌入魔力源的人兽改造技术|能力机制|TRUE|CH001,CH012|[EV0056](../01_master_timeline.md#ev0056)|True|True|False|False|
|[K061](K061.md)|巨蛾影子覆盖范围限制其夺魔作用|能力限制|TRUE|CH001|[EV0057](../01_master_timeline.md#ev0057)|False|True|False|False|
|[K062](K062.md)|翠雀奇境在此战分离兽概念救回缝合者|能力机制|TRUE|CH001|[EV0059](../01_master_timeline.md#ev0059)|False|True|False|False|
|[K063](K063.md)|翠雀与白玫的父亲是同一主体|秘密身份|TRUE|CH001,CH002,CH012|[EV0060](../01_master_timeline.md#ev0060)|True|True|False|False|
|[K064](K064.md)|翠雀曾赴柏安且与方亭有关联|地点|TRUE|CH001,CH007|[EV0061](../01_master_timeline.md#ev0061)|True|True|False|False|
|[K065](K065.md)|疑携樱宝石的被追小队已全灭|事件真相|UNKNOWN|CH001|[EV0062](../01_master_timeline.md#ev0062)|True|True|False|True|
|[K066](K066.md)|林昀已就任方亭异策局局长|身份|TRUE|CH001,CH002,CH024,CH031|[EV0063](../01_master_timeline.md#ev0063)|False|True|False|False|
|[K067](K067.md)|就任大会揭出六名潜伏暗子|组织成员|TRUE|仅客观/读者导航|[EV0064](../01_master_timeline.md#ev0064)|True|True|False|False|
|[K068](K068.md)|祖母绿提出用兽之源协助修复残存本相|计划|TRUE|CH001,CH008|[EV0065](../01_master_timeline.md#ev0065)|True|True|False|False|
|[K069](K069.md)|林昀将和翠雀结婚从而共同收养白静萱|家庭关系|FALSE|CH001,CH004|[EV0067](../01_master_timeline.md#ev0067)|True|True|True|False|
|[K070](K070.md)|白狼曾担任紫钻|秘密身份|TRUE|CH001,CH014,ORG009|[EV0068](../01_master_timeline.md#ev0068)|True|True|False|False|
|[K071](K071.md)|湖畔春天绑人和袭局佯攻属于同一陷阱|战斗情报|TRUE|CH001|[EV0069](../01_master_timeline.md#ev0069)|True|True|False|False|
|[K072](K072.md)|兵蜂七说白的父母是黑烬研究员|家庭关系|TRUE|CH001,CH004,CH067|[EV0070](../01_master_timeline.md#ev0070)|True|True|False|False|
|[K073](K073.md)|翠雀答应担任白静萱的妈妈式照护者|家庭关系|TRUE|CH001,CH003,CH004|[EV0071](../01_master_timeline.md#ev0071)|True|True|False|False|
|[K074](K074.md)|小璐为曙草付费与母亲形象投射有关|动机认知|TRUE|CH001,CH002|[EV0072](../01_master_timeline.md#ev0072)|True|True|False|False|
|[K075](K075.md)|鸢接到带走薄雪及矢车菊的额外任务|计划|TRUE|CH001,CH004,CH028|[EV0073](../01_master_timeline.md#ev0073)|True|True|False|False|
|[K076](K076.md)|陆红豆曾是唐菖蒲、现作为鸢参与爪痕行动|秘密身份|TRUE|CH001,CH013|[EV0073](../01_master_timeline.md#ev0073)|True|True|False|False|
|[K077](K077.md)|朝颜已恢复魔力并能参战|能力机制|TRUE|CH001,CH005|[EV0074](../01_master_timeline.md#ev0074)|False|True|False|False|
|[K078](K078.md)|百武能把气作物理化运用|能力机制|TRUE|CH001|[EV0075](../01_master_timeline.md#ev0075)|False|True|False|False|
|[K079](K079.md)|祖母绿提出为红用本相制作临时本体|计划|TRUE|CH001,CH008|[EV0076](../01_master_timeline.md#ev0076)|True|True|False|False|
|[K080](K080.md)|夏凉和白向翠雀转述小璐的商城目击|人际关系|TRUE|CH001,CH002,CH003|[EV0077](../01_master_timeline.md#ev0077)|True|True|False|False|
|[K081](K081.md)|翠雀关爱小璐是因喜欢安雅|动机认知|UNKNOWN|CH001,CH002,CH006|[EV0077](../01_master_timeline.md#ev0077)|True|True|False|True|
|[K082](K082.md)|林昀准许白静萱叫爸爸并承诺照护|家庭关系|TRUE|CH001,CH004|[EV0078](../01_master_timeline.md#ev0078)|True|True|False|False|
|[K083](K083.md)|林昀查得登记生日不等于2月14日|私人秘密|TRUE|CH001|[EV0079](../01_master_timeline.md#ev0079)|True|True|False|False|
|[K084](K084.md)|孩子报告的陌生支援少女与翠雀旧识可能相关|身份|UNKNOWN|CH001|[EV0080](../01_master_timeline.md#ev0080)|True|True|False|True|
|[K085](K085.md)|麻生圆香的魔法少女身份是玛格丽特|秘密身份|TRUE|CH001,CH007|[EV0081](../01_master_timeline.md#ev0081)|True|True|False|False|
|[K086](K086.md)|演唱会台上的歌手是当年的玛格丽特|秘密身份|TRUE|CH001,CH007|[EV0082](../01_master_timeline.md#ev0082)|True|True|False|False|
|[K087](K087.md)|翠雀与歌手玛格丽特是旧队友|人际关系|TRUE|CH001,CH003,CH004,CH007|[EV0082](../01_master_timeline.md#ev0082)|True|True|False|False|
|[K088](K088.md)|玛在葬礼前已由猫眼得知安雅死讯并受劝阻|历史事件|TRUE|CH001,CH006,CH007,CH034|[EV0083](../01_master_timeline.md#ev0083)|True|True|False|False|
|[K089](K089.md)|白蓟与小璐进行过造成冲突的私比|人际关系|TRUE|CH001,CH002,CH023|[EV0084](../01_master_timeline.md#ev0084)|True|True|False|False|
|[K090](K090.md)|两队导师曾将战胜柏安作为参考条件，后撤销|组织权限|TRUE|CH002,CH003,CH004,CH023,CH024,CH025|[EV0085](../01_master_timeline.md#ev0085)|False|True|False|False|
|[K091](K091.md)|翠雀计划借假考生身份赴国度治疗|计划|TRUE|CH001,CH007|[EV0085](../01_master_timeline.md#ev0085)|True|True|False|False|
|[K092](K092.md)|苏胜紫最后通话时称准备独自去间界|计划|TRUE|CH001,CH005,CH007,CH018|[EV0086](../01_master_timeline.md#ev0086)|True|True|False|False|
|[K093](K093.md)|翠雀近期出现变身失控和魔丝自行打结|伤势|TRUE|CH001,CH005,CH007|[EV0087](../01_master_timeline.md#ev0087)|True|True|False|False|
|[K094](K094.md)|翠雀向夏教授屏障符文与爆术组合|能力机制|TRUE|CH001,CH003|[EV0088](../01_master_timeline.md#ev0088)|False|True|False|False|
|[K095](K095.md)|浊化模拟偏移而不改变魔力底色|能力机制|TRUE|CH001|[EV0089](../01_master_timeline.md#ev0089)|False|True|False|False|
|[K096](K096.md)|小璐在交流赛主动放出穿防银白魔力|能力机制|TRUE|CH001,CH002,CH007|[EV0090](../01_master_timeline.md#ev0090)|False|True|False|False|
|[K097](K097.md)|兽之源在鸢报告时已交祖母绿|事件真相|TRUE|CH008,CH014|[EV0091](../01_master_timeline.md#ev0091)|True|True|False|False|
|[K098](K098.md)|父亲林昀和翠雀正在恋爱|人际关系|FALSE|CH001,CH002|[EV0092](../01_master_timeline.md#ev0092)|True|True|True|False|
|[K099](K099.md)|白静萱在局内称林昀为爸爸|家庭关系|TRUE|CH001,CH004|[EV0092](../01_master_timeline.md#ev0092)|True|True|False|False|
|[K100](K100.md)|林小璐是林昀的亲生女儿|家庭关系|TRUE|CH001,CH002,CH013|[EV0093](../01_master_timeline.md#ev0093)|True|True|False|False|
|[K101](K101.md)|银屏山装置能破坏防网并引来兽潮|战斗情报|PARTIALLY_TRUE|CH001,CH002,CH003,CH004,CH005,CH007,CH023,CH024,CH025|[EV0094](../01_master_timeline.md#ev0094)|False|True|False|False|
|[K102](K102.md)|鸢的兽变是心解而非魔法少女繁开|能力机制|TRUE|CH007|[EV0094](../01_master_timeline.md#ev0094)|False|True|False|False|
|[K103](K103.md)|薄雪在银屏山展现黑绿兽形|能力机制|TRUE|CH002,CH003,CH004,CH005,CH007,CH023,CH024,CH025|[EV0096](../01_master_timeline.md#ev0096)|False|True|False|False|
|[K104](K104.md)|白静萱就是鸢任务要求带走的薄雪|战斗情报|TRUE|CH004,CH013|[EV0096](../01_master_timeline.md#ev0096)|True|True|False|False|
|[K105](K105.md)|翠雀杯底的低比例意味着当场濒死|伤势|FALSE|CH001,CH005|[EV0097](../01_master_timeline.md#ev0097)|True|True|True|False|
|[K106](K106.md)|塞米是一只来自间界的妖精|身份|TRUE|CH002,CH003,CH023,CH025,CH028|[EV0098](../01_master_timeline.md#ev0098)|False|True|False|False|
|[K107](K107.md)|塞米此巢可用睁闭眼改变相互感知|能力机制|TRUE|CH002,CH025,CH028|[EV0099](../01_master_timeline.md#ev0099)|False|True|False|False|
|[K108](K108.md)|石塔是辅助装置而非主要储供魔核心|能力机制|TRUE|CH003,CH023|[EV0100](../01_master_timeline.md#ev0100)|False|True|False|False|
|[K109](K109.md)|翠雀只把小璐当成樱的替身|动机认知|FALSE|CH001,CH002|[EV0101](../01_master_timeline.md#ev0101)|True|True|True|False|
|[K110](K110.md)|白静萱被黑烬列作祭子|身份|TRUE|CH001,CH002,CH003,CH004,CH007,CH008,ORG011|[EV0026](../01_master_timeline.md#ev0026)|True|True|False|False|
|[K111](K111.md)|龙胆假宝石用于伪造身份记录而不重塑身体|能力限制|TRUE|CH001|[EV0103](../01_master_timeline.md#ev0103)|True|True|False|False|
|[K112](K112.md)|旧书记所记录的异常指向王之门|事件真相|UNKNOWN|CH001|[EV0105](../01_master_timeline.md#ev0105)|True|True|False|True|
|[K113](K113.md)|王钥第三晶石波动预示另一未显形态|能力机制|UNKNOWN|CH001|[EV0106](../01_master_timeline.md#ev0106)|True|True|False|True|
|[K114](K114.md)|木百合被父亲送至琴行后实际上遭遗弃|家庭关系|TRUE|CH001,CH024|[EV0107](../01_master_timeline.md#ev0107)|True|True|False|False|
|[K115](K115.md)|木百合的父亲会回来接她|家庭关系|UNKNOWN|CH024|[EV0107](../01_master_timeline.md#ev0107)|True|True|False|True|
|[K116](K116.md)|兽之源已转往卢恩诺雷研究所|地点|UNKNOWN|仅客观/读者导航|[EV0108](../01_master_timeline.md#ev0108)|True|True|False|True|
|[K117](K117.md)|翠雀向三新人说明自己要用假名执行秘密任务|计划|TRUE|CH001,CH002,CH003,CH004|[EV0109](../01_master_timeline.md#ev0109)|True|True|False|False|
|[K118](K118.md)|龙胆是一名十岁的真实新人|身份|FALSE|CH030|[EV0109](../01_master_timeline.md#ev0109)|True|True|True|False|
|[K119](K119.md)|祖母绿本次用爱之源修复翠雀残存宝石|能力机制|TRUE|CH001,CH008|[EV0110](../01_master_timeline.md#ev0110)|True|True|False|False|
|[K120](K120.md)|妮娜为姐妹同队向石蒜付出回响|动机认知|TRUE|CH001,CH009|[EV0111](../01_master_timeline.md#ev0111)|True|True|False|False|
|[K121](K121.md)|翠雀治疗后魂痛消失且奇境可再次展开|伤势|TRUE|CH001|[EV0112](../01_master_timeline.md#ev0112)|True|True|False|False|
|[K122](K122.md)|陵园摘面具少女是妮娜即墨荷|秘密身份|TRUE|CH001,CH009|[EV0113](../01_master_timeline.md#ev0113)|True|True|False|False|
|[K123](K123.md)|墨荷声称当前为国度执行任务|组织成员|UNKNOWN|CH001,CH009|[EV0113](../01_master_timeline.md#ev0113)|True|True|False|True|
|[K124](K124.md)|林昀选择2月14作为纪念生日|私人秘密|TRUE|CH001,CH002|[EV0114](../01_master_timeline.md#ev0114)|True|True|False|False|
|[K125](K125.md)|墨荷当前团队与爪痕有关联|组织成员|TRUE|CH001,CH009,ORG009|[EV0115](../01_master_timeline.md#ev0115)|True|True|False|False|
|[K126](K126.md)|墨荷团队声称能修复翠雀的魔装损失|计划|UNKNOWN|CH001,CH009|[EV0115](../01_master_timeline.md#ev0115)|True|True|False|True|
|[K127](K127.md)|翠雀收到王冠巧克力后因安雅往事落泪|动机认知|TRUE|CH001,CH002,CH006|[EV0116](../01_master_timeline.md#ev0116)|True|True|False|False|
|[K128](K128.md)|郁金香正在墨荷身边活动|组织成员|TRUE|CH001,CH009,CH015|[EV0117](../01_master_timeline.md#ev0117)|True|True|False|False|
|[K129](K129.md)|矢车菊讨厌妮娜|人际关系|FALSE|CH001,CH009|[EV0118](../01_master_timeline.md#ev0118)|True|True|True|False|
|[K130](K130.md)|郁金香目前使用金蛇代号|秘密身份|TRUE|CH001,CH015|[EV0120](../01_master_timeline.md#ev0120)|True|True|False|False|
|[K131](K131.md)|矢车菊已返回国度|身份|TRUE|CH001|[EV0120](../01_master_timeline.md#ev0120)|False|True|False|False|
|[K132](K132.md)|翠雀有意成为蓝宝石权杖|计划|TRUE|CH001,CH002,CH003,CH004,ORG002|[EV0121](../01_master_timeline.md#ev0121)|True|True|False|False|
|[K133](K133.md)|藏箱的女孩是折鹤兰的女儿|家庭关系|FALSE|CH033|[EV0122](../01_master_timeline.md#ev0122)|True|True|True|False|
|[K134](K134.md)|本届笔试存在混乱术干扰并获处理|事件真相|TRUE|仅客观/读者导航|[EV0123](../01_master_timeline.md#ev0123)|False|True|False|False|
|[K135](K135.md)|小璐笔试失常不全是未努力背书|事件真相|TRUE|CH002|[EV0123](../01_master_timeline.md#ev0123)|True|True|False|False|
|[K136](K136.md)|龙胆是一个与翠雀不同的新人前辈|身份|FALSE|CH001,CH032|[EV0124](../01_master_timeline.md#ev0124)|True|True|True|False|
|[K137](K137.md)|本场迷宫暗规四公布解谜奖励与专属捷径|组织权限|TRUE|仅客观/读者导航|[EV0125](../01_master_timeline.md#ev0125)|False|True|False|False|
|[K138](K138.md)|引离能在本次迷宫移开植物墙的局部枝条|能力机制|TRUE|CH003,CH055,CH056|[EV0126](../01_master_timeline.md#ev0126)|False|True|False|False|
|[K139](K139.md)|本场迷宫广播暗规五规定节点全破后出现出口|组织权限|TRUE|仅客观/读者导航|[EV0127](../01_master_timeline.md#ev0127)|False|True|False|False|
|[K140](K140.md)|墨荷的爪痕代号是黑猫|秘密身份|TRUE|CH001,CH009,ORG009|[EV0169](../01_master_timeline.md#ev0169)|True|True|False|True|
|[K141](K141.md)|测绘队掌握的地图提供迷宫出口候选位置|地点|TRUE|CH003|[EV0129](../01_master_timeline.md#ev0129)|False|True|False|False|
|[K142](K142.md)|薄荷与箭根薯疑涉黑烬|组织成员|TRUE|CH001|[EV0130](../01_master_timeline.md#ev0130)|True|True|False|False|
|[K143](K143.md)|薄荷向小璐和白说明兽子、祭子与食祭的部分定义|能力机制|TRUE|CH002,CH004|[EV0131](../01_master_timeline.md#ev0131)|True|True|False|False|
|[K144](K144.md)|薄荷提供箭、醉、羊、蛇及自己的黑烬名单|组织成员|TRUE|CH001,ORG011|[EV0131](../01_master_timeline.md#ev0131)|True|True|False|False|
|[K145](K145.md)|薄雪检测数据呈现偏移|能力机制|TRUE|CH004|[EV0132](../01_master_timeline.md#ev0132)|False|True|False|False|
|[K146](K146.md)|王钥检测显示具备权杖潜力|能力机制|PARTIALLY_TRUE|CH001,CH008|[EV0132](../01_master_timeline.md#ev0132)|True|True|False|False|
|[K147](K147.md)|白玫的正式公示评级是SS|能力机制|TRUE|CH002,ORG002|[EV0133](../01_master_timeline.md#ev0133)|False|True|False|False|
|[K148](K148.md)|女王已通过指示渠道关注白玫|政治信息|TRUE|CH001,CH002,CH017|[EV0133](../01_master_timeline.md#ev0133)|False|True|False|False|
|[K149](K149.md)|王钥尚有不圆满之处|能力限制|UNKNOWN|CH001|[EV0134](../01_master_timeline.md#ev0134)|True|True|False|True|
|[K150](K150.md)|樱是小璐的母亲|家庭关系|TRUE|CH002,CH004,CH029|[EV0021](../01_master_timeline.md#ev0021)|True|True|False|False|
|[K151](K151.md)|新紫钻培养小璐的条件包含留国并远离矢车菊|计划|TRUE|CH001,CH002,CH029|[EV0135](../01_master_timeline.md#ev0135)|True|True|False|False|
|[K152](K152.md)|箭根薯血蝠能够从伤口吸取魔力|能力机制|TRUE|CH002|[EV0136](../01_master_timeline.md#ev0136)|False|True|False|False|
|[K153](K153.md)|王钥基础形态每次析出仅附一次回魔，之后需自充|能力限制|TRUE|CH002|[EV0136](../01_master_timeline.md#ev0136)|True|True|False|False|
|[K154](K154.md)|龙胆是矢车菊的女儿|家庭关系|FALSE|CH001,CH002,CH030,CH032|[EV0137](../01_master_timeline.md#ev0137)|True|True|True|False|
|[K155](K155.md)|龙胆携带秘密任务且考核有内幕|计划|TRUE|CH030,CH032,ORG003|[EV0137](../01_master_timeline.md#ev0137)|True|True|False|False|
|[K156](K156.md)|箭根薯必须维持完整人形才能施符|能力限制|FALSE|CH002|[EV0138](../01_master_timeline.md#ev0138)|False|True|True|False|
|[K157](K157.md)|夏凉在云境末日仍遭追逐|战斗情报|TRUE|CH001,CH003|[EV0139](../01_master_timeline.md#ev0139)|True|True|False|False|
|[K158](K158.md)|黑猫另有未向金蛇说明的任务|计划|TRUE|CH009,CH015|[EV0140](../01_master_timeline.md#ev0140)|True|True|False|False|
|[K159](K159.md)|郁金香预感的灾难将发生|战斗情报|UNKNOWN|CH001,CH015|[EV0141](../01_master_timeline.md#ev0141)|True|True|False|True|
|[K160](K160.md)|此前半蜕是敌方针对后续攻城的试演|事件真相|UNKNOWN|CH001,CH009|[EV0142](../01_master_timeline.md#ev0142)|True|True|False|True|
|[K161](K161.md)|妮姆在墨荷当次亲验时安全|生死状态|TRUE|CH009,CH020|[EV0142](../01_master_timeline.md#ev0142)|True|True|False|False|
|[K162](K162.md)|战场出现第二只羽|战斗情报|TRUE|仅客观/读者导航|[EV0143](../01_master_timeline.md#ev0143)|False|True|False|False|
|[K163](K163.md)|石蒜在矢与墨离开后独自昙开|历史事件|TRUE|CH001,CH009|[EV0144](../01_master_timeline.md#ev0144)|True|True|False|False|
|[K164](K164.md)|墨荷猜握今可为救矢找到规避崩毁办法|计划|TRUE|CH009|[EV0145](../01_master_timeline.md#ev0145)|True|True|False|False|
|[K165](K165.md)|握今在该战暂缓了矢的崩毁|能力机制|TRUE|CH001|[EV0145](../01_master_timeline.md#ev0145)|True|True|False|False|
|[K166](K166.md)|战后处理伤员的妖精人员自述效忠国度|组织成员|TRUE|CH001|[EV0146](../01_master_timeline.md#ev0146)|True|True|False|False|
|[K167](K167.md)|妮姆在战争中死亡|生死状态|TRUE|CH001,CH020|[EV0147](../01_master_timeline.md#ev0147)|True|True|False|False|
|[K168](K168.md)|妮姆最后以踏明引兽离开平民并冲向雷区|历史事件|TRUE|CH001,CH020|[EV0148](../01_master_timeline.md#ev0148)|True|True|False|False|
|[K169](K169.md)|龙胆与翠雀是同一名魔法少女|秘密身份|TRUE|CH001,CH030,CH032|[EV0149](../01_master_timeline.md#ev0149)|True|True|False|False|
|[K170](K170.md)|褐鹈原本是魔法少女木槿|秘密身份|TRUE|CH046|[EV0150](../01_master_timeline.md#ev0150)|True|True|False|False|
|[K171](K171.md)|祖母绿在金蛇交易中保留特定经历并查账反制|能力机制|TRUE|CH008,CH015|[EV0151](../01_master_timeline.md#ev0151)|True|True|False|False|
|[K172](K172.md)|薄荷与箭根薯是共同生活过的姐妹并卷入食祭|家庭关系|TRUE|CH002,CH004,CH026,CH027|[EV0152](../01_master_timeline.md#ev0152)|True|True|False|False|
|[K173](K173.md)|白狼使用妃黛莉之名|身份|TRUE|CH014|[EV0153](../01_master_timeline.md#ev0153)|True|False|False|False|
|[K174](K174.md)|本届末场考核已经暂停并组织撤离|组织权限|TRUE|仅客观/读者导航|[EV0154](../01_master_timeline.md#ev0154)|False|True|False|False|
|[K175](K175.md)|本次袭击目标可能是女王|计划|TRUE|CH002,CH004,CH017,CH026,CH027|[EV0156](../01_master_timeline.md#ev0156)|True|True|False|False|
|[K176](K176.md)|可以用改成残兽底色替代少女力量失效|能力机制|UNKNOWN|CH001|[EV0157](../01_master_timeline.md#ev0157)|True|True|False|True|
|[K177](K177.md)|恨今难握通过时间错位表现作用|能力机制|UNKNOWN|CH001|[EV0158](../01_master_timeline.md#ev0158)|True|True|False|True|
|[K178](K178.md)|幻命织华在末战造成特定胜负结果|战斗情报|UNKNOWN|仅客观/读者导航|[EV0158](../01_master_timeline.md#ev0158)|False|False|False|True|
|[K179](K179.md)|开篇方亭已有新任魔法少女公开出战|身份|TRUE|CH001|[EV0160](../01_master_timeline.md#ev0160)|False|True|False|False|
|[K180](K180.md)|林昀曾参加花园防卫战|历史事件|TRUE|CH001,CH005|[EV0161](../01_master_timeline.md#ev0161)|True|True|False|False|
|[K181](K181.md)|小璐在比试前已由玛教会浊化操作|能力机制|TRUE|CH002|[EV0162](../01_master_timeline.md#ev0162)|True|True|False|False|
|[K182](K182.md)|妮妮已获返国观察培训通知，摩可正式任职文件尚待送达|组织权限|TRUE|CH001,CH010,CH011|[EV0163](../01_master_timeline.md#ev0163)|True|True|False|False|
|[K183](K183.md)|田胜在福利院曾主动施术救人|历史事件|TRUE|CH031|[EV0025](../01_master_timeline.md#ev0025)|True|True|True|False|
|[K184](K184.md)|白静萱的魔力底色由残兽偏向魔法少女|能力机制|TRUE|CH001,CH002,CH004,CH008|[EV0068](../01_master_timeline.md#ev0068)|True|True|True|False|
|[K185](K185.md)|林昀是女王单独创造、没有其他亲源的孩子|家庭关系|UNKNOWN|CH001,CH009,CH017,ORG001|[EV0176](../01_master_timeline.md#ev0176)|True|True|False|True|
|[K186](K186.md)|少女力量的延续依赖女王|能力机制|UNKNOWN|CH001,CH009,CH017|[EV0176](../01_master_timeline.md#ev0176)|True|True|False|True|
|[K187](K187.md)|安雅已经死亡|生死状态|TRUE|CH001,CH002,CH004,CH006,CH007|[EV0009](../01_master_timeline.md#ev0009)|True|True|False|False|
|[K188](K188.md)|白静萱正在准备返校|计划|TRUE|CH002,CH004|[EV0186](../01_master_timeline.md#ev0186)|True|True|False|False|
|[K189](K189.md)|当晚的残兽可能给新人带来危险|战斗情报|TRUE|CH001|[EV0188](../01_master_timeline.md#ev0188)|True|True|False|False|
|[K190](K190.md)|林昀能与心之种建立连接|能力机制|TRUE|CH001,CH042|[EV0189](../01_master_timeline.md#ev0189)|True|True|False|False|
|[K191](K191.md)|翠雀当场报出花牌41076|组织权限|TRUE|CH001,CH002|[EV0003](../01_master_timeline.md#ev0003)|False|True|False|False|
|[K192](K192.md)|夏凉知道林小璐是魔法少女白玫|秘密身份|TRUE|CH002,CH003|[EV0005](../01_master_timeline.md#ev0005)|False|True|False|False|
|[K193](K193.md)|合照显示安雅与旧队成员的旧交|人际关系|TRUE|CH002,CH003,CH006|[EV0020](../01_master_timeline.md#ev0020)|True|True|False|False|
|[K194](K194.md)|当期引离已经表现魔力反射和传输|能力机制|TRUE|CH001,CH002|[EV0022](../01_master_timeline.md#ev0022)|False|True|False|False|
|[K195](K195.md)|变身可以让白静萱缺失的肉眼永久再生|能力机制|UNKNOWN|CH004|[EV0024](../01_master_timeline.md#ev0024)|True|True|False|True|
|[K196](K196.md)|白静萱是福利院来袭者追索的目标|战斗情报|TRUE|CH004,CH031|[EV0026](../01_master_timeline.md#ev0026)|True|True|False|False|
|[K197](K197.md)|工触十一已经死亡|生死状态|TRUE|CH039|[EV0027](../01_master_timeline.md#ev0027)|False|True|False|False|
|[K198](K198.md)|林昀男性身份只是女孩矢车菊的社会伪装|秘密身份|FALSE|CH001,CH047|[EV0030](../01_master_timeline.md#ev0030)|True|True|True|False|
|[K199](K199.md)|局长宣布审查资格后提供魔法武装|计划|TRUE|仅客观/读者导航|[EV0064](../01_master_timeline.md#ev0064)|True|True|False|False|
|[K200](K200.md)|两份兽之源曾按祖母绿所述分别分流到爪痕相关方|历史事件|UNKNOWN|CH001,CH008,ORG009|[EV0068](../01_master_timeline.md#ev0068)|True|True|False|True|
|[K201](K201.md)|白静萱的父母因她而死且恶意利用她|家庭关系|UNKNOWN|CH004|[EV0070](../01_master_timeline.md#ev0070)|True|True|False|True|
|[K202](K202.md)|朝颜的繁开名为忆海百记并涉及记录复制|能力机制|TRUE|CH001,CH005|[EV0074](../01_master_timeline.md#ev0074)|True|True|False|False|
|[K203](K203.md)|退役后红思与已经恢复魔力的个案存在|能力机制|TRUE|CH001,CH005|[EV0076](../01_master_timeline.md#ev0076)|True|True|False|False|
|[K204](K204.md)|陆红豆知道林小璐是魔法少女|秘密身份|TRUE|CH002,CH013|[EV0093](../01_master_timeline.md#ev0093)|True|True|False|False|
|[K205](K205.md)|塞米能兽化并在本场展开巢穴|能力机制|TRUE|CH002,CH003,CH023,CH025,CH028|[EV0098](../01_master_timeline.md#ev0098)|False|True|False|False|
|[K206](K206.md)|翠雀再次透支献祭存在严重风险并须静养|能力限制|PARTIALLY_TRUE|CH001|[EV0112](../01_master_timeline.md#ev0112)|True|True|False|False|
|[K207](K207.md)|墨荷的义肢由妖精为她制作|伤势|UNKNOWN|CH001,CH009|[EV0113](../01_master_timeline.md#ev0113)|True|True|False|True|
|[K208](K208.md)|墨荷能说出翠雀曾三次昙开的经历|私人秘密|TRUE|CH001,CH009|[EV0115](../01_master_timeline.md#ev0115)|True|True|False|False|
|[K209](K209.md)|王钥内部检测报告评级为S+|能力机制|TRUE|CH001,CH008|[EV0132](../01_master_timeline.md#ev0132)|True|True|False|False|
|[K210](K210.md)|偷袭祖母绿者自称蜂之使徒|身份|TRUE|CH008|[EV0143](../01_master_timeline.md#ev0143)|False|True|False|False|
|[K211](K211.md)|墨荷在战争中失去了右臂|伤势|TRUE|CH001,CH009|[EV0147](../01_master_timeline.md#ev0147)|True|True|False|False|
|[K212](K212.md)|林格曾任大妖精长并带走林昀本相|家庭关系|UNKNOWN|CH001,CH016,ORG001|[EV0176](../01_master_timeline.md#ev0176)|True|True|False|True|
|[K213](K213.md)|林昀男孩身体由林格伪造|秘密身份|UNKNOWN|CH001,CH016,ORG001|[EV0176](../01_master_timeline.md#ev0176)|True|True|False|True|
|[K214](K214.md)|红思与向翠雀表白并收到不能做恋人的答复|人际关系|TRUE|CH001,CH005|[EV0054](../01_master_timeline.md#ev0054)|True|True|False|False|
|[K215](K215.md)|玛在演唱会重逢前已由木的消息知道翠雀复出踪迹|历史事件|TRUE|CH001,CH007|[EV0061](../01_master_timeline.md#ev0061)|True|True|False|False|
|[K216](K216.md)|红受控时试图思考禁区会遗忘、试图说出会失声|能力限制|TRUE|CH005|[EV0052](../01_master_timeline.md#ev0052)|True|True|True|False|
|[K217](K217.md)|白对湖畔虐杀过程的记忆失真并被翠协助修饰|私人秘密|TRUE|CH001,CH004|[EV0104](../01_master_timeline.md#ev0104)|True|True|True|False|
|[K218](K218.md)|吴姐妹在分离后曾共同受训半年并约定一起回家|家庭关系|TRUE|CH026,CH027|[EV0178](../01_master_timeline.md#ev0178)|True|True|False|False|
|[K219](K219.md)|女王确已遗忘当年放兽决定的动机|动机认知|UNKNOWN|CH009,CH017|[EV0155](../01_master_timeline.md#ev0155)|True|True|False|True|
|[K220](K220.md)|女王承认下过当年向内城放兽的命令|事件真相|TRUE|CH009,CH017|[EV0155](../01_master_timeline.md#ev0155)|True|True|False|False|
|[K221](K221.md)|墨荷等早期逃亡者并非主动寻求兽魔而是受毒害后求生|历史事件|TRUE|CH009|[EV0180](../01_master_timeline.md#ev0180)|True|True|False|False|
|[K222](K222.md)|女王在食祭四人听到羊说法时已经死亡|生死状态|FALSE|CH002,CH004,CH017|[EV0156](../01_master_timeline.md#ev0156)|True|True|True|False|
|[K223](K223.md)|兵触三未在死亡前把双祭子判断成功报告给蛾|事件真相|TRUE|CH012,CH039|[EV0031](../01_master_timeline.md#ev0031)|True|True|False|True|
|[K224](K224.md)|林小璐与白静萱都是祭子|身份|UNKNOWN|CH001,CH002,CH004,CH039|[EV0031](../01_master_timeline.md#ev0031)|True|True|False|True|
|[K225](K225.md)|妮妮与摩可在女王花园共同成长|人际关系|TRUE|CH001,CH010,CH011,CH017|[EV0163](../01_master_timeline.md#ev0163)|True|True|False|False|
|[K226](K226.md)|摩可知道林昀与翠雀是同一人|人际关系|UNKNOWN|CH001,CH010|[EV0067](../01_master_timeline.md#ev0067)|True|True|False|True|
|[K227](K227.md)|安雅与林昀结婚后成为小璐的父母|家庭关系|TRUE|CH001,CH002,CH006,CH007|[EV0184](../01_master_timeline.md#ev0184)|True|True|False|False|
|[K228](K228.md)|林昀童年认为未见面的母亲可能已经死亡|动机认知|TRUE|CH001|[EV0176](../01_master_timeline.md#ev0176)|True|True|False|False|
|[K229](K229.md)|年轻秘书是红思与的真实侄女|身份|FALSE|CH001,CH005|[EV0086](../01_master_timeline.md#ev0086)|True|True|True|False|
|[K230](K230.md)|公开SS评级意味着公众知道白玫全部王钥机制|能力机制|FALSE|CH002|[EV0133](../01_master_timeline.md#ev0133)|True|False|True|False|
|[K231](K231.md)|本次食祭最终只允许且只会剩一个生还者|能力机制|UNKNOWN|CH002,CH004|[EV0152](../01_master_timeline.md#ev0152)|True|True|False|True|
|[K232](K232.md)|苏胜紫已加入爪痕|组织成员|UNKNOWN|CH001,CH018|[EV0086](../01_master_timeline.md#ev0086)|True|True|False|True|
|[K233](K233.md)|玛格丽特从未期待白蓟而且只是偏心白玫|人际关系|FALSE|CH002,CH007,CH023|[EV0090](../01_master_timeline.md#ev0090)|True|True|True|False|
|[K234](K234.md)|白蓟对玛格丽特的依恋超出玛原先以为的公事师生关系|人际关系|TRUE|CH007,CH023|[EV0090](../01_master_timeline.md#ev0090)|True|True|True|False|
|[K235](K235.md)|林小璐拥有祭子天赋|身份|UNKNOWN|CH001,CH002,CH004|[EV0131](../01_master_timeline.md#ev0131)|True|True|False|True|
