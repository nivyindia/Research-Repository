# Canonical Object Model — Company OS V7

**Code:** ALL-STRAT-001  
**Title:** Canonical Object and Master-Data Model  
**Department:** ALL  
**Type:** STRAT  
**PARA Bucket:** Resource  
**Version:** v1.0  
**Lifecycle Status:** Draft  
**Confidentiality:** Internal  
**Owner (Accountable):** Workspace Admin / CEO Office  
**Responsible:** Ops Head  
**Created Date:** 2026-10-03  
**Last Updated:** 2026-10-03  
**Next Review:** 2027-01-03  
**Tags:** object-model, master-data, canonical, relationships  
**Related Documents:** GOVERNANCE/01-Department-Code-Registry, GOVERNANCE/02-Document-Type-Code-Registry, Brands.md, Org-Chart.md, Company-Overview.md

> **Purpose:** Single verified cross-object relationship model for Company OS V7.  
> **Rule:** REUSE existing registries. This document defines the objects, required attributes, and relationships. It does **not** replace Doc 01, Doc 02, Brands.md, or any other existing source of truth.

---

## 1. Primary hierarchy (operating chain)

```
Company
  → Brand
    → Department
      → Function
        → Role
          → Person
            → Responsibility
              → Goal
                → Plan
                  → Initiative
                    → Project
                      → Milestone
                        → Task
                          → Work
                            → Output
                              → KPI
                                → Report
                                  → Dashboard
                                    → Review
                                      → Decision
                                        → Change
                                          → Record
                                            → Evidence
```

Every operational outcome must be traceable along this chain (or a documented subset of it).

---

## 2. Cross-cutting master objects

These attach to one or more points in the primary hierarchy:

| Object | Attaches primarily to |
|---|---|
| Customer | Brand, Department (Sales/CS), Project, Output |
| Vendor | Department (Ops/Admin/Finance), Project |
| Partner | Brand, Department |
| Product / Service | Brand, Department (RND/Sales/CS) |
| Process | Department, Function |
| SOP | Process, Department, Role |
| Document | Any object (via Doc 04 metadata) |
| System | Department, Integration, AI Agent |
| AI Agent | Department, System, Process |
| Integration | System ↔ System |
| Issue | Any object |
| Exception | Issue, Process, Decision |

---

## 3. Object definitions

For every object the following attributes apply where relevant:

| Attribute | Meaning |
|---|---|
| stable ID/code | Unique, never reused |
| name | Human-readable |
| owner | Accountable role (from Doc 01 or Role registry) |
| status | Lifecycle state |
| lifecycle | Allowed transitions |
| classification | Confidentiality (Public / Internal / Confidential / Restricted) |
| source of truth | Canonical file or system |
| relationships | Parent / child / related IDs |
| evidence | Required proof of existence or completion |
| creation/update metadata | Created, updated, version |
| responsible department/role | From Doc 01 |

### 3.1 Organizational objects

| Object | ID pattern | Source of truth (existing) | Notes |
|---|---|---|---|
| **Company** | COMP-001 | Company-Overview.md | Single legal/group entity: Billion Dreams United |
| **Brand** | ADV, NXT, … | Doc 01 §C + Brands.md | Confirmed: ADV, NXT. Tentative: ACAD, ALNC, JOBS, CARE |
| **Department** | CEO, STR, OPS, … | Doc 01 §A/B + departments.json | 16 core + ALL + PROJ |
| **Function** | [DEPT]-FN-[nnn] | *To be populated under each department* | Sub-capability inside a department (e.g. SALES-FN-001 Lead Gen) |
| **Role** | [DEPT]-ROLE-[nnn] | Doc 01 Owner Role column + Org-Chart.md | Accountable / Responsible roles; people fill roles |
| **Person** | PERS-[nnn] or employee ID | Org-Chart.md (to be extended) / HR system | Real human; may hold multiple Roles |
| **Responsibility** | [ROLE]-RESP-[nnn] | RACI (diagram + future registry) | Specific duty of a Role; links to Goals and Work |

### 3.2 Strategy & execution objects

| Object | ID pattern | Source of truth | Notes |
|---|---|---|---|
| **Goal** | [SCOPE]-GOAL-[nnn] | Goal Cascade diagram + future Goal registry | Scope = COMP / [DEPT] / [PERS] |
| **Plan** | [SCOPE]-PLAN-[yyyy] or [nnn] | Planning Cadence diagram + future Plan registry | Annual / Quarterly / Monthly / Weekly / Daily |
| **Initiative** | [DEPT]-INIT-[nnn] | Strategy docs / roadmap | Multi-project strategic thrust |
| **Project** | PROJ-[ShortCode] | 02_PROJECTS/ + PROJ-DOC type | Time-bound; uses existing project template |
| **Milestone** | [PROJ]-MS-[nnn] | Inside project Working Docs / Charter | Checkpoint with date and acceptance criteria |
| **Task** | [PROJ]-TASK-[nnn] or system task ID | Project system / TickTick / GitHub Issues | Atomic work unit; may be recurring |
| **Work** | [TASK]-WORK-[date] or daily log ID | Daily execution record | Actual effort performed on a Task |
| **Output** | [TASK/WORK]-OUT-[nnn] | Deliverable / artifact | Concrete result of Work |

### 3.3 Measurement & control objects

| Object | ID pattern | Source of truth | Notes |
|---|---|---|---|
| **KPI** | [SCOPE]-KPI-[nnn] | Future KPI registry + Review Loop diagram | Metric with owner, target, frequency |
| **Report** | [DEPT]-REP-[period] | Doc 02 type REP | Periodic aggregation of KPI / activity data |
| **Dashboard** | DASH-[scope] | dashboard.md + dashboard-generate.yml | Live or generated view of KPIs/Reports |
| **Review** | [SCOPE]-REV-[yyyy-mm] | Review Loop diagram | Formal management review meeting/record |
| **Decision** | [SCOPE]-DEC-[nnn] | Decision/Escalation diagram + future Decision log | Outcome of Review or escalation |
| **Change** | [SCOPE]-CHG-[nnn] | Future Change record | Implementation of a Decision; may update SOP/Process |
| **Record** | [DEPT]-REC-[nnn] | Doc 02 type REC | Evidence of an event (approval, completion, meeting) |
| **Evidence** | Linked to Record / Output / Change | Same as Record or attachment | Proof retained for audit |

### 3.4 Cross-cutting objects (summary)

| Object | ID pattern | Initial source |
|---|---|---|
| Customer | CUST-[nnn] | Future master (CRM) |
| Vendor | VEND-[nnn] | Future master |
| Partner | PART-[nnn] | Future master |
| Product/Service | PROD-/SVC-[nnn] | Future master (per Brand) |
| Process | [DEPT]-PROC-[nnn] | Linked to SOP |
| SOP | [DEPT]-SOP-[nnn] | Doc 02 + department SOPs/ |
| Document | [DEPT]-[TYPE]-[nnn] | Doc 02 + Doc 04 metadata |
| System | SYS-[nnn] | Future integration registry |
| AI Agent | AGENT-[nnn] | Future AI agent registry (P18) |
| Integration | INT-[nnn] | Doc 10 + Automation map |
| Issue | ISS-[nnn] | Future issue log |
| Exception | EXC-[nnn] | Linked to Issue / Decision |

---

## 4. Required relationships (minimum)

| From | To | Cardinality | Required link field |
|---|---|---|---|
| Company | Brand | 1:N | brand.company_id |
| Brand | Department (operating) | N:M | via Org / ownership |
| Department | Function | 1:N | function.department_code |
| Function | Role | 1:N | role.function_id |
| Role | Person | N:M | assignment (current) |
| Role | Responsibility | 1:N | responsibility.role_id |
| Responsibility | Goal | N:M | goal.responsibility_ids |
| Goal | Plan | 1:N | plan.goal_id |
| Plan | Initiative / Project | 1:N | initiative/project.plan_id |
| Project | Milestone | 1:N | milestone.project_id |
| Milestone / Project | Task | 1:N | task.parent_id |
| Task | Work | 1:N | work.task_id |
| Work | Output | 1:N | output.work_id |
| Output / Goal | KPI | N:M | kpi.linked_object_ids |
| KPI | Report | N:M | report.kpi_ids |
| Report | Dashboard | N:M | dashboard.report_ids |
| Dashboard / KPI | Review | N:M | review.input_ids |
| Review | Decision | 1:N | decision.review_id |
| Decision | Change | 1:N | change.decision_id |
| Change / Work / Output | Record / Evidence | 1:N | record.linked_object_id |

Cross-cutting objects must carry at least one foreign key into the primary chain (department_code, project_id, person_id, or document code).

---

## 5. Lifecycle (shared pattern)

Where applicable, objects follow:

```
Draft → Under Review → Approved → Published/Active → Under Revision → Retired/Archived
```

Document-specific lifecycle is governed by Doc 04. Project/Task/Work may use operational statuses (Not Started / In Progress / Blocked / Done / Cancelled) in addition to the document lifecycle when they are records.

---

## 6. Source-of-truth map (existing vs. to-create)

| Object group | Existing canonical source | Gap |
|---|---|---|
| Company, Brand, Department | Company-Overview, Brands, Doc 01 | Brand confirmations; Function list |
| Role, Person | Doc 01 Owner Role; Org-Chart | Person registry; Role assignment table |
| Responsibility | RACI diagram | Responsibility registry |
| Goal, Plan, Initiative | Goal Cascade + Planning Cadence diagrams | Goal/Plan registries with IDs |
| Project, Milestone, Task | 02_PROJECTS template; PROJ-DOC type | Milestone/Task ID conventions in use |
| Work, Output | — | Daily work / output record template |
| KPI, Report, Dashboard, Review | Review Loop diagram; dashboard.md | KPI registry |
| Decision, Change, Exception, Issue | Decision/Escalation diagram | Decision/Change/Issue record templates |
| Document, SOP, Process | Doc 02, Doc 04, SOP Architecture diagram | Process registry |
| Customer, Vendor, Partner, Product | — | Master-data registries (Phase 4 / P16) |
| System, Integration, AI Agent | Automation map, AIOS diagram | Agent + Integration registries (Phase 6) |
| Evidence / Record | Doc 02 REC type | Evidence standard (P14/P32) |

**This model does not create parallel registries where one already exists.** New registries are created only for gaps listed above, in later phases, using the ID patterns defined here.

---

## 7. Validation rules (minimum)

1. No object may exist without an Owner (Accountable role).
2. Every Goal must link to at least one Plan or be explicitly marked "unplanned".
3. Every Task must link to a Project or a recurring Work definition.
4. Every KPI must have a target, frequency, and owner.
5. Every Decision must link to a Review or an Issue/Exception.
6. Every Change must link to a Decision and produce Evidence/Record.
7. Document codes must follow Doc 01 + Doc 02; object IDs above are logical and may map 1:1 to document codes where the object is itself a document.

---

## 8. Traceability scenarios (definition of done for the model)

**Scenario A (strategy → evidence)**  
Company Goal → Department Goal → Employee Goal → Plan → Project → Task → Daily Work → Output → KPI → Review → Decision → Change → Evidence

**Scenario B (document)**  
Document Draft → Review → Approve → Publish → Use → Change → Supersede → Archive

**Scenario C (issue)**  
Issue → Exception → Escalation → Decision → Corrective Change → SOP Update → KPI Review → Evidence

These scenarios are the acceptance tests for later phases (P32). The model above is the contract they must satisfy.

---

## 9. Change control

- Updates to this model require Owner approval and a version bump.
- New object types are added here first, then any supporting registry.
- Existing Doc 01 / Doc 02 / Brands remain the authority for department, document-type, and brand codes; this model only references them.

---

## 10. Implementation status (P06)

| Item | Status |
|---|---|
| Object list (primary + cross-cutting) | Defined |
| Attribute set | Defined |
| Relationship matrix | Defined |
| ID patterns | Defined |
| Source-of-truth map | Defined |
| Reuse of existing registries | Confirmed (no duplicates created) |
| Function / Role / Person / Responsibility / Goal / Plan / KPI / Decision / Change registries | Deferred to later phases (P07–P14) with patterns fixed here |

**P06 exit:** One verified object/relationship model exists and is the single reference for all subsequent phases.
