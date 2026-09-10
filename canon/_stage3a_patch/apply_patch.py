"""One-time, four-request navigation/disambiguation patch. No historical builder invocation."""
from pathlib import Path
import json,copy
P=Path(__file__).resolve().parents[2];C=P/'canon';B=C/'_stage3a_patch';log=[]
def load(path):return json.loads((C/path).read_text(encoding='utf-8-sig'))
def write(path,text):
 f=C/path;raw=f.read_bytes() if f.exists() else b'';bom=raw.startswith(b'\xef\xbb\xbf');old=raw.decode('utf-8-sig');newline='\r\n' if '\r\n' in old else '\n'
 text=text.replace('\r\n','\n').replace('\n',newline);f.write_bytes((b'\xef\xbb\xbf' if bom else b'')+text.encode('utf-8'))
def field(cr,db,id,key,new):
 r=next(r for r in db if r['id']==id);old=copy.deepcopy(r.get(key));assert old!=new
 log.append(dict(id=f'P3A-{len(log)+1:03}',request=cr,path='characters/records.json' if id.startswith('CH') else 'knowledge/records.json',record=id,field=key,before=old,after=new,kind='DISAMBIGUATION_OR_NAVIGATION',facts_changed=False));r[key]=new

def replace(cr,path,old,new):
 f=C/path;s=f.read_text(encoding='utf-8-sig');assert old in s,(path,old);assert old!=new
 log.append(dict(id=f'P3A-{len(log)+1:03}',request=cr,path=path,field='exact_text',before=old,after=new,kind='MIRRORED_TEXT_OR_NAVIGATION',facts_changed=False));write(path,s.replace(old,new))
def append(cr,path,text):
 s=(C/path).read_text(encoding='utf-8-sig');log.append(dict(id=f'P3A-{len(log)+1:03}',request=cr,path=path,field='append_navigation',before=None,after=text,kind='NAVIGATION_ONLY',facts_changed=False));write(path,s.rstrip()+'\n\n'+text+'\n')
H=load('characters/records.json');K=load('knowledge/records.json');CH={x['id']:x for x in H};KK={x['id']:x for x in K}
cr='CR-3A-001';oldstage=CH['CH005']['stages'][1][2];newstage='A：E071、EV0017；常规退役使原魔力源封存，不等兽化受控期不能感知妖精；该期已有妮妮交流（EV0053、REL056），不能把表面退役状态当全部实际能力'
st=copy.deepcopy(CH['CH005']['stages']);st[1][2]=newstage;field(cr,H,'CH005','stages',st)
oldnav=CH['CH005']['knowledge'];newnav='开篇掌握局方记录不等知道所有旧战争内幕；受控改造期间已能与妮妮交流（EV0053、REL056），月圆节林昀才发现其能见摩可。EV0054记人形及感官恢复，后续少女战力另按EV0074等节点；不把复原误作首次获得妖精感知，也不据此断言取回原封印魔力源或全部旧能力。最后视频只提供联络范围。'
field(cr,H,'CH005','knowledge',newnav)
# Source-rendered stage contains links; replace only the inaccurate clause.
replace(cr,'characters/CH005_红思与.md','看听妖精能力不能延续','常规退役使原魔力源封存，不等兽化受控期不能感知妖精；该期已有妮妮交流（EV0053、REL056），不能把表面退役状态当全部实际能力')
for path in ['characters/CH005_红思与.md','knowledge/by_character/CH005_knowledge.md']:replace(cr,path,oldnav,newnav)
cr='CR-3A-002';nav='评价导航：CH029→CH006；现任紫钻向小璐自述曾有公务接触、无私交，并回顾自己对樱的疑虑及可能偏见（D/E，EV0135，L34287–34298）。仅导航评价者视角；不确认安雅有阴谋，不推其回向态度。'
for id,name in [('CH006','安雅'),('CH029','现任紫钻')]:
 field(cr,H,id,'relations',CH[id]['relations']+' '+nav)
 f=f'characters/{id}_{name}.md';s=(C/f).read_text(encoding='utf-8-sig');needle='相关事件所登记的 TEMP 入口：';start=s.index('## 9｜');pos=s.index(needle,start)
 linked=nav.replace('CH029→CH006','[CH029](CH029_现任紫钻.md)→[CH006](CH006_安雅.md)').replace('EV0135','[EV0135](../01_master_timeline.md#ev0135)').replace('L34287–34298','[L34287–34298](../../source/下班，然后变成魔法少女_第1-282章.txt:34287)')
 replace(cr,f,s[pos:pos+len(needle)],linked+'\n\n'+needle)
append(cr,'relationships/RELATIONSHIP_MATRIX.md','## Stage 3A Patch｜尚未单建REL的评价导航\n\n[CH029 现任紫钻](../characters/CH029_现任紫钻.md) → [CH006 安雅](../characters/CH006_安雅.md)：在[EV0135](../01_master_timeline.md#ev0135)对小璐回述公务接触、无私交及昔日疑虑，承认可能偏见（[L34287–34298](../../source/下班，然后变成魔法少女_第1-282章.txt:34287)）。D/E评价不等安雅有阴谋，也不补安雅的回向认知。此处是可发现性导航，不是新REL，不增加未知以外的关系维度。')
cr='CR-3A-003';reason=CH['CH010']['reason'];newreason='长期队友，参与招募、登记联络、术语解释与家庭关系误会的流转；未证获得K018（林昀＝翠雀），不因Tier A或信息流转作用授予身份秘密'
field(cr,H,'CH010','reason',newreason);replace(cr,'characters/CH010_摩可.md',reason,newreason)
old=CH['CH010']['knowledge'];new=old+' K226保持UNKNOWN：未证获得K018，按无证不授予处理，不反推已证实永远不知道。'
field(cr,H,'CH010','knowledge',new)
for path in ['characters/CH010_摩可.md','knowledge/by_character/CH010_knowledge.md']:replace(cr,path,old,new)
cr='CR-3A-004'
origin={'kind':'ORIGIN_NAVIGATION_ONLY','knowledge_id':'K018','transition_id':'K018-T005','subject':'CH002','event':'EV0067','point':14075,'content_scope':'仅导航该节点所含的父亲与翠雀恋爱误解片段；K018的DISBELIEVES是在否定同一身份，不能复制成K098的认知状态。','valid_until_transition':'K098-T001','source_ranges':[[13835,13854],[13969,13983]],'qualification':'原文支持持有恋爱误解；不以此额外证实先猜同人再否定的因果，见STAGE3A_PATCH_FOLLOWUPS。节点是保守接管位置，不宣称首次产生该想法。'}
field(cr,K,'K098','cross_references',[origin]);field(cr,K,'K018','cross_references',[{'kind':'MISCONCEPTION_CONTINUATION','knowledge_id':'K098','transition_id':'K098-T001','subject':'CH002','event':'EV0092','origin_transition_id':'K018-T005','content_scope':'恋爱误解片段后来被放下，仍未由此确认林翠同人。原有两命题的truth和各自state不互换。'}])
text='## Stage 3A Patch｜误解链交叉导航（不新增T节点）\n\n[K018](K018.md)的`K018-T005`（CH002／EV0067）包含“改认为二人在恋爱”的误解片段；[L13835–13854](../../source/下班，然后变成魔法少女_第1-282章.txt:13835)、[L13969–13983](../../source/下班，然后变成魔法少女_第1-282章.txt:13969)支持当期持有该解释。[K098](K098.md)的`K098-T001`（EV0092）记录后来不再相信，依据[L20728–20746](../../source/下班，然后变成魔法少女_第1-282章.txt:20728)，其中L20746是林昀听取陈述后的概括。\n\n恢复EV0067之后、EV0092之前的快照时，先查询同主体同阶段的K018，沿`cross_references`读取限定恋爱误解片段；到EV0092再采用K098-T001的DISBELIEVES。K018的DISBELIEVES否定“同一身份”，不能直接当成否定“恋爱”。早于源节点不授予；不能跨主体共享。\n\n本次选用导航方案：235个K和365个T节点不变，原查询函数不新增隐式联查。只过滤K098的states在早期仍没有直接节点，调用者须依本交叉导航补读K018；不会伪称已为K098新增MISUNDERSTANDS状态。\n\n“先猜中同一人再主动否定”的更强因果在本次所读关键段未获直接核实，保留原记录并另列[后续复核](../STAGE3A_PATCH_FOLLOWUPS.md)，不由本导航升级为新事实。'
for path in ['knowledge/K018.md','knowledge/K098.md']:append(cr,path,text)
append(cr,'knowledge/by_character/CH002_knowledge.md','## Stage 3A Patch｜恋爱误解的阶段导航\n\n[K098](../K098.md)与[K018](../K018.md)现已双向交叉导航：EV0067后从K018-T005读取当期恋爱误解片段；EV0092采用K098-T001的不再相信。直接K098查询在早期没有T节点，需要按本导航补读；既有状态值不互换，也不授予林翠同人秘密。此为导航补全，不是增加确认知识。“先猜中再否定”的因果另见[待核项](../../STAGE3A_PATCH_FOLLOWUPS.md)。')
append(cr,'knowledge/KNOWLEDGE_TRANSITIONS.md','## Stage 3A Patch｜跨命题衔接（非新增Transition）\n\nCH002：[K018-T005](K018.md)／EV0067的恋爱误解片段 → [K098-T001](K098.md)／EV0092的不再相信。前者DISBELIEVES针对“同一人”，后者DISBELIEVES针对“恋爱”，不可混成同一命题。来源限定与恢复方法见[K098交叉导航](K098.md)。本表仍为365个原T节点。')
write('characters/records.json',json.dumps(H,ensure_ascii=False,indent=2)+'\n');write('knowledge/records.json',json.dumps(K,ensure_ascii=False,indent=2)+'\n')
(B/'patch_changes.json').write_text(json.dumps(log,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Logged patches',len(log),'unique files',len({x['path'] for x in log}))
