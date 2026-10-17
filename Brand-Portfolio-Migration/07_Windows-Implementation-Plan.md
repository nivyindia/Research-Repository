# Windows Implementation Plan — Audit, Duplicates, Rename & Move Map

**Date:** 2026-10-18  
**Mode:** PLAN ONLY — do **not** move on GitHub until you run this locally  
**How you will run:** Pull repo → run Batch/Python script on Windows → push

---

## 1. Goal

1. Audit source files (done at cluster level; expand as you implement).  
2. Detect duplicates (same title / same SHA patterns).  
3. Rename to clean ASCII names.  
4. Move into logical brand folders (00–12 + Shared).  
5. Leave pointers or keep sources until verified.

---

## 2. Target folders (already created on GitHub)

```
Shared-Brand-Assets/00_…07_
Nivy Next/00_…12_
Nivy Crafts/00_…12_
Nivy Hype/00_…12_
Nivy Ops/00_…12_
```

**Brand rules**

| Brand | Owns |
|-------|------|
| Nivy Next | Tech, web, apps, AI |
| Nivy Crafts | Design, video, motion |
| Nivy Hype | Social, PPC, paid ads, performance marketing |
| Nivy Ops | VA, admin, CRM, lead research ops |
| Shared | Company master identity, legal, common templates |

---

## 3. Source areas to process (priority order)

| Priority | Source folder | Notes |
|----------|---------------|--------|
| P0 | `Nivy Next/` | ~882 .md — main work |
| P1 | `Notion - Nivy OS/` | Many duplicates of Next + SOPs + VA sheet |
| P2 | `Brand Systems/` | Legal/policies → Shared |
| P3 | `Nivy Research Data/` | Business plan / research |
| Skip now | Academy, Advisory, Artisan, Global, Jobs, Nexus, Automation, Communities, GAOS, International-DM, Company OS, Chats | Out of 4-brand scope |

---

## 4. Already on target (do not re-move blindly)

These already exist under brand folders (from earlier sessions). Script should **skip if destination exists** or only align paths:

| Current location | Status |
|------------------|--------|
| `Nivy Hype/03_Services-and-Catalog/PPC-Advertising-Service-Page-V3.md` | OK |
| `Nivy Hype/03_Services-and-Catalog/Social-Media-Advertising-Service-Page-V3.md` | OK |
| `Nivy Hype/04_Pricing-and-Packages/SEO-Packages-and-Pricing.md` | OK (canonical) |
| `Nivy Hype/04_Pricing-and-Packages/Global-Social-Media-Management-Packages.md` | OK |
| `Nivy Hype/11_Operations-and-Delivery/DELIVERY-SOP-001-…` | OK |
| `Nivy Hype/11_Operations-and-Delivery/DELIVERY-SOP-003-…` | OK |
| `Nivy Crafts/03_Services-and-Catalog/Video-Editing-Service-Page.md` | OK |
| `Shared-Brand-Assets/02_Legal-and-Compliance/*` | OK (Batch 1) |
| `Shared-Brand-Assets/01_Company-Information/00_Canonical-…` | Placeholder only |
| Old Hype `02_Pricing` / `09_SOPs` | Pointers only — optional delete after local verify |

---

## 5. Duplicate groups (rename/move rule: keep ONE canonical)

Compare **content hash** on Windows before deleting. Same title ≠ same content always.

### 5.1 Company identity (many copies in Nivy Next + Notion OS)

| Logical name | Action |
|--------------|--------|
| Company Vision Statement | Keep 1 → `Shared-Brand-Assets/01_Company-Information/Company-Vision-Statement.md` |
| Mission Statement | Keep 1 → same folder `Mission-Statement.md` |
| Core Values & Beliefs | Keep 1 → `Core-Values-and-Beliefs.md` |
| Brand Promise & Philosophy | Keep 1 → `Brand-Promise-and-Philosophy.md` |
| Culture Code | Keep 1 → `Culture-Code-and-Guiding-Principles.md` |
| About Us | Keep 1 → Shared or Next `02_Company-Profile/` |

Extra copies: rename to `*_DUPLICATE.md` in an `_Archive-Duplicates/` folder under source, **or** leave in place until hash match confirmed.

### 5.2 Indexes repeated

HR, Sales, Finance, CEO pages appear multiple times under Nivy Next — treat as **internal OS**, default **do not move** into client brand catalog; optional later → Shared or keep in Next root archive.

### 5.3 Service pages already moved

Original Notion/Next paths may still hold **MOVED** pointer files — do not treat as second copy of content.

---

## 6. MOVE MAP (for your Batch/Python script)

Format for script CSV columns:  
`action,source_relative_path,dest_relative_path,new_filename,brand,notes`

### 6.1 Hype (if still only under Nivy Next / Notion — verify before move)

| action | source (pattern) | dest | new_filename |
|--------|------------------|------|----------------|
| move | `Nivy Next/*SEO Packages*` (if still full content, not pointer) | `Nivy Hype/04_Pricing-and-Packages/` | `SEO-Packages-and-Pricing.md` |
| move | `Nivy Next/*PPC Advertising*Service*` | `Nivy Hype/03_Services-and-Catalog/` | `PPC-Advertising-Service-Page-V3.md` |
| move | `Nivy Next/*Social Media Advertising*Service*` | `Nivy Hype/03_Services-and-Catalog/` | `Social-Media-Advertising-Service-Page-V3.md` |
| move | `Nivy Next/*Global Social Media Management Packages*` | `Nivy Hype/04_Pricing-and-Packages/` | `Global-Social-Media-Management-Packages.md` |
| move | `Notion - Nivy OS/*DELIVERY SOP-001*SMM*` | `Nivy Hype/11_Operations-and-Delivery/` | `DELIVERY-SOP-001-Social-Media-Management.md` |
| move | `Notion - Nivy OS/*DELIVERY SOP-003*Performance*` | `Nivy Hype/11_Operations-and-Delivery/` | `DELIVERY-SOP-003-Performance-Marketing-Ads.md` |
| skip | if dest already has non-pointer content | — | skip |

### 6.2 Crafts

| action | source | dest | new_filename |
|--------|--------|------|----------------|
| move | `Notion - Nivy OS/*Video Editing*Service*` (if not pointer) | `Nivy Crafts/03_Services-and-Catalog/` | `Video-Editing-Service-Page.md` |
| copy+label | `Nivy Next/*Video Production Portfolio*` | `Nivy Crafts/06_Portfolio-and-Proof/` | `Video-Production-Portfolio-REFERENCE-ONLY.md` |

### 6.3 Next

| action | source | dest | new_filename |
|--------|--------|------|----------------|
| move | `Nivy Next/*Website Version*Full Copy*` | `Nivy Next/07_Website-and-Landing-Pages/` | `Website-Full-Copy.md` |
| move | `Nivy Next/*Sales Deck*PPT*` | `Nivy Next/05_Sales-and-Business-Development/` | `Sales-Deck-PPT-Version.md` |
| move | `Nivy Next/*Business Profile Execution Plan*` | `Nivy Next/00_Project-Management/` | `Business-Profile-Execution-Plan.md` |
| copy+label | `Nivy Next/*Web Development Portfolio*` | `Nivy Next/06_Portfolio-and-Proof/` | `Web-Development-Portfolio-REFERENCE-ONLY.md` |
| move | Branding / Visual Identity pages | `Nivy Next/01_Brand-Identity/` | clean names |
| move | Services One-Pager, Detailed Services (after audit) | `Nivy Next/03_Services-and-Catalog/` | clean names |

### 6.4 Ops

| action | source | dest | new_filename |
|--------|--------|------|----------------|
| extract | `Notion - Nivy OS/*VA Reference Sheet*` | **Do not move whole file** | Split VA section only → `Nivy Ops/04_Pricing-and-Packages/VA-Services-Pricing.md` (manual or Python section extract) |

### 6.5 Shared

| action | source | dest | new_filename |
|--------|--------|------|----------------|
| move | `Brand Systems/*Data Protection*Privacy*` | `Shared-Brand-Assets/02_Legal-and-Compliance/` | `Nivy-Tech-Data-Protection-Privacy-Framework.md` |
| move | `Brand Systems/*Intellectual Property*Ownership*` | `Shared-Brand-Assets/02_Legal-and-Compliance/` | `Nivy-Tech-IP-Content-Ownership-Policy.md` |
| move | `Brand Systems/*Customer Experience Polic*` | `Shared-Brand-Assets/02_Legal-and-Compliance/` | `Customer-Experience-Policy.md` |
| move | `Brand Systems/Company policies*` | `Shared-Brand-Assets/02_Legal-and-Compliance/` | `Company-Policies.md` |
| skip | Brand Systems “Click me to…” tutorial pages | — | ignore |

### 6.6 Do NOT move

- `Services & Offers` **index** until children mapped (breaks links).  
- Mass HR / Finance / CEO / Untitled stubs.  
- Out-of-scope brand folders.  
- Portfolios as “client proof” without rewrite.  
- Mixed VA Pricing whole file without split.

---

## 7. Rename rules (apply on move)

1. Strip Notion UUID suffix: ` Name abc123….md` → `Name.md`  
2. Replace spaces with `-`  
3. Remove emoji from **filenames** (keep in H1 if needed)  
4. ASCII only for Windows safety  
5. Max path length: keep dest path under ~200 chars  

Example:  
`🔍 SEO Packages & Pricing 2f434207fb4d81fb8f0cd3a0161a1f56.md`  
→ `SEO-Packages-and-Pricing.md`

---

## 8. Suggested Windows workflow

1. `git pull`  
2. Dry-run Python: list matches for each pattern, print source→dest  
3. Hash check duplicates (same size + hash → mark DUPLICATE)  
4. Execute moves with `shutil.move` or `robocopy` / `move`  
5. Write `MOVED.md` pointer at old path (optional)  
6. `git add -A` → commit → push  
7. Spot-check links in Services & Offers index

### Minimal Python sketch (you implement)

```python
# dry_run=True first
MOVES = [
  # (glob_or_exact_src, dest_dir, new_name),
  (r"Nivy Next\\*SEO Packages*", r"Nivy Hype\\04_Pricing-and-Packages", "SEO-Packages-and-Pricing.md"),
  # ... fill from section 6
]
```

---

## 9. Audit status honesty

| Scope | Status |
|-------|--------|
| Folder structure | Complete |
| High-value service/pricing/SOP/portfolio **content** audit | Done for key files |
| Full 882-file line-by-line content audit | **Not complete** — cluster + pattern based |
| Duplicate groups (identity) | Identified by title pattern; confirm by hash on Windows |
| This plan | Ready for local script implementation |

---

## 10. Safety (must follow on Windows)

- Dry-run before real move  
- Never delete until dest verified  
- Skip if destination already has real content  
- REFERENCE-ONLY flag on third-party portfolios  
- No pricing edits during move  
- Log every row: timestamp, src, dest, ok/fail  

---

## 11. Next after you implement Batch on Windows

1. Fill Shared Vision/Mission from approved copy  
2. VA sheet split → Ops  
3. Services & Offers children one-by-one  
4. Verification pass + broken link fix  

**End of plan — no files were moved in this commit except this document.**
