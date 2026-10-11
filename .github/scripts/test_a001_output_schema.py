#!/usr/bin/env python3
"""Positive and negative tests for the A001 evidence-pack JSON Schema."""
from pathlib import Path
import json
import sys

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = ROOT / "Chats/ChatGPT/Multi Agent AIOS/agents/market-research/output.schema.json"


def sample_report():
    return {
        "schema_version": "1.0",
        "research_question": "Assess example market demand",
        "scope": {"target_market": "Example B2B market", "geography": "United States"},
        "findings": [{
            "finding_id": "F-001",
            "claim": "A sourced demand signal exists",
            "claim_type": "fact",
            "evidence_grade": "B",
            "confidence": "medium",
            "as_of_date": "2026-10-11",
            "evidence_refs": ["E-001"]
        }],
        "evidence": [{
            "evidence_id": "E-001",
            "source_title": "Example source",
            "canonical_url": "https://example.com/research",
            "publisher": "Example Publisher",
            "publication_date": "2026-10-01",
            "accessed_at": "2026-10-11T10:00:00Z",
            "source_type": "official_publication",
            "summary": "Source summary supporting F-001",
            "supports": ["F-001"]
        }],
        "implications": [{
            "implication": "Validate demand with customer interviews",
            "finding_refs": ["F-001"],
            "caveats": ["One source is not sufficient for a market-size estimate"]
        }],
        "assumptions": [{
            "assumption_id": "ASM-001",
            "statement": "The target segment buys this service",
            "reason": "Initial hypothesis to validate",
            "owner": "research_operations",
            "confidence": "low",
            "validation_action": "Interview target customers"
        }],
        "contradictions": [],
        "gaps": [{
            "unknown": "Willingness to pay",
            "materiality": "high",
            "next_action": "Conduct price interviews"
        }],
        "confidence": {"level": "medium", "rationale": "Limited evidence; further validation is required"},
        "researched_at": "2026-10-11T10:00:00Z",
        "limitations": ["Example test fixture, not real market research"],
        "review_required": True
    }


def validate_cross_references(report):
    finding_ids = {item.get("finding_id") for item in report.get("findings", [])}
    evidence_ids = {item.get("evidence_id") for item in report.get("evidence", [])}
    problems = []
    for finding in report.get("findings", []):
        for evidence_id in finding.get("evidence_refs", []):
            if evidence_id not in evidence_ids:
                problems.append(f"finding {finding.get('finding_id')} references unknown evidence {evidence_id}")
    for evidence in report.get("evidence", []):
        for finding_id in evidence.get("supports", []):
            if finding_id not in finding_ids:
                problems.append(f"evidence {evidence.get('evidence_id')} supports unknown finding {finding_id}")
    if problems:
        raise ValueError("; ".join(problems))


def main():
    with SCHEMA_PATH.open(encoding="utf-8") as handle:
        schema = json.load(handle)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    valid = sample_report()
    errors = list(validator.iter_errors(valid))
    if errors:
        raise AssertionError("valid sample rejected: " + "; ".join(error.message for error in errors))
    validate_cross_references(valid)

    cases = []
    missing_evidence = sample_report()
    missing_evidence["findings"][0]["evidence_refs"] = []
    cases.append(("finding without evidence reference", missing_evidence))

    invalid_confidence = sample_report()
    invalid_confidence["confidence"]["level"] = "certain"
    cases.append(("invalid confidence", invalid_confidence))

    bad_timestamp = sample_report()
    bad_timestamp["researched_at"] = "not-a-date"
    cases.append(("invalid researched_at timestamp", bad_timestamp))

    missing_assumptions = sample_report()
    del missing_assumptions["assumptions"]
    cases.append(("missing assumptions section", missing_assumptions))

    unexpected_field = sample_report()
    unexpected_field["unreviewed_claims"] = ["unexpected"]
    cases.append(("unexpected top-level field", unexpected_field))

    for name, candidate in cases:
        errors = list(validator.iter_errors(candidate))
        if not errors:
            raise AssertionError(f"invalid sample unexpectedly accepted: {name}")

    bad_finding_ref = sample_report()
    bad_finding_ref["findings"][0]["evidence_refs"] = ["E-DOES-NOT-EXIST"]
    try:
        validate_cross_references(bad_finding_ref)
    except ValueError:
        pass
    else:
        raise AssertionError("unknown evidence reference was not rejected")

    bad_support_ref = sample_report()
    bad_support_ref["evidence"][0]["supports"] = ["F-DOES-NOT-EXIST"]
    try:
        validate_cross_references(bad_support_ref)
    except ValueError:
        pass
    else:
        raise AssertionError("unknown finding support reference was not rejected")

    print(f"A001 output schema tests passed: 1 valid sample, {len(cases)} schema-negative cases, and 2 referential-integrity cases.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"A001 output schema tests FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
