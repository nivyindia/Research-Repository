# Portal Outage — Mini Playbook (Centre Level)

**Folder:** `06-OPERATIONS-AND-TRAINING/`  
**Created:** 2026-10-04  
**Status:** Pilot ops  
**Scope:** Third-party government/bank/provider portals down or failing

---

## 1. Principles

1. **Do not** invent offline workarounds that collect OTPs, passwords, or full Aadhaar into local notebooks.  
2. **Do not** charge for failed transactions.  
3. **Do not** blame citizens; explain and reschedule.  
4. Log failure for MIS / tickets.

---

## 2. Detection

| Signal | Action |
|--------|--------|
| Login error / timeout | Retry once; note time |
| Multiple citizens same error | Likely portal-side |
| Single user only | Check user docs / local network |

---

## 3. Immediate steps (operator)

1. Stop repeating failed attempts that lock accounts.  
2. Inform citizen: service temporarily unavailable; no extra fee.  
3. Offer to retry later or take **callback request** (name + phone only).  
4. Record: `failed_txn_count` + short note (no PII dumps).  
5. If prolonged (>30–60 min) or widespread: raise ticket to L2/HQ.

---

## 4. What not to do

| Forbidden | Why |
|-----------|-----|
| Take cash “to process tonight offline” | Fraud / overcharge risk |
| Ask citizen to share OTP on WhatsApp | Data abuse |
| Use personal unofficial apps as substitute | Auth + security |
| Claim “government has closed scheme” without fact | Misinformation |

---

## 5. HQ / L2

| Step | Action |
|------|--------|
| Confirm outage scope | Multiple centres? |
| Broadcast status | Partner channel |
| Log provider incident | If material |
| Clear when portals recover | Resume + clear callback queue |

---

## 6. After recovery

- Work callback list in order  
- No penalty to partner for pure provider outage  
- If partner invented fees during outage → incident + review  

---

## Cross-links

- Daily checklist: `03-DAILY-OPENING-CLOSING-CHECKLIST.md`  
- Escalation form: `04-INCIDENT-ESCALATION-FORM.md`  
- Dry-run Scene D: `13-IMPLEMENTATION/05-SOFT-LAUNCH-DRY-RUN-SCRIPT.md`
