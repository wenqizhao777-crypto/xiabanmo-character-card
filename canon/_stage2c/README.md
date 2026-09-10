# Stage 2C复现与历史边界

- `input_baseline.json`、`canon_before.zip`：改动前快照，不变。
- `review_queue.json`、`changes.json`：完整CR/CC、字段前后像与证据。
- `integrate.py`、`amend*.py`：本次一次性迁移轨迹，已经执行，**不要重跑**。
- `render_current.py`：仅渲染当前正式records；不重新执行旧阶段事实整理。
- `regression.py`：读取当前数据，实际运行55查询、60组合情境、原38快照回归。
- `validate.py`：检查完整数据、引用、未知保存、变更链及受保护文件哈希。
- `reports.py`：生成人可读文档；`--freeze`仅允许此前检查PASS。
- `finalize.py`：冻结后登记模块/文件清单与SHA256；排除自身清单和重复生成的检查结果以避免自指哈希循环。

回归输出中的PARTIAL/HEARD/DISBELIEVES等是主体状态，不是客观真值。原阶段_build*输入与Review保存历史，不能覆盖当前Baseline。
