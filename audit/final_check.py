"""第一阶段最终只读核验；仅输出audit内校验资料。"""
from pathlib import Path
from collections import Counter
import json,re,hashlib,sys,subprocess
ROOT=Path(r'C:\Users\Administrator\Desktop\下班魔角色卡重构');A=ROOT/'audit'
def rd(n):return json.loads((A/n).read_text('utf-8'))
def wr(n,x):(A/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
errors=[]
def ck(v,s):
 if not v:errors.append(s)
r=subprocess.run([sys.executable,'-X','utf8',str(A/'check_integrity.py')],capture_output=True,text=True,encoding='utf-8');ck(r.returncode==0,'基础检查失败: '+r.stdout[-1800:]+r.stderr[-500:])
S=(ROOT/'source/下班，然后变成魔法少女_第1-282章.txt').read_text('utf-8').splitlines();ledger=rd('reading_ledger.json');cp=rd('resume_checkpoint.json');ev=rd('evidence_records.json');issues=rd('issue_records.json');ms=rd('missing_records.json');chap=rd('chapter_index.json')
ranges=[('initial',[1,1285])]+[(x['session'],x['new_source_range']) for x in ledger['sessions']]+[('initial_tail',[36130,38825])]
parts=[];seen=set()
for name,(a,b) in ranges:
 chars=sum(len(x) for x in S[a-1:b]); ck(not seen.intersection(range(a,b+1)),'批次重计'+name);seen.update(range(a,b+1));parts.append({'session':name,'start':a,'end':b,'lines':b-a+1,'chars':chars})
for x in ledger['sessions']:
 a,b=x['new_source_range'];ck(x['new_lines']==b-a+1,'批次行数'+x['session'])
 if 'new_chars' in x:ck(x['new_chars']==sum(len(i) for i in S[a-1:b]),'批次字符'+x['session'])
ck(seen==set(range(1,len(S)+1)),'批次阅读区间存在空缺');ck(sum(x['chars'] for x in parts)==1641637,'批次并集字符')
ck(cp['last_completed_source_chapter']=='卷二 第二百八十二章 琥珀','末章名称');ck(chap[-1]['end_line']==len(S) and chap[-1]['title']=='# 第二百八十二章 琥珀','章节索引终点')
for j,x in enumerate(chap):
 ck(x['start_line']<=x['end_line'] and S[x['start_line']-1].strip()==x['title'].strip(),'标题定位'+str(j+1))
 if j:ck(chap[j-1]['end_line']+1==x['start_line'],'标题索引不连贯'+str(j+1))
known={x['id'] for x in ev+issues+ms}|{f'U{i:03}' for i in range(1,9)}|{'S018'}
for n in ['evidence_records.json','issue_records.json','missing_records.json']:
 for x in rd(n):
  body=json.dumps(x,ensure_ascii=False)
  for ref in re.findall(r'(?<![A-Za-z0-9])[ECSRMU]\d{3}(?!\d)',body):ck(ref in known,x['id']+'引用失效'+ref)
  for left,right in re.findall(r'([ECSRMU]\d{3})[—–-]([ECSRMU]\d{3})',body):
   if left[0]==right[0]:
    for i in range(int(left[1:]),int(right[1:])+1):ck(f'{left[0]}{i:03}' in known,x['id']+'范围引用失效')
ck(sorted(int(x['id'][1:]) for x in issues if x['id'].startswith('S'))==list(range(1,18))+[19],'S有效编号及撤销占位');ck(sorted(x['id'] for x in issues if x['id'].startswith('R'))==[f'R{i:03}' for i in range(1,6)],'R编号')
U=(A/'05_user_confirmation_required.md').read_text('utf-8');ck(re.findall(r'^## (U\d{3})',U,re.M)==[f'U{i:03}' for i in range(1,9)],'U编号');ck(U.count('**状态：** USER_CONFIRMATION_REQUIRED')==8,'U状态数')
for n in ['evidence_records.json','issue_records.json','missing_records.json']:
 data=rd(n);tokens=[json.dumps({k:v for k,v in x.items() if k not in ['id','session']},sort_keys=True,ensure_ascii=False) for x in data];ck(len(set(tokens))==len(tokens),'重复完整记录'+n)
chain_stats={}
for field,data in [('evidence_changes',ev),('missing_changes',ms)]:
 last={};changes=[]
 for x in rd('maintenance_changes.json')['record_changes']:
  if x['file']==('evidence_records.json' if field=='evidence_changes' else 'missing_records.json') and isinstance(x['before'],dict):changes.append(('maintenance_01',x))
 for f in sorted(A.glob('session_*_changes.json')):
  for x in rd(f.name)[field]:changes.append((f.name,x))
 for x in rd('final_changes.json')[field]:changes.append(('final',x))
 for file,x in changes:
  id=x.get('id',x.get('record'));ck(bool(x.get('reason')),'修订缺原因'+file+id)
  if id in last:ck(last[id]==x['before'],field+'前后链不接'+id+file)
  last[id]=x['after']
 for id,x in last.items():ck(x==next(i for i in data if i['id']==id),field+'当前值不接'+id)
 chain_stats[field]={'changes':len(changes),'records':len(last)}
chain_stats['issue_changes']={'changes':len(rd('judgment_changes.json')),'records':len({x['id'] for x in rd('judgment_changes.json')})}
ed=(A/'01_evidence_index.md').read_text('utf-8');quote_errors=[]
for x in ev:
 block=re.search(r'(?ms)^## '+x['id']+r'\n(.*?)(?=^## |\Z)',ed)[1]
 qs=re.findall(r'^> (.*)$',block,re.M);ck(bool(qs),'无定位片段'+x['id'])
 text='\n'.join(S[x['start']-1:x['end']])
 for q in qs:
  if q.strip() not in text:quote_errors.append(x['id'])
ck(not quote_errors,'证据片段非主范围原文:'+','.join(quote_errors))
for f in A.rglob('*.md'):
 for link in re.findall(r'\]\(([^\n]*?)\)',f.read_text('utf-8')):
  target=link.strip('<>');base,_,anchor=target.partition('#')
  if not base or re.match(r'https?://',base):continue
  lm=re.search(r':(\d+)$',base);line=int(lm[1]) if lm else None;base=re.sub(r':\d+$','',base)
  path=Path(base) if re.match(r'^[A-Za-z]:',base) else f.parent/base
  ck(path.exists(),'Markdown目标不存在 '+str(f.relative_to(A))+':'+link)
  if path.is_file() and line and path.suffix in ['.txt','.js','.md']:ck(1<=line<=len(path.read_text('utf-8').splitlines()),'Markdown行号越界 '+link)
  if path.name=='01_evidence_index.md' and anchor:ck(anchor.upper() in known,'证据锚点错误 '+link)
coverage=rd('technical/catalog_review_coverage.json');ck(coverage['counts']==dict(profiles=75,regions=36,factions=23,cg=50,aliasGroups=10),'手机目录计数');ck(not coverage['raw_unaccounted_content'],'raw未覆盖');ck(not any(x['route']=='UNACCOUNTED' for x in coverage['sections']),'目录漏读');ck(sum(coverage['route_counts'].values())==1044,'目录段数')
# 先前已保存的原始提取资料不允许借最终维护重写。
base=rd('final_baseline.json');now={str(f.relative_to(ROOT)):{'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in ROOT.rglob('*') if f.is_file()}
changed=[k for k in base if k in now and base[k]!=now[k]];added=[k for k in now if k not in base];deleted=[k for k in base if k not in now]
ck(not deleted,'最终阶段删除文件');ck(all(k.replace('\\','/').startswith('audit/') for k in changed+added),'最终阶段audit外写入')
immutable=[]
for k in base:
 q=k.replace('\\','/')
 if q.startswith('audit/card_text/') or q in ['audit/card_entries.json','audit/extracted_chara.json','audit/extracted_ccv3.json','audit/technical/phone_catalog.json'] or re.match(r'audit/technical/(script_\d+\.js|regex_\d+\.html)$',q):
  immutable.append(k);ck(base[k]==now.get(k),'提取副本被改 '+k)
hashes={}
for rel,b in rd('input_manifest.json').items():
 f=ROOT/rel;n={'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()};ck(n==b,'输入哈希变动'+rel);hashes[rel]={'baseline':b,'current':n,'unchanged':n==b}
for name in ['canon','final']:ck(not any(f.is_file() for f in (ROOT/name).rglob('*')),'禁止目录新增内容'+name)
wr('input_verification.json',{**hashes,'canon_files':[],'final_files':[]})
result={'status':'PASS' if not errors else 'FAIL','date':'2026-09-09','phase_one_completed':cp['status']=='COMPLETE','errors':errors,'counts':{'E':545,'C':138,'S_active':18,'S_withdrawn':['S018'],'R':5,'M':41,'U':8,'main':161},'coverage':ledger['coverage'],'source_parts':parts,'source_no_gap_no_double_count':seen==set(range(1,len(S)+1)) and sum(x['chars'] for x in parts)==1641637,'chapter_titles_verified':len(chap),'evidence_quotes_verified':len(ev)-len(set(quote_errors)),'revision_chain_checks':chain_stats,'all_current_record_refs_valid':not any('引用' in e for e in errors),'input_hashes':hashes,'immutable_extracted_files_verified':len(immutable),'audit_only_changes_verified':not deleted and all(k.replace('\\','/').startswith('audit/') for k in changed+added),'worldbook_bodies_read':143,'phone_catalog_sections_accounted':1044,'host_runtime_tested':False,'technical_scope':'前三脚本完整静态阅读、所有资料目录和可见UI文字、关键手机生成/过滤/快照/隔离路径；未全程序/CSS逐行审，未真实宿主运行。','health_73_55':rd('report_validation.json').get('health_73_55',{}).get('status'),'health_90_96':cp.get('health_90_percent',{}).get('status'),'active_next_source_line':None}
wr('final_integrity.json',result)
v=rd('report_validation.json');v['final_integrity']=result;wr('report_validation.json',v)
print(json.dumps({k:result[k] for k in ['status','errors','counts','source_no_gap_no_double_count','chapter_titles_verified','evidence_quotes_verified','revision_chain_checks','immutable_extracted_files_verified']},ensure_ascii=False))
sys.exit(bool(errors))
