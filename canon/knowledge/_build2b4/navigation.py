from pathlib import Path
import json,re,collections,importlib.util
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'canon/knowledge'
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def write(name,text):(OUT/name).write_text(text+'\n',encoding='utf-8')
R=load('canon/knowledge/records.json');C=load('canon/characters/records.json');REL=load('canon/relationships/records.json');M=load('canon/knowledge/temp_to_k.json');E={e['id']:e for e in load('canon/events/records.json')}
spec=importlib.util.spec_from_file_location('query',OUT/'query_knowledge.py');q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
def k(r,prefix=''):return f'[{r["id"]}]({prefix}{r["id"]}.md)'
def ev(e,prefix='../'):return f'[{e}]({prefix}01_master_timeline.md#{e.lower()})'
def txt(s):return str(s).replace('|','／').replace('\n',' ')
stats=dict(formal=len(R),temp=len(M),temp_merged=sum(x['status']=='MERGED' for x in M),temp_empty_retired=sum(x['status']=='EMPTY_SHELL_RETIRED' for x in M),temp_split=sum(x['status']=='SPLIT' for x in M),new_knowledge=sum(not x['temp_ids'] for x in R),profiles=10,transitions=sum(len(x['states']) for x in R),error_propositions=sum(x['has_error'] for x in R),error_states=sum(s['to_state']=='MISUNDERSTANDS' for r in R for s in r['states']),memory_loss_states=sum(s['to_state']=='MEMORY_LOSS' for r in R for s in r['states']),unknown_propositions=sum(x['important_unknown'] for x in R),unknown_states=sum(s['to_state']=='UNKNOWN' for r in R for s in r['states']),explicit_unaware_states=sum(s['to_state']=='UNAWARE' for r in R for s in r['states']),private_or_secret_propositions=sum(x['secret'] for x in R),high_secret_propositions=sum(x['scope']=='HIGHLY_SECRET' for x in R),disclosures=sum(len(x['disclosures']) for x in R),snapshot_count=sum(len(c['snapshots']) for c in C if c['tier']=='A'),relationships_scanned=len(REL),characters_scanned=len(C))
(OUT/'_build2b4/stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
lines=['# Canon认知与信息壁垒数据库','','**Stage 2B-4：完成。最终检查结果见 [Review](../STAGE2B4_REVIEW.md)。**',f'正式ID：K001–K{len(R):03}。207个TEMP均有处理去向；不更改原TEMP、Timeline、Character或Relationship。', '', '本库分三件事：命题客观是否为真；谁在何时凭什么接触了多少；是否实际向另一个人披露。世界书有一条事实，不等角色或User能够读取。','','## 先读哪里','','- [恢复规则](RESTORE_POLICY.md)：如何按开局节点和主体选择可用信息，未知默认不授予。','- [TEMP迁移](TEMP_TO_K_MAP.md)：旧207条逐条去向、合并/拆分/空壳退役原因。','- [核心人物矩阵](KNOWLEDGE_MATRIX.md)、[认知变化索引](KNOWLEDGE_TRANSITIONS.md)、[披露链](DISCLOSURE_CHAINS.md)。','- [38个快照对照](SNAPSHOT_CHECK.md)、[172条关系边界对照](RELATIONSHIP_CROSSWALK.md)、[70人物扫描](CHARACTER_SCAN.md)。','- [结构化数据](records.json)、[只读查询](query_knowledge.py)、[群体定义](GROUP_SCOPE.md)。','- [本阶段统计](%s)、[检查结果](%s)。'%('_build2b4/stats.json','_build2b4/check_result.json'),'','## Tier A入口','']
for c in C[:10]:lines.append(f'- [{c["id"]} {c["name"]}](by_character/{c["id"]}_knowledge.md)')
lines+=['','## 编号和状态规则','','新增从下一K号追加；不得按字母、人物或年代重排ID。`Kxxx-Tnnn`只标某条中的获取/修正节点，节点号不代表故事时间。临时导入号继续保留在映射中。','`TRUE/FALSE/UNKNOWN`是命题真值；`CONFIRMED/PARTIAL/HEARD/SUSPECTS/MISUNDERSTANDS`等是主体状态。D口述可以证明“此人说过”，不能直接证明说法内容。','范围：PUBLIC、COMMON、ORGANIZATION_INTERNAL、ROLE_RESTRICTED、PRIVATE、SECRET、HIGHLY_SECRET、UNKNOWN_SCOPE。PRIVATE及以上敏感项没有证据便不授予；PUBLIC只是可接触，不是所有人已读。','上游有误只在Review登记。旧卡IF、原创坦白/会议、User全知与游戏规则均未采用。没有选择RP开局或进入下一阶段。','','## 命题总目录','','|ID/档案|明确命题|类型|客观真值|人物/组织导航|首见导航事件|私密/秘密|有阶段|错误认知|未决|','|---|---|---|---|---|---|---|---|---|---|']
for r in R:lines.append('|'+ '|'.join([k(r),r['proposition'],r['type'],r['truth'],','.join(r['character_refs']+r['organization_refs']) or '仅客观/读者导航',ev(r['first_documented_event']) if r['first_documented_event'] else '见证据',str(r['secret']),str(bool(r['states'])),str(r['has_error']),str(r['important_unknown'])])+'|')
write('README.md','\n'.join(lines))
lines=['# 认知变化总索引','','节点保留原前态、后态和来源。UNKNOWN前态不是确证此前完全不知；存在同场先误后纠时按原文子段/within_event_sequence排序。EV号与表中顺序都不是日历。','','|K/节点|主体|From|To|Event|来源及限定内容|原文定位|','|---|---|---|---|---|---|---|']
for r in R:
 for s in r['states']:lines.append('|'+ '|'.join([k(r)+' '+s['id'],s['subject'],s['from_state'],s['to_state'],ev(s['event']),txt(s['source']+'：'+s['known_content']),','.join(f'L{a}–{b}' for a,b in s['source_ranges'])])+'|')
write('KNOWLEDGE_TRANSITIONS.md','\n'.join(lines))
lines=['# 重要信息披露链','','知情不等已披露；NOT_DISCLOSED是具体保密证据或未登记传播，不能覆盖另一阶段已经披露的事实。完整命题中的来源字段保留其他有据传播，本表集中列主动隐瞒、谎言、公开和多跳链。','','|K|来源→接收者|事件|披露状态|内容边界|','|---|---|---|---|---|']
for r in R:
 for d in r['disclosures']:lines.append(f'|{k(r)}|{d["source"]} → {",".join(d["targets"]) or "本次公开可接触对象"}|{ev(d["event"])}|{d["state"]}|{d["content"]}|')
write('DISCLOSURE_CHAINS.md','\n'.join(lines))
lines=['# 核心人物认知矩阵','','使用窄表，按主体与命题定位；并非10×全部K的空矩阵。表列的是记录到的不同阶段状态，不能把后态提前，也不能把未知填成假。各行进入K主档看T节点；末尾查询不自动代表其他开局。','','|类别|K|主体|已记录状态与事件|','|---|---|---|---|']
for r in R:
 for cid in [c['id'] for c in C[:10]]:
  ss=[s for s in r['states'] if s['subject']==cid]
  if ss:lines.append(f'|{r["type"]}|{k(r)} {r["proposition"]}|{cid}|'+ '；'.join(f'{s["event"]} {s["to_state"]}' for s in ss)+'|')
write('KNOWLEDGE_MATRIX.md','\n'.join(lines))
(OUT/'by_character').mkdir(exist_ok=True)
categories=[('已确认知道',['CONFIRMED']),('部分知道',['PARTIAL','HEARD','EXPOSED']),('怀疑、推测与未经独立证实的相信',['SUSPECTS','BELIEVES']),('错误认知、遗忘与纠正',['MISUNDERSTANDS','DISBELIEVES','MEMORY_LOSS','FORGOTTEN']),('明确不知道的重要事项',['UNAWARE']),('原著末尾仍未证其知情',['UNKNOWN'])]
for c in C[:10]:
 cid=c['id'];allrows=[(r,s) for r in R for s in r['states'] if s['subject']==cid]
 lines=[f'# {cid}｜{c["name"]}认知档案','','本页按状态类别索引全部有据阶段，**不是把全部条目合成当前全知人格**。同一K可先误解、后纠正，或后失忆；必须按T节点时间读取。','安雅等已故主体不得获得死后信息；未列的秘密默认不知情/未证，不能因关系、组织或同住自动继承。','人物原导航：'+c['knowledge'],'','- [人物档案](../../characters/'+next((ROOT/'canon/characters').glob(cid+'_*.md')).name+')','- [恢复政策](../RESTORE_POLICY.md)；[核心快照对照](../SNAPSHOT_CHECK.md)。','']
 if cid=='CH007':lines+=['**原导航修正：** 上述原件“演唱会前不能默认知安雅死亡”不再作为本库有效结论。原文证明她葬礼前已获死讯，木也在重逢前给过翠雀来访线索。见K187、K215及Review R001。','']
 if cid=='CH004':lines+=['**快照修正：** EV0078的老师/叔叔是事件中间称谓；末端已再次获准叫爸爸，不能把暂退状态当整个事件后的当前状态。见K073/K082及Review R006。','']
 for label,states in categories:
  lines += ['## '+label,'']
  selected=[(r,s) for r,s in allrows if s['to_state'] in states]
  for r,s in selected:lines.append(f'- {k(r,"../")} `{s["id"]}`｜{s["event"]}／{s["acquisition"]["epoch"]}／**{s["to_state"]}**：{s["known_content"]}')
  if not selected:lines.append('此分类没有已证的专属条目；不等于该人物没有任何未知/误解。')
  lines.append('')
 lines+=['## 后续才会知道与阶段恢复','', '从较早节点开始时，后面的记录仅作导航，不能提前注入。先选择下列人物快照，再按已发生的获取节点和来源恢复；历史回忆按发生期，不按章节顺序。','']
 for snap in c['snapshots']:
  evn=re.search(r'EV\d+',snap['node'])[0];before='之前' in snap['node'] or '之前' in snap['认知'] and cid=='CH007' and evn=='EV0082'
  result=q.lookup(cid,evn,before=before)
  lines += [f'- **{snap["node"]}**：原认知摘要“{snap["认知"]}”。本库保守查询可返回{len(result["allowed"])}条状态，拦截/待核{len(result["denied_or_unresolved"])}条；不是该人物所有生活常识总量。']
 lines += ['','## 截止与保密边界','', 'EOF仅到卷二282《琥珀》。幻命织华完整效果、食祭最终结局、尚未传播的幕后信息不补全。其他主体知道的命题，只有明确转述后才可进入本页。','本库不授予User全知权限；User需要另按选定身份、阶段与亲历初始化。']
 write(f'by_character/{cid}_knowledge.md','\n'.join(lines))
lines=['# 群体知识范围','','G编号只是一次接收场景的限定集合，不能拿组织或参赛资格自动补成员。未具名群体不建立70人物空矩阵，也不推“国度全员知道”。具体已经具名的三新人、四追击者、九参战者按原文场景拆到CH。','','|ID|群体称呼|时点|成员限制|','|---|---|---|---|']
for g in load('canon/knowledge/groups.json'):lines.append(f'|{g["id"]}|{g["label"]}|{ev(g["event"])}|{g["membership"]} {g["grant_policy"]}|')
write('GROUP_SCOPE.md','\n'.join(lines))
lines=['# 70个人物认知导航扫描','','逐条核对原knowledge字段与新库，未据此给所有人生成知识。相关K是导航，不代表该人物已获知。','','|CH|原认知提醒|本库相关K|处理|','|---|---|---|---|']
for c in C:
 rs=[r for r in R if c['id'] in r['character_refs']]
 direct=sum(s['subject']==c['id'] for r in R for s in r['states'])
 lines.append(f'|{c["id"]} {c["name"]}|{txt(c["knowledge"])}|'+('、'.join(k(r) for r in rs) or '保留原导航，无新增有据获取')+f'|{direct}条专属节点；无证据部分默认不授予。|')
write('CHARACTER_SCAN.md','\n'.join(lines))
snapshot_rows=[]
issues={('CH001','EV0036'):'R007：原位置写医院；实际夏凉家阳台。认知确认本身成立，不能造医院目击者。',('CH003','EV0036'):'R007：同上，夏家私谈与医院有区别。',('CH007','EV0082'):'R001：安雅死讯在葬礼前已获；重逢前也获木来访线索，原快照不应写将来才知死亡。',('CH004','EV0078'):'R006：该事件内先暂退称谓、后又获准叫爸；事件末态不得固定为仅叔叔/老师。'}
lines=['# Tier A的38个快照检查','','保留上游原文；本表为本阶段检查及调用修正导航，不静默改写人物档案。修正建议详见Review。每个快照只检查人物实际知道的范围，不用客观整库替换认知摘要。','','|CH/快照|原认知摘要|检查结论|可返回状态/拦截|','|---|---|---|---|']
for c in C[:10]:
 for sn in c['snapshots']:
  event=re.search(r'EV\d+',sn['node'])[0];before='之前' in sn['node'];result=q.lookup(c['id'],event,before)
  note=issues.get((c['id'],event),'未发现此认知摘要将具体后期信息直接赋予该主体；照护/关系/能力字段仍须同时限阶段。')
  if c['id']=='CH006' and event=='EV0182':note='已故节点禁止新知识，查询拒绝；不创造死后心理。'
  snapshot_rows.append(dict(character=c['id'],snapshot=sn['node'],original=sn,review=note,lookup=result))
  lines.append(f'|{c["id"]} {sn["node"]}|{txt(sn["认知"])}|{note}|{len(result["allowed"])}/{len(result["denied_or_unresolved"])}|')
write('SNAPSHOT_CHECK.md','\n'.join(lines));(OUT/'_build2b4/snapshot_checks.json').write_text(json.dumps(snapshot_rows,ensure_ascii=False,indent=2),encoding='utf-8')
lines=['# 172条有向关系的认知边界对接','','全部172条读取knowledge_boundary与identity_boundary，逐条扫描阶段claim中的知情、误认、表白、家属、旁听与误解相关表达。既有关系中K_TEMP是事件候选，不是给Source/Target的授权。下面仅列新库相关命题，不做关系字段批量回写。','','|REL|方向|相关K导航|认知检查|','|---|---|---|---|']
cross=[]
for r in REL:
 refs=[x for x in R if r['id'] in x['relationship_refs']]
 note='没有由该关系自动生成知识；信任/依恋/合作与知道对方完整情感分开。'
 if r['id']=='REL067':note='R004：EV0032对白隐瞒死亡；不能把“逐步得知其死亡”合挂此点。真正死讯接EV0055。'
 if r['id']=='REL053':note='R003：EV0163该厨房对话的听者是翠雀，不是摩可；不能据此授权摩可本次新获安排。'
 cross.append(dict(relationship=r['id'],source=r['source'],target=r['target'],formal_knowledge=[x['id'] for x in refs],review=note,original_boundary=r['knowledge_boundary'],identity_boundary=r['identity_boundary']))
 lines.append(f'|[{r["id"]}](../relationships/{r["id"]}.md)|{r["source"]}→{r["target"]}|'+('、'.join(k(x) for x in refs) or '无新增有据传播；原边界继续限制')+f'|{note}|')
write('RELATIONSHIP_CROSSWALK.md','\n'.join(lines));(OUT/'_build2b4/relationship_checks.json').write_text(json.dumps(cross,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(stats,ensure_ascii=False))
