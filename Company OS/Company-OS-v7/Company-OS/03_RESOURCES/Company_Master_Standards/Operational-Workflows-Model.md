# Operational Workflows Model — Company OS V7

**Code:** ALL-STRAT-005  
**Title:** Operational Workflows Model  
**Department:** ALL  
**Type:** STRAT  
**PARA Bucket:** Resource  
**Version:** v1.0  
**Lifecycle Status:** Draft  
**Confidentiality:** Internal  
**Owner (Accountable):** Ops Head / Workspace Admin  
**Responsible:** PMO / Dept Owners  
**Created Date:** 2026-10-03  
**Last Updated:** 2026-10-03  
**Next Review:** 2027-01-03  
**Tags:** workflows, SOP, lifecycle, customer, talent, meeting, issue, capacity  
**Related Documents:** Canonical-Object-Model.md, Strategy-Execution-Model.md, KPI-Management-Review-Model.md, GOVERNANCE/04-Classification-Naming-Rulebook.md  
**Related Diagrams:** NIVY-SOP-ARCHITECTURE, NIVY-SALES-ACQUISITION-FLOW, NIVY-SERVICE-DELIVERY-FLOW, NIVY-TALENT-PIPELINE, NIVY-DECISION-ESCALATION-FLOW, NIVY-FINANCE-FLOW

> **Purpose:** Connect major operational workflows to the canonical object model.  
> **Rule:** REUSE existing diagrams and Doc 04 lifecycle. Define object linkage and minimum records only where missing.

---

## P15 — Document / Process / SOP lifecycle

### Document lifecycle (Doc 04 — authoritative)

```
Draft → Under Review → Approved → Published → Under Revision → Retired (Archive)
```

| Stage | Required |
|---|---|
| Draft | Owner, Code, metadata header |
| Under Review | Consulted notified |
| Approved | Owner sign-off; Next Review set |
| Published | Informed notified; searchable |
| Under Revision | Old version stays Published until new Approved |
| Retired | Superseded By set; move to 04_ARCHIVE |

### Process → SOP → Work → QC → Evidence

Aligned to **NIVY-SOP-ARCHITECTURE**:

```
Business Process
  → SOP / Policy
    → Trigger + Inputs
      → Roles / RACI
        → Step-by-step execution
          → Tools / Systems
            → Output + Evidence
              → KPI / Quality check
                → Exception / Escalation
                  → Version / Review / Archive
```

**Process record (minimum)**

```
ID: [DEPT]-PROC-[nnn]
Name:
Owner:
Linked SOP codes:
Trigger:
Inputs:
Outputs:
KPI IDs:
Exception path: (Exception record or SOP section)
Status: Active | Under Revision | Retired
```

**SOP** uses Doc 02 type SOP + Doc 04 metadata. Optional section (Doc 07 §6): Common Exceptions / What to Do If…

**QC acceptance:** every operational Output linked to a Process/SOP should have explicit acceptance criteria (pass/fail or checklist FORM). Failed QC → Issue or Exception.

---

## P16 — Customer / Vendor / Product / Service master data

### Master records (minimum fields)

**Customer**
```
ID: CUST-[nnn]
Name / legal name:
Brand: (ADV | NXT | …)
Status: Lead | Opportunity | Active | Inactive | Churned
Owner (Accountable): Sales / CS role
Primary contact:
Segment / ICP:
Linked Opportunity / Project / Contract IDs:
Source system: (CRM when integrated)
```

**Vendor**
```
ID: VEND-[nnn]
Name:
Category:
Owner: Ops / Admin / Finance
Status: Active | Inactive
Contract / payment terms ref:
```

**Partner**
```
ID: PART-[nnn]
Name:
Type: Referral | Franchise | Alliance | Other
Owner:
Status: Active | Inactive
```

**Product / Service**
```
ID: PROD-[nnn] or SVC-[nnn]
Name:
Brand:
Department (delivery):
Description:
Pricing ref: (document or system)
Status: Active | Retired
```

**Source of truth:** until CRM/ERP is designated, maintain registries under `03_RESOURCES/Company_Master_Standards/` or department Records. Integration contracts (P17) will point systems at these IDs.

*No full populated master lists are created here — only the schema so later phases do not invent conflicting IDs.*

---

## Major commercial workflow — Lead → Retention

Aligned to **NIVY-SALES-ACQUISITION-FLOW** + **NIVY-SERVICE-DELIVERY-FLOW**:

```
Market / ICP
  → Lead sources
    → Prospect data (research → verify → enrich → segment)
      → Outreach + follow-up
        → Qualify
          → Discovery / meeting
            → Proposal / quote
              → Negotiation
                → Close / contract / onboard  → Customer (Active)
                  → Scope → Project → Plan
                    → Tasks / execution
                      → QC
                        → Client delivery / approval
                          → Billing → Collection
                            → Retention / repeat / referral
```

### Object linkage

| Stage | Primary objects |
|---|---|
| Lead / Prospect | Customer (Status: Lead/Opportunity), Task, Work |
| Opportunity | Customer, Goal/KPI (pipeline), Meeting |
| Close | Customer → Active, Contract Record, Project |
| Delivery | Project, Task, Work, Output, QC (FORM/REC) |
| Billing / Collection | Record (FIN), Customer, Project |
| Retention | Customer, CS Goal/KPI, Review |

---

## Talent workflow — Need → Employee

Aligned to **NIVY-TALENT-PIPELINE**:

```
Workforce need / Role
  → Source candidates
    → Screening
      → Interview
        → Paid test / assignment
          → Select / offer
            → Onboard / train
              → Probation + KPI/QC
                → Regular role → Develop / Retain / Exit
```

### Object linkage

| Stage | Primary objects |
|---|---|
| Need | Role, Responsibility, capacity (P28) |
| Candidate | Person (candidate status), Records |
| Select / Offer | Decision, Record |
| Onboard | Person → Employee, Training Tasks, SOP |
| Probation | Person Goals, KPIs, Review |
| Regular | Role assignment, ongoing Work |

---

## P26 — Meeting → Decision → Action → Follow-up

```
Meeting (MEET document or calendar event)
  → Agenda
    → Discussion
      → Decision(s)  → Decision records
        → Action items → Tasks (owner + deadline)
          → Follow-up → next Meeting or Review
            → Evidence (minutes REC/MEET)
```

**Meeting record minimum**

```
ID: [DEPT]-MEET-[yyyy-mm-dd] or Doc 02 MEET code
Title:
Date / time:
Chair:
Participants:
Agenda items:
Decision IDs raised:
Action Task IDs: (owner, due date)
Minutes / Evidence path:
Next meeting date:
```

**Rule:** Every Decision from a meeting gets a Decision ID (KPI-Management-Review-Model). Every action gets a Task with owner and deadline. Unclosed actions are carried to the next meeting agenda.

---

## P27 — Issue → Exception → Escalation → Resolution → Learning

Builds on P14 records:

```
Issue
  → (if process deviation) Exception
    → Escalate (per Decision Escalation flow)
      → Decision
        → Corrective Change
          → Resolution
            → Root cause note
              → SOP / Process update (if needed)
                → KPI / Review feedback
                  → Evidence
```

| Step | Record |
|---|---|
| Issue | ISS-[nnn] |
| Exception | EXC-[nnn] |
| Escalation | Decision path + optional EXC status |
| Resolution | Issue/Exception Status = Resolved/Closed |
| Root cause | Field on Exception or linked REC |
| Corrective action | Change record |
| Learning | SOP Under Revision → new version; FAQ update (Doc 07 §7) |
| KPI review | Linked KPI actual + Review record |

---

## P28 — Capacity / workload / resource allocation

### Principles

1. Capacity is owned at Department (and optionally Team) level.
2. Workload = sum of open P0+P1 Tasks + committed Project effort for assigned Persons.
3. Allocation happens when assigning Tasks to Persons who hold the relevant Role/Responsibility (P12).
4. Overload = open critical work exceeds agreed capacity → Exception or escalate to Dept Owner.

### Capacity snapshot (lightweight)

```
Period: [week / month]
Department / Person:
Available capacity: (hours or story points)
Committed: (from Tasks / Projects)
Buffer:
Notes / hiring need:
```

Store under department Reports/ or PMO Records when used. Full resource system is optional until headcount justifies it.

---

## Integration touchpoints (forward to P17)

| Workflow | Likely systems |
|---|---|
| Lead → Customer | CRM, Email, LinkedIn, WhatsApp |
| Delivery | Project tool, GitHub, shared drive |
| Billing | Finance / accounting |
| Talent | HR / ATS, Email |
| Meetings | Calendar, MEET docs |
| Issues | GitHub Issues, TickTick, internal log |

Central integration contracts are defined in Phase 6 (P17); workflows above only require that master IDs (CUST, PERS, PROJ, etc.) remain stable across systems.

---

## Phase 4 exit check

Operational records can connect to the canonical model:

| Workflow | Traceable to |
|---|---|
| Document lifecycle | Doc 04 + Process/SOP IDs |
| Lead→Retention | Customer → Project → Output → KPI → Review |
| Talent→Employee | Role → Person → Goal → Work → KPI |
| Meeting→Follow-up | Meeting → Decision → Task → Evidence |
| Issue→Learning | Issue → Exception → Decision → Change → SOP → Review |
| Capacity | Person/Dept → Task load → Exception if overload |

---

## What was reused vs. created

| Reused | Created |
|---|---|
| Doc 04 lifecycle | Process record minimum |
| SOP Architecture diagram | Master-data field schemas (Customer, Vendor, Partner, Product/Service) |
| Sales / Delivery / Talent diagrams | Workflow ↔ object linkage tables |
| Decision Escalation + P14 records | Meeting record + P26/P27/P28 rules |
| Canonical + Strategy + KPI models | — |

No parallel CRM, HR, or SOP system was created inside the repo.

---

## Open items (not blockers for Phase 4 exit)

- Populate Customer/Vendor/Product registries when CRM data is available
- Written SOPs for each major process step (department work)
- Integration contracts (P17) and AI agent registry (P18)
- Formal capacity tool if needed at scale
