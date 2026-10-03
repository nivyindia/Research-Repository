# Draw.io Standard — Nivy Company Visual System

## Canonical format
- File format: .drawio
- Editable source is canonical.
- PNG/PDF exports are presentation derivatives, never the source of truth.

## Naming
Use: NIVY-[DOMAIN]-[SUBJECT].drawio

Examples:
- NIVY-COMPANY-MASTER-MAP.drawio
- NIVY-GOAL-CASCADE.drawio
- NIVY-AIOS-ARCHITECTURE.drawio

## Page structure
Each Draw.io file should normally use pages/tabs for 01-MASTER, 02-DETAIL, 03-FLOW when needed, and 04-REFERENCE when needed.

## Visual semantics
- Rounded rectangle = entity / role / system
- Rectangle = process / task / activity
- Diamond = decision
- Document shape = artifact / evidence / SOP
- Cylinder = data store
- Cloud = external system/service
- Arrow = relationship or flow
- Dashed arrow = dependency/reference
- Boundary/container = department, system or domain

## Relationship semantics
Label important arrows with verbs such as owns, reports to, depends on, creates, receives, transforms, approves, executes, measures, reviews, escalates and archives.

## Hierarchy semantics
Goal hierarchy:
Vision → Strategy → Annual Goal → Quarterly Goal → Monthly Target → Weekly Objective → Daily Priority → Task → Output → KPI

Operational hierarchy:
Department → Function → Role → Responsibility → SOP → Task → Evidence → Review

Technology/data hierarchy:
Source → Raw Data → Processed Data → Knowledge → Operational System → Agent/Human → Action → Result → Evidence

## Source/provenance
Each master diagram should contain a small SOURCE / CONTROL area with canonical source paths, last reviewed date, diagram status, owner, and related diagrams.

## Stable IDs
Use stable semantic IDs where practical, for example ORG-COMPANY, ORG-DEPT-SALES, GOAL-COMPANY-ANNUAL, PLAN-Q1, PROJECT-..., TASK-..., SYS-CRM, SYS-GITHUB, SYS-NOTION.

## Quality rules
- Prefer one clear relationship over many crossing arrows.
- Use containers to show ownership boundaries.
- Keep master diagrams high-level; move detail to child diagrams.
- Every child diagram identifies its parent map.
- Never encode credentials, tokens, passwords or private secrets.
- Keep terms synchronized with canonical repository terminology.

## Change control
Proposed change → source check → edit → Draw.io validation → visual review → tracker update → commit

## Completion definition
A Draw.io file is not DONE merely because it exists. It must open correctly, represent the intended model, pass terminology/source reconciliation, and have tracker evidence recorded.
