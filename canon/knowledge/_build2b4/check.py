from pathlib import Path
import json,re,hashlib,collections,importlib.util,urllib.parse
ROOT=Path(__file__).resolve().parents[3];O=ROOT/'canon/knowledge';errors=[];tests=[]
def load(p):return json.loads((ROOT/p).read_text(encoding='utf-8-sig'))
def check(condition,name,detail=''):
 tests.append(dict(check=name,result='PASS' if condition else 'FAIL',detail=detail))
 if not condition:errors.append(name+': '+str(detail))
R=load('canon/knowledge/records.json');M=load('canon/knowledge/temp_to_k.json');E={e['id']:e for e in load('canon/events/records.json')};C={c['id'] for c in load('canon/characters/records.json')};RR={r['id'] for r in load('canon/relationships/records.json')};G={g['id'] for g in load('canon/knowledge/groups.json')};A={e['id'] for e in load('audit/evidence_records.json')};RK={r['id'] for r in R}
check([r['id'] for r in R]==[f'K{i:03}' for i in range(1,len(R)+1)],'K_ID_CONTIGUOUS_UNIQUE')
check({m['temp'] for m in M}=={f'K_TEMP_{i:03}' for i in range(1,208)} and len(M)==207,'ALL_207_TEMP_MAPPED')
check(all(m['formal_ids'] and set(m['formal_ids'])<=RK for m in M),'TEMP_TARGETS_EXIST')
check(len({r['proposition'] for r in R})==len(R),'NO_EXACT_DUPLICATE_PROPOSITIONS')
required={'subject','event','from_state','to_state','known_content','source','acquisition','certainty','correctness','observation','interpretation','disclosure_state','sharing','source_ranges'}
states={'UNAWARE','EXPOSED','HEARD','SUSPECTS','BELIEVES','PARTIAL','CONFIRMED','MISUNDERSTANDS','DISBELIEVES','FORGOTTEN','MEMORY_LOSS','UNKNOWN'}
issues=[]
for r in R:
 if r['truth'] not in {'TRUE','FALSE','PARTIALLY_TRUE','DISPUTED','UNKNOWN'}:issues.append(r['id']+' truth')
 if r['grade'] not in 'ABCDEF':issues.append(r['id']+' grade')
 if r['canon_status'] not in {'CONFIRMED','STRONGLY_SUPPORTED','INFERRED','DISPUTED','UNKNOWN'}:issues.append(r['id']+' canonstate')
 if not set(r['events'])<=E.keys() or not set(r['character_refs'])<=C or not set(r['relationship_refs'])<=RR or not set(r['evidence_navigation'])<=A:issues.append(r['id']+' foreignkey')
 for a,b in r['source_ranges']:
  if not 1<=a<=b<=38825:issues.append(r['id']+' range')
 for s in r['states']:
  if not required<=s.keys() or s['subject'] not in C|G or s['from_state'] not in states or s['to_state'] not in states:issues.append(r['id']+' state')
  if s['sharing']!='NO_AUTOMATIC_SHARING':issues.append(r['id']+' sharing')
  if s['acquisition']['epoch']=='CURRENT' and not isinstance(s['acquisition']['point'],int):issues.append(r['id']+' time')
  if s['subject']=='读者':issues.append(r['id']+' reader')
check(not issues,'STRUCTURE_ENUMS_FOREIGN_KEYS_RANGES',issues)
check(all(r['default_deny'] for r in R),'DEFAULT_DENY_DECLARED')
check(all(r['source_layer']=='NOVEL_TEXT' for r in R),'NO_USER_IF_OR_OLD_CARD_AUTHORITY')
check(len(list((O/'by_character').glob('CH*_knowledge.md')))==10,'TEN_TIER_A_PROFILES')
check(len(load('canon/knowledge/_build2b4/snapshot_checks.json'))==38,'ALL_38_SNAPSHOTS_CHECKED')
check(len(load('canon/knowledge/_build2b4/relationship_checks.json'))==172,'ALL_172_REL_BOUNDARIES_CHECKED')
sp=importlib.util.spec_from_file_location('query',O/'query_knowledge.py');q=importlib.util.module_from_spec(sp);sp.loader.exec_module(q)
tm={int(x['temp'][-3:]):x['formal_ids'][0] for x in M}
def result(ch,ev,t,before=False,deny=False):
 data=q.lookup(ch,ev,before);return [x for x in data['denied_or_unresolved' if deny else 'allowed'] if x['knowledge_id']==tm[t]]
def isstate(ch,ev,t,state,before=False):return any(x['state']==state for x in result(ch,ev,t,before))
check(isstate('CH003','EV0019',20,'SUSPECTS'),'SUMMER_ID_SUSPICION_NOT_CONFIRMATION')
check(isstate('CH003','EV0036',20,'CONFIRMED'),'SUMMER_ID_CONFIRMATION_AT_PHONE_TEST')
check(not result('CH003','EV0036',20,before=True) or not any(x['state']=='CONFIRMED' for x in result('CH003','EV0036',20,before=True)),'SUMMER_NO_EARLY_CONFIRMATION')
check(isstate('CH003','EV0110',42,'MISUNDERSTANDS'),'GENDER_DIRECTION_ERROR_RETAINED')
check(not result('CH002','EV0158',20) and not result('CH004','EV0158',20),'CHILDREN_ID_NOT_DISCLOSED_AT_EOF')
check(isstate('CH030','EV0137',165,'MISUNDERSTANDS') and isstate('CH030','EV0149',165,'DISBELIEVES'),'LONGDAN_DAUGHTER_LIE_CORRECTED')
check(not result('CH030','EV0149',20),'GIRL_ALIAS_CHAIN_NOT_MALE_ID')
check(isstate('CH007','EV0082',201,'CONFIRMED',before=True),'MAR_KNOWS_ANYA_DEATH_BEFORE_CONCERT')
check(not result('CH010','EV0163',195) and isstate('CH001','EV0163',195,'PARTIAL'),'NINI_KITCHEN_CORRECT_RECIPIENT')
check(not result('CH009','EV0155',198) and isstate('CH009','EV0157',198,'HEARD'),'QUEEN_PARENTAGE_NOT_EARLY_BLACKCAT')
check(not result('CH001','EV0128',149),'READER_BLACKCAT_REVEAL_NOT_CUI_GRANT')
check(not result('CH031','EV0063',27) and bool(result('CH031','EV0063',27,deny=True)),'TIAN_MEMORY_NOT_RESTORED_FROM_EVENT_DB')
check(isstate('CH005','EV0097',110,'DISBELIEVES'),'CUP_RATIO_ERROR_CORRECTED')
check(q.lookup('CH006','EV0158')['status']=='DECEASED_NO_NEW_KNOWLEDGE','ANYA_DEATH_BARRIER')
check(all(not result(c,'EV0158',191) for c in C),'UNWRITTEN_FINAL_RESULT_NOT_GRANTED')
check(not result('CH002','EV0132',158),'NO_PUBLIC_SS_BEFORE_PUBLICATION')
check(not result('CH002','EV0031',199),'CHILD_DOES_NOT_INHERIT_PARENT_HISTORICAL_SECRET')
check(bool(result('CH001','EV0001',199)),'LIN_RETAINS_OWN_HISTORICAL_MEETING_NOT_READER_LEAKAGE')
data=q.lookup('CH003','EV0158')
check(all('truth' not in x and 'proposition' not in x and 'reader_revelations' not in x for x in data['allowed']),'QUERY_PAYLOAD_EXCLUDES_OBJECTIVE_AND_READER_FIELDS')
links=0;bad=[]
files=list(O.rglob('*.md'))+[ROOT/'canon/README.md',ROOT/'canon/STAGE2B4_REVIEW.md']
for f in files:
 if not f.exists():bad.append(str(f));continue
 text=f.read_text(encoding='utf-8-sig')
 for target in re.findall(r'(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)',text):
  target=target.strip('<>');part=target.split('#',1)[0]
  if re.match(r'\w+://',part):continue
  links+=1;dest=(f.parent/urllib.parse.unquote(part)).resolve() if part else f
  if not dest.exists():bad.append(f.relative_to(ROOT).as_posix()+': '+target);continue
  if '#' in target:
   anchor=target.split('#',1)[1]
   if dest.suffix=='.txt' and re.fullmatch(r'L\d+',anchor):
    if not 1<=int(anchor[1:])<=38825:bad.append('badline '+target)
   elif re.fullmatch(r'(?:ev\d+|k_temp_\d+|e\d+)',anchor):
    dt=dest.read_text(encoding='utf-8-sig')
    if f'id="{anchor}"' not in dt and not re.search(r'^## '+anchor+r'(?:\s|$)',dt,re.M|re.I):bad.append('badanchor '+target)
check(not bad,'LOCAL_LINKS_AND_STABLE_ANCHORS',{'count':links,'bad':bad})
baseline=load('canon/knowledge/_build2b4/input_baseline.json');changes=[]
for rel,h in baseline.items():
 f=ROOT/rel
 if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest()!=h:changes.append(rel)
check(not changes,'PROTECTED_INPUT_HASHES_UNCHANGED',{'count':len(baseline),'changed':changes})
hashes={str(p.relative_to(ROOT)).replace('\\','/'):hashlib.sha256(p.read_bytes()).hexdigest() for dr in ['source','current'] for p in (ROOT/dr).rglob('*') if p.is_file()}
check(hashes.get('source/下班，然后变成魔法少女_第1-282章.txt')=='18819c3060f411fd8bbb24e859657d24a7628317aed18c9106831f73eb250fa2','SOURCE_KNOWN_HASH')
check(hashes.get('current/260808.png')=='3d6a1d85f42d0980aac7ce9ff62f0a94d51f3c5c3272c3eaedf39ef1b8bd517d','CARD_KNOWN_HASH')
output=dict(status='PASS' if not errors else 'FAIL',checks=tests,errors=errors,protected_files=len(baseline),links_checked=links,input_hashes=hashes,scope='结构、引用、哈希及代表性信息壁垒查询；语义判断见Review和原文回查，不声称自动证明全部自然语言。')
(O/'_build2b4/check_result.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(status=output['status'],errors=errors,checks=len(tests),protected=len(baseline),links=links),ensure_ascii=False))
raise SystemExit(bool(errors))
