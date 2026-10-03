# Phase 7 — Diagram System Reconciliation

**Date:** 2026-10-03  
**Status:** COMPLETE  
**Principle:** Use existing 19+ Draw.io files. Do not create a second diagram hierarchy.

---

## P31 — Canonical diagram location decision

| Decision | Detail |
|---|---|
| **Canonical location** | `docs/OWNER-CONTROL/05-VISUALS/` |
| **V7 integration point** | `Company OS/Company-OS-v7/Diagrams/` (index/plan only — **no duplicate .drawio**) |
| **Standard** | `08-DRAWIO-STANDARD.md` |
| **Rationale** | All editable sources already live under OWNER-CONTROL; V7 README already points there; splitting would violate one-concept-one-diagram |
| **Future migration** | If moved under V7 later: update all references first, then move with history |

---

## P21 — Diagram inventory (D01–D19+)

| ID | File | Scope | Canonical model alignment | Owner (default) |
|---|---|---|---|---|
| D01 | NIVY-COMPANY-MASTER-MAP | Company OS overview + execution loop | Company, Strategy, Org, Ops, Tech, Execution chain | CEO / Workspace Admin |
| D02 | NIVY-BRAND-ARCHITECTURE | Brands + shared capabilities | Brand, Company | CEO |
| D03 | NIVY-ORGANIZATION-MAP | Owner → functions | Department, Function | CEO / Ops |
| D04 | NIVY-GOAL-CASCADE | Vision→Daily→KPI | Goal, Plan cadence, KPI | STR / CEO |
| D05 | NIVY-PLANNING-CADENCE | Annual→Daily + Review | Plan | STR / PMO |
| D06 | NIVY-TASK-HIERARCHY | Goal→Plan→Project→Milestone→Task→Output→KPI | Project, Milestone, Task, Output, KPI | PMO |
| D07 | NIVY-REVIEW-LOOP | Plan→Execute→Evidence→Review→Decide | Review, Decision, Evidence | Ops / PMO |
| D08 | NIVY-SALES-ACQUISITION-FLOW | Lead→Close→Revenue | Customer, Opportunity | Head of Sales |
| D09 | NIVY-SERVICE-DELIVERY-FLOW | Onboard→Delivery→Billing→Retention | Project, Output, Customer | CS Lead |
| D10 | NIVY-TALENT-PIPELINE | Need→Employee | Role, Person | CHRO |
| D11 | NIVY-FINANCE-FLOW | Finance cycle | Record, Customer, KPI | CFO |
| D12 | NIVY-DATA-KNOWLEDGE-ARCHITECTURE | Data→Knowledge | Document, System | CDO / CTO |
| D13 | NIVY-AIOS-ARCHITECTURE | AIOS layers | AI Agent, System | CTO |
| D14 | NIVY-AUTOMATION-INTEGRATION-MAP | Triggers→Actions | Integration | CTO |
| D15 | NIVY-RESEARCH-KNOWLEDGE-LIFECYCLE | Research→Operational | Document promotion | Workspace Admin |
| D16 | NIVY-RESPONSIBILITY-RACI-MAP | Goal→RACI→Evidence | Responsibility, Role | Ops |
| D17 | NIVY-DECISION-ESCALATION-FLOW | Issue→Decision→Evidence | Decision, Exception | Ops / RISK |
| D18 | NIVY-ACCESS-SECURITY-MAP | Identity→Audit | Access, Classification | CTO / RISK |
| D19 | NIVY-SOP-ARCHITECTURE | Process→SOP→Archive | Process, SOP, Evidence | Ops / QA |
| D20* | NIVY-OWNER-CONTROL-MASTER | Owner control composite | Company control | CEO |
| D21* | NIVY-MASTER-ROADMAP | Roadmap | Plan / Initiative | STR |
| D22* | NIVY-HISTORY-TIMELINE | History | Company | CEO |

\* Additional existing files beyond the original 19-count naming; treated as part of the same canonical set.

All files are `.drawio` XML sources under `docs/OWNER-CONTROL/05-VISUALS/`.

---

## Terminology reconciliation

| Diagram language | Canonical Object Model term |
|---|---|
| Vision / North Star / Strategy | Company Goal / Strategy docs (STRAT) |
| Annual / Quarterly / Monthly / Weekly / Daily | Plan cadence + Goal levels |
| Task / Subtask / Deliverable | Task / Work / Output |
| KPI / Result / Evidence | KPI / Output / Evidence / Record |
| Department / Team / Role | Department / Function / Role / Person |
| SOP / Policy | SOP / POL (Doc 02) |
| Agent / Integration | AI Agent / Integration |

**No contradictory second vocabulary introduced.** Models in Company Master Standards use the same chain as Goal Cascade + Task Hierarchy + Review Loop.

---

## P22 — Department management views

**Not a new diagram.** Compose from existing visuals + data:

| View element | Source diagram / model |
|---|---|
| Department purpose / structure | Organization Map, Brand Architecture |
| Department goals | Goal Cascade + Goal-Registry |
| Plans / projects | Planning Cadence, Task Hierarchy, 02_PROJECTS |
| Work / capacity | Strategy-Execution-Model, Operational-Workflows P28 |
| KPIs / reviews | Review Loop, KPI-Management-Review-Model |
| RACI | Responsibility RACI Map |

**Dashboard architecture (logical):** Department filter over Company dashboard inputs (P25).

---

## P23 — Employee management views

**Not a new diagram.**

| View element | Source |
|---|---|
| Role / responsibilities | RACI Map, Doc 01 Owner Role, Org-Chart |
| Goals | Goal Cascade (person level), Goal-Registry |
| Tasks / daily work | Task Hierarchy, Strategy-Execution daily log |
| KPIs / reviews | KPI model employee cadence |
| Talent status | Talent Pipeline |

---

## P24 — Company / Department / Employee daily execution model

**Covered by:**
- Goal Cascade (Daily Priorities → Task/Output)
- Planning Cadence (Daily Execution node)
- Task Hierarchy
- Strategy-Execution-Model §P11

No additional Draw.io file required.

---

## P25 — Management dashboard architecture

| Layer | Content | Visual / system source |
|---|---|---|
| Company | Goals, KPIs, financial/commercial, phase health | Company Master Map + KPI model + dashboard.md |
| Department | Dept goals, projects, KPIs | Org Map + Goal/KPI registries |
| Project | Milestones, tasks, outputs | Task Hierarchy + 02_PROJECTS |
| Employee | Goals, tasks, daily work | Goal Cascade + daily log |
| Daily | Priorities, blockers, outputs | Planning Cadence daily node |
| Doc health | Unowned, stale, links | dashboard-generate.yml |

**Rule:** Dashboards reference canonical IDs; they do not define alternate metrics.

---

## P30 — Cross-diagram validation

| Check | Result |
|---|---|
| Single location | Pass — all under OWNER-CONTROL/05-VISUALS |
| No duplicate hierarchy in V7/Diagrams | Pass — index only |
| Goal→…→KPI chain consistent across D04, D05, D06, D07 | Pass — same sequence |
| Org vs Brand | Pass — Brand under Company; shared capabilities |
| Sales→Delivery→Finance handoff | Pass — Customer/Project continuity |
| Research→Canonical→AIOS | Pass — D15 + D13 + D14 |
| Decision/SOP/Security | Pass — D17, D19, D18 align with governance docs |
| Open in Draw.io | Pass — valid mxfile XML structure on inspected samples |
| Provenance | Partial — standard requires SOURCE/CONTROL block; many files are minimal XML and should gain provenance labels in a future visual polish pass |

**Known limitation:** Visual polish (SOURCE/CONTROL stamps, stable semantic cell IDs, parent-child page tabs) remains recommended improvement, not a structural gap.

---

## Gaps — new diagrams?

| Potential view | Decision |
|---|---|
| Department management | **No new diagram** — compose D03+D04+D07 |
| Employee management | **No new diagram** — compose D04+D06+D16+D10 |
| Daily execution | **No new diagram** — D04/D05/D06 |
| Management dashboard | **No new diagram** — architecture documented; data from registries + dashboard.md |

---

## Updates to visual tracker

Recommended status (for `docs/OWNER-CONTROL/05-VISUALS/07-PROGRESS-TRACKER.md`):

- V20 Cross-diagram validation → **DONE** (this document)
- V21 index → V7 Diagrams README already points to canonical path
- Overall program phase note may lag; **Company OS Combined tracker is authoritative for OS program**

---

## Phase 7 exit check

| Item | Status |
|---|---|
| P21 reconciliation | Done — inventory + terminology |
| P22–P25 views | Defined via composition; no duplicate diagrams |
| P30 cross-validation | Done — checks above |
| P31 location decision | **Keep `docs/OWNER-CONTROL/05-VISUALS/`** |
| No second diagram hierarchy | Confirmed |

---

## Files created

- `Audit-and-Tasks/P07_Diagram_System_Reconciliation.md` (this file)
