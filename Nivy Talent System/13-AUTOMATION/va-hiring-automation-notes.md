---
migration_date: "2026-09-27"
status: extracted-notes
source: Inferred from VA Hiring SOPs, forms, and Drive assets
---

# VA Hiring Funnel — Automation Notes

## Current / Observed Automation

### Google Form + Sheet
- Application / screening form collects responses
- Auto-scoring enabled on knowledge questions where possible
- Responses land in VA Hiring Dashboard spreadsheet
- Score field used for Pass/Fail routing

### Email Control
- Hiring stages: email-driven progression (invite-only)
- No follow-ups in pure hiring stages (discipline filter)
- Paid Training path: automated Day 1–5 email sequence (Feedback → Course → Proof → Urgency → Final Call)

### Apps Script (present in Drive)
- `VA screening form` script
- `Step 2 - Hiring Funnel` script
- Purpose: form handling / funnel triggers (exact logic not extracted; review scripts in Drive if needed)

### WhatsApp
- Hiring stages: notification only (minimal)
- Training conversion path: active follow-ups + testimonials

---

## Recommended Automation Map (for future build)

| Trigger | Action | Tool suggestion |
|---------|--------|-----------------|
| Form submit | Log to sheet + auto-score + confirmation email | Google Form → Sheet → Apps Script / n8n |
| Score ≥ threshold | Move to Trial Task stage + send task email | n8n / Apps Script |
| Score < threshold or no submit | Redirect to Paid Training sequence | n8n email sequence |
| Trial task deadline | Flag overdue; route fail → Paid Training | Sheet + time trigger |
| Interview booked (Calendly) | Update stage status | Calendly webhook → Sheet |
| Orientation attended | Flag for selection shortlist | Manual or form check-in |
| Agreement signed | Add to Free Training cohort | Sheet status + group add |
| Daily KPI below 65% | Warning / Paid Training option | Dashboard rule |

---

## Principles from SOPs
- Email = control system for hiring
- Deadlines strict; no manual extension
- Batch size max 50 for Stage 0
- Track everything in sheet (stage, status, deadline, source)
- Never put raw candidate PII into GitHub

## Gap
Full n8n / Apps Script export not migrated. Treat this file as the automation design note derived from process docs.
