# Company Standardization — Working Specification

**Status:** Working specification — not yet canonical  
**Purpose:** Preserve the Company Standardization requirements discussed in ChatGPT and use them as the audit baseline before changing Company OS V7.

## 1. Standardization Scope

The Company OS should standardize:

- Company master information
- Organization, departments, divisions and brands
- Roles, ownership, responsibilities and authority
- Goals, plans, projects, tasks and daily work
- Processes, SOPs and work instructions
- Policies, standards and controls
- Documents, records, reports, templates and meeting notes
- Naming, classification, metadata, versioning and lifecycle
- Governance, approvals, decisions, exceptions and change management
- Employees, roles, responsibilities, work allocation and performance
- KPIs, reporting, dashboards and review cycles
- Customers, vendors, partners and other business entities
- Products/services and commercial operations
- Sales, marketing, CRM and customer-success operations
- HR/talent and employee lifecycle
- Finance/accounting and financial controls
- Technology, data, AI and automation
- Risk, compliance, legal, security and quality
- Projects/resources/archive
- Knowledge management and navigation
- External-system integrations
- Master data and canonical sources

## 2. Core Object Relationship

The standard operating model should support:

**Company → Department → Role → Employee → Responsibility → Goal → Plan → Project → Task → Work → Output → KPI → Report → Review → Decision → Change → Record**

Related business objects such as customer, vendor, product/service, process, document, system, AI agent and external integration should connect to the appropriate objects above.

## 3. Standardization Principle

**REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING**

Existing Company OS V7 structures must be reused where they already satisfy the requirement. Do not create a parallel standardization system.

## 4. Implementation Rule

Before modifying canonical Company OS standards:

1. Compare V5, V6, V7 and Final-v7.
2. Verify actual governance documents and repository structure.
3. Identify duplicate, conflicting and superseded definitions.
4. Validate metadata, lifecycle and GitHub automation against implementation.
5. Build the final gap matrix.
6. Apply only verified gap fixes.
7. Run an end-to-end validation.

## 5. Canonical Destination

The intended canonical standards layer is:

`Company-OS-v7/Company-OS/03_RESOURCES/Company_Master_Standards/`

This working specification remains in the V7 audit workspace until the audit determines which parts should become canonical standards.

## 6. Related Audit Files

- `Company_Standardization_Audit.md`
- `Company_Standardization_Audit_Progress.md`

**Important:** This file records the requirements discussed during the current standardization effort. It is not itself the final Company Standardization standard.
