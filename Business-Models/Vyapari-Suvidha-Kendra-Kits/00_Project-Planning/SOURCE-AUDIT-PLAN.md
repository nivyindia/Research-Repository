# Source Audit and Migration Plan / स्रोत जाँच और माइग्रेशन योजना

## 1. Audit status and access blocker / जाँच की स्थिति और पहुँच में बाधा

**हिंदी:** 2026-10-20 को Google Drive तक पहुँच की उपलब्धता जाँची गई। Browser tabs की सूची में `Nivy_Partner_Welcome_Kit_2026` नाम का Google Drive folder tab दिखा, लेकिन Drive tab पढ़ने का प्रयास browser connection error के कारण विफल रहा। Google Drive connector खोजने पर वह administrator द्वारा disabled और installation के लिए unavailable दिखा। इसलिए अभी Drive की कोई भी फ़ाइल खोले बिना उसका content audit करना संभव नहीं हुआ। यह source audit शुरू करने का प्रयास है, पूर्ण audit नहीं।

**English:** On 2026-10-20, Google Drive access was checked. The browser tab list showed a Google Drive folder tab titled `Nivy_Partner_Welcome_Kit_2026`, but reading the Drive tab failed because of a browser connection error. The Google Drive connector appeared disabled by the administrator and unavailable for installation. Therefore, the contents of Drive files could not yet be inspected. This records an attempted access check, not a completed source audit.

**अगला आवश्यक कदम / Required next step:** कृपया तीनों source folders की फ़ाइलें यहाँ upload करें (अधिमानतः ZIP सहित subfolders), या Google Drive/browser connection को फिर से उपलब्ध कराएँ। जब तक source files पढ़ने योग्य नहीं होंगी, file-by-file mapping और content extraction नहीं की जा सकती।

**Next step:** Upload the files from all three source folders here (preferably as ZIPs preserving subfolders), or restore usable Google Drive/browser access. File-by-file mapping and content extraction cannot proceed until the source files are readable.

## 2. Sources to inspect / जाँच के स्रोत
1. Google Drive — Partner Welcome Kit folder / पार्टनर स्वागत किट फ़ोल्डर।
2. Google Drive — Distributor Field Kit folder / डिस्ट्रीब्यूटर फील्ड किट फ़ोल्डर।
3. Google Drive — Training Folder / प्रशिक्षण फ़ोल्डर।
4. Referenced approved service catalogue, pricing/commission sheet, agreements, onboarding/KYC checklist, SOPs, support/marketing policy and brand assets / संदर्भित स्वीकृत सेवा सूची, मूल्य/कमीशन शीट, समझौते, onboarding/KYC checklist, SOP, support/marketing policy और brand assets।
5. Relevant files already present in the GitHub kit structure / GitHub kit structure में पहले से मौजूद संबंधित फ़ाइलें।

## 3. Inventory fields / फ़ाइल सूची के आवश्यक fields
For every source file, record / हर source file के लिए दर्ज करें:
- Unique audit ID / विशिष्ट audit ID।
- Exact source folder and original path/link / मूल फ़ोल्डर और path/link।
- Original file name and file type / मूल नाम और file type।
- Created/modified date and version, if available / उपलब्ध होने पर creation/modification date और version।
- Owner/author/approver, if known / ज्ञात होने पर owner/author/approver।
- Audience: Retailer/Franchisee, Distributor, both or internal-only / पाठक-वर्ग।
- Topic and matching File Outline Register row / विषय और संबंधित outline row।
- Status: approved, draft, outdated, unknown, duplicate, conflicting, restricted or irrelevant / स्थिति।
- Key facts and exact page/section/source location / मुख्य तथ्य और सटीक page/section।
- Proposed and final destination / प्रस्तावित और अंतिम destination।
- Migration status/date / migration स्थिति और तारीख।
- Gaps, conflicts, follow-up owner/action / कमी, विरोधाभास, जिम्मेदार व्यक्ति और अगली कार्रवाई।

## 4. Audit workflow / जाँच की प्रक्रिया
1. List every file and subfolder in each source folder / हर source folder और subfolder की पूरी सूची बनाएँ।
2. Inspect the content of relevant files; do not rely on filenames alone / केवल filenames पर निर्भर न रहें; content पढ़ें।
3. Preserve source names, paths and version metadata / मूल नाम, paths और version metadata सुरक्षित रखें।
4. Map each file to one or more File Outline Register rows / हर file को एक या अधिक outline rows से जोड़ें।
5. Compare duplicate files and versions before selecting a canonical copy / canonical copy चुनने से पहले duplicates और versions की तुलना करें।
6. Flag conflicts in services, prices, commissions, incentives, settlement, document requirements, support promises and company facts / सेवाओं, कीमतों, कमीशन, incentives, settlement, documents, support promises और company facts के विरोधाभास दर्ज करें।
7. Separate source statements from assumptions and current policy / source statements, assumptions और current policy अलग रखें।
8. Propose a destination for each useful file / हर उपयोगी file का destination तय करें।
9. Do not delete or overwrite original sources during migration / migration में मूल स्रोत delete या overwrite न करें।
10. Record exclusions and reasons; archive superseded GitHub copies with links where appropriate / बाहर रखी सामग्री और कारण दर्ज करें; आवश्यकतानुसार पुराने GitHub versions archive करें।
11. Update the Progress Tracker and Decisions Log after each batch / हर batch के बाद tracker और decisions log अपडेट करें।
12. Verify every resulting file follows Hindi-first bilingual format / हर तैयार file में पहले देवनागरी हिंदी और उसके बाद English अनुवाद जाँचें।

## 5. Coverage labels / coverage स्थिति
- **Existing — verified / मौजूद — सत्यापित:** current/approved source clearly covers the requirement / वर्तमान स्वीकृत source requirement पूरा करता है।
- **Partial / आंशिक:** some details exist, but gaps remain / कुछ जानकारी है, लेकिन कमी बाकी है।
- **Missing / अनुपलब्ध:** no supporting source found / supporting source नहीं मिला।
- **Conflict / विरोधाभास:** sources disagree / sources में अंतर है।
- **Outdated / पुराना:** superseded or beyond effective date / superseded या effective date से बाहर।
- **Needs confirmation / पुष्टि आवश्यक:** authority/currentness unclear / authority या currentness स्पष्ट नहीं।
- **Not applicable / लागू नहीं:** requirement does not apply and reason is recorded / कारण सहित लागू नहीं।

## 6. Priority / प्राथमिकता
- **P0 — release blocker / जारी करने से रोकने वाली:** prices, commissions, statutory/third-party charges, settlement, lead/marketing promises, legal terms, service availability / कीमतें, कमीशन, शुल्क, settlement, leads/marketing promises, legal terms, service availability।
- **P1 — operational critical / संचालन के लिए अत्यावश्यक:** onboarding, documents, fulfilment SOP, payment workflow, complaints/escalations, customer communication / onboarding, documents, SOP, payment, complaints और customer communication।
- **P2 — enablement / सक्षम बनाने वाली सामग्री:** training, scripts, collateral, CRM, reporting, competitor research / training, scripts, collateral, CRM, reporting, competitor research।
- **P3 — polish / अंतिम सुधार:** layout, styling and supplementary examples / layout, styling और अतिरिक्त examples।

## 7. Migration safety / माइग्रेशन सुरक्षा
- Keep a source-to-destination map / source-to-destination map रखें।
- A copied file is not automatically approved / file copy अपने आप approval नहीं है।
- Do not put completed KYC/customer data, identity scans, passwords or sensitive personal data in GitHub / completed KYC, customer data, identity scans, passwords या sensitive personal data GitHub में न रखें।
- Redact personal/customer information before extracting reusable templates / reusable templates बनाने से पहले personal/customer information हटाएँ।
- Preserve historical versions where policies/commercial terms changed / policy या commercial terms बदलने पर historical versions रखें।
- Mark unverified documents; never silently merge conflicting terms / unverified documents चिह्नित करें; विरोधी terms को चुपचाप merge न करें।
- Obtain authorized confirmation for the canonical commercial source / canonical commercial source की अधिकृत पुष्टि लें।

## 8. Required audit outputs / जाँच के deliverables
1. Source Inventory Register / स्रोत फ़ाइलों की सूची।
2. Outline-to-Source Coverage Matrix / outline और source का mapping।
3. Duplicate and Conflict Register / duplicate और विरोधाभास रजिस्टर।
4. Missing Information and Decision List / अनुपलब्ध जानकारी और निर्णय सूची।
5. Migration Log / migration log।
6. Updated Progress Tracker / अपडेटेड प्रगति ट्रैकर।
7. Bilingual quality check for each deliverable / हर deliverable की द्विभाषी गुणवत्ता जाँच।
