# Technology & AIOS Blueprint — CSC-Style Channel

**Folder:** `10-TECH-AND-SYSTEMS/`  
**Created:** 2026-10-04  
**Status:** Blueprint skeleton  
**Principle:** REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING

---

## 1. Capability map (what the network needs)

| Capability | Purpose | Build vs buy (default stance) |
|------------|---------|--------------------------------|
| Partner / franchise CRM | Leads, onboarding, territory, scorecard | Prefer existing CRM + light custom |
| Partner portal | Login, docs, rate cards, tickets, announcements | Portal module or PRM |
| Service catalogue | Authorised services, fees, SOPs links | CMS / structured DB |
| KYC / document workflow | Partner + (where lawful) customer docs | Secure storage + checklist; no excess PII |
| Payment / commission ledger | Wallet float, commissions, payouts | Accounting + rules engine |
| Ticketing / escalation | L1–L3 support | Helpdesk tool |
| LMS / certification | Training tracks, quizzes, certificates | Open-source LMS first |
| Dashboard / MIS | Txn proxies, KPIs, district heatmaps | BI on top of CRM/ledger |
| Territory management | Pincode/district assignment | CRM custom fields or GIS light |
| Inventory / e-commerce (optional) | Retail SKUs if Nivy sells products | ERP module when needed |
| Analytics & automation | Alerts, n8n/AI agents for ops | Automate after processes stable |

---

## 2. Reuse-first candidate stack (research shortlist — not final selection)

| Layer | Candidates to evaluate | Notes |
|-------|------------------------|-------|
| CRM | Vtiger (open core), Dolibarr, HubSpot free tier, ERPNext CRM | India-friendly options exist |
| ERP / accounts / GST | **ERPNext**, Dolibarr, Odoo Community | ERPNext often cited for Indian SMBs / GST |
| LMS | **Moodle**, Frappe LMS, Tutor/LearnDash (WP) | Moodle for formal cohorts; Frappe if ERPNext-aligned |
| PRM / partner portal | xAmplify Open PRM (self-host claim), custom on ERPNext | Validate licence & maturity before commit |
| Automation | n8n, Make, Zapier | Prefer self-host n8n for sensitive flows |
| Ticketing | FreeScout, osTicket, CRM cases | |
| Identity | Official provider portals only (Aadhaar etc.) | Never rebuild identity rails |

**Do not** rebuild Digital Seva Portal, e-District, or UIDAI stacks. Integrate or deep-link where authorised.

---

## 3. AIOS / agent use-cases (after data hygiene)

| Agent idea | Trigger | Guardrail |
|------------|---------|-----------|
| Onboarding incomplete | Application stuck > N days | Human approval for reject |
| Training nudge | Certificate expiring | No fake completion |
| Ticket triage | New complaint | No auto-legal advice |
| MIS summary | Weekly | Aggregates only |
| Knowledge bot | SOP questions | Cite internal docs only |

No agent may handle raw Aadhaar/PAN/biometrics or invent commission rates.

---

## 4. Security & compliance baselines

- Least-privilege roles (HQ / State / District / Centre)
- Audit logs on commission and KYC access
- Encryption in transit; secrets in vault
- No storage of OTPs, full card numbers, biometrics templates beyond provider apps
- Backup & disaster recovery tested quarterly
- Align with IT Act / DPDP obligations (legal Phase 10)

---

## 5. Implementation phases (tech)

1. **MVP:** CRM + shared drive SOPs + WhatsApp ops + spreadsheet commission (pilot only)
2. **v1:** Partner portal + LMS + ticketing + basic ledger
3. **v2:** Automation, territory dashboards, provider API integrations where contracts allow
4. **v3:** AI assist + advanced analytics

---

## 6. Next tech tasks

- [ ] Score ERPNext vs Dolibarr vs Vtiger against Nivy channel requirements
- [ ] Define data model: Partner, Centre, Territory, Service, TxnSummary, Ticket
- [ ] Pilot district IT checklist (devices, bandwidth, power)
- [ ] Integration policy: when to deep-link vs embed

---

## Cross-links

- Operations: `06-OPERATIONS-AND-TRAINING/`
- Economics: `04-UNIT-ECONOMICS/`
- Legal: `09-LEGAL-COMPLIANCE/`
