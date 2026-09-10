"""Stage 2B-4: authored decisions -> auditable files. Writes knowledge/ only.
curation.tsv is manual semantic curation, not an automatic truth classifier.
"""
from pathlib import Path
import re,json,copy,collections
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'canon/knowledge'
def read(p):return (ROOT/p).read_text(encoding='utf-8-sig')
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
EV={x['id']:x for x in json.loads(read('canon/events/records.json'))}
CH={x['id']:x for x in json.loads(read('canon/characters/records.json'))}
REL=json.loads(read('canon/relationships/records.json'))
EE={x['id']:x for x in json.loads(read('audit/evidence_records.json'))}
TEMP={}
for b in re.split(r'(?=<a id="k_temp_)',read('canon/knowledge/TEMP_INDEX.md'))[1:]:
 n=int(re.search(r'## K_TEMP_(\d+)',b)[1]); rows=[]
 for ev,h,fr,to,ch in re.findall(r'\|\[(EV\d+)\][^|]+\|([^|]+)\|([^|]+?) → ([^|]+)\|([^|]+)\|',b):rows.append(dict(event=ev,holder=h,old_from=fr,old_to=to,channel=ch))
 TEMP[n]={'id':f'K_TEMP_{n:03}','title':re.search(r'## K_TEMP_\d+｜([^\n\r]+)',b)[1],'rows':rows,'raw':b}
SPEC={};MERGE={};WHY={}
for line in Path(__file__).with_name('curation.tsv').read_text(encoding='utf-8').splitlines():
 f=line.split('|');n=int(f[0])
 if f[1].startswith('='):MERGE[n]=int(f[1][1:]);WHY[n]=f[2]
 else:SPEC[n]=dict(proposition=f[1],type=f[2],truth=f[3],grade=f[4],scope=f[5],boundary=f[6])
assert set(SPEC)|set(MERGE)==set(range(1,208))
def base(n):return base(MERGE[n]) if n in MERGE else n
names={}
for c in CH.values():names[c['name']]=c['id']
for cid,ns in {1:'翠雀 矢车菊 林昀',2:'白玫 小璐 林小璐 小',3:'夏凉 小锦 夏',4:'白静萱 薄雪 白',5:'红思与 朝颜 红',6:'安雅 樱',7:'玛格丽特 麻生圆香 玛',8:'祖母绿 祖',9:'妮娜 墨荷 黑猫',10:'摩可',11:'妮妮',12:'摩丝 蛾',13:'鸢 陆红豆 唐菖蒲',14:'白狼',15:'金蛇 郁金香',20:'妮姆',24:'木百合 木',29:'新紫钻',34:'猫眼 金绿猫眼'}.items():
 for n in ns.split():names[n]=f'CH{cid:03}'
names.update({'土丁桂':'CH030','兔形妖精':'CH042'})
GROUPS={}
expansions={'翠雀/小璐':['CH001','CH002'],'林昀/翠雀':['CH001'],'小璐/夏凉':['CH002','CH003'],'三新人':['CH002','CH003','CH004'],'翠雀、玛格丽特':['CH001','CH007'],'小璐、白静萱':['CH002','CH004'],'追击四新人':['CH002','CH003','CH023','CH025'],'两队新人':['CH002','CH003','CH004','CH023','CH024','CH025'],'四人':['CH002','CH004','CH026','CH027'],'夏凉、姐妹':['CH003','CH055','CH056']}
expansions['在场九人']=['CH001','CH002','CH003','CH004','CH005','CH007','CH023','CH024','CH025']
expansions['其余在场同伴']=['CH002','CH003','CH005','CH007','CH023','CH024','CH025']
def subjects(holder,event):
 if holder=='读者':return []
 if holder in expansions:return expansions[holder]
 parts=re.split(r'[、/]',holder)
 if all(x in names for x in parts):return list(dict.fromkeys(names[x] for x in parts))
 key=(event,holder)
 if key not in GROUPS:
  gid=f'G{len(GROUPS)+1:03}';GROUPS[key]=dict(id=gid,label=holder,event=event,members=[],membership='仅原文所指本次实际听见/目击者；未给全名时不补名册。',scope='EVENT_LOCAL',grant_policy='不可因组织/参赛资格自动加入本组；须另核原文在场与接收。')
 return [GROUPS[key]['id']]
NORM={'UNKNOWN':'UNKNOWN','CONFIRMED':'CONFIRMED','PARTIALLY_CONFIRMED':'PARTIAL','INFERRED':'SUSPECTS','SUSPECTED':'SUSPECTS','MISUNDERSTOOD':'MISUNDERSTANDS','REJECTED':'DISBELIEVES','BELIEVED':'BELIEVES'}
# Historical acquisitions are not ordered by EV number or reveal line. No total order is invented.
HIST={9,10,37,50,51,52,53,58,79,81,95,111,118,141,142,143,144,145,146,147,148,165,166,167,168,169,176,177,178,180,181,182,183,184,185,187,189}
historical_relations=[(189,37),(37,111),(111,118),(118,141),(141,142),(142,143),(143,144),(144,145),(145,146),(146,176),(176,147),(147,148),(142,177),(177,147),(148,165),(147,180),(180,181),(168,169),(169,181),(51,183),(183,184),(184,182),(182,9),(9,10),(182,52),(52,53),(95,166),(166,167)]
def when(ev,ranges,force=None,point=None):
 number=int(ev[2:]);epoch=force or ('HISTORY' if number in HIST else 'CURRENT')
 return dict(epoch=epoch,event=ev,point=point if point is not None else (max(b for a,b in ranges) if epoch=='CURRENT' else None),description=EV[ev]['time'],order_policy='历史用偏序，不按回忆在正文的行号；当代用实际发生/获知子段末行作边界。')
RECORDS=[];BYTEMP={};CHANGES=[]
def make(spec,temps):
 r=dict(id=f'K{len(RECORDS)+1:03}',**spec,canon_status={'A':'CONFIRMED','B':'STRONGLY_SUPPORTED','C':'INFERRED','D':'UNKNOWN','E':'UNKNOWN','F':'UNKNOWN'}[spec['grade']],source_layer='NOVEL_TEXT',temp_ids=[TEMP[t]['id'] for t in temps],states=[],reader_revelations=[],disclosures=[],evidence_navigation=[],source_ranges=[],events=[],character_refs=[],organization_refs=[],power_refs=[],relationship_refs=[],truth_scope='命题限定的事件/时期；不是无条件永久当前事实。',default_deny=True,if_boundary='不采用旧卡补桥、原创会议、提前坦白或用户全知。')
 RECORDS.append(r)
 for t in temps:BYTEMP.setdefault(t,[]).append(r)
 return r
for n,s in SPEC.items():make(s,[t for t in TEMP if base(t)==n])
def add_state(r,subject,event,fr,to,content,channel,ranges=None,epoch=None,point=None,grade=None,certainty=None,disclosure='NOT_DISCLOSED',source_subjects=None,observation=None,interpretation=None,validity='PERSISTENT_AS_KNOWLEDGE',temp=None):
 ranges=ranges or EV[event]['source_ranges'];time=when(event,ranges,epoch,point)
 g=dict(subject=subject,event=event,from_state=fr,to_state=to,known_content=content,source=channel,source_subjects=source_subjects or [],acquisition=time,first_acquisition_note='本命题对此主体有证据的节点；UNKNOWN前态不声称这是生命中第一次接触。',source_ranges=ranges,evidence_navigation=EV[event]['audit_navigation'],knowledge_grade=grade or ('D' if to in ['SUSPECTS','BELIEVES','MISUNDERSTANDS','DISBELIEVES'] else 'A'),certainty=certainty or {'CONFIRMED':'确信本条限定内容','PARTIAL':'仅掌握所列片段，未证全貌','HEARD':'听到；是否采信未证','SUSPECTS':'线索推测未确认','MISUNDERSTANDS':'持错误/失真解释','UNAWARE':'本时点明确未获知','UNKNOWN':'未证是否获知','MEMORY_LOSS':'记忆有缺口，不能恢复完整经历','DISBELIEVES':'不接受此命题','BELIEVES':'相信但独立真值另查'}.get(to,'见状态'),correctness='UNKNOWN' if r['truth'] in ['UNKNOWN','DISPUTED'] or to in ['UNKNOWN','UNAWARE','HEARD','PARTIAL','SUSPECTS','MEMORY_LOSS'] else ('CORRECT_REJECTION' if to=='DISBELIEVES' and r['truth']=='FALSE' else 'INCORRECT' if to=='MISUNDERSTANDS' or (r['truth']=='FALSE' and to in ['BELIEVES','CONFIRMED']) else 'CORRECT_WITHIN_SCOPE'),observation=observation or channel,interpretation=interpretation or ('仅上述知识范围；完整机制/动机/来源和未来结果不由此推定。'),disclosure_state=disclosure,sharing='NO_AUTOMATIC_SHARING',validity=validity,temp_origin=TEMP[temp]['id'] if temp else None)
 r['states'].append(g);return g
def record_for(t):return BYTEMP[t][0]
for t,data in TEMP.items():
 r=record_for(t)
 for row in data['rows']:
  ev=row['event'];holder=row['holder'];rg=None;ep=None;pt=None;fr=NORM[row['old_from']];to=NORM[row['old_to']]
  if t==195:holder='翠雀';rg=[[15428,15474]]
  if t in [186,204]:continue # same acquisition duplicated in188/97; retain full TEMP mapping.
  if t==39:ev='EV0039';rg=[[8390,8438]];ep='CURRENT'
  if t==19:ev='EV0020';rg=[[4299,4311]];ep='CURRENT'
  if t==196:rg=[[10204,10216]];to='MEMORY_LOSS'
  if t==198:rg=[[37924,38025]]
  if t in [188]:rg=[[38595,38618]]
  if t==197:rg=[[14859,14912]]
  if t==93:rg=[[18678,18718]];ep='CURRENT'
  if t==205:rg=[[19364,19371]];ep='HISTORY'
  if t in [20,136] and to=='UNKNOWN':to='UNAWARE'
  if t in [15,51,150,174] and to=='UNKNOWN':to='UNAWARE'
  if t in [13,68,73,75,78,123,126,130,133,154,155,186,188,198,199,189]:
   if to=='PARTIAL':to='HEARD'
  if t==137:to='DISBELIEVES'
  if t==110:to='MISUNDERSTANDS'
  if t==72:to='MISUNDERSTANDS'
  if t==154:to='HEARD'
  if t==199:rg=[[38060,38228]]
  content=r['proposition']
  content_overrides={4:'摩可称自己从花园偷跑后获得任命；来历与任命细节只听其自述。',8:'小璐把父亲在葬礼拥抱另一女子理解成背弃母亲。',14:'夏说父亲死去、母亲因杀父坐牢；她对自己责任和母亲动机的解释未获独立证实。',19:'爸爸说在我上电视那天就知道我是魔法少女。',25:'摩可承诺变身能治病、恢复眼睛；承诺还没有兑现。',32:'林昀和眼前矢车菊有关联；王把男身理解成女孩的社会伪装。',33:'获同伴转述和伤势线索：新人合作对抗兵触三；未亲眼看到全部战斗。',39:'听翠讲旧队成员先后加入和旧店往事；未因此获全部内心回忆。',42:'小前辈原本应是女性，后来变成男人；男性不可能成为魔法少女。',45:'翠雀出示的牌是矢车菊的牌，但为何如此、其男身和全部旧事仍不知道。',51:'尚未收到天音已觉醒的消息。',55:'红的反应显出无法自由说出幕后，完整控制机制尚不清楚。',62:'敌话让白听到樱已死及小璐是其女儿，之后昏迷不再接收后续说话。',66:'她所说的“女儿被黑烬袭击”让我领会翠雀与白玫父亲的关联。',71:'祖提出以兽之源协助修残存本相的方案，能否成功和具体操作待后续。',75:'兵蜂七称我与黑烬实验相关、父母是研究员，并贬低我的自我；其中恶意解释未核。',80:'朝颜恢复力量救援，现场表现可见；完整繁开解释另条。',82:'祖提出用本相造临时本体以帮助红继续生活工作；还不是完成证明。',88:'爸爸去世后查登记簿，才知2月14并非登记生日；我仍选择这一天。',93:'玛说猫眼两年前告诉她樱死并劝她不赴葬礼，以免把林推向复仇。',96:'翠透露假考生入境治疗计划；更早红已知道，不等三后辈也知。',97:'玛转述苏最后通话说要去间界，此后十二年没再联络；不知道是否真的到达。',102:'鸢报告兽源已归祖，但承认没有核实；白狼此时暂按真处理。',107:'我先当成繁开，鸢解释这是兽心解放；尚不掌握完整机制。',110:'杯中比例很低，是否翠已经撑不住了？',115:'翠说薄雪被黑烬当作祭子；玛明确还不知道祭子的定义。',117:'白自称祭子，讲湖畔战斗和兽魔；没有讲父母身份，战记已经修饰。',124:'翠说有秘密任务，须使用龙胆假号；并未解释治疗与政治全貌。',125:'准考证将龙胆写成十岁新人，我暂按证件认识她。',128:'自测丝线不再引魂痛，奇境能开；祖仍要求静养，不许立刻试繁开。',130:'墨称在替国度执行任务，我对这说法仍有疑虑。',132:'问爪痕联系后墨沉默，我怀疑她的团队与爪痕有关。',133:'墨说可以修复我的魔装；我未见修复完成。',134:'翠哭了，解释是想起往事；具体安雅送剑回忆没有完整告诉我。',136:'翠雀与林昀的生日似乎巧合地相同，尚未识破同一身份。',138:'祖说郁金香叛逃爪痕，结合她与墨共同活动，我确认墨团队与爪痕有关。',139:'祖根据线人情报多方推认郁金香就是金蛇。',145:'龙胆作为新人前辈与我互动，我还不知道她是翠雀。',150:'未在墨与蜂密谈现场，尚未由该密谈获黑猫代号。',153:'小白转告薄荷箭根薯有兽味，因此怀疑她们牵涉黑烬。',154:'听薄荷解释兽子、祭子、食祭规则，只掌握她所说部分。',155:'薄供出自己及箭、醉、羊、蛇等名单，仍须核实，不是全组织名册。',156:'检测资料有偏移异常，未识别成兽底色身份。',157:'检测和理论认为王钥有权杖潜力，还没实现授职或全部开发。',160:'木棉对武器的直觉和本场表现使我猜王钥可能还不圆满。',168:'感觉夏还在被追，后来才得成绩；不知道她预布了什么陷阱。',172:'刚才亲自确认妹妹安全；不预知后续命运。',174:'已经离开，未亲眼看石蒜独自昙开的现场。',175:'我想到一种或许能救队长的办法，还没有把全部猜测告诉她。',177:'处理伤员的人自称效忠国度；我见到其行为，但尚不能断定所有伤员的结局。',182:'记得特定交易经历和支出，可对账采取反制；这不等掌握普遍回溯机制。',183:'从现场对话知道薄荷箭根薯是姐妹且陷入食祭，不知道全部童年、半年受训与分派历史。',187:'白猜目标可能女王，羊说自己偷听过；缺乏场外确认。',188:'女王在眼前声称队长是她的孩子，我此前并不知道这条关系。',198:'女王自称我的母亲、唯一亲源，称我为女儿；我先激动认母，后出现疑惧与质问。',199:'女王解释战争与少女力量对她的依存；并未给出可独立核验的全貌。',200:'我赶到后听懂姐妹都牵挂对方，并阻止自伤；不是获知此前所有回忆。',204:'玛说最后一次通话只听苏要去间界，此后失联。',205:'苏在最后一次通话说准备去间界，目的称寻找自我；之后我失去联系。',206:'匿名声音只警告当晚残兽危险，尚没有地点。'}
  content=content_overrides.get(t,content)
  if holder=='读者':
   r['reader_revelations'].append(dict(event=ev,source_ranges=rg or EV[ev]['source_ranges'],note='仅叙述揭露/文本未解；不是CH、ORG或所有在场者的认知授权。',temp_origin=TEMP[t]['id']));continue
  for subject in subjects(holder,ev):
   if t==20 and subject=='CH002' and ev=='EV0067':content='我猜过爸爸和翠雀可能同一人，却自行否定，改认为二人在恋爱。'
   add_state(r,subject,ev,fr,to,content,row['channel'],rg,ep,pt,temp=t)
  if ev!=row['event'] or to!=NORM[row['old_to']] or holder!=row['holder']:CHANGES.append(dict(temp=TEMP[t]['id'],before=row,after={'event':ev,'state':to,'holder':holder},reason=r['boundary']))

def extra(prop,typ,truth,grade,scope,boundary,temps=(),events=()):
 r=make(dict(proposition=prop,type=typ,truth=truth,grade=grade,scope=scope,boundary=boundary),list(temps));r['events']=list(events);return r
def state(t,*args,**kw):return add_state(record_for(t),*args,**kw)
def split(t,prop,typ,truth='TRUE',grade='A',scope=None,boundary='',content=None):
 original=record_for(t);r=extra(prop,typ,truth,grade,scope or original['scope'],boundary or original['boundary'],[t])
 for s in original['states']:
  q=copy.deepcopy(s);q['known_content']=content or prop;q['correctness']='UNKNOWN';r['states'].append(q)
 return r

# Atomisation: compound TEMP is preserved in mapping, not duplicated as an unbounded payload.
split(3,'翠雀当场报出花牌41076','组织权限',content='她报花牌41076；尚未知道为什么牌对应旧名。')
split(5,'夏凉知道林小璐是魔法少女白玫','秘密身份',content='共同邀请与现场行动让我知道小璐是白玫。')
split(21,'合照显示安雅与旧队成员的旧交','人际关系',content='照片上有妈妈与旧队的人；尚不知林昀的少女身份。')
split(24,'当期引离已经表现魔力反射和传输','能力机制',content='测试见到镜面反射和魔力传送；仅当期范围，尚无后来迷宫用途。')
eye=split(25,'变身可以让白静萱缺失的肉眼永久再生','能力机制','UNKNOWN','D',boundary='摩可承诺未兑现；魔力改善视力不等肉眼再生。',content='摩可说变身可以恢复眼睛；我尚不知是否可靠。')
for s in eye['states']:s['to_state']='HEARD';s['correctness']='UNKNOWN'
split(27,'白静萱是福利院来袭者追索的目标','战斗情报',content='白当面说明她是目标；只知眼前合作相关信息。')
split(29,'工触十一已经死亡','生死状态',content='由对话与形势得工触十一死讯，尚非完整现场目击。')
wrong=split(32,'林昀男性身份只是女孩矢车菊的社会伪装','秘密身份','FALSE',content='林昀大概是女孩矢车菊为了社会生活伪装出的男性。')
for s in wrong['states']:s['to_state']='MISUNDERSTANDS';s['correctness']='INCORRECT';s['knowledge_grade']='D'
split(70,'局长宣布审查资格后提供魔法武装','计划',content='大会宣布先审资格再配武装；不是所有人已获得装备。')
split(73,'祖称两份兽之源曾分别受爪痕相关方掌握','历史事件','UNKNOWN','D',content='祖讲兽之源分流秘闻；我只有这份口述，非亲历完整流转。')
bl=split(75,'白静萱的父母因她而死且恶意利用她','家庭关系','UNKNOWN','D',content='敌人把父母死与我的存在联系起来，并贬低我的自我；我受到冲击，未独立核验。')
for s in bl['states']:s['to_state']='BELIEVES';s['correctness']='UNKNOWN';s['knowledge_grade']='D'
split(80,'朝颜的繁开名为忆海百记并涉及记录复制','能力机制',scope='SECRET',content='红仅向翠私下说明繁开和复制；敌人不因在附近就听到。')
split(82,'退役后红思与已经恢复魔力的个案存在','能力机制',content='红恢复力量的个案可见；祖的普遍恢复理论尚非全验证。')
split(105,'陆红豆知道林小璐是魔法少女','秘密身份',content='小璐自报父女关系并主动变身，我因此认出这个目标。')
split(111,'塞米能兽化并在本场展开巢穴','能力机制',content='亲眼遇兽形及巢穴分隔，不知道他早年如何获得该能力。')
risk=split(128,'翠雀再次透支献祭存在严重风险并须静养','能力限制','PARTIALLY_TRUE','D',content='祖制止繁开测试、要求静养并警告再献祭风险。')
split(130,'墨荷说义肢由妖精为她制作','伤势','UNKNOWN','D',content='墨称右手是妖精义肢；没有说其中两份本源位格。')
split(133,'墨荷能说出翠雀曾三次昙开的经历','私人秘密',content='墨说得出我三次昙开的事；其团队究竟共享多少信息尚不清楚。')
split(157,'王钥内部检测报告评级为S+','能力机制',content='本次内部检测采用花模板，结论S+；尚无公开SS。')
split(173,'偷袭祖母绿者自称蜂之使徒','身份',content='现场听其自报蜂之使徒；不确认与当代蜂同一。')
split(178,'墨荷在战争中失去了右臂','伤势',content='战后探望看见断臂；原伤过程与义肢未来配置另论。')
f=split(198,'女王称林格是带走林昀本相的大妖精长','家庭关系','UNKNOWN','D',content='女王称林格是园丁和大妖精长、带走了本相；林听后惊疑。')
f['states']=[s for s in f['states'] if s['subject']=='CH001'];f['states'][0]['source_ranges']=[[38000,38025]]
f=split(198,'女王称林昀的男孩身体由林格伪造','秘密身份','UNKNOWN','D',content='女王说林格丢弃原身体、伪造男孩身体；我不以此放弃男性认同。')
f['states']=[s for s in f['states'] if s['subject']=='CH001'];f['states'][0]['source_ranges']=[[38009,38025]]

# Additional stages, source-level corrections, disclosure chains.
state(201,'CH007','EV0083','UNKNOWN','CONFIRMED','猫眼在安雅死亡后、葬礼前通知樱死了。','猫眼→玛；玛当代回述',[[18678,18699]],epoch='HISTORY',source_subjects=['CH034'])
state(201,'CH004','EV0032','UNKNOWN','UNAWARE','还盼以后见到樱，不知道她已经死亡。','翠隐瞒，只说离开',[[6523,6543]])
state(201,'CH004','EV0055','UNAWARE','PARTIAL','敌人说樱死了，并说她是小璐的母亲。','摩丝当面揭示',[[11870,11942]],source_subjects=['CH012'])
state(201,'CH002','EV0009','UNKNOWN','CONFIRMED','妈妈已死，我参加了葬礼。','丧亲与葬礼亲历',[[1889,1959]],epoch='HISTORY')
state(36,'CH004','EV0055','MISUNDERSTANDS','DISBELIEVES','樱并非只是离开；听到她已死的说法。','摩丝→白',[[11870,11942]],source_subjects=['CH012'])
state(20,'CH007','EV0081','UNKNOWN','CONFIRMED','战后彼此解除变身，知道林昀与矢车菊是同一人；后来识翠继续接此人。','双方主动解除变身',[[17965,18030]],epoch='HISTORY',source_subjects=['CH001'])
state(20,'CH001','EV0189','UNKNOWN','CONFIRMED','自己能以心之种变成魔法少女；自己是林昀。','自身经历',[[444,510]],epoch='HISTORY')
state(20,'CH006','EV0037','UNKNOWN','CONFIRMED','林昀为保护我成为魔法少女，之后与我组队。','生前共同经历，未将远处目击连接补成亲见',[[7576,7589]],epoch='HISTORY')
state(20,'CH002','EV0158','UNAWARE','UNAWARE','仍分别看待爸爸与翠雀，没有得到同一身份坦白。','最终审计C006/C138与实际揭露对象核对',[[36205,36257],[38595,38825]],validity='BOUNDARY_ONLY')
state(20,'CH004','EV0158','UNAWARE','UNAWARE','仍把林昀爸爸和翠雀妈妈看成两人，没有男身秘密披露给我。','C009/S010末次认知边界核对',[[23577,23608],[38523,38593]],validity='BOUNDARY_ONLY')
state(35,'CH030','EV0149','UNKNOWN','CONFIRMED','龙胆就是翠雀，翠雀就是矢车菊；不知道其男性日常身份。','本人揭伪装并报号',[[36205,36257]],source_subjects=['CH001'])
state(35,'CH032','EV0149','UNKNOWN','CONFIRMED','已听本人报少女代号链；没有听林昀男身。','本人揭伪装并报号',[[36205,36257]],source_subjects=['CH001'])
for t in [125,145,165]:
 for who in ({125:['CH030'],145:['CH032'],165:['CH030','CH032']}[t]):state(t,who,'EV0149','MISUNDERSTANDS','DISBELIEVES','此前新人/女儿解释已被本人揭伪装推翻。','翠雀亲自报号',[[36205,36257]],source_subjects=['CH001'])
state(42,'CH003','EV0110','MISUNDERSTANDS','MISUNDERSTANDS','仍认为小前辈原为女性后变男性；纠正话题被打断。','私语与未完成纠正',[[25653,25794]])
state(51,'CH001','EV0055','UNAWARE','PARTIAL','现在实际见到薄雪使用天音，得知她已经觉醒魔装。','接战时所见',[[11759,11833]])
state(110,'CH005','EV0097','MISUNDERSTANDS','DISBELIEVES','翠纠正杯量比较：低比例不等不同人的绝对余量，更不等当场濒死。','翠雀说明',[[21680,21876]],point=21876,source_subjects=['CH001'])
state(196,'CH031','EV0025','UNKNOWN','CONFIRMED','我决定冒险施术救白静萱，随后与她合作。','自己实际行动',[[4934,5067]])
state(197,'CH001','EV0068','UNKNOWN','MISUNDERSTANDS','听祖初判薄雪是少女向残兽偏移，按这个方向理解。','祖早期解释',[[14076,14393]],source_subjects=['CH008'])
state(197,'CH008','EV0068','UNKNOWN','MISUNDERSTANDS','先按少女偏向残兽解释白的情况。','自身初步判断',[[14076,14393]])
state(197,'CH008','EV0171','MISUNDERSTANDS','PARTIAL','检查后改判残兽底色偏向少女；确切成因我也不知道。','本人检查与改口',[[14859,14912]])
state(197,'CH002','EV0104','UNKNOWN','MISUNDERSTANDS','我听完修饰过的故事，理解成白与我一样是向残兽偏移。','白部分说明与翠协助隐瞒',[[23577,23608]],source_subjects=['CH004','CH001'])
state(115,'CH003','EV0104','UNKNOWN','PARTIAL','我先私问白，知道祭子/兽魔部分情况；父母身份仍隐。','白私下交代',[[23587,23601]],point=23593,source_subjects=['CH004'])
state(115,'CH004','EV0026','UNKNOWN','HEARD','兵触三用祭子称呼和病因说法描述我，我还没有完整机制知识。','敌人称呼与解释',[[5250,5330]],source_subjects=['CH039'])
state(115,'CH001','EV0171','HEARD','PARTIAL','造圣、圣子、兽子、祭子是相关词；祖也没有完整定义。','祖检查后的解释',[[14888,14908]],source_subjects=['CH008'])
state(115,'CH008','EV0171','UNKNOWN','PARTIAL','档案里出现造圣、圣子、兽子、祭子等术语，具体操作和释义不全。','间界传闻与资料台',[[14888,14908]])
state(153,'CH001','EV0131','SUSPECTS','PARTIAL','薄荷自承黑烬兽子并给名单；只确认已听这些供述，名单仍待核。','小转告与薄的供述',[[32751,33023]],source_subjects=['CH002','CH026'])
state(183,'CH026','EV0179','BELIEVES','PARTIAL','听妹妹表达真实牵挂，知道她不愿通过杀我存活。','姐妹直接交谈',[[37099,37161]],source_subjects=['CH027'])
state(183,'CH027','EV0179','UNKNOWN','PARTIAL','姐姐仍想让我活下去，先前的隔阂解释需修正。','姐妹直接交谈',[[37099,37161]],source_subjects=['CH026'])
state(97,'CH001','EV0086','HEARD','SUSPECTS','听去间界和过往线索，猜苏是否投奔爪痕；无名单佐证。','自己推理',[[19364,19410]],point=19410)

# Missing high-risk propositions found through character/relationship/full-audit navigation.
def added(prop,typ,truth,grade,scope,bound,evs,rows):
 r=extra(prop,typ,truth,grade,scope,bound,events=evs)
 for row in rows:add_state(r,*row)
 return r
new={}
new['redfeel']=added('红思与向翠雀表白并收到不能做恋人的答复','人际关系','TRUE','A','PRIVATE','明确表达与拒绝双方知道；不因后来照护抹去拒绝。',['EV0054'],[
 ('CH001','EV0054','UNKNOWN','CONFIRMED','红向我表白，我明确答不能做恋人。','当面表白与答复',[[11641,11758]]),
 ('CH005','EV0054','UNKNOWN','CONFIRMED','我表白后被明确告知不能成为恋人。','翠直接答复',[[11641,11758]])])
new['mardeath']=added('玛在演唱会重逢前已由木的消息知道翠雀复出踪迹','历史事件','TRUE','A','PRIVATE','区别玛先知踪迹与林台上认玛；她旧快照不能写从未获复出信息。',['EV0061'],[('CH007','EV0061','UNKNOWN','PARTIAL','木描述蓝发大帽巡查使，我纠正名字翠雀并获方亭线索。','木→玛',[[12697,12779]])])
new['redmemory']=added('红受控时试图思考禁区会遗忘、试图说出会失声','能力限制','TRUE','A','HIGHLY_SECRET','不等知情后只选择不说；反抗存在、认知可被压制。',['EV0052'],[('CH005','EV0052','PARTIAL','MEMORY_LOSS','清醒时试图想起禁区内容会被迫遗忘，想说时不能发声。','亲历受控',[[11498,11601]])])
new['whiteMemory']=added('白对湖畔虐杀过程的记忆失真并被翠协助修饰','私人秘密','TRUE','A','HIGHLY_SECRET','小夏只听王道战斗版本；不得自动给白完整客观战记。',['EV0104'],[('CH001','EV0104','UNKNOWN','CONFIRMED','白的记忆已经失真，我帮她整理成救人胜敌的故事并隐去父母。','本人观察与协助',[[23589,23601]]),('CH004','EV0104','CONFIRMED','MISUNDERSTANDS','那次是逆境中觉醒、打败坏人并救人的故事。','失真回忆和准备过的说辞',[[23589,23601]])])
new['rain']=added('吴姐妹在分离后曾共同受训半年并约定一起回家','家庭关系','TRUE','A','PRIVATE','小白听现场姐妹心意不等获这段完整回忆。',['EV0178'],[('CH026','EV0178','UNKNOWN','CONFIRMED','与小雨重聚后共同受训半年，曾约一起回家。','本人经历',[[36973,36985]]),('CH027','EV0178','UNKNOWN','CONFIRMED','和姐姐受训半年，曾约一起回家。','本人经历',[[36973,36985]])])
new['queenforget']=added('女王确已遗忘当年放兽决定的动机','动机认知','UNKNOWN','D','HIGHLY_SECRET','只有本人称遗忘，不能设置客观FORGOTTEN；黑猫仍未获得答案。',['EV0155'],[('CH009','EV0155','UNKNOWN','HEARD','女王说已经把那段理由忘了，没给我答案。','女王自述',[[37528,37541]])])
new['queenorder']=added('女王承认下过当年向内城放兽的命令','事件真相','TRUE','A','HIGHLY_SECRET','自认行为A，命令内容与最终责任链按D口供边界。',['EV0155'],[('CH009','EV0155','SUSPECTS','PARTIAL','女王承认下过放兽命令；为何这样做未得到解释。','当面对质',[[37528,37541]])])
new['toxin']=added('墨荷等早期逃亡者并非主动寻求兽魔而是受毒害后求生','历史事件','TRUE','A','HIGHLY_SECRET','读者迟到解释；墨的经历不自动让翠、塞米或全部爪痕后来成员知道。',['EV0180','EV0181'],[('CH009','EV0180','SUSPECTS','PARTIAL','被检出兽底色时曾怀疑自己藏塞米所致，狱中交流才知许多无此经历者也遭冤判。','自己遭遇→狱友交流',[[37579,37597]]),('CH009','EV0181','PARTIAL','CONFIRMED','逃亡后毒发，多人死亡，前紫钻以兽源解毒换追随。','亲历毒发及救援',[[37598,37609]])])
new['queenDead']=added('女王在食祭四人听到羊说法时已经死亡','生死状态','FALSE','A','SECRET','羊称死讯并非实证；场外女王仍在交谈战斗。',['EV0156'],[('CH002','EV0156','UNKNOWN','HEARD','羊称女王已死，场外实况没有亲证。','羊偷听说法',[[38523,38593]]),('CH004','EV0156','UNKNOWN','HEARD','羊说女王已死，我不能直接验证场外。','羊偷听说法',[[38523,38593]])])
new['dualfail']=added('兵触三未在死亡前把双祭子判断成功报告给蛾','事件真相','TRUE','A','HIGHLY_SECRET','判断D，传播中断A；不能因为敌方组织有关联就补报送成功。',['EV0031'],[('CH012','EV0031','UNKNOWN','UNKNOWN','没有证据收到兵触三所拟双祭子报告。','传信意图被死亡中断',[[6087,6319]])])
new['doubleguess']=added('林小璐与白静萱都是祭子','身份','UNKNOWN','D','HIGHLY_SECRET','兵触三据白魔认定为D；不得由共同颜色确证同源同类。',['EV0031'],[('CH039','EV0031','UNKNOWN','BELIEVES','看两人的魔力，我认为有两个祭子，准备向蛾报告。','战斗观察与本人判断',[[6087,6319]])])
new['garden']=added('妮妮与摩可在女王花园共同成长','人际关系','TRUE','A','PRIVATE','伙伴来源不是生物学兄妹；任职与传讯另条。',['EV0163'],[('CH010','EV0163','UNKNOWN','PARTIAL','妮妮谈共同成长与返国安排；不是任我代它履职。','妮妮说明',[[15428,15474]]),('CH011','EV0163','UNKNOWN','CONFIRMED','我与摩可共同成长，向它说明返国和职务安排。','本人经历及谈话',[[15428,15474]])])
new['mokoidentity']=added('摩可知道林昀与翠雀是同一人','人际关系','UNKNOWN','F','HIGHLY_SECRET','懂术语、同住、引导家庭误会均不能证明知男身；禁止按妖精物种全知。',['EV0067'],[('CH010','EV0067','UNKNOWN','UNKNOWN','未证获得林昀与翠雀同一人的秘密。','人物CH010及关系REL047/048边界核对',[[13593,14075]])])
new['anyaFamily']=added('安雅与林昀结婚后成为小璐的父母','家庭关系','TRUE','A','PRIVATE','母亲死亡后不能更新其知识；婴儿在场不授予家庭历史理解。',['EV0183','EV0184'],[('CH006','EV0184','UNKNOWN','CONFIRMED','与林昀组成家庭，小璐是我们的孩子。','生前家庭亲历',[[18031,18032],[18464,18472]]),('CH001','EV0184','UNKNOWN','CONFIRMED','与安雅组成家庭，小璐出生。','家庭亲历',[[18031,18032],[18464,18472]]),('CH007','EV0184','UNKNOWN','CONFIRMED','我在小璐出生时抱过她并见证命名。','本人在场，红不在',[[18464,18472]])])
new['childmother']=added('林昀童年认为未见面的母亲可能已经死亡','动机认知','TRUE','A','PRIVATE','确认幼年曾如此猜，不证明母亲死亡；女王相似外貌与宣称晚于此。',['EV0176'],[('CH001','EV0176','UNKNOWN','BELIEVES','父亲不谈母亲，我想她可能已经不在人世。','童年自行解释',[[37924,37941]])])
new['redcover']=added('年轻秘书是红思与的真实侄女','身份','FALSE','A','PRIVATE','25岁履历/侄女口径为掩护；不等真血亲、新独立角色。',['EV0086'],[('CH001','EV0086','UNKNOWN','DISBELIEVES','侄女秘书是红治疗后的掩护身份。','参与方案与复职',[[19232,19346]]),('CH005','EV0086','UNKNOWN','DISBELIEVES','我用侄女身份复职，不是真来了另一个侄女。','本人执行掩护',[[19232,19346]])])
new['gradeLeak']=added('公开SS评级意味着公众知道白玫全部王钥机制','能力机制','FALSE','A','PRIVATE','等级公开不能传输未公开检测、起源与限制。',['EV0133'],[])
new['singleSurvivor']=added('本次食祭最终只允许且只会剩一个生还者','能力机制','UNKNOWN','D','SECRET','箭/薄的规则宣告与最终效果分开；正文没写结界终局。',['EV0152','EV0156'],[('CH002','EV0152','UNKNOWN','HEARD','听到食祭互杀和只能一人活的规则说法，仍在设法合作。','现场对话',[[36748,36873]]),('CH004','EV0152','UNKNOWN','HEARD','听到食祭规则；没有看到它最终如何结束。','现场对话',[[36748,36873]])])
new['sulan']=added('苏胜紫已加入爪痕','组织成员','UNKNOWN','D','SECRET','林由去间界、研究兽体等猜测；查名单无果，不能变成事实。',['EV0086'],[('CH001','EV0086','UNKNOWN','SUSPECTS','猜苏可能投奔爪痕，但没有得到名单或行踪确认。','林自行推断',[[19364,19410]])])
new['garden']['states']=[s for s in new['garden']['states'] if s['subject']!='CH010']
add_state(new['garden'],'CH001','EV0163','SUSPECTS','PARTIAL','妮妮确认摩可来自花园，本来应成长为园丁；两者儿时为伙伴，没有人类式血亲。','妮妮→翠雀的厨房谈话',[[15428,15474]],source_subjects=['CH011'])
new['baijiMis']=added('玛格丽特从未期待白蓟而且只是偏心白玫','人际关系','FALSE','A','PRIVATE','白蓟把不责怪误听成不期待；后抱歉并未取消比试事实。',['EV0090'],[('CH023','EV0090','UNKNOWN','MISUNDERSTANDS','导师没批评我，是不是一直没期待我，只偏心白玫？','将安慰理解成否定',[[20333,20364]]),('CH023','EV0090','MISUNDERSTANDS','DISBELIEVES','听到分析、获得导师抱歉，堵塞的心结开始解开。','翠分析→玛拥抱道歉',[[20365,20391]])])
new['marBaiji']=added('白蓟对玛格丽特的依恋超出玛原先以为的公事师生关系','人际关系','TRUE','A','PRIVATE','实际哭泣表达、翠分析与玛领会后道歉，不直接规定浪漫关系。',['EV0090'],[('CH007','EV0090','UNKNOWN','MISUNDERSTANDS','我以为她懂事省心，关系主要是导师和学生，不至于有这样热烈的情感。','此前个人理解，随哭泣暴露偏差',[[20363,20386]]),('CH007','EV0090','MISUNDERSTANDS','PARTIAL','听翠分析并见她哭，我意识到自己忽略了她的依恋，真心抱歉。','学生表达、翠分析、自省',[[20365,20391]])])
new['xiaogift']=added('林小璐拥有祭子天赋','身份','UNKNOWN','D','HIGHLY_SECRET','薄荷断言、白近感微波与翠迟到怀疑分别记录，不能证明唯一天生兽子或完整起源。',['EV0131'],[('CH002','EV0131','UNKNOWN','HEARD','薄荷说我是祭子，白说气息模糊得像错觉；我未因此确认起源或接受兽魔。','薄荷断言与白回应',[[32860,32892]]),('CH004','EV0131','UNKNOWN','SUSPECTS','近距离感小璐，好像有兽魔，但微弱得像错觉。','亲自感知，明确模糊',[[32860,32866]]),('CH001','EV0131','UNKNOWN','SUSPECTS','女儿转薄荷话后，我回想旧敌的两个祭子说法，才真正怀疑小璐也可能有此天赋。','昨日转述加旧现场线索回接',[[33011,33022]])])
add_state(new['doubleguess'],'CH001','EV0031','UNKNOWN','EXPOSED','听逃离福利院的敌人自言自语“两个祭子”，当时不明词义，未想到女儿。','亲耳听见；后文L33013–18明确回接',[[33013,33018]],epoch='CURRENT',point=6319)
state(75,'CH001','EV0078','UNKNOWN','PARTIAL','白说父母、失去八音盒以及敌哼旧曲，我部分理解她为何相信敌人并失控；不证父母恶意。','白车内回述',[[17461,17514]],source_subjects=['CH004'])
state(149,'CH001','EV0157','UNAWARE','UNKNOWN','眼前认得墨荷并知道其爪痕立场；文本未明确展示我何时获得“黑猫”代号这条边。','实际对话仍称墨荷；旁白称黑猫不等口头报号',[[38595,38650]])
state(149,'CH009','EV0169','UNKNOWN','CONFIRMED','我以黑猫代号和残兽底色归来，与塞米离开国度。','本人更换代号的经历',[[22054,22083]],epoch='HISTORY')
state(199,'CH009','EV0157','HEARD','BELIEVES','首领早已告诉我女王死会使少女失去力量，并准备换底色对策；我在此向翠说明。','白狼此前告知，墨当前转述',[[38634,38645]],source_subjects=['CH014'])
state(199,'CH001','EV0157','PARTIAL','BELIEVES','我以女王死会使全体少女失去力量为护驾理由；惊讶墨说早已知道。','自身风险判断与墨回应',[[38634,38645]],source_subjects=['CH009'])
record_for(97)['states']=[s for s in record_for(97)['states'] if s['to_state']!='SUSPECTS']
# A statement's occurrence is not the truth of its embedded assertion.
record_for(198)['proposition']='林昀是女王单独创造、没有其他亲源的孩子'
for r in RECORDS:
 if r['id']=='K200':r['proposition']='两份兽之源曾按祖母绿所述分别分流到爪痕相关方'
 if r['id']=='K207':r['proposition']='墨荷的义肢由妖精为她制作'
 if r['id']=='K212':r['proposition']='林格曾任大妖精长并带走林昀本相'
 if r['id']=='K213':r['proposition']='林昀男孩身体由林格伪造'
# These are witnessed communication occurrences; embedded content keeps D/F.
record_for(154)['proposition']='薄荷向小璐和白说明兽子、祭子与食祭的部分定义'
record_for(154)['truth']='TRUE';record_for(154)['grade']='A';record_for(154)['canon_status']='CONFIRMED'
record_for(154)['boundary']='确认她作出解释；词义只限她提供的范围，食祭唯一生还结局另见未证命题。'
record_for(195)['proposition']='妮妮已获返国观察培训通知，摩可正式任职文件尚待送达'
record_for(195)['boundary']='厨房对话实际是妮妮→翠雀；准备当天动身，不等已到国度或摩可已收到任职文件。'
for s in record_for(195)['states']:s['known_content']='妮妮说国度昨晚通知返国培训，预计今天动身；之后应有人送摩可的正式任职文件和魔镜。';s['source']='妮妮向翠雀在厨房说明';s['source_subjects']=['CH011']
record_for(62)['proposition']='蛾向白揭出樱死及小璐母女关系，白受到冲击'
record_for(62)['type']='事件真相'
# Correct the acquisition of mother/daughter relation, rather than leave it only in the bundled speech.
state(161,'CH004','EV0055','UNKNOWN','PARTIAL','摩丝说樱就是小璐的妈妈。','敌人当面揭露',[[11870,11942]],source_subjects=['CH012'])
state(161,'CH002','EV0021','UNKNOWN','CONFIRMED','爸爸说明妈妈就是魔法少女樱。','林的照片与解释',[[4358,4422]],source_subjects=['CH001'])
for s in record_for(172)['states']:s['validity']='EVENT_LOCAL'
for t in [31,54,74,89,94,106,109,110,120,123,168,169,170,171,175,177,182,190,206]:
 for s in record_for(t)['states']:
  s['validity']='EVENT_LOCAL' if s['to_state'] in ['SUSPECTS','HEARD'] else s['validity']

# Refine several state semantics without erasing TEMP history.
for t in [125,145]:
 for s in record_for(t)['states']:
  if s['to_state']=='PARTIAL':s['to_state']='MISUNDERSTANDS';s['knowledge_grade']='D';s['correctness']='INCORRECT'
for t in [13,68,119,120,133,169,170,171,190]:
 for s in record_for(t)['states']:
  if s['to_state'] in ['PARTIAL','HEARD']:s['correctness']='UNKNOWN'
for s in record_for(198)['states']:
 if s['subject']=='CH001':s['to_state']='PARTIAL';s['interpretation']='经历了希望、认母、疑惧和质问；未接受其全部身体/父权定义。';s['knowledge_grade']='D'
# Correct first confirmation vs exposure and false before states.
for s in record_for(19)['states']:s['from_state']='SUSPECTS'
for s in record_for(196)['states']:
 if s['event']=='EV0170':s['known_content']='只记得躲藏等救援，又觉得与实际经历不符；具体救人片段有缺口。'
for s in record_for(125)['states']:
 if s['event']=='EV0149':s['from_state']='MISUNDERSTANDS'
for s in record_for(97)['states']:
 if s['to_state']=='SUSPECTS':s['related_inference']='去爪痕的猜测不是去间界这个消息本身的后退。';s['validity']='EVENT_LOCAL'

# Pairwise disclosure is stored independently; silence is not falsehood, and knowledge is not permission.
def disclose(t,source,targets,event,status,content,ranges):
 record_for(t)['disclosures'].append(dict(source=source,targets=targets,event=event,state=status,content=content,source_ranges=ranges,sharing='仅此有证据传播；禁止扩散到同组织/同住者。'))
disclose(20,'CH001',['CH003'],'EV0036','DISCLOSED','本人承认同一人，其他身世没有全讲。',[[7131,7291]])
disclose(20,'CH001',['CH002','CH004'],'EV0117','EVADED','双手机/离场视频和同生日解释维持分开印象。',[[27737,28129]])
disclose(20,'CH001',['CH005'],'EV0050','DISCLOSED','避人解除变身。',[[11281,11378]])
disclose(90,'CH007',['CH001'],'EV0081','DISCLOSED','战后解除变身互认。',[[17965,18030]])
disclose(36,'CH001',['CH004'],'EV0032','LIED_ABOUT','谎称樱只是两年前离开。',[[6480,6543]])
disclose(115,'CH004',['CH003','CH002'],'EV0104','PARTIALLY_DISCLOSED','只讲祭子、兽魔、修饰后的湖畔战；隐去父母。',[[23587,23601]])
disclose(14,'CH001',['CH002'],'EV0016','NOT_DISCLOSED','尊重夏暂不告诉小完整家史。',[[3183,3253]])
disclose(35,'CH036',['CH012','CH039'],'EV0028','NOT_DISCLOSED','麻雀没有分享矢车菊识别。',[[5834,5893]])
disclose(165,'CH002',['CH030','CH032'],'EV0137','LIED_ABOUT','编龙胆为矢车菊女儿。',[[34708,34967]])
disclose(180,'CH001',['CH030','CH032'],'EV0149','DISCLOSED','揭龙胆伪装，仅少女身份链。',[[36205,36257]])
disclose(158,'ORG002',[],'EV0133','PUBLIC','公示白玫SS；不公开全部机制。',[[33573,33844]])
disclose(147,'ORG002',[],'EV0130','PUBLIC','观礼与事后传播穿植物墙实绩；此前保密不能回填。',[[32418,32750]])
disclose(93,'CH007',['CH001'],'EV0083','DISCLOSED','回述猫眼通知与阻赴葬礼理由。',[[18678,18718]])
disclose(97,'CH018',['CH007'],'EV0187','DISCLOSED','最后通话仅说计划去间界寻找自我。',[[19364,19371]])
disclose(97,'CH007',['CH001','CH005'],'EV0086','PARTIALLY_DISCLOSED','转达十二年前最后联络；实际去向未知。',[[19364,19378]])
disclose(141,'CH001',['CH002','CH003','CH004'],'EV0121','DISCLOSED','说明蓝杖意向并要求保密。',[[29506,29568]])
disclose(198,'CH017',['CH001'],'EV0176','PARTIALLY_DISCLOSED','母亲/唯一亲源/身体来源等宣称；并非全真相实证。',[[37924,38228]])
disclose(198,'CH017',['CH009'],'EV0157','PARTIALLY_DISCLOSED','当场称翠雀为孩子。',[[38595,38618]])
disclose(51,'CH004',['CH001'],'EV0047','NOT_DISCLOSED','等老师回城再讲，尚未通报魔装。',[[9905,10008]])
disclose(59,'CH005',['CH011'],'EV0053','PARTIALLY_DISCLOSED','交手机，只说巡查使与小心；不讲林男身。',[[11602,11627]])

# Explicit source links for semantically related records, not inferred holder grants.
for t,ids in {17:[('power','PS005'),('org','ORG002')],24:[('power','PS029')],28:[('power','PS030')],51:[('power','PS030')],71:[('power','PS027')],73:[('org','ORG009')],80:[('power','PS032')],81:[('power','PS037')],82:[('power','PS027')],99:[('power','PS009')],100:[('power','PS024')],107:[('power','PS025')],112:[('power','PS020')],115:[('power','PS026'),('org','ORG011')],116:[('power','PS038')],120:[('power','PS031')],126:[('power','PS027')],128:[('power','PS018')],132:[('org','ORG009')],141:[('org','ORG002')],147:[('power','PS029')],149:[('org','ORG009')],154:[('power','PS026')],155:[('org','ORG011')],157:[('power','PS031')],158:[('power','PS031'),('org','ORG002')],160:[('power','PS031')],163:[('power','PS025')],164:[('power','PS031')],166:[('org','ORG003')],173:[('power','PS019')],176:[('power','PS034')],182:[('power','PS035')],189:[('power','PS023')],190:[('power','PS034')],197:[('power','PS023')],198:[('org','ORG001')],199:[('power','PS002')]}.items():
 for r in BYTEMP[t]:
  for kind,id in ids:r['power_refs' if kind=='power' else 'organization_refs'].append(id)
for r in RECORDS:
 events=set(r['events']);ranges=[];en=set()
 for z in r['states']+r['reader_revelations']+r['disclosures']:
  events.add(z['event']);ranges+=z['source_ranges'];en.update(EV[z['event']]['audit_navigation'])
 for ev in events:
  if not ranges:ranges+=EV[ev]['source_ranges']
  en.update(EV[ev]['audit_navigation'])
 r['events']=sorted(events);r['source_ranges']=sorted(set(tuple(x) for x in ranges));r['evidence_navigation']=sorted(en)
 people={s['subject'] for s in r['states'] if s['subject'].startswith('CH')}
 for d in r['disclosures']:
  if d['source'].startswith('CH'):people.add(d['source'])
  people.update(t for t in d['targets'] if t.startswith('CH'))
 # Named semantic entities are navigation only, never access grants.
 for n,cid in names.items():
  if len(n)>=2 and n in r['proposition']:people.add(cid)
 r['character_refs']=sorted(people)
 r['relationship_refs']=[x['id'] for x in REL if x['source'] in people and x['target'] in people]
 r['organization_refs']=sorted(set(r['organization_refs']));r['power_refs']=sorted(set(r['power_refs']))
 # Deduplicate exact repeated holder-state from multiple TEMP (not different acquisition steps).
 seen=set();kept=[]
 for s in r['states']:
  key=(s['subject'],s['event'],s['to_state'],s['known_content'],str(s['source_ranges']))
  if key not in seen:kept.append(s);seen.add(key)
 r['states']=kept
 for i,s in enumerate(r['states'],1):
  s['id']=f"{r['id']}-T{i:03}"
  if r['id']=='K187' and s['subject']=='CH007':
   s['acquisition']['history_anchor']='EV0009';s['acquisition']['description']='安雅死亡后、葬礼前获猫眼通知；EV0083只为当代回述来源。'
  if r['id']=='K228':s['validity']='HISTORICAL_BELIEF_ONLY';s['acquisition']['description']='幼年自行猜测，早于成为魔法少女；不能充当女王会面后的当前判断。'
  if r['id']=='K225' and s['subject']=='CH011':s['acquisition']['description']='EV0163向翠回述共同成长，此前的亲历起点未细化。'
  if s['event']=='EV0187':s['acquisition']['description']='十二年前最后通话；EV0086当代转述不得倒置。'
  # Explicit sub-scene order for correction within the same EV.
  if r is record_for(110) and s['event']=='EV0097':s['within_event_sequence']=2 if s['to_state']=='DISBELIEVES' else 1
  if r['id'] in ['K233','K234']:s['within_event_sequence']=2 if s['to_state'] in ['DISBELIEVES','PARTIAL'] else 1
 r['important_unknown']=r['truth'] in ['UNKNOWN','DISPUTED'] or any(s['to_state']=='UNKNOWN' for s in r['states'])
 r['has_error']=r['truth']=='FALSE' or any(s['to_state'] in ['MISUNDERSTANDS','MEMORY_LOSS'] for s in r['states'])
 r['secret']=r['scope'] in ['SECRET','HIGHLY_SECRET','PRIVATE','ORGANIZATION_INTERNAL']
 r['first_documented_event']=min(events,key=lambda e:min(a for a,b in EV[e]['source_ranges'])) if events else None
 r['first_event_note']='正文最早导航事件，不作为全局获取时间；获取时间以各T节点为准。'
 r['verification']='207TEMP逐项语义整理＋189Event语义对照＋70CH/172REL边界扫描＋高风险源段复核；不冒称本阶段重新全文逐字阅读。'

# Output Markdown and machine records.
def evlink(e):return f'[{e}](../01_master_timeline.md#{e.lower()})'
def elink(e):return f'[{e}](../../audit/01_evidence_index.md#{e.lower()})'
def slink(a,b):return f'[L{a}–{b}](../../source/下班，然后变成魔法少女_第1-282章.txt#L{a})'
def clink(c):
 fn=next((ROOT/'canon/characters').glob(c+'_*.md')).name;return f'[{c} {CH[c]["name"]}](../characters/{fn})'
def relink(r):return f'[{r}](../relationships/{r}.md)'
def ids(t):return '、'.join(f'[{r["id"]}]({r["id"]}.md)' for r in BYTEMP[t])
def clean(x):return str(x).replace('|','／').replace('\n',' ')
for r in RECORDS:
 lines=[f'# {r["id"]}｜{r["proposition"]}','', '## 客观层','',f'- 类型：{r["type"]}；客观真值：**{r["truth"]}**；Canon状态：{r["canon_status"]}；证据等级：{r["grade"]}。',f'- 有效范围：{r["truth_scope"]}',f'- 结论与限制：{r["boundary"]}',f'- 传播范围：{r["scope"]}。范围标签不等实际知情名单；无证据默认不授予。',f'- 事件：'+ '、'.join(evlink(e) for e in r['events']),f'- 原文窗口：'+'、'.join(slink(a,b) for a,b in r['source_ranges']),'- 审计证据导航：'+'、'.join(elink(e) for e in r['evidence_navigation']),'- 人物导航（不是授权）：'+'、'.join(clink(c) for c in r['character_refs']),'- 组织：'+('、'.join(r['organization_refs']) or '无已证独立组织主体持有本条的群体授权。'),'- 力量体系：'+('、'.join(r['power_refs']) or '无单独机制引用。'),'- 关系导航：'+('、'.join(relink(x) for x in r['relationship_refs']) or '本条不建立新关系边。'),'- TEMP：'+('、'.join(f'[{t}](TEMP_INDEX.md#{t.lower()})' for t in r['temp_ids']) or '本阶段从人物/关系/审计导航新增。'),'','## 主体认知与变化','', '以下是各自有证据的获取节点，不是所有主体在一个全局“当前”共享的答案。UNKNOWN不是明确不知；CONFIRMED仅限所列内容。不得把本页客观层或别人的节点直接注入NPC。','']
 for s in r['states']:
  lines += [f'### {s["id"]}｜{s["subject"]}｜{s["from_state"]} → {s["to_state"]}','',f'- 获取节点：{evlink(s["event"])}；{s["acquisition"]["epoch"]}；{s["acquisition"]["description"]}。当代子段边界：{s["acquisition"]["point"] or "不按揭示行号排序"}。',f'- 当时可知内容：{s["known_content"]}',f'- 来源/方式：{s["source"]}；已具名来源：'+('、'.join(s['source_subjects']) or '按来源文字，不补幕后传信人。'),f'- Observation（实际接触的线索）：{s["observation"]}',f'- Interpretation（如何理解）：{s["interpretation"]}',f'- 确信：{s["certainty"]}；内容正确性：{s["correctness"]}；认知证据层：{s["knowledge_grade"]}。',f'- 时效：{s["validity"]}；{s["first_acquisition_note"]}',f'- 披露/共享：{s["disclosure_state"]}是本节点未登记对外传播的默认；具体有据传播读下节，不能据默认推出永远没说。跨角色自动共享：禁止。','- 证据：'+'、'.join(slink(a,b) for a,b in s['source_ranges']),'']
 if not r['states']:lines+=['未从读者视角或客观层派生任何NPC知情授权。','']
 lines+=['## 披露与传播链','']
 for d in r['disclosures']:lines += [f'- {d["source"]} → {"、".join(d["targets"]) or "本次公告可接触对象，非所有人实知"}；{evlink(d["event"])}；**{d["state"]}**：{d["content"]} 证据 '+ '、'.join(slink(a,b) for a,b in d['source_ranges'])]
 if not r['disclosures']:lines+=['没有另外证实的转述边。认知来源只支持该获取，不能据此补一次向队伍的汇报。']
 lines+=['','## 读者揭示与调用边界','']
 for z in r['reader_revelations']:lines+=[f'- {evlink(z["event"])}：{z["note"]}']
 lines += ['- '+r['if_boundary'],'- 后续恢复先读[恢复规则](RESTORE_POLICY.md)，按主体、阶段和已发生传播读取T节点；客观真值不是NPC答案。', '- '+r['verification'],'']
 (OUT/(r['id']+'.md')).write_text('\n'.join(lines),encoding='utf-8')
dump(OUT/'records.json',RECORDS);dump(OUT/'groups.json',list(GROUPS.values()));dump(OUT/'_build2b4/migration_changes.json',CHANGES)
mapping=[]
lines=['# Knowledge TEMP → 正式K映射','','207条原件保持不变。一个TEMP拆出的多个K按具体内容取用；合并只合命题，不合主体与获取时点。空壳退役不是删除审计历史。','','|原ID与标题|正式去向|处理与理由|','|---|---|---|']
for t in TEMP:
 rs=BYTEMP[t];status='EMPTY_SHELL_RETIRED' if t==203 else 'MERGED' if t in MERGE else 'SPLIT' if len(rs)>1 else 'CONVERTED'
 reason=WHY.get(t,rs[0]['boundary']);mapping.append(dict(temp=TEMP[t]['id'],original_title=TEMP[t]['title'],original_rows=TEMP[t]['rows'],formal_ids=[r['id'] for r in rs],status=status,reason=reason))
 lines.append(f'|[{TEMP[t]["id"]}](TEMP_INDEX.md#{TEMP[t]["id"].lower()}) {TEMP[t]["title"]}|{ids(t)}|{status}：{reason}|')
(OUT/'TEMP_TO_K_MAP.md').write_text('\n'.join(lines)+'\n',encoding='utf-8');dump(OUT/'temp_to_k.json',mapping)
dump(OUT/'_build2b4/history_partial_order.json',dict(edges=[[f'EV{a:04}',f'EV{b:04}'] for a,b in historical_relations],note='只有已支持的先后边；无边不代表同日或可按编号补全。'))
print('curated',len(RECORDS),'K;',sum(len(r['states']) for r in RECORDS),'states; TEMP',len(mapping),'groups',len(GROUPS))
