import json, hashlib, re
from pathlib import Path
from datetime import datetime
P=Path(__file__).resolve().parents[2];C=P/'canon'
R=json.loads((C/'events/records.json').read_text('utf-8'))
CH=json.loads((P/'audit/chapter_index.json').read_text('utf-8-sig'))
E={x['id']:x for x in json.loads((P/'audit/evidence_records.json').read_text('utf-8-sig'))}
M=json.loads((P/'audit/missing_records.json').read_text('utf-8-sig'))
S=(P/'source/下班，然后变成魔法少女_第1-282章.txt').read_text('utf-8').splitlines()
REG=json.loads((C/'_build/temp_registry.json').read_text('utf-8'))
errors=[]
ids={x['id'] for x in R}
if [x['id'] for x in R]!=[f'EV{i:04d}' for i in range(1,len(R)+1)]:errors.append('EV不连续或重复')
for x in R:
 for k in ['id','time_tier','time','source_ranges','evidence_grade','status','participants','witnesses','later_informed','meaningfully_unaware','before','occurrence','direct_result','long_term','changes','related_events','character_refs','knowledge_refs','note']:
  if k not in x:errors.append(x['id']+'缺字段'+k)
 if x['source_layer']!='NOVEL_TEXT':errors.append(x['id']+'混入非正文')
 if x['time_tier'] not in ['T1','T2','T3','T4']:errors.append(x['id']+'时间枚举')
 if x['evidence_grade'] not in list('ABCDEF'):errors.append(x['id']+'证据枚举')
 for a,b in x['source_ranges']:
  if not 1<=a<=b<=len(S):errors.append(x['id']+'源行越界')
 if not x['checked_anchors']:errors.append(x['id']+'无回查锚点')
 for a,b in x['checked_anchors']:
  if not any(u<=a<=b<=v for u,v in x['source_ranges']):errors.append(x['id']+'回查锚点越支持范围')
 for z in x['related_events']:
  if z not in ids:errors.append(x['id']+'无效关联'+z)
 for z in x['audit_navigation']:
  if z not in E:errors.append(x['id']+'无效E'+z)
 for k in x['knowledge']:
  if len(k)!=5:errors.append(x['id']+'知识边字段')
 for q in x['relationships']:
  if len(q)!=3:errors.append(x['id']+'关系边字段')

# 只读区全量路径与内容哈希，涵盖第一阶段审计历史。
baseline=json.loads((C/'_build/readonly_baseline.json').read_text('utf-8-sig'))
current={}
for folder in ['source','current','audit','final']:
 if (P/folder).exists():
  for f in (P/folder).rglob('*'):
   if f.is_file():current[str(f.relative_to(P))]=hashlib.sha256(f.read_bytes()).hexdigest()
protected_diff=[k for k in sorted(set(baseline)|set(current)) if baseline.get(k)!=current.get(k)]
if protected_diff:errors.append('只读区变化:'+','.join(protected_diff))

# 标题/证据职责覆盖用于遗漏复核，不把无EV的段落算未读。
outside={290:'首次复变失败及白日来电，补EV0188',439:'首次心之种连接，补EV0189',911:'林昀指导女儿的初衷，EV0003—5背景，无另一次状态转换',987:'赴电器街寻找夏凉，EV0005招募的过程',1048:'试探与保护，EV0005招募过程',1109:'夏凉坦白与接受招募，EV0005；不另割一份同事件',2186:'家属联络与机关双向保密条件，EV0006/13与后续知识数据库',3255:'摩可追踪精度与临时托教，EV0006/7的战术/日常补充',4077:'选礼及出战准备，EV0018/19前段'}
coverage=['# 原著结构覆盖与构建范围','','已处理全部提供文件的正文阶段，末尾为卷二282。第一阶段100%是既有审计阅读状态；本轮是全文状态提取与重要锚点回查，不冒称重新逐字读完1641637字符。表中“支持窗口”只证明可导航，不证明该章每条静态知识已入库。','','|原著标题|源行|事件支持窗口/处理职责|','|---|---|---|']
for c in CH:
 matches=[x['id'] for x in R if any(a<=c['end_line'] and b>=c['start_line'] for a,b in x['source_ranges'])]
 reason='、'.join(matches) if matches else outside.get(c['start_line'],'作者附言/发布或未采用草案：保留输入，排除世界事件')
 coverage.append(f'|{c["volume"]} {c["title"].lstrip("# ")}|L{c["start_line"]}–{c["end_line"]}|{reason}|')
(C/'events/SOURCE_COVERAGE.md').write_text('\n'.join(coverage),'utf-8')
disp=[]
for e in E.values():disp.append(dict(id=e['id'],events=[x['id'] for x in R if e['id'] in x['audit_navigation']],role='导航，原文才是事实依据'))
for m in M:
 es=set(re.findall(r'E\d{3}',m['evidence']));linked=[x['id'] for x in R if es.intersection(x['audit_navigation'])]
 disp.append(dict(id=m['id'],title=m['title'],events=linked,role='仅主题交叉检索；静态百科、详细机构与能力分类仍留后续'))
(C/'_build/navigation_crosscheck.json').write_text(json.dumps(disp,ensure_ascii=False,indent=2),'utf-8')

result=dict(time=datetime.now().isoformat(),event_count=len(R),knowledge_count=len(REG['knowledge']),relationship_count=len(REG['relationships']),source_lines=len(S),source_chars=sum(map(len,S)),protected_file_count=len(current),protected_differences=protected_diff,errors=errors,scope='结构/引用/哈希自动检查，不替代语义检查')
(C/'_build/check_result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),'utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
