# Phased Migration Plan

## Objective
Audit and organize existing material in `nivyindia/Research-Repository` into Nivy Next, Nivy Crafts, Nivy Hype, Nivy Ops, and a shared-assets area. Cover the full business asset lifecycle—not only website/SEO content.

## Scope of audit
1. Brand guidelines: logos, colours, fonts, visual identity, voice, taglines and brand messaging.
2. Company profiles: introductions, capability statements, About pages and business descriptions.
3. Services: service descriptions, deliverables, scope boundaries, catalogs and one-pagers.
4. Pricing: rate cards, packages, proposals, quotations, internal costing, historical pricing and approval status.
5. Sales: decks, pitches, discovery-call scripts, objections, follow-ups, outreach templates and sales playbooks.
6. Proposals and partnerships: client proposals, partnership proposals and pitch materials.
7. Portfolio and proof: work samples, case studies, testimonials, metrics and evidence.
8. Website: site maps, page plans, service pages, landing pages, FAQs, conversion plans and drafts.
9. SEO/GEO/AEO: keyword research, intent maps, content briefs, technical/on-page SEO, off-page SEO, GEO/AEO and competitor research.
10. Online presence: social profiles, business profiles, directory listings, profile descriptions and platform-specific assets.
11. Marketing: content calendars, social posts, campaigns, email marketing, ads and creative briefs.
12. Operations and delivery: SOPs, onboarding, quality control, delivery workflows, reusable templates and client handover.
13. Research and tools: market research, competitor research, external solutions, training materials and reference databases.

## Phase 0 — Establish control documents
**Goal:** Create the plan, tracker, inventory method, mapping rules and safety rules.
**Deliverables:** This plan and the related control files.
**Exit criteria:** All control documents exist and have a clear owner/status.
**Status:** In progress (control documents being established).

## Phase 1 — Repository inventory
**Goal:** Identify candidate files and folders throughout the repository, not just files whose names contain a brand name.
**Actions:**
- Search each asset category and each brand name.
- Record exact path, filename/title, file type, URL and search source.
- Include files under `Nivy Next/`, `Notion - Nivy OS/`, `Nivy Research Data/`, `Nivy Nexus/`, `Chats/Claude/`, `Chats/ChatGPT/`, and `External Solutions/` where relevant.
- Distinguish confirmed files from search leads and inaccessible/unclear items.
**Deliverable:** Master inventory with source path and evidence.
**Exit criteria:** Search coverage and known limitations are documented; no claim of completeness without evidence.
**Status:** Not started.

## Phase 2 — Content and version audit
**Goal:** Determine what each candidate actually contains and whether it is final, draft, obsolete, duplicate, shared or uncertain.
**Actions:**
- Read the actual document; filename alone is insufficient.
- Compare similar versions and exports.
- Identify pricing approval/effective date and flag contradictions.
- Identify mixed-brand documents and whether they need splitting.
- Record canonical candidate and confidence/reason.
**Deliverable:** Audited inventory and duplicate/version decisions.
**Exit criteria:** Each in-scope item has a proposed classification or an explicit Review Required status.
**Status:** Not started.

## Phase 3 — Brand mapping and target design
**Goal:** Assign each asset to the correct brand or shared area.
**Actions:**
- Map each asset to Nivy Next, Nivy Crafts, Nivy Hype, Nivy Ops, Shared Brand Assets, External Reference, Archive Candidate or Review Required.
- Define destination paths and cross-brand dependencies.
- Identify missing assets without creating them prematurely.
**Deliverable:** Approved source-to-destination migration register and final folder structure.
**Exit criteria:** Every proposed move has a rationale; ambiguous items are held for review.
**Status:** Not started.

## Phase 4 — Approval gate
**Goal:** Confirm the mapping before modifying existing material.
**Actions:**
- Present source path, proposed destination, action, reason, version status and risk.
- Ask for approval of the batch or explicitly agreed scope.
- Do not move, delete, rename or overwrite existing source documents before approval.
**Deliverable:** Approved migration batch/register.
**Exit criteria:** Approval is recorded.
**Status:** Not started.

## Phase 5 — Controlled migration
**Goal:** Move or reorganize only approved items.
**Actions:**
- Preserve source history and provenance where possible.
- Prefer Git moves/renames or new commits; do not silently replace source content.
- For mixed-brand documents, retain the original and create brand-specific derivatives only when justified.
- For shared assets, keep one canonical copy and link/reference it from brand documents where practical.
- Update links and the migration register after each batch.
**Deliverable:** Migrated files and commit references.
**Exit criteria:** Each migrated item has a destination, action result and commit/reference.
**Status:** Not started.

## Phase 6 — Verification and closeout
**Goal:** Ensure the migration is complete and usable.
**Actions:**
- Check that every approved source item exists at its intended destination.
- Check links, duplicates, names, content integrity and cross-brand boundaries.
- Record unresolved items and exceptions.
- Produce a final audit summary and list remaining gaps.
**Deliverable:** Verification report and closeout tracker.
**Exit criteria:** All approved items verified or marked as an exception with a reason.
**Status:** Not started.

## Phase 7 — Separate online-presence and international SEO implementation plan
**Goal:** After asset organization, plan how each brand will target international markets.
**Actions:** Map high-intent keywords to search intent and funnel stage; plan website pages, social profiles, business listings, directory listings, off-page SEO, content and conversion assets by brand.
**Dependency:** Start only after the content inventory and brand/service boundaries are sufficiently reliable.
**Deliverable:** Separate four-brand online-presence implementation plan.
**Status:** Deferred until migration audit provides reliable source material.

## Dependencies and gates
- Phase 2 depends on Phase 1.
- Phase 3 depends on Phase 2.
- Phase 4 approval is required before Phase 5.
- Phase 6 follows each migration batch.
- Phase 7 depends on a reliable service/catalog/brand asset baseline.

## Definition of done
- All relevant assets have been inventoried or recorded as an explicit search gap.
- Every asset has a documented classification and action.
- Approved files are migrated and verified.
- Shared assets have a canonical source.
- Pricing and brand claims have version/approval status.
- No source was deleted or overwritten without explicit approval.
- A separate international online-presence plan can be built from verified service and brand information.
