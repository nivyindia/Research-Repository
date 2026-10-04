# Browser Automation, AI Agents & Extensions Library — 2026-10

**Purpose:** Comprehensive free / freemium / open-source tools, frameworks, managed services, and Chrome extensions for browser automation, computer-use agents, RPA-style task automation, and agentic AI that can click, fill forms, scrape, research, and complete multi-step web tasks autonomously.

**Why this matters for Nivy:** Browser automation is the practical “hands” layer for any agent that needs to operate real websites (YouTube Studio, social platforms, CRMs, research sites, admin panels) without official APIs.

**Reuse rule:** Prefer open-source / self-hosted first (Playwright, Browser Use, Stagehand, Playwright MCP, Steel, Nanobrowser). Use managed free tiers only for prototyping. Always add human-approval gates for actions that publish, spend money, or change live data.

---

## 1. Core open-source browser automation frameworks (foundation)

| Tool | Type | Free? | What it does | Link |
|------|------|-------|--------------|------|
| **Playwright** | Framework | Fully free (OSS) | Modern cross-browser automation (Chromium/Firefox/WebKit), auto-wait, tracing, codegen | https://playwright.dev / https://github.com/microsoft/playwright |
| **Selenium** | Framework | Fully free | Classic WebDriver standard, multi-language, Grid for parallel | https://www.selenium.dev |
| **Puppeteer** | Framework | Fully free | Headless Chrome control (Node) | https://pptr.dev |
| **WebdriverIO** | Framework | Fully free | High-level automation with good reporting | https://webdriver.io |
| **Cypress** | Framework | Free core | Developer-friendly testing & limited automation | https://www.cypress.io |

**Recommended default for new Nivy agents:** Playwright.

---

## 2. AI-native browser agent frameworks (agentic layer)

| Tool | Type | Free? | What it does | Link |
|------|------|-------|--------------|------|
| **Browser Use** | Python agent framework | Fully free self-host + freemium cloud | LLM agents control real browsers (click, type, extract). High WebVoyager scores | https://github.com/browser-use/browser-use |
| **Stagehand** | TypeScript SDK on Playwright | Fully free | `act` / `extract` / `observe` primitives + action caching | https://github.com/browserbase/stagehand |
| **Playwright MCP** | MCP server | Fully free | Official Microsoft MCP that exposes Playwright to any MCP client (Claude, Cursor, custom agents) | https://github.com/microsoft/playwright-mcp |
| **Skyvern** | Vision-based agent platform | Free credits + self-host | Vision + LLM, handles novel UIs without brittle selectors, 2FA support | https://github.com/Skyvern-AI/skyvern |
| **Steel** | Managed + OSS browser infra | Free self-host + freemium cloud | Open-source alternative to Browserbase; stealth, sessions, CDP | https://github.com/steel-dev/steel-browser |
| **BrowserOS** | Open-source AI browser | Fully free | Chromium + built-in AI agent, local models via Ollama | Search BrowserOS GitHub |
| **Nanobrowser** | Chrome extension | Fully free | Multi-agent team that automates browsing tasks inside your real Chrome | Chrome Web Store / GitHub |
| **MagenticLite** | Open-source agent | Fully free | Browser + local files agent | Search MagenticLite |
| **UI-TARS (ByteDance)** | Multimodal agent | Free | Screenshot → structured UI control for desktop + browser | Search UI-TARS |
| **Microsoft OmniParser** | UI parser | Free | Screenshot → interactable elements for agents | https://github.com/microsoft/OmniParser |

---

## 3. Managed / cloud browser infrastructure (free tiers)

| Tool | Free tier | Notes | Link |
|------|-----------|-------|------|
| **Browserbase** | 1 browser-hour/month, 3 concurrent, 3 agent runs | Popular managed Chromium for agents | https://www.browserbase.com |
| **Steel** | Self-host unlimited + cloud credits | Best open + managed hybrid | https://steel.dev |
| **Kernel** | $0 + monthly credits, profiles, stealth, extensions | Strong free feature set | https://www.kernel.sh |
| **Browserless** | Free plan available | Classic headless Chrome cloud | https://www.browserless.io |
| **Hyperbrowser** | Limited free credits | Agent-friendly | https://hyperbrowser.ai |
| **Anchor Browser** | Free credits | CDP + Playwright support | Search Anchor Browser |
| **Cloudflare Browser Run** | Free low tier | Cheap entry | Cloudflare docs |

---

## 4. Chrome extensions for agentic / automation use

| Extension | Free? | What it does | Notes |
|-----------|-------|--------------|-------|
| **Nanobrowser** | Free | Multi-agent browser automation inside Chrome | Strong local alternative to cloud agents |
| **Bardeen AI** | Freemium | Playbooks that scrape, fill forms, move data across web apps | Closest to “Zapier inside browser” |
| **Magical** | Freemium | AI workflow automation across sites | Form filling + data entry |
| **Merlin AI** | Free limited | Universal AI sidebar on any page (summarize, draft, act) | Lightweight |
| **AutoGPT for Chrome** | Free/trial | Goal-oriented autonomous browsing | Classic agent style |
| **Claude in Chrome** | Freemium | Governed Chrome agent (forms, research, scheduled tasks) | High quality when available |
| **vidIQ / TubeBuddy** | Free tiers | YouTube-specific SEO automation inside Studio | Already in content catalog |
| **YTubViral / Vidscape** | Free | YouTube SEO score + AI titles inside Studio | See content catalog |

---

## 5. Classic RPA / no-code automation (still useful)

| Tool | Free? | Link |
|------|-------|------|
| **n8n** | Fully free self-host | https://n8n.io / https://github.com/n8n-io/n8n |
| **Activepieces** | Free self-host | Open-source Zapier alternative |
| **Huginn** | Fully free | Self-hosted agent that watches the web |
| **Browserflow** | Freemium | Visual browser automation |
| **Axiom.ai** | Freemium | No-code browser bots |
| **UiPath Community** | Free for individuals | Enterprise RPA with free community edition |
| **Automation Anywhere Community** | Free limited | Similar |

---

## 6. Recommended Nivy browser-automation stacks

### Stack A — Fully local / zero cost (preferred for privacy & control)
1. Playwright (or Puppeteer)
2. Browser Use **or** Stagehand **or** Playwright MCP
3. Local LLM (Ollama) or cheap API key
4. Optional: Nanobrowser extension for interactive use
5. Human approval gate before any publish/spend action

### Stack B — Fast prototyping
1. Playwright MCP + Claude Desktop / Cursor
2. Or Browser Use cloud free tier / Browserbase free hour
3. Switch to Stack A once workflow is stable

### Stack C — Production agent fleet
1. Steel or Browserbase (managed sessions + stealth)
2. Stagehand or Browser Use as the agent layer
3. n8n / LangGraph for orchestration + approvals
4. Observability + audit log

---

## 7. Safety & governance notes (mandatory)

- Never give an agent unrestricted write access to live accounts without an approval step.
- Prefer read-only research agents first.
- Log every browser action (Playwright tracing, session replay).
- Respect robots.txt, rate limits, and platform Terms of Service.
- For YouTube / social publishing: keep a human-in-the-loop gate even if the agent prepares the upload.

---

## 8. Cross-links inside this library

- Content creation free tools → `97-free-freemium-external-content-creation-tools-catalog-2026-10.md`
- Open-source YouTube / social agents → `23-jarvis-voice-creator-youtube-social-marketing-reuse-catalog-2026-09.md`
- Company-wide agent systems → catalogs in `02-company-department-models` and `03-solution-catalogs`

**Last updated:** 2026-10-04
**Next discovery gaps:** Instagram/TikTok native upload automation with approval, CAPTCHA-solving policies, multi-account session management, stealth fingerprint rotation best practices.
