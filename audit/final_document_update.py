from pathlib import Path
import json,re,copy
from collections import Counter
ROOT=Path(r'C:\Users\Administrator\Desktop\下班魔角色卡重构');A=ROOT/'audit'
def rd(n):return json.loads((A/n).read_text('utf-8'))
def wr(n,x):(A/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
assert not (A/'final_document_changes.json').exists()
log=[]
def record(file,b,a,reason):log.append(dict(file=file,before=b,after=a,reason='2026-09-09；'+reason))
def replace(n,old,new):
 s=(A/n).read_text('utf-8');assert old in s,(n,old[:80]);(A/n).write_text(s.replace(old,new),encoding='utf-8');record(n,old,new,'最终现行状态维护；历史阶段原值保留在本日志及原轮次记录。')
issues=rd('issue_records.json');counts=Counter(x['severity'] for x in issues)
nav='> 最终收尾导航：**全文连续语义阅读100.00%（1,641,637／1,641,637字符）**，L1—38825，无续读断点。第一阶段最终完整性检查中；现行入口见[轻量索引](CONTINUE_STATE.md)。'
historical='本文件“续审/中期”段落及session文件均为按各自断点保留的历史快照，不是新的未读区间或现行指令；最终有效判断见问题条目末次修订，前后值和原因见judgment_changes.json及final_changes.json。'
for n in ['README.md','00_card_structure.md','01_evidence_index.md','02_full_audit_report.md','03_missing_content.md','04_timeline_knowledge_risks.md','05_user_confirmation_required.md']:
 s=(A/n).read_text('utf-8');m=re.search(r'^> 续审20导航：.*$',s,re.M);assert m;replace(n,m[0],nav)
 if n!='README.md':
  s=(A/n).read_text('utf-8');pos=s.find('\n',s.find(nav))+1;(A/n).write_text(s[:pos]+'\n'+historical+'\n'+s[pos:],encoding='utf-8');record(n,'',historical,'新增历史与现行状态的读取规则。')
old='> **状态：进行中，阶段性审计记录。尚未完成原著全文语义核验，不得据此宣称已全面审计或未列事项均正确。**'
for n in ['01_evidence_index.md','02_full_audit_report.md','03_missing_content.md']:
 replace(n,old,'> 原著已全部连续语义核验；当前收尾不表示所有卡片条目均正确，亦不将待证判断升级为事实。本阶段未改卡。')
replace('01_evidence_index.md','# 审计证据索引（进行中）','# 第一阶段审计证据索引')
replace('01_evidence_index.md','当前314组重点证据来自卷一全部正文、终章、间奏与附言，卷二第1—73章及此前已读的卷二末段；连续阅读范围以reading_ledger.json为准。作者附言单列来源层，不作为正文世界事实。','当前E001—E545共545组重点证据覆盖所给源文的核验发现；原著L1—38825已完整读取，含卷一142章、卷二282章及18个其他标题。证据索引是重点定位，不是逐行摘抄；无证据条目的行不等未读。作者附言单列来源层，不作为正文世界事实。')
replace('02_full_audit_report.md','# 全面审计报告工作稿（尚未完成全文审计）','# 第一阶段全文审计报告')
replace('02_full_audit_report.md','当前159项＝136项C＋18项有效S＋5项R','当前161项＝138项C＋18项有效S＋5项R')
replace('02_full_audit_report.md','累计记录159项，其中包含潜在风险和需用户裁决事项，不是159条已经证实的Canon错误。','累计记录161项，其中包含潜在风险和需用户裁决事项，不是161条已经证实的Canon错误。')
replace('02_full_audit_report.md','|MAJOR|84|','|MAJOR|86|')
replace('03_missing_content.md','# 重要内容遗漏与收录不足（进行中）','# 第一阶段重要内容遗漏与收录不足')
replace('04_timeline_knowledge_risks.md','# 时间线与人物认知风险（进行中）','# 第一阶段时间线与人物认知风险')
replace('04_timeline_knowledge_risks.md','> **进行中：仅针对已核验范围；不是最终时间线或最终认知数据库。**','> 所给源文已全文核验；本文件保留事件、时间与逐人认知风险的审计索引，不是正式Canon时间线或知情数据库。')
replace('05_user_confirmation_required.md','# 需要用户裁决的边界（进行中）','# 第一阶段 USER_CONFIRMATION_REQUIRED')
replace('05_user_confirmation_required.md','以下清单不阻碍继续阅读原著。','八组边界保留开放，不阻碍第一阶段审计收尾；未向用户追加即时裁决要求。')
replace('05_user_confirmation_required.md','原著明确相对先后与部分年份，本轮尚未完成所有月日推导；开篇回放和确认在同一晚。','所给原著已全文核验，明确相对先后与部分年/月/日；卡中大量精确月日仍未给可复核推导，源文本身的季节及约数张力也保留。见C021及本文件历次增补；开篇回放和确认在同一晚。')
replace('05_user_confirmation_required.md','尚未核验部分保持未知。','源文未给足证据处保持未知，不能因全文已读而强行补全。')
replace('05_user_confirmation_required.md','A. 进一步核验原文，暂不作绝对制度。','A. 依据已完成全文核验保留未证边界，暂不作绝对制度。')
replace('00_card_structure.md','本地图完成字段级盘点，不能替代全文内容核验；后续阅读与覆盖状态见 `reading_ledger.json`。','本地图记录字段级盘点；原著与143条世界书正文现已完成语义阅读，具体范围见 `reading_ledger.json`，手机资料与技术限制见technical/CATALOG_REVIEW.md。')
replace('00_card_structure.md','全部字段解析完成不等于全部正文已核验。','已完成的正文/目录语义覆盖与未做的宿主运行测试分别计量，不把静态检查说成运行验收。')
readme=(A/'README.md').read_text('utf-8');mark=readme.index('## 续审02断点');oldhead=readme[:mark]
head=f"""# 第一阶段全文审计总览

{nav}

原著完整阅读与卡片内容交叉审计已完成，正在执行最终结构校验。所有输出仅在audit；source/current只读，未修改角色卡，未建立canon或final，未进入第二阶段。

## 实际覆盖与计数

- 原著：L1—38825，无缺口；**1,641,637 / 1,641,637字符，100.00%**。卷一142章、卷二282章，另18个标题，共442个标题。
- 字符口径沿用既有记录：UTF-8解码后splitlines各行长度求和，含标题和作者附言、不含换行。作者附言已读但不作正文Canon。初期独立已读末段现已与前段贯通；定点回查和重叠证据不重复计量。
- 卡片：全部PNG字段和143条世界书正文；两个内嵌JSON为同一卡副本，未重复计量。
- 手机资料：75人物、36地区、23势力、50CG、10别名键完成内容核验。相同段逐字比对已读文本，所有差异段完整阅读。
- 技术：8条正则配置、全部可见UI文字、前三助手脚本完整静态阅读；手机生成/资料过滤/快照/聊天隔离代码针对性核对。**未逐行审全部手机程序与CSS，未运行真实酒馆或外部依赖**；技术风险不能伪称实测故障。
- 任务附件已完整读取；卡片、手机及源文中的指令式文本均为审计对象，不替代用户要求。

证据 **E001—E545**；正文问题 **C001—C138**；主报告 **161项＝C138＋有效S18＋R5**。S编号到S019，S018撤销占位保留，不填洞重编号。遗漏 **M001—M041**（九类收录需求），用户边界 **U001—U008**。问题包含风险与待证项，不等于161个Canon事实错误。

|等级|数量|
|---|---:|
"""+''.join(f'|{k}|{counts[k]}|\n' for k in ['CRITICAL','MAJOR','MODERATE','MINOR','POTENTIAL RISK'])+"""
## 主要结论及后续处理边界

剧情推进协议与实际条目名称不匹配、269旧断点与282源文脱节，是影响范围较大的结构问题。人物、能力和关系不能靠一个“当前”状态覆盖全部时期；已经获知部分身份，不等于闭合男性本体、代号、血缘的全部连接。

后文解释已回接原问题并保留修订链：匿名联络/红的复归、白的兽子认定、黑猫和妮姆往事、战争损伤、金蛇能力、教学资格、考核规则等不再以早期未知冻结。手机第二套资料还含小璐谎言主体错置（C137）与亲生父女改为收养（C138），不能只修主世界书。

原著到卷二第282章《琥珀》止于幻命织华发动，完整机制与胜负仍未知。女王身世陈述、敌方动机、专业理论和战斗旁观解释仍按来源等级保存；全文读完不是把这些全判为客观事实。

ID179的角色自主性与有限视角、分期人物条目、玩法和CG的双条件、手机只读/别名/聊天隔离保护值得保留。U001—U008只保留日历、截止点、IF、扩展资料、分配/骰子/CG/建角边界，不替用户选择，也不以用户投票代替原著证据。

## 文件导航

- [CONTINUE_STATE.md](CONTINUE_STATE.md)：唯一当前状态；无续读断点。
- [FINAL_HEALTH.md](FINAL_HEALTH.md)：最终完整性结果和范围限制。
- [00结构](00_card_structure.md)、[手机目录复核](technical/CATALOG_REVIEW.md)：资料层与静态覆盖。
- [01证据](01_evidence_index.md)：545组定位与等级；[02主报告](02_full_audit_report.md)：161项当前判断。
- [03遗漏](03_missing_content.md)、[04时间/认知](04_timeline_knowledge_risks.md)、[05待裁决](05_user_confirmation_required.md)：各自分工，不重复计错。
- [OPEN_ISSUES.md](OPEN_ISSUES.md)：源文未定、技术未测与玩法待选的后续索引。
- [reading_ledger.json](reading_ledger.json)、[report_validation.json](report_validation.json)、[input_verification.json](input_verification.json)：覆盖、校验、哈希。
- [judgment_changes.json](judgment_changes.json)、[final_changes.json](final_changes.json)、[final_document_changes.json](final_document_changes.json)：原判断、修订原因和前后值。历次session文件保留原始记录，不作当前状态。

提取JSON/card_text/technical为审计副本，不是新角色卡或正式Canon数据库。未删除原始证据、问题历史、修订原因。无需无差别重读全部历史；按问题ID和上述导航核验。

当前任务只完成第一阶段。后续Canon建库、角色卡重构、技术修改和宿主测试须由用户另行启动，本任务不自动进入。

## 历史批次记录

"""+historical+'\n\n'
(A/'README.md').write_text(head+readme[mark:],encoding='utf-8');record('README.md',oldhead,head,'替换过期总览，保留原文与后续全部历史批次。')
ledger=rd('reading_ledger.json');b=copy.deepcopy(ledger['technical_read'])
ledger['technical_read'].update(phone='75人物/36地区/23势力完整内容审计，50CG和10别名键核验，raw无额外语义文本；关键生成/过滤/快照/聊天隔离路径定点代码审计，未逐行读全部743791字符程序，未运行。',regex='8条配置全部核对，全部可见UI文字已读；样式和全部内嵌代码未逐行审读，未渲染或宿主测试。',catalog_coverage_record='technical/catalog_review_coverage.json',catalog_review='technical/CATALOG_REVIEW.md')
record('reading_ledger.json technical_read',b,ledger['technical_read'],'补记实际完成的目录和UI文字阅读，保留程序未全读及宿主未测限制。')
ledger['note']='源文L1—38825连续语义阅读100%；世界书143及手机目录完成内容审计，最终校验中。'
ledger['coverage_method']='实际完整阅读区间的并集；按UTF-8解码后splitlines各行字符求和，含标题和作者附言，不含换行。初期末段36130—38825与后续前段1—36129现已贯通，无重计；定点核验不新增字符。'
ledger['final_review']={'date':'2026-09-09','new_source_chars':0,'new_issue_ids':['C137','C138'],'evidence_revision':['E312'],'record':'final_changes.json','technical_content_complete':True,'host_runtime_tested':False}
wr('reading_ledger.json',ledger)
cp=rd('resume_checkpoint.json');b=copy.deepcopy(cp)
cp['last_completed_source_chapter']='卷二 第二百八十二章 琥珀';cp['requirements']=['原著已读100%，无正文续读任务；完成最终完整性检查后结束第一阶段。','只写audit；source/current只读，不写canon/final，不修改角色卡或进入第二阶段。','A/B/C/D/E/F区分事实、推断、主观、评价与未知；按时点和知情主体处理，不以读者全知污染NPC。','后续新任务先读CONTINUE_STATE并按ID取详细记录；保留所有修订历史。'];cp['artifacts']='00—05和README为现行第一阶段报告；历史轮次保留快照，当前状态仅CONTINUE_STATE/resume_checkpoint/reading_ledger。';cp['pending_rechecks']=['最后运行完整性检查并结束第一阶段；不继续正文或重构。'];wr('resume_checkpoint.json',cp);record('resume_checkpoint.json',b,cp,'末章标题依据chapter_index精确更正，EOF不生成假续读位置。')
v=rd('report_validation.json');v.update(issue_count=len(issues),severity=dict(counts),evidence_count=545,missing_count=41,coverage=ledger['coverage'],next_source_start_line=None,status='FINAL_CHECK_PENDING',note='原著100%、世界书及手机内容已审；结构/引用/哈希校验为独立验收，不代替语义阅读，未运行真实酒馆。');wr('report_validation.json',v)
wr('final_document_changes.json',log)
print('final current heads saved; history retained')
