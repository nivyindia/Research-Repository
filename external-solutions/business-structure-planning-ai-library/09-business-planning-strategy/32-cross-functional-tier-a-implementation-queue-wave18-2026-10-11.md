# Wave 18 — Cross-Functional Tier-A Implementation Queue — 2026-10-11

## Purpose
Resume the canonical roadmap after the A001 supporting-work checkpoint. This queue derives from stable G01–G75 IDs; it does not replace the master gap register and does not mark gaps closed.

## Baseline evidence
- Main roadmap: `04-business-plan-intelligence-execution-implementation-roadmap-2026-10.md`.
- Stable gap register: `03-international-business-plan-gap-analysis-2026-10.md`.
- Normalized matrix: `26-normalized-requirement-to-resource-matrix-wave13-2026-10-11.md`.
- Cross-functional resource map: `25-cross-functional-resource-to-gap-mapping-wave12-2026-10-11.md`.
- External builder candidates remain Pre-Qualification until exact files, license, dependencies, security, runtime and reproducibility are checked.
- Finance remains blocked: Year-1 narrative revenue is $68,500 while the quarterly P&L rows sum to $190,000. Neither is approved until monthly drivers reconcile.
- Direct execution of the committed A001 Code-node JavaScript passed 11/11 expected cases; this is not live n8n evidence. GitHub Actions CI remains unconfirmed.

## Operating rule
`REUSE → MAP → VERIFY → INTEGRATE → TEST → BUILD ONLY WHAT IS MISSING`.
Catalogs and specifications are candidates, not proof of working capability.

## Prioritized cross-functional queue

| Queue | Stable gap IDs | Workstream | Acceptance evidence |
|---|---|---|---|
| Q0 | G33, G34, G38, G69, G73 | Evidence, assumptions and data quality | Claim-to-source links; dates/URLs/geography; assumption owner/status/confidence; freshness checks; reproducible source snapshot; missing-data flags |
| Q1 | G04, G05, G06, G07, G08, G09, G40, G55, G57 | Market intelligence, sizing, competitor/pricing and localization | Structured research; top-down/bottom-up TAM/SAM/SOM reconciliation; normalized competitor/pricing records; country-specific evidence and contradiction handling |
| Q2 | G17, G18, G19, G20, G21, G24, G37 | Financial model and unit economics | Workbook/formula inventory; monthly revenue/cost/cash bridge; reconciled baseline; margin/CAC/LTV/payback; scenarios; independent arithmetic checks |
| Q3 | G10, G11, G12, G13, G14, G15, G16, G28, G43, G45, G54 | GTM-to-delivery operating model | Demand-to-sales-to-capacity-to-workforce-to-cash dependencies; roles, SLA, handoffs and hiring triggers tied to forecast |
| Q4 | G23, G25, G26, G27, G31, G32, G60, G65, G74, G75 | Country, compliance, privacy, architecture and vendor risk | Dated country source register; professional review flags; data map, permissions, vendor dependency and entity/contract/money-flow assumptions |
| Q5 | G36, G39, G41, G44, G51, G52, G64, G68 | Independent QA, customer validation, approvals and execution conversion | Separate evaluator, customer evidence gates, explicit approvals, pass/fail criteria, traceable plan-to-task conversion |
| Q6 | G46, G47, G48, G49, G50, G66, G67, G71 | Monitoring and learning loop | KPI dictionary, actual-vs-plan, rolling forecast, cost budget, early-warning thresholds, corrective-action owner and versioned learning log |

## Dependency rules
1. Research claims and assumptions feed sizing, offer/pricing and country selection.
2. Sales and marketing demand must be constrained by delivery capacity, hiring ramp and quality.
3. Pricing and scope feed delivery costs, contribution margin, collections and working capital.
4. Country/entity decisions affect tax, contracts, privacy, payments, FX and hiring; translation alone is not localization.
5. QA, approval and versioning gates apply across all workstreams.
6. Execution conversion requires explicit human approval; monitoring retains actuals and plan-version history.

## Immediate next batch

### Batch A — Evidence and assumptions foundation (Q0)
1. Inspect exact source/evidence schemas, source catalogs, assumption ledger and evaluation suite; record file/version and overlaps.
2. Define a shared record linking claim, assumption, source URL, publication/access dates, geography, methodology, evidence grade, owner, confidence, review date and decision impact.
3. Define fail-closed rules for unsupported claims, stale sources, unresolved contradictions and unowned assumptions.
4. Create positive/negative fixtures and identify the existing runner.
5. Integrate the shared contract into research, financial model and plan output only after tests.

### Batch B — Financial reconciliation in parallel (Q2)
1. Inspect workbooks with an XLSX-capable parser: sheets, formulas, hidden sheets, named ranges, external links and calculation mode.
2. Reconcile monthly client cohorts, recognized revenue, invoices, collections, delivery costs, commissions, OPEX and cash runway.
3. Keep the approved baseline blocked until the revenue discrepancy is explained and independently checked.

## Stop conditions
- No tool/runtime activation without owner, version, authorization, health check and test evidence.
- No legal/tax assertion promoted without dated authoritative sources and qualified review where needed.
- No financial base case approved while revenue/cash bridges disagree.
- No material market claim treated as fact without traceable evidence.
- No source or duplicate deleted before provenance, license and overlap comparison.

## Status
Cross-functional queue established; gaps are not marked implemented or closed. Next gate: qualify the evidence/assumption assets and inspect the financial workbooks, then integrate and test shared contracts.
