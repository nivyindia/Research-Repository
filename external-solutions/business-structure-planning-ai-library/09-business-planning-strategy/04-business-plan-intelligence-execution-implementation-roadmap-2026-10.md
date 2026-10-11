# Business Plan Intelligence & Execution System — Implementation Roadmap — 2026-10

## Objective
Build a reusable, evidence-backed system that can create, validate, compare, approve, execute and continuously improve business plans for different industries, business models and countries.

## Operating rule
REUSE -> MAP -> VERIFY -> INTEGRATE -> TEST -> BUILD ONLY WHAT IS MISSING.

Do not import entire repositories or build 70 separate agents just because the gap register contains 70+ capabilities. Cluster related gaps into reusable system components.

## Phase 0 — Establish the baseline
**Deliverables**
- Master gap register with stable IDs, severity, evidence, existing candidate, status, owner and acceptance criteria.
- Resource-to-gap mapping for existing Nivy assets and external candidates.
- Duplicate/overlap map.
- Clear definition of what counts as Covered, Partial, Missing, Verified and Production-ready.

**Exit gate:** Every Tier A gap has an owner and either a reuse candidate or an explicit build decision.

## Phase 1 — Inspect and qualify reusable assets
Inspect priority candidates in this order:
1. Full-plan workflow and output generation.
2. Market research and source provenance.
3. Country/localization and compliance.
4. Financial model, unit economics and cash-flow logic.
5. Independent QA and validation.
6. GTM/sales/marketing economics.
7. Plan-to-project/task conversion.

For each asset, record exact path, source URL, license, commit/version, dependencies, input/output schema, test status, security notes, overlaps and adaptation effort.

**Exit gate:** No asset is marked reusable until its exact files, license and basic behavior have been reviewed.

## Phase 2 — Define the common data model
Create structured schemas for:
- Business plan and version
- Country profile
- Market and customer segment
- Competitor and pricing offer
- Product/service offer
- Assumption and evidence/source
- Sales/marketing funnel
- Delivery capacity and workforce
- Financial drivers, statements and scenarios
- Risk and early-warning indicator
- KPI, initiative, project, task and owner
- Decision, approval and change log

**Exit gate:** All modules exchange structured data instead of passing only free-form prose.

## Phase 3 — Build the decision-grade core
Prioritize these components:
1. Evidence registry + claim-to-source traceability.
2. Assumption register + confidence/status.
3. Country localization profiles.
4. Integrated sales -> delivery -> staffing -> finance model.
5. Unit economics, working capital and scenario engine.
6. Independent plan and financial QA.
7. Customer-validation workflow and stage gates.

**Exit gate:** A sample plan's major claims, financial outputs and recommendations can be traced and checked.

## Phase 4 — Add international expansion intelligence
Add country comparison and market-entry decision support:
- Market attractiveness and demand evidence
- Local competitors and pricing
- Currency and FX exposure
- Tax and regulatory checklist
- Entity/contracting/payment assumptions
- Hiring and contractor constraints
- Privacy/data-transfer considerations
- Language, culture and channel adaptation
- Country concentration and geopolitical risk where relevant

**Exit gate:** The same business model can produce distinct, sourced country variants; changing the currency symbol alone does not count as localization.

## Phase 5 — Convert approved plans into execution
On explicit human approval, convert the plan into:
- Departments and roles
- Budgets and hiring triggers
- KPIs/OKRs and metric definitions
- SOPs and quality controls
- Initiatives, projects, tasks, owners and dependencies
- CRM/sales stages and marketing experiments
- Review cadence and approval rights

**Exit gate:** An approved plan creates actionable, assigned work without silently taking consequential actions.

## Phase 6 — Monitoring and learning loop
Implement:
- Actual-vs-plan reporting
- Variance analysis and corrective actions
- Rolling forecast/replanning
- Early-warning thresholds for cash, CAC, conversion, margin, retention and delivery quality
- Regulatory/competitor/market change monitoring
- Decision and plan-version history
- Post-launch experiment and learning records

**Exit gate:** The plan can be updated from actual performance with a traceable explanation of what changed and why.

## Phase 7 — Pilot, evaluate and release
Use a small, diverse test set:
- Local service business
- Digital agency
- Franchise/service-centre model
- SaaS/startup
- Manufacturing/trading business
- One cross-border expansion case

Evaluate factual accuracy, source quality, localization, financial consistency, operational feasibility, usefulness of decisions, completeness, runtime/cost and failure recovery.

**Release gate:** Critical checks pass, high-risk limitations are visible, and human review is required for legal/tax/investment-sensitive conclusions.

## Recommended status labels
- Discovered
- Mapped
- License/security checked
- Adapted
- Tested
- Accepted
- Integrated
- Monitored
- Rejected / Duplicate

## Initial priority order
1. Baseline + resource-to-gap mapping
2. Evidence/provenance + assumption register
3. Country localization profiles
4. Integrated operating/financial model
5. Independent QA
6. Customer validation/stage gates
7. Plan-to-Company-OS conversion
8. Actual-vs-plan and early-warning loop
9. Additional context-dependent modules

## Definition of done
The system is ready for a controlled pilot when it can:
- Create a complete plan from structured intake.
- Clearly separate verified facts from assumptions.
- Link material claims to dated sources.
- Compare at least two markets or strategic options.
- Reconcile sales, delivery capacity, staffing, pricing and financial forecasts.
- Produce downside/base/upside scenarios and cash runway.
- Flag missing or uncertain country-specific legal/tax/privacy inputs.
- Pass independent QA or clearly report failures.
- Require approval before execution changes.
- Convert the approved plan into assigned work.
- Track actual performance and preserve plan/version/decision history.

## Key decision
Do not start by building a large multi-agent system. First create the baseline map and common schemas, then integrate the highest-value reusable components. This minimizes duplication and makes later automation testable.


---

## Audit checkpoint — scope completeness and direction review — 2026-10-11

### Verdict

**The intended scope is broad enough on paper, but implementation is not complete.** The canonical blueprint explicitly includes sales, marketing, customer success, delivery/operations, HR/workforce, technology/data/AI, legal/tax, finance/funding, risk/resilience, implementation, KPIs, and appendices. The gap analysis labels many of these as **Partial**, not complete. The work so far is still mostly blueprint/catalog/static review; it is not yet a tested, integrated agent system.

This is a checkpoint against the original goal: a reusable system that can generate decision-grade plans for different business types and countries, then convert approved plans into operating workflows. Financial-model auditing is one submodule, not the main objective.

### Required plan modules — scope and actual status

| Module | Required in-depth coverage | Current evidence/status | Remaining work |
|---|---|---|---|
| Intake and plan control | Audience/decision, business stage/type, geography, jurisdiction, currency, constraints, data consent, deliverables, approval authority | Blueprint specified | Convert into structured intake schema, required/conditional questions, validation and test fixtures |
| Research and market intelligence | Industry, demand, TAM/SAM/SOM, customer interviews, ICP/personas, buying process, competitor map/pricing, alternatives, source freshness, counterevidence | Blueprint + resource catalogs; gap analysis says partial | Inspect exact source assets, define research protocol and evidence scoring; validate a real sample |
| Strategy and business model | SWOT/TOWS, PESTLE, Five Forces when useful, value chain, differentiation, strategic options, business model, assumptions, experiments, pivot/kill/scale gates | Specified; some standardization gaps remain | Create reusable decision templates, measurable experiment cards and review criteria |
| **Sales plan** | Sales motion; ICP and territory; lead-source/channel strategy; funnel stages and definitions; qualification; outreach/cadence; discovery/demo/proposal/negotiation/close; conversion rates; sales-cycle length; quota; rep capacity/ramp; pipeline coverage; CRM; forecast; commissions; partner/channel sales; retention/expansion | Present in blueprint and mapped to GTM skills, but marked **Partial** in gap analysis | Build a complete sales-plan schema and formulas; connect pipeline assumptions to staffing, revenue, cash collection and forecast; test outbound, inbound, channel and enterprise/PLG variants |
| **Marketing plan** | Positioning/messaging; segments; objectives; funnel; channel-by-channel strategy (SEO, content, social, paid, email, PR, events, referrals, partners, marketplaces as relevant); budget; calendar; owner; conversion event; attribution; CAC/ROAS/payback; creative/testing plan; analytics; privacy/consent; channel-specific launch and optimization | Present in blueprint and external candidate map; marked **Partial** | Create a detailed channel plan template and metrics dictionary; model budget → leads → qualified leads → customers → revenue; include experiments, attribution limits and stop/scale rules |
| **GTM and market entry** | Launch sequence, offer, pricing, sales motion, channels, local entry mode, partner selection, localization, country sequencing and readiness gates | Specified but partial | Integrate country choice with competitive evidence, compliance, unit economics and launch milestones |
| **Customer success and lifecycle** | Onboarding, activation, adoption, service/support, SLA, complaints/escalations, retention, churn, renewal, expansion, NPS/CSAT where meaningful, customer profitability and feedback loop | Blueprint specified | Create lifecycle workflows and metrics by archetype; link churn/retention to revenue, delivery load and cash |
| **Operations and delivery plan** | Customer-to-cash/procure-to-pay maps; delivery workflow; capacity/utilization/throughput; service levels; quality/acceptance; staffing shifts; vendors/suppliers; inventory/logistics where relevant; support/escalations; facilities/equipment; dependencies; business continuity and disaster recovery | Blueprint specified; gap analysis marks core delivery operations **Partial** and continuity as a unified layer missing | Build archetype-specific operating models, capacity equations, QA/SLA controls, bottleneck/dependency analysis, recovery and contingency plans |
| **Organization, HR and training** | Org chart, role charters, RACI, skills, hiring sequence/triggers, cost, ramp/productivity, compensation, onboarding/training, performance, labor/contractor classification, succession and workforce capacity | Blueprint specified; partial | Link demand and workload to headcount and payroll; create hiring-trigger model and role/training packs |
| **Product/service and technology** | Scope, deliverables/exclusions, roadmap, build/buy/reuse, architecture, integrations, security, data, IP, support, uptime/maintenance and total cost of ownership | Blueprint specified; partial | Add archetype-specific product/service modules and technology dependency/failure analysis |
| **Finance and funding** | Driver-based revenue/cost, integrated P&L/balance sheet/cash flow, working capital, CAC/LTV/contribution/payback, pricing/margin floors, runway, break-even, base/downside/upside, sensitivity, funding ask/use of funds, repayment/dilution as relevant | Narrative documents and finance audit exist; executable integrated model is **Blocked/unverified** | Resolve documented conflicting assumptions, source inputs, identify/reuse or approve building a model, independently recalculate and test scenarios |
| **Legal, tax, regulatory and cross-border** | Entity, ownership, permits, contracts, IP, employment, tax/VAT/GST, privacy, cybersecurity, payments, data transfer, import/export, sector rules, permanent establishment/transfer pricing where relevant | Blueprint specified; country-level evidence and professional validation incomplete | Create jurisdiction/sector overlays using primary sources, dated citations and qualified review; mark out-of-scope issues clearly |
| **Risk, resilience and governance** | Risk register, likelihood/impact, controls, residual risk, owner, triggers, contingency, pre-mortem, fraud/cyber/vendor/concentration risks, BCP/DR, approvals and escalation | Specified; second-order gaps remain | Standardize scoring and triggers; run tabletop tests and require explicit risk acceptance |
| **Execution and monitoring** | 30/60/90-day and annual plans; milestones; work breakdown; owners; budget; dependencies; KPIs/OKRs; SOPs; project/task conversion; actual-vs-plan; variance actions; rolling forecasts; learning/version history | Roadmap specified; integration not proven | Define shared IDs/data contracts and build an approved-plan-to-task workflow with audit logs and human approval |
| **Outputs and appendices** | Owner/operator plan, lender/investor/grant/partner variants, pitch and implementation pack, sources, assumptions, calculations, evidence, licenses, legal-review flags and reconciliation | Blueprint specified; release gates not run | Generate sample outputs for different audiences, cross-check consistency and test final rendering/accessibility |
| **Business-type overlays** | Service/agency, retail/trading, manufacturing, SaaS/software, marketplace, franchise/service-centre, nonprofit/impact, asset-heavy, regulated, multi-location and cross-border models | Some archetypes explicitly listed; coverage tests not run for all | Add conditional modules and pass/fail fixtures for each archetype; record N/A with rationale instead of silently omitting sections |

### Library audit: what we can and cannot claim

Existing catalogs already point to reusable candidates for full-plan generation, strategy/consulting, sales and marketing skills, finance, workflows, and company execution. Examples include the external full-plan builders and skill collections cataloged in `02-external-business-plan-agents-skills-and-planning-systems-2026-10.md`, and the existing Internet Reuse / AI Agent Skills / Business Builder catalogs referenced there.

However, **a catalog entry is not proof that the capability is available, licensed, compatible, correct, or integrated**. Current qualification is uneven:
- Selected files from two business-plan repositories and a release-gate resource have been statically inspected.
- License/dependency/security checks for all exact assets are not complete.
- No end-to-end universal plan-generation run has been demonstrated.
- No end-to-end sales/marketing/operations-to-finance reconciliation test has been demonstrated.
- No archetype test suite or release-ready evidence bundle exists yet.
- Finance documents are mostly narrative/static; the Nivy integrated executable model remains unverified.

### Correct phase/status at this checkpoint

| Phase | Honest status | Exit proof still required |
|---|---|---|
| 0 — Baseline, capability map, reuse/gap map | **In progress / partially documented** | One deduplicated canonical register with every requirement, source asset, owner, priority, status and acceptance test |
| 1 — Exact asset qualification | **In progress; not complete** | Exact file/commit, license, dependencies, security, schema, overlap, test and reuse decision for each selected asset |
| 2 — Common data model | **Specified conceptually; not implemented/validated** | Versioned schemas and valid/invalid fixtures; linked IDs across research, assumptions, sales, operations, finance, risk and tasks |
| 3 — Decision-grade core | **Not yet proven end-to-end** | Working evidence/assumption registries, integrated driver model, independent QA and stage gates |
| 4 — International overlays | **Specified; not validated across countries** | At least two country variants with sourced, materially distinct legal/market/tax/operating assumptions |
| 5 — Plan-to-execution | **Architecture described; integration not proven** | Approved plan creates departments, budgets, CRM/marketing experiments, SOPs and assigned tasks without unapproved actions |
| 6 — Monitoring/learning | **Specified; not demonstrated** | Simulated actuals trigger reconciled variance analysis, alerts, corrective actions and versioned reforecast |
| 7 — Pilot/release | **Not started / blocked by prior gates** | Passing diverse archetype fixtures, test logs, issue register, human approvals and release evidence |

### Mandatory next sequence — do not drift into a finance-only project

1. **Freeze scope and make one deduplicated requirement-to-library matrix** from the canonical blueprint, gap analysis, Nivy reuse catalogs and external candidates. Include every module above and assign stable IDs.
2. **Inspect existing sales, marketing, operations, HR, customer-success and execution libraries first**; map exact reusable files to requirements before adding new assets.
3. **Complete exact-file qualification** for highest-value candidates (license, version/commit, dependencies, security, inputs/outputs, overlap and testability).
4. **Define the shared data contracts** for evidence, assumptions, ICP/competitors, sales funnel, channel budget, delivery capacity, staffing, financial drivers, risks, KPIs and execution tasks.
5. **Integrate one thin end-to-end vertical slice**: intake → sourced research → strategy → sales + marketing plan → operations/capacity → staffing → financial scenarios → risk/QA → human approval → implementation tasks.
6. **Test multiple archetypes** (agency/service, trading, franchise/service centre, SaaS, manufacturing) and at least one country-localization contrast. Record failures; do not call a module complete just because a template exists.
7. **Keep the finance audit as a submodule** that blocks financial claims when necessary, but does not replace sales/marketing/operations or the universal-system objective.

### Acceptance rule for every requirement

Every requirement must have: stable ID; applicability rule; required inputs; method/formula where applicable; output schema; source/library candidates; license/security decision; owner; dependencies; evidence and confidence; validation test; acceptance criteria; status; and a reason if not applicable. “Covered” is reserved for tested behavior with recorded evidence, not a heading or a document.


---

## Cross-functional mapping continuation — Wave 12 — 2026-10-11

The next dated cross-functional resource-to-gap mapping delta is recorded here:
[Wave 12 — Cross-Functional Resource-to-Gap Mapping](25-cross-functional-resource-to-gap-mapping-wave12-2026-10-11.md).

**What changed:** No roadmap phase or priority order changed. This pass extends Phase 0 mapping beyond the finance submodule and makes Sales, Marketing, Operations/Delivery, HR/Workforce, Customer Success, Evidence/Governance, Legal/Localization, Technology/Data, Execution, Finance, Archetypes and QA visible in one dependency-aware map.

**Current status:** Static mapping only. Phase 0 exit criteria remain open; no candidate is newly marked tested, integrated, or production-ready.

**Return point:** Continue normalizing one deduplicated requirement-to-resource matrix, then qualify exact files/licenses/dependencies/schemas and tests in the roadmap's Phase 1 order. Keep the financial model's P0 validation blockers active in parallel; do not let finance-only auditing replace the full roadmap.


---

## Requirement matrix normalization — Wave 13 — 2026-10-11

The existing 75 stable gap IDs have been normalized into a single requirement-to-resource working matrix:
[Wave 13 — Normalized Requirement-to-Resource Matrix](26-normalized-requirement-to-resource-matrix-wave13-2026-10-11.md).

**Result:** 75 source gap rows captured with original capability/state/priority retained, candidate internal source paths, and an explicit next-verification requirement. This is mapping evidence only; no gap was upgraded to tested or production-ready.

**Next gate:** Reconcile the matrix against the initial and dated capability registers; then qualify exact Tier A/P0 assets (version, license/security, dependencies, input/output schema, test evidence, owner and acceptance criteria). Preserve the full cross-functional scope and keep finance validation as a parallel P0 workstream.


---

## Research/evidence asset qualification — Wave 14 — 2026-10-11

Static exact-file qualification of A001 Market Research Agent is recorded in [Wave 14 — Market Research Agent Contract Audit](27-market-research-agent-contract-audit-wave14-2026-10-11.md).

**Finding:** The agent definition/prompt are well specified, but SK001 is still `planned`, SK002 is also `planned`, the three allowed tools are registered as `planned`, and the status record says `runtime_verified: false`. Therefore this asset remains specified—not tested or production-ready.

**Next micro-step:** Resolve skill/tool/event-schema prerequisites, create contract fixtures, then run an authorized harmless public-source smoke test and 10-case golden set. Do not change the existing runtime status without evidence. This is a Phase 1 evidence-layer work item; full roadmap scope and parallel finance blockers remain active.


---

## Wave 15 — Market Research Contract Fixtures and Event Contract Draft — 2026-10-11

- **Completed:** authored 12 SK001 contract fixtures; drafted the `market.research.requested` and `research.completed` event contracts; changed SK001 registry state from `planned` to `specified` based on the existing canonical specification and fixture artifact.
- **Evidence report:** [Wave 15 contract fixtures and event-contract draft](28-market-research-contract-fixtures-and-event-contract-draft-wave15-2026-10-11.md).
- **Commits:** fixtures `15e399eb8aaa35bd5d0785fe5ee69ab8defc75df`; event-contract draft `90eaba4d4950b1aa3479d2a803f972b5d8af373a`; SK001 registry update `4d1a732db697ef76c8fb4189cb9f6c9e9c0e363a`; Wave 15 report `a404944927accd065246ad0318d3bc003a92e6ab`.
- **Status discipline:** artifacts are authored but not schema-validated or executed. Proposed research events are not production-registered. A001 `runtime_verified: false` remains unchanged; all three research tools remain `planned`.
- **Next gate:** validate YAML/schema with the actual project validator; reconcile payload/envelope and idempotency semantics against agent/workflow/data contracts; execute the 12 fixtures in a harness; only then run a harmless public-source runtime smoke test and record logs/event persistence.
- **Route protection:** this is a supporting Market Research/provenance workstream. Continue the main roadmap's cross-functional plan-system scope (sales, marketing, delivery/operations, workforce, customer success, compliance/localization, finance, QA, execution and monitoring); do not let the research-agent work displace it.
