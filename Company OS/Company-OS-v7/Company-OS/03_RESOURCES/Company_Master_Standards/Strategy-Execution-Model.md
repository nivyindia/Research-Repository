# Strategy & Execution Model — Company OS V7

**Code:** ALL-STRAT-002  
**Title:** Strategy, Planning and Execution Model  
**Department:** ALL  
**Type:** STRAT  
**PARA Bucket:** Resource  
**Version:** v1.0  
**Lifecycle Status:** Draft  
**Confidentiality:** Internal  
**Owner (Accountable):** CEO Office / Workspace Admin  
**Responsible:** Ops Head / PMO  
**Created Date:** 2026-10-03  
**Last Updated:** 2026-10-03  
**Next Review:** 2027-01-03  
**Tags:** strategy, goals, planning, execution, hierarchy, RACI, work  
**Related Documents:** Canonical-Object-Model.md, GOVERNANCE/01-Department-Code-Registry, Brands.md, Org-Chart.md, 02_PROJECTS/README.md  
**Related Diagrams:** NIVY-COMPANY-MASTER-MAP, NIVY-BRAND-ARCHITECTURE, NIVY-ORGANIZATION-MAP, NIVY-GOAL-CASCADE, NIVY-PLANNING-CADENCE, NIVY-RESPONSIBILITY-RACI-MAP

> **Purpose:** Operationalize the Canonical Object Model for hierarchy, goal cascade, planning cadence, daily work, and responsibility allocation.  
> **Rule:** REUSE existing registries and diagrams. This document defines linkage rules, minimum record fields, and templates only where missing.

---

## P07 — Company hierarchy

### Canonical chain

```
Company (Billion Dreams United / Nivy Global)
  → Brand (ADV, NXT, …)
    → Department (Doc 01 codes)
      → Function ([DEPT]-FN-[nnn])
        → Role ([DEPT]-ROLE-[nnn] or Doc 01 Owner Role)
          → Person (PERS-[nnn] / employee ID)
```

### Source of truth (do not duplicate)

| Level | Canonical source |
|---|---|
| Company | Company-Overview.md |
| Brand | Doc 01 §C + Brands.md |
| Department | Doc 01 §A/B + departments.json |
| Function | *Registry below (seed)* |
| Role | Doc 01 Owner Role column + Org-Chart.md |
| Person | Org-Chart.md (extend as people join) |

### Function registry (seed)

Functions are sub-capabilities inside a department. Add rows as needed; do not invent department codes.

| Function ID | Department | Name | Owner Role | Status |
|---|---|---|---|---|
| CEO-FN-001 | CEO | Owner Control / Final Decisions | Founder/CEO | Active |
| STR-FN-001 | STR | Strategy & Annual Planning | CSO | Active |
| SALES-FN-001 | SALES | Lead Generation & Outreach | Head of Sales | Active |
| SALES-FN-002 | SALES | Closing & Account Growth | Head of Sales | Active |
| CS-FN-001 | CS | Delivery & Retention | CS Lead | Active |
| HR-FN-001 | HR | Talent Pipeline & Onboarding | CHRO | Active |
| FIN-FN-001 | FIN | Billing, Collection, Cashflow | CFO | Active |
| TECH-FN-001 | TECH | AIOS / Automation / Systems | CTO | Active |
| PMO-FN-001 | PMO | Project & Milestone Control | Head of PMO | Active |
| QA-FN-001 | QA | QC & Internal Audit | QA Lead | Active |

*Expand per department as roles stabilize. Org-Chart remains the place for named people.*

### Brand ↔ Department operating rule

- Brands (ADV, NXT, …) share company capabilities (Sales, Delivery, Finance, HR, AIOS) unless a brand-specific override is documented.
- Department codes from Doc 01 apply across brands; brand code is an additional dimension on Goals, Projects, Customers, and Outputs when needed.

---

## P08 — Goal → Plan → Initiative → Project → Task → Work → Output

### Linkage rules

| From | To | Required field on child |
|---|---|---|
| Goal | Plan | `plan.goal_ids` |
| Plan | Initiative | `initiative.plan_id` |
| Plan / Initiative | Project | `project.plan_id` or `project.initiative_id` |
| Project | Milestone | `milestone.project_id` |
| Project / Milestone | Task | `task.parent_id` (project or milestone) |
| Task | Work | `work.task_id` + date |
| Work | Output | `output.work_id` |

### Minimum record fields

**Goal**
```
ID: [SCOPE]-GOAL-[nnn]     (SCOPE = COMP | [DEPT] | [PERS] | [BRAND])
Name:
Owner (Accountable):
Scope: Company | Brand | Department | Person
Period: Annual | Quarterly | Monthly | …
Target / Success criteria:
Parent Goal ID: (if cascaded)
Status: Draft | Active | Achieved | Missed | Retired
Linked Plan IDs:
Linked KPI IDs:
```

**Plan**
```
ID: [SCOPE]-PLAN-[yyyy] or [SCOPE]-PLAN-[yyyy]-Q[n]
Name:
Owner:
Cadence: Annual | Quarterly | Monthly | Weekly | Daily
Goal IDs:
Period start / end:
Capacity notes:
Status: Draft | Active | Closed
Linked Initiative / Project IDs:
```

**Initiative**
```
ID: [DEPT]-INIT-[nnn]
Name:
Owner:
Plan ID:
Strategic intent:
Status: Proposed | Active | Completed | Cancelled
Linked Project IDs:
```

**Project** — uses existing `02_PROJECTS/` structure and `PROJ-DOC-[ShortCode]` naming.
```
Folder: 02_PROJECTS/[Project Name — Year]/
Charter fields (in PROJ-DOC):
  Project ID / ShortCode:
  Plan ID / Initiative ID:
  Goal IDs:
  Owner / RACI:
  Start / Target end:
  Milestones (list):
  Success criteria / Outputs:
```

**Milestone**
```
ID: [PROJ]-MS-[nnn]
Name:
Project ID:
Due date:
Acceptance criteria:
Status: Pending | Met | Missed | Deferred
```

**Task**
```
ID: [PROJ]-TASK-[nnn]  or external system ID (TickTick / GitHub Issue)
Name:
Parent: Project ID or Milestone ID
Owner (Responsible):
Priority: P0 | P1 | P2 | P3
Dependencies: [task IDs]
Recurring: Yes/No + cadence
Status: Not Started | In Progress | Blocked | Done | Cancelled
```

**Work** (daily execution instance)
```
ID: [TASK]-WORK-[YYYY-MM-DD]  or daily log entry
Task ID:
Person ID:
Date:
Planned effort / Actual effort:
Notes / blockers:
Output IDs produced:
```

**Output**
```
ID: [TASK/WORK]-OUT-[nnn]
Name / description:
Work ID / Task ID:
Type: Deliverable | Document | Data | Decision | Other
Evidence link / path:
Acceptance: Accepted | Rejected | Pending
```

---

## P09 — Company / Department / Employee goal cascade

Aligned to **NIVY-GOAL-CASCADE** diagram:

```
Vision / North Star
  → Strategy
    → Annual Goals (Company)
      → Quarterly Objectives (Company + Department)
        → Monthly Targets (Department + Person)
          → Weekly Objectives (Person / Team)
            → Daily Priorities (Person)
              → Task / Output
                → KPI / Result / Evidence
```

### Cascade rules

1. Every **Department Goal** must reference a parent **Company Goal** (or be explicitly marked independent with Owner approval).
2. Every **Employee Goal** must reference a parent **Department Goal** (or Role Responsibility).
3. Goals without a linked Plan are allowed only as `Status: Draft` or marked `unplanned` with review date.
4. Cascade is recorded via `Parent Goal ID` on the child Goal record.

### Example chain (illustrative — replace with real IDs when populated)

| Level | Example ID | Example name |
|---|---|---|
| Company Goal | COMP-GOAL-001 | Grow international advisory revenue 2026 |
| Department Goal | SALES-GOAL-001 | Generate qualified pipeline for ADV |
| Employee Goal | PERS-001-GOAL-001 | Close N advisory clients in Q1 |
| Plan | SALES-PLAN-2026-Q1 | Q1 Sales Plan |
| Project | PROJ-ADV-Pipeline2026 | Advisory Pipeline System |
| Task | PROJ-ADV-Pipeline2026-TASK-003 | Run weekly outreach sequence |
| Work | …-WORK-2026-10-03 | 3 Oct outreach block |
| Output | …-OUT-001 | 12 qualified leads logged |

---

## P10 — Annual → Quarterly → Monthly → Weekly → Daily planning

Aligned to **NIVY-PLANNING-CADENCE** diagram:

| Cadence | Focus | Owner | Typical artifacts |
|---|---|---|---|
| **Annual** | Vision, Strategy, Annual Goals, Budget | CEO / STR | COMP-PLAN-[yyyy], STRAT docs |
| **Quarterly** | Objectives, Department Goals, Capacity | Dept Owners + PMO | [DEPT]-PLAN-[yyyy]-Q[n] |
| **Monthly** | Targets, Projects, Resource allocation | Dept Owners / PMO | Project status, capacity notes |
| **Weekly** | Priorities, Tasks, Owners, Dependencies | Team leads / Individuals | Weekly plan / task board |
| **Daily** | Top priorities, Work blocks, Outputs, Exceptions | Individual | Daily Work records |
| **Review** | Actual vs target → Lessons → Adjust | All levels | Review records (Phase 3) |

### Planning record minimum

Every Plan (any cadence) must include:
- Plan ID, Cadence, Period start/end
- Linked Goal IDs
- Owner
- Status
- Linked child Plans or Projects (where applicable)

Daily planning is expressed as **Work** records linked to **Tasks**, not a separate Plan type unless a team needs a formal daily plan document.

---

## P11 — Daily / recurring work, priorities, dependencies

### Daily execution model

```
Weekly Plan / Task list
  → Daily priority selection (max 3–5 P0/P1 items per person)
    → Work blocks (time-boxed)
      → Output(s)
        → Update Task status
          → Log blockers / exceptions
```

### Priority scale

| Priority | Meaning |
|---|---|
| P0 | Blocker / same-day critical |
| P1 | Must complete this week |
| P2 | Scheduled; flexible within period |
| P3 | Backlog / nice-to-have |

### Dependencies

- Task `Dependencies` field lists prerequisite Task IDs.
- A Task may not move to `Done` while a listed dependency is not `Done` (unless Owner accepts risk and records Decision).
- Recurring work: set `Recurring: Yes` + cadence (daily/weekly/monthly); each occurrence creates a Work instance.

### Daily Work log (lightweight template)

```markdown
# Daily Work — [Person] — [YYYY-MM-DD]

| Task ID | Priority | Planned | Actual | Output ID | Status | Notes |
|---|---|---|---|---|---|---|
| | | | | | | |

Blockers / Exceptions:
Tomorrow carry-forward:
```

Store under the person's department `Records/` or linked project `Working Docs/` as appropriate. Prefer system task tools (TickTick / GitHub) when integrated; this template is the canonical fallback.

---

## P12 — Employee responsibility → work allocation

Aligned to **NIVY-RESPONSIBILITY-RACI-MAP** diagram:

```
Company Goal / Outcome
  → Department Owner (Accountable)
    → Role / Responsible Executor
      → Support / Consulted
        → Approver (if distinct)
          → Evidence / Output
            → KPI / Review
              → Escalate / Reassign
```

### Responsibility record

```
ID: [ROLE]-RESP-[nnn]
Role ID / Owner Role:
Name of responsibility:
Description:
Linked Goal IDs:
Linked Process / SOP codes:
Typical Tasks / recurring Work:
KPI IDs:
```

### Allocation rules

1. **Accountable** (A) = one Owner Role per Goal / Project / Document (Doc 01 + Doc 04).
2. **Responsible** (R) = person(s) who perform the Work; recorded on Task and Work.
3. **Consulted** (C) / **Informed** (I) = per document metadata or Project RACI.
4. Work allocation = assigning Tasks to Persons who hold the relevant Role/Responsibility.
5. Overload signal: if a Person has more open P0+P1 Tasks than capacity allows, escalate to Department Owner (Exception path — Phase 4).

### Seed responsibility examples

| Responsibility ID | Role | Responsibility | Linked area |
|---|---|---|---|
| CEO-ROLE-001-RESP-001 | Founder/CEO | Final strategy and capital decisions | Company Goals |
| SALES-ROLE-001-RESP-001 | Head of Sales | Pipeline and revenue targets | SALES Goals / Plans |
| PMO-ROLE-001-RESP-001 | Head of PMO | Project milestone control | Projects / Milestones |
| CS-ROLE-001-RESP-001 | CS Lead | Delivery quality and retention | CS Goals / Outputs |

*Full RACI matrices live with the relevant Project Charter or Department README; this model defines the object and link rules only.*

---

## Traceability (Phase 2 exit check)

A representative chain must be expressible:

**Company Goal → Department Goal → Employee Goal → Plan → Project → Task → Daily Work → Output**

Using the ID patterns and linkage fields above. Population of real IDs is operational work; the model and templates are the contract.

---

## What was reused vs. created

| Reused | Created in this document |
|---|---|
| Doc 01, Brands, Company-Overview, Org-Chart | Function registry seed |
| 02_PROJECTS template + naming | Goal/Plan/Initiative/Milestone/Task/Work/Output field specs |
| Goal Cascade diagram | Cascade rules + Parent Goal ID |
| Planning Cadence diagram | Cadence table + Plan minimum fields |
| RACI diagram | Responsibility record + allocation rules |
| Canonical Object Model | Operationalized for P07–P12 |

No second hierarchy or parallel project system was created.

---

## Open items (not blockers for Phase 2 exit)

- Populate real Company/Department/Employee Goals for current year
- Confirm remaining Brand codes (ACAD, ALNC, JOBS, CARE)
- Expand Function and Responsibility registries as roles stabilize
- Wire TickTick / GitHub Issues as Task system of record when integration is ready (P17)
