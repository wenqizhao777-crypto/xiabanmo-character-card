"""Read-only validation of delivery and protected inputs; writes only check_result.json."""
import collections
import datetime
import hashlib
import json
import re
from pathlib import Path

C = Path(__file__).resolve().parents[1]
ROOT = C.parent
HERE = Path(__file__).resolve().parent
FILES = {'WR':'02_world_rules.md','PS':'03_power_system.md','ORG':'04_organizations.md','LOC':'05_locations.md'}
COUNTS = {'WR':14,'PS':38,'ORG':19,'LOC':36}
errors = []
def check(value, message):
    if not value:
        errors.append(message)
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

rows = json.loads((HERE/'manifest.json').read_text('utf-8'))
ids = [x['id'] for x in rows]
check(len(ids)==len(set(ids))==107, 'manifest duplicate or unexpected total')
events = json.loads((C/'events/records.json').read_text('utf-8'))
evs = {x['id'] for x in events}
check(len(evs)==189, 'Stage 2A event count changed')
textmap = {f:(C/f).read_text('utf-8') for f in FILES.values()}
alltexts = '\n'.join(textmap.values())
source = ROOT/'source/下班，然后变成魔法少女_第1-282章.txt'
source_lines = source.read_text('utf-8-sig').splitlines()
check(len(source_lines)==38825 and sum(map(len,source_lines))==1641637, 'source line/character counts changed')
for prefix, f in FILES.items():
    expected = [f'{prefix}{i:03d}' for i in range(1,COUNTS[prefix]+1)]
    actual = re.findall(r'^## ('+prefix+r'\d{3})｜',textmap[f],re.M)
    check(actual==expected, f'{prefix} headings missing, duplicate or out of order')
    check([r['id'] for r in rows if r['file']==f]==expected, f'{prefix} manifest mismatch')
for r in rows:
    i = r['id']; s = textmap[r['file']]
    m = re.search(r'<a id="'+i.lower()+r'"></a>.*?(?=<a id=|\Z)',s,re.S)
    check(m is not None, f'{i} anchor missing')
    if not m:
        continue
    z=m.group()
    for field in ['类型','状态','证据等级','适用范围','定义','限制／不能推出的结论','阶段变化／例外','原著定位','关联Event','关联条目','争议／未知']:
        check('- '+field in z, f'{i} missing field {field}')
    if i.startswith('PS'):
        for field in ['Layer 1','Layer 2','Layer 3','Layer 4','使用／成立条件','资源／消耗']:
            check('- '+field in z, f'{i} missing power layer {field}')
        check('None' not in z, f'{i} unfilled generated field')
    if i.startswith('ORG'):
        for field in ['结构／已知职位','权限／资源','管辖／活动范围']:
            check('- '+field in z, f'{i} missing organization field {field}')
    if i.startswith('LOC'):
        for field in ['所属／管理者','相对位置','常驻／相关人物','公开／进入条件']:
            check('- '+field in z, f'{i} missing location field {field}')
    for a,b in r['ranges']:
        check(1<=a<=b<=len(source_lines), f'{i} invalid source range {a}-{b}')
        check(f'[L{a}–L{b}]' in z, f'{i} source range missing in Markdown')
    for e in r['events']:
        check(e in evs, f'{i} missing EV {e}')
    for x in r['related']:
        check(x in ids, f'{i} missing module target {x}')
    for x in re.findall(r'\b(?:WR\d{3}|PS\d{3}|ORG\d{3}|LOC\d{3})\b',z):
        check(x in ids, f'{i} unresolved inline module ID {x}')

groups = json.loads((HERE/'unresolved_index.json').read_text('utf-8'))
check([g['id'] for g in groups]==[f'WQ{n:03d}' for n in range(1,41)], 'unknown group ID mismatch')
check({x for g in groups for x in g['refs']}==set(ids), 'unknown navigation coverage mismatch')
newdocs = list(FILES.values())+['README.md','UNRESOLVED.md','INFERENCE_GUARDRAILS.md','STAGE2B1_REVIEW.md','_stage2b1/README.md']
links_checked=0
for f in newdocs:
    p=C/f;check(p.exists(),f'missing deliverable {f}')
    if not p.exists():continue
    txt=p.read_text('utf-8')
    for href in re.findall(r'\]\(([^)]+)\)',txt):
        href=href.strip('<>')
        if href.startswith(('http:','https:')):continue
        path,_,anchor=href.partition('#')
        path=re.sub(r':\d+$','',path)
        target=(p.parent/path).resolve() if path else p
        check(target.exists(),f'{f}: missing link target {href}')
        if target.exists() and anchor:
            check(f'<a id="{anchor}"></a>' in target.read_text('utf-8-sig'),f'{f}: missing anchor {href}')
        links_checked+=1

baseline=json.loads((HERE/'input_baseline.json').read_text('utf-8'))
allowed={str(Path('canon')/f) for f in list(FILES.values())+['README.md']}
changed=[];protected_checked=0
for rel,h in baseline.items():
    p=ROOT/rel
    if rel not in allowed:protected_checked+=1
    if not p.exists() or sha(p)!=h:
        changed.append(rel)
        check(rel in allowed,f'protected input changed or removed: {rel}')
check(set(changed)==allowed,'expected five allowed existing files not matched')
newallowed={'canon/UNRESOLVED.md','canon/INFERENCE_GUARDRAILS.md','canon/STAGE2B1_REVIEW.md'}
newfiles=[]
for p in ROOT.rglob('*'):
    if not p.is_file():continue
    rel=str(p.relative_to(ROOT))
    if rel not in baseline:
        posix=p.relative_to(ROOT).as_posix();newfiles.append(posix)
        check(posix in newallowed or posix.startswith('canon/_stage2b1/'),f'unauthorized new file: {posix}')
counts={k:len(re.findall(r'^## '+k+r'\d{3}｜',textmap[f],re.M)) for k,f in FILES.items()}
result={
    'checked_at_local':datetime.datetime.now().astimezone().isoformat(),
    'status':'PASS' if not errors else 'FAIL',
    'errors':errors,
    'counts':counts,'entries':len(ids),'unresolved_groups':len(groups),
    'links_checked':links_checked,'source_lines':len(source_lines),'source_chars_excluding_newlines':sum(map(len,source_lines)),
    'baseline_files':len(baseline),'protected_existing_files_checked':protected_checked,
    'changed_existing_files':changed,'new_files':newfiles,
    'source_sha256':sha(source),'card_sha256':sha(ROOT/'current/260808.png'),
    'stage2a_events':len(evs),
    'knowledge_temp_count':len(re.findall(r'^## K_TEMP_\d+｜',(C/'knowledge/TEMP_INDEX.md').read_text('utf-8'),re.M)),
    'relationship_temp_count':len(re.findall(r'^## REL_TEMP_\d+｜',(C/'relationships/TEMP_INDEX.md').read_text('utf-8'),re.M)),
    'module_sizes_chars':{f:len(t) for f,t in textmap.items()},
    'scope':'Structural/reference/input-hash checks; not an automatic proof of semantic truth or human acceptance.'
}
check(result['knowledge_temp_count']==207,'knowledge count changed')
check(result['relationship_temp_count']==49,'relationship count changed')
result['status']='PASS' if not errors else 'FAIL'
(HERE/'check_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','errors','counts','entries','unresolved_groups','links_checked','protected_existing_files_checked','knowledge_temp_count','relationship_temp_count']},ensure_ascii=False,indent=2))
raise SystemExit(0 if not errors else 1)
