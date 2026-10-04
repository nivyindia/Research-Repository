# Tech Stack Scorecard — CRM / ERP / LMS / Ticketing

**Folder:** `10-TECH-AND-SYSTEMS/`  
**Created:** 2026-10-04  
**Status:** Evaluation scorecard (not a final purchase decision)  
**Principle:** REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING

---

## 1. Scoring criteria (1–5 each)

| Criterion | Weight |
|-----------|--------|
| Fits multi-tier partner channel (L0–L3) | High |
| India GST / accounting practicality | High |
| Self-host or data-residency options | High |
| LMS or training add-on path | Medium |
| Ticketing / cases | Medium |
| Implementation cost & skills available | High |
| Avoid rebuilding gov portals | Mandatory pass |

---

## 2. Candidate comparison (directional)

| Platform | CRM | Accounts/GST | LMS path | Ticketing | Self-host | Fit notes | Score draft |
|----------|-----|--------------|----------|-----------|-----------|-----------|-------------|
| **ERPNext** (Frappe) | Yes | Strong India community / GST modules | Frappe LMS | Issues / helpdesk apps | Yes | One ecosystem for partner + ledger; learning curve | **4.2** |
| **Dolibarr** | Yes | SMB accounting | Limited native LMS | Tickets | Yes | Lighter; may need more glue for LMS | **3.5** |
| **Vtiger** (open core) | Strong CRM | Weaker as full ERP | External LMS | Cases | Yes / cloud | Good funnel; pair with accounts tool | **3.6** |
| **Odoo Community** | Yes | Yes | eLearning apps | Helpdesk | Yes | Broad; edition/licence discipline needed | **3.8** |
| **HubSpot free + sheets** | Lead CRM | No | External | Limited | Cloud | Pilot-only MVP; not full ledger | **2.8** (MVP only) |
| **Moodle** | No | No | **Best-in-class LMS** | No | Yes | Pair with CRM/ERP; do not use alone | N/A (component) |
| **FreeScout / osTicket** | No | No | No | Yes | Yes | Component for support | N/A (component) |
| **n8n** | Automation | — | — | — | Yes | After processes stable | N/A (component) |

**Draft recommendation for pilot:**  
- **MVP:** CRM stages (any) + spreadsheet MIS (field dictionary) + WhatsApp + shared SOPs.  
- **v1 target to evaluate hands-on:** **ERPNext** (partner + basic ledger) **or** Vtiger/Dolibarr + separate accounts, plus **Moodle** if training volume needs it.  
- **Never** rebuild Digital Seva / e-District / UIDAI.

---

## 3. Decision gates before commit

- [ ] 2-week sandbox of top 2 stacks with fake L3 onboarding flow  
- [ ] Confirm GST invoice needs for Nivy fees (if any)  
- [ ] Role model: HQ / L1 / L2 / L3 permissions  
- [ ] Backup + access-log trial  
- [ ] Cost of implementation partner vs in-house

---

## 4. Data model minimum (any stack)

Partner, Centre, Territory, ServiceCatalogue, FeeListVersion, Ticket, Incident, TrainingCertificate, TxnSummary (aggregates only).

See: `14-MONITORING-QC-SUSTAINABILITY/03-MIS-FIELD-DICTIONARY.md`

---

## Cross-links

- Blueprint: `01-TECH-AIOS-BLUEPRINT.md`  
- MIS dictionary: `14-MONITORING-QC-SUSTAINABILITY/03-MIS-FIELD-DICTIONARY.md`
