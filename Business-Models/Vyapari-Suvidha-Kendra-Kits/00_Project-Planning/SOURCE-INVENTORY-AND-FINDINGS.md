# Source Inventory and Initial Findings / स्रोत सूची और प्रारंभिक निष्कर्ष

**तारीख / Date:** 2026-10-20  
**दायरा / Scope:** GitHub `main` branch पर उपलब्ध तीन स्रोत फ़ोल्डरों का path-level inventory, Git blob identity comparison और प्रारंभिक privacy/quality triage।  
**सीमा / Limitation:** इस रिपोर्ट में file names, sizes, Git blob SHAs और folder structure जाँचे गए हैं। DOCX/XLSX/PDF-जैसी binary सामग्री का पूरा पाठ इस connector से extract नहीं हो पाया; इसलिए commercial facts, prices, contract clauses या training correctness को content-verified/approved नहीं माना गया है।

## 1. Executive findings / मुख्य निष्कर्ष

- **पार्टनर किट / Partner kit:** 23 DOCX files सूचीबद्ध हैं; सभी का Git blob SHA एक ही है (`746d8fa1d7b9600619b671b44a886b8ed30f6f38`) और प्रत्येक का आकार 6,480 bytes है। इसका अर्थ है कि Git में ये 23 files byte-for-byte identical हैं, जबकि filenames अलग-अलग विषय दर्शाते हैं। इन्हें अभी अलग-अलग वास्तविक सामग्री के रूप में स्वीकार न करें।
- **डिस्ट्रीब्यूटर किट / Distributor kit:** 11 DOCX files सूचीबद्ध हैं; सभी का वही blob SHA (`746d8fa1d7b9600619b671b44a886b8ed30f6f38`) और आकार 6,480 bytes है। इसलिए distributor के 11 अलग नाम वाले दस्तावेज़ भी एक-दूसरे के समान binary content हैं।
- **कुल समान-content जोखिम / Shared-content risk:** Partner और Distributor मिलाकर 34 अलग नाम वाली DOCX files एक ही blob हैं। यह P0 quality blocker है; original files से वास्तविक सामग्री दोबारा export/upload करके verify करना आवश्यक है।
- **Training folder:** 148 files और 12 directories मिले। इनमें 122 JPG, 6 JPEG, 8 DOCX, 9 XLSX, 2 TXT और 1 PSD हैं। `12a.jpg` और `Catalog.jpg` एक ही blob SHA share करते हैं।
- **गोपनीयता जोखिम / Privacy risk:** `Training Test/Test 2/Sample Documents/` के भीतर filenames में Aadhaar, PAN, bank statement और electricity bill जैसे पहचान/वित्तीय दस्तावेज़ दर्शाए गए हैं। इनकी वास्तविक सामग्री और redaction status अभी verify नहीं है। चूँकि repository content सार्वजनिक रूप से fetch हो रहा है, इन sample files को संभावित संवेदनशील डेटा मानकर P0 review करें; इन्हें partner-facing kit में copy न करें।
- **Approval स्थिति / Approval status:** इस inventory से कोई pricing, commission, payout, service availability, legal term या marketing promise approved नहीं होता।

## 2. Source summary / स्रोतों का सार

| स्रोत फ़ोल्डर / Source folder | Files / फ़ाइलें | Directories / फ़ोल्डर | प्रारंभिक स्थिति / Initial status |
|---|---:|---:|---|
| `Nivy_Partner_Welcome_Kit_2026` | 23 | 10 | P0 — 23/23 DOCX same blob; contents need replacement/verification / 23/23 DOCX एक जैसे; पुनः जाँच आवश्यक |
| `Nivy_Distributor_Field_Meeting_Kit` | 11 | 4 | P0 — 11/11 DOCX same blob; contents need replacement/verification / 11/11 DOCX एक जैसे; पुनः जाँच आवश्यक |
| `Training` | 148 | 12 | P0 privacy triage + content review needed / privacy triage और content review आवश्यक |
| **कुल / Total** | **182** | **26** | **Inventory done; content audit partial / inventory पूरा; content audit आंशिक** |

## 3. Priority actions / प्राथमिक कार्रवाई

1. **P0 — संवेदनशील sample documents / Sensitive sample documents:** GitHub पर `Training Test/Test 2/Sample Documents/` की access/privacy समीक्षा करें। यदि वास्तविक व्यक्तियों के पहचान या बैंक दस्तावेज़ हैं, तो उन्हें public repository से हटाने/गोपनीय सुरक्षित स्थान पर ले जाने और repository history exposure का आकलन करने की तत्काल कार्रवाई करें। यह रिपोर्ट किसी file को delete नहीं करती।
2. **P0 — DOCX source integrity / DOCX की वास्तविकता:** Partner और Distributor के सभी 34 DOCX filenames को source-of-truth originals से दोबारा मिलाएँ। सही binary content, filename mapping, version और approval प्रमाणित होने तक इन्हें placeholder/invalid-source risk मानें।
3. **P0 — Commercial source verification / व्यावसायिक स्रोत सत्यापन:** `Training Docs/Franchise Price List.xlsx`, `Training Docs/Price List 1.3.xlsx`, `Training Docs/Pitch.xlsx`, `Training Docs/CA Catalogue/Excel Catalog.xlsx` और `Catalogue 1.52.docx` की actual sheets/text पढ़कर version/effective date/source/approval तुलना करें। केवल filename से price या commission चुनना निषिद्ध है।
4. **P1 — Training test samples / प्रशिक्षण test samples:** training tests और Mujeeb submission में personal data हो सकता है; reuse से पहले privacy, purpose, consent, redaction और access check करें।
5. **P1 — Coverage mapping / coverage mapping:** प्रत्येक उपयोगी source file को `FILE-OUTLINE-REGISTER.md` की संबंधित row से जोड़ें; missing/conflicting/outdated/approved status तभी दें जब file content पढ़ा गया हो।

## 4. Detailed file inventory / विस्तृत फ़ाइल सूची

**नोट / Note:** `Git blob SHA` Git में content identity दिखाता है। एक SHA वाली अलग paths वाली files का stored content identical होता है। File path technical identifier है; descriptive status हिंदी पहले, फिर English में है।

| स्रोत / Source | मूल path / Original path | आकार (bytes) / Size | Git blob SHA | प्रारंभिक स्थिति / Initial status |
|---|---|---:|---|---|
| Nivy_Partner_Welcome_Kit_2026 | `01_Onboarding_and_Identity/01_Welcome_Letter_and_Escalation_Matrix_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `01_Onboarding_and_Identity/02_Authorized_Partner_Certificate_Template_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `01_Onboarding_and_Identity/03_Partner_Handbook_and_SOP_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `02_CRM_and_Prospecting_Tools/Cold_Outreach_Calling_Script_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `02_CRM_and_Prospecting_Tools/Google_Maps_Lead_Extraction_Guide_SOP_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `03_Message_Bank_and_Communication/Festival_Greetings_Templates/Festival_Wish_Text_Messages_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `03_Message_Bank_and_Communication/Important_Tax_Alerts_and_Due_Dates_Calendar_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `03_Message_Bank_and_Communication/Value_Addition_Tax_Tips_List_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `03_Message_Bank_and_Communication/WhatsApp_FollowUp_and_Conversion_Scripts_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `04_Print_Ready_Branding_Material/Brand_Style_Guide_and_Printing_Specifications_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `04_Print_Ready_Branding_Material/Client_Inquiry_and_Receipt_Forms/Client_Document_Acknowledgement_Receipt_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `04_Print_Ready_Branding_Material/Client_Inquiry_and_Receipt_Forms/Physical_Client_Inquiry_Form_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `04_Print_Ready_Branding_Material/Visiting_Cards_and_Letterheads/Official_Letterhead_A4_Format_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `05_Sales_Collateral_and_Checklists/Client_Document_Checklists/Checklist_Company_Incorporation_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `05_Sales_Collateral_and_Checklists/Client_Document_Checklists/Checklist_GST_Registration_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `05_Sales_Collateral_and_Checklists/Client_Document_Checklists/Checklist_ITR_Filing_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `05_Sales_Collateral_and_Checklists/Master_Service_Catalog_and_Pricing_Sheet_2026_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `05_Sales_Collateral_and_Checklists/Nivy_Tax_and_IT_Services_Pitch_Deck_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `05_Sales_Collateral_and_Checklists/Objection_Handling_and_FAQ_Guide_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `05_Sales_Collateral_and_Checklists/Service_One_Pagers/01_GST_Registration_and_Filing_Overview_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `05_Sales_Collateral_and_Checklists/Service_One_Pagers/02_Income_Tax_Return_Guide_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `05_Sales_Collateral_and_Checklists/Service_One_Pagers/03_Company_Incorporation_and_MCA_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Partner_Welcome_Kit_2026 | `05_Sales_Collateral_and_Checklists/Service_One_Pagers/04_Statutory_Audit_and_Accounting_Services_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `01_Pitch_and_Presentation/Nivy_Partner_Program_Pitch_Deck_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `01_Pitch_and_Presentation/Partner_Earning_Calculator_Overview_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `01_Pitch_and_Presentation/Revenue_Sharing_and_Commission_Structure_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `02_Legal_and_Onboarding_Forms/Draft_Franchise_Partner_Agreement_Specimen_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `02_Legal_and_Onboarding_Forms/Non_Disclosure_Agreement_Draft_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `02_Legal_and_Onboarding_Forms/Partner_KYC_and_Application_Form_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `03_Work_Portfolio_and_Proof_of_Work/Company_Profile_and_Client_Testimonials_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `03_Work_Portfolio_and_Proof_of_Work/Sample_Client_Audit_Report_Masked_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `03_Work_Portfolio_and_Proof_of_Work/Sample_GST_and_Income_Tax_Filing_Proof_Masked_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `04_Meeting_Collaterals/Agency_Services_Summary_Brochure_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Nivy_Distributor_Field_Meeting_Kit | `04_Meeting_Collaterals/Physical_Meeting_Discussion_Checklist_v1.0.docx` | 6480 | `746d8fa1d7b9600619b671b44a886b8ed30f6f38` | समान blob: विषय-वस्तु अलग होने की पुष्टि नहीं / Identical blob: distinct content not verified |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/12A permanent.jpg` | 127929 | `feadd3463061277bec9e34f88d089a925e044be5` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/12A prov.jpg` | 127137 | `e617a94ee64a43e84ef74f843e14d47df73f7bd6` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/12a.jpg` | 102635 | `35cd53a01413234598d9f69124de654fc169bf6a` | समान blob duplicate pair / Identical-blob duplicate pair |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Add director.jpg` | 175678 | `416d20ec7ef69d75b7804b0a6293ff0c15e4526c` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/CLosing comp.jpg` | 129448 | `169d9cfa30009206993fc34dad59c6a7020a2a05` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/CSR withour DSC.jpg` | 159860 | `717e69ab9870d1bb9dfcae077f2535585ad80b37` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/CSR.jpg` | 2074529 | `2a11a845daf024ab62bc51c3da2200970cde5c12` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/CSR1.jpg` | 119944 | `f13fadaeb59f26403a4c14273ed34254de10d4dc` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Catalog.jpg` | 102635 | `35cd53a01413234598d9f69124de654fc169bf6a` | समान blob duplicate pair / Identical-blob duplicate pair |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Central ex.jpg` | 1341584 | `82cbc3260b11fb76bd1f06bf3c7ff9e19199cbe2` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/DIN Reg.jpg` | 1195684 | `033a098548e6745f119a57a6cf81f2d9b9934caa` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/DIR3KYC.jpg` | 153806 | `86a336e294e601e42dff8080a9205f8b966a5299` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/DSC comb.jpg` | 2151005 | `f756f48d8227fc1fe97d9d11658f7d946debe312` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/DSSC.jpg` | 2120383 | `d99a02ed5277bdf010a10ead3e353d8d5f074ca3` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Data Set 1.jpg` | 139881 | `9f795fcd4cf109ab961087d4b70d4ebac6b05e9c` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Data Set 2.jpg` | 143051 | `2ce195f0b6197ae08a47f6def3418e11af26be4a` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Data Set 3.jpg` | 149166 | `d2a1c73b6366ad16c5c92c1a02fbb3bfac6a6fe4` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Distributorship.jpg` | 2134623 | `1efa12b2bafe1c6672e238c92cb54849083812f4` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/E anudaan.jpg` | 122273 | `0e39e2e79603077088175083ab066b1e27aba61b` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/EPFOESIC.jpg` | 112998 | `3be1022b8960f094dbcfb0691eb4dbca451d91a7` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/ESIC2.jpg` | 117889 | `945a0c6c962621e558d724cea7d0ef9baf0b0c32` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Eanudaan.jpg` | 2079959 | `6990c3a9172a63f60a6f05efd60e7303d97cab51` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Eway.jpg` | 1227439 | `b05a1b20002e3a457bb5ae98c26d5e1b4ca75ed5` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/FCRA 2.jpg` | 160683 | `d8b1685608d3762e30c21860bdacfda9f4514835` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/FCRA.jpg` | 2071977 | `fb513646a7dc068227af36797401b17bc90b911c` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/FRANCHISE.jpg` | 2124056 | `d4b498fc570e6cdb7ce6516fb40dea15557df500` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/FSSAI Basic.jpg` | 129449 | `15b489c38b6ea8abc4ddaf0c5b9a45416dc0306a` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/FSSAI Renewal.jpg` | 156639 | `36c9e1c7c841ec51ff1f503515f1c2259ca13233` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/FSSAI State.jpg` | 130271 | `6a888b2b7b8dd1613be342cd867042ed05f5c0bc` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/FSSAI central.jpg` | 171870 | `09bb53439e5c41db2d02620740e0d04eeb8f9cce` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/FSSAI.jpg` | 112990 | `a112445464e39604e50427f5dba7b8ab7e17684b` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Farmer Producer 2.jpg` | 116625 | `37a363e6dd4827850a6b3653445dcf4e5062e3f8` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/GEM PORTAL.jpg` | 117471 | `037755fe55f34d9e9cf6c9057fe171d14b9744e9` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/GST 150.jpg` | 147371 | `16bbd7b83a5ffd52e7a9f4a6cf68bec6a45446fc` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/GST FILING.jpg` | 96273 | `4121717bef08207e098dbc600f40f976eb165360` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/GST Nil.jpg` | 142848 | `83ae2f6c9ba450720a8b1e56e7024dbcfd74b308` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/GST REG.jpg` | 99898 | `a044aa80344ca89194b0aaf827031fe2baab904e` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/GST Reg2.jpg` | 120494 | `6857ae672de06dd8b36e8aca9ff7e063c4b2e94f` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/IEC 2.jpg` | 176058 | `3579f6611a87592fee3fdd7dc2578f97c0a69e3b` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/IEC.jpg` | 111944 | `007734bea8df7e64260b90a3d763e45d980d2ee4` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/ISO.jpg` | 2093691 | `c66b80a5c09b1e9c7d1ba7a657bf0ce4407d718e` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/ITR Business 1 cr.jpg` | 140220 | `374053601c494259370aa4fe414501e1c8de932b` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/ITR Business 10 -50jpg.jpg` | 143004 | `f1b60e100f58dfa3307bd0b405e739169ae75464` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/ITR Business 10 lac.jpg` | 143654 | `cde2a2b91b9ba7aade7705ecca3a9c74a84b60fb` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/ITR.jpg` | 99510 | `e55ba738b2665f50954def3cf80b83b2d85cfcc0` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Inc Auth Capital.jpg` | 136061 | `45cb5bd7442fc9e6d09d0eff7e7f0b3c571fa77f` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/LLP reg.jpg` | 155644 | `b330ed5489ec0143a7b61683854452706eb2db9a` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/LLP.jpg` | 98739 | `7e642f0bf42fb40094748a53e4b196988e4eb74c` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/MSME.jpg` | 123240 | `37dc5b7eb50339f2052d0ec2c148bdd2bb91adfb` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/NBFC.jpg` | 1303839 | `2c081c23fa922011363ccaa9ae8b0ef0fe5c6150` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Name chng.jpg` | 1235673 | `2dbc172318dc4fcf3934b31e6a93554d6670f409` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Nidhi.jpg` | 171821 | `131b8d59385b7d88df2e3ee9996182fd039fadcd` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Niti AYOg 2.jpg` | 128690 | `7d5a34c8c5a2909e4d1aef5c79c60746ff68ea1d` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/OPC Reg.jpg` | 131051 | `a7e6145be60a04155d3a58cf4e2e4ade92ffa112` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/OPC.jpg` | 121156 | `7ac3dd9dda6487666fe0a86b764065185b65b8c4` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/PUblic Ltd 2.jpg` | 128978 | `10c49e23dcd40a823c9994ea98b42c944b13b95c` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Private LTd.jpg` | 129403 | `cb5ff4a64a0bdcda40b5ecd2c0da97177f3c7bb1` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Pvt Ltd.jpg` | 124994 | `d0a60f0e5b24d05978d1f149e17d6e5982fbaf8b` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/SECT  8.jpg` | 116982 | `fa67da1f7618a97e57292ff297f3708c9f2cbee8` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/SHOP ESTABLISHMENT.jpg` | 110710 | `c01283b7bfd25aad897e82bbc20f8338566aac5c` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Sample.psd` | 2147886 | `d49db43543535146dfdaa19108c4ac9e7ad82716` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Share transfer.jpg` | 124379 | `db79c694f0d34984f558645b7976a95600e5b7a4` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Soc.jpg` | 2085101 | `9db434728c5991b30e6271ce808a6c0652f74d05` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/TM.jpg` | 104769 | `50710dcf820f4772889c06a769bdb082a3c70836` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/TM.txt` | 130150 | `a4da62600a9dd5f1cc8fae7132e8fa0929fadb8d` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Trademark Reg.jpg` | 129037 | `f16a9afce09ca3205e6e35f05ce5587db21a4a8e` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Type 15-50.jpg` | 145821 | `01979f2b7a2b8ea4c04938b77f5568070d06ae78` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Type16.jpg` | 181953 | `ded79f0b8bb97555b002fc4a3c9441217cb6cf1f` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Type22.jpg` | 1202676 | `32eab7c2c6695cec055212660ea26b05ab18f3bc` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Type4-2.jpg` | 141351 | `49fb01bf4fac80b08fe21e08d3457b5341d1585e` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Type4.jpg` | 134314 | `05f4d6a696524a1a0fe44833779293c30ca681c4` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Type5 1-15.jpg` | 144712 | `2b6bfdaa29fb5726e716592aa7b8706eea5438c8` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/Type5 100.jpg` | 147479 | `cf54d1d4ef2e9e52a1c8d932c77a6c825fda75be` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/annual audit.jpg` | 125048 | `fdedbdfbe2026dda049ae1cf7195f19011cac278` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/aoa chng.jpg` | 1195069 | `38d7d3ac44806b40d98d34e66ad92c03b1fbcc1a` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/comp to regu_ar.jpg` | 126123 | `5aa1dafc1ef93e1f06307660e4635207051bed4a` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/cppp.jpg` | 128050 | `d858e9ddbc99db90f26b63dd1779939f75043f10` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/dgft dsc.jpg` | 123671 | `dc3d8f12928a139d318d16c2d95971dbd77d0f0f` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/dpiit seed fund.jpg` | 139531 | `14e415e5f8872a880374ea9f1dea4bc09a2b9065` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/dpiit tax.jpg` | 140874 | `4002dc8ca1adc1e952632ef569a2eeacce4691d1` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/dpiit.jpg` | 135337 | `5e3b18fa6a5feba18d7654e74932468985037627` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/dsc combo.jpg` | 132635 | `e54594df91cb27961256a869e64cca817cdb27e7` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/dsc.jpg` | 120475 | `46888f1ede9c9fc9598b06a9b840c1807abf8ec2` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/epfo return 0.jpg` | 1015754 | `2562a96007dca9ffa1b6360b3488d66447ead038` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/epfo return 20+.jpg` | 178284 | `481380d7df7c9ce96176d132cdc099b785df02e4` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/epfo return 20.jpg` | 1051287 | `124a74dd682084ede7e39b3ff22d2e073c849bda` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/farmer producer.jpg` | 1237453 | `909ffe2bd3438ebf59c99fdd18408771e045e795` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gem.jpg` | 134473 | `ef1db14db458bfbc6a1263e53d2a8c08b93a1c2b` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst 1-15 bill.jpg` | 1215431 | `bf73700b6b1c965f8f072be290fb7c45244eb058` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst audit.jpg` | 138143 | `35718d0f80811b29ae3c3b6ca2d5a9bbb9db1955` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst cancel compl.jpg` | 141286 | `1e98a9081d657d3fe91ef08d72dcb96406111679` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst cancel.jpg` | 139881 | `c5bc2516cbf53112210f1be2c16a1905001be36b` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst core field.jpg` | 120888 | `d860c6e59d49b5ba662cc0275b7613419e48f43e` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst msme.jpg` | 125352 | `10c2e0e9b1e649eff92ebf5d8513806df3e703ef` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst nil filing.jpg` | 1234507 | `3f984be55ba4657cdb132ae2f71276ea34e289a5` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst non core field.jpg` | 118969 | `33a1e61f0bc2e32b1cd2201d46e4dc5b2b284da0` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst refund 5 cr.jpg` | 144305 | `472499e3004f612bf1470ebcb972d849ad6b6017` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst refund.jpg` | 141850 | `78a1b3615e706c54c952ba62ccb8635445db4af7` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst register.jpg` | 1202676 | `bb8a5aa2e4067175e19b5808312f4bc8a83cbc99` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/gst revocation.jpg` | 1018347 | `e9f4a2cb95ff920aabe1c5fc5472015cd943fcaf` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/itr above 50.jpg` | 1304571 | `411b2b24f7b7d061c1026f9432ddf53bb8326772` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/itr indi.jpg` | 1293188 | `6aaa981c602dc432a1a0c34af80285a9f9fd30d1` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/itr ini 10-50.jpg` | 1285721 | `cf4d718476b9b7cef3a47637a12c0ff007561e08` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/micro fin.jpg` | 1231877 | `03b428362ac4cbddf16d2760f79fbe86d5b49eae` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/moa change.jpg` | 113489 | `458b5b19305dbf37b5600b4b21e153ea8817f6fd` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/moa chng.jpg` | 1197189 | `66fd1e65325fff527d11b6fd723835201964cada` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/niti.jpg` | 2075983 | `50e32b34e546c60fcdd3ce458fcd2d9c19f8862d` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/office chng outsde city.jpg` | 130445 | `f4c52b5581a2748f1ccd454f70f885eda0ba87c6` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/office chng.jpg` | 129432 | `1121060a293e4a756524ec07b4afd72942269e7d` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/org dsc.jpg` | 128250 | `99cb2ffb4c2b31e9dd1be428ca0e02c7db97d2db` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/pan.jpg` | 134128 | `9fa64cd6b25bf65da7e18608263b1b4095e653c3` | P0 गोपनीयता जाँच / P0 privacy review; sensitive data possible |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/partnership.jpg` | 120821 | `ac50318417816cbdd54d7cb645a5d392d3df815e` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/prjct business.jpg` | 139482 | `174f2a4ead419a3c1d2d4a0bdbf6d1e9ecae9634` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/project for individual.jpg` | 139578 | `53765ac15d890f56edd27ebd11eacf37410d7a02` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/project loan.jpg` | 142636 | `59c3b1a8d44e2d63fa201c27acba32fbfff8fbd6` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/public ltd.jpg` | 120018 | `130fa9b1999183073c1d899a710ec293d7038305` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/shop act.jpg` | 119406 | `480a0d89d54882963f98fcde3e6f8ebee6e49b3e` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/st.jpg` | 2086428 | `49ec1c7d839e0d69ff61100ed65a1c948e0b391e` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/startup inda.jpg` | 138520 | `705a3e46c2bb4990b9206e4334b58c3873cf0d06` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/tan.jpg` | 133931 | `05ace82606e33663e2a62957378d7b59557df733` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/tds.jpg` | 133813 | `268f0f2e50d33551d6013e1efb48fa09f51649f6` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalog PIcs/trust.jpg` | 2075258 | `0d57f848d9b6126de469522ddad23ae2f4391073` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/CA Catalogue/Catalogue 1.52.docx` | 51578 | `fea1e7add1c2aae2d7d4252b67b537d6fa948b46` | P0 commercial content/version/approval verify / commercial content/version/approval जाँचें |
| Training | `Training Docs/CA Catalogue/Excel Catalog.xlsx` | 23833 | `329655b7e5fc825699281ce752d9e9e7f844880d` | P0 commercial content/version/approval verify / commercial content/version/approval जाँचें |
| Training | `Training Docs/CA Catalogue/Logo red bg 12.jpg` | 642899 | `b64b02c758d4619378da96cd5f1af097052259d2` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Docs/Franchise Price List.xlsx` | 183407 | `98734a60c9e1062ff4383f27247236a6f1c0ab73` | P0 commercial content/version/approval verify / commercial content/version/approval जाँचें |
| Training | `Training Docs/Pitch.xlsx` | 20077 | `42fb369a0d80cfd1a117c4e03c2bb27b9c31d50c` | P0 commercial content/version/approval verify / commercial content/version/approval जाँचें |
| Training | `Training Docs/Price List 1.3.xlsx` | 196253 | `5d095fb3668c274cce5bfc6bffbc78155e3d9aab` | P0 commercial content/version/approval verify / commercial content/version/approval जाँचें |
| Training | `Training Test/Test 1/CRM Sheet.xlsx` | 14003 | `34f806c425387ea405c37435f3b9b15048e0d2a2` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test 1/FAQ test.docx` | 8584 | `91c712897dc57eefa933c107393b9ddec99c7f6a` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test 1/Test Overview.txt` | 101 | `8bc97918e72461bd5c643a309981627fbf271a68` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test 2/A- Name Verification.docx` | 11051 | `72ee64f316279cafc6c7091d51dae112b80eee29` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test 2/B - Doc Verification Test.docx` | 410887 | `907ca999b4761d05064c3645f6ea2d1e3ee0ab3e` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test 2/C- Prepare Excel using this Format.xlsx` | 24678 | `31545103917d32c18149bf63100e5b464b50bc7d` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test 2/D- Prepare Docs Using this format.docx` | 316639 | `a6e2de5697945ac4dd92522d4acd98e89b696eed` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test 2/Sample Documents/Company/Elec bill.jpeg` | 95439 | `e07e5d8e8802bdc80790d6eacd00f42a7509de48` | P0 गोपनीयता जाँच / P0 privacy review; sensitive data possible |
| Training | `Training Test/Test 2/Sample Documents/Director 1/Adhr.jpeg` | 38147 | `8a0c1d0ff6c9af7d0b9e10ea229c5a6607f73435` | P0 गोपनीयता जाँच / P0 privacy review; sensitive data possible |
| Training | `Training Test/Test 2/Sample Documents/Director 1/Bnk St Director 1.jpeg` | 49348 | `33fa28392d1c585cf128654aa6c1e8ce7a814e3d` | P0 गोपनीयता जाँच / P0 privacy review; sensitive data possible |
| Training | `Training Test/Test 2/Sample Documents/Director 1/PAN.jpg` | 89166 | `8f4dc10f754a8e1462e2a05ca1386d4c2d49b968` | P0 गोपनीयता जाँच / P0 privacy review; sensitive data possible |
| Training | `Training Test/Test 2/Sample Documents/Director 2/Adhar.jpeg` | 163897 | `879410209bf6a7b65273928d876abc660590394d` | P0 गोपनीयता जाँच / P0 privacy review; sensitive data possible |
| Training | `Training Test/Test 2/Sample Documents/Director 2/Bank ST Dir2.jpeg` | 32122 | `79e36e1331952ae440375f4c90812113b91c013a` | P0 गोपनीयता जाँच / P0 privacy review; sensitive data possible |
| Training | `Training Test/Test 2/Sample Documents/Director 2/PAN.jpeg` | 29565 | `a11a074c7a8433d224b1461b8dbc4e48ec732d59` | P0 गोपनीयता जाँच / P0 privacy review; sensitive data possible |
| Training | `Training Test/Test Submission/Mujeeb/A- Name Verification.docx` | 12399 | `a19b670b7dc14388f15b406d50b25080ea9c3510` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test Submission/Mujeeb/B - Doc Verification Test.docx` | 411253 | `ad8bd56ae23fa25e9c5b3592fb74c6716e91bca5` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test Submission/Mujeeb/C- Prepare Excel using this Format.xlsx` | 13366 | `d8d91b43e948b2b9900f17337705dd2f5080f091` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test Submission/Mujeeb/CRM Sheet.xlsx` | 14370 | `d43d1606ce2c66426f52c0255d1b6e55efea536b` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test Submission/Mujeeb/D- Prepare Docs Using this format.docx` | 28427 | `5f065bd57f880ce4ebf6de3933cb251b73333c0b` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |
| Training | `Training Test/Test Submission/Mujeeb/Vinamra.xlsx` | 14455 | `3868334b247efaa2ff9493b96880ca6f3c879dc6` | पाठ सामग्री अभी extract नहीं हुई / Content not yet extracted |

## 5. Acceptance criteria to close audit / audit पूरा करने की शर्तें

- हर DOCX/XLSX की वास्तविक content पढ़ी गई हो और exact source/version दर्ज हो। / Actual content of every DOCX/XLSX is inspected and exact source/version recorded.
- Duplicate files को hash और content comparison से अलग-अलग classify किया गया हो। / Duplicate files are classified using hash and content comparison.
- Prices, commission, incentives, settlement, third-party fees और service availability के लिए approved source, effective date और approver दर्ज हों। / Approved source, effective date and approver are recorded for commercial claims.
- सभी identity/customer sample files redacted हों या restricted secure storage में रखे जाएँ; GitHub में sensitive data न हो। / Identity/customer samples are redacted or stored securely; no sensitive data remains in GitHub.
- Source-to-outline coverage, gaps/conflicts, migration decisions और final bilingual quality gate अपडेट हों। / Source-to-outline coverage, gaps/conflicts, migration decisions and bilingual quality gate are updated.

## 6. Change log / बदलाव का रिकॉर्ड

| तारीख / Date | बदलाव / Change | कारण / Reason |
|---|---|---|
| 2026-10-20 | तीन GitHub source folders का recursive file inventory और blob identity check जोड़ा / Added recursive inventory and blob identity checks for three GitHub source folders | Source folders are now accessible on GitHub main / स्रोत फ़ोल्डर GitHub main पर उपलब्ध हैं |
