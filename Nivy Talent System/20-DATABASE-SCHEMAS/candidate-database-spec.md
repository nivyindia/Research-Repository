# Candidate Database Specification

**Created:** 2026-09-27  
**PII rule:** Production DB holds personal data under access control. **GitHub holds schemas only** — no response dumps.  
**Related forms:** `03-CANDIDATE-ACQUISITION/contact-information-form-schema.md`, `va-screening-form-schema.md`

---

## 1. Design goals

1. One **person** record across applications and roles  
2. Full **lifecycle stage** visible for ops  
3. Scores and decisions auditable  
4. Talent-pool flags for re-engagement without re-entry chaos  
5. Minimal fields for matching; rich fields in secure store only  

---

## 2. Core entities

### 2.1 `persons` (identity)

| Field | Type | Notes |
|-------|------|--------|
| person_id | UUID / PK | Internal |
| full_name | string | |
| email | string | Unique preferred |
| phone | string | E.164 if possible |
| city / state | string | Sourcing |
| created_at / updated_at | timestamptz | |

*PII — restricted roles only.*

### 2.2 `applications`

| Field | Type | Notes |
|-------|------|--------|
| application_id | PK | |
| person_id | FK | |
| source | enum | job_portal, social, referral, institute, walk_in, other |
| role_applied | enum | BDE, HR, VA_SMM, OTHER |
| applied_at | timestamptz | |
| form_payload_ref | string | Link to Form/Sheet row ID — not copied to Git |

### 2.3 `eligibility`

| Field | Type | Notes |
|-------|------|--------|
| application_id | FK | |
| education_ok | bool | ≥60% / 6 CGPA rules |
| backlog_ok | bool | max 1 active |
| gap_months | int | max 24 declared |
| degree_category | string | technical/mgmt vs restricted |
| eligibility_status | enum | pass, fail, review |

### 2.4 `assessments`

| Field | Type | Notes |
|-------|------|--------|
| assessment_id | PK | |
| application_id | FK | |
| type | enum | role_fit_quiz, screen_exam, practical, three_task, mcq_basic, mcq_advanced, interview |
| score | numeric | 0–100 or x/y normalized |
| band | enum | strong_80, developing_65_79, below_65 |
| consistency_flag | enum | stable, volatile, n_a |
| assessed_at | timestamptz | |
| assessor_id | string | human owner; AI assist noted in meta |

### 2.5 `stage_history`

| Field | Type | Notes |
|-------|------|--------|
| id | PK | |
| application_id | FK | |
| stage | enum | see lifecycle stages below |
| entered_at | timestamptz | |
| exited_at | timestamptz | nullable |
| decision | enum | advance, hold, reject, withdraw, convert_ft, exit |
| note | text | short; no sensitive health data |

**Stages (align lifecycle):**  
`sourced → applied → eligible → screened → practical → consistency → training → internship → probation → core | pool | project | exited`

### 2.6 `offers_and_comp`

| Field | Type | Notes |
|-------|------|--------|
| id | PK | |
| application_id | FK | |
| offer_type | enum | ft, internship, academy |
| amount | numeric | |
| currency | string | INR |
| status | enum | drafted, sent, accepted, declined, expired |
| sent_at / accepted_at | timestamptz | |

### 2.7 `talent_pool_membership` → see pool schema

### 2.8 `documents_meta` (not files in Git)

| Field | Notes |
|-------|--------|
| doc_type | id, address, education, photo, cheque |
| storage_uri | Drive/secure bucket |
| verified | bool |
| verified_by / at | |

---

## 3. Lifecycle stage enum (canonical)

```
sourced
applied
eligible
screened
practical
consistency_tasks
training
internship
probation
core_staff
talent_pool
project_work
exited
rejected
cooldown
```

---

## 4. Intake flow → DB writes

| Step | Write |
|------|--------|
| Form submit | persons upsert + applications insert |
| Auto eligibility rules | eligibility row |
| Quiz/exam | assessments |
| Path choice Job vs Academy | stage_history + tag |
| Offer | offers_and_comp |
| Day 90 / confirm | stage → probation or core or pool |

---

## 5. Access control (minimum)

| Role | persons PII | scores | offers |
|------|-------------|--------|--------|
| HR ops | Y | Y | Y |
| Hiring manager | limited | Y (own roles) | Y (own) |
| Mentor/TL | name + stage | Y (assigned) | N |
| Analyst | anonymized | aggregate | N |
| GitHub / public | **schema only** | N | N |

---

## 6. Implementation notes

- Start: Google Sheets + Form IDs as `form_payload_ref` is fine for MVP  
- Next: Airtable / Notion DB / Postgres  
- Never commit CSV exports of responses to this repo  

See also: `10-TALENT-POOL/talent-pool-schema.md`
