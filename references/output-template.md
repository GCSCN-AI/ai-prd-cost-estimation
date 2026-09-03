# Assessment Output Template

Use this structure for a reusable report. Keep tables concise and link every claim to a source location.

## Applicability Gate

```text
gate: pass | fail | not applicable
product_purpose:
business_users_or_owners:
business_processes:
system_boundary:
excluded_scope:
gate_evidence:
reviewer:
```

If the gate is `fail` or `not applicable`, stop and report the reason. Do not calculate `US`, `C`, `CF`, `D`, `V`, `AS`, or `P`.

## Input Boundary

```text
project:
stage:
inputs:
document_roles:
excluded_inputs:
source_versions:
```

## Method And Confidence

```text
primary_method:
unit:
why_selected:
cross_checks:
confidence:
```

## Functional Size

| ID | Functional process | Actor/trigger | Main evidence | Alternate paths | Unit weight | State | Citation |
| --- | --- | --- | --- | --- | ---: | --- | --- |

```text
UAW = ...
UUCW or primary component total = ...
US = ...
```

## Complexity

| Dimension | Score | Evidence | Unknowns | Reviewer decision |
| --- | ---: | --- | --- | --- |
| L |  |  |  |  |
| W |  |  |  |  |
| D |  |  |  |  |
| A |  |  |  |  |
| I |  |  |  |  |
| Q |  |  |  |  |
| O |  |  |  |  |

```text
C = ...
```

## Delivery, Uncertainty, Productivity

```text
D = ... or not assessable; reason = ...
CF = ...; stage = ...; scenario = ...
V = ... or provisional baseline; source/history = ...
```

## Confidence

| Parameter/output | Label | Evidence coverage | Assumption/unknown notes | Reviewer agreement | Replay/backtest | Rationale |
| --- | --- | ---: | --- | --- | --- | --- |
| US |  |  |  |  |  |  |
| C |  |  |  |  |  |  |
| D |  |  |  |  |  |  |
| CF |  |  |  |  |  |  |
| V |  |  |  |  |  |  |
| AS/P |  |  |  |  |  |  |

Use the weakest applicable parameter confidence for `AS` and for cost `P`. State when a label is low or not assessable because validation data is absent.

## Range And Review

```text
AS = US × CF = ...
P = AS × (C / C') × D × V = ...
range = ...
top_drivers = ...
unknowns_to_close = ...
approver = ...
model_version = ...
rules_version = ...
```

## Validation Notes

State item coverage, reviewer agreement or comparison baseline, reproducibility of calculations, double-counting checks, and the conditions that would trigger a re-estimate.
