# Stage 2B-1过程与核验导航

四份主Markdown是现行事实条目；本目录不是Canon事实来源，不得用索引覆盖主文件。

- `input_baseline.json`：动笔前310个既有文件的SHA-256基线，路径相对项目根；本轮四模块和README允许改变，其余既有文件保持。
- `manifest.json`：107条ID、文件、原著范围与引用；只存导航，不复制完整定义。
- `unresolved_index.json`：40组未解主题到主条目的映射。
- `revision_notes.json`：本轮草稿核对的旧措辞、新措辞及部分原因；不是修改Stage 1或2A的记录。
- `write_entries.py`：本轮使用的追加辅助，已有索引时禁止初始化重置；不得对旧_build脚本进行全量重建。
- `initial_check_result.json`：首次检查记录；仅结果文件自身尚未生成导致两个链接暂缺，后续检查已通过。
- `validate.py`、`check_result.json`：编号、字段、引用、链接、原著行号边界、未知导航和输入保护检查。运行validate只更新本目录结果，不自动修改事实或旧数据库。

语义核验方法：利用Stage 1最终证据及Stage 2A定位，按概念回查原著关键段落；没有重新全文连续阅读，也不把机器范围检查称为事实真伪证明。被截断的工具输出不计作已完整读过，必要锚点重新用小窗口读取。

TW资料路由：已使用consult-tavernweave-library，加载ST-A0与沟通/路由参考；本轮只做原著事实资料层，无新库候选采用，无运行时API实现。没有进行SillyTavern实机验证，也没有将自动检查标为用户验收通过。
