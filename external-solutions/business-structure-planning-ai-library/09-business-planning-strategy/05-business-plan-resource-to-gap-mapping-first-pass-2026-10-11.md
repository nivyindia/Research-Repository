# Business Plan Resource-to-Gap Mapping — First Pass (2026-10-11)

Status: Repository discovery and partial mapping. This is not runtime validation.

## Confirmed repository resources

| ID | Source path | Observed contents | Gap coverage candidate | Decision / next check |
|---|---|---|---|---|
| MAP-01 | `Nivy Artisan/International-Business-Plan-Topics.md` | Business-plan outline including executive summary, company, market, customer, competitors, SWOT/PESTLE/Five Forces, offers, pricing, sales, marketing, operations, delivery, technology, automation, organization, hiring and risk | G01-G03, G06-G16, G29 | Reuse as a checklist; compare with alternate copies and extend for evidence, governance, country localization and lifecycle |
| MAP-02 | `Nivy Research Data/Nivy Next Financial Model 29bb3416c76d818bbe6ae31cc86e3929.md` | Links to cash flow, growth budgeting, cost structure/unit economics, global + India tax, currency risk, international payments/bad debt, risk planning, financial automation, scaling, LTV, pricing experiments, accountability and dashboards | G17-G22, G24, G29, G40, G43+ | Strong internal candidate; inspect linked section files and validate calculations before accepting |
| MAP-03 | `Notion - Nivy OS/Nivy Next Financial Model e4feb94b1a2a8214823701f5c30c9a4c.md` | Parallel financial-model index with similar section structure | G17-G22, G24 | Likely duplicate/alternate copy; compare versions and choose canonical source |
| MAP-04 | `external-solutions/business-structure-planning-ai-library/09-business-planning-strategy/03-international-business-plan-gap-analysis-2026-10.md` | Expanded gap matrix, including market intelligence, finance, tax, compliance, evidence, assumptions and QA | All gap groups | Use as master capability list; retain stable IDs and add resource, evidence, owner, status and acceptance columns |
| MAP-05 | `external-solutions/business-structure-planning-ai-library/09-business-planning-strategy/04-business-plan-intelligence-execution-implementation-roadmap-2026-10.md` | Phased roadmap from baseline and asset qualification through common data model, decision core, execution integration and monitoring | Cross-cutting | Use as implementation sequence; this mapping is its first-pass evidence companion |
| MAP-06 | `external-solutions/business-structure-planning-ai-library/07-department-sales/93-sales-micro-level-completeness-audit.md` | Search results show provenance, dependency mapping, assumption register and open-question register patterns | G33-G36, governance | Adapt common register fields; inspect source schema before copying |
| MAP-07 | `external-solutions/business-structure-planning-ai-library/00-navigation-governance/03-MASTER-BUSINESS-CREATION-TO-AUTONOMY-LIST-2026-09.md` | Master business-creation checklist includes evidence/provenance, research confidence, QA and packaging | Evidence, QA, execution | Cross-map against all capabilities to avoid duplicate governance design |

## Market Research Agent: file-level inspection completed; runtime still unverified

Canonical paths confirmed:
- `Chats/ChatGPT/Multi Agent AIOS/agents/market-research/agent.yaml`
- `Chats/ChatGPT/Multi Agent AIOS/agents/market-research/prompt.md`
- Status record: `Chats/ChatGPT/Multi Agent AIOS/02-agents/F1-A001-status.yaml`

The YAML defines A001, required inputs `research_question` and `target_market`, optional geography/industry/segment/time horizon, a structured report output, evidence provenance, material-claim cross-checks, confidence assessment, approved public sources, tool allow-list and failure handling. The prompt repeats the research workflow and includes evidence grades A-D, a report contract and explicit stop conditions.

**Important status:** The status file explicitly says `runtime_verified: false`, `status: 25`, and `next_micro_step: F.1.2`. Therefore this is a well-specified design, not proof of a working agent.

**Next verification work:** resolve the registered SK001/SK002 and TOOL-FIRECRAWL-EXTRACT / TOOL-BROWSER-USE-RESEARCH / TOOL-POSTGRES-QUERY-READONLY contracts; confirm schemas, permissions and runtime wiring; run one harmless public-data test; then build a 10-case golden test set. Record pass/fail, citations, output validity, unsupported-claim rate, and failure handling. Do not mark the agent production-ready before these tests.

## Additional file-level inspection findings

### International business-plan blueprint
Canonical source found: `Nivy Research Data/New Research04-08-26/Business-Plan-for-DM-AI-IT.md`. It is explicitly designed for an India-based digital marketing + AI + IT + web-development company targeting international markets. It contains a detailed outline and is useful as a vertical-specific reference, but must not be treated as a universal template without adapting the service-business assumptions.

### Unit economics and cash-flow files
- `Nivy Research Data/SECTION 4 — Cost Structure & Unit Economics 2b1b3416c76d80ef9d8dceef8b03af78.md` includes service prices, delivery-cost examples, freelancer benchmarks, sales commissions and software budgets.
- `Nivy Research Data/💹 Financial Model — Part 2 Cash Flow Clarity Syste 2b1b3416c76d80c6b36bd2a972b2efcf.md` includes revenue tracking, aging reports, multi-currency cash flows, expense categories and payout processes.
- Matching copies are present under `Notion - Nivy OS/`, so duplicate/canonical-source reconciliation is necessary.

**Validation warning:** The cost/price numbers are documented examples, not verified current market benchmarks. They need source dates, geography, service scope, sample size and fresh validation. The cash-flow guidance is a process outline; the file inspection did not establish that a working spreadsheet, formulas or automated reconciliations exist. Do not use these values as financial truth without validation.

## Initial gap decisions

- **Reuse candidate:** existing business-plan outline; financial-model index and its linked sections; existing governance/register patterns.
- **Adapt likely needed:** international/country-specific assumptions, source freshness/provenance, standardized input/output schemas, risk and approval gates.
- **Build only if missing after inspection:** unified master gap register; common plan data model; independent plan/financial QA; plan-to-execution conversion and actual-vs-plan feedback loop.
- **Do not do yet:** bulk-import external repositories, declare any agent production-ready, or create one agent per gap.

## External candidates to qualify (not approved)

The external catalog at `02-external-business-plan-agents-skills-and-planning-systems-2026-10.md` lists full-plan, finance, strategy and consulting candidates, including `Musengimana/develop-a-business-plan-in-minutes`, `peterbamuhigire/business-plan-skills`, `shinpr/ai-business-planner`, `fareswebnet/ai-startup-finance-skills`, `abinauv/business-consulting` and `astDeniss/business-skills`.

Before reuse, record exact commit, license and notices, dependencies, security review, input/output schema, test results, localization needs and overlap with existing Nivy files. Discovery catalog entries alone do not prove current license or quality.

## Master-register fields to use

`Gap ID | Capability | Severity | Existing source path | Evidence found | Coverage (Covered/Partial/Missing/Unverified) | Reuse/Adapt/Integrate/Build/Reject | Owner | Acceptance criteria | Test result | Next action`

## Next steps in order

1. Wire and safely test A001 Market Research Agent: canonical files are now located; runtime remains unverified.
2. Compare internal plan-outline duplicates and select a canonical outline.
3. Inspect linked financial-model sections, formulas and assumptions; mark untested elements explicitly.
4. Expand this table into one row per gap from the 75-capability analysis.
5. Qualify external candidates only for gaps that remain after internal reuse.

## Acceptance rule

A resource is not “Integrated” merely because it exists in GitHub. Require exact source/version, license/security review, dependencies, input/output schema, reproducible tests, localization notes, limitations and traceability to the gap it satisfies.
