#!/usr/bin/env python3
"""Static contract consistency checks for A001 / SK001.

This is not a runtime test. It verifies repository artifacts remain mutually
consistent and prevents accidental promotion of untested contracts.
"""
from pathlib import Path
import json
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]


def load_yaml(relative_path):
    path = ROOT / relative_path
    with path.open(encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    fixture_path = "Chats/ChatGPT/Multi Agent AIOS/03-skills/SK001-market-research/fixtures/contract-fixtures.yaml"
    event_path = "Chats/ChatGPT/Multi Agent AIOS/06-data/event-schemas/research-events-v1.yaml"
    mapping_path = "Chats/ChatGPT/Multi Agent AIOS/02-agents/agent-skill-mappings.yaml"
    skill_registry_path = "Chats/ChatGPT/Multi Agent AIOS/03-skills/registry.yaml"
    tool_registry_path = "Chats/ChatGPT/Multi Agent AIOS/04-tools/TOOL_REGISTRY.yaml"
    agent_path = "Chats/ChatGPT/Multi Agent AIOS/agents/market-research/agent.yaml"
    status_path = "Chats/ChatGPT/Multi Agent AIOS/02-agents/F1-A001-status.yaml"
    workflow_path = "Chats/ChatGPT/Multi Agent AIOS/08-infrastructure/n8n/workflows/A001-market-research-trigger.json"

    fixtures = load_yaml(fixture_path)
    require(fixtures.get("skill_id") == "SK001", "fixtures must target SK001")
    cases = fixtures.get("cases", [])
    ids = [case.get("id") for case in cases]
    require(len(cases) == 12, f"expected 12 SK001 fixtures, found {len(cases)}")
    require(len(ids) == len(set(ids)), "fixture IDs must be unique")
    required_categories = {
        "valid_input", "invalid_input", "evidence_conflict", "freshness",
        "provenance", "authorization", "resilience", "insufficient_evidence",
        "output_validation", "normalization", "source_quality",
    }
    present_categories = {case.get("category") for case in cases}
    require(required_categories.issubset(present_categories),
            f"missing fixture categories: {sorted(required_categories - present_categories)}")

    events = load_yaml(event_path)
    require(events.get("status") == "draft", "research events must remain draft before review")
    event_records = events.get("events", {})
    require("market.research.requested" in event_records, "request event contract missing")
    require("research.completed" in event_records, "completion event contract missing")
    envelope_required = set(events.get("envelope", {}).get("required", []))
    canonical_envelope = {
        "event_id", "event_type", "event_version", "occurred_at", "source",
        "company_id", "entity_type", "entity_id", "correlation_id",
        "causation_id", "payload", "metadata",
    }
    require(canonical_envelope.issubset(envelope_required),
            f"event envelope fields missing: {sorted(canonical_envelope - envelope_required)}")

    mapping = load_yaml(mapping_path)
    a001_mappings = [item for item in mapping.get("mappings", []) if item.get("agent_id") == "A001"]
    require(len(a001_mappings) == 1, "exactly one A001 mapping record is required")
    a001_mapping = a001_mappings[0]
    require(a001_mapping.get("status") == "blocked", "A001 mapping must remain blocked until approval/tests")
    require("SK001" in a001_mapping.get("required_skills", []), "SK001 must be a required A001 skill")
    require(a001_mapping.get("failure_behavior") == "fail_closed", "mapping must fail closed")

    skills = load_yaml(skill_registry_path)
    skill_status = {item.get("id"): item.get("status") for item in skills.get("skills", [])}
    require(skill_status.get("SK001") == "specified", "SK001 registry status must be specified")
    require(skill_status.get("SK002") == "planned", "SK002 must not be treated as available")

    tools = load_yaml(tool_registry_path)
    tool_status = {item.get("tool_id"): item.get("status") for item in tools.get("entries", [])}
    research_tools = [
        "TOOL-FIRECRAWL-EXTRACT",
        "TOOL-BROWSER-USE-RESEARCH",
        "TOOL-POSTGRES-QUERY-READONLY",
    ]
    for tool_id in research_tools:
        require(tool_status.get(tool_id) == "planned",
                f"{tool_id} unexpectedly changed; require explicit tool qualification/review")

    agent = load_yaml(agent_path)
    require(set(agent.get("inputs", {}).get("required", [])) == {"research_question", "target_market"},
            "A001 required inputs do not match SK001 contract")
    require("research.completed" in agent.get("outputs", {}).get("downstream_events", []),
            "A001 output event declaration missing")

    output_schema_path = ROOT / "Chats/ChatGPT/Multi Agent AIOS/agents/market-research/output.schema.json"
    with output_schema_path.open(encoding="utf-8") as handle:
        output_schema = json.load(handle)
    schema_required = set(output_schema.get("required", []))
    agent_required = set(agent.get("outputs", {}).get("required_fields", []))
    require(schema_required == agent_required,
            f"A001 agent output fields and JSON Schema differ: schema_only={sorted(schema_required - agent_required)}, agent_only={sorted(agent_required - schema_required)}")
    required_evidence_fields = {
        "schema_version", "research_question", "scope", "findings", "evidence",
        "implications", "assumptions", "contradictions", "gaps", "confidence",
        "researched_at", "limitations", "review_required",
    }
    require(required_evidence_fields.issubset(schema_required),
            f"A001 evidence-pack contract missing fields: {sorted(required_evidence_fields - schema_required)}")

    status = load_yaml(status_path)
    require(status.get("runtime_verified") is False, "A001 must remain runtime_unverified until evidence exists")

    with (ROOT / workflow_path).open(encoding="utf-8") as handle:
        workflow = json.load(handle)
    require(workflow.get("active") is False, "A001 n8n workflow must remain inactive until runtime approval")
    normalize_node = next((node for node in workflow.get("nodes", []) if node.get("id") == "a001-normalize"), None)
    require(normalize_node is not None, "A001 normalization node missing")
    code = normalize_node.get("parameters", {}).get("jsCode", "")
    for token in [
        "market.research.requested",
        "event_version !== '1.0'",
        "company_id",
        "correlation_id",
        "envelope.metadata",
        "payload.research_question",
        "payload.target_market",
        "runtime_invoked: false",
        "validated_pending_runtime",
    ]:
        require(token in code, f"A001 trigger code missing expected guard/token: {token}")

    print(
        "A001/SK001 static contract checks passed: "
        f"{len(cases)} fixtures, {len(event_records)} draft event contracts, "
        f"{len(research_tools)} intentionally planned tools. Runtime remains unverified."
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"A001/SK001 contract validation FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
