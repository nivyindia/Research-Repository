# Candidate Discovery V1 — Software Stack & Tool Map

**Purpose:** Define exactly which online software is used at each stage of the Nivy Talent System, what each tool does, what data it stores, and where automation happens.

## 1. Recommended V1 stack

| Layer | Primary tool | What it does | System-of-record? |
|---|---|---|---|
| Documentation / SOP | GitHub | SOPs, schemas, role packs, rubrics, prompts, versioning | No candidate PII |
| Candidate application | Google Forms | Application/intake forms | No |
| Candidate operational table | Google Sheets | MVP candidate pipeline, IDs, source/campaign, stage, task status | Yes for V1 operational metadata |
| Candidate documents | Google Drive | CVs, portfolios, assessment artifacts, controlled documents | Yes for documents |
| Candidate email | Gmail / Google Workspace | Application, screening, assessment, status and offer communication | Communication record |
| Scheduling | Google Calendar | Interviews, screens, work trials, reviews | No |
| Video interview | Google Meet | Remote screening/interviews | No |
| Templates | Google Docs | Email/offer/interview/assessment templates | No |
| Automation/orchestration | n8n | Form → Sheet → Drive → Gmail → Calendar → AI → reminders → logs | No |
| Lightweight custom logic | Google Apps Script | Form/Sheet helper logic where n8n is not suitable | No; only controlled operational logic |
| AI assistance | Approved LLM/API or local model | Extraction, summarisation, routing suggestions, missing-evidence detection | No |
| Source research | Search engine + public websites + approved platform tools | Discover institutions, communities, portfolios and sourcing channels | No |
| Job/community distribution | Nivy Jobs + approved job/social/community channels | Candidate reach | No |
| Analytics | Google Sheets + Looker Studio where useful | Funnel/source/outcome reporting | No |
| Code/version control | GitHub | Versioned process definitions | No candidate PII |

## 2. MVP principle

Do not buy a full ATS before the process is proven.

V1 can operate with:

MVP FLOW: Google Forms → Google Sheets → Google Drive → Gmail → Calendar/Meet → n8n → AI assistance → Human review

GitHub remains the **process-definition repository**, not the candidate database.

## 3. Google Workspace folder structure

Create one restricted Google Drive root:

Nivy Talent System — Operations

Recommended folders:

- 00_ADMIN
- 01_ROLE_PROFILES
- 02_JOB_CAMPAIGNS
- 03_CANDIDATE_CV
- 04_CANDIDATE_APPLICATIONS
- 05_SCREENING
- 06_ASSESSMENTS
- 07_CONSISTENCY_TASKS
- 08_TRAINING
- 09_INTERNSHIP_WORK_TRIAL
- 10_PROBATION
- 11_OFFERS_AGREEMENTS
- 12_TALENT_POOL
- 13_REPORTS
- 99_ARCHIVE

Candidate folders should use the internal Candidate ID rather than exposing unnecessary personal information in folder names.

Example: CAND-2026-000123

## 4. Core Google Sheets

Use separate controlled sheets/tabs rather than one uncontrolled master spreadsheet.

### Candidates
- Candidate ID
- Person ID
- Application ID
- name
- email
- phone
- city
- role
- current stage
- source ID
- campaign ID
- application date
- availability
- work mode
- CV Drive reference
- consent/contact status
- owner
- next action
- next action date

### Sources
- Source ID
- source family
- source name
- URL/reference
- source owner
- active/inactive
- notes

### Campaigns
- Campaign ID
- Source ID
- role
- city/region
- start date
- end date
- campaign owner
- landing/form link
- target
- status

### Stage History
- Candidate ID
- application ID
- stage
- entered
- exited
- decision
- reason category
- reviewer
- evidence reference

### Assessments
- Candidate ID
- assessment ID
- assessment type
- task version
- assigned
- due
- submitted
- score
- evidence link
- reviewer
- result

### Consistency Tasks
- Candidate ID
- task number
- assigned date
- due date
- submitted date
- quality
- deadline
- instruction following
- communication
- correction response
- supervision required
- reviewer

### Outcomes
- Candidate ID
- role
- route
- work start
- outcome date
- quality result
- retention/result
- re-engagement
- source quality feedback

## 5. Google Forms

Create separate forms only where the process genuinely differs.

### Form A — Candidate Application
First intake.

### Form B — Screening Confirmation
Availability and structured pre-screen.

### Form C — Assessment Submission
Task completion metadata/link.

### Form D — Reviewer Evidence Form
Internal evidence capture.

### Form E — Candidate Feedback
Post-assessment/work-trial feedback where useful.

Avoid creating dozens of role-specific forms. Use a common core plus role-specific sections/questions.

## 6. Gmail

Use a dedicated recruitment mailbox or controlled Google Workspace account.

Suggested labels:

- TALENT/NEW
- TALENT/SCREEN
- TALENT/ASSESSMENT
- TALENT/CONSISTENCY
- TALENT/INTERNSHIP
- TALENT/OFFER
- TALENT/REJECTED
- TALENT/TALENT-POOL
- TALENT/REENGAGEMENT
- TALENT/EXCEPTIONS

n8n should send standard transactional messages from approved templates and log the event in the candidate record.

## 7. Google Calendar + Meet

Use Calendar for:
- screening calls
- interviews
- assessment review calls
- internship/work-trial check-ins
- probation reviews

Each event should contain:
- Candidate ID
- role
- stage
- owner
- purpose
- relevant Drive/Sheet reference

Use Google Meet for remote calls when appropriate.

## 8. Google Drive document controls

Drive is the document store, not the decision engine.

Recommended:
- restricted access
- least privilege
- no public candidate CV folders
- no public candidate spreadsheets
- versioned templates
- controlled sharing
- retention/archive policy

Candidate documents should be referenced from the operational record instead of copied into GitHub.

## 9. n8n responsibilities

n8n is the orchestration layer.

Typical sequence:

Trigger → Validate → Create/resolve Candidate ID → Deduplicate → Write candidate record → Store/route document → Send communication → Create task/calendar event → Wait → Reminder → Capture result → Update stage → Log event

n8n should:
- connect systems
- schedule actions
- call approved APIs
- execute deterministic rules
- call AI assistance
- create audit/event records
- retry failed operations
- alert humans on exceptions

n8n should NOT become the permanent candidate database.

## 10. AI responsibilities

AI may:
- extract CV fields
- summarise public professional information
- identify missing evidence
- suggest role routing
- prepare screen summaries
- summarise assessment evidence
- draft candidate communications
- identify source trends
- generate reviewer queues

AI must not:
- invent candidate evidence
- infer protected/sensitive characteristics
- use demographic proxies for capability
- make irreversible hiring/rejection decisions without human review
- replace observed work evidence

## 11. Future migration path

When Google Sheets becomes insufficient:

Google Forms/other intake → n8n → ATS/CRM/Postgres → Drive → Gmail/Calendar → analytics

The following identifiers must remain stable:
- Candidate ID
- Person ID
- Application ID
- Source ID
- Campaign ID
- Assessment ID

This preserves historical source-to-outcome analysis.

## 12. V1 cost-control rule

Prefer existing/free or already-available tools first.

Add a paid product only when it solves a measured bottleneck such as:
- excessive manual data entry
- high candidate volume
- duplicate handling
- scheduling complexity
- communication volume
- assessment scale
- reporting limitations
- compliance/access requirements

Every new tool must have a defined owner, purpose, data handled, integration point and exit/migration path.
