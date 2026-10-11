# Growth Engine Marketing Workflow — Exact-File Static Audit, Wave 22
**Date:** 2026-10-11  
**Roadmap:** Continue the main roadmap; no route change.  
**Method:** REUSE → MAP → VERIFY → INTEGRATE → TEST → BUILD ONLY WHAT IS MISSING.  
**Scope:** Five Phase-1 n8n workflow JSON files in the canonical `growth-engine-automation-phase1-2` copy. Static parse/structure review only; no n8n import, credential check, endpoint call, or live execution performed.

## 1. Executive result
The repository does contain concrete workflow JSON for Modules 1.1–1.5; this is more than planning documents. All five fetched files parsed as JSON successfully and expose 53 nodes / 41 connection-map entries in total. However, each export declares `active: false`; this audit does **not** establish that they import cleanly into the target n8n instance, have working credentials, connect to the live services, or pass runtime tests.

The evidence also resolves the apparent Track M conflict:
- **Partly present:** 1.1 creates social-platform posts from published Odoo blog posts; 1.2 performs weekly SEO checks/updates; 1.3 accepts Typebot inbound leads and writes to Odoo plus `clients_master`; 1.4 qualifies inbound leads; 1.5 syncs CRM stage changes.
- **Still unproven/missing:** a universal bridge from all Track M sources (social DMs/comments, community sign-ups, partner/referral touchpoints, CTA events) into the same deduplicated inbound contract; a live growth-experiment tracker; and M2–M6 automation coverage end-to-end. Do not claim the entire Track M is built or wholly absent.

## 2. Exact-file inventory
| Module | Canonical repository path | Blob SHA | Static result |
|---|---|---|---|
| 1.1 Content → Social Factory | `Chats/Claude/growth-engine-automation-phase1-2/growth-engine-automation/phase-1/1.1-content-social-factory/workflow.json` | `aa879bfddaf185d750439ede01096f07e192d43b` | JSON parses; 9 nodes; scheduled trigger; writes to Mixpost endpoints; workflow inactive in export |
| 1.2 SEO Automation | `Chats/Claude/growth-engine-automation-phase1-2/growth-engine-automation/phase-1/1.2-seo-automation/workflow.json` | `898a66ef45e866fa8396ab013a4a6ff493e0f761` | JSON parses; 15 nodes; scheduled trigger; GSC/Ollama/DB/email nodes; workflow inactive in export |
| 1.3 Website Lead Capture | `Chats/Claude/growth-engine-automation-phase1-2/growth-engine-automation/phase-1/1.3-website-lead-capture/workflow.json` | `a1b09f0f4aa1877306b530c4783ac405f983540c` | JSON parses; 7 nodes; POST webhook `typebot-lead-capture`; Odoo lead + `clients_master` write; workflow inactive in export |
| 1.4 Inbound Form Qualification | `Chats/Claude/growth-engine-automation-phase1-2/growth-engine-automation/phase-1/1.4-inbound-form-qualification/workflow.json` | `40712e138f344cda983b6f5913819f031a657e2e` | JSON parses; 12 nodes; POST webhook `lead-qualification`; qualification, DB update and notifications; workflow inactive in export |
| 1.5 Central CRM Sync | `Chats/Claude/growth-engine-automation-phase1-2/growth-engine-automation/phase-1/1.5-central-crm-sync/workflow.json` | `65ad5b4df98a7a06c0c86bf2171568e6dc1b0e38` | JSON parses; 10 nodes; scheduled CRM-stage sync; routes qualified/won/proposal states; workflow inactive in export |

Aggregate: 53 nodes; 41 connection-map entries; all five exports set `active: false`. Node and connection counts are static facts only, not a quality score.

## 3. High-priority findings before live use
### WF-SEC-01 — Public webhook authentication is not demonstrated (P0)
1.3 and 1.4 contain webhook nodes. In the inspected node list, there is no explicit HMAC/signature or signed-token verification node before the business actions. The master tracker itself requires public webhooks to validate HMAC/signature or signed tokens. Confirm whether authentication is enforced by a trusted upstream gateway; otherwise add verification, replay protection, timestamp/nonce rules where appropriate, rate limits and negative tests before activation.

### WF-CONTENT-02 — AI-generated social content appears to publish without human approval (P0/P1 gate)
1.1 includes Ollama rewriting followed by Mixpost posting to LinkedIn, X, Instagram and Facebook, with no visible approval node in this workflow. This conflicts with the AI Marketing Automation Stack's rule that strategy/content decisions remain human-reviewed. Add an approval queue (draft → reviewer → publish), or document an explicit low-risk allowlist and policy exception. Test rejection, edit, duplicate and retry cases.

### WF-SEO-03 — AI-generated meta descriptions are written directly to the website database (P1)
1.2 includes an `UPDATE website_page` step after Ollama generates descriptions. Before live execution, add a preview/diff, length/content checks, human approval or a tightly bounded safe auto-update policy, backup/rollback and audit log. Test missing pages, malformed output, SQL-expression edge cases, idempotency and rollback. Do not infer that this update is live merely because the node exists.

### WF-INGEST-04 — Existing inbound bridge is narrower than Track M's full scope (P1)
1.3 handles a Typebot webhook and writes the lead to Odoo and `clients_master`; 1.4 qualifies inbound leads; 1.5 syncs CRM stage changes. This covers a useful subset of the proposed M-W5 bridge. Static review does not establish ingestion for social DMs/comments, community sign-ups, partner/referral forms, blog CTA events or all inbound sources. Define a shared source/channel/consent/dedup contract and map each source to the existing capture workflow rather than creating a duplicate CRM pipeline.

### WF-DATA-05 — CRM lifecycle and attribution fields need reconciliation (P1)
1.3 inserts `source` and status values into `clients_master`; 1.4 updates qualification status/score; 1.5 detects Odoo stage changes. Confirm field semantics, source normalization, idempotency, lead deduplication, consent/permission evidence, and whether marketing attribution survives every handoff. Align these fields with the campaign contract from Wave 21 and the existing database schema before adding columns or new tables.

## 4. Recommended next micro-sequence
1. **Freeze activation:** keep these exported workflows inactive until security and data gates are checked in a test environment.
2. **Exact schema review:** inspect the matching README, deployment guide, SQL schema and environment-variable list for each module; reconcile all duplicate copies without deleting them.
3. **Security tests:** missing/invalid signature, replayed request, malformed body, oversized payload, rate-limit behavior and no side effects on rejection.
4. **Approval tests:** AI output rejected/edited/approved; prevent auto-publication until approved; verify audit log and duplicate protection.
5. **Data-flow tests:** one lead each from Typebot and direct form; deduped repeat; missing email; source attribution; qualification failure; Odoo unavailable; Postgres unavailable; retry without duplicate creation.
6. **SEO safe-write tests:** dry-run diff, bounded update count, human review, backup/rollback, invalid model response and failure alert.
7. **Thin end-to-end pilot:** only after tests, trace one approved content/campaign touchpoint to lead → qualification → opportunity → delivery capacity → invoice/collection and compare actual with the financial plan.

## 5. Reconciliation against prior documents
- `Chats/Claude/Growth Engine/N8N-MASTER-FULL-FUNNEL-WORKFLOW-AND-PROGRESS-TRACKER (1).md` claims Phase 1 modules 1.1–1.5 are built, but its own wording that workflows are "working" must be distinguished from this static review: repository JSON exists and parses; live credentials/runtime have not been verified here.
- `Chats/Claude/Sales-Funnel-Marketing-Gap-Additions.md` identifies Track M and the universal marketing-to-Stage-06 bridge as gaps. Refine rather than blindly repeat that claim: 1.3/1.4/1.5 already provide Typebot/direct-form/CRM subsets, while full source coverage and experiment tracking remain unproven.
- `International-Digital-Marketing/00-Master-Plan-Framework.md` and Wave 21 remain the strategic requirement layers; this audit adds exact-file evidence, not a new marketing plan.

## 6. Acceptance checklist
- [ ] Canonical copy chosen and duplicate copies classified with provenance.
- [ ] All five workflows import into a non-production n8n instance.
- [ ] Credentials, environment variables, service endpoints and DB schema validated without exposing secrets.
- [ ] Public webhooks reject unsigned/invalid/replayed requests.
- [ ] AI-generated content cannot publish without required approval.
- [ ] SEO writes are previewed, bounded, auditable and reversible.
- [ ] End-to-end and negative tests pass; evidence and commit/version recorded.
- [ ] Owner approves activation; no claim of runtime/production readiness before that gate.

**Current disposition:** useful reusable workflow foundation found; static JSON parse confirmed. Security, human approval, integration breadth, environment configuration and runtime acceptance remain open.