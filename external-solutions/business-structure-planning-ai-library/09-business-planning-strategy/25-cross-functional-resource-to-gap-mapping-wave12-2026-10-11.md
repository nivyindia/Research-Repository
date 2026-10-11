# Cross-Functional Resource-to-Gap Mapping — Wave 12
**Updated:** 2026-10-11  
**Roadmap phase:** Phase 0 — Baseline + resource-to-gap mapping; prepares Phase 1 exact-file qualification  
**Status:** Static repository mapping only. No external asset is approved for reuse, no agent/runtime behavior is verified, and no system integration is claimed.

## 1. Purpose and governing rule

Continue the canonical Business Plan Intelligence & Execution System roadmap; this is a dated evidence delta, not a replacement roadmap.

**REUSE → MAP → VERIFY → INTEGRATE → TEST → BUILD ONLY WHAT IS MISSING.**

The current work must not collapse into a finance-only project. Finance remains a P0 blocker, but sales, marketing, operations/delivery, HR/workforce, customer success, legal/compliance, technology/data, execution, monitoring and international overlays are all required.

## 2. What this pass establishes

Repository search confirms that relevant internal resources already exist across several domains. They are useful discovery/mapping candidates, but the presence of a catalog or framework is not proof that the relevant capability is executable, correctly configured, licensed for the intended use, integrated, or tested.

| Map ID | Business-plan capability | Existing internal candidate(s) | Current evidence/status | Main gap / next verification |
|---|---|---|---|---|
| XMAP-01 | Sales strategy, ICP, prospecting, qualification, opportunity, proposals, closing, forecasting and RevOps | `03-solution-catalogs/91-sales-resource-extraction-and-capability-map.md`; `03-solution-catalogs/90-sales-resource-discovery-catalog.md`; `03-solution-catalogs/92-sales-micro-workflow-gap-and-resource-catalog.md`; `03-solution-catalogs/94-sales-complete-micro-resource-catalog.md` | Broad catalog and capability map present; much is candidate-level | Select canonical source per capability; inspect exact linked assets, versions, license, dependencies, schemas and tests; map sales assumptions to the business-plan model |
| XMAP-02 | Marketing strategy, channel plan, content, SEO, paid media, social, lifecycle, attribution and budget | `02-company-department-models/34-expanded-international-company-capability-catalog.md`; `03-solution-catalogs/18-skill-mining-map.md`; `03-solution-catalogs/23-jarvis-voice-creator-youtube-social-marketing-reuse-catalog-2026-09.md`; `Chats/Claude/International-Marketing-Plan.md` | Taxonomy and some specialist reuse research present; no universal plan-to-budget/attribution contract verified | Locate and inspect marketing skill/source files; create channel-plan schema covering objective, audience, offer, budget, owner, cadence, funnel metric, attribution, evidence and stop/scale threshold |
| XMAP-03 | Delivery/operations: service design, process, capacity, SLA, quality, suppliers, procurement and fulfillment | `02-company-department-models/34-expanded-international-company-capability-catalog.md`; `03-solution-catalogs/35-business-process-value-stream-reuse-catalog-2026-09.md`; `06-adoption-implementation/33-master-implementation-roadmap.md` | Capability taxonomy and end-to-end value-stream catalog present; process entries are discovery candidates | Map each operating assumption to process, role, capacity unit, cycle time, utilization, quality threshold, supplier dependency and cost driver; verify archetype-specific models |
| XMAP-04 | HR/workforce plan: organization, roles, hiring triggers, compensation, skills, capacity and people cost | `06-adoption-implementation/68-employee-workforce-adoption-map.md`; `02-company-department-models/34-expanded-international-company-capability-catalog.md`; `00-navigation-governance/02-capability-map.md` | Workforce adoption map specifies reusable layers and tests; implementation not demonstrated | Link roles and hiring triggers to demand/capacity and monthly payroll/contractor costs; inspect actual candidate implementations and RBAC/data controls |
| XMAP-05 | Customer success, support, onboarding, retention, renewal, expansion and customer feedback | `03-solution-catalogs/18-skill-mining-map.md`; `03-solution-catalogs/35-business-process-value-stream-reuse-catalog-2026-09.md`; sales capability map in `03-solution-catalogs/91-sales-resource-extraction-and-capability-map.md` | Skill-family and value-stream discovery references present; business-plan handoff is partial | Define lifecycle, service levels, onboarding milestones, retention/churn, renewal, expansion, customer health, escalation and feedback-to-plan data contracts |
| XMAP-06 | Evidence, assumptions, confidence, decisions, reproducibility and audit trail | `09-business-planning-strategy/03-international-business-plan-gap-analysis-2026-10.md`; `09-business-planning-strategy/07-canonical-international-business-plan-blueprint-2026-10-11.md`; `03-solution-catalogs/18-skill-mining-map.md` | Required concept is specified in planning documents; common operational schema is not yet demonstrated end-to-end | Define stable IDs and schemas for source, claim, assumption, confidence, as-of date, jurisdiction, owner, counterevidence, decision and version; test claim-to-source traceability |
| XMAP-07 | Legal, tax, privacy, contracts, sector regulation and country localization | `09-business-planning-strategy/07-canonical-international-business-plan-blueprint-2026-10-11.md`; `09-business-planning-strategy/03-international-business-plan-gap-analysis-2026-10.md`; `03-solution-catalogs/18-skill-mining-map.md` | Checklist/reference coverage; country-specific verified determinations not established | Create jurisdiction overlays with official source/date, applicability, reviewer, unresolved question and escalation; qualified review required for consequential legal/tax advice |
| XMAP-08 | Technology, data, AI governance, integrations, security, resilience and tool cost | `00-navigation-governance/02-capability-map.md`; `06-adoption-implementation/77-master-automation-and-implementation-registry.md`; `06-adoption-implementation/84-automation-test-and-evaluation-suite.md`; `03-solution-catalogs/18-skill-mining-map.md` | Registry/test-suite references exist; a business-plan-specific integration contract and test evidence are not established | Inspect schemas and evaluation cases; define permissions, data boundaries, human approvals, failure recovery, cost budgets and audit events |
| XMAP-09 | Execution conversion: approved plan to departments, initiatives, projects, tasks, owners, budgets and dependencies | `03-solution-catalogs/35-business-process-value-stream-reuse-catalog-2026-09.md`; `06-adoption-implementation/33-master-implementation-roadmap.md`; `06-adoption-implementation/77-master-automation-and-implementation-registry.md` | Process and implementation catalogs exist; universal plan-to-task workflow remains unverified | Define shared IDs linking objective → initiative → task → owner → budget → KPI; enforce explicit approval before creating or changing consequential work |
| XMAP-10 | Finance, unit economics, scenarios, working capital, tax/FX and actual-vs-plan | `09-business-planning-strategy/14-master-capability-coverage-register-wave5-update-2026-10-11.md`; `15-xlsx-candidate-classification-wave6-2026-10-11.md`; `16-canonical-finance-source-map-and-assumption-audit-wave7-2026-10-11.md`; `18-master-capability-coverage-register-wave7-update-2026-10-11.md`; Waves 8–11 files `19`–`23` | Static audit advanced; integrated workbook/model still blocked and not validated | Preserve existing P0s: workbook binary inspection, $68,500 vs $190,000 Year-1 revenue conflict, source-backed drivers, independent fixtures, qualified review and approval |
| XMAP-11 | Business-type and audience variants | `09-business-planning-strategy/07-canonical-international-business-plan-blueprint-2026-10-11.md`; `Nivy Artisan/International-Business-Plan-Topics.md`; `Nivy Research Data/New Research04-08-26/Business-Plan-for-DM-AI-IT.md` | Universal blueprint plus vertical-specific outline exists; archetype test results not established | Build conditional module rules and test service agency, franchise/service centre, SaaS, manufacturing/trading and cross-border variants; record justified N/A decisions |
| XMAP-12 | Independent QA, release gates, monitoring and learning | `06-adoption-implementation/84-automation-test-and-evaluation-suite.md`; `09-business-planning-strategy/04-business-plan-intelligence-execution-implementation-roadmap-2026-10.md` | QA/release intent specified; universal end-to-end pass evidence absent | Define mandatory checks, severity, evidence artifacts, independent recalculation, failure behavior, human approval, actual-vs-plan review and version history |

## 3. Cross-functional dependencies that must be reconciled

1. **Demand → sales funnel → delivery capacity → workforce → costs/cash:** sales volume cannot be forecast independently of conversion rates, delivery throughput, utilization, hiring triggers, payment terms and cash collection.
2. **Marketing spend → qualified demand → sales outcomes:** budgets need channel-specific targets, attribution definitions, conversion assumptions, time lags and stop/scale thresholds.
3. **Offer/pricing → delivery scope/quality → margin:** pricing must map to scope, labor, software, contractor costs, rework, support, taxes/fees and approval limits.
4. **Customer success → retention/expansion → LTV/cash:** onboarding, churn, renewal timing, support cost and expansion must feed the same forecast assumptions.
5. **Country overlay → go-to-market and operations:** country-specific language, channels, payments, contracts, privacy, hiring and tax assumptions must change the model, not just the currency label.
6. **Approved plan → execution system → actuals:** every initiative needs a stable identifier, owner, budget, KPI, due date, dependency and review rule so actual results can be compared with the original plan.

## 4. Phase 0/1 exit criteria — still open

- [ ] One deduplicated requirement-to-resource matrix with stable gap IDs and exact file paths.
- [ ] Every Tier A/P0 gap has an owner, evidence, acceptance criteria and a reuse candidate or explicit build decision.
- [ ] Candidate asset license, version/commit, dependencies, security and input/output contract are recorded.
- [ ] Duplicate outlines/catalogs are classified without deleting source history.
- [ ] Statuses distinguish discovered, mapped, inspected, license/security checked, adapted, integrated, tested and accepted.
- [ ] Sales, marketing, operations, HR, customer success, legal, technology, finance and execution coverage are all represented.
- [ ] No capability is called tested or production-ready without reproducible test evidence.

## 5. Next execution sequence

### Next gate A — normalize the matrix
Use the canonical blueprint and 75+ gap analysis as the requirement backbone. Merge existing resource maps/registers without changing stable IDs. Add exact source path, candidate artifact, source/version, license/security status, schema, dependencies, status, evidence, owner, acceptance test and next action.

### Next gate B — exact-file qualification by dependency order
1. Evidence registry + assumption ledger and source provenance.
2. Market research / country profile and localization.
3. Sales + marketing funnel and budget drivers.
4. Delivery capacity + workforce/hiring cost.
5. Customer success, retention and renewal drivers.
6. Integrated finance model and independent calculation fixtures.
7. Independent QA and human approval.
8. Approved-plan-to-task conversion and actual-vs-plan monitoring.

### Next gate C — thin end-to-end slice
Only after the above contracts are defined, use one low-risk service-business example to trace intake → evidence → assumptions → strategy → GTM → delivery/staffing → finance → QA → approval → execution tasks. Keep it a test fixture; do not treat it as a released plan.

## 6. Route and continuity record

- **Route change:** none. This is the planned Phase 0 resource-to-gap mapping work, expanding beyond the finance submodule.
- **Why this pass:** prior waves deepened finance auditing while the overall roadmap still requires a cross-functional consolidated capability map.
- **Impact:** adds cross-domain candidates and explicit integration dependencies; does not close any runtime/test gate.
- **Return point:** continue Phase 0 matrix normalization and Phase 1 exact-file qualification; retain the finance model as a parallel P0 blocker, not the sole workstream.
- **Do not do:** bulk-import external repositories, declare catalogs production-ready, build one agent per gap, or overwrite/delete duplicate source material before comparison.

## 7. Acceptance statement

This wave is complete as a **static cross-functional mapping delta only**. Phase 0 is not yet complete; Phase 1 qualification, common schemas, end-to-end integration and pilot testing remain unfinished.
