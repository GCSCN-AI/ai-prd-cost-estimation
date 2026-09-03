---
name: ai-software-estimation
description: "Estimate enterprise management software size and complexity from requirements and design documents with traceable evidence, deterministic calculations, and human review."
---

# AI Software Estimation

Use this skill when a project needs an early or design-stage estimate of functional size, business complexity, delivery conditions, uncertainty, or unit productivity from PRDs, use cases, architecture/design notes, capability lists, or similar documents.

## Operating Boundary

Treat the model as an evidence extraction and explanation assistant. Keep method selection, counting rules, formulas, approved coefficients, and the final approval deterministic and reviewable. Never invent missing requirements, actors, transactions, platform capabilities, team history, or cost data.

## Applicability Gate

Apply this skill only to enterprise management software: software used by an organization to manage business objects, roles, permissions, workflows, transactions, records, compliance, operations, or internal/external business processes. The estimate must have a declared system boundary and an identifiable business owner or operational context.

Do not apply this method to developer or tool software, consumer internet products, general content or social products, games, media or creative applications, embedded or real-time control systems, scientific/high-performance computing, or infrastructure/platform products whose dominant work is not business-process management. These systems may have different size units, quality attributes, and productivity drivers; return **not applicable** instead of forcing an estimate.

If a product is mixed, isolate the enterprise-management subsystem and estimate only that boundary. If the boundary cannot be isolated, stop and report the gate as failed. Record the gate result, evidence, excluded scope, and reviewer before calculating `US`, `C`, `CF`, `D`, or `V`.

Keep four evidence states separate:

- **Observed**: directly supported by a quoted source location.
- **Assumed**: an explicit local convention needed to compute a provisional estimate.
- **Unknown**: required information that the sources do not provide.
- **Rejected**: a tempting interpretation excluded by the counting boundary.

Read [references/scoring-rubric.md](references/scoring-rubric.md) for the default method-selection, US/AS/C/D/CF/V rules and validation gates. Read [references/output-template.md](references/output-template.md) when producing a reusable assessment record. Run `scripts/inventory_markdown.py` before manually counting Markdown capability lists or headings.

## Confidence Assessment

Confidence is assessed per parameter and per output. Do not use a model's self-reported probability as the estimate confidence. Record at least:

- evidence coverage: counted items or scored dimensions with a citation or explicit assumption divided by the total;
- assumption and unknown rates: items that rely on local conventions or missing source evidence;
- boundary stability: the difference between two independent reviews of `US` and the per-dimension spread of `C`;
- reproducibility: whether a fixed model, prompt, and rules reproduce the same ledger, plus exact deterministic formula replay;
- validation strength: prototype checks for `D`, stage/risk replay for `CF`, and time-based holdout backtests for `V`.

Use qualitative gates rather than a false-precision percentage. High confidence requires a reviewed baseline, complete citations, independent reviewer agreement within the organization's calibrated tolerance, deterministic replay, and the parameter-specific validation evidence. Medium confidence fits a structured but not fully approved PRD/design with explicit assumptions and partial review. Low confidence applies to concept notes, capability inventories, unresolved boundaries, missing citations, or absent validation data. `AS` confidence is limited by `US` and `CF`; cost confidence for `P` is limited by the weakest of `US`, `C`, `D`, `CF`, and `V`. If `D` or `V` is missing, report cost confidence as low or not assessable even when `US` is strong.

Starting thresholds such as `US` relative disagreement <=10% for high and <=20% for medium, or `C` absolute disagreement <=0.5 for high and <=1.0 for medium, are organization calibration points rather than industry constants. Revisit them with completed-project data. Always report the evidence metrics and the reason for the label.

## Workflow

1. Run the applicability gate. Record the product purpose, users, business processes, system boundary, excluded scope, evidence, and reviewer. Stop with **not applicable** when the gate fails or a mixed product cannot be isolated.
2. Inventory the inputs. Record file names, versions or dates, document role, project stage, and whether the material is a formal PRD/design or only a concept note/capability inventory. State when no implementation source or approved design is available.
3. If the input is a directory containing multiple direct project folders, enter batch mode: enumerate the folders, apply the applicability gate and full assessment independently to each folder, retain a separate evidence ledger and result, and never sum functional size or cost across folders. A later comparison table may rank projects only after each individual estimate is complete.
4. Select one primary size unit for each project. Use UCP when the material is organized around actors and use cases but lacks field-level detail. Use NESMA/IFPUG when ILF, EIF, EI, EO, and EQ evidence is available. Use COSMIC when functional processes expose Entry, Exit, Read, and Write movements. Other methods may be cross-checks; never add different units together.
5. Extract a closed functional-process list. Each record needs actor/source, trigger, business outcome, main and material alternate paths, data interaction, acceptance evidence, source citation, and confidence. Count user-visible functions, scheduled jobs, APIs, files, and integrations only when they are inside the selected system boundary.
6. Calculate `US`, the unadjusted primary size, with the approved deterministic table. Preserve the item-level ledger and show any low-confidence or excluded items. Use `AS = US × CF` for the uncertainty-adjusted size so raw and adjusted size cannot be confused.
7. Score `C` from design evidence across `L/W/D/A/I/Q/O` on 0-5 anchors. Unknown evidence stays unknown and produces a follow-up question or an explicitly conservative assumption; it is never silently scored as zero. Apply one approved project-type weight vector and show the weighted calculation.
8. Assess `D` only when team, platform, reuse, quality, delivery, scope, and platform-boundary evidence exists. Match requirements to a versioned capability/asset catalogue. Do not infer a coefficient from a marketing statement or let the model write coefficients.
9. Assess `CF` from project stage and an evidence-backed uncertainty register. The model may find unresolved interfaces, acceptance gaps, scope signals, and stale documents; a named owner chooses the approved stage interval and optimistic/conservative scenario.
10. Assess `V` only from normalized historical data or an explicitly labeled external benchmark. Prefer transparent analogy or robust statistical models with time-based holdout validation. If data is insufficient, return a baseline range and mark `V` provisional.
11. Run validation gates. Every item must have a source citation or an explicit assumption; no evidence may be charged in both `C` and `CF`; formula outputs must be reproducible; unknowns, exclusions, model/rule versions, human edits, and approver must be recorded.
12. Report each result as a range with confidence, not a single authoritative number. Separate `US`, `AS`, `C`, `D`, `CF`, and `V`; explain the top cost drivers and the next evidence needed to narrow the range.

## Output Contract

Return, in order:

1. Applicability gate and excluded scope.
2. Input boundary and maturity assessment.
3. Method selection and rejected alternatives.
4. Functional-process ledger and `US` calculation.
5. Complexity evidence and weighted `C` calculation.
6. `D`, `CF`, and `V` status, including unknowns and assumptions.
7. Range calculation using `AS = US × CF` and the approved cost formula.
8. Risks, validation checks, confidence, and explicit human approval points.

Do not modify source requirements or design documents while estimating. Keep generated ledgers and reports separate from source files unless the user explicitly requests an article or report update.
