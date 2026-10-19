# Next Work Plan — Continue Without Deferred Audits / अगली कार्ययोजना — स्थगित जाँचों के बिना आगे बढ़ना

## 1. Scope decisions for this work batch / इस कार्य-चरण के दायरे के निर्णय

**हिंदी:** उपयोगकर्ता के निर्देश के अनुसार `Catalogue 1.52.docx` को अभी नवीनतम catalogue reference माना जाएगा। यह निर्देश version selection के लिए है; इससे catalogue की पूरी सामग्री, approval, service availability या किसी commercial term की स्वतंत्र पुष्टि नहीं होती।

**English:** Per the user's instruction, `Catalogue 1.52.docx` will be treated as the latest catalogue reference for now. This is a version-selection instruction; it does not independently verify the full content, approval, service availability, or any commercial term in the catalogue.

**हिंदी:** सभी prices, commissions, shares, earnings, fees और price comparisons इस कार्य-चरण से बाहर रहेंगे। किसी draft, example, pitch या table में राशि नहीं जोड़ी जाएगी। जहाँ ऐसी जानकारी आवश्यक हो, वहाँ `[COMMERCIAL REVIEW — DEFERRED]` placeholder रहेगा।

**English:** All prices, commissions, shares, earnings, fees, and price comparisons are excluded from this work batch. No monetary amounts will be added to drafts, examples, pitches, or tables. Where this information is needed, use the placeholder `[COMMERCIAL REVIEW — DEFERRED]`.

**हिंदी:** 34 समान DOCX files की जाँच और Training sample files की privacy/access जाँच को अलग workstream के लिए स्थगित रखा जाएगा। उन files को अभी verified source नहीं माना जाएगा, न उन्हें final deliverables में copy किया जाएगा।

**English:** The investigation of the 34 identical DOCX files and the privacy/access review of Training sample files are deferred to a separate workstream. Those files will not be treated as verified sources or copied into final deliverables for now.

## 2. Work that can continue now / जो काम अभी आगे बढ़ सकता है

| क्रम / No. | काम / Work | अभी क्या बनेगा / Output now | सीमा / Boundary |
|---|---|---|---|
| 1 | Outline-to-source mapping / Outline और sources का मिलान | Filename/path आधारित प्रारंभिक mapping matrix / Preliminary mapping matrix based on filenames and paths | Content verified नहीं माना जाएगा / Not content-verified |
| 2 | Partner customer journey / Partner की customer journey | Inquiry → needs discovery → document checklist → case logging → fulfilment handoff → status update → closure / पूछताछ से case closure तक workflow | Exact KYC, service eligibility और turnaround पर placeholders / Placeholders for exact KYC, eligibility, and turnaround |
| 3 | Distributor field workflow / Distributor field workflow | Prospecting → first meeting → needs qualification → approved catalogue introduction → follow-up → onboarding handoff / Prospect से onboarding handoff तक workflow | कोई unverified earning, lead, territory या support promise नहीं / No unverified earnings, lead, territory, or support promises |
| 4 | Sales and communication assets / बिक्री और communication सामग्री | Discovery questions, meeting checklist, neutral follow-up scripts, objection logging / सवाल, meeting checklist, follow-up scripts, objection log | Price/commission answers deferred / Price और commission वाले उत्तर स्थगित |
| 5 | Operations and quality / संचालन और गुणवत्ता | Case register fields, document-receipt acknowledgement structure, complaint/escalation log, daily/weekly reporting templates / Case register, acknowledgement, complaint log, reporting templates | Data minimization; real personal data GitHub में नहीं / Minimize data; no real personal data in GitHub |
| 6 | Training framework / Training ढाँचा | Role-wise learning path, SOP index, competency checklist, knowledge-check outline / Role-wise learning path और competency checklist | Training sample files को copy किए बिना / Without copying Training sample files |
| 7 | Long-format drafts / विस्तृत guides | Partner Master Guide और Distributor Field Playbook के non-commercial sections / दोनों guides के non-commercial sections | Unverified facts visibly marked `[VERIFY]` / Unverified facts visibly marked |
| 8 | Short booklets / संक्षिप्त booklets | Long guides review के बाद concise 8–10 / 9–12 page drafts / Review के बाद संक्षिप्त drafts | Final print approval अभी नहीं / Not approved for final print |

## 3. Execution sequence / काम का क्रम

1. **हिंदी:** File Outline Register के हर requirement को workstream, expected output और source-confidence label से जोड़ें।  
   **English:** Map each File Outline Register requirement to a workstream, expected output, and source-confidence label.

2. **हिंदी:** पहले non-commercial workflows और reusable templates तैयार करें; हर unknown fact पर `[VERIFY]` या `[OWNER CONFIRMATION]` लिखें।  
   **English:** Build non-commercial workflows and reusable templates first; mark every unknown fact with `[VERIFY]` or `[OWNER CONFIRMATION]`.

3. **हिंदी:** Partner और Distributor के लिए अलग-अलग role-specific long guides बनाएँ; साझा प्रक्रिया को common reference में रखें।  
   **English:** Build separate role-specific long guides for Partners and Distributors; keep shared processes in a common reference.

4. **हिंदी:** Drafts को source links और decision IDs से जोड़ें, ताकि बाद में source audit के बाद बदलाव traceable रहें।  
   **English:** Link drafts to source paths and decision IDs so changes remain traceable after the later source audit.

5. **हिंदी:** Long guides के consistency review के बाद ही short offline booklets तैयार करें।  
   **English:** Prepare short offline booklets only after reviewing the long guides for consistency.

6. **हिंदी:** अंत में स्थगित audit workstream खोलें: DOCX integrity, privacy/access, और commercial verification अलग-अलग।  
   **English:** Open the deferred audit workstreams at the end: DOCX integrity, privacy/access, and commercial verification separately.

## 4. Source confidence labels / स्रोत-विश्वसनीयता के labels

- **Filename-only / केवल filename:** केवल file name/path से विषय का अनुमान; content की पुष्टि नहीं।
- **Drafted framework / प्रारूप तैयार:** प्रक्रिया का ढाँचा है, पर policy/source approval नहीं।
- **Source-backed / source से समर्थित:** पढ़े गए source में स्पष्ट प्रमाण उपलब्ध।
- **Owner-confirmed / owner द्वारा पुष्ट:** अधिकृत owner ने लिखित पुष्टि दी।
- **Approved for release / जारी करने हेतु approved:** आवश्यक factual, operational, commercial, privacy और bilingual gates पूरे।

## 5. Do not do in this batch / इस चरण में ये काम नहीं करने हैं

- Prices, fees, commission, shares, income projections या break-even amounts न भरें।
- 34 identical DOCX files को अलग-अलग valid documents मानकर reuse न करें।
- Potential identity/financial sample documents को copy, quote या publish न करें।
- Lead supply, marketing support, territory exclusivity, guaranteed earnings, service turnaround या legal compliance का दावा बिना प्रमाण न करें।
- Draft को approved या print-ready न कहें।

## 6. Completion criteria for this batch / इस चरण के पूरा होने की शर्तें

**हिंदी:** इस batch को तब पूरा माना जाएगा जब preliminary mapping matrix तैयार हो, non-commercial workflows और templates का पहला draft बन जाए, दोनों long guides के non-commercial sections भर जाएँ, unknowns log हो जाएँ और Progress Tracker अपडेट हो जाए। इससे final approval या release स्वतः नहीं मिलेगा।

**English:** This batch is complete when the preliminary mapping matrix exists, first drafts of non-commercial workflows and templates are created, non-commercial sections of both long guides are drafted, unknowns are logged, and the Progress Tracker is updated. This does not automatically grant final approval or release.
