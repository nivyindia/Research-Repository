# Complete Digital Marketing Automation Catalog — 2026-10

**Purpose:** Full-depth coverage of every major digital marketing division with open-source agents, multi-agent systems, n8n/Activepieces workflows, skills and tools. Nothing should be left uncovered for a complete marketing automation layer.

**Divisions covered:**
1. SEO (Technical, On-page, Content, GEO/AEO, Link building)
2. Content Marketing & Blog Automation
3. Social Media Marketing & Growth
4. Email Marketing & Sequences
5. Paid Ads / Performance Marketing
6. Analytics, Reporting & Optimization
7. Lead Generation & Outreach
8. Full Marketing Agency / Department Multi-Agent Systems
9. n8n / Workflow Orchestration Libraries

**Related existing catalogs:** 23 (YouTube/Social), 97 (free tools), 98 (browser), 100 (social growth), 101-103 (deep dives).

**Reuse rule:** Prefer self-hosted + human-approval gates. Verify commercial rights, API costs and platform ToS.

---

## 1. SEO (Search Engine Optimization) — Full Stack

| Resource | Type | Coverage | Link |
|----------|------|----------|------|
| **Digital Marketing Agents** | Multi-agent | SEO + blog + social + ads + email + analytics | https://github.com/Shivay00001/digital-marketing-agents |
| **SEO Machine / Claude SEO pipelines** | Claude Code skills | Keyword research, competitor SERP, content writing, optimization, GSC/GA4 integration, WordPress publish | Search “SEO Machine Claude” / claude-seo skills |
| **AgentWrite** | Multi-agent (LangGraph) | Research → draft → critique → SEO-optimized articles | https://github.com/deeprodge/AgentWrite |
| **ai-content-lab** | CrewAI multi-agent | Research, writing, SEO optimization | https://github.com/tiagomonteiro0715/ai-content-lab |
| **ai-seo-multi-agent-system** | CrewAI + distributed | Technical audit, performance monitor, competitor intelligence, GSC/GA4 | https://github.com/avinash-gupta-rdz/ai-seo-multi-agent-system |
| **seo-blog-automation** | n8n multi-agent | SEO/AEO blog pipeline with GEO compliance, anti-AI-tell editing, optional publish | https://github.com/Juliankie-creator/seo-blog-automation |
| **Marketing-AI-Agents** | Full pipeline | Keyword → SEO blog → images → publish → backlink outreach | https://github.com/zachd1234/Marketing-AI-Agents |
| **Multi-Agent-SEO-Blog-Generator** | Multi-agent | Research → outline → write → SEO enhance → proofread | https://github.com/Uddhav-24/Multi-Agent-SEO-Blog-Generator |
| **ericosiu/ai-marketing-skills** | Skills library | SEO gaps, landing page audits, content scoring, ICP finding | https://github.com/ericosiu/ai-marketing-skills |

**SEO sub-capabilities mapped:** Keyword research, SERP analysis, content briefs, on-page optimization, technical audits, internal linking, schema, GEO/AEO (AI Overviews), competitor gap analysis, GSC/GA4 data loops.

---

## 2. Content Marketing & Blog Automation

Covered heavily by the SEO agents above + existing media factory in catalog 23.

Additional:
- Podcast → content atomization (Podcast Shorts Factory already in 23)
- Long-form → multi-platform repurposing pipelines
- Brand voice + humanizer layers (see pendpost brand-lint and anti-AI-tell editors)

---

## 3. Social Media Marketing (already strong in library)

See catalogs:
- `23-jarvis-...` (Mesh Pilot, SamurAIGPT, LocoAgent, etc.)
- `100-social-media-accounts-growth-agents-catalog-2026-10.md`
- `102-deep-dive-social-pendpost-mcp-stack-2026-10.md`

Key additions from this batch:
- **Marketing Agent Teams (MAT)** — 30+ agents across 7 clusters for multi-platform (TikTok, IG, YT, FB, Reddit, X, Pinterest) | https://github.com/Ahil-NS/marketing-agent-teams
- **opensoul** — Full agentic marketing agency stack (Director → Strategist → Producer → Creative → Growth → Analyst) | https://github.com/iamevandrake/opensoul

---

## 4. Email Marketing & Sequences

| Resource | Type | What it covers | Link |
|----------|------|----------------|------|
| **Digital Marketing Agents** | Multi-agent | Email campaigns + sequences | https://github.com/Shivay00001/digital-marketing-agents |
| **agentic-ai-marketing-workflow-n8n** | n8n | Lead gen → email verification → personalized outreach → human approval → Gmail send | https://github.com/N1wan7ha/agentic-ai-marketing-workflow-n8n |
| **JeweledTech agentic-framework** | Full company agents | Outbound Sales Manager, Outreach Agent (sequences, follow-ups) | https://github.com/JeweledTech/agentic-framework |
| **Digital-FTE** | Autonomous employee | Gmail watcher + draft replies + approval | https://github.com/AbdullahMalik17/Digital-FTE |
| **ericosiu/ai-marketing-skills** | Skills | Building outbound lists, mining sales calls for sequences | https://github.com/ericosiu/ai-marketing-skills |

**Missing deep native email platforms:** Most open-source coverage is via n8n + Gmail/SMTP + LLM personalization rather than full ESP clones. Use n8n + your free Gmail/Outlook + LLM for sequences.

---

## 5. Paid Ads / Performance Marketing

| Resource | Coverage | Link |
|----------|----------|------|
| **Digital Marketing Agents** | Paid ads management | Same repo as above |
| **claude-ads** style skills | Google Ads management | Search claude-ads / AI marketing skills |
| **Creative Ad Agent** | Ad concepts + images from website | Already in catalog 23 |
| **Atlas Marketing Studio / Open AI UGC** | UGC ad creatives | Already in catalog 23 |
| **opensoul Growth Marketer** | Paid acquisition + CRO + A/B | https://github.com/iamevandrake/opensoul |

Deep native Meta/Google Ads API agents are thinner in pure open-source; most production systems use n8n + official APIs + LLM for creative/copy + human approval for spend.

---

## 6. Analytics, Reporting & Optimization

- Metabase / Apache Superset (already in catalog 23)
- Deep Research agents for competitive + performance reports
- GSC + GA4 integrations inside SEO multi-agent systems above
- Social analytics via pendpost / Postiz / platform native tools

---

## 7. Lead Generation & Outreach

| Resource | Pipeline | Link |
|----------|----------|------|
| **agentic-ai-marketing-workflow-n8n** | Google scrape → email verify → human approve → personalized email | https://github.com/N1wan7ha/agentic-ai-marketing-workflow-n8n |
| **Marketing-AI-Agents** | Content + backlink outreach with personalized pitches | https://github.com/zachd1234/Marketing-AI-Agents |
| **ericosiu/ai-marketing-skills** | ICP finding, outbound list building | https://github.com/ericosiu/ai-marketing-skills |
| **Pre-Sales Agent / Comp AI CRM / AI-CRM** | Already in catalog 23 | See 23 |

---

## 8. Full Marketing Agency / Department Multi-Agent Systems

| Resource | Structure | Link |
|----------|-----------|------|
| **opensoul** | Director + Strategist + Producer + Creative + Growth + Analyst | https://github.com/iamevandrake/opensoul |
| **Marketing Agent Teams (MAT)** | 30+ agents in 7 clusters, 7-stage pipeline | https://github.com/Ahil-NS/marketing-agent-teams |
| **JeweledTech agentic-framework** | Full company incl. Marketing + Sales departments + 87 n8n workflows | https://github.com/JeweledTech/agentic-framework |
| **Digital Marketing Agents** | SEO + blog + social + ads + email + analytics | https://github.com/Shivay00001/digital-marketing-agents |
| **CompanyOS / Cyber AI Team / AgentOS** | Broader company agents that include marketing | Already in catalog 23 |

---

## 9. n8n / Workflow Orchestration Libraries (Critical Layer)

| Resource | Size / Focus | Link |
|----------|--------------|------|
| **YuriCrystal/n8n-marketing-flows** | 79 workflows (social, sentiment, news, ads, SEO) + local Ollama versions | https://github.com/YuriCrystal/n8n-marketing-flows |
| **agentic-ai-marketing-workflow-n8n** | Lead gen + email + social | https://github.com/N1wan7ha/agentic-ai-marketing-workflow-n8n |
| **seo-blog-automation** | Full SEO/AEO blog pipeline in n8n | https://github.com/Juliankie-creator/seo-blog-automation |
| **n8n-workflow-templates** (autonomous social) | Scheduled social content engine | Search Mfrostbutter/n8n-workflow-templates |
| **JeweledTech** | 87 n8n workflows across departments | https://github.com/JeweledTech/agentic-framework |
| **n8n core** | The orchestration engine itself | https://github.com/n8n-io/n8n |

**Recommendation:** Self-host n8n (Docker, free) + import the marketing flow libraries above. Pair with free LLMs (Ollama / free API tiers) where possible.

---

## 10. Coverage Status vs Ideal Digital Marketing Stack

| Division | Status in Library | Notes |
|----------|-------------------|-------|
| SEO (full) | Strong | Multi-agent + n8n + skills |
| Content / Blog | Strong | Multiple pipelines |
| Social Media | Very Strong | Dedicated catalogs + pendpost |
| Email Marketing | Medium-Strong | n8n + agents + sequences; less full ESP |
| Paid Ads | Medium | Creative + some management; spend control via human |
| Analytics & Reporting | Strong | BI tools + research agents |
| Lead Gen & Outreach | Strong | Multiple n8n + agent pipelines |
| Full Agency Orchestration | Strong | opensoul, MAT, JeweledTech, CompanyOS |
| Workflow Layer (n8n) | Strong | 79+ marketing flows + core n8n |

**Remaining thin areas (for future discovery):**
- Native deep Meta/Google Ads bidding agents with full budget safety
- Complete open-source ESP (email service provider) clones
- Advanced attribution / multi-touch modeling agents
- Influencer discovery + outreach at scale with strong compliance

---

## 11. Recommended Free Starting Stack for Complete Digital Marketing

1. **Orchestration:** Self-hosted n8n + YuriCrystal marketing flows
2. **SEO + Content:** Digital Marketing Agents or SEO multi-agent systems + Claude/Gemini free
3. **Social:** pendpost (human approval) + existing social agents
4. **Email:** n8n + Gmail + LLM personalization
5. **Research & Reports:** Deep Research agents
6. **Website/Landing:** Novamira + Local WordPress
7. **Analytics:** Metabase or Superset + platform native

**Last updated:** 2026-10-04
**This catalog closes the major gaps for full digital marketing automation coverage.**
