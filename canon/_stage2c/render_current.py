"""Render current Canon facts only. Never rerun historical curation builders."""
from pathlib import Path
import json,re,ast,importlib.util,textwrap,zipfile
P=Path(__file__).resolve().parents[2];C=P/'canon';B=C/'_stage2c'
def load(p):return json.loads((C/p).read_text(encoding='utf-8-sig'))
def put(p,s):(C/p).write_text(s.rstrip()+'\n',encoding='utf-8')
EV=load('events/records.json');CH=load('characters/records.json');REL=load('relationships/records.json');K=load('knowledge/records.json')
cs={x['id']:x for x in CH};cp={x['id']:f'{x["id"]}_{x["name"]}.md' for x in CH}
# Existing render functions imported without main, so current JSON is never replaced by stale dossiers.
sp=importlib.util.spec_from_file_location('char_render',C/'characters/_build2b2/build.py');m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);m.PEOPLE=cs
for d in CH:
 s=m.render(d).replace('以上仅供后续有向关系建库','以上为历史人物关系摘要；正式有向关系已建库').replace('现有事件未登记专门 TEMP；后续按本档案原著定位补建。','现有事件未登记专门 TEMP；正式K导航另列。')
 s+='\n## Stage 2C 正式导航\n\n关联关系（逐阶段读取）：'+('、'.join(f'[{v}](../relationships/{v}.md)' for v in d['formal_relationship_refs']) or '无已建正式边')+'。\n\n本主体专属认知节点索引（不等同时知情）：'+('、'.join(f'[{v}](../knowledge/{v}.md)' for v in d['formal_knowledge_refs']) or '无专属获取节点，未知不补')+'。\n'
 put('characters/'+cp[d['id']],s)
# Reuse only the rendering statements of old relation builder; exclude fact curation.
fn=C/'relationships/_build2b3/build.py';tree=ast.parse(fn.read_text(encoding='utf-8-sig'));defs=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ['put','ch','event','evidence','src','rel','safe']]
loop=next(n for n in tree.body if isinstance(n,ast.For) and n.lineno==34);body=[n for n in loop.body if n.lineno>=83];safe_loop=ast.For(target=loop.target,iter=loop.iter,body=body,orelse=[]);ast.fix_missing_locations(safe_loop)
ns=dict(cs=cs,cp=cp,rows=REL,D=C/'relationships');exec(compile(ast.Module(body=defs+[safe_loop],type_ignores=[]),str(fn),'exec'),ns)
for r in REL:
 f=C/'relationships'/f'{r["id"]}.md';s=f.read_text(encoding='utf-8')
 s=s.replace('留Stage 2B-4按本档源行补链','正式库无证则不授予')
 s+='\n\n## Stage 2C 正式认知导航\n\n'+('、'.join(f'[{v}](../knowledge/{v}.md)' for v in r['formal_knowledge_refs']) or '无正式获取节点；关系不产生默认知情')+'。仅索引，不给双方批量授权。\n'
 f.write_text(s,encoding='utf-8')
# Render current knowledge objects only.
fn=C/'knowledge/_build2b4/build.py';tree=ast.parse(fn.read_text(encoding='utf-8-sig'));nodes=[n for n in tree.body if 318<=n.lineno<=337 and isinstance(n,(ast.FunctionDef,ast.For))]
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(fn),'exec'),dict(ROOT=P,OUT=C/'knowledge',CH=cs,RECORDS=K))
# Retain timeline group order and all original details, replace rows from current records, append stable new IDs.
f=C/'01_master_timeline.md';old=zipfile.ZipFile(B/'canon_before.zip').read('canon/01_master_timeline.md').decode('utf-8-sig').replace('\r','');header=old.split('---\n\n# 事件详情')[0]
header=header.replace('共 **189 个事件**；知识命题 **207**，有向关系 **49**。','共 **192 个事件**；正式知识命题 **235**、有向关系 **172**。历史导入为207个知识TEMP、49个关系TEMP。')
header=header.replace('[最终检查](BUILD_CHECK.md)','[Stage 2C最终检查](STAGE2C_FINAL_REVIEW.md)')
def esc(t):return str(t).replace('|','／').replace('\n',' ')
for x in EV[:189]:
 row=f'|[{x["id"]} {esc(x["title"])}](#{x["id"].lower()})|{x["time_tier"]} · {esc(x["time"])}|{esc(x["changes"])}|'
 header=re.sub(r'^\|\['+x['id']+r' .*$',lambda _:row,header,flags=re.M)
header+='\n## Stage 2C补入的独立历史节点\n\n编号追加不代表晚于当代；各自相对时序见限定，未给日期不补。\n\n|事件|时间等级与时间|核心变化|\n|---|---|---|\n'
for x in EV[189:]:header+=f'|[{x["id"]} {esc(x["title"])}](#{x["id"].lower()})|{x["time_tier"]} · {esc(x["time"])}|{esc(x["changes"])}|\n'
fn=C/'_build/render.py';tree=ast.parse(fn.read_text(encoding='utf-8-sig'));loop=next(n for n in tree.body if isinstance(n,ast.For) and isinstance(n.target,ast.Name) and n.target.id=='x' and n.lineno>105)
ns=dict(R=EV,out=[],esc=esc,src=lambda a,b:f'[L{a}–{b}](../source/下班，然后变成魔法少女_第1-282章.txt:{a})',ev=lambda z:f'[{z}](01_master_timeline.md#{z.lower()})');exec(compile(ast.Module(body=[loop],type_ignores=[]),str(fn),'exec'),ns)
details='\n'.join(ns['out'])
for x in EV:
 marker=f'## {x["id"]}｜{x["title"]}\n';nav='\n- **正式关系导航**：'+('、'.join(f'[{v}](relationships/{v}.md)' for v in x['formal_relationship_refs']) or '无登记')+'；**正式认知导航**：'+('、'.join(f'[{v}](knowledge/{v}.md)' for v in x['formal_knowledge_refs']) or '无登记')+'。导航不等在场或知情授权。\n- **查询时间层**：'+x['knowledge_epoch']+'；取得时间仍按K节点，不按EV编号。\n'
 details=details.replace(marker,marker+nav)
put('01_master_timeline.md',header+'\n---\n\n# 事件详情\n\n'+details)
# Refresh knowledge navigation through its rendering-only script; redirect generated diagnostics out of historical phase dir.
fn=C/'knowledge/_build2b4/navigation.py';s=fn.read_text(encoding='utf-8-sig')
s=s.replace("(OUT/'_build2b4/stats.json')","(ROOT/'canon/_stage2c/knowledge_stats.json')").replace("(OUT/'_build2b4/snapshot_checks.json')","(ROOT/'canon/_stage2c/snapshot_checks38.json')").replace("(OUT/'_build2b4/relationship_checks.json')","(ROOT/'canon/_stage2c/relationship_checks172.json')")
s=s.replace('不更改原TEMP、Timeline、Character或Relationship。','TEMP原始记录保留；Stage 2C已核证整合上游，见总Review。').replace('上游有误只在Review登记。','上游修订已通过Stage 2C逐项核证，旧Review保留历史。')
s=s.replace('原件“演唱会前不能默认知安雅死亡”不再作为本库有效结论','旧件曾写的“演唱会前不能默认知安雅死亡”已由CR014修正').replace('保留上游原文；本表为本阶段检查及调用修正导航，不静默改写人物档案。修正建议详见Review。','本表已从Stage 2C修订后的上游重算；旧建议的核证及修订链见STAGE2C_REVIEW_QUEUE。')
s=s.replace("'_build2b4/stats.json','_build2b4/check_result.json'","'../_stage2c/knowledge_stats.json','../_stage2c/check_result.json'")
exec(compile(s,str(fn),'exec'),{'__file__':str(fn)})
# Index paths/tiers preserved; update current changed row metadata and formally label TEMP import.
f=C/'characters/README.md';s=zipfile.ZipFile(B/'canon_before.zip').read('canon/characters/README.md').decode('utf-8-sig')
for d in CH:
 lines=s.splitlines()
 for i,l in enumerate(lines):
  if l.startswith('|') and d['id'] in l and '|' in l and ('582' in l or '629' in l) and d['id'] in ['CH052','CH054','CH055','CH056']:
   lines[i]=l.replace('582','604') if d['id'] in ['CH052','CH054'] else l.replace('629','582')
 s='\n'.join(lines)
s+='\n\n## Stage 2C当前入口\n\n70个稳定人物ID不变；人物页面与records.json已同步。正式关系及认知导航已逐人列入，TEMP区仅保留原始导入称呼；P_TEMP_118的木芙蓉为旧错字，正确实体是CH052木棉，不新增同名实体。复核见[Stage2C](../STAGE2C_FINAL_REVIEW.md)。\n'
f.write_text(s,encoding='utf-8')
# Other existing indexes carry current annotation; detailed source/history content retained.
for path in ['events/README.md','events/STATE_CHAINS.md','relationships/README.md','relationships/RELATIONSHIP_MATRIX.md','relationships/CHARACTER_RELATION_SCAN.md','relationships/TEMP_TO_REL_MAP.md','knowledge/TEMP_TO_K_MAP.md','knowledge/RESTORE_POLICY.md']:
 f=C/path;s=zipfile.ZipFile(B/'canon_before.zip').read('canon/'+path).decode('utf-8-sig');prefix='../'
 s=s.replace('582个阶段','583个阶段').replace('582 个阶段','583 个阶段').replace('582阶段','583阶段')
 note='\n\n## Stage 2C有效状态\n\n当前为192 EV、70 CH、172 REL（583阶段）、235 K（365获取节点）。历史TEMP原文及阶段Review保存原口径，当前调用以records.json、正式档案及[Stage 2C修订队列](../STAGE2C_REVIEW_QUEUE.md)为准。早期构建脚本及其输入仅供追溯，不可直接重跑覆盖当前库。CR021将K017父早知与渠道解释分为EV0019/EV0020；CR008/009/018将错挂的历史与当代关系、知情分开。\n'
 if path=='events/README.md':s=s.replace('由_build/render.py同步生成','由Stage 2C受控渲染同步；旧_build/render.py仅留作历史')
 f.write_text(s+note,encoding='utf-8')
print('Rendered current records; historical curation not executed.')

# Logged navigation corrections applied after regenerating the original-format indexes.
for c in load("_stage2c/changes.json"):
    if int(c["id"][2:]) >= 1006 and c["module"]=="Document" and c["record"] in ["events/STATE_CHAINS.md","relationships/README.md","knowledge/README.md"]:
        f=C/c["record"];s=f.read_text(encoding="utf-8-sig")
        if c["before"] in s: f.write_text(s.replace(c["before"],c["after"]),encoding="utf-8")
