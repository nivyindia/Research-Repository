# KPI & Management Review Model — Company OS V7

**Code:** ALL-STRAT-004  
**Title:** KPI, Report, Dashboard, Review, Decision, Change and Evidence Model  
**Department:** ALL  
**Type:** STRAT  
**PARA Bucket:** Resource  
**Version:** v1.0  
**Lifecycle Status:** Draft  
**Confidentiality:** Internal  
**Owner (Accountable):** CEO Office / Workspace Admin  
**Responsible:** Ops Head / PMO / Dept Owners  
**Created Date:** 2026-10-03  
**Last Updated:** 2026-10-03  
**Next Review:** 2027-01-03  
**Tags:** KPI, review, decision, change, evidence, dashboard  
**Related Documents:** Canonical-Object-Model.md, Strategy-Execution-Model.md, Goal-Registry.md, dashboard.md, GOVERNANCE/07-Governance-Health-AI-Policy.md  
**Related Diagrams:** NIVY-REVIEW-LOOP, NIVY-DECISION-ESCALATION-FLOW, NIVY-GOAL-CASCADE

> **Purpose:** Define the management control loop so every KPI result can lead to Review → Decision → Change → Evidence.  
> **Rule:** REUSE Review Loop diagram, Decision/Escalation diagram, Doc 07 health metrics, and existing dashboard.md. Create record templates only where missing.

---

## P13 — KPI → Report → Dashboard → Review

### Control chain

```
Goal / Output
  → KPI (metric + target + owner + frequency)
    → Report (period aggregation)
      → Dashboard (live or generated view)
        → Review (formal management review)
          → Decision
            → Change / Action
              → Result + Evidence
```

Aligned to **NIVY-REVIEW-LOOP**: Plan → Execute → Capture Evidence → Review → Decide/Adjust → Next Cycle.

### KPI record

```
ID: [SCOPE]-KPI-[nnn]     (SCOPE = COMP | [DEPT] | [PROJ] | [PERS] | [BRAND])
Name:
Description:
Owner (Accountable):
Linked Goal IDs:
Linked Object IDs: (Output / Process / Project as applicable)
Metric definition: (formula / data source)
Unit:
Target:
Baseline: (optional)
Frequency: Daily | Weekly | Monthly | Quarterly | Annual
Direction: Higher-is-better | Lower-is-better | Target-band
Status: Draft | Active | Retired
Confidentiality:
Evidence source: (system / report path / manual)
```

### Report record

Uses Doc 02 type **REP** where the report is a document.

```
ID: [DEPT]-REP-[period] or document code
Name:
Period start / end:
KPI IDs covered:
Owner:
Summary values: (actual vs target per KPI)
Variance notes:
Linked Dashboard IDs:
Status: Draft | Published
```

### Dashboard

| Scope | Purpose | Existing / target |
|---|---|---|
| Documentation health | Orphan, stale, unowned, broken links | dashboard.md + dashboard-generate.yml (Doc 07 §9) |
| Company management | Company Goals / KPIs / financial-commercial | *To build views (P25)* |
| Department | Dept Goals, projects, KPIs, capacity | *P22* |
| Project | Milestone, task, output status | Project Working Docs / board |
| Employee | Goals, tasks, daily work, personal KPIs | *P23* |
| Daily execution | Priorities, blockers, outputs | Strategy-Execution-Model daily log |

**Rule:** One fact has one source (Doc 07 Canonical-Source Rule). Dashboards reference KPI/Report IDs; they do not invent alternate metrics.

### Review record

```
ID: [SCOPE]-REV-[yyyy-mm] or [yyyy-mm-dd]
Name: (e.g. Weekly Ops Review 2026-10-03)
Scope: Company | Department | Project | Employee | Daily
Cadence: Daily | Weekly | Monthly | Quarterly | Ad-hoc
Owner / Chair:
Participants:
Input KPI IDs / Report IDs / Dashboard refs:
Period covered:
Actual vs target summary:
Decisions raised: (Decision IDs)
Actions / Changes: (Change IDs)
Next review date:
Evidence / minutes link: (MEET or REC document)
Status: Scheduled | Completed | Cancelled
```

### Review cadence (minimum)

| Level | Cadence | Typical chair |
|---|---|---|
| Company | Quarterly (+ monthly pulse optional) | CEO / STR |
| Department | Monthly | Dept Owner |
| Project | Per milestone / weekly status | Project Owner / PMO |
| Employee | Monthly (or per probation/performance cycle) | Manager |
| Daily execution | Daily standup / end-of-day log | Individual / Team lead |
| Documentation health | Weekly auto + Quarterly audit | Workspace Admin |

---

## P14 — Decision / Change / Exception / Evidence records

Aligned to **NIVY-DECISION-ESCALATION-FLOW**:

```
Issue / Decision required
  → Classify (Routine | Operational | Strategic | Risk)
    → Check SOP / Policy / Authority
      → Role Owner decides
        → Approval required? → Escalate if yes
          → Record Decision + rationale
            → Execute + Capture Evidence
              → Review / Learn
```

### Decision record

```
ID: [SCOPE]-DEC-[nnn]
Title:
Date:
Classification: Routine | Operational | Strategic | Risk
Triggered by: Review ID | Issue ID | Exception ID | Ad-hoc
Owner (decider):
Approver: (if different)
Options considered:
Decision outcome:
Rationale:
Linked Change IDs:
Linked Evidence / Record IDs:
Status: Proposed | Approved | Rejected | Superseded
```

### Change record

```
ID: [SCOPE]-CHG-[nnn]
Title:
Decision ID: (required)
Type: Process | SOP | System | Org | Goal/Plan | Other
Description of change:
Owner (implementer):
Target objects: (SOP code, Process ID, System ID, etc.)
Implementation plan / steps:
Rollback plan: (if applicable)
Due date:
Status: Planned | In Progress | Implemented | Verified | Rolled back
Evidence IDs:
Result / verification notes:
```

### Exception record

```
ID: [SCOPE]-EXC-[nnn]
Title:
Date raised:
Raised by:
Related Issue ID: (if any)
Related Process / SOP:
Description: (deviation from standard)
Impact:
Interim handling:
Escalation path taken:
Linked Decision ID:
Linked Change ID: (corrective)
Status: Open | Mitigated | Closed | Accepted-risk
Learning / SOP update required: Yes/No
```

### Issue record (companion to Exception)

```
ID: [SCOPE]-ISS-[nnn]
Title:
Date:
Reporter:
Severity: Low | Medium | High | Critical
Category: Operational | Quality | System | People | Customer | Other
Description:
Linked objects:
Exception ID: (if escalated to exception handling)
Decision ID:
Status: Open | In Progress | Resolved | Closed
Resolution summary:
```

### Evidence / Record

Uses Doc 02 type **REC** when stored as a document.

```
ID: [DEPT]-REC-[nnn] or attachment reference
Linked object IDs: (Work, Output, Decision, Change, Review, KPI actual)
Type: Approval | Completion | Meeting minutes | Screenshot | Export | Other
Location / path / URL:
Captured by:
Captured date:
Retention: (per policy)
```

**Rule:** Every Decision that results in action must produce at least one Change or an explicit "no change" note. Every implemented Change must produce Evidence. Every Review must list Decision IDs raised (or "none").

---

## Management views (inputs for P22–P25)

| View | Primary inputs |
|---|---|
| Company | COMP Goals, COMP KPIs, financial/commercial reports, quarterly Review |
| Department | DEPT Goals, DEPT KPIs, projects, monthly Review |
| Project | Milestones, Tasks, Outputs, project KPIs |
| Employee | Person Goals, Tasks, Work log, personal KPIs |
| Daily execution | Daily priorities, Work blocks, blockers, Outputs |
| Operational health | Doc health dashboard + process KPIs |
| Financial / commercial | FIN reports + SALES/CS KPIs |

---

## KPI Registry seed (illustrative)

| KPI ID | Name | Scope | Frequency | Target | Owner | Linked Goal | Status |
|---|---|---|---|---|---|---|---|
| COMP-KPI-001 | Company OS phase completion | Company | Monthly | 100% of planned phases for period | Workspace Admin | COMP-GOAL-001 | Active |
| COMP-KPI-002 | Documentation health — unowned docs | Company | Weekly | 0 | Workspace Admin | COMP-GOAL-001 | Active |
| SALES-KPI-001 | Qualified pipeline (ADV) | Department | Weekly | *TBD* | Head of Sales | SALES-GOAL-001 | Draft |
| CS-KPI-001 | On-time delivery rate | Department | Monthly | *TBD* | CS Lead | — | Draft |

*Replace TBD targets when leadership confirms. Documentation health metrics already computed by dashboard-generate.yml.*

---

## End-to-end management path (Phase 3 exit check)

```
KPI actual (from Report/Dashboard)
  → Review (Actual vs target)
    → Decision (Continue | Correct | Escalate | Reprioritize | Close)
      → Change (if corrective)
        → Result
          → Evidence (REC / attachment)
            → Next cycle Plan update
```

Illustrative chain for this program:

| Step | Example |
|---|---|
| KPI | COMP-KPI-001 — Phase completion |
| Report / Dashboard | Combined Progress Tracker + doc health dashboard |
| Review | Phase gate reviews (Phase 0, 1, 2, …) |
| Decision | Proceed to next phase / hold for human input |
| Change | New model files, tracker updates |
| Evidence | Git commits + this document set |

---

## What was reused vs. created

| Reused | Created |
|---|---|
| NIVY-REVIEW-LOOP diagram | KPI / Report / Review field specs |
| NIVY-DECISION-ESCALATION-FLOW | Decision / Change / Exception / Issue / Evidence field specs |
| Doc 07 health dashboard metrics | Management cadence table |
| dashboard.md + dashboard-generate.yml | KPI registry seed |
| Doc 02 REP / REC types | Linkage rules to Goal / Plan / Project |
| Canonical + Strategy-Execution models | — |

No parallel review system or second dashboard hierarchy was created.

---

## Open items (not blockers for Phase 3 exit)

- Populate real KPI targets for Sales, CS, Finance
- Department/Employee/Company management dashboard views (P22–P25)
- Meeting→Decision→Action formal template (P26)
- Full Issue→Exception→Learning loop operationalization (P27)
