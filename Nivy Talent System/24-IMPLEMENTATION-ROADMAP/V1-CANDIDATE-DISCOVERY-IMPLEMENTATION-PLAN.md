# V1 Candidate Discovery Implementation Plan

## Priority
P0 — highest-priority V1 workstream.

Before scaling communities, partners or automation, define how Nivy recognises a potentially strong candidate and obtains reliable evidence.

## Build sequence

### 1. Role Success Profiles
Create five profiles:
- Computer/Data Operator
- Accounting
- Digital Marketing
- AI/Automation
- BDE/Sales

### 2. Source map
For every role map direct sources, communities, colleges, institutes, referrals, job boards, portfolio/professional sources and historical candidates.

### 3. Canonical intake
One application model with source/campaign attribution.

### 4. Qualification
Implement hard requirements, role-fit questions, structured screen, practical task and evidence rubric.

### 5. Reliability observation
Run three small paid tasks with controlled deadlines and communication expectations.

### 6. Evidence record
Store requirement status, assessment evidence, observed behaviours, task outcomes, reviewer notes, missing evidence and next action.

### 7. Talent Pool
Promote evidence-backed profiles into the appropriate pool category.

## V1 candidate-finding operating loop

1. Define what success looks like
2. Identify where those candidates can be found
3. Acquire candidate
4. Verify minimum requirements
5. Gather job-relevant evidence cheaply
6. Observe repeated behaviour
7. Advance using documented evidence
8. Record downstream outcome
9. Learn which sources/signals predicted success
10. Improve the next campaign

This creates a closed-loop sourcing system rather than a static recruitment database.

## V1 automation backlog

P0:
- application → candidate ID
- source attribution
- duplicate detection
- screening scheduling
- assessment issue/reminder
- submission capture
- evidence record
- reviewer queue
- status communication

P1:
- candidate profile extraction
- source/campaign analytics
- role routing
- AI evidence summarisation
- missing-data detection
- reactivation queue

P2:
- public-source research assistant
- institute/college target discovery
- candidate research assistant
- AI-assisted matching

## Acceptance tests

V1 is not complete until:
- 100 candidates can enter with one canonical identity each
- source/campaign is known for every candidate
- the same role uses the same qualification rules
- candidate evidence is separated from self-reported claims
- reliability is observed across repeated work
- duplicate candidates are detected
- recruiter can see next action without opening multiple systems
- consequential automated recommendations have a human review path
- downstream outcomes can be traced to source and qualification evidence

## Reuse-first resources

Existing resources to inspect/adapt:
- 03-CANDIDATE-ACQUISITION/va-screening-form-schema.md
- 03-CANDIDATE-ACQUISITION/fresher-intake-process.md
- 04-SCREENING/
- 05-PAID-ASSESSMENT/
- 06-SCORING/
- 16-ROLE-WISE-SYSTEMS/
- 10-TALENT-POOL/
- Nivy Research Data/Screening
- Notion - Nivy OS/Screening
- Nivy Jobs/Sales-Process-Steps.md
- Chats/ChatGPT/Multi Agent AIOS/agents/lead-intelligence/
