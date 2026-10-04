# Centre Partner Application Form — Field List

**Folder:** `05-FRANCHISE-PROGRAM-DESIGN/`  
**Created:** 2026-10-04  
**Status:** Form spec for web / paper / CRM  
**Aligns with:** Onboarding checklist, CRM fields, term-sheet structure

---

## 1. Applicant identity

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| full_name | text | Y | |
| father_or_spouse_name | text | N | If used in KYC pack |
| date_of_birth | date | Y | Adult check |
| gender | enum | N | Optional |
| mobile | phone | Y | Primary OTP channel |
| alt_mobile | phone | N | |
| email | email | N | |
| aadhaar_last4_only | text | N | Prefer full KYC offline; avoid storing full Aadhaar in form DB if possible |
| pan_last4_or_masked | text | N | Same privacy caution |
| current_address | text | Y | |
| permanent_address | text | N | |
| city_village | text | Y | |
| state | text | Y | |
| district | text | Y | |
| pincode | text | Y | |

**Privacy:** Prefer document upload to secure folder over typing full Aadhaar/PAN into CRM.

---

## 2. Proposed centre

| Field | Type | Required |
|-------|------|----------|
| proposed_location_description | text | Y |
| location_map_link_or_pin | text | N |
| space_type | enum: shop / home-front / dedicated / other | Y |
| approx_area_sqft | number | N |
| ownership | enum: owned / rented / family / other | N |
| power_backup_available | bool | Y |
| internet_type | enum: broadband / 4G / other | Y |
| existing_hardware_summary | text | N |
| photo_storefront | file | N at apply; Y before LIVE |
| photo_interior | file | N at apply; Y before LIVE |

---

## 3. Experience & activity

| Field | Type | Required |
|-------|------|----------|
| current_occupation | text | Y |
| runs_existing_centre_or_shop | bool | Y |
| existing_csc_or_bc | bool | Y |
| existing_authorisations_note | text | if yes |
| digital_literacy_self_rate | enum 1–5 | N |
| languages | multi | Y |
| referral_source | enum | Y |
| referral_name | text | N |

---

## 4. Declarations (checkboxes — required)

- [ ] I understand this is **not** a CSC franchise or government appointment unless separate written authority exists.  
- [ ] I understand **no income is guaranteed**.  
- [ ] I will not use CSC/government logos without licence.  
- [ ] Information provided is true; false info may reject application.  
- [ ] I consent to contact for this application and to processing of data for due diligence per privacy notice.

---

## 5. Document upload list (application stage)

| Document | Required at APP | Notes |
|----------|-----------------|-------|
| Photo ID | Y | |
| Address proof | Y | |
| PAN (or Form 60 path if allowed) | Y/policy | |
| Passport photo | Y | |
| Shop/rent proof | N / Y if dedicated | |
| Cancelled cheque / bank proof | Y before AGR | |

---

## 6. Internal-only fields (staff)

| Field | Notes |
|-------|-------|
| eligibility_score | Optional |
| territory_conflict | Y/N |
| dd_status | |
| assigned_owner | |
| notes | No citizen OTP/PII dumps |

---

## Cross-links

- Onboarding checklist: `02-PARTNER-ONBOARDING-CHECKLIST.md`  
- CRM fields: `10-TECH-AND-SYSTEMS/03-CRM-STAGE-AND-FIELD-LIST.md`  
- Privacy outline: `09-LEGAL-COMPLIANCE/03-PRIVACY-NOTICE-OUTLINE.md`
