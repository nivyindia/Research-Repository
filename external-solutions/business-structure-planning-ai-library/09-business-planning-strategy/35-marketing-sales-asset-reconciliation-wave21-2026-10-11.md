# International Marketing & Sales Asset Reconciliation — Wave 21
**Date:** 2026-10-11  
**Roadmap:** Main Updated Implementation Roadmap remains the single source of truth. No route change.  
**Method:** REUSE → MAP → VERIFY → INTEGRATE → TEST → BUILD ONLY WHAT IS MISSING.  
**Status:** Static content comparison; no runtime integrations or channel performance claims.

## 1. Executive finding
The repository already contains three overlapping but complementary layers. Do **not** create another generic international marketing plan:
1. **Master marketing architecture:** `International-Digital-Marketing/00-Master-Plan-Framework.md` (37? no—16 pillars plus SOSTAC/RACE plan spine, cross-cutting systems, digital marketing OS and completeness checks).
2. **Deep international marketing topic inventory:** `Chats/Claude/International-Marketing-Plan.md` (70 numbered sections; adds advanced GTM, market prioritization, industry playbooks, procurement/security readiness, email deliverability, attribution, RevOps, responsible AI, crisis, payments and board reporting).
3. **Sales execution architecture:** `Nivy Research Data/New Research04-08-26/International-Sales-Plan-Guide.md` (sales KPIs, ICP, country prioritization, packaging/pricing, funnel, outbound/inbound, sequences, SOPs, technology, hiring/compensation, proposals, onboarding, retention, financial sales model, 90-day launch and enterprise extensions).
The canonical business-plan blueprint already connects GTM to delivery, workforce, finance, legal, risk and execution. The unresolved gap is therefore not topic count; it is a verified shared contract and traceable execution from marketing activity → qualified pipeline → delivery capacity → revenue/cash → actual-vs-plan.

## 2. Source evidence and qualification
| Asset | Exact path | Static finding | Qualification |
|---|---|---|---|
| Marketing plan skeleton | `International-Digital-Marketing/00-Master-Plan-Framework.md` | SOSTAC + RACE spine; situation analysis, objectives/math, strategy, tactics index, action plan/RACI, KPI/control; 16 pillars and cross-cutting systems | Structure exists; topic details and implementation status must be checked per linked file |
| Marketing deep inventory | `Chats/Claude/International-Marketing-Plan.md` | Sections 1–70; includes channels and advanced global-agency operating practices | Imported conversation/document, not proof of current best practice or implementation; numeric benchmarks are unverified examples |
| Sales plan | `Nivy Research Data/New Research04-08-26/International-Sales-Plan-Guide.md` | 24 core sections plus enterprise addendum; sales execution and 90-day plan | Assumptions, pricing, country ranking and KPIs require current evidence and business-specific validation |
| Sales funnel gap note | `Chats/Claude/Sales-Funnel-Marketing-Gap-Additions.md` | Existing 54-stage sales funnel is described as sales-motion oriented; growth-engine assets may be disconnected from the funnel/n8n stages | Treat the disconnection as a hypothesis until exact workflow files and event wiring are inspected |
| Canonical business-plan blueprint | `external-solutions/business-structure-planning-ai-library/09-business-planning-strategy/07-canonical-international-business-plan-blueprint-2026-10-11.md` | GTM includes marketing, sales and customer success and is connected to operations, people, finance, risk and execution | Requirement backbone; does not establish runtime capability |
| Resource-to-gap map | `external-solutions/business-structure-planning-ai-library/09-business-planning-strategy/25-cross-functional-resource-to-gap-mapping-wave12-2026-10-11.md` | XMAP-02 explicitly identifies missing plan-to-budget/attribution contract; XMAP-01 sales resources need exact-file qualification | Continue as current Phase 0/1 tracking record |

## 3. Duplication and canonical ownership decisions
| Capability | Canonical home | Reuse from other assets | Do not duplicate |
|---|---|---|---|
| Plan governance, evidence, objectives, RACI, controls | Marketing framework A00–A07 + business-plan blueprint governance | Evidence pack and key issue register from framework | Separate executive-summary, SWOT or KPI definitions in every channel document |
| Market/country and competitor research | Business-plan blueprint market/environment section; marketing framework B02/B03/B07 | Marketing deep inventory and sales guide country overlays | Uncited country rankings, market sizes, or pricing presented as facts |
| Positioning, ICP, offers and pricing | Business-plan blueprint customer/business model/GTM sections | Marketing framework B01/B04/B05; sales guide ICP and packaging | Different ICP or price assumptions in sales and marketing plans |
| Channel tactics: SEO, content, social, video, PR, paid | Marketing framework B06–B12; detail files under its own folder map | 70-section marketing inventory and existing social/video catalogs | A new umbrella plan that repeats every channel without owners, inputs and measures |
| Lead generation, funnel, qualification, proposals, close | Sales Plan Guide + verified canonical sales workflow | 54-stage funnel and sales resource catalogs | Rebuild a funnel before checking existing workflows and exact assets |
| CRM, lifecycle, retention, attribution and RevOps | Shared GTM measurement contract; sales guide for sales-specific SOPs | Marketing framework B14/B15; marketing sections 25, 51, 52, 60 | Separate incompatible definitions of lead, MQL, SQL, opportunity, CAC and sourced revenue |
| Budget, CAC, revenue forecast and ROI | Integrated financial model as source of truth | Channel plans supply assumptions and spend; sales guide supplies conversion assumptions | Marketing spreadsheet forecasting revenue independently of the finance model |
| Delivery, workforce, compliance and execution | Business-plan blueprint sections G–M and capability register | Marketing trust, security, talent and support sections | Treating marketing plan completion as proof of company readiness |

## 4. Missing integration contract — highest-value build
Create one shared, versioned record for every channel/campaign and connect it to CRM and the financial/operating model. Minimum required fields:

- Identity: `plan_id`, `initiative_id`, `channel_id`, `market_id`, `service_line_id`, `version`, `status`.
- Evidence: target segment/ICP, source IDs, observation date, assumptions, confidence, known counterevidence, reviewer.
- Strategy: objective, funnel stage, offer, message, intended audience, localization, exclusion criteria.
- Execution: owner, budget/currency, start/end dates, cadence, creative/content asset IDs, landing page, CTA, dependencies.
- Measurement: primary KPI, formula/denominator, baseline, target, data source, attribution model/window, reporting cadence.
- Revenue linkage: leads, qualified leads, opportunities, wins, deal value, gross margin, sales cycle, collection timing; explicitly distinguish sourced, influenced and unattributed revenue.
- Capacity linkage: expected delivery hours/units per win, SLA, skill/role demand, hiring/contractor trigger, quality/rework allowance.
- Decision rules: pause/continue/scale threshold, minimum sample/time window, stop-loss budget, owner approval and review date.
- Governance: privacy/consent basis, outreach compliance checks, approved claims, AI/human review, asset license, change history.

No performance benchmark should be copied into the financial base case unless it has a source, date, applicability note and reviewer approval. Track unknown values as unknown—not zero.

## 5. Priority execution queue
### P0 — map and qualify existing assets
1. Inventory files linked by the marketing framework folder map and each of the 16 pillar folders; capture exact paths, hashes/commits, license, dependencies, schema, tests, last verified date and reuse/adapt/build decision.
2. Inspect the 54-stage funnel and its automation/event wiring. Verify whether the proposed Track M (positioning, SEO, content, social, growth experiments, community/partnerships) exists elsewhere and whether any handoff into CRM/n8n is actually wired.
3. Normalize lifecycle vocabulary across marketing, sales, customer success and finance: visitor → lead → qualified lead → opportunity → won/lost → onboarded → retained/expanded/churned. Preserve existing stage IDs where practical; map aliases instead of destructive renaming.
4. Add channel/campaign records to the assumption/evidence ledger and financial drivers. No campaign revenue should be added without conversion, timing, deal-size, margin and collection assumptions.

### P1 — implement a thin, measurable pilot
5. Choose one service line, one ICP, one country and no more than two initial acquisition channels using evidence and available delivery capacity—not a generic global launch.
6. Define baseline, target, spend cap, measurement source, owner, minimum evaluation window and stop/scale rule before launch.
7. Trace one test record end-to-end: campaign → lead → qualification → opportunity → proposal → win/loss → delivery capacity → invoice/collection → actual-vs-plan dashboard.
8. Add independent test fixtures for duplicate leads, missing consent/compliance status, missing attribution, delayed close, churn, capacity overflow and budget threshold breach.

### P2 — scale only after evidence
9. Expand country/channel coverage after the pilot's data quality, unit economics, delivery quality and customer outcomes pass review.
10. Produce a monthly executive view that separates sourced pipeline, influenced pipeline, bookings, recognized revenue, collected cash, gross margin and delivery utilization.

## 6. Acceptance criteria
- [ ] Every existing candidate asset is mapped to one canonical capability and exact path; duplicates are classified, not deleted.
- [ ] Each reused artifact has license/version/dependency and security status recorded.
- [ ] One shared lifecycle/attribution vocabulary is approved across marketing, sales, finance and customer success.
- [ ] Campaign spend and funnel assumptions feed the same integrated financial model; no independent conflicting revenue forecast.
- [ ] A test fixture demonstrates traceability from campaign to actual/cash and delivery capacity.
- [ ] Tests, results, limitations and human approvals are recorded before any runtime/production claim.
- [ ] Main roadmap remains unchanged; any future route change records reason, impact and return point.

## 7. Known limitations / next verification
This is a static comparison of repository documents. It does not verify live workflow execution, actual CRM/n8n wiring, current market benchmarks, deliverability, analytics tags, or license terms for every linked asset. Marketing framework file SHA at inspection: `d79ef1416a93e71cc76db2132c9fc3a409b8c7c8`; international marketing inventory SHA: `2e310c2da3dfe05c134de88a2f4ccbdc71567932`; sales guide SHA: `747923191fe937a93c736e0503d605b36c70703f`; canonical blueprint SHA: `01cd836d5ad97c400f8c7527d0590901218ab6c4`.
