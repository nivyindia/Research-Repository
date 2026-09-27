# Contact Information Form — Schema Only

**Source:** Google Drive → HR / Fresher Screening Forms → Contact Information (Google Form)  
**Form ID:** `1QDmzrlnLKAzmFcnvya85JqcOgBwzrk6ipNGRynPmq-M`  
**Responses sheet (structure only):** `1spRbaO8Rf1aMZia0BPMCxga3tTnBlVAmN-e2BiyXsPw`  
**Link (form):** https://docs.google.com/forms/d/1QDmzrlnLKAzmFcnvya85JqcOgBwzrk6ipNGRynPmq-M/edit  
**Migrated:** 2026-09-27  
**Status:** Schema extracted — **no candidate PII**

---

## Purpose

Primary fresher / candidate intake form used for VA, BDE/Sales, Social Media Management, and related entry roles. Collects contact + eligibility + program understanding quiz + academic basics.

## Field schema (no response data)

| Field group | Field name | Type / notes |
|-------------|------------|--------------|
| Meta | Timestamp | Auto |
| Identity | Name | Text |
| Identity | Gender | Choice |
| Contact | Email | Email |
| Contact | Email Address | Email (duplicate/alternate) |
| Contact | Country | Text |
| Contact | Phone with country code | Phone |
| Contact | Whatsapp with country code | Phone |
| Role | Position | Choice (e.g. Virtual Assistant, Sales/BDE, Social Media Management) |
| Assets | CV/Portfolio | File upload link |
| Status | Status / Shortlist / Training / Offer Letter / Performance | Internal workflow columns |
| Referral | Referred by Institute Name and Location | Text |
| Goals | What is your Career Goal | Text |
| Academic | What is Your Degree (BBA/BCA etc) | Text |
| Academic | Percentage of Marks in 10th | Number |
| Academic | Percentage of Marks in 12th | Number |
| Academic | Percentage of Marks in Graduation | Number |
| Academic | Applying for | Choice |
| Motivation | Reasons you are applying for jobs | Multi-select |
| Program quiz | Primary highlight of the 3-month training program | MCQ |
| Program quiz | Bond of ₹5000 if exit before completion — agree? | Yes/No |
| Program quiz | Earn per sale during training | MCQ |
| Program quiz | Score above 80% outcome | MCQ |
| Program quiz | Educational background NOT eligible | MCQ |
| Program quiz | Minimum % / CGPA in 10th, 12th, degree | MCQ |
| Program quiz | Work mode for this role | MCQ |
| Program quiz | Score 65–80% outcome | MCQ |
| Program quiz | Key requirement to apply | MCQ |
| Program quiz | Consequence of leaving training mid-way | MCQ |
| Program quiz | What is provided if not selected after training | MCQ |
| Ops quiz | When must you select shift for upcoming week | MCQ |
| Ops quiz | Evening shift second daily report due | MCQ |
| Ops quiz | Primary reason for Workfolio tracking | MCQ |
| Ops quiz | Full-time expected active screen time (9-hr shift) | MCQ |
| Ops quiz | Total break time full-time | MCQ |
| Ops quiz | Rule for mandatory meetings | MCQ |
| Ops quiz | Missed daily check-in report — what to do | MCQ |
| Ops quiz | What Workfolio does NOT track | MCQ |
| Ops quiz | Days of mandatory meetings | MCQ |
| Ops quiz | Part-time expected active screen time | MCQ |
| Mindset quiz | WFH misconceptions (real work, accountability, balance, communication, who succeeds, job-switching risk) | MCQ series |

## Workflow columns (internal)

Seen on responses sheet (do not store candidate answers publicly):

- Status / Eligible / Selected / Not Eligible  
- Shortlist, Training, Offer Letter, Performance  
- Referral Column  

## PII rule

- **Never** commit raw response rows (names, phones, emails, CV links).  
- Schema + question text only in this repo.  
- Live candidate data stays in Drive / private ATS.

## Talent System mapping

| Destination | Use |
|-------------|-----|
| `03-CANDIDATE-ACQUISITION/` | This schema + intake process |
| `04-SCREENING/` | Program + ops + mindset quiz themes feed screening design |
| `18-TEMPLATES/` | Future form rebuild / ATS field map |
| `12-CANDIDATE-COMMUNICATION/` | Status labels for outreach stages |

## Next

- Rebuild form field map in ATS of choice  
- Separate eligibility quiz from contact fields for cleaner scoring  
