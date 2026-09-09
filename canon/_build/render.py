import json, re, hashlib, copy
from pathlib import Path
from datetime import datetime
P=Path(__file__).resolve().parents[2];C=P/'canon';SRC=P/'source/下班，然后变成魔法少女_第1-282章.txt'
R=json.loads((C/'events/records.json').read_text('utf-8'))
CH=json.loads((P/'audit/chapter_index.json').read_text('utf-8-sig'))
E={x['id']:x for x in json.loads((P/'audit/evidence_records.json').read_text('utf-8-sig'))}
LOG=json.loads((C/'_build/revisions.json').read_text('utf-8'))
def add(base,title,time,layer,occ,state,refs,ranges,actors,knowledge,note):
 if any(x['title']==title for x in R):return
 x=copy.deepcopy(R[base-1]);x.update(id=f'EV{len(R)+1:04d}',title=title,time=time,time_tier='T3',time_layer=layer,occurrence=occ,changes=state,direct_result=state,before='见关联节点中的前态。',audit_navigation=refs,source_ranges=ranges,checked_anchors=ranges,participants=actors.split('、'),knowledge=knowledge,relationships=[],related_events=[f'EV{base:04d}'],note=note,witnesses='只就发生字段中各自参与的场景知情；历史内容另依来源性质。',meaningfully_unaware='见备注与知识TEMP。')
 R.append(x);R[base-1]['related_events'].append(x['id']);LOG['changes'].append(dict(event=x['id'],reason='遗漏索引交叉检查补足状态变化'))
add(88,'白静萱返校计划形成并逐步为同伴所知','十二月后半私下筹划；赴国度旅途中已有同伴协助','当代中段','翠雀考虑择校及文化准备，未立即入学；后续小璐在旅途帮白补西罗语。','教育：单纯战斗训练→筹备返校；计划：尚未正式入学',['E290','E377'],[[19813,19822],[25115,25117]],'翠雀、白静萱、林小璐',[['林小璐','白静萱准备返校','UNKNOWN','PARTIALLY_CONFIRMED','旅途补习与当时对话']],'控制兽性是翠雀的期待C，不是已验证疗法；未给具体学校或注册日期。')
add(86,'兰香拒研究院邀请、退役与去间界说法','旧队时期拒邀；满十年退役，最后联络距当代十二年','历史回溯','苏胜紫自述拒研究院邀请，任满十年退役离方亭；玛后来转述最后通话中苏说要去间界，此后失联。','身份：现役兰香→退役；联系：可联系→长期失联',['E280','E281'],[[19359,19370]],'苏胜紫、玛格丽特、林昀、红思与',[['林昀、红思与','苏胜紫去间界的最后通话消息','UNKNOWN','PARTIALLY_CONFIRMED','当代由玛转述，非亲见抵达']],'邀请细节D；实际去向、存亡与是否加入爪痕仍UNKNOWN。历史行动与当代传播分栏。')
add(1,'首次复变尝试失败与白日警告','开篇看回放当晚尝试；一周期间之后的工作日午间','当代前段','林昀取宝石后试变身却没有回应，转而请红关照女儿；工作日午间接匿名电话警告当晚残兽。','能力状态：退隐可变身的期待→首次尝试失败；认知：获当晚危机预警',[],[[315,340],[348,363]],'林昀、红思与、匿名来电者',[['林昀','当晚残兽可能有危险','UNKNOWN','SUSPECTED','断续匿名警告，尚无地点']],'暂时失灵不等永久失能；晚间回拨才得公园位置。不得把取宝石即写成当晚已复出。')
add(37,'林昀首次与心之种建立连接','距当代约二十二年前，安雅战斗遇险的黄昏','历史回溯','林昀为救安雅向兔形妖精争取测试，心之种在接触后发出纯白光并建立连接，妖精开始指导用魔力激活。','能力：普通少年→与心之种建立连接；认知：妖精预期失败→亲见成功',[],[[444,494],[504,510]],'林昀、兔形妖精、安雅',[['兔形妖精','林昀能与心之种连接','REJECTED','CONFIRMED','亲眼看到连接发光']],'安雅在远处作战，不等亲眼看见连接过程；这不是本轮对出生生理条件的独立裁决。')
R[188]['witnesses']='林昀与兔形妖精；安雅在远处作战，未证她看见测试。'
R[186]['knowledge']=[['玛格丽特','苏胜紫准备去间界','UNKNOWN','PARTIALLY_CONFIRMED','最后一次通话听本人说法']]
R[85]['knowledge'] += [k for k in [['林昀、红思与','苏胜紫最后通话的间界去向','UNKNOWN','PARTIALLY_CONFIRMED','当代玛转述']] if k not in R[85]['knowledge']]
for n,a in {9:[[1917,1952]],10:[[1956,1958]],121:[[29508,29516]],124:[[30395,30415]],173:[[30670,30707]],161:[[3360,3386]]}.items():R[n-1]['checked_anchors']+=a
for n,a in {159:[[7295,7297],[7364,7366],[7379,7380],[7448,7450]],170:[[10177,10180],[10208,10210]],130:[[32468,32471]]}.items():
 R[n-1]['checked_anchors']+=a
for x in R:
 # 旧候选分拆后，不把落在别的子事件中的锚点继续当成本项核验证据。
 x['review_context_ranges']=x.get('review_context_ranges',[])+[z for z in x['checked_anchors'] if not any(a<=z[0] and z[1]<=b for a,b in x['source_ranges'])]
 x['checked_anchors']=[[max(a,u),min(b,v)] for a,b in x['checked_anchors'] for u,v in x['source_ranges'] if max(a,u)<=min(b,v)]
 for k in x['knowledge']:
  if k[2]=='CHARACTER_BELIEF':k[2]='BELIEVED'
  if k[3]=='CHARACTER_BELIEF':k[3]='BELIEVED'
  if k[2]=='STRONGLY_SUPPORTED':k[2]='INFERRED'
  if k[3]=='STRONGLY_SUPPORTED':k[3]='INFERRED'
 x['later_informed']='；'.join(k[0]+'经'+k[4]+'获“'+k[1]+'” → '+k[3] for k in x['knowledge'] if k[0]!='读者') or '本节点未指明新的事后转述者；后续传播见关联事件。'
 x['verification']='SOURCE_ANCHORS_RECHECKED'
 x['checked_anchors']=[list(z) for z in sorted(set(map(tuple,x['checked_anchors'])))]
 x['revealed_at']=x['source_ranges']
 x['related_events']=sorted(set(x['related_events'])-{x['id']})
 x['qualified_claims']=[{'grade':'D','status':'CHARACTER_BELIEF','scope':'人物说法、诊断解释、价值判断的内容；其说出/作出行为本身可为A。'}, {'grade':'C','status':'INFERRED','scope':'发生与备注中的猜测、预感及未直接验证的机制，不自动升级。'}]
 if x.get('time_status')=='DISPUTED':x['qualified_claims'].append({'grade':'F','status':'DISPUTED','scope':'本节点日期/相对时间张力；见时间风险索引。'})
 if x['id']=='EV0158':x['qualified_claims'].append({'grade':'F','status':'UNKNOWN','scope':'繁开后胜负、刺杀结果、食祭结局、最终考核认证未提供。'})

def ch(a):return next(x for x in CH if x['start_line']<=a<=x['end_line'])
def src(a,b):
 q=ch(a);v=ch(b)
 label=q['volume']+' '+q['title'].lstrip('# ') + (('—'+v['title'].lstrip('# ')) if q!=v else '')
 return f'[{label} L{a}–L{b}](../source/下班，然后变成魔法少女_第1-282章.txt:{a})'
def ev(z,prefix=''):return f'[{z}]({prefix}01_master_timeline.md#{z.lower()})'
def esc(t):return str(t).replace('|','／').replace('\n',' ')
def write(p,t):(C/p).write_text(t,encoding='utf-8')

# 稳定TEMP索引注册：首次按Event分配，重排不重编号。
regp=C/'_build/temp_registry.json'
reg=json.loads(regp.read_text('utf-8')) if regp.exists() else dict(knowledge={},relationships={},people={})
def uid(group,key,prefix):
 d=reg[group]
 if key not in d:d[key]=f'{prefix}{len(d)+1:03d}'
 return d[key]
for x in R:
 x['knowledge_refs']=[];x['relationship_refs']=[];x['character_refs']=[]
 for k in x['knowledge']:
  kid=uid('knowledge',k[1],'K_TEMP_');x['knowledge_refs'].append(kid)
 for r in x['relationships']:
  rid=uid('relationships',r[0]+' → '+r[1],'REL_TEMP_');x['relationship_refs'].append(rid)
 for name in x['participants']:
  pid=uid('people',name,'P_TEMP_');x['character_refs'].append(pid)
write('_build/temp_registry.json',json.dumps(reg,ensure_ascii=False,indent=2))

kn=['# 知识传播TEMP导航','', '本轮仅预标记，不是完整知识数据库。每个命题单独编号，每条传播边保留持有人、事件和渠道。认知CONFIRMED表示当事人的确认程度；真假仍读事件证据等级。读者不等于NPC。同一命题的不同文字暂不粗合，正式建库时保留映射。','']
for topic,kid in reg['knowledge'].items():
 kn += [f'<a id="{kid.lower()}"></a>',f'## {kid}｜{topic}','','|事件|持有人|此前→之后|渠道/范围|','|---|---|---|---|']
 for x in R:
  for k in x['knowledge']:
   if k[1]==topic:kn.append(f'|{ev(x["id"],"../")}|{esc(k[0])}|{esc(k[2])} → {esc(k[3])}|{esc(k[4])}|')
 kn.append('')
write('knowledge/TEMP_INDEX.md','\n'.join(kn))
rel=['# 有向关系TEMP导航','','只登记本轮重要关系变化；不设好感数值，不把单向喜欢写成恋爱双方。起点→终点不可反向复制。','']
for pair,rid in reg['relationships'].items():
 rel += [f'<a id="{rid.lower()}"></a>',f'## {rid}｜{pair}','']
 for x in R:
  for r in x['relationships']:
   if r[0]+' → '+r[1]==pair:rel.append(f'- {ev(x["id"],"../")}：{r[2]}')
 rel.append('')
write('relationships/TEMP_INDEX.md','\n'.join(rel))
people=['# 人物与参与群体导航','','仅为事件查找入口，未建立人物百科。显示名可含历史代号、当代伪装与群体；不表示这些身份对NPC公开。林昀/矢车菊/翠雀/龙胆、红思与/朝颜、妮娜/墨荷/黑猫等关联必须按事件中的知情边读取，不能因在索引并列而在RP中公开。后续人物文件建议以本名建立并保留此索引映射。','']
for name,pid in reg['people'].items():
 people += [f'<a id="{pid.lower()}"></a>',f'## {name}','','相关事件：'+ '、'.join(ev(x['id'],'../') for x in R if name in x['participants']),'']
write('characters/README.md','\n'.join(people))

# 历史保持偏序/分组，不虚构所有往事的唯一总排序。
groups=[('历史独立支线：日期未与主线完全对齐',[79,95,166,178]),('旧队与参战起点及能力概览',[189,37,50,58,111,118]),('1979战争：前线、内城与伤员处置',[141,142,143,144,177,145,168,146,176,147,148]),('战后及当代以前：各条因果链',[169,180,181,167,185,165,51,183,184,81,187,182,9,10,52,53]),('当代前段：复出至月圆节',[]),('当代中段：就任、来客与赴国度',[]),('2000年认证考核：各队并行',[]),('末场：并行危机与文件终点',[])]
hist={n for _,ns in groups for n in ns}
for i,x in enumerate(R,1):
 if i in hist:continue
 mn=min(a for a,b in x['source_ranges'])
 gi=4 if mn<12884 else 5 if mn<29830 else 6 if mn<36131 else 7
 # 通过旧证据回接的当前事项按真实发生位置归类。
 if i==162:gi=5
 if i==160:gi=4
 groups[gi][1].append(i)
for j in range(4,8):groups[j][1].sort(key=lambda n:(min(a for a,b in R[n-1]['source_ranges']),n))
flat=[n for _,ns in groups for n in ns]
assert sorted(flat)==list(range(1,len(R)+1))
out=['# Master Timeline｜世界状态变化时间轴','','**本轮范围：全部已提供原著，首章至卷二第282章《琥珀》。** 时间线覆盖全书的重要状态转换；不是逐章摘要，也不声称百科事实已穷尽。阅读入口：[来源规则](00_source_policy.md)。事件ID稳定，正文出现顺序、历史发生順序与人物获知顺序分别保留。','', '事件主等级适用于直接发生的行动及结果；引号、人物解释、计划和推断按限定项读取。历史分组只给偏序，分组内没有证据的绝对日期仍UNKNOWN。并行事件的上下位置不是时间早晚证明。','',f'共 **{len(R)} 个事件**；知识命题 **{len(reg["knowledge"])}**，有向关系 **{len(reg["relationships"])}**。后续补节点仅追加ID，不重编号。','', '[重要状态链与争议](events/STATE_CHAINS.md) · [知识TEMP](knowledge/TEMP_INDEX.md) · [关系TEMP](relationships/TEMP_INDEX.md) · [最终检查](BUILD_CHECK.md)','']
for g,ns in groups:
 out += ['## '+g,'','|事件|时间等级与时间|核心变化|','|---|---|---|']
 for n in ns:
  x=R[n-1];out.append(f'|[{x["id"]} {esc(x["title"])}](#{x["id"].lower()})|{x["time_tier"]} · {esc(x["time"])}|{esc(x["changes"])}|')
 out.append('')
out += ['---','','# 事件详情','']
for x in R:
 out += [f'<a id="{x["id"].lower()}"></a>',f'## {x["id"]}｜{x["title"]}','',f'- **时间**：{x["time_tier"]}；{x["time"]}。{("DISPUTED：原文时间张力，见状态链。" if x.get("time_status")=="DISPUTED" else "")}',f'- **故事层／地点**：{x["time_layer"]}；{x["location"]}。',f'- **原著定位／读者揭示窗口**：'+ '；'.join(src(a,b) for a,b in x['source_ranges']),f'- **回查锚点**：'+ '、'.join(f'L{a}–{b}' for a,b in x['checked_anchors'])+'。支持区间与局部回查范围分开；不声称本轮逐字重读全部区间。',f'- **来源／证据／状态**：NOVEL_TEXT；{x["evidence_grade"]}／{x["status"]}（直接事件）；人物说法D、推断C、未知F不得随主等级升级。审计导航：'+ '、'.join(x['audit_navigation']),f'- **参与者**：'+ '、'.join(x['participants']),f'- **目击者**：{x["witnesses"]}',f'- **事后知情者**：{x["later_informed"]}',f'- **重要不知情／误解边界**：{x["meaningfully_unaware"]}',f'- **事件前状态**：{x["before"]}',f'- **发生**：{x["occurrence"]}',f'- **直接结果**：{x["direct_result"]}',f'- **状态变更**：{x["changes"]}',f'- **长期影响／回接**：'+ ('、'.join(ev(z) for z in x['related_events']) if x['related_events'] else 'UNKNOWN；未列独立后续结果。')+'（这些边用于状态续接/迟到解释，不自动表示因果、目击或严格先后）。',f'- **关联人物导航**：'+ '、'.join(f'[{name}](characters/README.md#{pid.lower()})' for name,pid in zip(x['participants'],x['character_refs'])),f'- **关联知识**：'+ ('、'.join(f'[{z}](knowledge/TEMP_INDEX.md#{z.lower()})' for z in x['knowledge_refs']) or '无独立信息传播预标记；不等于所有人无知。'),f'- **有向关系**：'+ ('、'.join(f'[{z}](relationships/TEMP_INDEX.md#{z.lower()})' for z in x['relationship_refs']) or '本节点未单列新关系边。'),f'- **备注与证据限制**：{x["note"]}','']
 if x['knowledge']:
  out+=['|持有人|命题|认知变化|渠道|','|---|---|---|---|']+[f'|{esc(k[0])}|{esc(k[1])}|{k[2]} → {k[3]}|{esc(k[4])}|' for k in x['knowledge']]+['']
 if x['relationships']:out+=['有向变化：'+'；'.join(a+' → '+b+'：'+v for a,b,v in x['relationships']),'']
write('01_master_timeline.md','\n'.join(out))
write('events/records.json',json.dumps(R,ensure_ascii=False,indent=2))
write('_build/revisions.json',json.dumps(LOG,ensure_ascii=False,indent=2))
write('events/README.md','# 事件资料导航\n\n[完整时间轴](../01_master_timeline.md)是人工阅读入口；[records.json](records.json)是同一事件集的结构化记录，两者由_build/render.py同步生成。EV稳定，显示排序不重编号。\n\n[状态链](STATE_CHAINS.md)记录重要跨阶段转换、未决问题和时间张力。本轮不另造逐章摘要或重复的单事件全文文件。\n')
write('knowledge/README.md','# 知识导航\n\n[知识TEMP索引](TEMP_INDEX.md)记录本轮信息传播边。正式K数据库、命题拆解、每角色知识快照尚未建立。后续须保留TEMP→正式ID映射。\n')
write('relationships/README.md','# 关系导航\n\n[关系TEMP索引](TEMP_INDEX.md)保留重要有向变化。正式人物关系数据库尚未建立；不以亲密度替代关系类型，也不实施好感/CG设计。\n')
print('rendered',len(R),'events',len(reg['knowledge']),'knowledge',len(reg['relationships']),'relationships')
