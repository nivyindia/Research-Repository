# End-to-End Candidate Discovery, Qualification & Hiring SOP — V1

**Status:** V1 operating SOP  
**Scope:** From identifying a hiring requirement to candidate discovery, qualification, practical testing, repeated paid work, internship/work trial, probation and Talent Pool entry.

## 1. Purpose

This SOP explains exactly how Nivy will find, verify, test, observe and deploy candidates.

Objective: find people who can actually perform the required work, follow instructions, meet deadlines, communicate blockers, learn from correction and become reliable contributors.

Canonical lifecycle:

Hiring Need → Role Success Profile → Source Plan → Campaign → Discovery → Intake → Candidate ID → Deduplication → Eligibility → Role Fit → Screen → Practical Test → 3 Consistency Tasks → Training if needed → Paid Work Trial/Internship → Probation → Verified Talent Pool/Core Staff/Project Pool → Outcome Feedback → Source Learning

## 2. Who uses this SOP

| Role | Main responsibility |
|---|---|
| Hiring Manager | Defines business need and approves role |
| Talent/HR Ops | Runs pipeline and candidate communication |
| Sourcer/Researcher | Finds candidates and sources |
| Screening Owner | Conducts structured screen |
| Assessor | Reviews practical evidence |
| Mentor/TL | Runs repeated tasks/training/work trial |
| Department Lead | Validates role capability |
| Finance/Admin | Handles approved payments/offers |
| Automation Owner | Maintains n8n/forms/sheets/integrations |
| Owner/Director | Handles exceptions and final strategic hiring decisions |

One person may perform multiple roles in V1.

## 3. Tool map by process step

| Step | Primary software | Secondary | Human owner |
|---|---|---|---|
| Demand capture | Google Form/Sheet or internal request | Gmail | Hiring Manager |
| Role definition | GitHub + Google Docs | Sheets | Hiring Manager |
| Source research | Search + public websites | Google Sheets | Sourcer |
| Job campaign | Nivy Jobs + job/social channels | Google Drive | Talent Ops |
| Candidate intake | Google Forms | Gmail | Candidate |
| Candidate record | Google Sheets | n8n | Talent Ops |
| CV storage | Google Drive | n8n | Talent Ops |
| Candidate acknowledgement | Gmail | n8n | Automation |
| Deduplication | n8n + Sheets/database | human review | Talent Ops |
| Eligibility | n8n rules | reviewer | Talent Ops |
| Screen booking | Google Calendar | Gmail/Meet | Talent Ops |
| Structured screen | Meet/phone | Google Form | Screener |
| Practical test | Drive/Docs/Sheets/Form | Gmail | Assessor |
| Assessment review | Google Sheets + Drive | AI summary | Assessor |
| Consistency tasks | Gmail + Drive/Sheets | Calendar | Mentor/TL |
| Training | Google Drive/Docs/Academy | Meet | Mentor |
| Work trial | task system + Drive | Calendar | TL |
| Internship | Academy/operational tools | Gmail/Calendar | Mentor |
| Probation | Sheets + Docs | Calendar | Manager |
| Talent Pool | Candidate database + Drive | Gmail | Talent Ops |
| Analytics | Sheets/Looker Studio | n8n | Talent Ops |
| Version control | GitHub | — | System owner |

## 4. Golden rules

1. CV = discovery input, not capability verdict.
2. Every candidate must have a source and campaign where applicable.
3. One person must not receive duplicate Candidate IDs.
4. Candidate PII stays in controlled operational systems.
5. GitHub stores schemas/SOPs/templates, not candidate PII or response dumps.
6. Practical evidence is stronger than self-report.
7. Reliability requires repeated observation.
8. A failed test does not automatically mean permanent rejection if the gap is trainable.
9. A good interview does not automatically prove reliability.
10. AI can assist; humans retain consequential decisions.
11. Every stage must have an owner and next action.
12. Every rejection/hold/advance action should have a reason category and evidence reference.
13. Never use protected or sensitive attributes as capability proxies.
14. Do not build the system around unsolicited bulk messaging, fake accounts, credential sharing or prohibited scraping.
15. Source quality is measured by downstream candidate outcomes, not CV volume.

## 5. STEP 0 — Hiring demand is created

Hiring Manager submits a hiring request.

Minimum fields:
- department
- role
- number required
- reason
- employment/engagement model
- expected start
- hours/week
- work mode
- budget/range
- must-have capabilities
- trainable capabilities
- manager
- urgency

Tool: Google Form → Google Sheet.

n8n:
1. receives request
2. creates Hiring Request ID
3. notifies Hiring Manager/HR
4. checks whether an existing role pack exists
5. creates role setup task if missing

Output: HIR-YYYY-000001.

No sourcing begins until the request is sufficiently defined.

## 6. STEP 1 — Create/confirm Role Success Profile

Before searching for candidates, open the relevant Role Pack.

Required:
- role objective
- must-have
- trainable
- competencies
- computer/tool requirements
- AI/tool familiarity
- reliability behaviours
- source plan
- screen questions
- practical test
- 3-task consistency plan
- evidence rubric
- advancement gates
- compensation/engagement options
- KPIs

If an existing role pack exists:
- reuse it
- adapt version
- record change
- do not create a duplicate document

Output: ROLE-VERSION = ROLE-NAME-vX.

## 7. STEP 2 — Build Source Map

The Sourcer identifies where the right candidates are likely to exist.

### Source families

A. Direct
- Nivy Jobs
- Nivy Academy
- referrals
- historical talent pool
- existing applicants

B. Institutional
- colleges
- universities
- placement cells
- training institutes
- bootcamps
- trainers
- mentors
- campus ambassadors

C. Communities
- LinkedIn communities
- Facebook groups/pages
- Telegram communities
- approved WhatsApp communities
- professional communities

D. Specialist
- freelancer networks
- portfolio communities
- developer communities
- accounting/finance networks
- specialist partners

E. Public professional research
Permitted public portfolios/professional profiles where platform terms and applicable rules allow.

Create SOURCE-ID, then CAMPAIGN-ID.

Example:
SRC-COLLEGE-001
CMP-SEO-LKO-2026-09-001

## 8. STEP 3 — Candidate discovery

The Sourcer executes the source plan.

For every discovery route record:
- Candidate reference if known
- Source ID
- Campaign ID
- role
- discovery date
- discovery route
- public profile/portfolio reference if appropriate
- contact status
- next action

### Inbound
Candidate sees a job post, Nivy Jobs listing, Academy opportunity, referral link or approved social post.

Candidate clicks:
Application Link → Google Form.

### Institutional
Institute/placement cell receives approved job description, role summary, application link, deadline and assessment process.

Candidates apply through the canonical form.

### Community
Post approved opportunity in permitted channels using canonical application link and source/campaign tracking.

Do not manually create uncontrolled candidate records from random messages unless the candidate enters the official intake process.

### Research
Sourcer identifies potentially relevant public professional profiles/portfolios.

Where contact is appropriate and permitted:
- use approved professional outreach
- identify source/campaign
- invite candidate to canonical application

Do not treat public profile information as verified capability.

## 9. STEP 4 — Candidate submits Google Form

Common intake captures:
- role applied
- full name
- email
- phone
- city/region
- education/experience
- availability
- work mode
- device/internet availability where relevant
- skills
- tools
- AI familiarity
- experience
- portfolio/CV
- compensation expectation where appropriate
- source
- campaign
- contact preference/consent fields appropriate to the workflow

Role-specific questions are added as sections.

Form submission:
Google Form → Google Sheet.

n8n watches/processes the new response.

## 10. STEP 5 — Candidate ID creation

n8n checks:
1. email match
2. phone match
3. existing person identifiers
4. previous applications
5. possible duplicate indicators requiring human review

If no match, create CAND-YYYY-000001.

If existing person:
- keep existing Person ID
- create new Application ID
- do not create duplicate person

Output:
Person → Candidate → Application.

## 11. STEP 6 — CV/document storage

If CV is submitted:
1. store in restricted Google Drive
2. create candidate folder/reference
3. save Drive reference in candidate record
4. do not copy CV into GitHub
5. do not make candidate folders public

Recommended:
03_CANDIDATE_CV/CAND-2026-000001/

## 12. STEP 7 — Automated acknowledgement

n8n sends Gmail acknowledgement containing:
- application received
- Candidate ID/reference
- role
- next step
- expected response time
- official contact route

Email event is logged.

If email fails:
- mark exception
- retry
- create human follow-up task

## 13. STEP 8 — Basic eligibility

n8n applies deterministic eligibility rules defined by the role pack.

Examples:
- required skill
- availability
- required work mode
- minimum necessary qualification
- legal/role-specific requirement
- language/tool requirement

Result:
PASS / REVIEW / NOT ELIGIBLE.

If ambiguous:
REVIEW QUEUE → Human decision.

Do not silently reject based on undefined criteria.

## 14. STEP 9 — AI-assisted profile extraction

If enabled, AI reads the CV/application and produces a structured summary:
- claimed skills
- claimed experience
- tools
- portfolio references
- availability
- role matches
- missing information
- evidence that should be tested

AI must distinguish CLAIMED from VERIFIED.

Example:
Claim: "Expert in SEO"
becomes:
Evidence needed: SEO practical task.

Human reviewer can correct AI extraction.

## 15. STEP 10 — Role-fit routing

Candidate is routed to one or more role tracks.

Example:
Marketing applicant → Digital Marketing/VA, SEO, Social/Content or Paid Ads.

Routing is a recommendation, not an automatic final hiring decision.

n8n can assign:
- role track
- reviewer
- next assessment

## 16. STEP 11 — Structured screening

Target duration: 15–20 minutes.

Tools:
- Google Calendar
- Google Meet or phone
- Google screening form

Verify:
- availability
- communication
- instruction following
- role basics
- learning examples
- concrete reliability examples
- blocker behaviour
- actual computer/AI tool usage

Do not score charisma as a proxy for reliability.

Output:
SCREEN-PASS / SCREEN-REVIEW / SCREEN-NOT-PASS plus evidence gaps.

## 17. STEP 12 — Practical assessment

Assign the role-specific task from the Role Pack.

Examples:

Computer/Data Operator:
- enter records
- identify duplicates
- format spreadsheet
- complete forms accurately

Digital Marketing/VA:
- research prospects
- create structured spreadsheet
- prepare simple content/social pack

SEO:
- keyword research
- basic on-page audit
- identify technical/content issues

Accounting:
- sample transactions
- reconciliation
- ledger/P&L exercise

AI/Automation:
- create/explain small automation
- n8n/API workflow
- debug a simple workflow

BDE/Sales:
- prospect research
- outreach draft
- role-play
- follow-up plan

The task should be realistic, bounded, versioned, scored with a rubric, and paid where it represents productive work and payment is applicable.

## 18. STEP 13 — Assessment assignment

n8n:
1. creates Assessment ID
2. selects task version
3. sends Gmail instructions
4. creates Drive workspace
5. records due date
6. schedules reminder
7. waits for submission
8. alerts reviewer

Candidate receives:
- task
- instructions
- deadline
- submission method
- payment terms if applicable
- support/contact route

## 19. STEP 14 — Assessment submission

Candidate submits through:
- Google Form
- Google Drive upload/link
- controlled document/sheet
- approved platform

Submission record:
ASSESS-YYYY-000001.

Reviewer sees:
- requirement
- candidate output
- rubric
- deadline
- communication history

## 20. STEP 15 — Evidence review

Score using the role-specific rubric.

Common dimensions:
- Quality
- Deadline
- Instruction following
- Communication
- Problem solving
- Learning
- Documentation
- AI/tool use

Record:
Observed / Claimed / Missing.

Do not convert unsupported claims into evidence.

## 21. STEP 16 — First routing decision

Possible outcomes:
- Advance
- Trainable gap
- Project-only
- Talent Pool
- Hold
- Exit

A human reviewer approves consequential progression/rejection.

## 22. STEP 17 — Three-task consistency protocol

One successful test is not enough to prove reliability.

Assign approximately three small tasks over a defined observation period.

Track:
- quality
- deadline
- instruction following
- communication
- correction response
- documentation
- supervision required

Example:
Task 1 → correction → Task 2 → increased responsibility → Task 3.

The important signal is whether performance remains reliable across repeated work.

## 23. STEP 18 — Training/remediation

If promising but there is a trainable gap:
1. identify exact gap
2. assign training material
3. set completion date
4. provide example
5. give practice task
6. review
7. retest
8. record learning evidence

Tools may include Nivy Academy, Google Docs, Google Drive, Google Meet and Google Forms.

Training completion alone is not proof of job capability. Re-test the actual skill.

## 24. STEP 19 — Paid work trial / internship

Set:
- start/end
- manager
- mentor
- tasks
- hours
- payment terms
- communication channel
- reporting format
- quality expectations
- escalation route

All productive work should have clear payment/engagement terms.

## 25. STEP 20 — Daily/weekly observation

Mentor/TL records:
- assigned
- completed
- quality
- deadline
- blocker
- communication
- correction
- supervision
- next task

Avoid vague notes such as "Good candidate".

Instead:
"Completed 48/50 records by deadline; 2 formatting errors; corrected after feedback; required one clarification."

This becomes usable evidence.

## 26. STEP 21 — Probation

For employees:

Day 0–30:
- attendance/availability
- deadline reliability
- quality
- reporting
- learning
- communication

Day 31–60:
- increase responsibility

Day 61–90:
- independent output
- consistency
- quality
- ownership
- coordination
- role KPIs

Possible outcomes:
- core staff
- continued development
- project-only
- talent pool
- exit

## 27. STEP 22 — Talent Pool promotion

Verified Talent Pool requires sufficient evidence.

Record:
- verified role(s)
- skill level/evidence
- availability
- work mode
- rate/compensation information where appropriate
- last observed date
- evidence references
- reliability observations
- preferred work type
- source
- previous outcomes

Talent Pool is not a list of everyone who applied.

## 28. STEP 23 — Source-to-outcome learning

Every candidate remains connected to:

Source → Campaign → Candidate → Qualification → Work → Outcome

Measure:
- applications/source
- eligibility rate
- screen rate
- assessment rate
- consistency completion
- verified talent rate
- hire/intern/project conversion
- successful outcome
- retention/re-engagement

Do not optimise for applicant volume alone.

## 29. STEP 24 — Communication automation

n8n standard events:
- application received
- missing information
- screen invitation
- screen reminder
- assessment invitation
- assessment reminder
- assessment received
- consistency task assigned
- task reminder
- training assigned
- work trial start
- status update
- talent pool confirmation
- re-engagement

Internal alerts:
- new candidate
- review required
- overdue assessment
- overdue reviewer action
- candidate exception
- source performance alert
- work-trial issue

Every automated communication should have Candidate ID, stage, action, deadline where relevant, and official contact route.

## 30. STEP 25 — Exception handling

Automation error → n8n error log → retry → human alert → manual completion → log resolution.

Common exceptions:

| Problem | Action |
|---|---|
| Duplicate candidate | merge/review, retain history |
| Missing CV | request upload |
| Invalid email | mark communication exception |
| Assessment late | reminder → human review |
| Reviewer late | manager alert |
| Drive access error | restricted-access repair |
| Form failure | manual intake backup |
| n8n failure | use manual SOP temporarily |
| AI extraction uncertain | human review |
| Payment/offer exception | Finance/HR review |

Never allow an automation failure to silently lose a candidate.

## 31. STEP 26 — Daily Talent Ops checklist

Every working day:
1. Check new applications.
2. Check duplicate queue.
3. Check eligibility exceptions.
4. Check screens due.
5. Check missed screens.
6. Check practical tasks due.
7. Check reviewer queue.
8. Check overdue candidate actions.
9. Check consistency tasks.
10. Check training/work-trial issues.
11. Check failed automations.
12. Check communication exceptions.
13. Update next-action dates.
14. Review urgent hiring requests.
15. Record unresolved exceptions.

## 32. Weekly Talent Ops review

Review:
- discovered
- applications
- eligible
- screened
- assessed
- consistency completed
- internships/work trials
- hires
- verified talent
- source performance
- false positives
- false negatives
- manual bottlenecks
- automation failures

Create change requests for Role Packs, sources, screens, assessments, consistency tasks, automation, communication and training.

## 33. Tool ownership matrix

| Tool | Owner | Backup | Critical failure response |
|---|---|---|---|
| Google Forms | Talent Ops | Admin | manual intake sheet |
| Google Sheets | Talent Ops | HR Ops | controlled backup/export |
| Google Drive | Admin/Talent Ops | IT | restricted-access repair |
| Gmail | Talent Ops | Admin | manual email |
| Calendar/Meet | Talent Ops | Manager | phone/manual scheduling |
| n8n | Automation Owner | Technical backup | manual SOP |
| AI | Automation/Research Owner | Human reviewer | manual extraction |
| GitHub | System Owner | Technical backup | local/versioned copy |
| Nivy Jobs | Talent Ops | Marketing | alternate source |
| Academy | Academy Owner | Mentor | manual training |

## 34. Minimum V1 implementation

Configure:
- Hiring Request Form
- Role Success Profile template
- Candidate Application Form
- Candidate Google Sheet
- Source Sheet
- Campaign Sheet
- Stage History Sheet
- Assessment Sheet
- Consistency Task Sheet
- Outcome Sheet
- restricted Drive structure
- Gmail templates/labels
- Calendar workflow
- n8n intake workflow
- duplicate detection
- Candidate ID generator
- screen scheduling
- assessment workflow
- reminders
- reviewer queue
- status communication
- error handling
- source-to-outcome dashboard
- human approval gates

## 35. V1 operating sequence — simple version

1. Hiring request
2. Select Role Pack
3. Select sources
4. Create Campaign ID
5. Publish/share application
6. Candidate submits Google Form
7. n8n creates/updates Candidate ID
8. CV goes to restricted Drive
9. Gmail acknowledgement
10. Eligibility check
11. Role routing
12. Schedule 15–20 min screen
13. Human screen
14. Send practical task
15. Candidate submits
16. Human reviews evidence
17. Training if needed
18. Three paid consistency tasks
19. Paid work trial/internship
20. Probation if employee
21. Core Staff / Verified Talent Pool / Project / Exit
22. Record outcome
23. Source quality updated
24. Improve next campaign

## 36. What must NOT happen

Do not:
- maintain candidate information across random personal spreadsheets
- store candidate PII in GitHub
- create multiple Candidate IDs for the same person
- judge capability from CV design
- judge reliability from interview confidence
- use certificates as proof of skill
- reject automatically because an AI summary looks weak
- let AI invent missing evidence
- run mass unsolicited outreach
- scrape prohibited/private data
- share CV folders publicly
- lose source/campaign attribution
- let candidates remain indefinitely without a next action
- run a practical task without clear instructions/deadline
- use unpaid productive work where payment/engagement terms are required
- call someone "verified talent" without actual evidence

## 37. Evidence standard

At every stage ask: What do we actually know?

E0 = No evidence  
E1 = Candidate/CV claim  
E2 = Structured screen  
E3 = Practical task  
E4 = Repeated paid tasks  
E5 = Controlled real work  
E6 = Internship/probation outcome

The objective is to move important hiring decisions toward E4–E6 evidence.

## 38. Final system principle

The Talent System is a learning loop:

SOURCE → DISCOVER → INTAKE → VERIFY → TEST → OBSERVE → DEVELOP → DEPLOY → MEASURE → LEARN

The system should become better at answering:
1. Where do good candidates come from?
2. Which signals actually predict useful work?
3. Which skills can be trained?
4. Which assessments predict real performance?
5. Which people become reliable contributors?
6. Which sources should receive more/less recruitment effort?
7. Which process step creates unnecessary manual work?

V1 should answer these questions with real candidate data before expanding automation or purchasing a complex ATS.
