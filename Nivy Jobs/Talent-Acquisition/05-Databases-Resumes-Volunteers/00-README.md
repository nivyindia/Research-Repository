# 05 — Databases / Resumes / Volunteers

**Policy:** PII gated. This folder holds **index and schema only**. No resume files, response sheets, or personal contact data are committed.

**Source roots:**
- Database folder: `10SuFDkIvHh2xSKsz4DQ6TblCB5Z0byT2`
- Resumes: `1RZFR8gpS-tsD710bnHWrCq-otzn3PPeQ`
- Volunteers Database: `1brUdAc3p588IvlYuhXm1aq2pFSSyIPps`

---

## Folder map (index only)

### Under Resumes (`1RZFR8gpS-tsD710bnHWrCq-otzn3PPeQ`)

| Subfolder / File | Type | Notes |
|------------------|------|-------|
| Accountant Resumes | Folder | Role-specific CVs |
| BDE Resumes | Folder | Role-specific CVs |
| CS | Folder | Company Secretary related |
| DM | Folder | Digital Marketing CVs |
| DM Internship | Folder | |
| DM Internship 2 | Folder | |
| HR Resumes | Folder | |
| Teaching | Folder | |
| DOC-20230312-WA0036_ | xlsx | Spreadsheet artifact |
| Internshala applications.xlsx | xlsx | Application log |
| Leader Hiring Portal (Responses).xlsx | xlsx | Form responses — **PII** |
| Offer Letter Excel Template.xlsx | xlsx | Template (non-candidate) |

### Under Volunteers Database (`1brUdAc3p588IvlYuhXm1aq2pFSSyIPps`)

| Subfolder | Type | Notes |
|-----------|------|-------|
| Excel contacts | Folder | Contact lists — **PII** |
| Interested Volunteers | Folder | |
| Linkedin Resumes | Folder | |
| Offer letters | Folder | See templates list below |
| Volunteer CV | Folder | |

### Offer letters folder (templates — 2021 era)

Reusable template filenames (no personal offer content committed):

- Content Design Offer Letter.docx
- Digital Mktng OFFER LETTER.docx
- Event Intern OFFER LETTER.docx
- HR OFFER LETTER.docx
- Public Relation Offer Letter.docx
- Sales and marketing.docx
- Dept wise work.docx
- Amrithalakshmi Promotion / Offer letter variants (named copies — treat as historical)

Canonical modern templates live under `01-VA-CA-Hiring-Funnel/` (VA Agreement + Offer Letter).

---

## Spreadsheet schemas (headers only — no row data)

### leads.xlsx (Drive root)

| Field | Notes |
|-------|-------|
| Owner/Founder | |
| Agency | |
| Website | |
| LinkedIn | |
| Email | **PII if populated** |

- Sheets: Sheet1
- Approx rows: ~51 (including header)
- Used as lead list structure for outreach / trial task style work

### CS_Data.xlsx

| Sheet | Headers (row 1) | Notes |
|-------|-----------------|-------|
| Sheet1 | Name, Phone, Working Anywhere, CA Firm Under u?, Exp | **Contains PII columns** — do not dump |
| Sheet2 | (empty/minimal) | |
| Sheet3 | (empty/minimal) | |

---

## What is NOT in this repo

- Individual PDF/JPG resumes
- Form response rows with names/emails/phones
- Full leads.xlsx or CS_Data.xlsx data rows

To use candidate data operationally, access originals on Google Drive under Nivy Careers account with proper access control.

---

## Related

- Hiring system: [../01-VA-CA-Hiring-Funnel/](../01-VA-CA-Hiring-Funnel/)
- Plan / Tracker: `docs/plans/talent-acquisition-migration/`

**Last updated:** 2026-09-27 (Phase 4 index-only)
