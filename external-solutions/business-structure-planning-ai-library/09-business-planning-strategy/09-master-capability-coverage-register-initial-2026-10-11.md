# Master Capability Coverage Register — Initial Baseline
**Updated:** 2026-10-11  
**Purpose:** Track whether the universal business-planning system has the required capabilities, evidence, owners, and validation. This is a living register; “specified” never means “tested.”

## Status legend
- **Specified** — instructions or content explicitly describe the capability.
- **Partial** — some coverage exists but important parts are absent.
- **Unverified** — the capability is claimed or suggested but underlying artifact/behavior has not been inspected.
- **Gap** — no sufficient implementation evidence identified yet.
- **Not tested** — no runtime verification performed.
- **Priority P0** — foundational blocker; **P1** — high value; **P2** — conditional/next wave.

## Initial coverage register

| ID | Capability requirement | Current source evidence | Coverage grade | Critical gap / risk | Validation method | Priority | Status |
|---|---|---|---|---|---|---|---|
| GOV-01 | Define decision, audience, scope, authority and deliverables | Peter orchestrator + stage gates; Musengimana SKILL.md | Specified | Need canonical schema and consistent state labels across systems | Missing-field and valid-intake fixtures | P0 | Not tested |
| GOV-02 | Keep client facts, sourced facts, assumptions and decisions distinct | Musengimana SKILL.md; Nivy research-agent spec | Specified | Cross-document IDs and change propagation not proven | Trace one assumption through plan/model/tasks | P0 | Not tested |
| GOV-03 | Maintain versioning, decision log, change log and provenance | Nivy agent spec; Peter release/evidence gates | Partial | One shared record format and durable references needed | Inspect all relevant schemas; run traceability fixture | P0 | Partially specified |
| RES-01 | Build research plan with sources, dates, confidence and counterevidence | Musengimana research rules; Peter claim/evidence gate; Nivy research agent | Specified | Source freshness/corroboration runtime behavior unknown | Research fixture with conflicting/stale sources | P0 | Not tested |
| RES-02 | Estimate TAM/SAM/SOM and bottom-up demand | Canonical outline; candidate plan maps | Partial | Method and arithmetic validation not yet audited in source files | Recompute sample market-sizing worksheet | P1 | Static review pending |
| RES-03 | Competitor, pricing and customer evidence | Outline and Nivy research-agent contract | Partial | Competitor sampling methodology and citation coverage not standardized | Test a defined geography/ICP against primary sources | P1 | Not tested |
| STR-01 | SWOT, PESTLE, Five Forces, TOWS and strategic options | Outline; Peter orchestrator stage gate | Specified | Need evidence links and decision rules, not checklist-only prose | Review one strategy case with evidence/countercase | P1 | Not tested |
| BM-01 | Model canvas, value proposition, segments, channels, revenue and costs | Canonical outline; Peter model-design gate | Specified | Need one machine-readable business-model contract | Schema validation + archetype examples | P0 | Not tested |
| BM-02 | Test demand and define pivot/kill/scale gates | Outline and orchestrator principles | Partial | Standard experiments, sample sizes, thresholds not consolidated | Design and assess 3 test cards | P1 | Gap in standardization |
| GTM-01 | Marketing strategy and channel-specific plan | Outline and Nivy service/agency material | Partial | Need consistent budget, owner, attribution, CAC and KPI definitions | Check plan against channel checklist | P1 | Static review pending |
| GTM-02 | Sales pipeline, CRM stages, forecasting and follow-up | Nivy Company OS and business-model outline | Partial | No single business-plan handoff schema located in this wave | Map stages, definitions, and conversion formulas | P1 | Not tested |
| OPS-01 | Delivery process, capacity, quality, SOP and SLA | Canonical outline; company OS materials | Partial | Need archetype-specific capacity model and QA acceptance criteria | Walkthrough of service and manufacturing examples | P1 | Static review pending |
| ORG-01 | Roles, RACI, hiring sequence and capacity cost | Nivy operations/hiring material; canonical outline | Partial | Must link role costs to forecast and milestones | Trace role plan into payroll/cash model | P1 | Not tested |
| TECH-01 | Technology architecture, integration, automation and fallback | Nivy AIOS research catalog | Partial | No unified plan-system architecture/decision record yet | Dependency and failure-mode review | P1 | Not tested |
| AI-01 | AI governance, human approvals, privacy and auditability | Nivy agent spec uses default-deny/provenance principles | Partial | Needs end-to-end business-plan policy and vendor/data controls | Threat-model and permission tests | P1 | Not tested |
| LEG-01 | Jurisdiction, licenses, tax, contracts and compliance obligations | Canonical outline; Musengimana jurisdiction rules | Partial | Country-specific legal/tax findings need qualified source and review | UAE/India checklist against official sources and reviewer | P0 | Not tested |
| INT-01 | International entry, localization, FX and cross-border risks | Outline; Nivy financial notes; Peter international-entry overlay | Partial | Nivy guidance mixes jurisdictions and unsourced recommendations | Country-specific market-entry and FX scenario review | P1 | Not tested |
| FIN-01 | Executable integrated P&L, balance sheet and cash flow | Musengimana describes BDC workbook engine; Nivy files are narrative | Unverified | No Nivy executable model inspected; third-party workbook license constraint | Open safe copy, recalculate, reconcile statements | P0 | Not tested |
| FIN-02 | Revenue drivers and direct/indirect cost model | Nivy unit-economics narrative; Musengimana model map referenced | Partial | Nivy sample benchmarks lack dated citations; full model map not yet inspected | Source each input and reconcile with formula workbook | P0 | Static review pending |
| FIN-03 | Unit economics: gross/contribution margin, CAC, LTV, payback, churn | Nivy unit-economics guidance | Partial | Definitions differ by business model; CAC figures not sourced in inspected file | Build formula definitions and example cases | P1 | Not tested |
| FIN-04 | Base/upside/downside cases, sensitivity and break-even | Musengimana specifies scenarios; Peter requires stress tests | Specified | Actual workbook and stress results not run | Run controlled scenario fixtures and independent recalculation | P0 | Not tested |
| FIN-05 | Formula integrity, source log, model audit and narrative reconciliation | Musengimana scripts are named; Peter finance/release gates | Specified by design | Scripts not run; third-party template license exception | Test copies; audit formulas; compare outputs and narrative | P0 | Not tested |
| FIN-06 | Forecast-to-actual, variance and reforecast workflow | Nivy dashboard/review guidance | Partial | No standard variance taxonomy and trigger-to-action contract | Simulate monthly variance and reforecast | P1 | Not tested |
| RISK-01 | Risk register with owner, likelihood, impact, control and contingency | Canonical outline; Nivy risk notes; Peter challenge gate | Partial | Shared scoring scales and residual-risk acceptance not standardized | Test risk register with escalations | P1 | Static review pending |
| RISK-02 | Early-warning indicators and threshold-based response | Canonical outline and previous gap analysis | Partial | Need indicator definitions, source, thresholds, owner, escalation and action | Inject threshold breach in tabletop test | P1 | Not tested |
| EXEC-01 | Milestones, work breakdown, owners, budgets and dependencies | Canonical outline; Nivy AIOS project/task concepts | Partial | Need common IDs connecting strategy → budget → tasks → KPIs | Trace a milestone to cost, owner, and outcome | P0 | Not tested |
| EXEC-02 | KPI tree, dashboards, review cadence and corrective action | Nivy financial dashboards and Company OS materials | Partial | Definitions/source of truth and review-to-decision loop not unified | Dashboard metric reconciliation and mock review | P1 | Not tested |
| PKG-01 | Audience-specific output (bank, investor, grant, owner, partner) | Peter stage-gate audience routes; Musengimana Word/Excel output | Specified | Audience requirements need checklists and local forms | Render sample outputs for 3 audiences | P1 | Not tested |
| QA-01 | Final QA, rendering, security/privacy, release approval | Peter release gate; Musengimana validation scripts | Specified by design | Scripts and release gate not executed; human authority remains essential | Run validators on a non-sensitive fixture | P0 | Not tested |
| ARCH-01 | Adapt to service, manufacturing, trading, SaaS, franchise and marketplace | Canonical blueprint includes archetype modules | Partial | Each module needs required inputs, formulas, gates and examples | Coverage test for each archetype | P1 | Blueprint only |
| LIC-01 | Source license, third-party asset and dependency inventory | Two candidate licenses inspected; BDC exception identified | Partial | Full transitive dependencies and all assets not audited | Generate per-repo SBOM/license manifest and review notices | P0 | Static review pending |
| INTG-01 | Single orchestration contract linking evidence, plan, model, risks, tasks and release | Peter provides strong gates; Musengimana provides deliverable workflow; Nivy has agent specs | Partial | No unified schema/event contract proven | Build sample end-to-end record and validate all references | P0 | Gap in integration |

## Initial priority order
1. **P0 foundation:** intake/data contract, assumption and evidence IDs, jurisdiction/compliance, executable integrated finance, formula/model QA, task-budget traceability, licensing.
2. **P1 decision quality:** market validation, strategy options, business-model tests, GTM metrics, capacity/quality, risk indicators, forecast-to-actual.
3. **Archetype overlays:** develop one validated profile at a time rather than assuming one generic template fits all.
4. **Runtime testing comes after static review:** test copies only, preserve originals, log versions and outcomes.

## Important interpretation
This is an **initial capability register**, not a certification that any system is complete. “Specified” means a file describes a method; it does not mean the implementation runs, the financial math is correct, or the result is suitable for a real investment/credit decision. The third-party BDC workbook is excluded from the Musengimana repository's MIT license according to its NOTICE; obtain and follow applicable terms before reuse.
