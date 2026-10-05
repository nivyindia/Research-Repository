# Master Agentic AI Systems, Frameworks, MCP, Skills, Plugins & Connectors Catalog — 2026-10

**Purpose:** Comprehensive open-source / free-first library of agentic AI systems, multi-agent frameworks, MCP servers & connectors, skills, plugins, harnesses, browser OS agents, and related automation layers. Goal: nothing critical should be missing when building high-automation Nivy stacks.

**Preference:** Open-source (MIT/Apache/AGPL) and free self-hosted first. Paid-only items are excluded or noted only as reference.

**Related catalogs:** All previous 23, 97–104 (content, social, website, browser, digital marketing).

---

## 1. Core Agentic Frameworks & Multi-Agent Orchestration (Open Source)

| Project | Type | License | Stars (approx) | Key Strength | Link |
|---------|------|---------|----------------|--------------|------|
| **LangGraph** | Stateful graph orchestration | MIT | 42k+ | Explicit control, checkpoints, human-in-loop | https://github.com/langchain-ai/langgraph |
| **CrewAI** | Role-based multi-agent crews | MIT | 59k+ | Fast role-playing teams | https://github.com/crewAIInc/crewAI |
| **AutoGen / AG2** | Conversational multi-agent | CC-BY / Apache | 61k+ | Multi-agent chat & collaboration | https://github.com/microsoft/autogen |
| **MetaGPT** | Software company role-play | MIT | 70k+ | Full company simulation | https://github.com/FoundationAgents/MetaGPT |
| **Dify** | Agentic workflows + RAG + tools | Open | 158k+ | Low-code + self-hosted production | https://github.com/langgenius/dify |
| **DeerFlow** | Long-horizon SuperAgent | Open | 83k+ | Research, code, create with sandboxes & subagents | https://github.com/bytedance/deer-flow |
| **Agno** | Lightweight high-perf agents | Open | 42k+ | Fast, memory, multimodal | Search Agno AI |
| **Pydantic AI** | Type-safe agents | MIT | 20k+ | Structured output, production | https://github.com/pydantic/pydantic-ai |
| **Mastra** | TypeScript agents | Open | 28k+ | RAG + observability | Search Mastra AI |
| **smolagents** | Minimal code-writing agents | Apache | 29k+ | Agents that write code to act | Hugging Face / GitHub |
| **OpenAI Agents SDK** | Agent + Runner + Handoffs | MIT | 29k+ | Clean primitives + MCP | OpenAI GitHub |
| **Google ADK** | Code-first agents | Apache | 21k+ | Vertex deployable | Google |
| **Microsoft Agent Framework** | Event-driven | MIT | — | .NET + Python production | Microsoft |
| **CAMEL** | Role-playing society | Apache | 17k+ | Agent society research | https://github.com/camel-ai/camel |
| **PraisonAI** | Multi-agent + self-reflection | MIT | 9k+ | Workflows with reflection | GitHub |
| **Atomic Agents** | Composable small parts | MIT | 6k+ | Modular composition | GitHub |
| **Hive** | Production multi-agent harness | Apache | 11k+ | Production focus | GitHub |
| **OpenAgents** | Agent networks (WebSocket/gRPC/MCP/A2A) | Apache | 4k+ | Cross-runtime | GitHub |

---

## 2. Personal / Desktop / Self-Hosted Agent Systems

| Project | Type | Notes | Link |
|---------|------|-------|------|
| **OpenClaw** | Self-hosted personal AI | Massive growth, 50+ integrations, skills | Search OpenClaw GitHub |
| **nanobot** | Lightweight self-hosted | WebUI, tools, memory, MCP, multi-agent | https://github.com/HKUDS/nanobot |
| **BrowserOS** | Open-source Agentic Browser | Chromium fork + built-in agents, MCP server, local models, privacy-first alternative to Comet/Atlas/Dia | https://github.com/browseros-ai/BrowserOS |
| **BrowserOS-agent** | Agent monorepo for BrowserOS | Agent loop + MCP + controller extension | https://github.com/browseros-ai/BrowserOS-agent |
| **JARVIS family** | Voice + computer-use | Already in catalog 23 (OpenDex, PersonalJarvis, OpenJarvis, etc.) | Catalog 23 |
| **Hermes Agent** | Persistent assistant | Memory, skills, scheduled tasks, messaging | Nous Research |
| **Openwork / coworker** | AI coworker platform | Open-source | GitHub |

**BrowserOS highlight:** Fully open-source (AGPL), runs agents locally with your logins, supports MCP, scheduled tasks, workflows, any LLM (including Ollama). Perfect free “agentic browser OS” layer.

---

## 3. MCP Servers, Connectors & Gateways (Open Source Focus)

### Official / Core
- **Official MCP Servers collection** (filesystem, git, fetch, memory, postgres, etc.) — canonical reference set
- **MCP TypeScript / Python SDKs**
- **MCP Registry** — discovery “app store” for servers

### High-value open-source MCP categories (from Glama & community)
- Filesystem / Shell / OS automation
- Databases (Postgres, Redis, vector DBs)
- Knowledge & Memory (persistent agent memory, Obsidian, notes)
- Browser / Web / Search
- GitHub / DevOps
- Calendar / Email / Productivity
- WordPress / CMS (Novamira, NIBWP already catalogued)
- Social / Publishing (pendpost MCP already catalogued)

### Gateways (for governing many MCP + A2A)
| Gateway | License | Notes | Link |
|---------|---------|-------|------|
| **Bifrost** | Apache 2.0 | High-perf MCP + LLM routing | Maxim AI |
| **agentgateway** | Apache 2.0 | Tool federation + A2A | Community |
| **IBM ContextForge** | Apache 2.0 | Federation + virtual servers | IBM |
| **Envoy AI Gateway** | Open | LLM + MCP governance | Envoy |

**Recommendation:** Start with official MCP servers + Playwright MCP + pendpost MCP + Novamira MCP + BrowserOS MCP. Add more as needed from Glama registry (96k+ servers exist; filter open-source only).

---

## 4. Skills, Plugins & Agent Skill Systems

- **Agent Skills / SKILL.md pattern** — many projects now use markdown skill files (YAML frontmatter + instructions)
- **ericosiu/ai-marketing-skills** — marketing agency skills (already referenced)
- **Automattic wordpress-agent-skills** — WordPress theme/site skills
- **Claude Code / Cursor / Cline skill ecosystems** — community skill packs
- **ecoclaw-mcp / skill managers** — local skill listing, forking, updating
- **DeepSeek Harness / plugin systems** — “everything is a plugin” style

Skills are the portable “how-to” layer that agents load on demand. Prefer projects that keep skills as plain markdown/files for easy reuse.

---

## 5. Browser & Computer-Use Agents (Open Source)

| Project | Type | Link |
|---------|------|------|
| **Browser Use** | Python LLM browser agent | https://github.com/browser-use/browser-use |
| **Stagehand** | Playwright + AI primitives | Browserbase GitHub |
| **Playwright MCP** | Official Microsoft MCP | https://github.com/microsoft/playwright-mcp |
| **Skyvern** | Vision-based browser agent | https://github.com/Skyvern-AI/skyvern |
| **Steel** | Open browser infra | https://github.com/steel-dev/steel-browser |
| **BrowserOS** | Full agentic browser OS | https://github.com/browseros-ai/BrowserOS |
| **Nanobrowser** | Chrome extension multi-agent | Chrome Web Store / GitHub |
| **UI-TARS** | Multimodal GUI agent | ByteDance |
| **OmniParser** | UI screenshot → elements | Microsoft |

(Already partially covered in catalog 98 & 103; this consolidates.)

---

## 6. Workflow / Low-Code Agentic Layers

| Project | Type | Link |
|---------|------|------|
| **n8n** | Workflow + AI agents | https://github.com/n8n-io/n8n |
| **Dify** | Agentic + RAG platform | https://github.com/langgenius/dify |
| **Activepieces** | Open Zapier alternative | GitHub |
| **Langflow / Flowise** | Visual agent builders | GitHub |
| **Windmill** | Code + workflow | GitHub |

Pair these with the marketing flow libraries already in catalog 104.

---

## 7. Recommended Free / Open-Source Starting Stack for Maximum Automation

1. **Orchestration core:** LangGraph or CrewAI or Dify (self-hosted)
2. **Browser layer:** BrowserOS + Browser Use + Playwright MCP
3. **Tool protocol:** Official MCP servers + domain MCPs (WordPress, Social, Filesystem, Memory)
4. **Skills:** Markdown skill packs + marketing/SEO skills
5. **Workflow glue:** n8n (self-hosted) + existing marketing flows
6. **Voice / Desktop:** JARVIS family or OpenClaw
7. **Memory & Knowledge:** Open-source memory MCP servers
8. **Human approval:** Always keep explicit gates (pendpost style, LangGraph interrupts, n8n wait nodes)

---

## 8. Discovery Sources (keep checking)

- https://github.com/kaushikb11/awesome-llm-agents
- Glama MCP Registry (filter open-source)
- Awesome MCP lists
- GitHub topics: agentic-framework, agent-framework, mcp-server
- BrowserOS, OpenClaw, DeerFlow release notes

---

## 9. Coverage Note

This catalog intentionally prioritizes **open-source and free self-hostable** systems. Thousands of MCP servers exist; the practical approach is:
- Start with the official set + the ones already integrated in our domain catalogs (marketing, website, social, browser).
- Add specialized open-source MCPs only when a concrete need appears.
- Avoid paid-only SaaS agent platforms.

**Last updated:** 2026-10-05  
**This file is the master index for agentic AI infrastructure in the Nivy library.**
