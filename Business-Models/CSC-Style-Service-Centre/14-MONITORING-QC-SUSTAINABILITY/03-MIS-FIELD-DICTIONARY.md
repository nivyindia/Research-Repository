# MIS Field Dictionary — Pilot / Network Reporting

**Folder:** `14-MONITORING-QC-SUSTAINABILITY/`  
**Created:** 2026-10-04  
**Status:** Field dictionary for pilot MIS (spreadsheet or CRM)  
**Rule:** Aggregate operational metrics only. No full Aadhaar/PAN/OTP/biometric storage in MIS.

---

## 1. Entity keys

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| centre_id | string | Y | Unique stable ID |
| partner_id | string | Y | L3 operator / entity |
| l2_id | string | N | Supporting distributor |
| l1_id | string | N | State/master if any |
| state | string | Y | |
| district | string | Y | |
| pincode | string | Y | |
| status | enum | Y | PROSPECT / ONBOARDING / PROBATION / LIVE / SUSPENDED / EXIT |
| activated_at | date | N | First LIVE date |
| fee_list_version | string | Y when LIVE | Must match posted list |

---

## 2. Daily ops snapshot (optional daily / required sample in pilot)

| Field | Type | Notes |
|-------|------|-------|
| report_date | date | |
| active_day | bool | Centre open for service |
| opening_float_cash | number | INR |
| closing_float_cash | number | INR |
| float_variance_flag | bool | If unexplained |
| fee_list_displayed | bool | Compliance |
| brand_ok | bool | No CSC/gov marks |
| failed_txn_count | integer | Portal/process failures |
| complaint_count | integer | Same-day logged |
| overcharge_flag | bool | Any suspected |
| notes | text | Short; no PII dumps |

---

## 3. Weekly / monthly KPI fields

| Field | Type | Cadence | Links to pilot KPI |
|-------|------|---------|-------------------|
| training_certified | bool | On change | 100% before LIVE |
| onboarding_days | integer | Once | Activation speed |
| ticket_count | integer | Weekly | Support load |
| ticket_first_response_hours | number | Weekly avg | ≤1 business day target |
| complaint_per_100_txn | number | Monthly | Quality |
| mystery_fee_pass | bool | Per audit | 100% target |
| mystery_brand_pass | bool | Per audit | 100% target |
| active_days_per_week | number | Weekly | ≥5 target |
| mis_submitted_on_time | bool | Monthly | ≥90% |
| nps_score | number | Survey wave | Baseline |
| gross_txn_count | integer | Monthly | Baseline only |
| gross_txn_value | number | Monthly | Baseline only; not vanity target |
| incident_critical_count | integer | Monthly | Fraud/data/brand |

---

## 4. Ticket / incident linkage

| Field | Type | Notes |
|-------|------|-------|
| ticket_id | string | From helpdesk |
| incident_id | string | Escalation form |
| severity | enum | LOW/MED/HIGH/CRITICAL |
| category | enum | Align escalation form types |
| resolved_at | datetime | |
| root_cause_code | string | Controlled vocabulary |

---

## 5. Role access (minimum)

| Role | Sees |
|------|------|
| L3 Centre | Own centre daily + own tickets |
| L2 | District centres aggregates + tickets |
| L1 | State aggregates |
| HQ | All + audit logs |

---

## 6. Explicitly forbidden in MIS store

- Full Aadhaar / PAN / bank account numbers  
- OTPs, biometric templates  
- Customer identity docs images (keep in lawful workflow tools only)  
- Invented commission forecasts presented as fact

---

## Cross-links

- Pilot KPIs: `13-IMPLEMENTATION/01-PILOT-KPIS-AND-LAUNCH-CHECKLIST.md`  
- Tech blueprint: `10-TECH-AND-SYSTEMS/01-TECH-AIOS-BLUEPRINT.md`  
- Partner scorecard: `01-PARTNER-HEALTH-SCORECARD.md`  
- Escalation form: `06-OPERATIONS-AND-TRAINING/04-INCIDENT-ESCALATION-FORM.md`
