# Goal Registry — Company OS V7

**Code:** ALL-STRAT-003  
**Title:** Goal Registry  
**Department:** ALL  
**Type:** STRAT  
**PARA Bucket:** Resource  
**Version:** v1.0  
**Lifecycle Status:** Draft  
**Confidentiality:** Internal  
**Owner (Accountable):** CEO Office  
**Responsible:** STR / PMO  
**Created Date:** 2026-10-03  
**Last Updated:** 2026-10-03  
**Next Review:** 2027-01-03  
**Tags:** goals, cascade, registry  
**Related Documents:** Strategy-Execution-Model.md, Canonical-Object-Model.md  
**Related Diagrams:** NIVY-GOAL-CASCADE

> **Purpose:** Canonical list of Goals with cascade links. Seeded with one illustrative end-to-end chain for model validation. Replace illustrative rows with real goals when leadership confirms.

---

## Registry

| Goal ID | Name | Scope | Period | Parent Goal ID | Owner | Status | Linked Plan IDs | Notes |
|---|---|---|---|---|---|---|---|---|
| COMP-GOAL-001 | Establish Company OS as single operating system for Nivy group | Company | Annual 2026 | — | Founder/CEO | Active | COMP-PLAN-2026 | Illustrative / system goal |
| COMP-GOAL-002 | Grow international revenue across ADV and NXT | Company | Annual 2026 | — | Founder/CEO | Draft | — | *Needs confirm — target %* |
| SALES-GOAL-001 | Build qualified pipeline for Advisory (ADV) | Department | Quarterly 2026-Q4 | COMP-GOAL-002 | Head of Sales | Draft | SALES-PLAN-2026-Q4 | Illustrative cascade child |
| PERS-CEO-GOAL-001 | Approve and publish Company OS V7 baseline | Person | Monthly 2026-10 | COMP-GOAL-001 | Founder/CEO | Active | — | Phase gate ownership |

---

## Example cascade (validation of P08/P09)

```
COMP-GOAL-001 (Company)
  └── PERS-CEO-GOAL-001 (Employee / Owner)
        └── Plan: COMP-PLAN-2026 (Annual — Company OS standardization)
              └── Project: Company OS V7 Standardization (this program)
                    └── Tasks: Phase 0…Phase 10 (see Combined Progress Tracker)
                          └── Work: daily implementation sessions
                                └── Output: Canonical-Object-Model, Strategy-Execution-Model, trackers, commits
```

```
COMP-GOAL-002 (Company) [Draft]
  └── SALES-GOAL-001 (Department) [Draft]
        └── Plan: SALES-PLAN-2026-Q4 [to create when activated]
              └── Project / Tasks / Work / Output — populate when goal is activated
```

---

## Rules

1. New Goals are added here first (or in an approved system of record that syncs here).
2. Department and Person Goals must set `Parent Goal ID` unless explicitly independent.
3. Status values: Draft | Active | Achieved | Missed | Retired.
4. Linked Plan IDs must exist in a Plan record or Project Charter.
5. This registry does not replace the Goal Cascade diagram; it supplies the data the diagram describes.

---

## Plan seed (companion)

| Plan ID | Cadence | Period | Goal IDs | Owner | Status |
|---|---|---|---|---|---|
| COMP-PLAN-2026 | Annual | 2026 | COMP-GOAL-001 | CEO Office | Active |
| SALES-PLAN-2026-Q4 | Quarterly | 2026-Q4 | SALES-GOAL-001 | Head of Sales | Draft |
