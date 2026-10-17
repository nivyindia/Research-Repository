# Repository Inventory and Audit Method

## Search locations
Search the whole repository, not only the four brand folders. Known relevant areas include:
- `Nivy Next/`
- `Nivy Crafts/`
- `Nivy Hype/`
- `Nivy Ops/`
- `Notion - Nivy OS/`
- `Nivy Research Data/`
- `Nivy Nexus/`
- `Chats/Claude/`
- `Chats/ChatGPT/`
- `External Solutions/`
- Other root-level folders and exports found during discovery.

## Search by both brand and asset category
Search terms should include names and variants such as:
- Brand identity, brand guideline, visual identity, logo, palette, typography, voice, tagline
- Pricing, rate card, price list, package, retainer, quotation, estimate, costing
- Services, service catalog, brochure, one-pager, capability statement
- Sales deck, pitch, proposal, outreach, discovery call, objection, follow-up
- Portfolio, case study, testimonial, proof, work sample, results
- Website, landing page, service page, sitemap, FAQ, conversion
- SEO, keyword, search intent, GEO, AEO, competitor, backlink, directory
- Social media, business profile, listing, company profile
- Marketing, campaign, ads, PPC, content calendar, email sequence
- Virtual assistant, operations, remote support, CRM, SOP, onboarding, delivery

## Required inventory fields
Each verified inventory row should contain:
- Unique asset ID
- Exact title and repository path
- File type and link
- Current location/owner area
- Primary brand (or Shared / External Reference / Review Required)
- Secondary brand(s), if applicable
- Asset category
- Actual content summary
- Version/date and approval status, if present
- Duplicate/version candidates
- Sensitive/internal/public-facing classification
- Proposed action: Keep, Move, Split, Link/Reference, Archive Candidate, or Review Required
- Proposed destination
- Rationale and confidence
- Audit status and auditor/date
- Approval status
- Migration commit and verification status, once applicable

## Classification rules
- **Brand-specific:** clearly belongs to one service brand.
- **Shared:** common company-level information or reusable cross-brand assets.
- **Mixed-brand:** contains substantial content for multiple brands; preserve original and propose split/derivatives.
- **External reference:** research or third-party framework; normally stays in research/reference location and is linked from the brand asset register.
- **Duplicate candidate:** similar title/content only; compare full text before declaring duplicate.
- **Archive candidate:** outdated or superseded, but retain until approved for archive.
- **Review required:** unclear ownership, unsupported claim, pricing conflict, or ambiguous version.

## Version and pricing checks
- Do not infer that a file is final from words such as “final” or “master” in the filename.
- Compare content, timestamps/metadata where available, approval notes, links and scope.
- Label prices as approved, draft, proposal-specific, internal-only, historical or unknown.
- Flag contradictions rather than choosing a price without evidence.
- Do not publish internal costing or client-sensitive material as public-facing content.

## Audit output
Produce:
1. Full inventory.
2. Duplicate/version comparison register.
3. Mixed-brand content register.
4. Pricing/claims review register.
5. Proposed source-to-destination migration register.
6. Search coverage and limitations report.
