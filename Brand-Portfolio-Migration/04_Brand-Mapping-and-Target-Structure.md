# Brand Mapping and Target Structure

## Brand boundaries

### Nivy Next
Technology, AI, website development, web applications, mobile applications and software development.

### Nivy Crafts
Graphic design, brand identity design as a creative service, video editing, motion graphics and creative production.

### Nivy Hype
Social media management, paid advertising, Google Ads, Meta Ads, PPC, campaign management and performance marketing.

### Nivy Ops
Virtual assistance, administrative support, remote support, CRM administration, lead research, data management and business operations delivered as client services.

## Shared assets
Use a root-level `Shared-Brand-Assets/` for canonical cross-brand material:
- Master company information
- Master brand/identity governance (where company-wide)
- Legal/compliance templates
- Shared testimonials/portfolio evidence where usage rights permit
- Common sales and proposal templates
- Common operating templates and cross-brand references

Brand-specific logo/identity, service claims, prices, offers and service pages remain in their respective brand areas.

## Proposed folder layout (apply selectively after inventory)

```text
Research-Repository/
├── Brand-Portfolio-Migration/
│   ├── README.md
│   ├── 01_Migration-Plan.md
│   ├── 02_Master-Tracker.md
│   ├── 03_Inventory-and-Audit.md
│   ├── 04_Brand-Mapping-and-Target-Structure.md
│   └── 05_Migration-Safety-Rules.md
├── Shared-Brand-Assets/
│   ├── 00_Master-Brand-Guidelines/
│   ├── 01_Company-Information/
│   ├── 02_Legal-and-Compliance/
│   ├── 03_Shared-Portfolio-and-Proof/
│   ├── 04_Common-Sales-Assets/
│   ├── 05_Common-Templates/
│   ├── 06_Shared-Tools-and-Resources/
│   └── 07_Cross-Brand-References/
├── Nivy Next/
│   ├── 00_Project-Management/
│   ├── 01_Brand-Identity/
│   ├── 02_Company-Profile/
│   ├── 03_Services-and-Catalog/
│   ├── 04_Pricing-and-Packages/
│   ├── 05_Sales-and-Business-Development/
│   ├── 06_Portfolio-and-Proof/
│   ├── 07_Website-and-Landing-Pages/
│   ├── 08_SEO-GEO-AEO/
│   ├── 09_Online-Presence/
│   ├── 10_Marketing-and-Content/
│   ├── 11_Operations-and-Delivery/
│   └── 12_Research-and-References/
├── Nivy Crafts/  (same shared top-level pattern; creative service subfolders)
├── Nivy Hype/    (same shared top-level pattern; marketing service subfolders)
└── Nivy Ops/     (same shared top-level pattern; operations service subfolders)
```

## Brand-specific service subfolders
- **Nivy Next:** AI-and-Automation, Website-Development, Web-Applications, Mobile-App-Development, Software-Development.
- **Nivy Crafts:** Graphic-Design, Brand-Identity-Design, Video-Editing, Motion-Graphics, Video-Production, Creative-Production.
- **Nivy Hype:** Social-Media-Management, Paid-Advertising, Google-Ads, Meta-Ads, PPC, Performance-Marketing, Campaign-Management.
- **Nivy Ops:** Virtual-Assistance, Administrative-Support, Remote-Support, CRM-Administration, Lead-Research, Data-Management, Business-Operations.

## Destination mapping examples (proposals only)
| Asset | Proposed destination | Condition |
|---|---|---|
| Brand-specific guidelines | Brand folder / `01_Brand-Identity/` | Verify brand and canonical version |
| Master company profile | `Shared-Brand-Assets/01_Company-Information/` | Keep brand-specific profile variants in each brand |
| Service catalog and one-pager | Brand folder / `03_Services-and-Catalog/` | Split mixed-brand source only after review |
| Approved price list and packages | Brand folder / `04_Pricing-and-Packages/` | Confirm approval and effective date |
| Sales pitch, proposal and outreach | Brand folder / `05_Sales-and-Business-Development/` | Keep common templates in Shared assets |
| Case study and work samples | Brand folder / `06_Portfolio-and-Proof/` | Confirm ownership, permission and brand relevance |
| Website copy and landing pages | Brand folder / `07_Website-and-Landing-Pages/` | Map each page to one service/intent |
| Keyword research and SEO plan | Brand folder / `08_SEO-GEO-AEO/` | Preserve research provenance |
| Social/business profiles | Brand folder / `09_Online-Presence/` | Shared account governance stays shared |
| Content calendars and campaigns | Brand folder / `10_Marketing-and-Content/` | Separate service brand and campaign scope |
| Client delivery SOPs | Brand folder / `11_Operations-and-Delivery/` | Company-wide SOPs remain shared |
| Third-party research/frameworks | Existing research area; link/reference from brand | Do not re-home source material unnecessarily |

This structure is a target proposal, not an instruction to create every subfolder immediately. Apply only where inventory shows a real need.
