# Company Standardization — Gap Matrix

**Scope:** Company OS V7 after relocation to `Company OS/Company-OS-v7/`
**Audit date:** 2026-10-03
**Principle:** REUSE → ADAPT → INTEGRATE → BUILD ONLY WHAT IS MISSING

## Confirmed baseline
V7 already provides the canonical standards layer at:
`Company-OS-v7/Company-OS/03_RESOURCES/Company_Master_Standards/`

A parallel Company Standardization architecture is not required.

## Gap matrix

| ID | Area | Current state | Gap | Priority | Planned action |
|---|---|---|---|---|---|
| G01 | Implementation state | Governance Doc 09 describes planned edits while some tracker items are marked complete | Actual state and tracker are inconsistent | P0 | Reconcile against actual files; mark only verified completion |
| G02 | Canonical version | V7 is now at canonical research location, but historical V5/V6/Final-v7 lineage is not yet reconciled | Superseded/snapshot status needs explicit record | P0 | Inventory historical versions and create version disposition matrix |
| G03 | Master-data/object model | Registries exist for departments, document types, ownership, etc. | No verified single cross-object model covering company→goal→work→KPI→decision→change | P0 | Define canonical object/relationship registry only after searching V7/research for an equivalent |
| G04 | Goals/plans/work | Projects and task architecture exist | Goal→plan→project→task→daily work/output linkage is not yet proven canonical | P1 | Document relationship model and minimum required IDs/links |
| G05 | People/roles/work | Org chart, ownership and department structures exist | Employee→role→responsibility→work allocation linkage needs canonical definition | P1 | Add/confirm Role, Responsibility and Work Allocation master definitions |
| G06 | KPI/reporting | Dashboard and reporting automation exist | KPI→report→dashboard→review relationship is not yet canonical | P1 | Define KPI registry and reporting relationship if absent |
| G07 | Decisions/changes/exceptions | Governance mechanisms exist | Enterprise-wide Decision, Change, Exception and Evidence records are not fully standardized | P1 | Define record types, metadata and linkage rules |
| G08 | Business entities | Wider OS research covers customers/vendors/products/services | Canonical master-data ownership and IDs are not verified in V7 | P1 | Audit CRM/customer/vendor/product/service master sources before adding anything |
| G09 | Integrations | GitHub automation is documented and partly implemented | CRM/HR/Finance/AI/external-system integration contracts are not centralized in Company Master Standards | P1 | Create integration registry only for verified systems and canonical data flows |
| G10 | Metadata enforcement | Confidentiality is implemented in validate-metadata.yml | Other metadata/lifecycle rules need end-to-end verification against all workflows | P1 | Test metadata + naming + lifecycle automation with representative documents |
| G11 | Lifecycle | Rules and automation exist | Archive/deprecation and supersession are not fully end-to-end verified | P1 | Run lifecycle test: Draft→Review→Approved→Published→Retired/Archive |
| G12 | Automation map | 10 automation workflows are present/documented | Map claims need file-by-file verification, especially deprecated/scaffolded workflows | P1 | Reconcile Doc 10 with actual workflow behavior |
| G13 | Navigation | Doc 06 contains corrected path model in text | Need to verify the actual Doc 06 file is the corrected/applied version | P1 | Verify and reconcile Doc 06 |
| G14 | Governance Doc 04/06/07 changes | Doc 09 says planned changes were not applied; Doc 07 currently says FINAL and references applied Doc 04 changes | Documentation status conflict | P0 | Treat actual files as authority; update change plan/status after verification |
| G15 | Duplicate/snapshot content | Historical Company OS versions/task lists existed in Claude archive | Duplicate/superseded copies can cause conflicting authority | P1 | Produce disposition: canonical / historical / archive / duplicate; do not delete without evidence |
| G16 | External publication | publish-sync is scaffolded | Target Wiki/Notion API details are missing | P2 | Keep scaffold; configure only when target is selected |

## Definition of done
All P0/P1 gaps have either an existing canonical V7 source with verified implementation, or one canonical new definition with owner, metadata, lifecycle, relationships and validation coverage.
