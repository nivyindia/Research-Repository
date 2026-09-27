# Candidate Discovery & Qualification Engine — V1 Priority

## Objective
The most important Talent System capability is not collecting the largest number of applicants. It is creating a repeatable system that finds, identifies and verifies candidates who are likely to perform well in the actual job.

Core flow:
Reach → Discovery → Eligibility → Evidence → Qualification → Observation → Talent Pool

A CV or interview alone is not treated as proof of capability.

## 1. Right-candidate definition

For every role create a Role Success Profile before sourcing.

### Hard requirements
- legally/operationally eligible
- required working hours
- required language
- genuine technical prerequisites
- required device/internet/work environment
- location/time-zone requirements only where genuinely job-relevant

### Job capability
- role-specific knowledge
- practical skill
- tool proficiency
- required communication
- problem solving
- learning speed

### Reliability / working behaviour
Measure through evidence:
- follows instructions
- meets deadlines
- communicates blockers early
- completes work consistently
- accepts corrections
- documents work
- works with appropriate supervision

### Motivation / fit
Assess job-relevant factors:
- understands the work
- realistic availability
- compensation expectations
- interest in the role
- willingness to learn required skills
- commitment compatible with the role

### Evidence hierarchy
Prefer:
1. observed work
2. paid practical task
3. repeated small tasks
4. structured references/work history where appropriate
5. structured interview
6. CV/self-report

Lower stages generate leads; higher stages generate stronger evidence.

## 2. Candidate Discovery Funnel

TOTAL REACH
→ DISCOVERED CANDIDATES
→ BASIC ELIGIBILITY
→ ROLE FIT
→ SCREEN
→ PRACTICAL TEST
→ 3-TASK CONSISTENCY
→ TRAIN / REMEDIATE
→ PAID INTERNSHIP / WORK TRIAL
→ VERIFIED TALENT

The objective is not to reject people early using weak proxies. Move uncertain candidates toward inexpensive, job-relevant evidence.

## 3. Source-to-quality model

Every candidate gets:
- source channel
- source organisation/partner
- campaign
- city/market
- referral
- community
- acquisition date

Measure sources by downstream evidence:
- application rate
- eligibility rate
- screen completion
- assessment completion
- assessment quality
- 3-task consistency
- internship completion
- probation outcome
- retention/re-engagement

High applicant volume does not automatically mean high source quality.

## 4. Candidate evidence model

| Signal | Evidence | Stage |
|---|---|---|
| Eligibility | application | Intake |
| Skill | practical test | Assessment |
| Reliability | deadlines + communication | Screen/Tasks |
| Instruction following | observed work | Tasks |
| Learning | correction → next attempt | Tasks/Training |
| Communication | structured interactions | Screen/Tasks |
| Ownership | response to blockers/errors | Tasks |
| Consistency | repeated tasks | 3-task stage |
| Role fit | job-specific evidence | All |
| Availability | declared + observed | Intake/Work trial |

AI may summarise evidence, identify missing evidence and recommend the next evidence-gathering step. It should not convert weak proxies into a definitive hiring decision.

## 5. V1 Role Success Profiles

Start with:
- Computer/Data Operator
- Accounting
- Digital Marketing
- AI/Automation
- BDE/Sales

Each role needs:
1. Must-have requirements
2. Trainable requirements
3. Operational constraints
4. 5–7 job competencies
5. 3 observable reliability behaviours
6. Practical test
7. Three consistency tasks
8. Interview questions
9. Evidence rubric
10. Minimum evidence required before advancement

## 6. V1 Qualification Gates

Gate 1 — Intake:
required fields, availability, role interest, prerequisites, source attribution, duplicate check.

Gate 2 — Structured screening:
15–20 minutes covering role understanding, past work evidence, availability, expectations, learning behaviour, mistakes and deadlines.

Gate 3 — Practical evidence:
short paid role-specific assessment.

Gate 4 — Consistency:
three small paid tasks over time.

Gate 5 — Work trial:
controlled real work where appropriate.

Gate 6 — Talent Pool:
evidence-backed profiles are promoted to verified talent status.

## 7. Discovery methods

### Pull
Nivy Jobs, Nivy Academy, forms, job boards, social/community channels and institute partners.

### Push
Permitted research of relevant public sources, professional profiles, portfolios and candidate communities.

### Network
Employee referrals, alumni, institute placement cells, trainers, campus ambassadors, community administrators and partner referrals.

### Reactivation
Historical candidates may be re-contacted only after identity matching and appropriate contact/consent checks.

## 8. Candidate Research Agent

Input:
Role Success Profile + target geography + experience level + approved sourcing channels.

The agent can:
- identify relevant public sources
- collect permitted public organisation/source information
- classify source relevance
- extract structured information where permitted
- deduplicate
- map evidence to role requirements
- identify missing information
- create research queues
- draft outreach

Human controls:
- source approval
- sensitive-data handling
- outreach approval where required
- consequential candidate progression

## 9. V1 automation

Source / Form / Referral
→ n8n
→ Identity + duplicate check
→ Basic eligibility
→ Role routing
→ Screen invitation
→ Assessment
→ Evidence capture
→ 3-task consistency
→ Human review
→ Talent Pool

Use existing n8n and Multi-Agent AIOS research before creating new architecture.

## 10. Anti-failure rules

- Do not rank candidates primarily by CV polish.
- Do not use college, city, age, gender, caste, religion or similar sensitive/protected characteristics as proxies for capability.
- Do not equate certificates with practical skill.
- Do not equate interview confidence with reliability.
- Do not use undefined subjective “culture fit”.
- Do not use one test to establish reliability.
- Do not let AI make irreversible hiring decisions.
- Do not treat applicant volume as source quality.
- Do not collect private contact data without an appropriate basis.
- Do not put candidate PII in GitHub.

## 11. V1 success metrics

Discovery: qualified candidates per role, source-to-qualified rate, cost/time per qualified candidate.

Qualification: screen completion, assessment completion, assessment quality, 3-task consistency.

Operations: recruiter hours per qualified candidate, automation rate, duplicate rate, candidate response time.

Downstream: internship completion, probation outcome, time to productivity, retention/re-engagement.

The system improves when downstream outcomes show which discovery sources and qualification signals actually predict successful work.
