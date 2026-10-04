# Consistency Audit Notes — 2026-10-04

**Folder:** `13-IMPLEMENTATION/`  
**Created:** 2026-10-04  
**Status:** Internal QA of programme docs  
**Scope:** Cross-links, claim safety, blank-number discipline

---

## 1. Strengths

- Clear **non-CSC / no income guarantee** language repeated across sales, FAQ, Hindi scripts, term-sheet footer, landing wireframe.  
- Ops path complete enough for dry-run: daily checklist, fraud playbook, escalation, hardware, soft-launch script.  
- L1/L2/L3 sales outlines exist without invented economics.  
- State snapshots (UP, Bihar, MP) use dated PIB figures.  
- DigiPay/AePS correctly marked **VERIFY** (no fake %).  
- 90-day runbook separates research from human execution.

---

## 2. Residual inconsistencies / watch items

| Item | Note | Action |
|------|------|--------|
| Onboarding file numbering | Early channel doc mentioned `03-ONBOARDING` vs actual `02-PARTNER-ONBOARDING-CHECKLIST` | Prefer actual paths in new docs |
| Marketing log “pending” rows | Older seed rows replaced by MKT-003+ in later updates | Trust latest log file on main |
| Unit economics volume | Many economics files pre-exist; do not contradict with invented annex rates | Fill Annex A only from primary sources |
| Hardware vs official CSC portal specs | Nivy list is practical minimum, not a clone of register.csc hardware table | Keep disclaimer on hardware file |
| Helpdesk numbers | CSC 14599 is CSC network; Nivy must publish own number for pilot | Assign before LIVE |

---

## 3. Claim-safety checklist (spot-check before any public page)

- [ ] No “CSC franchise”  
- [ ] No government emblem  
- [ ] No guaranteed income / ₹ per month  
- [ ] Term sheet version cited for any fee  
- [ ] Hindi and English disclaimers match in meaning  

---

## 4. Suggested doc hygiene (optional)

- Add `centre_id` format standard (e.g. UP-DIST-###) in one place  
- Single “canonical disclaimer” snippet file if copy-paste drift appears  
- Archive superseded tracker “next batch” bullets when done (already overwritten each batch)

---

## 5. Verdict

Repository is **coherent for pilot preparation**. Blocking issues are **approvals and execution**, not missing research skeletons.

---

## Cross-links

- Gap report: `02-GAP-REPORT-DRAFT.md`  
- Runbook: `07-EXECUTION-RUNBOOK-NEXT-90-DAYS.md`  
- Tracker: `CSC-BUSINESS-MODEL-FRANCHISE-PROGRESS-TRACKER.md`
