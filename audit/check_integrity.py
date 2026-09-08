"""只读审计资料并将校验结果增量写入audit/report_validation.json。"""
from pathlib import Path
from collections import Counter
import json,re,hashlib,sys
ROOT=Path(r'C:\Users\Administrator\Desktop\下班魔角色卡重构'); A=ROOT/'audit'
def rd(n):return json.loads((A/n).read_text(encoding='utf-8'))
errors=[]
def check(test,msg):
 if not test:errors.append(msg)
for p in A.rglob('*.json'):
 try:json.loads(p.read_text(encoding='utf-8'))
 except Exception as e:errors.append(f'JSON {p.name}: {e}')
ev=rd('evidence_records.json');issues=rd('issue_records.json');ms=rd('missing_records.json');ledger=rd('reading_ledger.json');cp=rd('resume_checkpoint.json');v=rd('report_validation.json')
for prefix,data in [('E',ev),('C',[x for x in issues if x['id'].startswith('C')]),('M',ms)]:
 ids=[x['id'] for x in data];check(len(ids)==len(set(ids)),prefix+'重复')
 check(sorted(int(x[1:]) for x in ids)==list(range(1,len(ids)+1)),prefix+'断号')
known={x['id'] for x in ev+issues+ms}
for data in [ev,issues,ms]:
 for x in data:
  for k,val in x.items():
   if isinstance(val,str):
    for ref in re.findall(r'\b[ECM]\d{3}\b',val):check(ref in known,f'{x["id"]}/{k}悬空{ref}')
ed=(A/'01_evidence_index.md').read_text(encoding='utf-8');cd=(A/'02_full_audit_report.md').read_text(encoding='utf-8');md=(A/'03_missing_content.md').read_text(encoding='utf-8')
for data,doc,pat,fields in [(ev,ed,r'(?ms)^## {id}\n(.*?)(?=^## |\Z)',['finding','level']),(issues,cd,r'(?ms)^## \[{id}\].*?\n(.*?)(?=^## |\Z)',['current','problem','accurate','impact','action','level','severity']),(ms,md,r'(?ms)^### {id}｜.*?\n(.*?)(?=^#{{2,3}} |\Z)',['details','scope'])]:
 for x in data:
  blocks=re.findall(pat.format(id=x['id']),doc);check(len(blocks)==1,'MD块'+x['id'])
  if blocks:
   for f in fields:check(x[f] in blocks[0],f'MD字段{x["id"]}/{f}')
for ids,got,label in [([x['id'] for x in ev],re.findall(r'^## (E\d{3})$',ed,re.M),'E'),([x['id'] for x in issues],re.findall(r'^## \[([CSR]\d{3})\]',cd,re.M),'C/S/R'),([x['id'] for x in ms],re.findall(r'^### (M\d{3})｜',md,re.M),'M')]:check(sorted(ids)==sorted(got),'MD总标题'+label)
last={}
for h in rd('judgment_changes.json'):
 id=h['id']
 if id in last:check(last[id]==h['before'],'修订链断裂'+id)
 last[id]=h['after']
for id,x in last.items():check(x==next(i for i in issues if i['id']==id),'末修订不同于当前'+id)
source=(ROOT/'source/下班，然后变成魔法少女_第1-282章.txt').read_text(encoding='utf-8').splitlines();ranges=ledger['source_full_read_ranges'];union=set()
for lo,hi in ranges:
 check(lo>=1 and hi<=len(source) and lo<=hi,'覆盖越界');check(not union.intersection(range(lo,hi+1)),'范围重复计数');union.update(range(lo,hi+1))
chars=sum(len(source[i-1]) for i in union);cov=ledger['coverage'];pct=round(chars*100/sum(map(len,source)),2)
check(chars==cov['continuous_semantic_chars']==cp['cumulative_characters'],'字符不一致');check(pct==cov['continuous_semantic_char_percent']==cp['cumulative_character_coverage'],'百分比不一致')
check(cov['source_total_chars_without_newlines']==sum(map(len,source))==1641637,'字符分母');check(len(union)==cov['continuous_semantic_lines'],'行数不一致')
if pct==100:
 check(union==set(range(1,len(source)+1)),'100仍有缺口');check(cp['next_source_start_line'] is None and cp['source_unread_main_range']==[],'100残留续读断点');check(cp['last_read_line']==len(source),'最终行不符')
else:
 check(cp['last_read_line']+1==cp['next_source_start_line'],'断点关系');check(cp['last_read_line'] in union and cp['next_source_start_line'] not in union,'断点不在未读边界')
check(sorted(set(x['id'] for x in rd('card_entries.json'))-set(ledger['card_entries_read']))==cp['card_body_unread_ids'],'卡剩余列表')
check(len(ledger['card_entries_read'])==cov['worldbook_full_bodies_read'],'卡正文统计')
for x in ev:
 check(1<=x['start']<=x['end']<=len(source),'证据范围'+x['id'])
 if x.get('quote_line'):check(x['start']<=x['quote_line']<=x['end'],'引文越界'+x['id'])
 if x.get('session')==cp['session']:
  check(all(i in union for i in range(x['start'],x['end']+1)),'新证未读范围'+x['id'])
  q=source[x.get('quote_line',x['start'])-1].strip();block=re.search(r'(?ms)^## '+x['id']+r'\n(.*?)(?=^## |\Z)',ed)
  check(block is not None and '> '+q in block[1],'新证片段不匹配'+x['id'])
broken=[];anchors=[]
for p in A.glob('*.md'):
 for link in re.findall(r'\]\(([^\n]*?)\)',p.read_text(encoding='utf-8')):
  target=link.strip('<>');base,_,anchor=target.partition('#')
  if not base or re.match(r'https?://',base):continue
  base=re.sub(r':\d+$','',base);path=Path(base) if re.match(r'^[A-Za-z]:',base) else p.parent/base
  if not path.exists():broken.append(f'{p.name}:{link}')
  if path.name=='01_evidence_index.md' and anchor and anchor.upper() not in known:anchors.append(f'{p.name}:{anchor}')
check(not broken,'失效文件链接');check(not anchors,'失效证据锚点')
hashes={}
for rel,b in rd('input_manifest.json').items():
 p=ROOT/rel;now={'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()};hashes[rel]={'baseline':b,'current':now,'unchanged':now==b};check(now==b,'输入变动'+rel)
baseline=rd(f'session_{cp["session"]}_baseline.json');now={str(p.relative_to(ROOT)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in ROOT.rglob('*') if p.is_file()}
changed=[p for p in baseline if p in now and now[p]!=baseline[p]];deleted=[p for p in baseline if p not in now];added=[p for p in now if p not in baseline]
check(not deleted,'删除文件');check(all(p.replace('\\','/').startswith('audit/') for p in changed+added),'audit外写入')
check(v['issue_count']==len(issues) and v['evidence_count']==len(ev) and v['missing_count']==len(ms),'校验文件计数');check(v['severity']==dict(Counter(x['severity'] for x in issues)),'严重度统计');check(v['coverage']==cov,'校验覆盖不同')
for n in ['README.md','CONTINUE_STATE.md','00_card_structure.md','01_evidence_index.md','02_full_audit_report.md','03_missing_content.md','04_timeline_knowledge_risks.md','05_user_confirmation_required.md']:
 head=(A/n).read_text(encoding='utf-8')[:1400];check(('无续读断点' in head or '无下一原著断点' in head) if pct==100 else str(cp['next_source_start_line']) in head,'首页断点'+n);check(f'{pct:.2f}%' in head,'首页覆盖'+n)
result=dict(status='PASS' if not errors else 'FAIL',checks=['JSON与E/C/M连续编号','Markdown/JSON字段及标题','引用目标及证据锚点','判断修订链','新证主范围和字面片段','覆盖并集及唯一断点','输入SHA256和audit写入边界','现行统计与卡阅读列表'],errors=errors,input_hashes=hashes,changed_existing_files=sorted(set(changed+[r'audit\report_validation.json'])),added_files=added,deleted_files=deleted,coverage=cov,next_source_start_line=cp['next_source_start_line'])
v['input_hashes_unchanged']=all(x['unchanged'] for x in hashes.values());v['broken_local_links']=broken;v['bad_evidence_anchors']=anchors;v['consistency_errors']=errors;v.setdefault('session_'+cp['session'],{})['integrity_check']=result;v['session_'+cp['session']]['status']=result['status'];(A/'report_validation.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'errors':errors,'counts':{'E':len(ev),'C':sum(x['id'].startswith('C') for x in issues),'M':len(ms)},'coverage':cov,'next':cp['next_source_start_line'],'inputs_unchanged':v['input_hashes_unchanged'],'changed_existing':len(changed),'new_files':len(added)},ensure_ascii=False))
sys.exit(bool(errors))
