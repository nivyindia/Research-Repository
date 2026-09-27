# Google Drive → Nivy Talent System — Phase-Wise Implementation Plan

**Date:** 2026-09-27  
**Repo:** nivyindia/Research-Repository  
**Target root:** `Nivy Talent System/`  
**Source:** Live Google Drive scan (HR, Employees, Course, Company Drive, root docs)  
**Tracker:** [03-DRIVE-CONTENT-MIGRATION-TRACKER.md](./03-DRIVE-CONTENT-MIGRATION-TRACKER.md)

---

## Objective

Drive mein scattered talent acquisition, recruitment, screening, training, HR policies aur related files ko extract karke existing Talent System folder structure mein organize karna — phases mein, tracker ke saath.

## Rules

1. **No raw PII** — candidate names/phones/emails form responses se repo mein nahi.
2. Har migrated file mein: original Drive name, file_id/link, migration date, status.
3. Markdown preferred; large binaries avoid.
4. Duplicate → newest keep; older → `99-ARCHIVE`.
5. Already in `Nivy Jobs` / `Nivy Academy` → thin cross-link, full duplicate nahi.
6. Work stays in `Research-Repository` until explicit promotion.

## Target Structure (already present)

```
Nivy Talent System/
├─ 00-START-HERE … 25-TESTING, 99-ARCHIVE
├─ MASTER-INDEX.md | PROGRESS-TRACKER.md | README.md
```

---

## Phase Overview

| Phase | Scope | Priority | Status |
|-------|--------|----------|--------|
| **0** | Live Drive inventory + classification | — | ✅ Done |
| **1** | Screening + Candidate Acquisition | P0 | 🔄 In Progress |
| **2** | Policies / SOPs / Handbooks | P0 | ⬜ Pending |
| **3** | Training & Fresher systems | P0 | ⬜ Pending |
| **4** | Roles matrix + Architecture alignment | P1 | ⬜ Pending |
| **5** | Assessments, ranking, templates | P1 | ⬜ Pending |
| **6** | Verification + index/tracker update | — | ⬜ Pending |

---

## Phase 0 — Inventory (DONE)

### Drive folders verified

| Folder | Relevance |
|--------|-----------|
| HR | Recruitment, Policies, Screening forms, Handbook |
| Employees | Training (Accounting, DM), Sales, Work |
| Course | Version 1.1 |
| NivyIndia - Company Drive | 02 HR, 05 Training & Learning |
| Root / Docs | Academy, motivation, ranking, orientation, matrix, certificates |

### High-value file map

| Source | File | Destination |
|--------|------|-------------|
| HR/Recruitment | HR Pre Interview Exams | `04-SCREENING/hr-pre-interview-exams.md` |
| HR/Recruitment | Sales Screening Question Paper | `04-SCREENING/sales-screening-question-paper.md` |
| HR/Fresher Screening Forms | Contact Information form | `03-CANDIDATE-ACQUISITION/` schema only |
| HR | HR Policies, HR Tasks, Work Guidelines, Allowances | `17-SOPS/` + `18-TEMPLATES/` |
| HR/Policies | Dept policies, Master Company Policies, HR Assessment | `17-SOPS/` + `05-PAID-ASSESSMENT/` |
| Root | Sales Professional Academy, Freshers motivation | `07-TRAINING/` |
| Root | Ranking System, Orientation, Basic Training MCQ | `06-SCORING/`, `07-TRAINING/`, `05-PAID-ASSESSMENT/` |
| Root | Roles & Responsibilities Matrix | `01-SYSTEM-ARCHITECTURE/` |
| Root | VA Basic/Advance, HR Training, Sales Training Schedule | `07-TRAINING/` |
| Root | Internship Certificate, Letterhead | `18-TEMPLATES/` + `08-PAID-INTERNSHIP/` |
| Employees/Training | Accounting, Digital Marketing | `16-ROLE-WISE-SYSTEMS/` + `07-TRAINING/` |
| Company Drive/05 | Course v1.1, Fresher Career, HR Training, SMM-VA | `07-TRAINING/` |

---

## Phase 1 — Screening + Acquisition (P0) — IN PROGRESS

**Goal:** Candidate intake + screening papers usable inside Talent System.

| ID | Action | Destination | Status |
|----|--------|-------------|--------|
| 1.1 | HR Pre Interview Exams → Markdown | `04-SCREENING/hr-pre-interview-exams.md` | ✅ Extracted |
| 1.2 | Sales Screening Question Paper → Markdown | `04-SCREENING/sales-screening-question-paper.md` | ✅ Extracted |
| 1.3 | 04-SCREENING README | `04-SCREENING/README.md` | ✅ Extracted |
| 1.4 | Contact form schema (fields only, no PII) | `03-CANDIDATE-ACQUISITION/contact-information-form-schema.md` | ⬜ |
| 1.5 | Fresher intake process note | `03-CANDIDATE-ACQUISITION/fresher-intake-process.md` | ⬜ |
| 1.6 | HR Assessment extract | `05-PAID-ASSESSMENT/hr-assessment.md` | ⬜ |

**Exit criteria:** Screening question bank started; intake schema documented; no PII committed.

---

## Phase 2 — Policies / SOPs (P0)

| ID | Action | Destination |
|----|--------|-------------|
| 2.1 | HR Policies | `17-SOPS/hr-policies.md` |
| 2.2 | HR Department Policies | `17-SOPS/hr-department-policies.md` |
| 2.3 | Master Company Policies | `17-SOPS/master-company-policies.md` |
| 2.4 | Work Guidelines | `17-SOPS/work-guidelines.md` |
| 2.5 | HR Tasks checklist | `17-SOPS/hr-tasks-checklist.md` |
| 2.6 | Admin / Ops / Purchase / Sales policies | `17-SOPS/` or role folders |
| 2.7 | Employee Allowances | `18-TEMPLATES/employee-allowances.md` |
| 2.8 | Cross-link Nivy Jobs Employee Handbook | MASTER-INDEX + README |

---

## Phase 3 — Training & Fresher systems (P0)

| ID | Action | Destination |
|----|--------|-------------|
| 3.1 | Sales Professional Academy | `07-TRAINING/sales-professional-academy.md` |
| 3.2 | Freshers motivation | `07-TRAINING/freshers-motivation.md` |
| 3.3 | Orientation | `07-TRAINING/orientation.md` |
| 3.4 | VA Basic + VA Advance Training | `07-TRAINING/` + role packs |
| 3.5 | HR Training | `07-TRAINING/hr-training.md` |
| 3.6 | Sales Training Schedule | `07-TRAINING/sales-training-schedule.md` |
| 3.7 | Course v1.1 / Fresher Career / SMM-VA inventory | `07-TRAINING/` subfolders |
| 3.8 | Accounting + Digital Marketing training | `16-ROLE-WISE-SYSTEMS/` + `07-TRAINING/` |
| 3.9 | Cross-link Nivy Jobs 90-Day Fresher + BDE Guidelines | READMEs |

---

## Phase 4 — Roles & Architecture (P1)

| ID | Action | Destination |
|----|--------|-------------|
| 4.1 | Roles & Responsibilities Matrix extract | `01-SYSTEM-ARCHITECTURE/roles-and-responsibilities-matrix.md` |
| 4.2 | Map roles into 16-ROLE-WISE-SYSTEMS packs | Sales, HR, Accounts, Marketing, VA, etc. |
| 4.3 | Lifecycle alignment note in architecture | `01-SYSTEM-ARCHITECTURE/` |

---

## Phase 5 — Assessments, Ranking, Templates (P1)

| ID | Action | Destination |
|----|--------|-------------|
| 5.1 | Basic Training MCQ | `05-PAID-ASSESSMENT/basic-training-mcq.md` |
| 5.2 | Ranking System for Employees | `06-SCORING/ranking-system.md` + `09-PROBATION/` |
| 5.3 | Internship Certificate template | `18-TEMPLATES/` + `08-PAID-INTERNSHIP/` |
| 5.4 | Letterhead template | `18-TEMPLATES/letterhead.md` |

---

## Phase 6 — Verification

| ID | Check |
|----|--------|
| 6.1 | Every file has source header (Drive link / id / date) |
| 6.2 | No PII in repo |
| 6.3 | MASTER-INDEX.md updated |
| 6.4 | PROGRESS-TRACKER.md updated |
| 6.5 | This plan + tracker marked current |
| 6.6 | Roadmap README summary accurate |

---

## Execution order

1. Finish Phase 1 remaining items  
2. Phase 2 (policies)  
3. Phase 3 (training)  
4. Phase 4 → 5 → 6  

**Related:** VA Hiring specific plan → [01-VA-HIRING-PHASE-WISE-IMPLEMENTATION-PLAN.md](./01-VA-HIRING-PHASE-WISE-IMPLEMENTATION-PLAN.md) (parallel track where VA funnel assets exist).
