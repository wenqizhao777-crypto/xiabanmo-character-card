# Reusable audit-only incremental batch finalizer. Called with audit script globals.
ledger=read('reading_ledger.json');prev=copy.deepcopy(ledger['coverage']);start,end=CFG['start'],CFG['end'];sid=change['session'];oldcp=read('resume_checkpoint.json')
ranges=[[1,end],[36130,38825]] if end<36129 else [[1,38825]]
chars=sum(len(S[n-1]) for lo,hi in ranges for n in range(lo,hi+1));lines=sum(hi-lo+1 for lo,hi in ranges)
assert chars-prev['continuous_semantic_chars']==sum(map(len,S[start-1:end]))
newcards=CFG['newcards'];oldcardcount=len(ledger['card_entries_read']);ledger['card_entries_read']=sorted(set(ledger['card_entries_read']+newcards));ledger['card_entries_targeted']=sorted(set(ledger['card_entries_targeted'])-set(ledger['card_entries_read']));cardcount=len(ledger['card_entries_read'])
cov=copy.deepcopy(prev);cov.update(continuous_semantic_chars=chars,continuous_semantic_char_percent=round(100*chars/1641637,2),continuous_semantic_lines=lines,continuous_semantic_line_percent=round(100*lines/38825,2),worldbook_full_bodies_read=cardcount)
ledger['coverage']=cov;ledger['source_full_read_ranges']=ranges
session=dict(session=sid,previous_next_line=start,new_source_range=[start,end],new_lines=end-start+1,new_chars=chars-prev['continuous_semantic_chars'],next_line=end+1,completed_chapters=CFG['chapters'],note=CFG['note'],**{k:v for k,v in change.items() if k not in ['session','evidence_changes','missing_changes']},revised_evidence_ids=[x['id'] for x in change['evidence_changes']],new_full_card_body_ids=newcards,rechecked_full_card_body_ids=CFG.get('rechecked',[]),rechecked_existing_card_sections=CFG.get('targeted',[]));ledger['sessions'].append(session);write('reading_ledger.json',ledger)
nc=next(c for c in chap if c['start_line']==end+1);last=next(c for c in reversed(chap) if c['start_line']<=end and c['kind']=='编号正文');cp=read('resume_checkpoint.json')
scene=CFG['scene'];pending=CFG['pending'];cp.update(next_source_start_line=end+1,next_source_end_hint=nc['end_line'],source_unread_main_range=[end+1,36129],next_source_chapter=nc['volume']+' '+nc['title'].lstrip('# '),last_completed_source_chapter=last['volume']+' '+last['title'].lstrip('# '),last_read_line=end,session=sid,cumulative_character_coverage=cov['continuous_semantic_char_percent'],cumulative_characters=chars,card_body_unread_ids=sorted(set(cards)-set(ledger['card_entries_read'])),integration_status=f'内部批次{sid}已保存；一致性检查后立即续读，不等待用户',latest_scene=scene,pending_rechecks=pending);write('resume_checkpoint.json',cp)
pct=f'{cov["continuous_semantic_char_percent"]:.2f}';sev=Counter(x['severity'] for x in issues);ni=len(issues);ec=len(ev);cc=max(int(x['id'][1:]) for x in issues if x['id'].startswith('C'));mc=len(missing);nextlabel=f'L{end+1}／'+cp['next_source_chapter'];oldni=ni-len(change['new_issue_ids']);oldcc=cc-len(change['new_issue_ids']);oldec=ec-len(change['new_evidence_ids']);oldmc=mc-len(change['new_missing_ids'])
nav=f'> 续审{sid}导航：唯一续读断点为 **{nextlabel}**，累计 **{pct}%（{chars}／1641637字符）**。先见[轻量续读索引](CONTINUE_STATE.md)；历史时点不能覆盖[现行断点](resume_checkpoint.json)。'
for n in ['00_card_structure.md','01_evidence_index.md','02_full_audit_report.md','03_missing_content.md','04_timeline_knowledge_risks.md','05_user_confirmation_required.md']:
 s=(A/n).read_text('utf-8');s=re.sub(r'^> 续审\d+导航：.*$',lambda m:nav,s,count=1,flags=re.M);mdwrite(n,s)
for n in ['README.md','02_full_audit_report.md']:
 s=(A/n).read_text('utf-8')
 for k,v in sev.items():s=re.sub(r'\|'+re.escape(k)+r'\|\d+\|',f'|{k}|{v}|',s,count=1)
 if n.startswith('02'):
  s=s.replace(f'当前{oldni}项＝{oldcc}项C',f'当前{ni}项＝{cc}项C',1).replace(f'累计记录{oldni}项',f'累计记录{ni}项',1).replace(f'不是{oldni}条',f'不是{ni}条',1)
 else:
  s=re.sub(r'^> 续审\d+已保存.*$',f'> 续审{sid}已保存；自主任务继续。唯一下一断点 **{nextlabel}**，累计 **{pct}%（{chars}／1641637字符）**。先读[CONTINUE_STATE.md](CONTINUE_STATE.md)；校验后立即续读。',s,count=1,flags=re.M)
  s=s.replace(f'累计完整语义阅读{oldcardcount}条正文',f'累计完整语义阅读{cardcount}条正文',1)
  s=re.sub(r'原著连续语义核验：L1–\d+及L36130–38825，共[^。]+。',f'原著连续语义核验：L1–{end}及L36130–38825，共{lines}/38825行（{cov["continuous_semantic_line_percent"]:.2f}%；按无换行字符{pct}%，{chars}/1641637字符）。',s,count=1)
  for a,b in [(f'**{oldni}项**',f'**{ni}项**'),(f'{oldni}项Canon',f'{ni}项Canon'),(f'另列{oldmc}项',f'另列{mc}项'),(f'源文L{start}–36129',f'源文L{end+1}–36129'),(f'：{oldec}组可回查证据',f'：{ec}组可回查证据'),(f'：{oldni}项工作稿',f'：{ni}项工作稿')]:s=s.replace(a,b,1)
  s=re.sub(r'从现行断点L\d+（[^）]+）',f'从现行断点L{end+1}（{cp["next_source_chapter"]}）',s,count=1)
  s+=f'\n## 续审{sid}｜'+CFG['title']+'\n\n'+f'连续L{start}—{end}，{CFG["chapters"]}，{session["new_lines"]}行/{session["new_chars"]}字符；累计{pct}%（{chars}/1641637）。下一{nextlabel}。新增证据{len(change["new_evidence_ids"])}组（至E{ec:03}）、问题{len(change["new_issue_ids"])}项（至C{cc:03}）、遗漏{len(change["new_missing_ids"])}项（至M{mc:03}），修订旧问题{len(change["updated_existing_issue_ids"])}项、证据{len(change["evidence_changes"])}项、遗漏{len(change["expanded_missing_ids"])}项。新读{len(newcards)}条卡正文，累计{cardcount}/143。\n\n'+CFG['summary']+'\n\n保存校验后立即继续，不等待用户。\n'
 mdwrite(n,s)
s=(A/'03_missing_content.md').read_text('utf-8').replace(f'M001—M{oldmc:03}',f'M001—M{mc:03}').replace(f'共{oldmc}项',f'共{mc}项').replace(f'L{start}—36129',f'L{end+1}—36129').replace(f'L{start}–36129',f'L{end+1}–36129');mdwrite('03_missing_content.md',s)
extra={'00_card_structure.md':f'本批完整新读{newcards}，累计{cardcount}/143；全文复核{CFG.get("rechecked",[])}、定点复核{CFG.get("targeted",[])}。卡内未来摘要不计原著覆盖。','04_timeline_knowledge_risks.md':knowledge+f'\n\n变更索引见session_{sid}_changes.json，完整旧问题修订链见judgment_changes.json。','05_user_confirmation_required.md':CFG['u_note']}
for n,body in extra.items():mdwrite(n,(A/n).read_text('utf-8')+f'\n## 续审{sid}｜增量与阶段校正\n\n'+body+'\n')
oldnav=(A/'CONTINUE_STATE.md').read_text('utf-8');rules=oldnav[oldnav.index('## 续读规则'):oldnav.index('## 当前场景与开放索引')];footer=oldnav[oldnav.index('## 详细资料职责与读取条件'):];footer=re.sub(r'\[\d+补证留痕\]\(session_\d+_changes.json\)',f'[{sid}补证留痕](session_{sid}_changes.json)',footer)
state=f'''# 续读接管索引｜第一阶段自主连续执行中

导航不替代详细证据与历史。正常完成条件为原著100%后通过最终第一阶段完整性检查；内部批次保存后立即续读，不能等待“继续”。

- **唯一下一断点：{nextlabel}**，章末提示L{nc['end_line']}。
- **累计字符{pct}%＝{chars:,}／1,641,637**；{lines}行。已读L1—{end}及独立末段L36130—38825，未贯通。{sid}新增L{start}—{end}，{session['new_lines']}行/{session['new_chars']}字符，{CFG['chapters']}。
- **E001—E{ec:03}、C001—C{cc:03}、M001—M{mc:03}**；下一E{ec+1:03}/C{cc+1:03}/M{mc+1:03}。主报告{ni}项＝C{cc}＋有效S18＋R5；S018撤销占位勿用；U001—U008八组。
- 卡正文{cardcount}/143，余{143-cardcount}；手机/HTML未全审、宿主未运行。阶段IN_PROGRESS_NOT_COMPLETE。

'''+rules+'## 当前场景与开放索引\n\n'+scene+'\n\n'+''.join('- '+x+'\n' for x in pending)+f'\n**本批维护：** {CFG["health"]}；本批完整性与输入哈希见report_validation.json。校验后立即续读。\n\n'+footer
mdwrite('CONTINUE_STATE.md',state)
v=read('report_validation.json');v.update(issue_count=ni,severity=dict(sev),evidence_count=ec,missing_count=mc,coverage=cov,next_source_start_line=end+1);v[f'session_{sid}']={'status':'PENDING_VALIDATION','session':session};write('report_validation.json',v)
print(json.dumps(dict(coverage=cov,next_line=end+1,E=ec,C=cc,M=mc),ensure_ascii=False))
