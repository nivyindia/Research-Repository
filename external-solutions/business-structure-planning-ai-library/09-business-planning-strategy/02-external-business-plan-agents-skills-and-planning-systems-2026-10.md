# External Business-Plan Agents, Skills, Prompts & Planning Systems — Research Wave 5 — 2026-10

**Library location:** `external-solutions/business-structure-planning-ai-library/09-business-planning-strategy/`  
**Purpose:** Discover reusable external assets that can help create many kinds of business plans, including strategic, operational, sales, marketing, GTM, finance, implementation, and risk sections. This is a discovery catalog, not a claim that every asset is production-ready.

**Reuse rule:** DISCOVER → CHECK EXISTING Nivy CATALOGS → DECOMPOSE → VERIFY SOURCE/LICENSE/SECURITY → REUSE → ADAPT → TEST → BUILD ONLY WHAT IS MISSING.

## 1. Highest-priority full-plan builders

| ID | Resource | Asset type / reported scope | Potential use | Reuse assessment | Qualification notes | Source |
|---|---|---|---|---|---|---|
| BPX-001 | develop-a-business-plan-in-minutes | Installable agent skill; cited industry research, Word plan, Excel financial forecast, scenarios, intake and validation scripts | Strong candidate for an end-to-end plan workflow and finance-model QA | **High-priority inspect** | README reports MIT for the skill but a separately governed BDC workbook is included with permission; inspect NOTICE, license and country/currency adaptation before use. Canadian defaults need localization. Requires Python, openpyxl/lxml and LibreOffice for workbook generation. | https://github.com/Musengimana/develop-a-business-plan-in-minutes |
| BPX-002 | peterbamuhigire/business-plan-skills | Business-plan and strategy skill engine; README reports 137 active skills, validation and routing tests | Broad lifecycle coverage and reusable skills for plan creation, monitoring and evaluation | **High-priority inspect** | Review skill list, license, routing rules, model-policy requirements and overlap with existing Nivy catalogs before importing. | https://github.com/peterbamuhigire/business-plan-skills |
| BPX-003 | shinpr/ai-business-planner | Guided planning framework for market research, business plans, PRDs, prototype specifications, pitch decks and decision tracking | Full idea-to-proposal workflow and review gates | **High-priority inspect** | README states MIT. Designed around Cursor/AGENTS.md-compatible tools; inspect dependencies and workflow portability. | https://github.com/shinpr/ai-business-planner |
| BPX-004 | Novesai AI Business Plan Generator | Local app generating an eight-section business/AI-program plan PDF; OpenAI-compatible endpoints and Ollama support | Useful output-format and section-structure reference; potential local generator | **Medium-priority inspect** | Repository reports MIT. Its documented eight-section focus is AI-program business plans, not a universal full company plan. Review implementation and dependencies. | https://github.com/novesai/ai-business-plan-generator |

## 2. Specialized skills for complete plan coverage

| ID | Resource | Coverage | Best use in a plan | Reuse assessment | Qualification notes | Source |
|---|---|---|---|---|---|---|
| BPX-005 | ai-startup-finance-skills | Research intelligence, strategy, investor readiness, 24-month budget, forecast, cash, balance sheet, ROI and financial model skeleton | Financial plan, scenarios, runway, use of funds, KPIs and diligence | **High-priority inspect** | README reports MIT; small/new repository, so test generated workbook and formulas. Educational/informational disclaimer; professional review still needed. | https://github.com/fareswebnet/ai-startup-finance-skills |
| BPX-006 | abinauv/business-consulting | 16 consulting skills and 24 commands; market research, competitor analysis, finance, strategy, pricing, risk, talent and digital transformation | Cross-functional business analysis and plan section generation | **High-priority inspect** | Built as a Claude plugin; inspect installation format, license, command dependencies and portability to other agents. | https://github.com/abinauv/business-consulting |
| BPX-007 | Business-Corporate-Strategy-Advisor-agent-skill | Strategy frameworks including Five Forces, value chain, SWOT/PESTEL, Blue Ocean, JTBD, GTM and scorecards | Strategy, market validation, risk and strategic alternatives | **Medium-priority inspect** | Treat frameworks as analytical aids; verify evidence and assumptions. Review license, dependencies and tests. | https://github.com/dungnotnull/Business-Corporate-Strategy-Advisor-agent-skill |
| BPX-008 | astDeniss/business-skills | 69 operational skills spanning sales, marketing, SEO, paid ads, analytics, content, customer success, operations, product, hiring and PR | Operational, sales and marketing plan detail | **High-priority inspect** | Already referenced in Nivy's Internet Reuse Catalog R26-019; avoid duplicate import. Inspect license/version and reuse specific skills. | https://github.com/astDeniss/business-skills |
| BPX-009 | borghei/Claude-Skills — GTM Strategy | Integrated GTM strategy: ICP, motion, channels, messaging, success metrics and launch plan | Sales plan, marketing plan, market entry and launch strategy | **High-priority inspect** | MIT + Commons Clause is reported in skill metadata; do not assume unrestricted commercial redistribution. Read the exact license. Existing broader Claude-Skills collection is already cataloged. | https://github.com/borghei/Claude-Skills/tree/main/project-management/gtm/gtm-strategy |
| BPX-010 | slgoodrich/agents — Go-to-Market Playbooks | Positioning, messaging, launch planning, market entry, pricing and GTM motions | Marketing/sales plan, channel strategy, launch calendar and positioning | **Medium-priority inspect** | Inspect top-level repository license and agent dependencies; skill is one component in a larger agent collection. | https://github.com/slgoodrich/agents/tree/main/plugins/ai-pm-copilot/skills/go-to-market-playbooks |
| BPX-011 | GAJETOso/financeskills | Finance, accounting, audit, compliance, reporting and financial engineering skills | Finance operations, controls, reporting and risk/compliance sections | **Medium-priority inspect** | Existing finance-skills candidates may overlap. Check the exact license and applicable accounting standards; not a substitute for licensed advice. | https://github.com/GAJETOso/financeskills |

## 3. Planning infrastructure and templates

| ID | Resource | Type | Role in reusable planning system | Qualification notes | Source |
|---|---|---|---|---|---|
| BPX-012 | Totally Lean | Lean Canvas with local AI | Early business-model assumptions, canvas and critique | Already listed in the existing Business Planning / AI Strategy Resource Catalog; evaluate current privacy/license terms. | https://www.leancanvas.online/en |
| BPX-013 | Business Model Canvas Template | Canvas template | Problem, customer, value proposition, channels, revenue, cost and key resources | Existing Nivy catalogs already reference the template; use as a component, not as a complete plan. | https://github.com/desireco/BusinessModelCanvasTemplate |
| BPX-014 | Microsoft Cloud Adoption Framework — Business plan for AI agents | Published planning guidance | Useful as a reference for AI-specific business cases, governance, technology planning and organizational readiness | Guidance document, not an installable agent; verify current documentation version. | https://github.com/MicrosoftDocs/cloud-adoption-framework/blob/main/docs/ai-agents/business-strategy-plan.md |
| BPX-015 | Dify Workflow Studio | Visual AI workflow builder | Orchestrate intake → research → section writers → evidence checks → human approval → document output | Platform component rather than a ready-made business-plan agent; current license and hosting constraints require review. | https://www.dify.ai/workflows |

## 4. Coverage map — which assets can support which plan sections?

| Business-plan section | First assets to inspect |
|---|---|
| Intake, assumptions and plan brief | BPX-001, BPX-002, BPX-003 |
| Executive summary and overall plan assembly | BPX-001, BPX-002, BPX-003 |
| Market research, industry and customer demand | BPX-001, BPX-002, BPX-005, BPX-006 |
| Competitor analysis and differentiation | BPX-006, BPX-007, BPX-008 |
| Business model, offer and pricing | BPX-003, BPX-006, BPX-007, BPX-012, BPX-013 |
| Sales plan, GTM, positioning and channels | BPX-008, BPX-009, BPX-010 |
| Marketing plan and launch calendar | BPX-008, BPX-009, BPX-010 |
| Operational plan and SOPs | BPX-002, BPX-006, BPX-008 |
| Organization, hiring and capability plan | BPX-002, BPX-006, BPX-008 |
| Financial model, cash flow, balance sheet and scenarios | BPX-001, BPX-005, BPX-011 |
| Risk, governance and compliance | BPX-005, BPX-006, BPX-007, BPX-011, BPX-014 |
| Implementation roadmap, KPIs and monitoring | BPX-002, BPX-003, BPX-005, BPX-007 |
| Document generation and final QA | BPX-001, BPX-002, BPX-004 |

## 5. Recommended evaluation order

1. **BPX-001** — inspect the full-plan skill, templates, workbook generator, validation scripts and localization controls.
2. **BPX-002** — compare its 137-skill engine against the full business-plan section map and Nivy's existing catalogs.
3. **BPX-003** — inspect the guided workflow and decision-history approach.
4. **BPX-005** — inspect financial-model skeleton, formula quality and scenario coverage independently.
5. **BPX-006 + BPX-007** — use as section-level consulting and strategy components.
6. **BPX-008 to BPX-011** — fill sales, marketing, operations and finance gaps selectively.
7. **BPX-004 / BPX-015** — consider only if a local PDF generator or visual workflow platform is actually needed.

## 6. Qualification status and safety rules

All entries in this wave are **discovered candidates**, not approved production dependencies. A link in this catalog does not mean code or files have been copied into Nivy.

Before vendoring or executing an asset:
- inspect exact license, notices and redistribution/commercial-use restrictions;
- record source commit, retrieval date and provenance;
- inspect dependencies, network/API calls and platform requirements;
- test on a non-sensitive sample;
- check prompt-injection handling, secrets, PII and data retention;
- verify formulas, arithmetic, source citations and cross-document consistency;
- localize jurisdiction, currency, tax/regulatory references and market data;
- keep material assumptions separate from verified facts;
- require qualified human review for financial, legal, tax, regulatory or funding decisions.

## 7. Relationship to existing Nivy assets

Do not create a parallel planning library. Cross-check and connect this catalog with:
- `01-business-planning-and-ai-strategy-resource-catalog.md`
- `../03-solution-catalogs/11-internet-reuse-catalog-2026-09.md`
- `../03-solution-catalogs/42-ai-agent-skills-prompts-generative-ai-reuse-catalog-2026-09.md`
- `../03-solution-catalogs/43-business-builder-autonomous-company-reuse-research-wave-1-2026-09.md`
- `../03-solution-catalogs/44-business-builder-reuse-research-wave-2-2026-09.md`
- `../03-solution-catalogs/45-business-builder-reuse-research-wave-3-deep-qualification-2026-09.md`
- `../03-solution-catalogs/46-exact-asset-extraction-wave-4-2026-09.md`

**Next research task:** inspect the top-priority repositories at exact-file level, compare against existing Nivy assets, and create an extraction manifest only for assets that pass license, quality, compatibility and duplication checks.
