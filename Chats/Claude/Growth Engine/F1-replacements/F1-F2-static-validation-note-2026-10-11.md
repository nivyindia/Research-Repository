# F1/F2 Static Validation Note — 2026-10-11

**Phase-1 F2 complete; Phase-2 F2 in progress (2.1, 2.2).**

| Module | HTTP retries | Key risks |
|---|---|---|
| 1.1–1.5 | done | WF-SEC-01, WF-CONTENT-02, WF-SEO-03, placeholders |
| 2.1 Multichannel Outreach | 4/4 | postal-reply-webhook auth; AI email/WA auto-send |
| **2.2 Nurture Sequence** | **3/3** | AI email/WA auto-send; nurture_step schema dep; possible double step increment |

## 2.2 static audit summary
- 10 nodes; 3 HTTP (Ollama, Waha, Odoo Discuss); 0 webhooks; active:false
- No original retry/errorWorkflow
- IF Final Nurture Step: true → Discuss alert; false → empty
- Requires `clients_master.nurture_step` and `last_nurture_sent`
- Email + WhatsApp both wire to Update Nurture Step → risk of double increment

## Next
F5 master migration (schema columns for nurture) or continue 2.3 F2.
