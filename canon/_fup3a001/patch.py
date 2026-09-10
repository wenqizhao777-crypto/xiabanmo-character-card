"""One-time FUP-3A-001 correction. No historical builder or Performance mutation."""
from pathlib import Path
import json,hashlib,zipfile,copy,sys,importlib.util,re
sys.dont_write_bytecode=True
P=Path(__file__).resolve().parents[2];C=P/'canon';B=C/'_fup3a001'
assert not (B/'changes.json').exists(),'One-time patch already applied'
paths=['events/records.json','01_master_timeline.md','knowledge/records.json','knowledge/K018.md','knowledge/K098.md','knowledge/by_character/CH002_knowledge.md','knowledge/KNOWLEDGE_TRANSITIONS.md','STAGE3A_PATCH_FOLLOWUPS.md','README.md','BASELINE_MANIFEST.md']
baseline={p.relative_to(P).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in P.rglob('*') if p.is_file() and B not in p.parents and '__pycache__' not in p.parts and p.suffix!='.pyc'}
(B/'input_hashes.json').write_text(json.dumps(baseline,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with zipfile.ZipFile(B/'before.zip','w',zipfile.ZIP_DEFLATED) as z:
 for p in paths:z.writestr('canon/'+p,(C/p).read_bytes())
log=[]
def load(p):return json.loads((C/p).read_text(encoding='utf-8-sig'))
def write(p,s):
 f=C/p;raw=f.read_bytes();newline='\r\n' if b'\r\n' in raw else '\n'
 f.write_bytes((b'\xef\xbb\xbf' if raw.startswith(b'\xef\xbb\xbf') else b'')+s.replace('\r\n','\n').replace('\n',newline).encode('utf-8'))
def record(p,id,field,old,new):
 assert old!=new
 log.append({'patch_id':f'F3A2-{len(log)+1:03}','followup':'FUP-3A-001','path':p,'record':id,'field':field,'before':copy.deepcopy(old),'after':copy.deepcopy(new),'reason':'核查原著及人物视角，撤回无据同人猜测/主动否定；保留恋爱误解与未识破边界，或同步其必要导航/版本状态。'})
def replace(p,old,new):
 s=(C/p).read_text(encoding='utf-8-sig');assert s.count(old)==1,(p,s.count(old),old[:60]);record(p,None,'text',old,new);write(p,s.replace(old,new,1))
def append(p,s):
 old=(C/p).read_text(encoding='utf-8-sig');record(p,None,'append',None,s);write(p,old.rstrip()+'\n\n'+s+'\n')

events=load('events/records.json');e=next(x for x in events if x['id']=='EV0067')
old=e['later_informed'];new=old.split('；林小璐')[0]+'；林小璐依据月圆夜见闻和摩丝说法持有恋爱误解，仍分别看待爸爸与翠雀；未获同一身份信息'
record('events/records.json','EV0067','later_informed',old,new);e['later_informed']=new
replace('01_master_timeline.md',old,new)
old=copy.deepcopy(e['knowledge']);e['knowledge'][1]=['林小璐','林昀＝翠雀','UNKNOWN','UNKNOWN','仍以两人/恋爱关系解释；没有同一身份披露，不据E193旧摘要补猜中与主动否定']
record('events/records.json','EV0067','knowledge',old,e['knowledge'])
replace('01_master_timeline.md','|林小璐|林昀＝翠雀|SUSPECTED → REJECTED|自行压下猜测改信恋爱|','|林小璐|林昀＝翠雀|UNKNOWN → UNKNOWN|仍以两人/恋爱关系解释；未获同一身份信息，不补猜中与主动否定|')
write('events/records.json',json.dumps(events,ensure_ascii=False,indent=2)+'\n')

knowledge=load('knowledge/records.json');k=next(x for x in knowledge if x['id']=='K018');k98=next(x for x in knowledge if x['id']=='K098');s=next(x for x in k['states'] if x['id']=='K018-T005');old=copy.deepcopy(s)
s.update(from_state='UNAWARE',to_state='UNAWARE',known_content='我仍分别看待爸爸与翠雀，把月圆夜的离家和救援解释为爸爸找来了翠雀，认为二人在恋爱；未识破同一身份。',source='当期小璐视角与恋爱误解；无同一身份披露',observation='月圆夜父亲离家、翠雀救援及摩丝的暧昧说法；梦境被本人解释为母亲认可后妈',interpretation='源文只支持当期的两人/恋爱解释，不支持她先猜同人再主动否定。E193旧摘要的电话线索不得移给小璐；恋爱片段只沿K098限定导航读取，不能授予K018。',knowledge_grade='A',certainty='本时点未识破同一身份；不证明她终生从未产生任何疑问',correctness='UNKNOWN')
record('knowledge/records.json','K018-T005','state_record',old,s)
oldref=copy.deepcopy(k98['cross_references']);origin=k98['cross_references'][0]
origin.update(content_scope='仅投影CH002在既有EV0067来源锚点持有的恋爱误解，不把K018的UNAWARE转换成K098状态，不提供同一身份秘密。',known_content_fragment='爸爸与翠雀有秘密的情侣关系，是爸爸在月圆夜把翠雀找来。',qualification='FUP-3A-001已核证为REJECT_CAUSAL_INTERPRETATION；原节点的先猜同人再否定撤回。来源锚点仍为保守接管位置，不宣称首次产生恋爱想法；本导航需由调用者按主体/时间显式读取。')
record('knowledge/records.json','K098','cross_references',oldref,k98['cross_references'])
write('knowledge/records.json',json.dumps(knowledge,ensure_ascii=False,indent=2)+'\n')

replace('knowledge/K018.md','### K018-T005｜CH002｜SUSPECTS → DISBELIEVES','### K018-T005｜CH002｜UNAWARE → UNAWARE')
for label,key in [('当时可知内容','known_content'),('来源/方式','source'),('Observation（实际接触的线索）','observation'),('Interpretation（如何理解）','interpretation')]:
 if key=='interpretation':
  text=(C/'knowledge/K018.md').read_text(encoding='utf-8-sig');start=text.index('### K018-T005');end=text.index('### K018-T006');block=text[start:end];newblock=block.replace(old[key],s[key],1);replace('knowledge/K018.md',block,newblock)
 else:replace('knowledge/K018.md',f'- {label}：'+old[key],f'- {label}：'+s[key])
replace('knowledge/K018.md','- 确信：不接受此命题；内容正确性：CORRECT_WITHIN_SCOPE；认知证据层：D。','- 确信：'+s['certainty']+'；内容正确性：UNKNOWN；认知证据层：A。')

nav='''## Stage 3A.2｜FUP-3A-001 核证后的误解链导航

[K018-T005](K018.md)仍是 CH002／EV0067／L14075 的保守来源锚点，但其同人命题状态已纠正为 **UNAWARE → UNAWARE**；「先猜同人再主动否定」不再作为当期事实。既有来源中的恋爱误解有[L13835–13854](../../source/下班，然后变成魔法少女_第1-282章.txt:13835)、[L13969–13983](../../source/下班，然后变成魔法少女_第1-282章.txt:13969)支持。

恢复该锚点之后、K098-T001／EV0092／L20884 之前的窗口，调用者沿 **K098.cross_references** 按 CH002、CURRENT、来源 point 与纠正截止节点读取 `known_content_fragment`；这是已核证恋爱误解的限定投影，不要求生产查询把 K018 放进 allowed，也不允许从 denied 的秘密命题抽取额外知识。早于锚点、不同比较时间层或其他主体均不授予。

到 EV0092 后优先采用[K098-T001](K098.md)的原 **DISBELIEVES**，不得继续注入旧恋爱说。纠正由[L20745–20746](../../source/下班，然后变成魔法少女_第1-282章.txt:20745)的林昀概括及[L20800–20805](../../source/下班，然后变成魔法少女_第1-282章.txt:20800)的小璐内心回顾共同支持。K018 的 UNAWARE 与 K098 的 DISBELIEVES 是不同命题，不能互换。

生产 `query_knowledge.py` 未改；早期直接过滤 K098.states 仍无节点，须显式补读导航。235 个 K、365 个 T 不变，两个原有锚点不动。原 Stage 3A 导航及旧状态完整保存在[本轮前像](../_fup3a001/before.zip)与[变更日志](../CHANGELOG_FUP3A001.md)；裁定见[FUP Review](../FUP3A001_REVIEW.md)。'''
for p in ['knowledge/K018.md','knowledge/K098.md']:
 text=(C/p).read_text(encoding='utf-8-sig');tail=text[text.index('## Stage 3A Patch｜误解链交叉导航'):].rstrip();replace(p,tail,nav)

p='knowledge/by_character/CH002_knowledge.md'
oldline='- [K018](../K018.md) `K018-T005`｜EV0067／CURRENT／**DISBELIEVES**：'+old['known_content']
replace(p,oldline+'\n','')
replace(p,'## 明确不知道的重要事项','## 明确不知道的重要事项\n\n- [K018](../K018.md) `K018-T005`｜EV0067／CURRENT／**UNAWARE**：'+s['known_content'])
text=(C/p).read_text(encoding='utf-8-sig');tail=text[text.index('## Stage 3A Patch｜恋爱误解的阶段导航'):].rstrip()
replace(p,tail,'## Stage 3A.2｜恋爱误解与身份未知分开读取\n\nK018-T005 已纠正为 UNAWARE→UNAWARE；不再假定先猜同人再主动否定。EV0067 后、EV0092 前的恋爱误解仍按 [K098.cross_references](../K098.md) 的限定片段与原锚点显式恢复；EV0092 后采用 K098-T001 的不再相信。早期生产查询不再把 K018-T005 放入 allowed；不能因此抹去有源的恋爱误解。见[核证结论](../../FUP3A001_REVIEW.md)及[Changelog](../../CHANGELOG_FUP3A001.md)。')
p='knowledge/KNOWLEDGE_TRANSITIONS.md'
oldrow='|[K018](K018.md) K018-T005|CH002|SUSPECTS|DISBELIEVES|[EV0067](../01_master_timeline.md#ev0067)|自行压下猜测改信恋爱：'+old['known_content']+'|L13593–13700,L13701–13817,L13818–13876,L13877–14010,L14011–14075|'
newrow='|[K018](K018.md) K018-T005|CH002|UNAWARE|UNAWARE|[EV0067](../01_master_timeline.md#ev0067)|'+s['source']+'：'+s['known_content']+'|L13593–13700,L13701–13817,L13818–13876,L13877–14010,L14011–14075|'
replace(p,oldrow,newrow)
text=(C/p).read_text(encoding='utf-8-sig');tail=text[text.index('## Stage 3A Patch｜跨命题衔接'):].rstrip()
replace(p,tail,'## Stage 3A.2｜跨命题衔接（非新增 Transition）\n\nCH002：EV0067 的恋爱误解 → EV0092 的不再相信。K018-T005 的同一身份命题改为 UNAWARE→UNAWARE，原恋爱片段继续由 [K098 交叉导航](K098.md)按主体及原时点投影；K098-T001 原 DISBELIEVES 不变。不是从 K018 的未知反推恋爱，也不是从 K098 的否定确认同人。365 个原 T ID 与锚点均保留，详见 [FUP Review](../FUP3A001_REVIEW.md)。')

# Refresh only the affected subject's displayed query counts; original CH002 snapshots remain byte-exact.
spec=importlib.util.spec_from_file_location('q',C/'knowledge/query_knowledge.py');q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
p='knowledge/by_character/CH002_knowledge.md';text=(C/p).read_text(encoding='utf-8-sig')
for ev in ['EV0003','EV0090','EV0099','EV0156']:
 r=q.lookup('CH002',ev);pattern=rf'- \*\*S\d+｜{ev}\*\*：[^\n]+';line=re.search(pattern,text).group(0)
 new=re.sub(r'可返回\d+条状态，拦截/待核\d+条',f"可返回{len(r['allowed'])}条状态，拦截/待核{len(r['denied_or_unresolved'])}条",line)
 if new!=line:replace(p,line,new)

replace('STAGE3A_PATCH_FOLLOWUPS.md','- 状态：**OPEN / SOURCE_CHAIN_REVIEW_REQUIRED**。','- 当前状态：**RESOLVED**；Stage 3A.2 核证结论 **REJECT_CAUSAL_INTERPRETATION**，详见 [FUP3A001_REVIEW](FUP3A001_REVIEW.md)。\n- 以下为 Stage 3A 建项时的历史快照，保留原判断与后续路径，不作为当前待核状态。\n- 历史状态：**OPEN / SOURCE_CHAIN_REVIEW_REQUIRED**。')
append('STAGE3A_PATCH_FOLLOWUPS.md','## Stage 3A.2 结案\n\nFUP-3A-001 = **RESOLVED**；结论 **REJECT_CAUSAL_INTERPRETATION**（任务 A/B/C 中属于 C：指定因果链不足以成立，连其首两步的顺序也未由所引原文确认）。电话试探及同人确认属于夏凉；小璐的完整恋爱推理并未写出先猜同人再主动否定。不得再把这一机制用作 CANON_PATTERN 或稳定 INTERPRETIVE_MODEL。\n\nEV0067 与 K018-T005 的相应无据归因已最小纠错；客观 truth、所有稳定编号、原时点及恋爱误解窗口不变。证据、前后像、局部回归、Performance 同步建议见 [Review](FUP3A001_REVIEW.md)和[Changelog](CHANGELOG_FUP3A001.md)。Performance 仍只读，尚未执行本次建议。V1.1 是保留的历史冻结基线，工作副本含本补丁，未自动冻结新版本。')

banner='''> **Stage 3A.2 当前工作副本说明：** 已应用 FUP-3A-001 的有日志最小纠错，当前工作副本不再与 V1.1 字节相同。**CANON_BASELINE_V1.1 = FROZEN 仅指保留的历史基线**；本轮没有建立或冻结 V1.2。当前增量依据是 [FUP3A001_REVIEW](FUP3A001_REVIEW.md)及 [CHANGELOG_FUP3A001](CHANGELOG_FUP3A001.md)，文件前后哈希见 [_fup3a001/verification.json](_fup3a001/verification.json)。以下原 V1.1 说明及统计作为历史保留；既有编号数量不变。'''
for p in ['README.md','BASELINE_MANIFEST.md']:
 text=(C/p).read_text(encoding='utf-8-sig');first=text.split('\n',1)[0];replace(p,first,first+'\n\n'+banner)

(B/'changes.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'patches':len(log),'modified_files':len({x['path'] for x in log}),'counts':{'EV':len(events),'K':len(knowledge),'T':sum(len(x['states']) for x in knowledge)}},ensure_ascii=False))
