# AI Software Estimation Skill

用于从 PRD、用例、设计说明和能力清单中生成可追溯的软件规模、复杂度、不确定性和交付条件评估。

## 适用范围

本 Skill 仅适用于企业管理软件：软件需要管理组织业务对象、角色、权限、工作流、交易、记录、合规或运营流程，并且能够声明系统边界和业务负责人。

开发者/工具软件、消费者互联网产品、一般内容或社交产品、游戏、媒体/创意应用、嵌入式或实时控制系统、科学计算以及基础设施/平台软件默认不适用。混合产品必须先拆出企业管理子系统；无法拆分时返回 `not applicable`。

门禁失败后不计算 `US`、`C`、`CF`、`D`、`V`、`AS` 或成本 `P`。Skill 不会把缺失证据补成零，也不会让模型直接决定计数口径、权重、系数或最终报价。

## 工作内容

- 从原文抽取带引用的功能过程和复杂度证据。
- 根据证据选择一个主计量单位，使用确定性规则重放 `US`、`AS` 和 `C`。
- 将文档成熟度、未决风险、平台能力和历史生产率分别记录，避免把置信度折算成 `CF`。
- 输出逐参数置信度、未知项、验证动作和具名人工审批点。

## 安装

将仓库目录复制到 Codex skills 目录：

```text
$CODEX_HOME/skills/ai-software-estimation/
```

目录应至少包含：

```text
SKILL.md
agents/openai.yaml
references/output-template.md
references/scoring-rubric.md
scripts/inventory_markdown.py
```

## 使用前验证

使用 Codex 的 `skill-creator` 校验脚本：

```text
python quick_validate.py path/to/ai-software-estimation
```

详细的计量规则、置信度门槛和输出契约见 `references/`。Skill 只生成评估记录，不修改 PRD 或设计文档。
