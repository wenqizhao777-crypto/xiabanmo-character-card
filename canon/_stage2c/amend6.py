from pathlib import Path
import ast,json,copy,re
P=Path.cwd();C=P/'canon';B=C/'_stage2c';ns=dict(P=P,C=C,B=B,json=json,copy=copy)
t=ast.parse((B/'integrate.py').read_text(encoding='utf-8-sig'));exec(compile(ast.Module(body=[n for n in t.body if isinstance(n,ast.FunctionDef)],type_ignores=[]),'helper','exec'),ns)
read=ns['read'];dump=ns['dump'];Q=read('canon/_stage2c/review_queue.json');CC=read('canon/_stage2c/changes.json');ns.update(queue=Q,changes=CC)
tc=ns['textchange'];start=len(CC)+1
q=Q[1];tc(q,'events/STATE_CHAINS.md','EV0126实体穿墙初试','EV0126引离干预术式维持的植物墙（术式传送为夏的解释）');tc(q,'events/STATE_CHAINS.md','引离后来能传墙不使最初可任意传人','本场墙体稀疏/恢复不证明任意实体穿墙或直接传人')
q=Q[24]
tc(q,'knowledge/README.md','**Stage 2B-4：完成。最终检查结果见 [Review](../STAGE2B4_REVIEW.md)。**','**Stage 2C整合回归：已完成核证；当前冻结状态见[最终Review](../STAGE2C_FINAL_REVIEW.md)。** 原Stage 2B-4 [Review](../STAGE2B4_REVIEW.md)保留历史。')
tc(q,'relationships/README.md','**Stage 2B-3：完成建档，检查结果见[Review](../STAGE2B3_REVIEW.md)。**','**Stage 2C整合回归：已完成核证，当前状态见[最终Review](../STAGE2C_FINAL_REVIEW.md)。** 原Stage 2B-3 [Review](../STAGE2B3_REVIEW.md)保留历史。')
tc(q,'relationships/README.md','若需身份信息权限，再到相关K_TEMP核持有人与渠道。','若需身份信息权限，到每条REL的正式K导航核持有人与渠道；K_TEMP仅为历史导入。')
tc(q,'relationships/README.md','未建立完整Knowledge数据库、关系数值、CG解锁或IF剧情。后续Stage 2B-4需用户新指令。本阶段的完成不表示故事已结束或每一未展示心理都已判明。','Knowledge正式数据库已建并完成Stage 2C整合；关系数值、CG与IF尚未实现。完成不表示故事已结束或每一未展示心理都已判明。')
# Update all relation directory row counts and claims from current records, retaining table format.
RR=read('canon/relationships/records.json');f=C/'relationships/README.md';s=f.read_text(encoding='utf-8-sig')
for r in RR:
 lines=[l for l in s.splitlines() if l.startswith('|['+r['id']+']')]
 for old in lines:
  cells=old.split('|');cells[4]=r['end'].replace('|','／');cells[5]=f'[{r["stages"][0]["event"]}](../01_master_timeline.md#{r["stages"][0]["event"].lower()})';cells[6]=str(len(r['stages'])-1);new='|'.join(cells)
  if old!=new:tc(q,'relationships/README.md',old,new);s=s.replace(old,new)
dump('canon/_stage2c/review_queue.json',Q);dump('canon/_stage2c/changes.json',CC)
f=B/'render_current.py';s=f.read_text(encoding='utf-8-sig');s+='\n# Logged navigation corrections applied after regenerating the original-format indexes.\nfor c in load("_stage2c/changes.json"):\n    if int(c["id"][2:]) >= '+str(start)+' and c["module"]=="Document" and c["record"] in ["events/STATE_CHAINS.md","relationships/README.md","knowledge/README.md"]:\n        f=C/c["record"];s=f.read_text(encoding="utf-8-sig")\n        if c["before"] in s: f.write_text(s.replace(c["before"],c["after"]),encoding="utf-8")\n';f.write_text(s,encoding='utf-8')
f=B/'reports.py';s=f.read_text(encoding='utf-8-sig').replace('35项结构与资料专项','全量结构与资料专项');f.write_text(s,encoding='utf-8')
print('Changes',len(CC))
