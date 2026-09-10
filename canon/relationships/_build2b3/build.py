"""只生成当前 Stage 2B-3 获准的 relationships/ 文件。"""
from pathlib import Path
import json,re,runpy,datetime
P=Path(__file__).resolve().parents[3]
D=P/'canon/relationships'
data=runpy.run_path(str(D/'_build2b3/curation.py')); rows=data['rows']
cs={x['id']:x for x in json.loads((P/'canon/characters/records.json').read_text(encoding='utf-8-sig'))}
ev={x['id']:x for x in json.loads((P/'canon/events/records.json').read_text(encoding='utf-8-sig'))}
ee={x['id']:x for x in json.loads((P/'audit/evidence_records.json').read_text(encoding='utf-8-sig'))}
cp={x:next((P/'canon/characters').glob(x+'_*.md')).name for x in cs}
old=(D/'TEMP_INDEX.md').read_text(encoding='utf-8-sig')
temps={m[0]:m[1] for m in re.findall(r'## (REL_TEMP_\d+)｜([^\n]+)',old)}
tb={}
for m in re.finditer(r'## (REL_TEMP_\d+)｜([^\n]+)\n(.*?)(?=\n<a id=|\Z)',old,re.S):
    tb[m[1]]={'label':m[2],'original':m[3].strip(),'events':re.findall(r'\[(EV\d+)\]',m[3])}
def put(path,text):
    path.write_text(text.rstrip()+'\n',encoding='utf-8')
def jput(path,obj):put(path,json.dumps(obj,ensure_ascii=False,indent=2))
def ch(c):return f'[{c} {cs[c]["name"]}](../characters/{cp[c]})'
def event(e):return f'[{e}](../01_master_timeline.md#{e.lower()})'
def evidence(e):return f'[{e}](../../audit/01_evidence_index.md#{e.lower()})'
def src(a,b):return f'[L{a}–L{b}](../../source/下班，然后变成魔法少女_第1-282章.txt:{a})'
def rel(r):return f'[{r["id"]}]({r["id"]}.md)'
def safe(s):return str(s).replace('|','／').replace('\n','<br>')
DIM=['熟悉度','信任','依赖','责任','敬意','戒备','恐惧','情感亲近','恋爱倾向','家庭认同']
STATUS={'A':'CONFIRMED','B':'STRONGLY_SUPPORTED','C':'INFERRED','D':'CHARACTER_BELIEF','E':'CHARACTER_BELIEF','F':'UNKNOWN'}
def graded(t):
    gs=re.findall(r'(?<![A-Z])([ABCDEF])(?=[／/:：])',t)
    return sorted(set(gs)) or ['F']
def item(t):
    gs=graded(t)
    return {'text':t,'grades':gs,'statuses':sorted(set(STATUS[x] for x in gs))}
by_pair={(r['source'],r['target']):r for r in rows}
for r in rows:
    r['source_layer']='NOVEL_TEXT';r['time_scope']='仅截至所给卷二282章；末次已写状态，不预测离场后关系'
    r['reverse_id']=by_pair.get((r['target'],r['source']),{}).get('id')
    r['tier_a_core']=cs[r['source']]['tier']=='A' or cs[r['target']]['tier']=='A'
    r['evidence_navigation']=[];r['knowledge_navigation']=[]
    for n,s in enumerate(r['stages'],1):
        e=ev[s['event']];s['sequence']=n
        s.setdefault('source_ranges',e['source_ranges'])
        s.setdefault('story_phase',e['time_layer']+'；'+e['time'])
        # 下列既有事件含历史插叙；单条关系使用相应故事时层，不能按其叙述时点模拟。
        if s['event']=='EV0151' and r['id'] in ['REL103','REL104']:
            s['story_phase']='海蒂童年及求学（当代EV0151支持窗口里的历史补叙）'
            s['source_ranges']=[[36425,36443]]
        if s['event']=='EV0083' and r['id']=='REL065':
            s['story_phase']='安雅生前末次通话；当代EV0083由玛转述'
        if s['event']=='EV0026' and r['id'] in ['REL067','REL068']:
            s['story_phase']='医院旧袭击（白八岁）；当代觉醒时回忆，不是樱死后再次行动'
        if s['event']=='EV0178':s['story_phase']='吴家童年／被带走／共同受训／分派的历史；具体子段见主张'
        if s['event']=='EV0103' and r['id']=='REL018':s['story_phase']='历史更进一步意向由当代回叙确认；不是当代新表白'
        if s['event']=='EV0168' and r['id']=='REL154':s['story_phase']='间界战争前的家园争论至战争受伤，均为历史'
        s['evidence_navigation']=e['audit_navigation']
        s['claim_metadata']=item(s['claim'])
        r['evidence_navigation']+=e['audit_navigation']
        r['knowledge_navigation']+=e.get('knowledge_refs',[])
    r['evidence_navigation']=sorted(set(r['evidence_navigation']))
    r['knowledge_navigation']=sorted(set(r['knowledge_navigation']))
    r['dimensions']={k:item(r['dimensions'].get(k,'F：UNKNOWN；当前未安全确认此维度。')) for k in DIM}
    # 合作有证据，信任的心理程度未必有；显式分栏而不是用合作强填信任。
    trust=r['dimensions']['信任']
    if 'A' in trust['grades'] and 'D' not in trust['grades']:
        trust['behavior_evidence']=trust['text']
        trust['text']='F：心理信任程度UNKNOWN。已确认行为另列：'+trust['text']+'。行为只支持该次托付/协作，不自动确认全面互信。'
        trust['grades']=['F'];trust['statuses']=['UNKNOWN']
    r['unknown_dimensions']=[k for k,v in r['dimensions'].items() if 'UNKNOWN' in v['statuses']]
    r['family_layers']={k:item(v) for k,v in (r.pop('family') or {}).items()}
    r['first_documented_event']=r['stages'][0]['event']
    r['first_event_scope']='本档最早有据关系节点；不主张所有初识日期已明确'
    r['stage_nodes']=len(r['stages']);r['key_transition_count']=max(0,len(r['stages'])-1)
    # 变动次数为索引节点间转换数，含重述确认；不是把每一行都当关系升温。
    r['knowledge_boundary']='只列相关事件的K_TEMP导航。它们可能由其他人持有；须核holder/渠道/时点，不批量赋予Source或Target。'
    if 'CH001' in [r['source'],r['target']]:
        r['identity_boundary']='CH001统一林昀／矢车菊／翠雀／龙胆客观主体；同名归一不合并对方眼中的不同身份。'
        who=r['target'] if r['source']=='CH001' else r['source']
        extra={'CH002':'小璐截至末尾不知父亲=翠雀；父女与导师依恋需并存。','CH004':'白仍把林与翠当不同人；爸爸妈妈称谓不暴露同一性。','CH003':'EV0036确认同一人，EV0110仍误会性别来源；不等知道完整身世。','CH024':'木的怪大叔/局长认识与翠雀救援分开；未识同一人。','CH030':'EV0137错误矢女儿解释→EV0149确认少女代号链，林男身未告。','CH032':'EV0149仅确认少女代号链；男性身份未告。','CH005':'历史EV0050解除变身后知同一人；侄女为掩护。','CH007':'旧战场双方解变才互认，舞台前重逢确认也有过程。','CH009':'战史、当代爪痕立场及女王身世宣称分别按节点；不凭本索引名字知所有秘密。'}.get(who,'别名知识须逐一查K_TEMP，不从CH归一推出全知。')
        r['identity_boundary']+=extra
    else:r['identity_boundary']='CH为客观主体索引；角色是否知道目标真名、家庭或秘密，仍按阶段证据。'
    r['special_treatment']='未据单场行为建立“只对目标如此”的排他待遇；本档行为不自动泛化为对所有人，反之亦然。'
    r['unresolved']=[r['boundary']]
    r['if_boundary']='U003/U007/U008：无据约会、原创承诺、CG进度、好感值及玩家介入不改写本记录。尚未发生的IF不进入NOVEL_TEXT。'
    out=[f'# {r["id"]}｜{cs[r["source"]]["name"]} → {cs[r["target"]]["name"]}',
        f'<a id="{r["id"].lower()}"></a>',
        '## 1｜基础信息',f'**Source：** {ch(r["source"])}  \n**Target：** {ch(r["target"])}  \n**关系类别：** {"、".join(r["categories"])}  \n**来源层：** NOVEL_TEXT  \n**当前原著末尾状态：** '+r['end'],
        '**证据等级：** 逐主张列A–F；A只确认所列行动/可靠叙述，D自述、E他评、C推断不升级。下列类别是导航，并不证明所有维度均成立。',
        '**末尾的含义：** '+r['time_scope']+'。已死者只保留生前关系与他人后续纪念，绝不获得死后知识。',
        ('**反向档案：** '+f'[{r["reverse_id"]}]({r["reverse_id"]}.md)' if r['reverse_id'] else '**反向档案：** 未单建；不代表反向不存在，更不允许复制本档。'),
        '**方向提醒：** '+('两向存在明确的信息、意愿、角色位置或阶段差异；不可镜像。' if r['asymmetric'] else '即使有反向档案，维度仍须分别取证。'),
        '## 2｜关系维度',
        '下列是截至末尾可用的定性结论。行动事实和心理程度分开；UNKNOWN不是“没有这种感情”。历史状态查下一节，不能把末态倒填到开局。',
        '|维度|证据/状态|当前结论与限定|','|---|---|---|']
    for k,v in r['dimensions'].items():out.append(f'|{k}|{"／".join(v["grades"])} · {"／".join(v["statuses"])}|{safe(v["text"])}|')
    out+=['维度依据见下方具体行为、阶段、源行；同一事件中的其他陈述并不一并为本维度作证。','## 3｜关系阶段表',
        '按本关系的故事阶段排列，不按EV编号排序；回忆的叙述窗口另外保留。节点数包含关系重申及边界确认，不是升温次数。',
        '|阶段|Source→Target状态|关联事件|正文窗口与审计导航|','|---|---|---|']
    for s in r['stages']:
        refs='、'.join(src(*w) for w in s['source_ranges'])
        ens='、'.join(evidence(x) for x in s['evidence_navigation'])
        out.append(f'|{s["sequence"]}. {safe(s["story_phase"])}|{safe(s["claim"])}|{event(s["event"])}|{refs}<br>{ens}|')
    if r['anchors']:out+=['**补充定点回查：** '+'、'.join(src(*w) for w in r['anchors'])+'。这些位置用于细化或纠正上游摘要，按本档限定解释。']
    out+=['## 4｜家庭与制度分层']
    if r['family_layers']:
        out+=['|层次|本方向记录|','|---|---|']
        out += [f'|{k}|{safe(v["text"])}|' for k,v in r['family_layers'].items()]
    else:out+=['本记录未据现有证据建立家庭关系。若含“家人”招揽、侄女掩护、师长类比，见维度及阶段；不生成收养、血缘或婚姻事实。']
    out+=['**制度层：** 师生、上下级、同僚仅指阶段表中的实际职务、授课或任务联系。私人敬意、依赖、爱慕在第2节独立取证；不从职位自动推导。',
        '## 5｜人物认知、主观说法与第三人评价',r['identity_boundary'],r['knowledge_boundary'],
        '相关事件候选：'+('、'.join(f'[{k}](../knowledge/TEMP_INDEX.md#{k.lower()})' for k in r['knowledge_navigation']) or '无现成K_TEMP可直接导航；保持UNKNOWN，留Stage 2B-4按本档源行补链。'),
        '阶段表和维度中的D明确属于说话/思考者的判断；E只属于评价者。A“说了某句话”不等其句内命题为A。第三人对亲密、动机或身份的解释不得代替双方表态。',
        '## 6｜未决、旧状态与使用限制',r['boundary'],r['special_treatment'],
        '临时愤怒、误会、嫉妒、恐惧和受控均为STAGE-BOUND。后文已有修复的旧解释仅作历史，不作为末态；未写恢复的状态也不擅自判为永久病态。',
        r['if_boundary'],'## 7｜迁移与追溯',
        ('原临时入口：'+'、'.join(f'[{t}](TEMP_INDEX.md#{t.lower()})' for t in r['temp_ids']) if r['temp_ids'] else '本方向为Stage 2B-3从人物导航、事件与正文补建。'),
        '完整映射和原始措辞保留在[TEMP_TO_REL_MAP](TEMP_TO_REL_MAP.md)。正文定位与既有E编号均不改；本轮问题登记在[Review](../STAGE2B3_REVIEW.md)。',
        '[返回关系目录](README.md) · [关系网络](RELATIONSHIP_MATRIX.md) · [来源规则](../00_source_policy.md) · [用户裁决](../../audit/USER_DECISIONS.md)']
    put(D/f'{r["id"]}.md','\n\n'.join(x if not x.startswith('|') else x for x in out).replace('|\n\n|','|\n|'))
jput(D/'records.json',rows)
jput(D/'_build2b3/curation_changes.json',data['amendments'])

# 49条TEMP逐条保留原文、事件及迁移理由，包括两条集合边的成员展开。
mapping=[]
for t in sorted(tb):
    rs=[r for r in rows if t in r['temp_ids']]
    note='保留方向；按后续证据补阶段与未知，不把原摘要直接当整条关系。'
    if len(rs)>1:note='集合主体逐成员展开；各成员有实际行为/受害/协作证据，不将集体心理复制给所有人。'
    if t=='REL_TEMP_032':note='妮娜与妮姆拆两个目标；矢车菊与林昀同CH001，保留历史军队阶段。'
    if t in ['REL_TEMP_001','REL_TEMP_008','REL_TEMP_019']:note='与同主体父女/导师面貌合并，保留小璐不知同人的认知隔离。019所指亡妻后内容定位L12400–12412，不能套EV0058的十五岁时层。'
    if t in ['REL_TEMP_002','REL_TEMP_006']:note='同一Source/Target合并；小璐眼中的林昀与翠雀仍是两种关系对象面貌，不共享其认知。'
    if t in ['REL_TEMP_003','REL_TEMP_010','REL_TEMP_009']:note='林/翠同CH001，家庭请求暂缓和生日补叙分开；不确立收养或情侣。'
    if t in ['REL_TEMP_012','REL_TEMP_020','REL_TEMP_022','REL_TEMP_023']:note='母亲承诺、爸爸称呼合并到同一客观人物方向，但白的双人理解、无法律手续与称谓变动完整保留。'
    if t in ['REL_TEMP_015','REL_TEMP_017','REL_TEMP_034']:note='红思与/朝颜同CH005、林昀/翠雀同CH001；单方感情延续，拒绝后的工作合作不是恋爱接受。'
    if t in ['REL_TEMP_025','REL_TEMP_026']:note='同一旧友方向合并；后叙确认曾有进一步想法，仍非双方恋爱，离城动机不只爱情。'
    if t=='REL_TEMP_028':note='私比纪律批评回接EV0084；EV0089为正式比试观战，EV0090才是败后误会与拥抱道歉；不将批评推晚。见Review R006。'
    if t in ['REL_TEMP_030','REL_TEMP_043']:note='黑猫/墨荷同CH009，塞米同CH028；重复方向合并，敌害→藏匿→共同离国/家园分期，非法律收养。'
    if t in ['REL_TEMP_033','REL_TEMP_036','REL_TEMP_039']:note='妮娜/墨荷/黑猫同CH009；历史队长与当代敌手分期，遗牌托付先于当代重逢，不按TEMP号排序。'
    if t=='REL_TEMP_038':note='原挂EV0146为战后破本相事件；谈身世与拒任实际EV0176，正式档改指EV0176，原文件只读保留。'
    if t in ['REL_TEMP_044','REL_TEMP_045']:note+=' 629成员CH002/CH004/CH026；吴姐妹早已共同成长，不能把CH026/CH027写成竞赛初识。'
    if t in ['REL_TEMP_046','REL_TEMP_047']:note='后文明确墨先为越狱首领、旧紫钻后来解毒援助，区分初创与后来的正副职务。'
    mapping.append({'temp':t,'original':tb[t],'formal':[r['id'] for r in rs],'reason':note})
jput(D/'temp_to_rel.json',mapping)
out=['# TEMP → REL 完整迁移映射','49条原入口全部处理；原[TEMP_INDEX.md](TEMP_INDEX.md)保持字节不变。合并只发生于同一客观有向人物对，认知面貌、历史阶段与原摘要均保留。','|TEMP|原方向|正式ID|处理原因|','|---|---|---|---|']
for m in mapping:out.append(f'|[{m["temp"]}](TEMP_INDEX.md#{m["temp"].lower()})|{safe(m["original"]["label"])}|'+ '、'.join(f'[{x}]({x}.md)' for x in m['formal'])+'|'+safe(m['reason'])+'|')
out+=['','## 原始阶段措辞与核对去向']
for m in mapping:
    out += [f'\n### {m["temp"]}｜{m["original"]["label"]}',m['original']['original'],f'\n处理：{m["reason"]} 正式档：'+ '、'.join(f'[{x}]({x}.md)' for x in m['formal'])]
put(D/'TEMP_TO_REL_MAP.md','\n'.join(out))

stats={'formal_relationships':len(rows),'temp_inputs':len(mapping),'temp_mapped_formal':len([r for r in rows if r['temp_ids']]),'new_directed_relationships':len([r for r in rows if not r['temp_ids']]),'tier_a_incident_directions':sum(r['tier_a_core'] for r in rows),'represented_characters':len(set(r[x] for r in rows for x in ['source','target'])),'stage_nodes':sum(r['stage_nodes'] for r in rows),'family_records':sum(bool(r['family_layers']) for r in rows),'unknown_dimension_slots':sum(len(r['unknown_dimensions']) for r in rows),'records_with_unknown':sum(bool(r['unknown_dimensions']) for r in rows),'disputed_claims':0,'marked_asymmetric_directions':sum(r['asymmetric'] for r in rows),'marked_asymmetric_pairs':len(set(tuple(sorted([r['source'],r['target']])) for r in rows if r['asymmetric'])), 'unpaired_directions':sum(not r['reverse_id'] for r in rows)}
jput(D/'_build2b3/statistics.json',stats)
out=['# 有向关系 Canon 数据库','**Stage 2B-3：完成建档，检查结果见[Review](../STAGE2B3_REVIEW.md)。**',
     f'正式关系{len(rows)}条（REL001–REL{len(rows):03}）；49条TEMP映射到{stats["temp_mapped_formal"]}条正式方向，另补{stats["new_directed_relationships"]}条。涉及{stats["represented_characters"]}个已有人物主体；已扫描全部70份人物导航。',
     'A→B与B→A各自建档。CH别名归一仅统一客观主体，不共享角色认知。原著末态不是任意开局默认；所有未知都不等“没有”，制度与亲密不互相代证。',
     '## 使用入口','1. 先按下表或[关系网络](RELATIONSHIP_MATRIX.md)定位有向记录。\n2. 选具体事件阶段，查看行动、维度和源行；不要按EV数字当年代。\n3. 若需身份信息权限，再到相关K_TEMP核持有人与渠道。\n4. [TEMP映射](TEMP_TO_REL_MAP.md)用于旧链接接管；[扫描记录](CHARACTER_RELATION_SCAN.md)说明未单建项。',
     '结构化等价数据：[records.json](records.json)。稳定ID只追加不重排，下次新关系从REL'+f'{len(rows)+1:03}'+'开始。原TEMP号、CH号、EV号均未修改。',
     '## 关系总目录','“首次”是本档最早有据节点，不保证每人的精确初识日期；“变化”是后续阶段节点数，含重申/确认，不是升温次数。“明显单向差异”兼指意愿、信息与角色位置不对称，绝不只指爱慕。',
     '|ID|Source|Target|原著末态摘要|首次节点|后续节点数|明显单向差异|未决项|档案|','|---|---|---|---|---|---|---|---|---|']
for r in rows:out.append(f'|{rel(r)}|{ch(r["source"])}|{ch(r["target"])}|{safe(r["end"])}|{event(r["first_documented_event"])}|{r["key_transition_count"]}|{"有，见两向" if r["asymmetric"] else "未作统一判定"}|'+('有，见第6节' if r['unknown_dimensions'] else '见档案')+f'|[{r["id"]}.md]({r["id"]}.md)|')
out+=['','## 边界与文件职责','- [TEMP_INDEX.md](TEMP_INDEX.md)：Stage 2A历史原件，含已识别错序/粗分；使用正式映射读取现状态。\n- [TEMP_TO_REL_MAP.md](TEMP_TO_REL_MAP.md)：49条逐项迁移、原话、合并/拆分理由。\n- [CHARACTER_RELATION_SCAN.md](CHARACTER_RELATION_SCAN.md)：70人扫描与未单建依据。\n- [records.json](records.json)与REL文件：同源生成的正式事实，任何新证据仍以正文优先。\n- [_build2b3/README.md](_build2b3/README.md)：输入哈希、人工整理、修订和校验；不是Canon权威。',
     '未建立完整Knowledge数据库、关系数值、CG解锁或IF剧情。后续Stage 2B-4需用户新指令。本阶段的完成不表示故事已结束或每一未展示心理都已判明。']
put(D/'README.md','\n\n'.join(out).replace('|\n\n|','|\n|'))
out=['# 关系网络索引','这是有向邻接目录，不是填满所有配对的矩阵。未单建反向表示没有在本阶段单独建模，不能解读为“没有关系”。事实仍以各REL阶段表为准。']
for c in cs:
    rs=[r for r in rows if r['source']==c]
    out += [f'\n## {c} {cs[c]["name"]}']
    if not rs:out+=['本轮无正式出向记录；见[人物扫描与边界](CHARACTER_RELATION_SCAN.md)。']
    for r in rs:out += [f'- {ch(c)} → {ch(r["target"])}：{rel(r)}。{r["end"]} 反向：'+(f'[{r["reverse_id"]}]({r["reverse_id"]}.md)' if r['reverse_id'] else '未单建')]
put(D/'RELATIONSHIP_MATRIX.md','\n'.join(out))

excluded={36:'麻雀袭击、识破与押解已由EV0028–EV0034保留；现阶段不为一次案件补持久私人关系。',37:'柏安拘押与对抗见EV0042–EV0046；事件后个人持续关系未写，保留加害事件。',41:'普通同级公司同事；不转异策局职务，不补私交。',42:'旧播种招募功能保留EV0037/EV0189；不凭招募给个人关系强度。',43:'柏安接线/播种职能见EV0042；没有持久私交证据。',46:'当代收押与组织身份见EV0150；不以同组织补对每名干部关系。',49:'第三队长制度链仍见CH049与EV0069；未补独立私密态度。',53:'考场交际与对战保留EV0134；未来是否长期交往未知。',54:'与木棉及后辈接触见EV0134；道歉/同场不补持续私交。',57:'夏的当场对手与情报对象，EV0126/EV0129保留；不延展长期敌意。',58:'女王命令和与新紫迎敌在EV0154保存；不机械复制所有权杖间私交。',59:'兽子控制/协作见EV0156；不为当场同困升级稳定联盟。',60:'接待及同院职务见EV0120；没有必要逐官员建立同套私交。',61:'同院接待见EV0120，保留公务事件。',62:'收押职责见EV0150，私人关系不足。',63:'候补接待见EV0120，战史不代证林昀身份知情。',66:'研究院收押执行者见EV0150；与月季不强并。',68:'仅同类列名，不把类别关联当亲属或熟识。',69:'历史蜂敌对见EV0143–EV0145；CH044同一性未决，禁止把两代蜂边直接移植。',70:'考核及研究邀请见EV0130/EV0133；邀请未接受，不建已确立导师关系。'}
out=['# 70个人物关系导航扫描','扫描输入：Stage 2B-2 records.json中全部70条的relations与knowledge。逐名检查长期、任务、家庭及秘密传播意义；新增反向只用独立行动证据。并非对所有提及者机械建边。','|CH|原人物关系导航（历史只读）|本轮出向 / 入向REL|未单建或注意事项|','|---|---|---|---|']
scan=[]
for c,x in cs.items():
    outgoing=[r['id'] for r in rows if r['source']==c];incoming=[r['id'] for r in rows if r['target']==c]
    mentioned=set(re.findall(r'CH\d{3}',x.get('relations','')))
    missing=sorted(z for z in mentioned if z in cs and (c,z) not in by_pair)
    reason=excluded.get(int(c[2:]),'已为重要独立关系建档。其余同队、同院、当场接触、反向未表态及集合提及保留原CH/EV导航；不因引用缺一方向就推定互惠。')
    if missing:reason+=' 未单建出向候选：'+ '、'.join(missing)+'；作为事件/机构导航保留，不以本表声称这些关系不存在。'
    scan.append({'character':c,'original_navigation':x.get('relations',''),'knowledge_boundary':x.get('knowledge',''),'outgoing':outgoing,'incoming':incoming,'unmodeled_navigation_targets':missing,'decision':reason})
    links=lambda ids:'、'.join(f'[{v}]({v}.md)' for v in ids) or '无'
    out.append(f'|{ch(c)}|{safe(x.get("relations",""))}|出：{links(outgoing)}<br>入：{links(incoming)}|{safe(reason)}|')
put(D/'CHARACTER_RELATION_SCAN.md','\n'.join(out));jput(D/'_build2b3/character_scan.json',scan)
put(D/'_build2b3/README.md','''# Stage 2B-3 构建与检查材料

本目录不是Canon权威。curation.py是逐方向人工整理，build.py只渲染relationships下文件；禁止把关键词命中当关系判定。正式记录见上级目录。

- input_baseline.json：本阶段写入前415个项目文件哈希；允许写入范围外逐一对比。
- curation_changes.json：原文复核后的初稿修改原因、前后值；不取代审计历史。
- character_scan.json：全部70条输入导航、建模与未单建决定。
- statistics.json：由最终正式数据计算的计数。
- check.py / check_result.json：编号、引用、阶段字段、方向、迁移及受保护文件校验。
- semantic_review.md：定点语义复核的证据、范围与剩余未知。

执行build.py会更新本阶段关系文件；不修改原TEMP_INDEX、人物、世界、事件、知识、source/current/audit。未涉及SillyTavern宿主测试。
''')
print(json.dumps(stats,ensure_ascii=False))
