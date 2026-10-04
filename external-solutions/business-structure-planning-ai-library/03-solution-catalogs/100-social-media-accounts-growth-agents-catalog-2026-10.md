# Social Media Accounts, Reading, Growth & Automation Agents Catalog — 2026-10

**Purpose:** Open-source agents, schedulers, MCP servers and tools for reading social accounts, generating content, publishing, engagement, follower growth, analytics and multi-platform management — with emphasis on human-approval gates and ethical use.

**Critical rule:** Aggressive auto-follow / mass engagement tools risk permanent bans. Prefer content quality + scheduled posting + light engagement. Always keep a human approval step before any public action.

**Related:** YouTube/social catalog `23-...`, free tools `97-...`, browser automation `98-...`.

---

## 1. Open-source multi-platform schedulers & publishers (MCP-ready)

| Resource | Platforms | Key features | Link |
|----------|-----------|--------------|------|
| **Postiz** | 30+ networks | Self-hostable Buffer alternative, AI assistant, agentic scheduling via MCP + CLI, n8n/Zapier | https://github.com/gitroomhq/postiz-app |
| **pendpost** | Instagram, FB, LinkedIn, YT, X, Telegram, Discord, Mastodon, Nostr, WordPress, Ghost… | Agent-first planner, human approval gate, brand-lint, MCP-native, MIT | https://github.com/pendpost/pendpost |
| **PostSider** | 33 connectors | Self-hostable, public API + SDK, MCP server (19 tools: draft, schedule, analytics, approval) | Search PostSider / lukaszblania |
| **trypost** | Multiple | Open-source PHP/Laravel social scheduler | GitHub trypostit/trypost |

---

## 2. Platform-specific growth & automation agents

| Resource | Focus | What it does | Link |
|----------|-------|--------------|------|
| **XActions** | X / Twitter | Complete toolkit: scrape, follow/unfollow, like, comment, analytics, MCP server, no API fees | https://github.com/nirholas/XActions |
| **OpenTwins** | Multi (esp. LinkedIn growth) | Open-source AI twins that grow presence (engagement, connections) — runs locally | https://opentwins.ai |
| **openclaw-social-media-skill** | X + LinkedIn | $0/month skill for agents — search mentions, profiles, trends without official APIs | https://github.com/zuocharles/openclaw-social-media-skill |
| **LocoAgent** | Social + browser | Real browser automation + MCP for social workflows | https://github.com/LocoreMind/locoagent |
| **Mesh Pilot AI Social Agent** | Shorts + multi-platform | Short-form video, captions, posting (already in catalog 23) | Catalog 23 |
| **Social-Media-AI-Agent (Maimoon)** | LinkedIn/X/IG | CrewAI/LangGraph multi-agent: analyze GitHub → generate & publish | https://github.com/Maimoon-github/Social-Media-AI-Agent |

---

## 3. Content + engagement skill graphs & multi-agent systems

| Resource | Scope | Notes | Link |
|----------|-------|-------|------|
| **Crewm8 Social Media Manager Skill Graph** | X, LinkedIn, IG, TikTok | 37 skills, 12 functions, agent-agnostic playbook | GitHub gokulsvision |
| **AutoGen-Social-Media-Manager** | Multi-platform | Local LLM (Mistral) multi-agent content + scheduling | https://github.com/imranfeb/AutoGen-Social-Media-Manager |
| Existing entries in catalog 23 | Social listening, UGC, podcast-to-shorts | SamurAIGPT, Mesh Pilot, Podcast Shorts Factory, etc. | `23-jarvis-...` |

---

## 4. Reading / listening / analytics agents

- Use **Browser Use / Stagehand / Playwright MCP** + social login sessions to read feeds, comments, competitor accounts.
- **XActions** and **openclaw-social-media-skill** provide structured search without paid APIs.
- Pair with Deep Research agents (catalog 23) for competitor matrices and weekly reports.
- Postiz / pendpost / PostSider expose analytics tools via MCP.

---

## 5. Recommended safe growth stacks

**Stack A — Content-first (lowest ban risk)**
1. pendpost or Postiz (self-hosted) + MCP
2. Content generation from catalog 23 / free tools 97
3. Human approval gate before every publish
4. Light scheduled engagement only

**Stack B — Research + engagement (careful)**
1. XActions or openclaw skill for reading/search
2. Browser Use / Nanobrowser for controlled interactions
3. Strict rate limits + human review of every action
4. Never mass-follow or mass-DM

**Stack C — Full agentic social team**
1. Multi-agent system (CrewAI / LangGraph) for strategy → content → schedule
2. Publishing layer = pendpost / Postiz MCP
3. Analytics feedback loop
4. Always keep kill-switch and audit log

---

## 6. Browser automation notes for social

Social platforms heavily detect automation. Prefer:
- Real browser profiles (Playwright persistent context or anti-detect browsers)
- Human-like delays and mouse movements
- Session cookies from real logins (never store passwords in agents)
- Tools already listed in catalog 98 (Browser Use, Steel, Nanobrowser, Skyvern)

---

## 7. Legal & platform risk warning

- Automated following, liking, commenting, or scraping can violate Terms of Service and lead to permanent bans.
- Use only for accounts you own, with explicit consent for any third-party accounts.
- Prefer official APIs where available and rate-limit aggressively.
- Document every automated action for audit.

**Last updated:** 2026-10-04
