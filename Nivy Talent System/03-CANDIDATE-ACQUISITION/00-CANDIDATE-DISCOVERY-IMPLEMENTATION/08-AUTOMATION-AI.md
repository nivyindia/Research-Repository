# Automation and AI Implementation

## Architecture

Approved source/form/job platform → n8n → ATS/CRM/database → candidate workflow → AI assistance → human review → communication → audit/event log

n8n is orchestration. It is not the candidate database and not the AI brain.

## V1 automations

### Intake
Application → validate → Candidate ID → source/campaign → duplicate check → acknowledgement.

### Routing
Role selected → Role Success Profile → correct screen and assessment path.

### Screening
Eligible → screen scheduling → reminders → completion capture → reviewer queue.

### Assessment
Issue task → deadline → reminder → submission capture → reviewer assignment → evidence record.

### Consistency
Task 1 → Task 2 → Task 3 → reliability summary → human review.

### Status
Approved status templates for progression, hold, training, rejection and re-engagement.

### Analytics
Source/campaign → stage conversion → downstream outcome.

## AI assistants

1. Source Research Assistant
2. Institution/Partner Research Assistant
3. Candidate Profile Extractor
4. Role-Routing Assistant
5. Screening Preparation Assistant
6. Evidence Summariser
7. Missing-Evidence Detector
8. Assessment Coordination Assistant
9. Source Analytics Assistant
10. Talent Pool Matching Assistant

## Human controls

Human approval is required for consequential progression, rejection, compensation exceptions and final hiring decisions.

## AI guardrails

- do not infer protected characteristics
- do not use sensitive data as capability proxy
- do not fabricate candidate evidence
- distinguish claims from verified evidence
- preserve provenance
- log material AI-assisted actions
- give reviewers visibility into evidence
