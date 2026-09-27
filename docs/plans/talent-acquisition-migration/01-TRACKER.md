# Tracker — Talent Acquisition Migration

**Plan:** [00-MASTER-IMPLEMENTATION-PLAN.md](00-MASTER-IMPLEMENTATION-PLAN.md)  
**Last updated:** 2026-09-27  
**Overall status:** IN PROGRESS — Phases 0–3 largely complete; Phase 4+ pending

---

## Summary Dashboard

| Phase | Name | Status | % |
|-------|------|--------|---|
| 0 | Discovery & Planning | **DONE** | 100% |
| 1 | Structure & Seed READMEs | **DONE** | 100% |
| 2 | Core VA/CA Hiring Funnel (S0–S8 + SOPs) | **DONE** | 100% |
| 3 | Secondary Hiring Assets (P1) | **DONE** | 100% |
| 4 | Databases & Sensitive Data (P2) | PENDING | 0% |
| 5 | Deduplication, Cross-links & Polish | PENDING | 0% |
| 6 | Handoff & Close | PENDING | 0% |

**Overall estimated completion:** ~55% (Phases 0–3 of 6)

---

## Phase 0 — Discovery & Planning

| ID | Task | Status | Notes |
|----|------|--------|-------|
| 0.1 | Scan Google Drive root + key folders | **DONE** | |
| 0.2 | Identify hiring / training / SOP / contract files | **DONE** | |
| 0.3 | Inspect existing `Nivy Jobs/` in repo | **DONE** | |
| 0.4 | Write Master Implementation Plan | **DONE** | v2 |
| 0.5 | Create Tracker + Inventory | **DONE** | |
| 0.6 | Commit plan files to proper folder | **DONE** | |

**Phase 0 status:** ✅ DONE

---

## Phase 1 — Structure & Seed READMEs

| ID | Task | Status | Notes |
|----|------|--------|-------|
| 1.1 | Create Talent-Acquisition tree | **DONE** | |
| 1.2 | Seed Talent-Acquisition 00-README | **DONE** | |
| 1.3 | Seed 01-VA-CA-Hiring-Funnel 00-README | **DONE** | |
| 1.4 | Seed remaining subfolder READMEs (02–06) | **DONE** | 02–05 seeded in Phase 3 |
| 1.5 | Update master index if needed | PENDING | Optional |

**Phase 1 status:** ✅ DONE

---

## Phase 2 — Core VA/CA Hiring Funnel Migration (P0)

| ID | Task | Status | Notes |
|----|------|--------|-------|
| 2.1–2.9 | S0–S8 Markdown files | **DONE** | |
| 2.10 | source-links.md | **DONE** | |
| 2.11 | VA Hiring Funnel SOP | **DONE** | |
| 2.12 | SOP Stage 0 Job Awareness | **DONE** | |

**Phase 2 status:** ✅ DONE

---

## Phase 3 — Secondary Hiring Assets (P1)

| ID | Task | Status | Notes |
|----|------|--------|-------|
| 3.1 | BDE Fresher Screening | **DONE** | BDE-Job-Screening-Questions.md + README; Quizzes indexed (forms) |
| 3.2 | Growth Partner Network | **DONE** | README + form index (form not text-extractable) |
| 3.3 | Freelancer Contract T&Cs | **DONE** | README + form index |
| 3.4 | VA Agreement (full) | **DONE** | `01-VA-CA-Hiring-Funnel/VA-Agreement.md` |
| 3.5 | VA Offer Letter (extra) | **DONE** | `01-VA-CA-Hiring-Funnel/VA-Offer-Letter-Template.md` |
| 3.6 | Part-Time Appointment Setter / SDR summary | PARTIAL | Noted in inventory; form/index only for now |

**Phase 3 status:** ✅ DONE (forms index-only where binary; readable docs migrated)

---

## Phase 4 — Databases & Sensitive Data (P2 — gated)

| ID | Task | Status | Notes |
|----|------|--------|-------|
| 4.1 | Inventory Resumes / Volunteers (names + counts) | PENDING | PII — index only |
| 4.2 | leads.xlsx schema summary | PENDING | |
| 4.3 | CS Data / other non-PII sheets | PENDING | |
| 4.4 | Human approval gate for any PII commit | PENDING | Required |

**Phase 4 status:** ⬜ PENDING (blocked on human approval for PII)

---

## Phase 5 — Deduplication, Cross-links & Polish

| ID | Task | Status | Notes |
|----|------|--------|-------|
| 5.1 | Compare Google Doc vs .docx; mark canonical | PENDING | |
| 5.2 | Cross-link existing Nivy Jobs content | PENDING | |
| 5.3 | Ensure every file has source Drive ID | PENDING | Mostly done for 0–3 |
| 5.4 | Update all READMEs + Tracker accuracy | PENDING | |
| 5.5 | Final inventory checklist sign-off | PENDING | |

**Phase 5 status:** ⬜ PENDING

---

## Phase 6 — Handoff & Close

| ID | Task | Status | Notes |
|----|------|--------|-------|
| 6.1 | Final status report | PENDING | |
| 6.2 | Update repo autonomous / master notes | PENDING | Optional |
| 6.3 | Mark plan COMPLETE in Tracker | PENDING | |
| 6.4 | Handoff note for product / Academy / ATS | PENDING | |

**Phase 6 status:** ⬜ PENDING

---

## Change Log

| Date | Change |
|------|--------|
| 2026-09-27 | Tracker created. Phases 0–2 marked DONE. |
| 2026-09-27 | S0–S8 + 2 SOPs + source-links committed. |
| 2026-09-27 | Master Plan v2 under `docs/plans/talent-acquisition-migration/`. |
| 2026-09-27 | **Phase 3 DONE:** VA Agreement, VA Offer Letter, BDE Screening Questions migrated; 02–05 folder READMEs seeded; Growth Partner + Freelancer forms indexed. |

---

## Next Action

**Immediate next:** Phase 4 (after human PII approval) **or** Phase 5 polish/cross-links.

Or direct: complete Appointment Setter/SDR form summary if form questions are exported manually.
