# Stage 2B-2 构建与核验材料

本目录只服务于人物库维护，不是另一份Canon事实来源。所有脚本写入范围限`canon/characters/`；运行前先确认用户授权范围。上游原著、审计和历史Canon保持只读。

- `input_baseline.json`：开始写入前323个既有文件的SHA-256基线。
- `legacy_readme.md`：原人物TEMP索引备份；正常查阅使用上一级`LEGACY_P_TEMP_INDEX.md`，其中相对链接才能正常指向原文件。
- `name_scan.json`：原164个入口在全文中的字面定位，只作检索，不是连续语义阅读证明；泛称、短字误命中和零命中都需人为辨认。
- `author_data.py`、`support_data.py`、`functional_data.py`：人物事实初稿。
- `refine.py`：按本轮原文回查、最终C修订修正初稿；**必须通过该入口生成最终输入**，不得直接用初稿覆盖交付。
- `dossiers.json`：已应用修正的唯一渲染输入；`../records.json`与之保持相同。
- `build.py`：渲染人物Markdown。只组织已写好的事实，不从关键词命中自动推理。
- `index.py`：生成目录和164个P_TEMP兼容入口、C/M修订导航。
- `audit_navigation.json`：每个核心人物的C、M、原卡问题位置及修订原因地址；原判断前后值仍在只读审计文件中。
- `temp_mapping.json`：P_TEMP到CH或群体/地点的映射。多人同场不能压为一个人。
- `check.py`、`check_result.json`：结构、编号、链接、快照、输入哈希检查；不冒充自动语义证明。

维护时依次执行（在项目根目录）：

```powershell
python -X utf8 canon/characters/_build2b2/refine.py
python -X utf8 canon/characters/_build2b2/build.py
python -X utf8 canon/characters/_build2b2/index.py
python -X utf8 canon/characters/_build2b2/check.py
```

新增人物使用末尾新号；已发布ID不因排序或合并改变。若以后确认CH044与CH069为同一主体，应保留旧ID重定向和裁决证据，不删除历史引用。

Unknown统计按每个人物第12节的一条编号记录计数；一条可包含相近的几个未明字段，不冒称已逐个字段穷举全书所有悬念。未核准字段只表示本库不安全采纳，不声称已经证明原著任何角落都不存在描述。追加资料仍须按原著核实。
