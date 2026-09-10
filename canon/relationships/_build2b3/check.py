from pathlib import Path
import json,re,hashlib,datetime,urllib.parse
P=Path(__file__).resolve().parents[3];D=P/'canon/relationships'
read=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
rows=read(D/'records.json');mapping=read(D/'temp_to_rel.json');base=read(D/'_build2b3/input_baseline.json')['files'];cs=read(P/'canon/characters/records.json');es=read(P/'canon/events/records.json');ee=read(P/'audit/evidence_records.json')
chars={x['id'] for x in cs};events={x['id'] for x in es};evidence={x['id'] for x in ee};ids={x['id'] for x in rows};issues=[]
def test(ok,msg):
    if not ok:issues.append(msg)
def allowed(path):return path.startswith('canon/relationships/') or path in ['canon/README.md','canon/STAGE2B3_REVIEW.md','canon/UNRESOLVED.md']
test([x['id'] for x in rows]==[f'REL{i:03}' for i in range(1,len(rows)+1)],'ID不连续/重复')
pair={(r['source'],r['target']):r for r in rows}
test(len(pair)==len(rows),'重复有向人物对')
test([m['temp'] for m in mapping]==[f'REL_TEMP_{i:03}' for i in range(1,50)],'TEMP不全或重复')
for m in mapping:
    test(bool(m['formal']) and set(m['formal'])<=ids,m['temp']+'映射失效')
    test(set(m['formal'])=={r['id'] for r in rows if m['temp'] in r['temp_ids']},m['temp']+'双向映射不一致')
for r in rows:
    rid=r['id'];test(r['source'] in chars and r['target'] in chars and r['source']!=r['target'],rid+'CH方向失效')
    test((D/f'{rid}.md').exists(),rid+'缺档')
    reverse=pair.get((r['target'],r['source']))
    test(r['reverse_id']==(reverse['id'] if reverse else None),rid+'反向引用错误')
    if reverse:test(r['stages']!=reverse['stages'],rid+'两向机械复制')
    test(len(r['dimensions'])==10,rid+'缺维度')
    test(bool(r['stages']),rid+'无阶段')
    for s in r['stages']:
        test(s['event'] in events,rid+'失效Event')
        test(bool(s['story_phase']) and bool(s['claim_metadata']),rid+'阶段或等级缺失')
        for a,b in s['source_ranges']:test(1<=a<=b<=38825,rid+'源行越界')
        test(set(s['evidence_navigation'])<=evidence,rid+'失效E引用')
    for a,b in r['anchors']:test(1<=a<=b<=38825,rid+'补充源行越界')
    if r['family_layers']:test(len(r['family_layers'])==7,rid+'家庭七层缺项')
    test(r['source_layer']=='NOVEL_TEXT',rid+'混入IF层')
    test('knowledge_navigation' in r and not any(k.startswith('K0') for k in r['knowledge_navigation']),rid+'越界正式知识')
    test(not any(isinstance(v,(int,float)) for v in r['dimensions'].values()),rid+'关系数字化')
test(len(read(D/'_build2b3/character_scan.json'))==70,'人物扫描不足70')
test(hashlib.sha256((D/'TEMP_INDEX.md').read_bytes()).hexdigest()==base['canon/relationships/TEMP_INDEX.md'],'原TEMP修改')
unresolved=(P/'canon/UNRESOLVED.md').read_bytes()
old_unresolved=unresolved.split(b'\n\n<!-- STAGE2B3_APPEND_BEGIN -->')[0]
test(hashlib.sha256(old_unresolved).hexdigest()==base['canon/UNRESOLVED.md'],'UNRESOLVED既有前缀被改写')
protected=0;changed=[];new_illegal=[]
for rel,h in base.items():
    if allowed(rel):continue
    protected+=1;f=P/rel
    if not f.exists() or hashlib.sha256(f.read_bytes()).hexdigest()!=h:changed.append(rel)
for f in P.rglob('*'):
    if f.is_file():
        rel=f.relative_to(P).as_posix()
        if rel not in base and not allowed(rel):new_illegal.append(rel)
test(not changed,'受保护文件变更:'+str(changed));test(not new_illegal,'越界新增:'+str(new_illegal))
# 所有新文档链接及三个获准主文档中的本地路径/行号/锚；源文件不写入。
files=list(D.glob('*.md'))+list((D/'_build2b3').glob('*.md'))+[P/'canon/README.md',P/'canon/STAGE2B3_REVIEW.md',P/'canon/UNRESOLVED.md']
cache={};line_counts={};links=0
def anchors(p):
    if p not in cache:
        t=p.read_text(encoding='utf-8-sig');ss=set(re.findall(r'<a\s+id="([^"]+)"',t))
        for h in re.findall(r'^#+\s+(.*)$',t,re.M):
            h=re.sub(r'[^\w\s\-]','',h.lower(),flags=re.UNICODE).strip().replace(' ','-');ss.add(h)
        cache[p]=ss
    return cache[p]
for f in files:
    test(f.exists(),'缺文件:'+str(f))
    if not f.exists():continue
    text=f.read_text(encoding='utf-8-sig')
    for dest in re.findall(r'(?<!!)\[[^\]]+\]\(([^\n]+?)\)',text):
        dest=urllib.parse.unquote(dest.strip('<>'))
        if re.match(r'^[a-z]+://',dest):continue
        links+=1
        path,_,anchor=dest.partition('#');line=None
        m=re.search(r':(\d+)$',path)
        if m:line=int(m[1]);path=path[:m.start()]
        target=(f.parent/path).resolve() if path else f.resolve()
        test(target.exists(),f.name+'失效路径:'+dest)
        if target.exists() and anchor:test(anchor in anchors(target),f.name+'失效锚:'+dest)
        if target.exists() and line:
            if target not in line_counts:line_counts[target]=len(target.read_text(encoding='utf-8-sig').splitlines())
            test(1<=line<=line_counts[target],f.name+'失效行:'+dest)
# 关键状态的结构回归门，语义正确性另见人工复核。
rr={r['id']:r for r in rows}
test('拒绝' in rr['REL014']['end'],'红被拒旧状态缺失')
test('EV0176' in [s['event'] for s in rr['REL028']['stages']],'女王谈话未纠Event')
test('EV0072' in [s['event'] for s in rr['REL141']['stages']],'江媛交友早期未补')
test(any('法理' in v['text'] for v in rr['REL033']['family_layers'].values()),'吴家法律自述漏记')
test('C' in rr['REL123']['dimensions']['责任']['grades'],'师承推断错误升级')
result={'checked_at':datetime.datetime.now().astimezone().isoformat(),'status':'PASS' if not issues else 'FAIL','formal_records':len(rows),'mapped_temp_inputs':len(mapping),'character_scan':70,'local_links_checked':links,'protected_files_unchanged':protected-len(changed),'protected_files_total':protected,'protected_changes':changed,'unauthorized_new_files':new_illegal,'original_temp_unchanged':hashlib.sha256((D/'TEMP_INDEX.md').read_bytes()).hexdigest()==base['canon/relationships/TEMP_INDEX.md'],'source_current_hashes':{r:h for r,h in base.items() if r.startswith(('source/','current/'))},'errors':issues,'scope_note':'自动检查验证结构、引用与文件保护；逐方向事实和分期由semantic_review及curation人工复核，不宣称脚本理解正文。'}
(D/'_build2b3/check_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False));raise SystemExit(bool(issues))
