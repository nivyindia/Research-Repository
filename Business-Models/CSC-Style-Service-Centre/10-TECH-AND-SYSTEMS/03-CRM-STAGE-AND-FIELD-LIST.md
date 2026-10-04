# CRM Stage & Field List — Partner Recruitment

**Folder:** `10-TECH-AND-SYSTEMS/`  
**Created:** 2026-10-04  
**Status:** Implementation checklist for pilot CRM  
**Aligns with:** Sales funnel stages + MIS dictionary + onboarding

---

## 1. Pipelines

| Pipeline | Track | Primary audience |
|----------|-------|------------------|
| Centre Partner | A | L3 |
| District Distributor | B | L2 |
| State / Master | C | L1 |

Optional: single pipeline with required **Track** field.

---

## 2. Stages (Track A default)

| Stage code | Stage name | Exit criteria |
|------------|------------|---------------|
| NEW | New | Contact verified |
| CON | Contacted | Interest or LOST |
| QUAL | Qualified | Application started |
| APP | Application | Docs submitted |
| DD | Due diligence | Clear or reject |
| PROP | Proposal | Term sheet shared |
| AGR | Agreement | Signed |
| ONB | Onboarding | Training + hardware gate |
| LIVE | Live | Probation or full |
| LOST | Closed-lost | Reason required |

---

## 3. Required lead / deal fields

| Field | Type | Required |
|-------|------|----------|
| full_name | text | Y |
| phone | phone | Y |
| alt_phone | phone | N |
| email | email | N |
| track | enum A/B/C | Y |
| source | enum (web/camp/referral/whatsapp/other) | Y |
| state | text | Y |
| district | text | Y |
| pincode | text | Y |
| current_activity | text | N |
| space_type | enum (shop/home-front/dedicated/other) | N |
| channel_owner | user | Y |
| next_action_date | date | Y |
| lost_reason | enum | if LOST |
| disclaimer_ack | bool | Y before PROP |
| application_link_sent | bool | N |
| term_sheet_version | text | at PROP |
| agreement_ref | text | at AGR |
| centre_id | text | at ONB/LIVE |
| territory_grant_id | text | at AGR/LIVE |
| training_certified | bool | before LIVE |
| hardware_gate_pass | bool | before LIVE |
| fee_list_version | text | at LIVE |

---

## 4. Attachment checklist (stages)

| Stage | Attachments |
|-------|-------------|
| APP | ID, address, photo, location proof |
| DD | KYC pack status, conflict check note |
| PROP | Term sheet PDF (approved version) |
| AGR | Signed agreement |
| ONB | Training certificate, hardware photos |
| LIVE | Fee-list photo, brand check photo |

---

## 5. Automations (phase later)

- NEW without CON in 1 business day → alert owner  
- PROP without reply 7 days → follow-up task  
- LIVE without training_certified → block (validation)  
- LOST requires lost_reason

---

## 6. Reports for pilot

- Funnel conversion by stage  
- Time in stage  
- LOST reasons  
- LIVE count by district  
- Certification lag (AGR → LIVE days)

---

## Cross-links

- Funnel: `08-SALES-PROPOSALS-AND-PITCHES/01-SALES-FUNNEL-AND-PROPOSAL-SKELETON.md`  
- MIS: `14-MONITORING-QC-SUSTAINABILITY/03-MIS-FIELD-DICTIONARY.md`  
- Onboarding: `05-FRANCHISE-PROGRAM-DESIGN/02-PARTNER-ONBOARDING-CHECKLIST.md`  
- Term sheet structure: `05-FRANCHISE-PROGRAM-DESIGN/05-PILOT-TERM-SHEET-STRUCTURE.md`
