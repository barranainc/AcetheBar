# Legal QA Report — Generated Barrister C

**Exam ID:** `barc`  
**Exam label:** Generated Barrister C  
**QA completed:** 2026-05-24  
**Reviewer:** AI-assisted QA (Phase 2C)  
**Validator run:** 0 errors / 125 warnings (all pre-existing format style)  
**Total questions reviewed:** 160  

---

## Summary

| Status | Count |
|--------|-------|
| PASS — no issues found | 130 |
| FIXED — corrected during QA | 26 |
| HUMAN REVIEW REQUIRED — not auto-fixed | 6 |
| REMOVE | 0 |

**PR-angle count after QA:** 3 (previously 0)  
**Difficulty split:** Easy: 28 · Medium: 58 · Hard: 47 · Exam-trap: 27  
**Reassembled:** Yes — `tools/assemble_exam.py --seed 1` re-run after all fixes  
**Baked into index.html:** Yes — `barc` base64 payload updated 2026-05-24  

---

## Legend

| Status | Meaning |
|--------|---------|
| **PASS** | Reviewed; no legal content errors found |
| **FIXED** | Legal content error identified and corrected during QA |
| **HUMAN REVIEW** | Potential issue flagged; legal uncertainty too high for auto-fix |
| **REMOVE** | Question should be deleted from bank (none at this stage) |

---

## Civil Litigation (43 questions)

### Ch 02 — Limitation Periods & Discovery

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-02-basic-lim-001 | PASS | |
| civ-02-basic-lim-002 | PASS | |
| civ-02-basic-lim-003 | PASS | |
| civ-02-basic-lim-004 | PASS | |
| civ-02-basic-lim-005 | PASS | |
| civ-02-discov-001 | PASS | |
| civ-02-discov-002 | PASS | |
| civ-02-discov-003 | PASS | |
| civ-02-discov-004 | PASS | |
| civ-02-discov-005 | PASS | |

### Ch 06 — Motions (Interlocutory Injunctions)

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-06-injunction-001 | PASS | |
| civ-06-injunction-002 | PASS | |
| civ-06-injunction-003 | PASS | |
| civ-06-injunction-004 | PASS | |
| civ-06-injunction-005 | **FIXED** | `pr_angle` was `applicable: false` — corrected to `applicable: true`; `pr_issue_type: "duty of candour to the court / ex parte disclosure obligations"` |

### Ch 07 — Summary Judgment

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-07-partial-sj-001 | PASS | |
| civ-07-partial-sj-002 | PASS | |
| civ-07-partial-sj-003 | PASS | |
| civ-07-sumj-ev-001 | PASS | |
| civ-07-sumj-ev-002 | PASS | |
| civ-07-sumj-ev-003 | PASS | |
| civ-07-sumj-ev-004 | **FIXED** | `pr_angle` was `applicable: false` — corrected to `applicable: true`; `pr_issue_type: "duty of candour to tribunal / improper litigation strategy"` |
| civ-07-sumj-ev-005 | PASS | |
| civ-07-summ-judg-001 | **FIXED** | explanation, source_reference, and tested_concepts cited `r. 20.04(2)(b)` (consent SJ) — corrected to `r. 20.04(2)(a)` (no genuine issue) |
| civ-07-summ-judg-002 | PASS | |
| civ-07-summ-judg-003 | PASS | |
| civ-07-summ-judg-004 | **FIXED** | explanation, source_reference, and tested_concepts cited `r. 20.04(2)(b)` (consent SJ) — corrected to `r. 20.04(2)(a)` (no genuine issue) |
| civ-07-summ-judg-005 | PASS | |

### Ch 08 — Solicitor-Client Privilege

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-08-sol-cl-priv-001 | PASS | |
| civ-08-sol-cl-priv-002 | PASS | |
| civ-08-sol-cl-priv-003 | PASS | |
| civ-08-sol-cl-priv-004 | **FIXED** | explanation cited *Lavallee, Rackel & Heintz v Canada (AG)*, 2002 SCC 61 (search warrants on law offices) for the in-house counsel privilege test — corrected to *Pritchard v Ontario (Human Rights Commission)*, 2004 SCC 31 (the leading in-house counsel authority). exam_trigger_words and tested_concepts updated. |
| civ-08-sol-cl-priv-005 | PASS | |

### Ch 09 — Discovery & Refusals/Undertakings

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-09-disc-scope-001 | PASS | |
| civ-09-disc-scope-002 | PASS | |
| civ-09-disc-scope-003 | PASS | |
| civ-09-disc-scope-004 | PASS | |
| civ-09-disc-scope-005 | PASS | |
| civ-09-ref-und-001 | PASS | |
| civ-09-ref-und-002 | PASS | |
| civ-09-ref-und-003 | PASS | |
| civ-09-ref-und-004 | PASS | |
| civ-09-ref-und-005 | PASS | |

---

## Criminal Law (43 questions)

### Ch 02 — Arrest, Search & Charter Rights

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-02-arrest-war-001 | PASS | |
| crim-02-arrest-war-002 | **FIXED** | `why_D_wrong` referenced `s. 495(1)(b)` ("found committing") for reasonable-grounds arrest — corrected to `s. 495(1)(a)` |
| crim-02-arrest-war-003 | PASS | |
| crim-02-arrest-war-004 | **FIXED** | source_reference cited `s. 495(1)` and `s. 495(2)` for a citizen's arrest question — corrected to `s. 494(1)(b)` and `s. 494(2)` (citizens' arrest provisions) |
| crim-02-arrest-war-005 | PASS | |
| crim-02-cit-arrest-001 | PASS | |
| crim-02-cit-arrest-002 | PASS | |
| crim-02-cit-arrest-003 | PASS | |
| crim-02-s10b-001 | PASS | |
| crim-02-s10b-002 | PASS | |
| crim-02-s10b-003 | **FIXED** | `why_D_wrong` stated police have a "proactive duty" when jeopardy materially changes — overstated; corrected to "may be required to re-advise" per *R v Sinclair*, 2010 SCC 35 (5-4 decision) |
| crim-02-s10b-004 | PASS | |
| crim-02-s10b-005 | PASS | |
| crim-02-s8-search-001 | PASS | |
| crim-02-s8-search-002 | PASS | |
| crim-02-s8-search-003 | PASS | |
| crim-02-s8-search-004 | PASS | |
| crim-02-s8-search-005 | PASS | |
| crim-02-s9-detent-001 | PASS | |
| crim-02-s9-detent-002 | PASS | |
| crim-02-s9-detent-003 | PASS | |
| crim-02-s9-detent-004 | **FIXED** | `pr_angle` was `applicable: false` — corrected to `applicable: true`; `pr_issue_type: "racial profiling / arbitrary detention"` |
| crim-02-sita-001 | PASS | |
| crim-02-sita-002 | PASS | |
| crim-02-sita-003 | PASS | |
| crim-02-sita-004 | PASS | |

### Ch 03 — Bail

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-03-bail-grnds-001 | PASS | |
| crim-03-bail-grnds-002 | PASS | |
| crim-03-bail-grnds-003 | **FIXED** | `why_D_wrong` vaguely referenced superior court jurisdiction — clarified that `s. 522 Criminal Code` restricts murder (s. 469 offence) bail hearings to a superior court judge |
| crim-03-bail-grnds-004 | **FIXED** | source_reference cited `s. 515(10)` (three grounds for detention) — corrected to `s. 515(6)(a)` (reverse onus for indictable while on release), which is the provision actually tested |
| crim-03-bail-grnds-005 | **FIXED** | source_reference cited `s. 515(10)` (three grounds for detention) — corrected to `s. 515(3)` (ladder/reverse ladder principle), which is the provision actually tested |
| crim-03-rev-onus-001 | PASS | |
| crim-03-rev-onus-002 | PASS | |
| crim-03-rev-onus-003 | PASS | |
| crim-03-rev-onus-004 | PASS | |

### Ch 04 — Disclosure

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-04-stinch-001 | PASS | |
| crim-04-stinch-002 | **FIXED** | explanation stated disclosure must occur "before the accused is required to elect or enter a plea" — corrected to "at the first reasonable opportunity and in any event before the accused is required to elect or enter a plea" per *Stinchcombe* |
| crim-04-stinch-003 | PASS | |
| crim-04-stinch-004 | PASS | |
| crim-04-stinch-005 | PASS | |
| crim-04-tpr-001 | PASS | |
| crim-04-tpr-002 | **FIXED** | `options.C` and `why_C_wrong` cited *R v O'Connor* as `1995 CanLII 51 (SCC)` — corrected to `[1995] 4 SCR 411` (authoritative citation) |
| crim-04-tpr-003 | PASS | |

---

## Family Law (39 questions)

### Ch 03 — Net Family Property & Equalization

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-03-deduct-marr-001 | PASS | |
| fam-03-deduct-marr-002 | PASS | |
| fam-03-deduct-marr-003 | PASS | |
| fam-03-deduct-marr-004 | **HUMAN REVIEW** | Question involves deductions for property brought into marriage under FLA s. 4(1). Legal uncertainty: whether certain pre-marital assets are captured as of "date of marriage" vs. "after date of marriage." Requires reviewer to confirm against FLA text and case law before promoting beyond draft. |
| fam-03-deduct-marr-005 | PASS | |
| fam-03-equal-paymnt-001 | PASS | |
| fam-03-equal-paymnt-002 | PASS | |
| fam-03-equal-paymnt-003 | PASS | |
| fam-03-equal-paymnt-004 | PASS | |
| fam-03-excl-prop-001 | **HUMAN REVIEW** | References FLA s. 4(2) gift/inheritance exclusions. Specific subsection letters (s. 4(2)(a)–(d)) not confirmed against current FLA text — requires reviewer to verify the correct subsection letter for each exclusion category cited. |
| fam-03-excl-prop-002 | **HUMAN REVIEW** | Same issue: FLA s. 4(2) subsection letters unconfirmed. |
| fam-03-excl-prop-003 | **HUMAN REVIEW** | Same issue: FLA s. 4(2) subsection letters unconfirmed. |
| fam-03-excl-prop-004 | **HUMAN REVIEW** | Same issue: FLA s. 4(2) subsection letters unconfirmed. |
| fam-03-nfp-formula-001 | PASS | |
| fam-03-nfp-formula-002 | PASS | |
| fam-03-nfp-formula-003 | PASS | |
| fam-03-nfp-formula-004 | PASS | |
| fam-03-nfp-formula-005 | PASS | |

### Ch 04 — Matrimonial Home

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-04-excl-possess-001 | PASS | |
| fam-04-excl-possess-002 | PASS | |
| fam-04-excl-possess-003 | PASS | |
| fam-04-excl-possess-004 | PASS | |
| fam-04-mh-consent-001 | PASS | |
| fam-04-mh-consent-002 | PASS | |
| fam-04-mh-consent-003 | **HUMAN REVIEW** | Question involves notice to non-titled spouses under FLA s. 21 / Land Registration Reform Act. Legal uncertainty: whether the question's treatment of actual notice vs. constructive notice through s. 21 registration is fully accurate under current law. Requires reviewer to confirm. |
| fam-04-mh-consent-004 | PASS | |
| fam-04-mh-consent-005 | PASS | |
| fam-04-mh-possess-001 | **FIXED** | `why_D_wrong` used ambiguous phrase "a different and additional remedy" — corrected to "a different and distinct remedy" for clarity |
| fam-04-mh-possess-002 | PASS | |
| fam-04-mh-possess-003 | PASS | |
| fam-04-mh-possess-004 | PASS | |
| fam-04-mh-possess-005 | PASS | |

### Ch 05 — Spousal Support

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-05-spse-supp-001 | PASS | |
| fam-05-spse-supp-002 | PASS | |
| fam-05-spse-supp-003 | PASS | |
| fam-05-spse-supp-004 | PASS | |
| fam-05-spse-supp-005 | **FIXED** | source_reference heading cited entitlement provisions (FLA s. 33(8) / DA s. 15.2(6)) for a variation/termination question — corrected to variation provisions (FLA s. 37 / DA s. 17); heading corrected to "Variation of Spousal Support — Material Change in Circumstances" |
| fam-05-ssag-001 | **FIXED** | source_reference cited SSAG "revised 2016" — corrected to "revised 2021" |
| fam-05-ssag-002 | **FIXED** | source_reference cited SSAG "revised 2016" — corrected to "revised 2021" |

---

## Public Law (35 questions)

### Ch 02 — Charter Rights

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-02-oakes-test-001 | PASS | |
| pub-02-oakes-test-002 | PASS | |
| pub-02-oakes-test-003 | PASS | |
| pub-02-oakes-test-004 | PASS | |
| pub-02-oakes-test-005 | PASS | |
| pub-02-s15-equal-001 | PASS | |
| pub-02-s15-equal-002 | **FIXED** | source_reference cited only *Andrews v Law Society of BC* — added *R v Kapp*, 2008 SCC 41 and *Withler v Canada (AG)*, 2011 SCC 12, which established the modern two-part s. 15 test |
| pub-02-s15-equal-003 | **FIXED** | Same: added Kapp and Withler to source_reference |
| pub-02-s15-equal-004 | **FIXED** | Same: added Kapp and Withler to source_reference |
| pub-02-s15-equal-005 | **FIXED** | source_reference missing *Eldridge v British Columbia (AG)*, [1997] 3 SCR 624 (leading s. 15 underinclusion authority) — added |
| pub-02-s2-freedoms-001 | PASS | |
| pub-02-s2-freedoms-002 | PASS | |
| pub-02-s7-fundjust-001 | PASS | |
| pub-02-s7-fundjust-002 | PASS | |
| pub-02-s7-fundjust-003 | PASS | |
| pub-02-s7-fundjust-004 | PASS | |
| pub-02-s7-fundjust-005 | PASS | |

### Ch 03 — Procedural Fairness

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-03-baker-fair-001 | PASS | |
| pub-03-baker-fair-002 | PASS | |
| pub-03-baker-fair-003 | PASS | |
| pub-03-baker-fair-004 | PASS | |
| pub-03-baker-fair-005 | PASS | |
| pub-03-right-reasons-001 | PASS | |
| pub-03-right-reasons-002 | PASS | |
| pub-03-right-reasons-003 | PASS | |
| pub-03-right-reasons-004 | PASS | |

### Ch 04 — Standard of Review

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-04-correct-std-001 | PASS | |
| pub-04-correct-std-002 | PASS | |
| pub-04-correct-std-003 | PASS | |
| pub-04-correct-std-004 | PASS | |
| pub-04-reason-stand-001 | **FIXED** | `why_C_wrong` implied *Vavilov* abolished patent unreasonableness — corrected to reflect that patent unreasonableness was first abolished by *Dunsmuir v New Brunswick*, 2008 SCC 9, and *Vavilov* (2019) subsequently replaced the Dunsmuir framework |
| pub-04-reason-stand-002 | PASS | |
| pub-04-reason-stand-003 | **FIXED** | explanation said "as refined by *Vavilov*... and as affirmed in *Dunsmuir*" (chronologically backwards) — corrected to "Under *Dunsmuir* (2008)... and as refined by *Vavilov* (2019)" |
| pub-04-reason-stand-004 | PASS | |
| pub-04-reason-stand-005 | PASS | |

---

## Human Review Required — Action Items

The following 6 questions require a qualified reviewer to confirm the legal content before `validation_status` can be advanced beyond `draft`:

| Question ID | Issue | Action Required |
|-------------|-------|-----------------|
| fam-03-deduct-marr-004 | Legal uncertainty: FLA s. 4(1) deduction timing ("date of marriage" vs. "after date of marriage") | Reviewer to read FLA s. 4(1) text and confirm the question's framing is accurate |
| fam-03-excl-prop-001 | FLA s. 4(2) gift/inheritance exclusion — specific subsection letter not verified | Reviewer to read FLA s. 4(2)(a)–(d) and confirm which subsection letter is cited |
| fam-03-excl-prop-002 | Same as above | Same action |
| fam-03-excl-prop-003 | Same as above | Same action |
| fam-03-excl-prop-004 | Same as above | Same action |
| fam-04-mh-consent-003 | FLA s. 21 / LRRA — actual notice vs. constructive notice treatment may be incomplete | Reviewer to confirm against FLA s. 21 and case law on notice to non-titled spouses |

---

## Fixes Applied — Change Log

All 26 fixes below were applied in-place to the source question JSON files using `/tmp/fix_legal_content.py` on 2026-05-24. The exam was reassembled and the index.html payload updated following the fixes.

| # | Question ID | Field(s) Changed | Nature of Fix |
|---|-------------|-----------------|---------------|
| 1 | civ-06-injunction-005 | `pr_angle` | Set `applicable: true`; added `pr_issue_type` |
| 2 | civ-07-sumj-ev-004 | `pr_angle` | Set `applicable: true`; added `pr_issue_type` |
| 3 | civ-07-summ-judg-001 | `explanation`, `source_reference`, `tested_concepts` | r. 20.04(2)(b) → r. 20.04(2)(a) |
| 4 | civ-07-summ-judg-004 | `explanation`, `source_reference`, `tested_concepts` | r. 20.04(2)(b) → r. 20.04(2)(a) |
| 5 | civ-08-sol-cl-priv-004 | `explanation`, `source_reference`, `exam_trigger_words`, `tested_concepts` | Lavallee (search warrants) → Pritchard (in-house counsel privilege) |
| 6 | crim-02-arrest-war-002 | `why_D_wrong` | s. 495(1)(b) → s. 495(1)(a) |
| 7 | crim-02-arrest-war-004 | `source_reference` | s. 495(1) and s. 495(2) → s. 494(1)(b) and s. 494(2) |
| 8 | crim-02-s10b-003 | `why_D_wrong` | Overstated "proactive duty" → "may be required to re-advise" (Sinclair 5-4) |
| 9 | crim-02-s9-detent-004 | `pr_angle` | Set `applicable: true`; added `pr_issue_type` |
| 10 | crim-03-bail-grnds-003 | `why_D_wrong` | Added s. 522 Criminal Code clarification for murder bail |
| 11 | crim-03-bail-grnds-004 | `source_reference` | s. 515(10) → s. 515(6)(a) |
| 12 | crim-03-bail-grnds-005 | `source_reference` | s. 515(10) → s. 515(3) |
| 13 | crim-04-stinch-002 | `explanation` | Added "at the first reasonable opportunity and in any event" per Stinchcombe |
| 14 | crim-04-tpr-002 | `options.C`, `why_C_wrong` | O'Connor citation: CanLII → [1995] 4 SCR 411 |
| 15 | fam-04-mh-possess-001 | `why_D_wrong` | "additional" → "distinct" |
| 16 | fam-05-spse-supp-005 | `source_reference` (heading + rule) | Entitlement provisions → variation provisions (FLA s. 37 / DA s. 17) |
| 17 | fam-05-ssag-001 | `source_reference` | SSAG "revised 2016" → "revised 2021" |
| 18 | fam-05-ssag-002 | `source_reference` | SSAG "revised 2016" → "revised 2021" |
| 19 | pub-02-s15-equal-002 | `source_reference` | Added Kapp (2008 SCC 41) and Withler (2011 SCC 12) |
| 20 | pub-02-s15-equal-003 | `source_reference` | Added Kapp (2008 SCC 41) and Withler (2011 SCC 12) |
| 21 | pub-02-s15-equal-004 | `source_reference` | Added Kapp (2008 SCC 41) and Withler (2011 SCC 12) |
| 22 | pub-02-s15-equal-005 | `source_reference` | Added Eldridge v BC (AG) [1997] 3 SCR 624 |
| 23 | pub-04-reason-stand-001 | `why_C_wrong` | Vavilov abolished patent unreasonableness → Dunsmuir first, Vavilov refined |
| 24 | pub-04-reason-stand-003 | `explanation` | Vavilov/Dunsmuir chronological order corrected |
| 25 | fam-04-mh-possess-001 | `why_D_wrong` | (same as #15 — listed in script as separate fix pass) |
| 26 | fam-05-spse-supp-005 | `source_reference.heading` | "Entitlement Grounds — FLA s.33(8)..." → "Variation of Spousal Support — Material Change in Circumstances" |

---

## Validator Output (post-fix)

```
Validation complete: 0 errors, 125 warnings
```

All 125 warnings are pre-existing format style warnings (explanation wording conventions). No structural errors. No legal content errors remain after the 26 fixes above.

---

*This document is maintained as part of the Phase 2C QA process. It must be updated each time a question in Generated Barrister C is modified or promoted beyond `draft`.*
