# Candidate Discovery Data Model

## Entity chain

PERSON → CANDIDATE → APPLICATION → SCREENING → ASSESSMENT → OBSERVED WORK → TRAINING → INTERNSHIP → PROBATION → TALENT POOL → ASSIGNMENT → OUTCOME

One person may have multiple applications without duplicate person records.

## Candidate record

### Identity/contact
Candidate ID, name, email, phone, location, preferred contact, contact preference. Store live PII only in the operational system.

### Discovery
Source ID, source organisation/community, campaign ID, discovery date, referrer, discovery method, provenance/source URL where applicable.

### Profile
Target role(s), experience, education, skills, tools, AI literacy, CV/portfolio reference, availability, work mode, device/internet readiness, compensation expectations.

### Qualification
Eligibility, screen, assessment, evidence, consistency, training, internship, probation, disposition, next action.

### Outcome
Role/project, reviewer, quality, productivity, deadline adherence, retention, re-engagement and appropriate exit category.

## Traceability

Every candidate should be traceable:

Source → Campaign → Candidate → Qualification → Work → Outcome

This enables source-quality measurement and process improvement.

## GitHub boundary

Schemas and field definitions may be stored in GitHub. Candidate PII and live response records must remain in the operational ATS/CRM/database.
