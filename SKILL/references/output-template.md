# 评估报告模板

按以下顺序输出。每项结论都应能回指到输入文件的位置；没有证据时明确写 `Unknown`、`Assumed` 或“不可评估”。

## 1. 适用性门禁

```text
gate: pass | not applicable
product_purpose:
business_users_or_owners:
business_processes:
system_boundary:
excluded_scope:
gate_evidence:
reviewer:
review_date:
```

门禁为 `not applicable` 时，只报告失败条件和排除范围，不计算 `US`、`C`、`CF`、`D`、`V`、`AS` 或 `P`。

## 2. 输入边界与成熟度

```text
project:
stage: M0 | M1 | M2 | M3 | M4 | unknown
inputs:
document_roles:
excluded_inputs:
source_versions:
system_boundary:
```

说明哪些材料是正式 PRD/设计，哪些只是概念、能力清单、测试夹具或实现资产，并列出缺失的设计、部署和历史数据。

## 3. 方法选择

```text
primary_method:
unit:
why_selected:
cross_checks:
rejected_alternatives:
rules_version:
```

每个项目只能有一个主计量单位。说明为什么选择 UCP/UUCP、NESMA/IFPUG 或 COSMIC；页面、API、实体、文件、测试步骤等不得与主单位相加。

## 4. 功能规模账本

| ID | 功能过程 | Actor/触发 | 业务结果 | 主路径与替代路径 | 数据交互/验收 | 证据等级 | 状态 | 单位/权重 | 引用 | 评审决定 |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: | --- | --- |

```text
UAW = ...
UUCW = 5S + 10A + 15C = ...
US = UAW + UUCW = ...
```

只将 `E1/E2` 计入 `US`；`E0` 保留为待确认项。每行必须是 `Observed`、`Assumed`、`Unknown` 或 `Rejected` 之一。

## 5. 复杂度证据与计算

| 维度 | 分数 0～5 | 最低证据引用 | 已知约束 | Unknown | 评审决定 |
| --- | ---: | --- | --- | --- | --- |
| `L` 业务逻辑 |  |  |  |  |  |
| `W` 流程与状态 |  |  |  |  |  |
| `D` 数据一致性 |  |  |  |  |  |
| `A` 权限与安全 |  |  |  |  |  |
| `I` 外部集成 |  |  |  |  |  |
| `Q` 可靠性与性能 |  |  |  |  |  |
| `O` 交付与运维 |  |  |  |  |  |

```text
weights = 0.25/0.20/0.15/0.15/0.10/0.10/0.05
C = 0.25L + 0.20W + 0.15D + 0.15A + 0.10I + 0.10Q + 0.05O = ...
```

未知不得默认为零。若某维度明确不适用，附责任评审人的批准证据。

## 6. 交付、不确定性与生产率

```text
D = ... | not assessable
D_evidence:
CF = ...
CF_stage:
CF_scenario:
risk_register:
V = ... | provisional baseline | not assessable
V_source_and_history:
```

说明 `CF=f(M,R)` 的阶段区间和风险场景。确认约束进入 `C`，未决依赖进入 `CF`，不得重复计费。没有经过验证的 `D` 或 `V` 时，成本 `P` 为不可评估。

## 7. 置信度

| 参数/输出 | 标签 | 证据覆盖率 | 假设/未知 | 双人评审差异 | 重跑/回测 | 理由与限制 |
| --- | --- | ---: | --- | --- | --- | --- |
| 门禁 |  |  |  |  |  |  |
| `US` |  |  |  |  |  |  |
| `C` |  |  |  |  |  |  |
| `D` |  |  |  |  |  |  |
| `CF` |  |  |  |  |  |  |
| `V` |  |  |  |  |  |  |
| `AS` |  |  |  |  |  |  |
| `P` |  |  |  |  |  |  |

置信度按参数取最弱环节。`AS` 取 `US` 与 `CF` 的较低者；`P` 取 `US/C/D/CF/V` 的较低者。没有 `D` 或 `V` 时，`P` 标为低或不可评估。

## 8. 范围计算与审批

```text
AS = US × CF = ...
P  = AS × (C / C') × D × V = ... | not assessable
range:
top_drivers:
unknowns_to_close:
re_estimate_triggers:
approver:
approval_date:
model_version:
prompt_version:
retrieval_index_version:
rules_version:
```

## 9. 验证记录

说明：

- 计数项和评分项的引用覆盖率；
- `E1/E2` 追踪覆盖、F1、重复率和引用正确率；
- 两位评审人的 `US` 和 `C` 差异；
- 固定配置重跑是否重现公式和账本；
- `C/CF` 重复计费检查；
- `D` 原型、`CF` 变更回放和 `V` 时间留出回测；
- 达不到门槛时的人工复核动作和重新评估触发条件。
