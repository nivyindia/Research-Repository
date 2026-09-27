# Nivy Talent System — Full Implementation Plan

## 1. Target architecture

Nivy Talent System is the shared internal engine.

**Nivy Academy** = learning, assessment, remediation, certification and talent-development front end.

**Nivy Jobs** = opportunities, employers, recruitment, matching, placement and project-work front end.

Both feed one canonical **Talent Pool**.

## 2. Workstreams

### WS-01 — Research consolidation
Inventory existing Nivy Jobs/Academy/HR resources, compare duplicates, extract reusable assets, archive superseded material.

### WS-02 — Candidate data migration
Inventory careers/HR inboxes, spreadsheets, CSVs, old forms and resumes. Build secure staging, dedupe and canonical candidate IDs.

### WS-03 — Talent intake
One master registration model with programme/source/application context attached as separate records.

### WS-04 — Screening
Structured 15–20 minute screen with evidence-based scoring.

### WS-05 — Practical assessment
Paid role-specific assessment followed by three small paid tasks to measure consistency.

### WS-06 — Academy integration
Use Academy for targeted training and remediation rather than training every applicant before selection.

### WS-07 — Internship/work trial
Paid internship/apprenticeship with mentor, task assignment, QC and reporting.

### WS-08 — Probation
30/60/90-day evidence-based reviews.

### WS-09 — Talent pool
Maintain verified skills, assessment evidence, availability, work mode, compensation expectations and status.

### WS-10 — Jobs/employer matching
Match talent to Nivy/internal work, external employer roles, freelance projects and partner opportunities.

### WS-11 — Institute/city sourcing
Colleges, universities, training centres, hostels, referrals and Tier 2/3/4 campaigns.

### WS-12 — Automation
Forms + email + calendar + ATS/CRM + WhatsApp + database + n8n + AI assistance.

### WS-13 — Measurement
Funnel, quality, consistency, probation, source quality, time-to-productivity and automation reliability.

---

# 3. Phased implementation

## Phase 0 — Governance & consolidation
**Goal:** stop fragmentation.

- Create resource registry.
- Identify canonical versions.
- Preserve original source paths.
- Define PII boundary.
- Define Candidate ID.
- Define status/state machine.
- Define human-vs-AI decision boundaries.

**Exit:** one approved architecture and no ambiguous source of truth.

## Phase 1 — Historical data discovery
Sources:
- careers.nivi@gmail.com
- Nivy HR Team Gmail
- other approved recruitment inboxes
- Excel/CSV applicant files
- old forms
- existing resumes
- existing candidate lists
- old assessment/evaluation files

Actions:
- Export/collect only authorized data.
- Inventory fields.
- Detect duplicates.
- Separate candidate records from unrelated contacts.
- Preserve original source and date.
- Assign migration batch IDs.
- Map into canonical schema.

**Exit:** migration inventory + dedupe report.

## Phase 2 — Canonical candidate database
Minimum entities:
Candidate, ContactMethod, Consent/Preference, Application, Source, Role, Screening, Assessment, Submission, Score, Task, Training, Internship, Probation, Job, Assignment, Institute, Campaign, Availability, Communication, AuditLog.

**Exit:** searchable candidate/talent system with one identity.

## Phase 3 — Acquisition
Build:
- Nivy Jobs registration
- Academy learner registration
- internal referral
- institute referral
- job application
- freelancer/partner application
- employer job requirement

All forms feed the same candidate identity model.

## Phase 4 — Screening
Implement:
- basic eligibility
- structured 15–20 minute screen
- role-specific questions
- evidence notes
- automatic routing
- human review for borderline cases.

## Phase 5 — Paid assessment
Role packs:
Computer Operator, Accounting, Tax Support, BDE/Sales, Digital Marketing, SEO/PPC, Social Media, Content, Design/Video, WordPress, Software, AI/Automation, QA, Operations/VA.

Assessment:
Task Quality 25 + Deadline 20 + Instructions 15 + Communication 10 + Problem Solving 10 + Learning 10 + AI/Tools 5 + Documentation 5.

## Phase 6 — Consistency
Use 3 small paid tasks across approximately 3 weeks.

Measure:
- quality stability
- deadline reliability
- communication
- correction rate
- supervision required
- learning curve.

## Phase 7 — Academy
Candidates with a skill gap enter targeted Academy learning.

```
Assessment
→ Gap
→ Course/Module
→ Assignment
→ Re-test
→ Work
```

## Phase 8 — Paid internship/work trial
Assign real but controlled work, mentor and QC.

## Phase 9 — Probation
30/60/90 evidence and manager review.

## Phase 10 — Talent Pool
Verified candidates become searchable by:
role, skills, score/evidence, reliability, availability, location/time zone, work mode, rate and status.

## Phase 11 — Jobs/employer marketplace
Employer requirement → job record → matching → shortlist → interview → placement/project → outcome.

## Phase 12 — Institute/city network
Create partner pipeline and recurring campaigns. Measure downstream quality, not just applicant volume.

## Phase 13 — Automation
Automate only after workflows are stable.

Core automations:
1. New application → candidate ID
2. CV parse → structured profile
3. Duplicate detection
4. Eligibility routing
5. Screening invitation
6. Scheduling
7. Assessment issue/reminders
8. Submission capture
9. Evaluation draft
10. Status communication
11. Training assignment
12. Probation reminders
13. Talent availability alerts
14. Matching suggestions
15. KPI dashboards.

## Phase 14 — Pilot
Start with 3–5 candidates per role family.

Pilot roles:
- Computer/Data Operator
- Accounting
- Digital Marketing
- AI/Automation
- Sales/BDE

Do not mass-hire before the pipeline demonstrates repeatability.

---

# 4. Data architecture

Use:

```
PERSON
  ↓
CANDIDATE
  ↓
APPLICATION(S)
  ↓
SCREENING
  ↓
ASSESSMENT(S)
  ↓
OBSERVED WORK
  ↓
TRAINING (optional)
  ↓
INTERNSHIP
  ↓
PROBATION
  ↓
TALENT POOL
  ↓
JOB / PROJECT ASSIGNMENT
```

A person can have multiple applications, programmes and opportunities without creating duplicate identities.

---

# 5. Email and historical-data migration

Do not manually copy resumes one by one.

Build an ingestion process:

```
Inbox / Spreadsheet
→ export
→ staging
→ parse
→ dedupe
→ candidate matching
→ consent/contact preference
→ canonical Candidate ID
→ operational database
→ archive original
```

Recommended initial mailbox categories:
- Recruitment intake
- Existing applicants
- Shortlisted
- Rejected/closed
- Employees
- Freelancers/partners
- Institutes
- Employers
- Unknown / needs review

**Important:** access to the user's Gmail accounts is not assumed by this repository scan. When we start actual mailbox migration, the relevant Gmail/Drive connection or exported files must be supplied/authorized.

---

# 6. What goes into GitHub vs operational systems

| Data | GitHub Research Repo | Operational DB/ATS |
|---|---|---|
| SOPs | Yes | Copy/reference |
| Prompts | Yes | Runtime copy |
| Schemas | Yes | Implemented |
| Tool research | Yes | — |
| Assessment design | Yes | Runtime version |
| Candidate CV | No | Yes |
| Candidate phone/email | No | Yes |
| Historical applicant Excel | No raw PII | Yes |
| Score records | Schema only | Yes |
| Communication templates | Yes | Yes |
| Automation design | Yes | Runtime |
| Audit policy | Yes | Yes |

---

# 7. Folder strategy

Keep working here:

`Nivy Talent System/`

Do **not** split the engine into separate `Nivy Academy System` and `Nivy Jobs System` repositories/folders yet.

Inside the Talent System:
- common engine = current numbered folders
- Academy-specific integration = later under Academy Integration
- Jobs-specific integration = later under Jobs Integration
- shared Talent Pool remains common.

The existing `Nivy Academy/` and `Nivy Jobs/` folders remain source/provenance locations until their validated content is consolidated.

---

# 8. Definition of done

The system is implementation-ready when:

- one canonical candidate identity exists
- historical sources can be imported
- duplicates can be resolved
- applications can be tracked
- screening is standardized
- paid tests are standardized
- repeated work is measured
- Academy can remediate skill gaps
- internship/work trial is tracked
- probation is evidence-based
- talent pool is searchable
- Jobs can match talent to opportunities
- institute/city campaigns can feed the pipeline
- communications are automated with appropriate consent/controls
- KPIs are visible
- PII is outside GitHub
- every automated decision has an auditable human override where appropriate.