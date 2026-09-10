"""Stage 2B-1 文档写入辅助；仅操作本轮四模块和本目录的检查导航。
四份 Markdown 是现行条目；manifest 只存定位与引用，不能代替正文。
"""
import json
from pathlib import Path
C=Path(__file__).resolve().parents[1]
FILES={'WR':'02_world_rules.md','PS':'03_power_system.md','ORG':'04_organizations.md','LOC':'05_locations.md'}
NAMES={'WR':'世界运行规则','PS':'力量体系','ORG':'组织','LOC':'地点'}
M=C/'_stage2b1/manifest.json'
def initialize():
    if M.exists():raise RuntimeError('已有本轮条目，禁止重置')
    for key,f in FILES.items():
        (C/f).write_text(f'# {NAMES[key]}｜Stage 2B-1\n\n先读[来源规则](00_source_policy.md)。本文件是事实条目，非RP设定。固定ID不随排序改变。A只覆盖明确标注的客观表现/已确认内容；D人物理论、C推断、F未知分别存放，不以条目存在或主级为A把整段升级。ACTIVE等表示组织/地点运行状态，CONFIRMED等表示证据状态，两者不同。原文定位采用一基行号。\n\n未解问题见[统一导航](UNRESOLVED.md)，易错边界见[防误读规则](INFERENCE_GUARDRAILS.md)，本轮检查见[校验报告](STAGE2B1_REVIEW.md)。未在本文件点名为知情者的角色，其知识状态不由本库存在而自动改变。\n\n',encoding='utf-8')
    M.write_text('[]',encoding='utf-8')
def link(i):
    if i.startswith('EV'):return f'[{i}](01_master_timeline.md#{i.lower()})'
    if i.startswith('K_TEMP_'):return f'[{i}](knowledge/TEMP_INDEX.md#{i.lower()})'
    k=next(k for k in FILES if i.startswith(k))
    return f'[{i}]({FILES[k]}#{i.lower()})'
def add(i,name,kind,scope,definition,confirmed,limits,stage,ranges,events,related,unknown,theory='未另立人物理论；无独立依据的解释不补写。',observed=None,conditions=None,resources=None,state='CONFIRMED',grade='A',extra=None):
    rows=json.loads(M.read_text('utf-8'));assert not any(x['id']==i for x in rows),i
    k=next(k for k in FILES if i.startswith(k));f=FILES[k]
    out=f'<a id="{i.lower()}"></a>\n## {i}｜{name}\n\n'
    out+=f'- 类型：{kind}\n- 状态：{state}\n- 证据等级：{grade}（分项等级以下列标记为准）\n- 来源层：NOVEL_TEXT；审计/时间轴只作导航。\n- 适用范围：{scope}\n- 定义：{definition}\n'
    if k=='PS':
        out+=f'- Layer 1／客观表现〔A〕：{observed}\n- Layer 2／已确认机制〔A〕：{confirmed}\n- 使用／成立条件：{conditions}\n- 资源／消耗：{resources}\n- Layer 3／人物理论〔D〕：{theory}\n- Layer 4／推断〔C〕：不将上述表现之外的猜测升级为机制；本项需要保留的未证解释见理论及未知栏。\n'
    else:out+=f'- 已确认内容〔A〕：{confirmed}\n- 人物说法／评价〔D/E〕：{theory}\n'
    out+=f'- 限制／不能推出的结论：{limits}\n- 阶段变化／例外：{stage}\n'
    for key,value in (extra or {}).items():out+=f'- {key}：{value}\n'
    out+='- 原著定位：'+'；'.join(f'[L{a}–L{b}](../source/下班，然后变成魔法少女_第1-282章.txt:{a})' for a,b in ranges)+'\n'
    out+='- 关联Event：'+('、'.join(link(x) for x in events) or '无强制绑定；此条为静态说明，不虚构事件。')+'\n'
    out+='- 关联条目：'+('、'.join(link(x) for x in related) or '暂无')+'\n'
    out+=f'- 争议／未知〔F，若有张力则DISPUTED〕：{unknown}\n\n'
    with (C/f).open('a',encoding='utf-8') as h:h.write(out)
    rows.append(dict(id=i,name=name,file=f,ranges=ranges,events=events,related=related,unknown=unknown,state=state,grade=grade))
    M.write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__':initialize()
