# Repository Inventory — Full Audit Snapshot

**Date:** 2026-10-18  
**Repo:** nivyindia/Research-Repository  
**Branch:** main

## 1. Top-level folders (live)

| Folder | Role for 4-brand migration |
|---|---|
| **Nivy Next/** | Primary source of brand assets (~882 .md files). Heavy duplicates. |
| **Nivy Crafts/** | Target brand folder — structure 00–12 created; 1 service file moved. |
| **Nivy Hype/** | Target brand folder — structure 00–12 created; 6 files moved. |
| **Nivy Ops/** | Target brand folder — structure 00–12 created; empty of content. |
| **Shared-Brand-Assets/** | Target shared root — structure created; empty of content. |
| **Brand-Portfolio-Migration/** | Control documents for this project. |
| **Notion - Nivy OS/** | Parallel Notion export — many duplicates of Nivy Next + SOPs + VA pricing. |
| **Nivy Research Data/** | Business-plan style docs; many vision/mission/company duplicates. |
| **Brand Systems/** | Policies, legal frameworks, Notion helper pages, large export zip. |
| Other (Academy, Advisory, Artisan, Global, Jobs, Nexus, Automation, Communities, etc.) | Outside 4-brand scope for now — leave in place. |

## 2. Nivy Next — content clusters (from search + prior full reads)

Approximate **882 markdown files**. Major clusters:

| Cluster | Examples | Brand mapping |
|---|---|---|
| Company identity (heavy duplicates) | Vision, Mission, Core Values, Brand Promise, Culture Code, About Us (3+ copies each) | **Shared** → `Shared-Brand-Assets/01_Company-Information/` (pick 1 canonical) |
| Website / profiles | Website Full Copy, Sales Deck, Brochure, Business Profile Execution Plan, Social Media Version, Directory Version | Mixed → keep source OR split later; website → Next `07_`; deck → Next `05_` or Shared |
| Services & pricing | SEO Packages, PPC, Social Ads, Social Mgmt Packages, Services & Offers index, Pricing Packages, Digital Marketing Services | **Mostly Hype** (SEO/PPC/Social moved); rest audit before move |
| Creative | Video Editing page (moved), Video Production Portfolio, Graphic/design refs | **Crafts** |
| Tech / web | Web Development Portfolio, AI/Automation mentions in decks | **Next** |
| VA / Ops | VA section inside VA Pricing Sheet only (mixed file) | **Ops** (split needed) |
| Portfolios | Web Dev Portfolio, Video Production Portfolio | **Inspiration only** — third-party / hypothetical; do not claim as Nivy clients |
| Internal OS | HR, Sales SOPs, Finance, CEO, INDEX, Recruitment, Onboarding | Company OS — **Shared** or leave in Nivy Next internal; not client-facing brand pages |
| SEO SOPs stubs | Multiple empty/template SEO SOPs | Hype or Next `11_` after content exists |
| Untitled / empty | Many Untitled.md | Low priority; archive later |

## 3. Notion - Nivy OS

- Same company identity pages as Nivy Next (duplicates).
- Service pages: Video Editing (moved), others.
- **DELIVERY SOPs:** SMM + Performance Marketing (moved to Hype).
- **VA Pricing Reference Sheet** — mixed (Advisory + Marketing + Dev + AI + VA).
- LinkedIn photo setup, growth engine docs — ops/sales enablement.

**Action:** Treat as secondary source. Prefer Nivy Next or already-moved Hype/Crafts paths as canonical where content matches.

## 4. Nivy Research Data

Business plan sections: Executive Summary, Company Description, Problem & Solution, Industry & Market Analysis, Financial Plan, Service Offerings, Service Delivery Model, Risk, Growth, etc.

Many near-empty stubs. Duplicates of vision/value props.

**Action:** Research/reference — map useful ones to `Shared-Brand-Assets/01_` or brand `12_Research-and-References/`. Do not treat as live client service pages.

## 5. Brand Systems

- Company policies, Customer Experience Policy
- Nivy Tech Data Protection & Privacy Framework
- IP & Content Ownership
- Global Systems / Final Systems indexes
- Large Notion export zip + UI tutorial pages (low value)

**Action:** Legal/policy → `Shared-Brand-Assets/02_Legal-and-Compliance/`. Skip Notion tutorial pages.

## 6. Already moved (canonical now under brand folders)

| Asset | Destination |
|---|---|
| SEO Packages & Pricing | Nivy Hype / pricing |
| PPC Advertising Service Page V3 | Nivy Hype / services |
| Global Social Media Management Packages | Nivy Hype / pricing |
| Social Media Advertising Service Page V3 | Nivy Hype / services |
| DELIVERY SOP-001 SMM | Nivy Hype / SOPs |
| DELIVERY SOP-003 Performance Marketing | Nivy Hype / SOPs |
| Video Editing Service Page | Nivy Crafts / services |

## 7. Folder structure status

- **00–12** created under all 4 brands + **Shared-Brand-Assets** 00–07.
- Hype still has older paths `02_Pricing-and-Packages` and `09_SOPs-and-Delivery` from early moves — align to `04_` and `11_` in next cleanup batch.

## 8. Scale note

Full file-by-file content audit of 882+ files is not complete. This inventory is **structure + cluster classification**. High-value client-facing assets have been content-audited; mass internal OS / empty stubs remain for later passes.
