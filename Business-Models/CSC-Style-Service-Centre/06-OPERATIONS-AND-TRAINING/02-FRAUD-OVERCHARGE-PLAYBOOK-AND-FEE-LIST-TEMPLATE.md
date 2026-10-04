# Fraud & Overcharge Response Playbook + Citizen Fee-List Template

**Folder:** `06-OPERATIONS-AND-TRAINING/`  
**Created:** 2026-10-04  
**Status:** Operational draft — align with agreement termination clauses  
**Related:** Ops framework, pilot KPIs, legal clause map

---

## 1. Principles

1. Citizens pay **only** fees on the published centre fee list (or official provider schedule).  
2. Overcharging, hidden “convenience” fees, or forging receipts = **hard fail** (suspension path).  
3. Fraud / data abuse / brand impersonation of CSC or government = immediate escalation + termination track.  
4. No real Aadhaar/PAN/OTP storage in local notes beyond lawful process need.

---

## 2. Overcharge response (playbook)

| Step | Owner | Action | SLA |
|------|-------|--------|-----|
| 1 Detect | L1 centre / mystery audit / complaint | Log incident ID, service, alleged amount vs published list | Same day |
| 2 Contain | L2 / Partner success | Pause disputed service if pattern; preserve receipts/logs | 24h |
| 3 Verify | L2 + platform | Compare published fee list version in force on txn date | 48h |
| 4 Remedy | L2 | Refund excess to citizen if confirmed; document | 5 business days |
| 5 Sanction | Platform | Warning → probation → suspension per agreement | Per policy |
| 6 Report | MIS | Tag incident type; feed partner scorecard | Weekly roll-up |

**Mystery check rule (pilot):** Sample centres quarterly; 100% fee-list display compliance required (pilot KPI).

---

## 3. Fraud / serious misconduct triggers

| Trigger | Immediate action |
|---------|------------------|
| Using CSC / government emblems without licence | Suspend branding; written notice |
| Claiming to be official CSC / SCA / bank BC without authority | Suspend + legal review |
| Skimming / sharing customer OTP or biometrics | Immediate suspend; forensic log preserve |
| Ghost transactions / commission fraud | Suspend; settlement freeze pending review |
| Systematic overcharging after warning | Termination track |

Escalation matrix names must be filled before pilot launch (see pilot checklist).

---

## 4. Citizen-facing fee-list template (display)

**Post at centre entrance / counter (print + digital).** Update version number when catalogue changes.

```
--------------------------------------------------
NIVY CENTRE — SERVICE FEE LIST
Centre ID: ________   Version: ____   Effective: ____

Service                          | Official fee (INR) | Notes
---------------------------------|--------------------|------
[Authorised service A]           | ______             | Receipt mandatory
[Authorised service B]           | ______             | ...
[Assisted form help — if charged]| ______             | Only if allowed

NO OTHER CHARGES without written approval.
Grievance / helpdesk: _______________
This centre is a Nivy Centre Partner — NOT a CSC franchise.
--------------------------------------------------
```

Rules:
- Only services in the **pilot-authorised catalogue** appear.  
- If a government portal has its own prescribed fee, show that fee and do not add undeclared markup.  
- Hindi + English preferred for pilot districts in UP.

---

## 5. Daily ops link

Opening checklist must include: **fee list displayed and current version**.  
Closing: complaint log reviewed; overcharge flags escalated.

---

## 6. Training note

Include this playbook in partner certification. Practical assessment: “Customer challenges a fee — what do you do?”

---

## Cross-links

- Ops framework: `01-OPERATIONS-FRAMEWORK.md`  
- Pilot KPIs: `13-IMPLEMENTATION/01-PILOT-KPIS-AND-LAUNCH-CHECKLIST.md`  
- Legal subjects: `09-LEGAL-COMPLIANCE/01-LEGAL-CLAUSE-SUBJECT-MAP.md`  
- Partner scorecard: `14-MONITORING-QC-SUSTAINABILITY/`
