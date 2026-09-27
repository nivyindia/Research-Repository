# Automation Workflow Design Notes

**Created:** 2026-09-27  
**Status:** Design only — not production n8n JSON  
**Principle:** Automate reminders and routing; **humans decide** hire / fail / offer amount.

---

## 1. Priority automations (MVP order)

| # | Workflow | Trigger | Actions | Human gate |
|---|----------|---------|---------|------------|
| 1 | **Form incomplete reminder** | Application created; form not done in 24h | WA + email template B | Stop after 2 reminders |
| 2 | **Quiz deadline close** | Deadline −6h | WA reminder | — |
| 3 | **Path choice after pass** | Role-fit score ≥ threshold | Email/WA template C with two links | Score threshold set by HR |
| 4 | **Interview invite** | Stage = interview_scheduled | Calendar link + template E | Slot picked by HR |
| 5 | **Doc chase** | Offer accepted; docs missing | Template I every 48h × 3 | HR verifies docs |
| 6 | **Pool nurture** | Opening approved + match list | Template J to top N | HR approves list |
| 7 | **Probation review ping** | Day 28/58/88 | Template K to employee + manager | Manager writes score |

---

## 2. Suggested stack (lightweight)

| Layer | Option A (fast) | Option B (scale) |
|-------|-----------------|------------------|
| Forms | Google Form | Typeform / custom |
| Sheet / DB | Google Sheet | Postgres / Airtable |
| Automation | **n8n** or Make | n8n self-host |
| WA | Official API or approved BSP | Same |
| Email | Gmail / Workspace | Same + templates |
| Tracking | Workfolio (existing) | Keep |

Start with **Sheet + n8n + Gmail**; add WA API when volume hurts manual sends.

---

## 3. n8n sketch — Workflow 1

```
Cron / Form webhook
  → IF form_status != complete AND hours_since_apply >= 24
  → HTTP/WA send template B
  → IF still incomplete after 48h → second send
  → IF still incomplete after 72h → set stage=rejected_incomplete (or hold)
```

## 4. n8n sketch — Workflow 3

```
Sheet row updated: quiz1_score
  → IF score >= 14
  → Send email path choice (Job vs Academy links)
  → Set stage=path_choice_pending
  → Wait until deadline
  → IF no choice → reminder once → else close
```

---

## 5. Safety rules

1. **No auto-reject on score alone** without logged rule version  
2. **No salary numbers in WA groups**  
3. **PII** only to HR inboxes / secured Sheet ACLs  
4. Log every automated message: `person_id, template_id, channel, sent_at`  
5. Kill-switch: global “pause automations” flag in Sheet  

---

## 6. Do not automate yet

- Final hire / terminate  
- PIP creation  
- Ranking bonus calculation (assist OK; pay needs finance+manager)  
- Offer amount selection  

---

## 7. Related

Comms library · Candidate DB stages · HR training day pipeline · Contact form
