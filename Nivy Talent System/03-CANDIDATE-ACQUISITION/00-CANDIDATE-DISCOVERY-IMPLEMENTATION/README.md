# Candidate Discovery & Qualification — Implementation Package

This is the P0 implementation package for Nivy's most important hiring capability: finding the right people, not merely collecting more applicants.

## Canonical lifecycle

Target Role → Role Success Profile → Source Map → Discovery → Intake → Identity/Deduplication → Basic Eligibility → Role Fit → Structured Screen → Practical Evidence → Repeated Paid Tasks → Training/Remediation → Work Trial/Internship → Probation → Verified Talent Pool → Outcome Feedback → Source Learning

## Core principle

REACH → DISCOVER → VERIFY → TEST → OBSERVE → DEVELOP → TRUST → DEPLOY

## Package

| File | Purpose |
|---|---|
| 01-IMPLEMENTATION-PLAN.md | Build sequence and release gates |
| 02-PROGRESS-TRACKER.md | Single execution tracker |
| 03-COMMON-PROCESS.md | Process used by every role |
| 04-ROLE-VARIATION-MATRIX.md | What changes by role |
| 05-SOURCE-MATRIX.md | Candidate discovery channels |
| 06-EVIDENCE-FRAMEWORK.md | Evidence and reliability model |
| 07-DATA-MODEL.md | Operational records |
| 08-AUTOMATION-AI.md | n8n and AI implementation |
| 09-PILOT-ACCEPTANCE.md | Pilot and V1 release tests |
| 10-ROLE-PACK-TEMPLATE.md | Template for every role |

## Initial role families

Computer/Data Operator; Digital Marketing/VA; SEO; Social/Content; Paid Ads; Web Development; App Development; AI/Automation; Accounting/Bookkeeping; CPA/CEA/Finance Support; BDE/Sales; Project/Operations.

## Reuse rule

Existing Talent System assets remain source material. This package connects them into one implementation system.

Relevant existing assets:
- 03-CANDIDATE-ACQUISITION
- 04-SCREENING
- 05-PAID-ASSESSMENT
- 06-SCORING
- 16-ROLE-WISE-SYSTEMS
- 02-TALENT-SOURCING
- 10-TALENT-POOL

Do not duplicate mature assets unnecessarily.

## Data boundary

GitHub stores process definitions, schemas, rubrics and templates. Candidate PII, CVs, phone numbers, emails and live application responses belong in the operational ATS/CRM/database.
