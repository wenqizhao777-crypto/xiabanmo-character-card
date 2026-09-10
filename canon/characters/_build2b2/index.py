import json,pathlib,re,collections
from build import ROOT,OUT,EV,E
data=json.loads((OUT/'records.json').read_text(encoding='utf8'));P={x['id']:x for x in data}
def ch(n):
 k=f'CH{n:03}';return f'[{k}｜{P[k]["name"]}]({k}_{P[k]["name"]}.md)'
old=(OUT/'_build2b2/legacy_readme.md').read_text(encoding='utf8')
(OUT/'LEGACY_P_TEMP_INDEX.md').write_text(old,encoding='utf8')
mapping={1:[1],2:[2],3:[11],4:[1],5:[10],6:[3],7:[5],8:[40],10:[12],12:[4],13:[35],14:[31],15:[39],16:[4],17:[39],18:[36],19:[47],21:[21],22:[34],26:[6],27:[7],28:[18],29:[42],30:[48],35:[24],36:[23],37:[25],38:[43],39:[22],40:[37],44:[7],45:[11],47:[66],49:[49],52:[8],54:[67],57:[50],58:[13],59:[28],60:[5],61:[16],66:[14],68:[13],69:[38],70:[65],71:[14],74:[9],77:[15],78:[46],79:[30],81:[1],82:[6],83:[19],84:[9],85:[20],86:[9],87:[15],88:[33,60,61,62,63],93:[32],94:[26],96:[17],97:[29],98:[58],100:[70],102:[55],103:[56],104:[57],108:[44],109:[27],110:[2],111:[3,55,56],114:[70],118:[52],119:[53],120:[54],122:[3,55,56],124:[33],125:[15],127:[69],132:[20],134:[66],135:[62],136:[27],137:[45],139:[59],142:[65],143:[13],144:[14],146:[64],154:[26],155:[27]}
# 月季是考核主考且后续直接参与项目测试，纳入功能档；号码接在已有冻结段之后。
if 'CH070' not in P:
 raise RuntimeError('先在事实源中建立月季CH070，禁止仅凭索引造档')
mapping[47]=[] # 卢恩诺雷是地点，不是主任；显式清除任何错误候选。
notes={3:'首次来电视角仍匿名；后文妮妮电话线回接，不据合并恢复固定号码或固定三通。',15:'该入口同时含兵触三与未具名黑袍人；链接不把全组压成一人。',47:'原显示名卢恩诺雷是城，不建人物；见LOC013。',69:'未具名师父，保留最小索引。',70:'天女是时代通称；链接仅该场救命者，不代表通称只有一人。',71:'本入口发生在旧紫钻语境；裸称紫钻跨时需另辨CH029。',88:'混合群体：已命名者导航，其他来客不自动同级。',95:'“姐妹”跨场有吴姐妹、山卷等，按原事件辨主体。',118:'旧写木芙蓉；原著实际木棉（Review R001），保留旧入口但不当Canon别名。',127:'仅历史蜂之使徒；与当代CH044未强并。',132:'记忆为载体，人物已死，不建复活个体。',135:'“等”还含未具名协作者，不把整个团队归雪毬。',136:'混合内外场群体，只链接点名个体。',164:'未具名兔形妖精；候选沃波CH042未确认同一，不另造确定人名。'}
counts=collections.Counter(x['tier'] for x in data)
s='# 人物 Canon 数据库｜Stage 2B-2\n\n**状态：已完成本阶段人物事实档案建设与完整性检查；详见[本轮Review](../STAGE2B2_REVIEW.md)。**\n\n'
s+='[来源规则](../00_source_policy.md)与[人工裁决](../../audit/USER_DECISIONS.md)控制事实/IF边界。原著审计100%状态未改变；本阶段按全文证据导航做人物提取与重点回查，不声称又重读一遍全文。\n\n'
s+='## 使用方法\n\n先选人物，再选事件阶段；不得直接将“末尾状态”用于开篇。章节回忆的揭晓位置与发生年代不同。关系与认知仅为TEMP导航，尚未进入Stage 2B-3／2B-4。资料并列秘密别名不等人物知道别名。\n\n'
s+='- Tier A：核心、多阶段复杂人物，独立完整档案及八维快照。\n- Tier B：持续影响主线的重要配角，独立标准档案。\n- Tier C：事件、能力、身份或传播链需要的功能性简档。\n- Tier D：仅为区分未具名主体的最小索引。\n\n'
s+=f'共{len(data)}条稳定主体记录：A {counts["A"]}、B {counts["B"]}、C {counts["C"]}、D {counts["D"]}；A/B独立完整或标准档案{counts["A"]+counts["B"]}份，C/D简档{counts["C"]+counts["D"]}份。CH044与CH069同一性未定，因此本数是记录数，不宣称已证同样数量的独立自然人。\n\n'
s+='## 总目录\n\n|Character ID／档案|别名／称号|Tier|主要组织|重要能力|复杂阶段|后续关系／认知需求|状态|\n|---|---|---|---|---|---|---|---|\n'
for d in data:
 s+='|'+ '|'.join([ch(int(d['id'][2:])),d['aliases'],d['tier'],d['org'],d['power'],'是' if d['tier'] in 'AB' else '局部事件', '关系／认知均需按当事人核定','完成；未知保留'])+'|\n'
s+='\n## 身份与别名使用规则\n\n'
s+='|称呼|处理|\n|---|---|\n|林昀／矢车菊／龙胆|CH001，同人不同阶段或伪装，不能对外全公开。|\n|翠雀|CH020妮姆先用，CH001林昀后承继；不是同一人。|\n|紫钻|CH014前任／白狼与CH029现任是不同人物。|\n|墨荷／妮娜／黑猫|CH009；猫形妖精塞米是CH028，不是副首领另一个身体。|\n|蛾／摩丝|CH012，秘密身份与公开局长身份同人。|\n|朝颜／红思与|CH005；原肉身、本相、临时本体不同，不另造侄女CH。|\n|猫尾草／木芙蓉|旧资料错误导航字形；本文以猫尾CH021、木棉CH052记录，原始记录待授权修复。|\n|羊踟蹰／羊踯躅|CH059保留源文异文与待规范状态，不静默改原文。|\n|蜂／蜂之使徒|CH044／CH069暂分事件主体且互指同一性待核；不宣称必为同一或必不同。|\n|天女|旧时代泛称；不能全局替换为一个人物，CH065仅该次救援者。|\n\n'
s+='## 原P_TEMP入口兼容映射\n\n164个原锚点继续有效。原Stage 2A完整导航原样保存在[LEGACY_P_TEMP_INDEX](LEGACY_P_TEMP_INDEX.md)，以下只维护映射，不改旧事件。`GROUP/UNNAMED`不是已确立新人物，也不因分组共享知识。\n\n'
legacy=re.findall(r'<a id="(p_temp_\d+)"></a>\s*## ([^\n]+)',old)
maps=[]
for anchor,name in legacy:
 i=int(anchor.split('_')[-1]);dest=mapping.get(i,[])
 note=notes.get(i,'按原事件辨知情人；别名合并不共享未获得的知识。' if dest else '群体、职能泛称或未具名主体；按原事件辨成员，不机械建人。')
 target='、'.join(ch(n) for n in dest) if dest else 'GROUP / UNNAMED / 地点导航'
 s+=f'<a id="{anchor}"></a>\n### {anchor.upper()}｜{name}\n\n{target}。{note} [原事件列表](LEGACY_P_TEMP_INDEX.md#{anchor})。\n\n'
 maps.append({'temp':anchor.upper(),'label':name,'characters':[f'CH{n:03}' for n in dest],'scope':note})
s+='## 文件职责与维护\n\n- [records.json](records.json)：与Markdown档案同源的结构化数据，便于按CH/事件查询。\n- [_build2b2/dossiers.json](_build2b2/dossiers.json)：渲染输入；正文事实优先回查原著。修改需同步渲染并检查。\n- [_build2b2/audit_navigation.json](_build2b2/audit_navigation.json)：核心人物对应C/M与修订原因地址；原审计不复制、不改写。\n- [_build2b2/check_result.json](_build2b2/check_result.json)：编号、链接、快照与只读输入检查。\n- [_build2b2/README.md](_build2b2/README.md)：构建、复核和维护说明。\n\n不建立正式关系／认知库，不设计开局UI，不生成角色台词或RP心理模板。下一阶段须另行授权。\n'
(OUT/'README.md').write_text(s,encoding='utf8')
(OUT/'_build2b2/temp_mapping.json').write_text(json.dumps(maps,ensure_ascii=False,indent=2),encoding='utf8')
issues={a['id']:a for a in json.loads((ROOT/'audit/issue_records.json').read_text(encoding='utf-8-sig'))}
missing={a['id']:a for a in json.loads((ROOT/'audit/missing_records.json').read_text(encoding='utf-8-sig'))}
changes=json.loads((ROOT/'audit/judgment_changes.json').read_text(encoding='utf-8-sig'))
nav=[]
for d in data:
 if d['tier']!='A':continue
 rows=[]
 for k in d['audit_issues']:
  rev=[{'session':z.get('session'),'reason':z.get('reason'),'json_index':idx} for idx,z in enumerate(changes) if z.get('id')==k]
  a=issues[k];rows.append({'id':k,'title':a['title'],'card_entry_indices':a['card'],'source':'audit/issue_records.json; 按id定位末次accurate','revision_history':'audit/judgment_changes.json; 保留before/after','revisions':rev,'final_closure':'audit/final_changes.json、audit/final_document_changes.json（如有该项）'})
 nav.append({'character':d['id'],'issues':rows,'missing':[{'id':k,'title':missing[k]['title'],'source':'audit/missing_records.json; 按id定位'} for k in d['audit_missing']],'timeline_risk':'audit/04_timeline_knowledge_risks.md; 按C/事件/人物查阅','decisions':'audit/USER_DECISIONS.md U001–U008'})
(OUT/'_build2b2/audit_navigation.json').write_text(json.dumps(nav,ensure_ascii=False,indent=2),encoding='utf8')
print('index',len(data),'legacy anchors',len(legacy))
