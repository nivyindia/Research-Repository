# Inventory — Google Drive Sources for Talent Acquisition Migration

**Last updated:** 2026-09-27  
**Related:** [00-MASTER-IMPLEMENTATION-PLAN.md](00-MASTER-IMPLEMENTATION-PLAN.md) · [01-TRACKER.md](01-TRACKER.md)

---

## 1. Root-Level Folders (Relevant)

| Folder Name | Drive Folder ID | Relevance | Migration Target |
|-------------|-----------------|-----------|------------------|
| CA Assistant Hiring Funnel | `1WmFe0J6YF3ptpnmHwCuTB1TfuV5qGLSC` | Full VA/CA pipeline (docx S0–S8) | 01-VA-CA-Hiring-Funnel (secondary) |
| Virtual Assistant Hiring Funnel | `17hYnCGqrUa4V1BP2jRXITTQTTg-Uwbou` | Primary Google Docs S0–S8 + Forms + SOPs | 01-VA-CA-Hiring-Funnel (canonical) |
| Fresher BDE Job Screening | `1TkSWPAjECAI2ASHuy-qvW0FgnNWkimlR` | BDE assessment quizzes | 02-BDE-Fresher-Screening |
| Pocket Income Job | `10PLWg7KVIX_L8PqeAhEDiQ5X4QjrzXXe` | Growth Partner Network | 03-Growth-Partner-Network |
| DM Freelancer | `1M5EGQCLGxBjC6Enp0Apg4PYOusGMW-fU` | Freelancer Contract T&Cs | 04-Freelancer-Contracts |
| Database | `10SuFDkIvHh2xSKsz4DQ6TblCB5Z0byT2` | Resumes + Volunteers | 05-Databases-Resumes-Volunteers |

---

## 2. Core VA Hiring Funnel Documents (Canonical — Migrated)

| Stage | Name | Drive File ID | Type | GitHub Path | Status |
|-------|------|---------------|------|-------------|--------|
| S0 | S0.0 - VA Hiring Funnel – Step-by-Step System | `1jD22mk6wo6kcp5ST4BlUauL7llpOUxBmGI4a8GGIvhE` | Google Doc | `01-VA-CA-Hiring-Funnel/S0-Step-by-Step-System.md` | **MIGRATED** |
| S1 | S1 - VA Job Description | `1p79jWJ1Md3N-cbfIDK1aJShstMpGEI0nMzQQdhAXkz4` | Google Doc | `.../S1-Job-Description.md` | **MIGRATED** |
| S2 | S2 - Google Form with Screening | `1yj4-KsgagGDOhdcNFafh22HzjlHc-UD7XKllG6yYuUg` | Google Doc | `.../S2-Google-Form-Screening.md` | **MIGRATED** |
| S3 | S3 Trial Task | `1YyrE42yYlUB9UUGsisK6XJ89mTxQDCARIq7pxrR9mGw` | Google Doc | `.../S3-Trial-Task.md` | **MIGRATED** |
| S4 | S4 - Interview | `1kVgMqax6ILNW_WEAyyPyVZRi8skTrKVUExsj8UTtKs8` | Google Doc | `.../S4-Interview.md` | **MIGRATED** |
| S5 | S5: Live Orientation Call | `1l547jbgkUZaopfRZdxGQKGvaH-9-fnsraXTm7JzckMY` | Google Doc | `.../S5-Live-Orientation-Call.md` | **MIGRATED** |
| S6 | S6 Final Selection + Contract Signing | `121ua_C7OOyD6P9Gs2yvIyZR5ATgNED-nzpW92lpr3z4` | Google Doc | `.../S6-Final-Selection-Contract.md` | **MIGRATED** |
| S7 | S7: Training & Probation Period (3 Months) | `1iphaeoXzTrTcZIv9Nwn4oSW7cRENJq04AOEbdfiaQjM` | Google Doc | `.../S7-Training-Probation.md` | **MIGRATED** (source minimal) |
| S8 | S8: Permanent Hiring - Offer Letter | `1eI3tdC1DphSaPHnN196c5J_ikNTUuXvahyp00A-fJmo` | Google Doc | `.../S8-Offer-Letter.md` | **MIGRATED** |

---

## 3. SOPs (Migrated)

| Name | Drive File ID | GitHub Path | Status |
|------|---------------|-------------|--------|
| VA HIRING FUNNEL – SOP | `1_6xG_vglNYywpsMYvWDVbv32u3LDpHld3ygzgksIbzw` | `06-SOPs-and-Automation/VA-Hiring-Funnel-SOP.md` | **MIGRATED** |
| SOP: STAGE 0 – JOB AWARENESS | `1fifA3jtYHyNpQjYNRuBpbon8q8Rbo8O6Vo4ZjwHxvJM` | `06-SOPs-and-Automation/SOP-Stage-0-Job-Awareness.md` | **MIGRATED** |

---

## 4. Secondary / P1 Assets (Pending)

| Name | Drive ID / Location | Target | Status |
|------|---------------------|--------|--------|
| VA Agreement | `1qshVutu4ZbMtBOuI8SIuxeUSeNjR2Benuv9xz1E6vCw` | 01 or 04 | PENDING |
| VA Offer Letter | `1dfa9M4uYoCK1TqhWSj6DSrDZGZmFrKALMfmuTKhsNJo` | 01 | PENDING |
| Quiz 1 - Nivy BDE Role Fit | Folder `10K0_raBM6R4vjjlwThrGzk1pebrhhFKm` | 02 | PENDING |
| Quiz 2 - Nivy BDE Job Assessment | Folder `1YXUpk-HX-29aw9pCZx8hZV60i4A0HpnY` | 02 | PENDING |
| Quiz 3 - Nivy BDE Student Assessment | Folder under Fresher BDE | 02 | PENDING |
| Nivy Growth Partner Network (Form) | `1FLmwVHFxQf1hmjVLcyn8sEOpBK9CnbIPtDc6Dn5U7i4` | 03 | PENDING |
| Freelancer Contract Terms & Conditions | Form under DM Freelancer | 04 | PENDING |
| Nivy Part Time Appointment Setter | Form `1In4vtjbA3rjaWi4tE2eCkF2bBSsEfnj-rqTXD4SOTYc` | 01/03 | PENDING |
| Nivy SDR Responses | Sheets under Appointment Setter folder | Index only | PENDING |

---

## 5. CA Assistant Folder (Secondary / Archive)

Parallel .docx versions of S0–S8 + JSON + Excel exist under CA Assistant Hiring Funnel. Prefer Google Docs from VA folder as canonical. .docx can be archived or linked later under `raw/` if needed.

| Name (examples) | Notes |
|-----------------|-------|
| S0 - VA Hiring Funnel – Step-by-Step System.docx | Secondary |
| S1 - VA Job Description.docx | Secondary |
| ... S2–S8 .docx | Secondary |
| Step 2 - Hiring Funnel.json | Automation artifact |
| VA Email Applications.xlsx | Application log |

---

## 6. Databases / PII (Gated — Phase 4)

| Folder / File | Notes | Policy |
|---------------|-------|--------|
| Resumes | Many candidate PDFs | Index only without approval |
| Volunteers Database | Volunteer CVs | Index only |
| BDE / Accountant / HR Resumes | Role-specific | Index only |
| leads.xlsx | Root-level | Schema summary only |
| Offer letters/ (old 2021 templates) | Reusable templates | Can migrate as templates |
| CS Data.xlsx / CS.xml | Possibly non-PII | Review then decide |

---

## 7. Other Noted Files

| Name | Notes |
|------|-------|
| Messaging.docx (~50 MB, 2 copies) | Possibly sales messaging — review if useful |
| USA Trial Task (Sheet) | Trial task data |
| Digital Marketing Executive - Bengaluru.xlsx | Job/candidates related |
| All projects.pdf | Candidate portfolio-like |
| TAsks.txt | Small task list |

---

## 8. Migration Status Legend

| Status | Meaning |
|--------|---------|
| **MIGRATED** | Clean Markdown (or equivalent) in GitHub with source ID |
| PENDING | Identified; not yet converted/committed |
| SKIPPED | Explicitly out of scope or blocked (e.g. PII without approval) |
| INDEX ONLY | Metadata/count/structure only; no content dump |

---

**Note:** Originals remain on Google Drive. GitHub holds research/source copies only.
