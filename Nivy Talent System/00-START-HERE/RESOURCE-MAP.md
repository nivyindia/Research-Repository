# Repository-Wide Talent Resource Map

**Scan scope:** repository tree (11,654 paths) + targeted content searches for Jobs, Careers, Academy, HR, recruitment, hiring, applicant, resume/CV, internship, training, placement, assessment, probation, talent, freelancer and automation.

## Decision: where should Nivy Jobs and Nivy Academy live?

### Nivy Talent System = shared operating engine
Keep the **Talent System** as the internal engine that powers the whole talent lifecycle.

### Nivy Jobs = business-facing talent/opportunity product
Nivy Jobs should use the Talent System for:
- talent registration
- job/internship applications
- screening
- assessment
- verification
- talent pool
- matching
- employer hiring
- freelance/project opportunities
- placement operations

### Nivy Academy = training/development product
Nivy Academy should use the Talent System for:
- learner intake
- skills profile
- assessment
- learning gaps
- practical assignments
- certification evidence
- internship/apprenticeship
- alumni/talent pool
- placement/job matching

### Shared architecture

```
                    NIVY TALENT SYSTEM
                  (Shared Talent Engine)
                           |
          +----------------+----------------+
          |                                 |
      NIVY ACADEMY                      NIVY JOBS
   Learn / Assess / Train          Jobs / Match / Place
          |                                 |
          +---------------+-----------------+
                          |
                    TALENT POOL
                          |
              +-----------+-----------+
              |                       |
        Nivy Internal Work      External Employers
```

**Do not create separate candidate databases for Academy and Jobs.** Use one canonical candidate/talent identity and multiple programme/application records.

## High-value resources already found

| Existing resource | Current location | Use |
|---|---|---|
| Talent Recruitment Plan 1.0 | `Nivy Jobs/` | Source map, categories, talent database, employer side, community, verification, revenue model |
| Talent Recruitment Plan duplicate | `Notion - Nivy Jobs/` | Compare with Nivy Jobs original; retain provenance |
| Nivy Careers Complete Business Plan | `Nivy Nexus/` + Notion copy | Recruitment business model, ATS/tools, employer markets, execution |
| Nivy Careers recruiter profile | `Nivy Nexus/` | Recruiter role and sourcing capability |
| Nivy Academy Jobs Integration Plan | `Nivy Academy/` | Academy → talent pool → jobs integration |
| Academy Course Improvement Plan | `Nivy Academy/` | Certification, employer portal, placement/internship opportunities |
| Fresher intake process | `Nivy Talent System/03-CANDIDATE-ACQUISITION/` | Existing intake/screen/assessment workflow |
| Evaluation Sheet - Nivy.xlsx | `Chats/Claude/` | Existing scoring/evaluation asset; inspect and normalize |
| Nivy Academy.zip | `Chats/Claude/` | Potential source archive; inspect before migration |
| Nivy Jobs.zip | `Chats/Claude/` | Potential source archive; inspect before migration |
| Notion - Nivy Jobs.zip | `Chats/Claude/` | Potential source archive; inspect before migration |
| Company OS HR v7 | `Chats/Claude/Company OS/Company-OS-v7/.../HR/` | HR folder architecture, SOPs, templates, records, reports, work instructions |
| Multi-Agent AIOS | `Chats/ChatGPT/Multi Agent AIOS/` | Agent schemas and n8n/event architecture reusable for automation |
| Growth Engine n8n workflows | `Chats/Claude/growth-engine-automation*/` | Lead intake, CRM sync, outreach, booking, proposal, onboarding, reporting patterns |
| Sales funnel workflows | `Chats/Claude/sales-funnel-*/` | Capture → clean → enrich → score → CRM → engage → close |
| Company Culture / Employee Motivation | `Chats/Claude/` | Role cards, employee practices and retention ideas |
| Business Platforms Overview | `Chats/Claude/` | Existing marketplace/staffing/recruitment models |
| Institute Partnership Growth Model | `Notion - Global Systems Workpace/` | Institute pipeline and recruitment-pool model |
| GAAP 30-Day Launch Plan | `Notion - Nivy OS/` + Nivy Research Data copy | Student/campus partner acquisition model |
| Data Scraping Methods / legal map | `Nivy Research Data/` | Candidate-source constraints and consent-oriented sourcing research |
| CSV exports / People | Multiple workspace/export folders | Potential historical records; must be classified before ingestion |
| Nivy_ChatGPT_Index.csv | `Chats/Claude/` | Discovery/indexing aid for historical conversations |

## Important existing design overlap

There are already several generations of HR/Company OS folders and duplicate Notion/ChatGPT/Claude exports. **Do not merge them blindly.**

Use:
1. Source registry
2. Deduplication
3. Version comparison
4. Evidence/quality review
5. Canonicalization
6. Archive old versions with provenance

## Historical candidate data

The repository tree contains CSV exports and an existing `Evaluation Sheet - Nivy.xlsx`. The user also has historical applicant data in email inboxes and Excel files.

These should become a **separate operational data-ingestion project**, not GitHub documentation.

Target ingestion flow:

```
Gmail / Excel / CSV / old forms / resumes
        ↓
Secure staging
        ↓
PII inventory + duplicate detection
        ↓
Candidate identity resolution
        ↓
Consent/contact-preference status
        ↓
Profile extraction
        ↓
Canonical Candidate ID
        ↓
ATS/CRM/database
        ↓
Talent System lifecycle
```

Never commit raw resumes, phone lists or candidate PII to GitHub.

## Resource use principle

Do not ask "which old file should we use?" in isolation.

Ask:
**Which existing resource already solves this process, what is missing, and what should be reused/adapted/integrated?**

That is the governing rule for the next phases.