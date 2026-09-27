# VA Hiring → Nivy Talent System
## Phase-Wise Implementation Plan + Tracker

**Created:** 2026-09-27  
**Repo:** nivyindia/Research-Repository  
**Target root:** `Nivy Talent System/`  
**Source:** Google Drive (careers.nivy / Nivy HR accounts)  
**Status:** Ready for Phase 1 execution

---

## Objective

Google Drive में scattered VA Hiring Funnel documents (SOPs, stages, templates, forms, dashboards) को systematically extract करके `Nivy Talent System` के existing structure में organize करना।  
No raw PII (candidate names, phones, emails, responses) will be committed to GitHub.

---

## Source Inventory (Confirmed from Drive)

### Core SOPs & Stage Documents
| Drive File | File ID (short) | Type | Proposed Destination |
|---|---|---|---|
| S0.0 - VA Hiring Funnel – Step-by-Step System | 1jD22mk6... | Doc | `17-SOPS/va-hiring-funnel-master.md` |
| VA HIRING FUNNEL – SOP | 1_6xG_vgl... | Doc | `17-SOPS/va-hiring-funnel-sop.md` |
| SOP: STAGE 0 – JOB AWARENESS | 1fifA3jt... | Doc | `17-SOPS/stage-00-job-awareness.md` |
| S1 - VA Job Description | 1p79jWJ1... | Doc | `18-TEMPLATES/va-job-description.md` |
| S2 - Google Form with Screening | 1yj4-Ksga... | Doc | `03-CANDIDATE-ACQUISITION/screening-form-structure.md` |
| S3 Trial Task | 1YyrE42y... | Doc | `05-PAID-ASSESSMENT/va-trial-task.md` |
| S4 - Interview | 1kVgMqax... | Doc | `04-SCREENING/va-interview-questions.md` |
| S5: Live Orientation Call | 1l547jbg... | Doc | `17-SOPS/stage-05-orientation.md` |
| S6 Final Selection + Contract Signing | 121ua_C7... | Doc | `17-SOPS/stage-06-selection-contract.md` |
| S7: Training & Probation Period (3 Months) | 1iphaeoX... | Doc | `07-TRAINING/va-training-probation.md` + `09-PROBATION/` |
| S8: Permanent Hiring - Offer Letter | 1eI3tdC1... | Doc | `18-TEMPLATES/va-offer-letter.md` |
| VA Offer Letter | 1dfa9M4u... | Doc | `18-TEMPLATES/va-offer-letter-v2.md` |
| VA Agreement | 1qshVutu... | Doc | `18-TEMPLATES/va-agreement.md` |

### Supporting Assets
| Drive File | Type | Destination |
|---|---|---|
| VA Hiring Dashboard | Spreadsheet | `21-METRICS-KPIS/va-hiring-dashboard-schema.md` (structure only) |
| VA Hiring + Pre-Interview Test | Form | `03-CANDIDATE-ACQUISITION/pre-interview-test-structure.md` |
| VA Screening / Responses | Form + Sheet | Schema only → `03-CANDIDATE-ACQUISITION/` |
| Nivy SDR Responses / lead lists | Sheets | Structure only (no PII) |
| Nivy Part Time Appointment Setter | Form | `16-ROLE-WISE-SYSTEMS/Appointment-Setter/` |

### Other Useful (Non-VA) Assets Found
| Item | Use | Destination Suggestion |
|---|---|---|
| 75M All Niches Datas folder | Lead gen niche data | `02-TALENT-SOURCING/` or separate Sales research |
| USA MoldMojo Prompt sheet for B-Roll | Content/AI video prompts | `Nivy Artisan` or Marketing research |
| TRAINEE'S FILE | Trainee outputs / hooks | `07-TRAINING/` |

---

## Phase-Wise Plan

### Phase 0 — Inventory & Classification
**Status:** ✅ DONE (2026-09-27)

- [x] Drive search completed
- [x] VA Hiring files inventoried
- [x] Target folders mapped
- [x] PII rules confirmed

---

### Phase 1 — Core SOPs & Master Funnel (Priority P0)
**Goal:** Complete hiring funnel documentation available as clean Markdown.

| # | Action | Source | Destination | Status |
|---|---|---|---|---|
| 1.1 | Extract & convert S0.0 Master Funnel | Drive Doc | `17-SOPS/va-hiring-funnel-master.md` | ⬜ Pending |
| 1.2 | Extract & convert VA HIRING FUNNEL – SOP | Drive Doc | `17-SOPS/va-hiring-funnel-sop.md` | ⬜ Pending |
| 1.3 | Extract Stage 0 SOP | Drive Doc | `17-SOPS/stage-00-job-awareness.md` | ⬜ Pending |
| 1.4 | Extract Stage 5 Orientation | Drive Doc | `17-SOPS/stage-05-orientation.md` | ⬜ Pending |
| 1.5 | Extract Stage 6 Selection + Contract | Drive Doc | `17-SOPS/stage-06-selection-contract.md` | ⬜ Pending |
| 1.6 | Update 17-SOPS/README.md with new files | — | `17-SOPS/README.md` | ⬜ Pending |

**Exit criteria:** All core stage SOPs present as Markdown with source attribution.

---

### Phase 2 — Screening, Assessment & Templates (Priority P0)
**Goal:** Screening questions, trial task, interview bank, offer/agreement templates ready.

| # | Action | Source | Destination | Status |
|---|---|---|---|---|
| 2.1 | Extract Interview questions (S4) | Drive Doc | `04-SCREENING/va-interview-questions.md` | ⬜ Pending |
| 2.2 | Extract Trial Task (S3) | Drive Doc | `05-PAID-ASSESSMENT/va-trial-task.md` | ⬜ Pending |
| 2.3 | Extract Job Description (S1) | Drive Doc | `18-TEMPLATES/va-job-description.md` | ⬜ Pending |
| 2.4 | Extract Offer Letter (S8 + VA Offer Letter) | Drive Docs | `18-TEMPLATES/va-offer-letter.md` | ⬜ Pending |
| 2.5 | Extract VA Agreement | Drive Doc | `18-TEMPLATES/va-agreement.md` | ⬜ Pending |
| 2.6 | Document Form structure (no PII) | Forms | `03-CANDIDATE-ACQUISITION/` | ⬜ Pending |

**Exit criteria:** Screening bank + templates usable by recruiters.

---

### Phase 3 — Training, Probation & Metrics (Priority P1)
**Goal:** Training/probation content + dashboard schema.

| # | Action | Source | Destination | Status |
|---|---|---|---|---|
| 3.1 | Extract Training & Probation (S7) | Drive Doc | `07-TRAINING/va-training-probation.md` + `09-PROBATION/` | ⬜ Pending |
| 3.2 | Document Hiring Dashboard schema | Spreadsheet | `21-METRICS-KPIS/va-hiring-dashboard-schema.md` | ⬜ Pending |
| 3.3 | Cross-link with Nivy Academy / Nivy Jobs if overlap | Existing folders | Update READMEs | ⬜ Pending |

**Exit criteria:** Training path documented; metrics structure clear.

---

### Phase 4 — Role Packs, Automation & Supporting Assets (Priority P2)
**Goal:** Role-specific systems + any automation notes.

| # | Action | Source | Destination | Status |
|---|---|---|---|---|
| 4.1 | Create Appointment Setter role pack | Forms + JD | `16-ROLE-WISE-SYSTEMS/Appointment-Setter/` | ⬜ Pending |
| 4.2 | Document any Apps Script / automation notes | Scripts | `13-AUTOMATION/` | ⬜ Pending |
| 4.3 | Inventory 75M Niches data (high-level) | Folder | `02-TALENT-SOURCING/niche-data-index.md` | ⬜ Pending |
| 4.4 | MoldMojo B-Roll prompts (if relevant to content roles) | Doc | Archive or Marketing research | ⬜ Pending |

---

### Phase 5 — Verification, Index Update & Close
**Goal:** Clean state, trackers updated, ready for next research cycle.

| # | Action | Status |
|---|---|---|
| 5.1 | Every migrated file has header: original name, Drive link/ID, migration date, status | ⬜ Pending |
| 5.2 | No PII committed | ⬜ Pending |
| 5.3 | Update MASTER-INDEX.md | ⬜ Pending |
| 5.4 | Update PROGRESS-TRACKER.md (tick completed items) | ⬜ Pending |
| 5.5 | Update this plan status to COMPLETED | ⬜ Pending |
| 5.6 | Short summary note in 24-IMPLEMENTATION-ROADMAP/README.md | ⬜ Pending |

---

## Execution Rules

1. **Markdown first** — Convert Google Docs to clean Markdown.
2. **No PII** — Never push candidate responses, names, phones, personal emails.
3. **Source attribution** — Every file header must include original Drive name + link/ID + date.
4. **Duplicates** — Keep newest/most complete version; older → `99-ARCHIVE/`.
5. **Stay inside** `Nivy Talent System/` unless explicitly told to promote elsewhere.
6. **One phase at a time** — Finish Phase 1 fully before starting Phase 2.

---

## Quick Status Tracker (Live)

| Phase | Name | Priority | Status | % |
|---|---|---|---|---|
| 0 | Inventory & Classification | — | ✅ Done | 100% |
| 1 | Core SOPs & Master Funnel | P0 | ⬜ Not Started | 0% |
| 2 | Screening, Assessment & Templates | P0 | ⬜ Not Started | 0% |
| 3 | Training, Probation & Metrics | P1 | ⬜ Not Started | 0% |
| 4 | Role Packs & Supporting Assets | P2 | ⬜ Not Started | 0% |
| 5 | Verification & Close | — | ⬜ Not Started | 0% |

**Overall Migration Progress:** 10% (Inventory only)

---

## Next Immediate Action

→ Start **Phase 1.1**: Extract `S0.0 - VA Hiring Funnel – Step-by-Step System` and push as `17-SOPS/va-hiring-funnel-master.md`

---

**Plan Owner:** Grok (Autonomous)  
**Last Updated:** 2026-09-27
