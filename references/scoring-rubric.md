# Scoring Rubric

## Applicability Gate

Use this rubric only for enterprise management software: software that manages organizational business objects, roles, permissions, workflows, transactions, records, compliance, operations, or internal/external business processes. Require a declared system boundary and an identifiable business owner or operational context.

Reject developer/tool software, consumer internet products, general content or social products, games, media/creative applications, embedded or real-time control systems, scientific/high-performance computing, and infrastructure/platform products whose dominant work is not business-process management. If a product is mixed, isolate the enterprise-management subsystem; otherwise return **not applicable** and do not calculate a size or cost.

## Method Selection

Use exactly one primary size unit per assessment.

| Evidence available | Primary method | Boundary |
| --- | --- | --- |
| Actors, use cases, and transaction narratives, but little field-level detail | UCP/UUCP | Group capabilities into user goals; do not count every UI control as a use case |
| ILF/EIF and EI/EO/EQ evidence | NESMA/IFPUG function points | Apply the selected NESMA maturity method or IFPUG counting rules consistently |
| Functional processes with Entry, Exit, Read, Write movements | COSMIC | Count data movements within the declared software boundary |
| A capability list with no interaction narrative | Provisional UCP | Group related bullets into capabilities, mark transaction counts as assumptions, and keep confidence low |

Page, entity, API, file, scheduled-job, component, and plugin counts are decomposition dimensions. They are not added to UCP, function points, or COSMIC points.

## Evidence Ledger

Use one row per functional process or complexity claim:

```text
id | source | citation | actor | trigger | outcome | main_path | alternate_path
data_interaction | method_unit | proposed_weight | evidence_state | confidence | reviewer_note
```

When a document is a concept note or capability inventory, record that status in the report. A capability claim such as “supports permissions” does not prove a field-level permission matrix, a deployed plugin, or a production-ready security control.

## Complexity Anchors

Score each dimension from 0 to 5. Quote evidence and list unknowns before assigning a score.

| Dimension | 0-1 | 2-3 | 4-5 |
| --- | --- | --- | --- |
| `L` business logic | Direct CRUD or simple validation | Conditions, calculations, multiple outcomes | Rule chains, dense exceptions, difficult rollback |
| `W` workflow/state | Stateless or one-step | Simple state flow | Strict, irreversible, scheduled, or event-driven transitions |
| `D` data consistency | One object save | Two-object coordination | Cross-object transaction, uniqueness, idempotency, concurrency |
| `A` access/security | One authenticated role | Role-level access | Object/field-level access, guest token, tenant isolation, sensitive-data controls |
| `I` external integration | No external dependency | One stable interface | Multiple systems, retries, throttling, signatures, async compensation |
| `Q` reliability/performance | Ordinary web target | Stated capacity or response target | High availability, peak load, offline, real-time, strict SLO |
| `O` delivery/operations | Single environment | Tests and basic monitoring | Multiple environments, migration, rollout, backup/recovery, continuous operations |

Default weights for a general transactional system are `0.25/0.20/0.15/0.15/0.10/0.10/0.05` for `L/W/D/A/I/Q/O`. Use an approved alternative vector for workflow, finance, BI, integration, or customer-facing systems and preserve the total weight of `1.00`.

## D, CF, V Boundaries

- `D` is delivery effort context: stack familiarity, reuse, quality gate, deployment/integration, scope, and platform boundary. Coefficients come from an approved table, not model prose.
- `CF` is stage-based uncertainty. The model identifies uncertainty; an owner maps it to the approved stage interval. A confirmed constraint belongs in `C`; an unconfirmed dependency belongs in `CF`.
- `V` is unit productivity or unit cost. Normalize scope, actual effort/cost, team, stack, quality gate, delivery scope, change, rework, defects, and AI usage before comparing projects. Do not use code volume as a universal productivity proxy.

Use canonical names in calculations:

```text
US = unadjusted primary size
AS = US × CF
P  = AS × (C / C') × D × V
```

If the source organization uses `S` for either raw or adjusted size, document the mapping before calculating.

## Confidence Rubric

Treat confidence as an evidence and validation judgment, not a probability emitted by the model. Record these measures for every project and parameter:

| Measure | Calculation or check | Interpretation |
| --- | --- | --- |
| Evidence coverage | cited or explicitly assumed counted items / total counted items | Must be 100% to pass the provisional validation gate |
| Assumption rate | assumed items / counted items | Higher values reduce confidence unless the convention is approved and stable |
| Unknown rate | unknown required fields / required fields | Unknowns remain risks; they are not converted to zero |
| Boundary stability | relative `US` difference between independent reviews; per-dimension `C` spread | Shows whether reviewers are counting the same scope |
| Reproducibility | repeated ledger similarity under fixed model/prompt/rules; exact formula replay | Detects model or workflow drift |
| Historical validation | prototype checks, risk replay, or time-based holdout interval coverage | Required before treating `D`, `CF`, or `V` as organizational baselines |

Use these labels as gates: **high** requires a reviewed baseline, complete citations, calibrated reviewer agreement, deterministic replay, and applicable validation; **medium** fits a structured but incompletely approved baseline with explicit assumptions and partial review; **low** applies to concept/capability material, unstable boundaries, missing citations, or absent validation. `AS` takes the lower confidence of `US` and `CF`. A cost result `P` takes the weakest confidence among `US`, `C`, `D`, `CF`, and `V`; missing `D` or `V` makes cost confidence low or not assessable. Relative disagreement thresholds (for example, 10%/20% for `US` and 0.5/1.0 points for `C`) are local starting points and must be calibrated with completed projects.

## Validation Gates

Minimum gates for a provisional estimate:

- 100% of counted items have a citation or explicit assumption.
- The selected primary method is declared and no heterogeneous units are summed.
- Re-running the deterministic ledger reproduces `US`, `AS`, and `P`.
- A second reviewer can distinguish observed, assumed, unknown, and rejected evidence.
- Evidence is charged once across `C` and `CF`.
- Historical `V` predictions use time-based holdout or are labeled as an external/provisional baseline.
- The report states who approved scores, coefficients, stage, and final range.
