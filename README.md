# AI PRD Cost Estimation

本仓库提供一套从 PRD 与设计文档评估软件规模、复杂度、不确定性和交付条件的方法与 Skill。方法适用于企业管理软件，以及具有明确交易、预约、服务交付、订单履约或活动运营流程的 B2C/B2B2C 软件。

## 内容

- [评估论文](基于需求文档和设计文档的软件规模与复杂度评估方法.md)：方法、研究问题、验证协议、ViBench 案头验证和适用边界。
- [SKILL/SKILL.md](SKILL/SKILL.md)：可供 Codex 使用的评估 Skill。
- `SKILL/references/`：计量规则、复杂度锚点、置信度门槛和评估输出模板。
- `SKILL/scripts/inventory_markdown.py`：确定性检查 Markdown 标题、列表和表格，辅助建立输入清单。

## 适用边界

方法要求业务目的、业务对象与动作、参与者与责任、系统边界和领域适配证据全部满足门禁。纯内容、纯社交、游戏、个人工具、通用工具、媒体/创意、嵌入式/实时控制、科学计算以及基础设施/平台软件不适用；混合产品必须先隔离可独立交付的业务子系统。

门禁失败时停止计算，不输出 `US`、`C`、`CF`、`D`、`V`、`AS` 或成本 `P`。缺少设计、平台、团队或历史生产率资料时，应明确标记为 `Unknown` 或不可评估，不能用模型补齐。

## 安装与验证

将 `SKILL` 目录复制或重命名为 Codex 的技能目录，例如：

```text
$CODEX_HOME/skills/ai-software-estimation/
```

使用 Skill Creator 的验证脚本检查结构：

```text
python <skill-creator>/scripts/quick_validate.py SKILL
```

评估只生成独立账本和报告，不修改 PRD 或设计源文件。
