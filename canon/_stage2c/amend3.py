from pathlib import Path
import ast,json,copy
P=Path.cwd();C=P/'canon';B=C/'_stage2c';ns=dict(P=P,C=C,B=B,json=json,copy=copy)
t=ast.parse((B/'integrate.py').read_text(encoding='utf-8-sig'));exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helper','exec'),ns)
read=ns['read'];dump=ns['dump'];queue=read('canon/_stage2c/review_queue.json');changes=read('canon/_stage2c/changes.json');EV=read('canon/events/records.json');CH=read('canon/characters/records.json');REL=read('canon/relationships/records.json');K=read('canon/knowledge/records.json');E={r['id']:r for r in EV};H={r['id']:r for r in CH};R={r['id']:r for r in REL};Q={r['id']:r for r in K};ns.update(E=E,H=H,R=R,Q=Q,EV=EV,queue=queue,changes=changes,evidence=read('audit/evidence_records.json'));ch=ns['change'];cr=ns['cr']
q=cr(32,'Stage2C/38快照位置回归','出生快照把家庭住所代替未明出生现场','KEEP_UNKNOWN',[[18464,18472],[7131,7150]],'源段确认出生、命名及旧队见证，没有定位该次出生场所；家庭住所不替代出生现场。夏凉阳台保留明文位置，删无稳定LOC的绝对声明。',['CH006:S02','CH001:S02','CH003:S02'])
ss=copy.deepcopy(H['CH006']['snapshots']);ss[1]['位置']='出生/命名具体场所UNKNOWN；家庭生活场所另见LOC027，不把家址当本次出生地点';ch(q,'Character','CH006','snapshots',ss)
for id in ['CH001','CH003']:
 ss=copy.deepcopy(H[id]['snapshots']);ss[1]['位置']='夏凉家阳台（L7141–7145）；家庭住所导航LOC028，阳台未建独立地点ID';ch(q,'Character',id,'snapshots',ss)
ch(queue[29],'Relationship','REL025','unresolved',[R['REL025']['boundary']])
cr(33,'Stage2C/Unknown-Disputed保存','唱名措辞张力及分层机制维持未决','KEEP_DISPUTED',[[36319,36319],[38819,38825]],'PS004两段措辞不能机械末句覆盖前句；保留替代调用实例与末尾概述张力。既有争议未获得新原著验证，不为冻结消除。',['PS004','PS017','WQ003'])
cr(34,'Stage2C/未解决项全集回归','原有未决与设计延期不作事实补全','KEEP_UNKNOWN',[], 'WQ/CQ/RQ、人物U、关系未知维度和K未解命题均复查；未知原理、法律手续、阵营同一性及末尾胜负无新增证明，保留。U006具体骰规则仍留后续用户，非Canon冻结阻塞。',['UNRESOLVED.md','INFERENCE_GUARDRAILS.md','USER_DECISIONS.md'])
for mod,rows in [('events',EV),('characters',CH),('relationships',REL),('knowledge',K)]:dump(f'canon/{mod}/records.json',rows)
dump('canon/_stage2c/review_queue.json',queue);dump('canon/_stage2c/changes.json',changes)
# Make current renderer safely repeatable; use pre-Stage2C index text, never build facts from old input.
f=B/'render_current.py';s=f.read_text(encoding='utf-8-sig').replace('import json,re,ast,importlib.util,textwrap','import json,re,ast,importlib.util,textwrap,zipfile')
s=s.replace("f=C/'01_master_timeline.md';old=f.read_text(encoding='utf-8-sig')","f=C/'01_master_timeline.md';old=zipfile.ZipFile(B/'canon_before.zip').read('canon/01_master_timeline.md').decode('utf-8-sig')")
s=s.replace("f=C/'characters/README.md';s=f.read_text(encoding='utf-8-sig')","f=C/'characters/README.md';s=zipfile.ZipFile(B/'canon_before.zip').read('canon/characters/README.md').decode('utf-8-sig')")
s=s.replace('relationships/CHARACTER_SCAN.md','relationships/CHARACTER_RELATION_SCAN.md')
s=s.replace("f=C/path;s=f.read_text(encoding='utf-8-sig');prefix='../'","f=C/path;s=zipfile.ZipFile(B/'canon_before.zip').read('canon/'+path).decode('utf-8-sig');prefix='../'")
f.write_text(s,encoding='utf-8')
print(len(queue),len(changes))
