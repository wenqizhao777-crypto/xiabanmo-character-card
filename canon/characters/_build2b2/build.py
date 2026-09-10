"""Stage 2B-2 文档渲染器。事实正文来自人工编写的 dossiers.json，导航来自只读既有记录。"""
import json, pathlib, re, hashlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[3]
OUT = ROOT / 'canon/characters'
def read(f): return json.loads((ROOT/f).read_text(encoding='utf-8-sig'))
EV = {x['id']: x for x in read('canon/events/records.json')}
E = {x['id']: x for x in read('audit/evidence_records.json')}
SRC = '../../source/下班，然后变成魔法少女_第1-282章.txt'
def link(t):
    paths={'EV':'../01_master_timeline.md','PS':'../03_power_system.md','WR':'../02_world_rules.md','ORG':'../04_organizations.md','LOC':'../05_locations.md','K_TEMP_':'../knowledge/TEMP_INDEX.md','REL_TEMP_':'../relationships/TEMP_INDEX.md'}
    for pre in ['K_TEMP_','REL_TEMP_','ORG','LOC','EV','PS','WR']:
        if t.startswith(pre):return f'[{t}]({paths[pre]}#{t.lower()})'
    if t.startswith('CH') and t in PEOPLE:return f'[{t}](CH{t[2:]}_{PEOPLE[t]["name"]}.md)'
    if t in E:return f'[{t}](../../audit/01_evidence_index.md#{t.lower()})'
    return t
def refs(t):
    t=re.sub(r'(?<![\w/])(REL_TEMP_\d+|K_TEMP_\d+|ORG\d{3}|LOC\d{3}|PS\d{3}|WR\d{3}|EV\d{4}|CH\d{3}|E\d{3})(?!\d)',lambda m:link(m[0]),t)
    return re.sub(r'\bL(\d+)(?:[–-]L?(\d+))?',lambda m:f'[L{m[1]}'+(f'–{m[2]}' if m[2] else '')+f']({SRC}:{m[1]})',t)
def section(n,title,body):return f'\n## {n}｜{title}\n\n'+refs(body)+'\n'
def bullets(arr):return '\n'.join('- '+v for v in arr)
def render(d):
    s=f'# {d["id"]}｜{d["name"]}\n\n事实档案；数据库并列别名不代表人物已知这些身份。来源与裁决遵循[来源规则](../00_source_policy.md)及[人工裁决](../../audit/USER_DECISIONS.md)。\n'
    s+=section(1,'基础身份',f'姓名：{d["name"]}。别名／称号：{d["aliases"]}。Tier {d["tier"]}：{d["reason"]}。\n\n首次确认／导航：{d["first"]}。\n\n所给原著末尾状态：{d["end"]}\n\n等级按每项标记：A直接叙述／实际表现；B强支持；C弱推断；D人物自述／理论；E他人评价；F未知。回忆揭晓位置不等于事件发生时间。')
    if d['tier'] in 'AB':
        s+=section(2,'身份与所属阶段表','| 阶段 | 身份／所属／职务 | 公开边界与证据 |\n|---|---|---|\n'+'\n'.join('| '+' | '.join(x)+' |' for x in d['stages']))
        ap=d['appearance'];s+=section(3,'外貌','\n\n'.join(f'### 3.{i} {title}\n\n{ap[i-1]}' for i,title in enumerate(['稳定特征（限定身体形态）','阶段性外貌','服装与场合','未知'],1)))
        s+=section(4,'能力与战斗事实',d['abilities']+'\n\n消耗：仅采用正文明确的魔力、伤势、准备与特殊条件；未给出量化消耗者为F，不填冷却或次数。认证与位阶是两个维度（WR004）；一次胜负不生成永久强弱排名。')
        s+=section(5,'关键经历与状态变化',bullets(d['changes']))
        s+=section(6,'心理与动机证据',bullets(d['psych']))
        s+=section(7,'可重复行为模式',bullets(d['patterns']))
        s+=section(8,'语言与称呼事实索引',d['language'])
    else:
        s+=section(2,'身份、职能、能力与关键作用',d['brief'])
    s+=section(9,'重要关系导航',d['relations']+'\n\n'+tempnav(d,'relationship_refs')+'\n\n以上仅供后续有向关系建库；家庭称呼、合作、同住及表白不自动建立法律亲属或双向恋爱。')
    s+=section(10,'重要认知导航',d['knowledge']+'\n\n'+tempnav(d,'knowledge_refs')+'\n\n这些是事件级候选入口，事件中其他持有者的知识不属于本人物。必须在对应记录中核对 holder、取得渠道和阶段后使用。')
    if d['tier']=='A':
        s+=section(11,'关键阶段 State Snapshot','各快照在指定事件结束处取样；没有列出的维度不从末尾状态回填。身份是作者侧事实视图，公开范围另见认知栏。\n\n'+'\n\n'.join('### '+x['node']+'\n\n'+bullets([k+'：'+x[k] for k in ['身份','所属','位置','能力','伤势','关系','认知','心理']]) for x in d['snapshots']))
    elif d['tier']=='B':s+=section(11,'阶段使用边界','以第2、4、5节的事件边界恢复身份与能力；未发生的终局状态不得带回首次登场。未另扩展核心人物级快照。')
    s+=section(12,'未知与争议',bullets([f'{d["id"]}-U{i:02d}｜{v}' for i,v in enumerate(d['unknown'],1)]))
    s+=section(13,'证据与旧审计回接',d.get('audit','旧卡不能作为事实来源；人物相关的未核定性格、年龄及关系不予补全。')+'\n\n'+bullets([f'{i}｜{E[i]["level"]}｜L{E[i]["start"]}–{E[i]["end"]}' for i in dict.fromkeys(d['evidence'])])+'\n\n证据原文与修订保留在原索引，不重复抄录。局部“当时未知”只在该段有效；本档案的后续阶段以新证据续接。已登记的旧记录冲突以 [STAGE2B2_REVIEW](../STAGE2B2_REVIEW.md) 为导航，不静默修改旧证据。')
    return s
def tempnav(d,key):
    ids=list(dict.fromkeys(k for ev in d['events'] for k in EV[ev][key]))
    return '相关事件所登记的 TEMP 入口：'+('、'.join(ids) if ids else '现有事件未登记专门 TEMP；后续按本档案原著定位补建。')
def main():
    global PEOPLE
    data=json.loads((OUT/'_build2b2/dossiers.json').read_text(encoding='utf-8'))
    PEOPLE={d['id']:d for d in data}
    for d in data:(OUT/f'{d["id"]}_{d["name"]}.md').write_text(render(d),encoding='utf-8')
    (OUT/'records.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('Rendered',len(data),dict(collections.Counter(d['tier'] for d in data)))
if __name__=='__main__':main()
