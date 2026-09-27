---
original_drive_name: "VA Hiring Dashboard / Screening Forms"
original_drive_id: "1uSGmeyqNZGQLpErzDhJqC3asSO3R3M5Pyb6NHwTm6Nk (and related forms)"
migration_date: "2026-09-27"
status: extracted-schema-only
source: Google Drive (Nivy HR / careers.nivy)
note: No candidate PII included. Field list and process structure only.
---

# VA Screening / Application Form — Schema (No PII)

## Purpose
Document the structure of the candidate intake + screening form used in the VA Hiring Funnel so it can be rebuilt or automated without storing personal data in GitHub.

---

## Core Identity Fields (operational — store only in ATS/CRM)
- Timestamp
- Email Address
- Full Name
- Phone Number
- Email ID
- Country

## Status / Context
- Are you a student / working / freelancer?

## Commitment & Schedule Filters (Yes/No style)
- Willing to work 8–9 hours daily (fixed schedule)?
- Available during fixed working hours (e.g. 10 AM – 6 PM)?
- Okay with NO flexible timing and strict schedule adherence?
- Serious about completing structured onboarding and training fully?
- Agree that missing training sessions without prior notice may cancel selection?
- Willing to commit for minimum 6 months?
- Agree to pay training compensation ($25–$50 USD) if leaving before 6 months?
- Willing to sign formal 6-month commitment agreement before starting?

## Reporting & Tracking Consent
- Comfortable submitting DAILY WORK REPORTS (Google Sheet/Form)?
- Okay with work and computer activities being tracked (reports/screenshots/activity logs)?
- Agree that failure to submit reports or improper work leads to strict action (warning/removal)?
- Understand that NO REPORT = NO WORK counted?
- Understand minimum 65% performance required to continue?
- Understand payment is strictly sales/target based (no sales may mean termination without payment)?
- Will inform in advance if unavailable during work hours?
- Understand frequent absence may lead to termination?
- Agree leaves must be pre-approved (24 hours prior except emergencies)?

## Motivation / Open Questions
- Why do you want this job?
- If given work today, will you start immediately without excuses?
- Have you left any job/training in between before? If yes, why?

## Final Declaration
- Section: Final Agreement Declaration (Checkbox Required)

## Knowledge / Screening Questions (auto-scoreable)
- What is the main role of a Virtual Assistant?
- What is lead generation?
- What is appointment setting?
- What is a follow-up?
- What is CRM used for?
- Which is a professional message?
- If a client says “not interested”, what should you do?
- What tone should be used in business communication?
- If a client doesn’t reply, what should you do?
- What is important in communication?
- Google Sheets is used for:
- Which tool is used for team communication?
- Excel is mainly used for:
- What is ChatGPT used for?
- CRM tools help in:
- If you don’t understand a task, what should you do?
- How do you manage multiple tasks?
- What ensures productivity?
- What should you do if you miss a task deadline?
- Daily reporting helps in:
- Working hours are important because:
- If you are unavailable during work hours:
- What happens if you don’t submit reports?
- Why is discipline important?
- What is the best attitude for this role?
- What is the minimum requirement to qualify for continuation in the program?
- What happens if a candidate does not follow reporting and work discipline rules?

---

## Process Notes
- Form feeds into Google Sheet (VA Hiring Dashboard)
- Auto-scoring enabled on knowledge section where possible
- Pass → Stage 2 (Trial Task)
- Fail / No submission → Paid Training Path redirect
- Score field present in responses sheet

## Data Rule
Never commit raw form responses (names, phones, emails) to this repository. Use only schema + anonymised process documentation.
