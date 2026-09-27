# Master Implementation Plan — Google Drive → Research-Repository
## Talent Acquisition & Jobs Training Migration

**Version:** 2.0  
**Date:** 2026-09-27  
**Repo:** `nivyindia/Research-Repository`  
**Branch:** `main`  
**Canonical folder:** `docs/plans/talent-acquisition-migration/`  
**Status:** IN PROGRESS

---

## 1. Objective

Google Drive में मौजूद **Talent Acquisition System**, **Hiring Funnels**, **Jobs Training**, **Screening**, **HR Policies**, **SOPs** और related useful company documents को systematically:

1. Identify करना
2. Organize करना
3. Markdown / structured form में convert करना
4. `Nivy Jobs/Talent-Acquisition/` के अंदर proper folder structure में migrate करना
5. Source links + inventory + tracker maintain करना

ताकि GitHub **source of truth** बने और बाद में Nivy Jobs / Academy / ATS systems में reuse हो सके।

---

## 2. Scope

### In Scope
- VA / CA Hiring Funnel (S0–S8)
- Hiring SOPs
- BDE Fresher Screening
- Growth Partner Network materials
- Freelancer contracts / T&Cs
- Offer letters & employment agreements (templates)
- leads.xlsx schema / summary (no full PII dump without approval)
- Messaging / sales-related docs if useful

### Out of Scope (unless explicitly approved)
- Full resume / candidate PII dumps
- Personal response sheets with emails/phones
- Inventing new content (only migrate + structure + metadata)

---

## 3. Target Folder Structure (GitHub)

```
Nivy Jobs/
├── 00-INDEX-AND-README.md
├── Talent-Acquisition/
│   ├── 00-README.md
│   ├── 01-VA-CA-Hiring-Funnel/
│   │   ├── 00-README.md
│   │   ├── S0-Step-by-Step-System.md
│   │   ├── S1-Job-Description.md
│   │   ├── S2-Google-Form-Screening.md
│   │   ├── S3-Trial-Task.md
│   │   ├── S4-Interview.md
│   │   ├── S5-Live-Orientation-Call.md
│   │   ├── S6-Final-Selection-Contract.md
│   │   ├── S7-Training-Probation.md
│   │   ├── S8-Offer-Letter.md
│   │   └── source-links.md
│   ├── 02-BDE-Fresher-Screening/
│   │   └── 00-README.md
│   ├── 03-Growth-Partner-Network/
│   │   └── 00-README.md
│   ├── 04-Freelancer-Contracts/
│   │   └── 00-README.md
│   ├── 05-Databases-Resumes-Volunteers/
│   │   └── 00-README.md          # index only by default
│   └── 06-SOPs-and-Automation/
│       ├── VA-Hiring-Funnel-SOP.md
│       └── SOP-Stage-0-Job-Awareness.md
└── ... (existing Nivy Jobs content remains)

docs/plans/talent-acquisition-migration/
├── 00-MASTER-IMPLEMENTATION-PLAN.md      ← this file
├── 01-TRACKER.md                         ← live status tracker
└── 02-INVENTORY.md                       ← full source inventory
```

---

## 4. Phase-Wise Plan

### Phase 0 — Discovery & Planning
**Goal:** Find all relevant Drive assets + write plan + create tracker

| Task | Description | Owner |
|------|-------------|-------|
| 0.1 | Scan Google Drive root + key folders | AI |
| 0.2 | Identify hiring / training / SOP / contract files | AI |
| 0.3 | Inspect existing `Nivy Jobs/` in repo | AI |
| 0.4 | Write Master Implementation Plan | AI |
| 0.5 | Create Tracker + Inventory files | AI |
| 0.6 | Commit plan files to `docs/plans/talent-acquisition-migration/` | AI |

**Exit criteria:** Plan + Tracker + Inventory committed; human can review.

---

### Phase 1 — Structure & Seed READMEs
**Goal:** Create empty/correct folder tree + index files in GitHub

| Task | Description |
|------|-------------|
| 1.1 | Create `Nivy Jobs/Talent-Acquisition/` tree |
| 1.2 | Seed `00-README.md` at Talent-Acquisition root |
| 1.3 | Seed `01-VA-CA-Hiring-Funnel/00-README.md` |
| 1.4 | Seed remaining subfolder READMEs (02–06) |
| 1.5 | Update master index if needed |

**Exit criteria:** Folder structure exists; READMEs describe purpose and status.

---

### Phase 2 — Core VA/CA Hiring Funnel Migration (P0)
**Goal:** Migrate S0–S8 + core SOPs as clean Markdown

| Task | File / Content |
|------|----------------|
| 2.1 | S0 Step-by-Step System |
| 2.2 | S1 Job Description |
| 2.3 | S2 Google Form Screening |
| 2.4 | S3 Trial Task |
| 2.5 | S4 Interview |
| 2.6 | S5 Live Orientation Call |
| 2.7 | S6 Final Selection + Contract |
| 2.8 | S7 Training & Probation |
| 2.9 | S8 Offer Letter |
| 2.10 | source-links.md (Drive IDs) |
| 2.11 | VA Hiring Funnel SOP |
| 2.12 | SOP Stage 0 Job Awareness |

**Method per file:** Read from Drive → convert to Markdown → add front-matter (source ID, export date) → push → mark tracker DONE.

**Exit criteria:** All S0–S8 + 2 SOPs live under `01-VA-CA-Hiring-Funnel/` and `06-SOPs-and-Automation/`.

---

### Phase 3 — Secondary Hiring Assets (P1)
**Goal:** BDE screening, Growth Partner, Freelancer, Agreement templates

| Task | Description |
|------|-------------|
| 3.1 | BDE Fresher Screening (Quiz 1/2/3 structure + READMEs) |
| 3.2 | Growth Partner Network form description + index |
| 3.3 | Freelancer Contract T&Cs |
| 3.4 | VA Agreement (full) |
| 3.5 | VA Offer Letter (extra template) |
| 3.6 | Part-Time Appointment Setter / SDR form summary |

**Exit criteria:** Subfolders 02–04 populated; legal templates under 01 or 04 as appropriate.

---

### Phase 4 — Databases & Sensitive Data (P2 — gated)
**Goal:** Index only unless human approves full export

| Task | Description |
|------|-------------|
| 4.1 | Inventory Resumes / Volunteers folders (names + counts only) |
| 4.2 | leads.xlsx schema summary (no full dump) |
| 4.3 | CS Data / other non-PII sheets if useful |
| 4.4 | Explicit human approval required before any PII content commit |

**Exit criteria:** Index README in `05-Databases-Resumes-Volunteers/`; no PII without written approval in tracker.

---

### Phase 5 — Deduplication, Cross-links & Polish
**Goal:** Clean structure, link existing Nivy Jobs content, final verification

| Task | Description |
|------|-------------|
| 5.1 | Compare Google Doc vs .docx versions; mark canonical |
| 5.2 | Cross-link existing `Nivy Jobs` files (Employee Handbook, BDE Guidelines, 90-Day Course, etc.) |
| 5.3 | Ensure every migrated file has source Drive ID |
| 5.4 | Update all READMEs + Tracker to 100% accurate status |
| 5.5 | Final inventory checklist sign-off |

**Exit criteria:** Tracker shows all in-scope items DONE or SKIPPED-with-reason; no broken structure.

---

### Phase 6 — Handoff & Close
**Goal:** Status report + ready for downstream use

| Task | Description |
|------|-------------|
| 6.1 | Write final status report in this folder |
| 6.2 | Update AUTONOMOUS / master repo notes if required |
| 6.3 | Mark plan COMPLETE in Tracker |
| 6.4 | Handoff note for Nivy Jobs product / Academy / ATS design |

**Exit criteria:** Plan status = COMPLETE; human can use migrated material.

---

## 5. Execution Rules (Mandatory)

1. **Preserve source** — Never delete from Drive; only copy/export.
2. **No invented content** — Only migrate what exists; structure + metadata only.
3. **PII caution** — Resumes, response sheets, personal data → index only unless human approves.
4. **One logical unit per commit** where practical.
5. **Idempotent** — Re-running a phase must not duplicate files.
6. **Tracker is source of truth for progress** — Update `01-TRACKER.md` on every meaningful change.
7. **Follow repo autonomous loop** where applicable: claim → work → verify → commit → release.

---

## 6. Success Criteria

- [ ] All identified core hiring-funnel docs present as Markdown under `Nivy Jobs/Talent-Acquisition/`
- [ ] Clear inventory with Drive source IDs
- [ ] Tracker accurately reflects DONE / IN_PROGRESS / PENDING / SKIPPED
- [ ] Existing `Nivy Jobs` content not broken
- [ ] Plan + Tracker + Inventory live under `docs/plans/talent-acquisition-migration/`
- [ ] Repo remains usable as research/source warehouse

---

## 7. Related Files

| File | Purpose |
|------|---------|
| [01-TRACKER.md](01-TRACKER.md) | Live phase + task status |
| [02-INVENTORY.md](02-INVENTORY.md) | Full Drive source inventory |
| Earlier plan (v1) | `docs/plans/GDRIVE-TALENT-ACQUISITION-MIGRATION-PLAN-v1.0-2026-09-27.md` (superseded by this v2) |

---

**Plan Author:** Grok (xAI) via connected Google Drive + GitHub tools  
**Last updated:** 2026-09-27
