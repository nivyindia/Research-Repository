# Google Drive → Nivy Talent System Migration Plan

**Date:** 2026-09-27  
**Repo:** nivyindia/Research-Repository  
**Target root:** `Nivy Talent System/`  
**Source:** User Google Drive (HR, Employees, Training & Learning, Course, Planning, Company Drive, etc.)

## Objective

Google Drive में scattered talent acquisition, recruitment, screening, training, HR policies और jobs-related files को systematically extract करके `Nivy Talent System` के existing folder structure में organize करना। Plan phases में divide है; execution उसी structure के अंदर content fill करेगा।

## Existing Target Structure (Already Present)

```
Nivy Talent System/
├─ 00-START-HERE
├─ 01-SYSTEM-ARCHITECTURE
├─ 02-TALENT-SOURCING
├─ 03-CANDIDATE-ACQUISITION
├─ 04-SCREENING
├─ 05-PAID-ASSESSMENT
├─ 06-SCORING
├─ 07-TRAINING
├─ 08-PAID-INTERNSHIP
├─ 09-PROBATION
├─ 10-TALENT-POOL
├─ 11-JOB-ALLOCATION
├─ 12-CANDIDATE-COMMUNICATION
├─ 13-AUTOMATION
├─ 14-INSTITUTE-PARTNERSHIPS
├─ 15-CITY-SOURCING
├─ 16-ROLE-WISE-SYSTEMS
├─ 17-SOPS
├─ 18-TEMPLATES
├─ 19-PROMPTS
├─ 20-DATABASE-SCHEMAS
├─ 21-METRICS-KPIS
├─ 22-RESEARCH
├─ 23-TOOLS-PLATFORMS
├─ 24-IMPLEMENTATION-ROADMAP   ← this plan lives here
├─ 25-TESTING
├─ 99-ARCHIVE
├─ MASTER-INDEX.md
├─ PROGRESS-TRACKER.md
└─ README.md
```

Related sibling folders already containing related material:
- `Nivy Jobs/` (Fresher course, BDE guidelines, HR policies extracts, client scripts)
- `Nivy Academy/` (AI courses, modules, tracks)

## Phase 0 — Inventory & Classification (DONE in this document)

### High-value Google Drive sources identified

| Source Location | File / Folder | Relevance | Proposed Target Folder |
|---|---|---|---|
| HR / Recruitment | HR Pre Interview Exams | Screening questions | 04-SCREENING + 05-PAID-ASSESSMENT |
| HR / Recruitment | Sales Screening Question Paper | Role-wise screening | 04-SCREENING + 16-ROLE-WISE-SYSTEMS/Sales |
| HR / Fresher Screening Forms | Contact Information (Form + Responses) | Candidate acquisition | 03-CANDIDATE-ACQUISITION |
| HR | HR Policies + Copy of HR Policies | Policies / handbook | 17-SOPS + 09-PROBATION |
| HR / Policies | Human Resources (HR) Department Policies | Core HR SOP | 17-SOPS |
| HR / Policies | Master Company Policies & Procedures Manual | Company-wide | 17-SOPS + 01-SYSTEM-ARCHITECTURE |
| HR / Policies | Administration & Management Department Rules | Admin SOP | 17-SOPS |
| HR / Policies | Operations Department Policies | Ops | 17-SOPS |
| HR / Policies | Sales Marketing & Customer Support Policies | Sales policies | 16-ROLE-WISE-SYSTEMS/Sales |
| HR / Policies | Purchase / Procurement Department Policies | Support | 17-SOPS |
| HR / Policies | HR Assessment | Assessment rubric | 05-PAID-ASSESSMENT + 06-SCORING |
| HR | HR Tasks | Recruiter/HR task list | 17-SOPS |
| HR | Types of Employee Allowances | Compensation | 09-PROBATION / 18-TEMPLATES |
| HR | Work Guidelines | Work rules | 17-SOPS |
| HR | Attendance (Sheet) | Ops data | 21-METRICS-KPIS (reference only) |
| Employees / Training | Accounting folder | Role training | 07-TRAINING + 16-ROLE-WISE-SYSTEMS/Accounts |
| Employees / Training | Digital Marketing folder | Role training | 07-TRAINING + 16-ROLE-WISE-SYSTEMS/Marketing |
| Root / Docs | Sales Professional Academy | Training curriculum | 07-TRAINING + Nivy Academy cross-link |
| Root | Freshers motivation | Onboarding / culture | 07-TRAINING + 08-PAID-INTERNSHIP |
| Root | Goal alignment | Performance | 09-PROBATION + 21-METRICS-KPIS |
| Root | Organization_HR_Document_Roles_and_Responsibilities_Matrix.xlsx | Roles matrix | 01-SYSTEM-ARCHITECTURE + 16-ROLE-WISE-SYSTEMS |
| Planning | Master Plan full | Strategic context | 22-RESEARCH (provenance) |
| Company Drive / 02 Human Resources | Recruitment, Policies, Work Ethics, Employee Files | Duplicate / newer copies | Cross-check & merge |
| Company Drive / 05 Training & Learning | Course v1.1, Fresher Career, HR Training, SMM-VA | Training material | 07-TRAINING |
| Course | Version 1.1 | Course content | 07-TRAINING / Nivy Academy |
| Students Internship Certificate + Letterhead | Templates | 18-TEMPLATES + 08-PAID-INTERNSHIP |

### Classification rules

1. **PII / personal candidate data** (form responses with names/phones) → do **not** push raw PII into public repo. Extract only structure, field list, sample anonymised rows, and process description.
2. **Policies & SOPs** → Markdown conversion, clean headings, version note + original Drive link in front-matter.
3. **Question papers / assessments** → place under 04-SCREENING or 05-PAID-ASSESSMENT; split by role if possible.
4. **Training curricula** → 07-TRAINING; cross-link to `Nivy Academy` and `Nivy Jobs` where overlap exists.
5. **Role matrices / org design** → 01-SYSTEM-ARCHITECTURE + 16-ROLE-WISE-SYSTEMS.
6. **Duplicates** → keep newest or most complete; older copies go to 99-ARCHIVE with note.

## Phase 1 — Core Screening & Acquisition Assets (Priority 1)

**Goal:** Make candidate intake + screening operational docs available inside Talent System.

| Action | Source | Destination path |
|---|---|---|
| Extract & convert HR Pre Interview Exams | Drive HR/Recruitment | `04-SCREENING/hr-pre-interview-exams.md` |
| Extract & convert Sales Screening Question Paper | Drive HR/Recruitment | `04-SCREENING/sales-screening-question-paper.md` + `16-ROLE-WISE-SYSTEMS/Sales/` |
| Document Contact Information form structure (fields only, no PII) | Fresher Screening Forms | `03-CANDIDATE-ACQUISITION/contact-information-form-schema.md` |
| Create acquisition process note from form + responses pattern | same | `03-CANDIDATE-ACQUISITION/fresher-intake-process.md` |
| Extract HR Assessment | Policies | `05-PAID-ASSESSMENT/hr-assessment.md` + `06-SCORING/` |

**Deliverable:** Screening question bank started + intake schema documented.

## Phase 2 — Policies, SOPs & Handbooks (Priority 1)

| Action | Source | Destination path |
|---|---|---|
| Convert HR Policies (primary) | HR | `17-SOPS/hr-policies.md` |
| Convert Human Resources Department Policies | Policies | `17-SOPS/hr-department-policies.md` |
| Convert Master Company Policies & Procedures Manual | Policies | `17-SOPS/master-company-policies.md` |
| Convert Work Guidelines | HR | `17-SOPS/work-guidelines.md` |
| Convert HR Tasks | HR | `17-SOPS/hr-tasks-checklist.md` |
| Convert Admin / Ops / Purchase / Sales policies | Policies | respective under `17-SOPS/` or role folders |
| Convert Types of Employee Allowances | HR | `18-TEMPLATES/employee-allowances.md` |
| Cross-link existing Nivy Jobs Employee Handbook extracts | Nivy Jobs | Update MASTER-INDEX + PROGRESS-TRACKER |

**Deliverable:** Single source of truth for HR/recruiter SOPs inside Talent System.

## Phase 3 — Training & Fresher Systems (Priority 1)

| Action | Source | Destination path |
|---|---|---|
| Extract Sales Professional Academy | Root Docs | `07-TRAINING/sales-professional-academy.md` |
| Extract Freshers motivation | Root | `07-TRAINING/freshers-motivation.md` |
| Extract Goal alignment | Root | `09-PROBATION/goal-alignment.md` |
| Inventory & extract Course v1.1 / Fresher Career / HR Training / SMM-VA | Company Drive 05 + Course | `07-TRAINING/` subfolders by track |
| Extract Accounting & Digital Marketing training folders | Employees/Training | `16-ROLE-WISE-SYSTEMS/Accounts/` + `Marketing/` + `07-TRAINING/` |
| Link / reconcile with existing Nivy Jobs 90-Day Fresher Course & BDE Guidelines | Nivy Jobs | Cross-references in 07-TRAINING README |
| Internship certificate + letterhead templates | Root | `18-TEMPLATES/` + `08-PAID-INTERNSHIP/` |

**Deliverable:** Training library started; fresher pathway materials consolidated.

## Phase 4 — Roles, Architecture & Org Design

| Action | Source | Destination path |
|---|---|---|
| Extract Organization_HR_Document_Roles_and_Responsibilities_Matrix | Spreadsheet | `01-SYSTEM-ARCHITECTURE/roles-and-responsibilities-matrix.md` (+ CSV if useful) |
| Map roles into 16-ROLE-WISE-SYSTEMS packs | matrix + policies | Computer Ops, Accounts, Sales, Marketing, HR, etc. |
| Update 01-SYSTEM-ARCHITECTURE with lifecycle alignment from policies | — | Architecture docs |

## Phase 5 — Research Provenance & Archive

| Action | Source | Destination |
|---|---|---|
| Master Plan full (strategic context) | Planning | `22-RESEARCH/master-plan-context.md` (summary + link) |
| Older / duplicate policy copies | various | `99-ARCHIVE/` with provenance note |
| Update MASTER-INDEX.md and PROGRESS-TRACKER.md | — | Reflect completed items |

## Phase 6 — Verification & Progress Update

1. Every migrated file has YAML/front-matter or header with:
   - Original Drive file name + file_id or web link
   - Migration date
   - Status (extracted / cleaned / needs review)
2. No raw PII committed.
3. PROGRESS-TRACKER checkboxes updated for:
   - Screening question bank
   - Training/remediation system (partial)
   - Internship SOP (templates)
   - Existing solution landscape (Drive sources)
4. Short status note in `24-IMPLEMENTATION-ROADMAP/README.md`.

## Execution Order (Immediate Next)

1. **Phase 1** — Screening + Acquisition (highest operational value)
2. **Phase 2** — Policies / SOPs
3. **Phase 3** — Training materials
4. Phase 4 → 5 → 6

## Notes / Constraints

- GitHub push uses text content (Markdown preferred). Binary/Office files will be converted to Markdown/CSV where possible; large binaries avoided unless essential.
- Form response sheets containing personal data will only contribute schema + process docs.
- If a Drive file is already substantially present in `Nivy Jobs` or `Nivy Academy`, we create a thin pointer + delta only (avoid full duplication).
- All work stays inside `Nivy Talent System/` unless cross-repo promotion is explicitly requested later.

---

**Status of this plan:** Created 2026-09-27. Ready for Phase 1 execution.
