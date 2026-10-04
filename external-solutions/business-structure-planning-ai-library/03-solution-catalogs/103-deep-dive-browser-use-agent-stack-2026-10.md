# Deep Dive: Browser Use + Playwright / Steel Agent Stack — 2026-10

**Goal:** Build a reliable AI browser agent that can navigate real websites, fill forms, extract data, perform multi-step tasks, and (with care) interact with social platforms or WordPress admin — using the highest-quality open-source agent framework currently available.

**Core library:** Browser Use (https://github.com/browser-use/browser-use)  
**Recommended companions:** Playwright (precision), Steel (managed stealth sessions), Stagehand, Playwright MCP.

**Related catalogs:** `98-browser-automation-...`, `100-social-...`, `99-website-...`

---

## 1. Minimal local setup (zero cloud)

```bash
# Python 3.11+
uv venv --python 3.11
source .venv/bin/activate          # Windows: .venv\Scripts\activate

uv pip install browser-use python-dotenv
uv run playwright install          # installs Chromium + stealth patches
```

Create `.env`:
```
OPENAI_API_KEY=sk-...
# or ANTHROPIC_API_KEY / GOOGLE_API_KEY etc.
ANONYMIZED_TELEMETRY=false
```

Minimal agent script (`agent.py`):
```python
import asyncio
from dotenv import load_dotenv
from browser_use import Agent
from browser_use.llm import ChatOpenAI   # or ChatAnthropic, ChatGoogle etc.

load_dotenv()

async def main():
    agent = Agent(
        task="Go to https://example.com and summarize the main heading and any CTA buttons",
        llm=ChatOpenAI(model="gpt-4o-mini"),
    )
    result = await agent.run()
    print(result.final_result())

asyncio.run(main())
```

Run: `python agent.py`

---

## 2. Production-ready stack with Steel (stealth + cloud browsers)

```bash
uv pip install browser-use steel-sdk python-dotenv
```

```python
import os, asyncio
from dotenv import load_dotenv
from steel import Steel
from browser_use import Agent, BrowserSession
from browser_use.llm import ChatOpenAI

load_dotenv()
client = Steel(steel_api_key=os.getenv("STEEL_API_KEY"))

async def main():
    session = client.sessions.create(use_proxy=True, solve_captcha=True)
    cdp_url = f"{session.websocket_url}&apiKey={os.getenv('STEEL_API_KEY')}"

    agent = Agent(
        task="Your multi-step task here",
        llm=ChatOpenAI(model="gpt-4o"),
        browser_session=BrowserSession(cdp_url=cdp_url),
    )
    result = await agent.run()
    print(result.final_result())

    client.sessions.release(session.id)

asyncio.run(main())
```

Steel free tier gives limited browser hours; self-host Steel for unlimited local use.

---

## 3. Hybrid: Browser Use + Playwright on the same Chrome instance

Share one Chromium via CDP so you get AI decision-making **and** precise Playwright selectors / screenshots / tracing.

(See official example: `browser-use/examples/browser/playwright_integration.py`)

Pattern:
1. Launch Chrome with `--remote-debugging-port=9222`
2. Connect both Playwright and Browser Use to `http://localhost:9222`
3. Give the Agent custom tools that call Playwright functions when needed

This is the most robust pattern for production workflows that mix exploration and deterministic steps.

---

## 4. Recommended task patterns for Nivy

**Safe / high-value uses**
- Competitor research & screenshot reports
- Reading public social feeds / comments (with rate limits)
- Filling internal admin forms after human login session
- Extracting structured data from any site for the research agents
- WordPress staging admin tasks (when combined with Novamira or after manual login)

**High-risk (use extreme caution + human approval)**
- Any social platform interaction that looks like mass engagement
- Login + password entry (prefer pre-authenticated persistent contexts)
- Publishing or spending money

Always wrap public actions with an explicit human confirmation step.

---

## 5. Full recommended Nivy browser agent stack

1. **Local development:** Browser Use + Playwright (CDP shared)
2. **Stealth / anti-detect needs:** Steel self-hosted or managed + Browser Use
3. **MCP exposure:** Playwright MCP server so Claude/Cursor can call browser tools directly
4. **Orchestration:** LangGraph or n8n for multi-step workflows + approval gates
5. **Observability:** Playwright tracing + session replay (Steel viewer or local recordings)

---

## 6. Safety checklist

- [ ] Persistent browser context with real user cookies (never store passwords in the agent)
- [ ] Explicit rate limits and human-like delays
- [ ] Kill switch / max steps per run
- [ ] Full action log + screenshots
- [ ] Never run unattended on production accounts without an approval gate
- [ ] Respect robots.txt and platform Terms of Service

**Last updated:** 2026-10-04
