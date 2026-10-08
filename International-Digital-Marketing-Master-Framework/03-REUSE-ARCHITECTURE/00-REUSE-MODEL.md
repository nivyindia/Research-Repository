# Reuse Architecture

## Decision Order (mandatory for every agent and human)

```
1. Exists in our Component Library / repository?
      → YES → REUSE
2. Official / industry / open-source resource exists?
      → YES → ADAPT
3. Compatible component exists?
      → YES → INTEGRATE
4. Small modification needed?
      → YES → EXTEND
5. Real gap verified?
      → YES → BUILD
6. After BUILD → STORE back into Component Library
```

**Default permission for agents: REUSE only.**  
Build requires explicit gap flag + approval (human-in-the-loop for net-new frameworks).

## Component Library Categories

See `12-COMPONENT-LIBRARY/` for frameworks, methodologies, sops, playbooks, templates, checklists, prompts, skills, ai-skills, ai-agents, agent-workflows, automation-workflows, apis, mcp-servers, connectors, open-source, tools, software, libraries, datasets, knowledge-bases, integrations, dashboards, kpi-definitions, benchmarks, case-studies, official-docs.

## Relationship Model

```
Capability (taxonomy topic)
    → Process
        → SOP / Playbook
            → Skill (human or AI)
                → Agent
                    → Tool / Software / API / MCP
                        → Workflow (automation)
                            → KPI
                                → Evidence / Benchmark
```

Store each node **once**. Topics only **reference** component IDs.

## Anti-Duplication Rules

1. Same framework applicable to many topics → one file under `frameworks/`, referenced everywhere  
2. Canonical path is the only editable location  
3. Cross-links use relative paths or stable IDs  
4. Superseded docs move to archive with redirect note  
5. External resources: store citation + summary, not full copyrighted text  
6. Provenance required: source URL, date, license if open-source  
