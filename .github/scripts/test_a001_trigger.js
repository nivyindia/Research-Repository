#!/usr/bin/env node
"use strict";

// Executes the exact JavaScript code stored in the A001 n8n Code node.
// This tests the normalization/validation boundary only, not the n8n server
// or the actual A001 agent runtime.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "../..");
const workflowPath = path.join(
  root,
  "Chats/ChatGPT/Multi Agent AIOS/08-infrastructure/n8n/workflows/A001-market-research-trigger.json"
);
const workflow = JSON.parse(fs.readFileSync(workflowPath, "utf8"));
const node = workflow.nodes.find((item) => item.id === "a001-normalize");
assert.ok(node, "A001 normalize node must exist");
const runNode = new Function("$json", node.parameters.jsCode);

function validEnvelope(overrides = {}) {
  return {
    event_id: "evt-test-001",
    event_type: "market.research.requested",
    event_version: "1.0",
    occurred_at: "2026-10-11T10:00:00.000Z",
    source: "contract-test",
    company_id: "company-test",
    entity_type: "MarketResearchRequest",
    entity_id: "request-test-001",
    correlation_id: "corr-test-001",
    causation_id: null,
    payload: {
      research_question: "Identify public demand signals",
      target_market: "Example B2B market"
    },
    metadata: {},
    ...overrides
  };
}

function expectReject(name, input, expectedMessage) {
  assert.throws(
    () => runNode(input),
    (error) => {
      assert.match(String(error.message), /A001 contract validation failed:/, name);
      assert.match(String(error.message), expectedMessage, name);
      return true;
    },
    name
  );
}

const accepted = runNode(validEnvelope());
assert.equal(accepted.length, 1);
assert.equal(accepted[0].json.status, "validated_pending_runtime");
assert.equal(accepted[0].json.runtime_invoked, false);
assert.equal(accepted[0].json.event_id, "evt-test-001");
assert.equal(accepted[0].json.input.research_question, "Identify public demand signals");
assert.equal(accepted[0].json.input.target_market, "Example B2B market");

expectReject("wrong event type", validEnvelope({ event_type: "research.completed" }), /event_type/);
expectReject("wrong event version", validEnvelope({ event_version: "2.0" }), /event_version/);
expectReject("missing event id", validEnvelope({ event_id: "" }), /event_id/);
expectReject("invalid timestamp", validEnvelope({ occurred_at: "not-a-date" }), /occurred_at/);
expectReject("missing metadata", validEnvelope({ metadata: null }), /metadata/);
expectReject("missing research question", validEnvelope({ payload: { target_market: "Example" } }), /research_question/);
expectReject("missing target market", validEnvelope({ payload: { research_question: "Estimate demand" } }), /target_market/);
expectReject("invalid source policy", validEnvelope({ payload: { research_question: "Q", target_market: "M", source_policy: [] } }), /source_policy/);
expectReject("invalid competitor set", validEnvelope({ payload: { research_question: "Q", target_market: "M", competitor_set: "not-an-array" } }), /competitor_set/);
expectReject("missing company id", validEnvelope({ company_id: " " }), /company_id/);

console.log("A001 trigger contract tests passed: 1 valid envelope and 10 negative cases. Runtime remains unverified.");
