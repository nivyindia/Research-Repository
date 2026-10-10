# International-Level Business Plan — Gap Analysis — 2026-10

## Executive finding

The Nivy Business Planning library already covers the normal business-plan headings and has multiple reusable builders/skills. The remaining gap is not primarily missing sections; it is missing or insufficiently qualified decision-grade capabilities around evidence, localization, modeling, validation, execution, and governance.

## Gap severity

| Gap | Status | Severity | What is needed |
|---|---|---|---|
| Business-plan assembly | Covered | Low | Existing full-plan candidates BPX-001/002/003 |
| Executive summary | Covered | Low | Generate only after underlying sections are validated |
| Company/business model | Covered | Low | Canvas + strategy resources already cataloged |
| Market research | Partially covered | Critical | Country/industry TAM-SAM-SOM, demand evidence, primary research, source grading |
| Competitor intelligence | Partially covered | High | Structured competitor database, pricing extraction, feature/service comparison, change monitoring |
| ICP/customer segmentation | Covered/partial | Medium | Existing Nivy ICP/Buyer Persona assets; connect to plan workflow |
| Positioning/value proposition | Covered/partial | Medium | GTM/strategy skills exist; require evidence-linked positioning |
| Sales plan | Covered/partial | High | Funnel economics, quota/capacity model, territory/account model, pipeline forecast |
| Marketing plan | Covered/partial | High | Channel economics, campaign calendar, attribution, budget allocation and experimentation |
| Operational plan | Covered/partial | Critical | Capacity model, service delivery architecture, SOP dependency map, SLA and QA model |
| Organization/hiring | Covered/partial | High | Workforce plan tied to revenue, workload, utilization and hiring triggers |
| Financial model | Partially covered | Critical | Three-statement model, unit economics, scenario engine, cash-flow timing, country/tax localization |
| Pricing | Partially covered | High | Competitor pricing evidence, cost/value checks, margin floor, packaging calculator |
| Legal/compliance | Partially covered | Critical for international use | Country-specific regulatory checklist, contracts, tax, privacy, licensing and professional-service boundaries |
| Risk management | Covered/partial | High | Quantified risk register, probability/impact, mitigation owner, trigger monitoring |
| Implementation roadmap | Covered | Medium | Convert plan into projects/tasks/owners/KPIs rather than static roadmap |
| KPI/OKR system | Covered/partial | Medium | KPI definitions, formulas, data sources, targets, owners and cadence |
| Business-plan QA | Partially covered | Critical | Independent reviewer/evaluator, numerical consistency, citation verification, assumption/fact separation |
| Research provenance | Partially covered | Critical | Source registry, retrieval date, evidence grade, claim-to-source mapping |
| International localization | Missing as a unified layer | Critical | Country/currency/tax/regulatory/payment/labor/data/privacy/local-market adaptation |
| Sensitivity analysis | Partially covered | High | Driver-based sensitivity, break-even, downside/base/upside and Monte Carlo where justified |
| Customer validation | Partial | High | Interview scripts, survey/experiment design, evidence scoring and decision gates |
| Go/no-go decision system | Missing as unified layer | High | Stage gates with objective criteria before market/service expansion |
| Document production | Covered/partial | Medium | DOCX/XLSX/PDF generation exists in candidates; require deterministic QA |
| Post-plan monitoring | Partial | High | Actual-vs-plan dashboard, forecast updates, variance analysis and plan revision loop |

## Critical missing layer #1 — Evidence & Research Intelligence

A high-quality international plan cannot depend only on an LLM-generated narrative.

Required flow: Question -> Search -> Primary/secondary sources -> Extract facts -> Source quality score -> Claim/evidence mapping -> Market model -> Conclusion.

Required outputs:
- market-size evidence;
- growth evidence;
- customer demand signals;
- competitor evidence;
- pricing evidence;
- regulatory evidence;
- source date;
- geography;
- confidence;
- assumption vs verified fact.

## Critical missing layer #2 — Internationalization Engine

The plan generator needs a reusable country profile object:

Country -> Currency -> Tax -> Corporate rules -> Employment -> Data/privacy -> Financial regulation -> Licensing -> Payments -> Market conventions -> Language -> Local competitors

The same business idea should therefore produce different plan variants for UAE, USA, UK, Canada, Australia, India, etc., rather than merely changing currency symbols.

## Critical missing layer #3 — Integrated Financial/Operating Model

The plan needs a driver-based model connecting:

Leads -> Qualified leads -> Meetings -> Proposals -> Wins -> Customers -> Retention -> Revenue -> Delivery workload -> Staff capacity -> Costs -> Gross margin -> Cash flow

This is more valuable than a standalone financial forecast because management can see what operational assumptions create the financial result.

## Critical missing layer #4 — Independent Plan QA

The final business plan needs a separate reviewer that checks:
- every major claim has evidence or is labeled an assumption;
- market-size math is internally consistent;
- revenue projections reconcile with customer counts and pricing;
- staffing matches workload;
- marketing budget matches acquisition assumptions;
- cash flow reflects payment timing;
- financial statements reconcile;
- country-specific claims are sourced;
- risks have owners and mitigations;
- recommendations follow from evidence.

## Critical missing layer #5 — Validation / Stage Gates

Gate 0 — Idea -> problem and customer hypothesis

Gate 1 — Market -> demand + competition + market attractiveness

Gate 2 — Offer -> willingness-to-pay + pricing + unit economics

Gate 3 — Sales -> acquisition channel + conversion + CAC evidence

Gate 4 — Delivery -> capacity + quality + contribution margin

Gate 5 — Financial -> cash flow + break-even + downside survivability

Gate 6 — Expansion -> repeatability + retention + management capacity

## What is NOT missing

The library already has enough raw material for:
- Business Model Canvas / Lean Canvas
- Strategy frameworks
- SWOT / PESTEL / Five Forces
- Market research
- ICP / personas
- Competitive intelligence
- GTM
- Sales
- Marketing
- Operations
- Finance
- HR / organization
- SOPs
- AI workforce/company design
- KPIs/OKRs
- project/task execution
- document generation
- agent orchestration

The problem is integration and qualification, not a shortage of isolated resources.

## Recommended target architecture

BUSINESS IDEA
-> INTAKE + ASSUMPTIONS
-> MARKET / CUSTOMER RESEARCH
-> COMPETITOR + PRICING INTELLIGENCE
-> BUSINESS MODEL
-> OFFER + POSITIONING
-> GTM
-> SALES PLAN
-> MARKETING PLAN
-> OPERATING PLAN
-> ORGANIZATION + WORKFORCE
-> TECHNOLOGY / AI PLAN
-> LEGAL / COMPLIANCE
-> FINANCIAL MODEL
-> RISK + SCENARIOS
-> IMPLEMENTATION ROADMAP
-> KPI / MONITORING
-> INDEPENDENT QA
-> EXECUTIVE PLAN
-> APPROVAL
-> EXECUTION SYSTEM
-> ACTUAL vs PLAN
-> REFORECAST

## Priority build/reuse order

1. Research/evidence + provenance layer
2. International country-localization layer
3. Integrated operating + financial model
4. Independent business-plan QA/evaluation
5. Validation/stage-gate system
6. Pricing/unit-economics calculator
7. Sales/marketing funnel economics
8. Plan-to-execution converter
9. Post-plan monitoring/reforecasting
10. Only then build remaining custom business-plan generation logic.

## Conclusion

Nivy does not need another generic Business Plan Generator.

The stronger architecture is a Business Plan Intelligence & Execution System that orchestrates the existing builders, research agents, strategy skills, finance skills, GTM skills and Company OS assets, then adds the missing evidence, localization, integrated modeling, QA and execution layers.

This is an assessment of the current Nivy library/catalog state; external candidates remain subject to exact-file, license, security, compatibility and quality verification.
