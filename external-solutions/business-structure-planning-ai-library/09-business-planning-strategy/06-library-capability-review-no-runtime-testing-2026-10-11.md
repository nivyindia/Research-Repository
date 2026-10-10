# Business-Plan Library Capability Review — 2026-10-11

**Repository:** `nivyindia/Research-Repository`  
**Review type:** source-definition/capability inspection only. No code was installed or executed, and no runtime test is claimed.

## Decision

The inspected library contains useful building blocks for an international business plan, but the current evidence does **not** show that one resource—or the resources already integrated together—will automatically produce a complete, reliable, country-specific plan for every business type.

Proceed with **REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING**. First assemble the plan pipeline and its evidence/QA controls; do not import every candidate or build a new multi-agent system yet.

## What was inspected

### Internal Nivy resources
- `00-navigation-governance/00-README.md`
- `03-solution-catalogs/11-internet-reuse-catalog-2026-09.md`
- `03-solution-catalogs/12-templates-and-playbooks-catalog.md`
- `06-adoption-implementation/32-master-reuse-library-index.md`
- `06-adoption-implementation/33-master-implementation-roadmap.md`
- `06-adoption-implementation/77-master-automation-and-implementation-registry.md`
- `06-adoption-implementation/84-automation-test-and-evaluation-suite.md`
- `09-business-planning-strategy/01-business-planning-and-ai-strategy-resource-catalog.md`
- `09-business-planning-strategy/02-external-business-plan-agents-skills-and-planning-systems-2026-10.md`
- `09-business-planning-strategy/03-international-business-plan-gap-analysis-2026-10.md`
- `Nivy Artisan/International-Business-Plan-Topics.md`
- `Chats/Claude/International-Business-Plan-Topics.md`
- `Nivy Research Data/Nivy Next Financial Model ...`
- `Nivy Research Data/SECTION 4 — Cost Structure & Unit Economics ...`
- `Nivy Research Data/💹 Financial Model — Part 2: Cash Flow Clarity System ...`

The two international-plan outline files were found to have the same content SHA in the inspected revision. Treat them as duplicates: designate one canonical outline and turn the other into a pointer/archive copy rather than maintaining two editable versions.

### External repositories: README-level capability check
1. [develop-a-business-plan-in-minutes](https://github.com/Musengimana/develop-a-business-plan-in-minutes) — describes cited industry research, a Word plan, Excel forecast, three scenarios and formula-preservation checks. The workbook is based on a Canadian institution's template; localize it for each target jurisdiction and inspect exact licensing of bundled components.
2. [business-plan-skills](https://github.com/peterbamuhigire/business-plan-skills) — describes 137 routed skills across plan sections, financial models and review. Its documented country defaults emphasize Uganda/Kenya/Tanzania, so localization is material.
3. [AI Business Planner](https://github.com/shinpr/ai-business-planner) — describes a guided workflow that separates known facts from assumptions and links the plan to MVP/proposal work; this alone does not prove full regulatory coverage or an integrated financial model.
4. [AI Startup Finance Skills](https://github.com/fareswebnet/ai-startup-finance-skills) — describes investor-readiness, budget, cash, balance-sheet, scenarios and unit-economics workflows; its own disclaimer requires qualified professional review.
5. [Novesai AI Business Plan Generator](https://github.com/novesai/ai-business-plan-generator) — describes a local PDF generator for an AI-program plan with eight sections; it is not a universal business-plan system.

These are publisher-described capabilities, not independent proof of successful outputs. Exact source code, dependencies, license notices, data handling, maintenance and formulas have not all been reviewed. No candidate is approved for production use yet.

## Coverage judgement

| Capability | Evidence found | Status | Required next step |
|---|---|---|---|
| Business-plan section outline | Broad internal topic outline and catalog | Strong starting point; not a complete method by itself | Canonicalize duplicate outline; define deliverables and acceptance criteria per section |
| Business model / canvas | Canvas templates and references | Partial | Tie customer, value, channels, revenue, cost and assumptions to evidence and economics |
| Market and competitor research | Market Research Agent specification; external skills described | Partial / runtime unverified | Inspect skill/tool contracts, source ledger, cross-checks, dates and confidence |
| Strategy and positioning | SWOT/PESTLE/Five Forces, GTM and strategy skills cataloged | Partial | Convert frameworks into evidence-backed choices, alternatives and decision log |
| Sales and marketing plan | GTM, channel and operational skills cataloged | Partial | Add channel budgets, funnel math, CAC/payback, owners, milestones and measurement |
| Operations and organization | Outline covers delivery, technology and hiring; operational skills cataloged | Partial | Capacity model, SOPs, RACI, vendors, quality and service-level controls |
| Financial model | Financial-model index, cash-flow guidance and unit-economics examples | Partial; working integrated model not proven | Verify spreadsheet/formulas; reconcile P&L, balance sheet, cash flow, scenarios, runway and break-even |
| Assumptions and evidence | Mentioned in planning/agent resources | Partial | One assumption register with value, rationale, source, confidence, owner, impact and validation date |
| Decision traceability | Some decision-history patterns in candidate resources | Partial | Decision log with options, rationale, approver, date and downstream effects |
| Auditability / reproducibility | Governance concepts in the gap analysis and agent prompt | Missing or unverified as an integrated control | Save source snapshots, retrieval dates, versions, calculations and output lineage |
| AI governance / security | Cataloged frameworks and policies | Partial | Permissions, data classification, prompt-injection controls, human approvals and logging |
| Early warning / monitoring | KPI/dashboard references | Partial | Thresholds for cash runway, gross margin, CAC, churn, pipeline, overdue receivables and capacity |
| Country localization | External candidates document limited regional defaults | Major gap for “international” use | Country profile per target market: entity, tax/VAT, labor, privacy, licenses, currency and evidence date |
| Plan-to-Company-OS execution | Internal implementation roadmap and company-OS assets | Partial / integration not proven | Convert approved plan into owners, projects, tasks, budgets, KPIs and review cadence |
| Legal/tax/regulatory validation | Referenced as research areas | Not verified as authoritative coverage | Official sources and qualified review; do not let generated text stand as legal/tax advice |
| Business-type-specific drivers | Candidate skills mention selected sectors | Partial | Add modules for services, SaaS, manufacturing/inventory, franchise, marketplace, retail and cross-border trade |

## Financial-model findings

Existing Nivy financial material covers useful operating concepts: revenue and cash tracking, receivables ageing, multi-currency receipts, payment fees, expenses, freelancer payouts, commissions, service prices and delivery costs, contribution margin, growth budgets, currency risk, LTV and pricing experiments.

However:
- Prices, CAC and delivery-cost values in reference documents must be treated as **examples, not current verified benchmarks**. Record source, date, geography, service scope and confidence before relying on them.
- An index or written procedure does not prove a functioning spreadsheet exists or that formulas have been checked.
- A reusable model should reconcile P&L, balance sheet and cash flow; include monthly cash/runway, working capital, break-even, headcount/capacity, financing, tax/currency, scenario/sensitivity and formula/error checks.
- One model driver set will not fit all business types. Use a shared core plus sector-specific modules.

## What to do next — in order

1. **Canonicalize the outline:** retain one source of truth and mark the duplicate.
2. **Inspect top-priority repositories at exact-file level:** start with `develop-a-business-plan-in-minutes`, `business-plan-skills`, `AI Business Planner`, and `AI Startup Finance Skills`. Capture entry files, skills/modules, generated artifacts, license/NOTICE, dependencies, tests and country assumptions.
3. **Inspect Nivy's actual financial workbook/files:** establish whether a working model exists; check formulas and reconciliation only after locating the actual workbook/source.
4. **Create the master coverage register** for all identified capability gaps with columns: Gap ID, capability, severity, internal/external source, exact file path, evidence, status (Covered/Partial/Missing/Unverified), action (Reuse/Adapt/Integrate/Build/Reject), localization needed, owner, acceptance criteria and test status.
5. **Define the universal plan data model and QA gates:** separate verified facts, sourced estimates, assumptions and decisions; require every material claim to have provenance; reconcile narrative numbers to the model.
6. **Only then choose imports and development work.** Run test cases after the static capability and compatibility review, as requested.

## Status labels used in this review

- **Inspected:** source content was opened and read at the stated level.
- **Publisher-described:** a capability is claimed by the repository's README/catalog.
- **Mapped:** related to a business-plan capability.
- **Runtime verified:** not established by this review.
- **Production ready:** not established by this review.

This review is a first bounded pass over the named business-planning resources, not a claim that every link in the entire External Solutions Library has been opened or that every repository/file has been exhaustively audited.
