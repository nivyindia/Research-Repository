# F1/F2 Static Validation Note — 2026-10-11

**Roadmap continuity:** Main roadmap unchanged. Phase-1 F2 complete; Phase-2 F2 started with 2.1.

## Staged replacements (all inactive)

| Module | Path | HTTP retries | Key open risks |
|---|---|---|---|
| 1.1 | `F1-replacements/1.1-content-social-factory/workflow.json` | 5/5 | WF-CONTENT-02 |
| 1.2 | `F1-replacements/1.2-seo-automation/workflow.json` | 5/5 | WF-SEO-03 |
| 1.3 | `F1-replacements/1.3-website-lead-capture/workflow.json` | 2/2 | WF-SEC-01 typebot-lead-capture |
| 1.4 | `F1-replacements/1.4-inbound-form-qualification/workflow.json` | 3/3 | WF-SEC-01 lead-qualification |
| 1.5 | `F1-replacements/1.5-central-crm-sync/workflow.json` | 1/1 | IF empty false branches; REPLACE_WITH_* IDs |
| **2.1** | `F1-replacements/2.1-multichannel-outreach/workflow.json` | **4/4** | WF-SEC-01 postal-reply-webhook; AI email/WhatsApp auto-send |

Note: User label "2.1 Odoo CRM Sync" maps to **1.5 Central CRM Sync** in the repo. **2.1 is Multi-channel Outreach.**

## Next
1. Continue Phase-2 F2 (2.2+) or F5 master migration as priority.
2. Do not activate any staged workflow until WF-SEC-01 / approval gates closed.
