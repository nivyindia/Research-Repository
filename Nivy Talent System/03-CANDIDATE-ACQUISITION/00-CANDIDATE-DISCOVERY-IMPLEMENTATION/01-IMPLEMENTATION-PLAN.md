# Candidate Discovery & Qualification — V1 Implementation Plan

## Priority

P0 — implement before scaling recruitment volume.

## 1. Foundation

- Confirm canonical Candidate ID.
- Confirm operational ATS/CRM/database.
- Confirm resume/application intake channel.
- Define pipeline states.
- Define source IDs and campaign IDs.
- Define consent/contact rules.
- Define human approval gates.

## 2. Role Success Profiles

Create one profile before sourcing each role.

Each profile must contain:
- role objective
- must-have requirements
- trainable requirements
- operational constraints
- 5–7 competencies
- computer/AI requirements
- 3–5 observable reliability behaviours
- source plan
- structured screen
- practical task
- three consistency tasks
- evidence rubric
- advancement gates
- compensation/engagement options

First five: Computer/Data Operator, Digital Marketing/VA, Accounting, AI/Automation, BDE/Sales.

## 3. Source Mapping

For each role map:
- direct applicants
- colleges/universities
- placement cells
- training institutes
- trainers/mentors
- hostels/PG/student communities where appropriate
- job platforms
- LinkedIn/professional communities
- Facebook/Telegram/approved WhatsApp communities
- referrals/alumni
- Nivy Jobs
- Nivy Academy
- historical candidates
- freelancers/contractors
- specialist partners

Every candidate must retain source and campaign provenance.

## 4. Candidate Discovery

Run four routes:

1. Inbound — job posts, forms, Nivy Jobs, Nivy Academy, referrals.
2. Institutional — colleges, placement cells, institutes, trainers and ambassadors.
3. Community — approved professional/social communities.
4. Research — permitted public professional/portfolio discovery.

## 5. Canonical Intake

One common application model with role-specific extensions.

Core information:
identity/contact in ATS/CRM, target role, source, campaign, education/experience, availability, work mode, device/internet, skills/tools, AI familiarity, compensation expectations, CV/portfolio reference and contact preference.

## 6. Progressive Qualification

1. Basic eligibility
2. Role-fit questions
3. 15–20 minute structured screen
4. Short role-specific paid practical task where appropriate
5. Three small paid consistency tasks
6. Controlled work trial/internship where useful
7. 30/60/90 probation for employees

## 7. Evidence and Routing

Possible routes:
- core hire
- verified talent pool
- internship/apprenticeship
- targeted training
- project/assignment pool
- specialist contractor
- outsourced partner
- re-engagement
- not currently suitable

Every route needs evidence and next action.

## 8. Automation

Source/Form → n8n → Candidate ID → duplicate check → role routing → screen invite → reminders → assessment capture → evidence record → reviewer queue → status message → next stage.

AI assists with profile extraction, source research, evidence summaries, missing-data detection, role routing and analytics.

Human approval remains for consequential progression, rejection and final hiring.

## 9. Outcome Learning

Connect source → campaign → candidate → qualification → work → outcome.

Measure which sources and evidence signals correlate with successful downstream performance.

## 10. V1 Release Gate

V1 is complete only when real candidates can move from discovery to evidence-backed disposition with source attribution and downstream outcome tracking.

Minimum acceptance:
- 100 candidate records
- multiple source types
- duplicate detection
- at least five role families
- role-specific evidence
- repeated-task observation
- human review
- traceable source-to-outcome data

## Deliberately outside V1

No autonomous hiring, mass scraping, complex AI matching, every possible role, or full international/community automation. First prove the discovery loop with real candidates.
