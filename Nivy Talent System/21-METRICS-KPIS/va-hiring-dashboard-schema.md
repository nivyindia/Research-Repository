---
original_drive_name: "VA Hiring Dashboard"
original_drive_id: "1uSGmeyqNZGQLpErzDhJqC3asSO3R3M5Pyb6NHwTm6Nk"
migration_date: "2026-09-27"
status: extracted-schema-only
source: Google Drive (Nivy HR)
note: Structure only. No candidate data.
---

# VA Hiring Dashboard — Schema & Metrics Notes

## Source
Google Spreadsheet used as operational tracker for the VA Hiring Funnel (linked to Google Form responses).

## Observed Columns / Fields (from Form Responses sheet)
- Timestamp
- Email Address
- Score
- Full Name / Phone / Email / Country (PII — store only in operational ATS)
- Student / Working / Freelancer status
- Multiple Yes/No commitment & discipline filters (see `03-CANDIDATE-ACQUISITION/va-screening-form-schema.md`)
- Motivation open answers
- Knowledge screening question responses
- Final agreement checkbox

## Recommended Operational Tracking Fields (for rebuild)

| Field | Purpose |
|-------|--------|
| Candidate ID (internal) | Unique non-PII key |
| Batch ID | Batch control (max 50) |
| Stage | Current funnel stage |
| Status | Pass / Fail / Pending / Redirected to Paid Training |
| Score | Auto or manual evaluation score |
| Email Sent Time | Stage 0 deadline control |
| Deadline | Stage-specific |
| Trial Task Submitted | Yes/No + timestamp |
| Interview Booked | Yes/No + slot |
| Orientation Attended | Yes/No |
| Agreement Signed | Yes/No |
| Training KPI % | Rolling performance |
| Source | Ad / Referral / Portal |
| Notes | Free text (no sensitive data in Git) |

## KPIs Suggested by Funnel Design
- Apply rate (Stage 0 → Stage 1): target 20–30%
- Test pass rate
- Trial task completion & quality rate
- Interview show-up rate
- Orientation attendance rate
- Agreement sign rate
- Training retention / 65%+ performance rate
- Paid Training conversion rate (from failures)
- Cost per hired / time-to-hire

## Rule
Dashboard remains operational in Google Workspace / ATS. Only schema and metric definitions live in this repository.
