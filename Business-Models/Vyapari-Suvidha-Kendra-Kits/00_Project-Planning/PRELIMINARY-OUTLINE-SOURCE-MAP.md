# Preliminary Outline-to-Source Map / प्रारंभिक outline-to-source mapping

**हिंदी:** यह mapping केवल उपलब्ध GitHub file paths और filenames पर आधारित है। जहाँ source का actual text नहीं पढ़ा गया है, वहाँ coverage को verified नहीं माना गया है। यह mapping planning aid है, approval record नहीं।

**English:** This mapping is based only on available GitHub file paths and filenames. Where actual source text has not been read, coverage is not verified. This is a planning aid, not an approval record.

## Mapping register / मैपिंग रजिस्टर

| Outline area / Outline क्षेत्र | Candidate source path(s) / संभावित source path | Preliminary coverage / प्रारंभिक coverage | Next action / अगली कार्रवाई |
|---|---|---|---|
| Service catalogue / सेवा सूची | `Training Docs/CA Catalogue/Catalogue 1.52.docx` | Latest reference designated by user; content not yet reviewed / उपयोगकर्ता ने latest reference बताया; content review बाकी | Extract service names, scope, eligibility and document requirements later; exclude all prices for now / बाद में service names, scope, eligibility और documents निकालें; अभी prices शामिल न करें |
| Catalogue spreadsheet / Catalogue spreadsheet | `Training Docs/CA Catalogue/Excel Catalog.xlsx` | Filename-only; not selected as latest / केवल filename से जानकारी; latest के रूप में selected नहीं | Compare only in deferred source audit / केवल स्थगित source audit में तुलना |
| Price/commercial spreadsheets / Price और commercial spreadsheets | `Training Docs/Franchise Price List.xlsx`; `Training Docs/Price List 1.3.xlsx`; `Training Docs/Pitch.xlsx` | Explicitly deferred / स्पष्ट रूप से स्थगित | Do not extract or use monetary amounts in this work batch / इस batch में राशि extract या उपयोग न करें |
| Partner identity/onboarding / Partner पहचान और onboarding | `Nivy_Partner_Welcome_Kit_2026/01_Onboarding_and_Identity/` | Path-level candidate only; DOCX integrity issue applies / केवल path-level candidate; DOCX integrity issue लागू | Do not rely on DOCX contents until the separate integrity review / अलग integrity review तक DOCX content पर निर्भर न हों |
| Partner prospecting and CRM / Partner prospecting और CRM | `Nivy_Partner_Welcome_Kit_2026/02_CRM_and_Prospecting_Tools/` | Path-level candidate only / केवल path-level candidate | Build neutral workflow templates independently; reconcile later / अभी neutral workflow templates बनाएँ; बाद में मिलान करें |
| Partner messages / Partner संदेश | `Nivy_Partner_Welcome_Kit_2026/03_Message_Bank_and_Communication/` | Path-level candidate only / केवल path-level candidate | Reuse only after source-integrity review / source-integrity review के बाद ही reuse करें |
| Partner sales collateral / Partner sales सामग्री | `Nivy_Partner_Welcome_Kit_2026/05_Sales_Collateral_and_Checklists/` | Path-level candidate only / केवल path-level candidate | Map checklists, one-pagers and FAQ by filename; validate content later / filenames के आधार पर map करें; content बाद में verify करें |
| Distributor field kit / Distributor field kit | `Nivy_Distributor_Field_Meeting_Kit/` | 11 named DOCX files inventory-listed but identical binary content / 11 DOCX inventory में हैं पर binary content समान है | Do not treat as distinct verified content / अलग verified content न मानें |
| Training material / Training सामग्री | `Training/` | 148 files inventoried; content not fully inspected / 148 files सूचीबद्ध; content पूरी तरह inspect नहीं | Use only safe, reviewed materials after separate privacy/integrity checks / अलग privacy/integrity check के बाद ही सुरक्षित सामग्री उपयोग करें |
| Customer operations / Customer संचालन | Existing outline sections: Partner `10_Customer_Service_and_SOPs`, shared support/reporting outlines / मौजूदा outline sections | Requirements defined; authoritative workflow source not yet verified / requirements defined; authoritative workflow source verify नहीं | Draft framework and mark policy-dependent fields `[VERIFY]` / framework draft करें और policy-dependent fields `[VERIFY]` mark करें |
| Distributor recruitment / Distributor recruitment | Existing Distributor outline sections: prospecting, meeting, qualification, follow-up, onboarding / मौजूदा Distributor outline sections | Requirements defined; source evidence pending / requirements defined; source evidence बाकी | Draft field workflow without earnings/support promises / earnings/support promises के बिना field workflow draft करें |

## Confidence rules / confidence के नियम

- **Filename-only / केवल filename:** Path or name suggests relevance; content is not confirmed.
- **Framework drafted / framework तैयार:** A process structure has been drafted; it is not company policy until approved.
- **Source-backed / source से समर्थित:** The source content has been read and directly supports the item.
- **Owner-confirmed / owner द्वारा पुष्ट:** An authorized owner has confirmed the item in writing.
- **Approved for release / जारी करने हेतु approved:** Required factual, operational, commercial, privacy and bilingual checks are complete.

## Explicit exclusions / स्पष्ट रूप से बाहर रखे गए विषय

**हिंदी:** इस mapping में कोई price, fee, commission, share, income projection या break-even राशि शामिल नहीं है। 34 identical DOCX files और संभावित sensitive Training samples को trusted source मानकर उपयोग नहीं किया गया है।

**English:** This map includes no price, fee, commission, share, income projection, or break-even amount. The 34 identical DOCX files and potentially sensitive Training samples have not been used as trusted sources.
