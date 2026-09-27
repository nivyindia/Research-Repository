# Google Drive → Research-Repository: Talent Acquisition & Jobs Training Migration Plan

**Version:** 1.0  
**Date:** 2026-09-27  
**Repo:** nivyindia/Research-Repository  
**Target Branch:** main  
**Status:** PLAN READY — Awaiting execution approval / Phase-1 start

---

## 1. Objective

Google Drive में मौजूद **Talent Acquisition System**, **Hiring Funnels**, **Jobs Training**, **Screening**, **HR Policies** और related research/docs को systematically identify करके, organize करके, और `nivyindia/Research-Repository` के अंदर proper folder structure में migrate करना।

सारा raw + structured material GitHub में copy करके रखा जाएगा ताकि:
- Source of truth GitHub बने
- बाद में Nivy Jobs / Nivy Academy / HR systems में reuse हो सके
- Duplicate / scattered Drive content consolidate हो

---

## 2. Source Inventory (Google Drive — Discovered)

### 2.1 Root-level Relevant Folders

| Folder Name | Drive Folder ID | Relevance |
|-------------|-----------------|-----------|
| **CA Assistant Hiring Funnel** | `1WmFe0J6YF3ptpnmHwCuTB1TfuV5qGLSC` | Full VA/CA hiring pipeline (S0–S8) |
| **Virtual Assistant Hiring Funnel** | `17hYnCGqrUa4V1BP2jRXITTQTTg-Uwbou` | Complete VA hiring system + SOPs + Forms |
| **Fresher BDE Job Screening** | `1TkSWPAjECAI2ASHuy-qvW0FgnNWkimlR` | BDE assessment quizzes & screening |
| **Pocket Income Job** | `10PLWg7KVIX_L8PqeAhEDiQ5X4QjrzXXe` | Growth Partner Network form + responses |
| **DM Freelancer** | `1M5EGQCLGxBjC6Enp0Apg4PYOusGMW-fU` | Freelancer contract T&Cs |
| **Database** | `10SuFDkIvHh2xSKsz4DQ6TblCB5Z0byT2` | Resumes + Volunteers Database |

### 2.2 Key Files inside CA Assistant Hiring Funnel

- `S0 - VA Hiring Funnel – Step-by-Step System.docx`
- `S1 - VA Job Description.docx`
- `S2 - Google Form with Screening.docx`
- `S3 Trial Task_.docx`
- `S4 - Interview.docx`
- `S5_ Live Orientation Call.docx`
- `S6 Final Selection + Contract Signing.docx`
- `S7_ Training & Probation Period (3 Months).docx`
- `S8_ Permanent Hiring - Offer Letter.docx`
- `Step 2 - Hiring Funnel.json`
- `VA Email Applications.xlsx`

### 2.3 Key Files inside Virtual Assistant Hiring Funnel

- Google Docs versions of S0–S8 (newer / primary)
- `VA Screening` (Google Form)
- `VA Screening (Responses)` spreadsheet
- `VA Email Applications` spreadsheet
- SOP subfolder
- Part Time Appointment Setter High Commission subfolder
- Apps Scripts for funnel automation

### 2.4 Other Relevant

- Fresher BDE: Quiz 1, 2, 3 folders (Role Fit, Job Assessment, Student Assessment)
- Pocket Income: Nivy Growth Partner Network form
- DM Freelancer: Freelancer Contract Terms & Conditions form
- Database/Resumes + Volunteers Database
- Root: `leads.xlsx`

> **Note:** Google Forms, Apps Scripts, and binary responses folders will be handled carefully (export as JSON/CSV/MD where possible; link originals in README).

---

## 3. Target Folder Structure in GitHub

Existing top-level folder **`Nivy Jobs`** already contains training, HR policies, BDE guidelines, etc.  
We will **extend** it (not replace) with a clean sub-structure for Talent Acquisition.

```
Nivy Jobs/
├── 00-INDEX-AND-README.md                    # Master index for this domain
├── Talent-Acquisition/
│   ├── 00-README.md
│   ├── 01-VA-CA-Hiring-Funnel/
│   │   ├── S0-Step-by-Step-System.md
│   │   ├── S1-Job-Description.md
│   │   ├── S2-Google-Form-Screening.md
│   │   ├── S3-Trial-Task.md
│   │   ├── S4-Interview.md
│   │   ├── S5-Live-Orientation-Call.md
│   │   ├── S6-Final-Selection-Contract.md
│   │   ├── S7-Training-Probation.md
│   │   ├── S8-Offer-Letter.md
│   │   ├── Hiring-Funnel.json
│   │   ├── source-links.md                   # Original Drive links
│   │   └── raw/                              # Original .docx if exported
│   ├── 02-BDE-Fresher-Screening/
│   │   ├── Quiz-1-Role-Fit/
│   │   ├── Quiz-2-Job-Assessment/
│   │   ├── Quiz-3-Student-Assessment/
│   │   └── 00-README.md
│   ├── 03-Growth-Partner-Network/
│   │   └── ...
│   ├── 04-Freelancer-Contracts/
│   │   └── ...
│   ├── 05-Databases-Resumes-Volunteers/
│   │   └── ... (metadata + index only; no PII dump without review)
│   └── 06-SOPs-and-Automation/
│       └── ...
├── Training-and-Probation/                   # Existing + new training docs
├── HR-Policies/                              # Existing policies consolidated
└── ... (existing files remain)
```

Additional recommended top-level (if needed later):
- `Nivy Academy/` already exists — cross-link training content.

---

## 4. Phased Implementation Plan

### Phase 0 — Preparation (Current)
- [x] Discover relevant Drive folders & files
- [x] Inspect existing `Nivy Jobs/` structure in repo
- [x] Write this Implementation Plan
- [ ] Commit this plan file to repo (this commit)
- [ ] Human review of plan + PII sensitivity confirmation

### Phase 1 — Structure Creation & Inventory Index
1. Create folder tree under `Nivy Jobs/Talent-Acquisition/` (empty placeholders + READMEs).
2. Create `Nivy Jobs/Talent-Acquisition/00-README.md` with full inventory table (Drive ID, name, type, target path, status).
3. Create `Nivy Jobs/00-INDEX-AND-README.md` linking Talent-Acquisition + existing content.
4. Commit structure.

**Deliverable:** Clean empty structure + master index committed.

### Phase 2 — Content Extraction & Conversion (Priority Order)
**Priority P0 (Core Funnel):**
- Virtual Assistant Hiring Funnel (Google Docs S0–S8) → Markdown
- CA Assistant Hiring Funnel (docx versions) → Markdown / keep raw
- Hiring Funnel JSON

**Priority P1:**
- BDE Fresher Screening quizzes structure
- SOPs folder
- Offer Letter, Contract, Training & Probation docs

**Priority P2:**
- Forms metadata + response schema (no full PII dumps)
- Freelancer Contract
- Growth Partner Network form description
- leads.xlsx summary / schema

**Method per file:**
1. `google_drive_read_file` or download artifact
2. Convert to clean Markdown (preserve structure, headings, lists)
3. Add front-matter: source Drive ID, original name, export date, conversion notes
4. Place in correct subfolder
5. Update inventory status → `MIGRATED`

**Binary / large files:** Store in `raw/` subfolder or link only + description.

### Phase 3 — Organization, Deduplication & Cross-linking
- Compare Google Docs vs .docx versions of S0–S8 → keep latest / most complete as canonical, archive other as `archive/`
- Link related existing files in `Nivy Jobs/` (Employee Handbook, BDE Guidelines, 90-Day Course, etc.)
- Add `source-links.md` in each subfolder pointing back to Drive
- Tag files with consistent naming: `S0-...`, `S1-...` etc.

### Phase 4 — Verification & Documentation
- Full inventory checklist: every discovered file has status (Migrated / Linked / Skipped-with-reason)
- README updates
- No accidental PII (resumes, personal emails in response sheets) committed without explicit approval
- Commit message convention: `Migrate: [folder] — [file] to Nivy Jobs/Talent-Acquisition/...`

### Phase 5 — Execution Complete & Handoff
- Final status report committed as `docs/plans/GDRIVE-TALENT-ACQUISITION-MIGRATION-STATUS.md`
- Update any master tracker / AUTONOMOUS-START-CONTINUE if required
- Ready for downstream use in Nivy Jobs product / Academy / ATS design

---

## 5. Execution Rules (Mandatory)

1. **Preserve source** — Never delete original from Drive. Only copy/export.
2. **No invented content** — Only migrate what exists; add structure + metadata only.
3. **PII caution** — Response sheets, resumes, personal data → index only or redact unless human explicitly approves full export.
4. **One logical unit per commit** where practical (or small batches).
5. **Idempotent** — Re-running a phase should not duplicate files.
6. **Follow repo autonomous loop** — Claim task, mark IN_PROGRESS, verify, commit, release.

---

## 6. Immediate Next Actions (after this plan is committed)

1. Human: Approve Phase 1 start (or request changes to structure).
2. AI/Executor: Create the folder tree + inventory README under `Nivy Jobs/Talent-Acquisition/`.
3. Begin Phase 2 with highest-value docs (S0–S8 VA Hiring Funnel).

---

## 7. Success Criteria

- [ ] All identified hiring-funnel core documents present as Markdown (or linked) under `Nivy Jobs/Talent-Acquisition/`
- [ ] Clear inventory with Drive source IDs
- [ ] Existing `Nivy Jobs` content not broken / duplicated unnecessarily
- [ ] Plan + status files live in `docs/plans/`
- [ ] Repo remains usable as research/source warehouse

---

**Plan Author:** Grok (xAI) via connected Google Drive + GitHub tools  
**Canonical location of this plan:** `docs/plans/GDRIVE-TALENT-ACQUISITION-MIGRATION-PLAN-v1.0-2026-09-27.md`
