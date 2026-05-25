# Legal QA — Generated Barrister E

**Exam ID:** `generated-barrister-e`  
**Label:** Generated Barrister E  
**Seed:** 3 · **Total Questions:** 160  
**QA Date:** 2026-05-25  
**Reviewer:** AI-assisted (Claude Sonnet 4.6) — requires human sign-off before study use  
**Source authority:** 2026 LSO Barrister licensing examination materials (internal knowledge only; no web browsing)

---

## Summary

| Verdict | Count |
|---------|------:|
| PASS | 154 |
| FIXED | 5 |
| HUMAN REVIEW REQUIRED | 1 |
| REMOVE | 0 |
| **Total** | **160** |

---

## Fixed Questions

| Question ID | File | What Changed |
|-------------|------|--------------|
| `crim-11-error-law-001` | `data/questions/criminal-law/ch11-appeals.json` | Typo in `call_of_question`: `"frounded"` → `"grounded"`. Legal content unaffected. |
| `pub-03-inst-bias-001` | `data/questions/public-law/ch03-admin-law.json` | Removed erroneous `Canadian Pacific Ltd v Matsqui Indian Band, [1995] 1 SCR 3` citation from `options.C` and `why_C_wrong`. Matsqui concerns Federal Court jurisdiction over Aboriginal band tribunal decisions — it is not authority for the investigative/adjudicative institutional bias doctrine. Replaced with `Committee for Justice and Liberty v National Energy Board, [1978] 1 SCR 369` (the actual governing authority for the reasonable apprehension of bias test), consistent with the `source_reference`. |
| `civ-02-psych-001` | `data/questions/civil-litigation/ch02-limitation-periods.json` | Commencement date changed from `July 2025` to `May 2025` throughout (fact_pattern, options B and C, explanation, why_B_wrong). With capacity regained June 2023, the two-year period expires June 2025; "July 2025" fell one month past expiry, making option C's "within two years" claim arithmetically wrong. Changing to "May 2025" (before the June 2025 expiry) makes option C correct and option B's "statute-barred" conclusion a wrong distractor, as intended. |
| `civ-02-ult-except-001` | `data/questions/civil-litigation/ch02-limitation-periods.json` | Corrected final sentence of `explanation`. Original sentence ("She may still be subject to the basic two-year limitation period running from the date of discovery under s.4") was wrong: Limitations Act, 2002, s.16(1)(h) removes ALL limitation periods — both the basic two-year (s.4) and ultimate 15-year (s.15) — for sexual assault claims. Replaced with accurate statement citing s.16(1)(h). |
| `fam-10-contempt-001` | `data/questions/family-law/ch10-fro.json` | Removed `"Courts of Justice Act, R.S.O. 1990, c. C.43, s. 140"` from `source_reference.rule_or_statute_reference`. CJA s.140 is the vexatious proceedings section and has no connection to contempt. The `Family Law Rules, O. Reg. 114/99, r. 31` citation already present is correct and sufficient for contempt motions in family proceedings. |

---

## Flagged Questions — HUMAN REVIEW REQUIRED

| Question ID | File | Reason |
|-------------|------|--------|
| `civ-02-demand-001` | `data/questions/civil-litigation/ch02-limitation-periods.json` | Explanation cites `"s. 5(3) of the Limitations Act, 2002"` as the source of the demand-obligation discovery rule (limitation period for a demand debt runs from the date demand is made). Section 5 of the Limitations Act, 2002 has only two subsections (s.5(1) discovery rule and s.5(2) presumption of knowledge); there is no s.5(3) addressing demand obligations. The demand-obligation rule derives from judicial interpretation of s.5(1)(a). A qualified reviewer should verify whether the 2026 LSO materials cite a specific provision for this rule and correct the citation if s.5(3) does not exist. The substantive legal proposition (limitation period for demand obligations runs from date of demand) is correct. |

---

## Per-Question Verdicts

### Civil Litigation (43 questions)

| # | Question ID | Verdict | Notes |
|---|-------------|---------|-------|
| 1 | `civ-02-agree-001` | PASS | |
| 2 | `civ-02-contrib-001` | PASS | |
| 3 | `civ-02-demand-001` | HUMAN REVIEW REQUIRED | s.5(3) citation unverifiable — see Flagged section |
| 4 | `civ-02-psych-001` | FIXED | Commencement date July→May 2025 to correct arithmetic |
| 5 | `civ-02-susp-ext-001` | PASS | |
| 6 | `civ-02-ult-except-001` | FIXED | Explanation corrected: s.16(1)(h) removes basic period too |
| 7 | `civ-03-app-act-001` | PASS | |
| 8 | `civ-03-crossclaim-001` | PASS | |
| 9 | `civ-03-defence-001` | PASS | |
| 10 | `civ-03-sod-001` | PASS | |
| 11 | `civ-03-strike-002` | PASS | |
| 12 | `civ-03-third-pty-001` | PASS | |
| 13 | `civ-04-corp-alt-001` | PASS | |
| 14 | `civ-04-exjuris-001` | PASS | |
| 15 | `civ-04-exjuris-002` | PASS | |
| 16 | `civ-05-amend-r26-001` | PASS | |
| 17 | `civ-05-dis-001` | PASS | |
| 18 | `civ-05-material-001` | PASS | |
| 19 | `civ-05-particulars-001` | PASS | |
| 20 | `civ-06-nom-001` | PASS | |
| 21 | `civ-06-striking-001` | PASS | |
| 22 | `civ-06-undertaking-001` | PASS | |
| 23 | `civ-07-costs-sj-002` | PASS | |
| 24 | `civ-07-costs-sj-003` | PASS | |
| 25 | `civ-08-aod-form-001` | PASS | |
| 26 | `civ-09-corp-disc-001` | PASS | |
| 27 | `civ-09-use-trial-003` | PASS | |
| 28 | `civ-10-ots-007` | PASS | |
| 29 | `civ-11-trial-proc-001` | PASS | |
| 30 | `civ-11-trial-proc-002` | PASS | |
| 31 | `civ-11-trial-proc-003` | PASS | |
| 32 | `civ-11-trial-proc-004` | PASS | |
| 33 | `civ-11-trial-proc-005` | PASS | |
| 34 | `civ-12-costs-event-001` | PASS | |
| 35 | `civ-12-pi-si-001` | PASS | |
| 36 | `civ-12-pi-si-002` | PASS | |
| 37 | `civ-13-app-001` | PASS | |
| 38 | `civ-13-div-ct-001` | PASS | |
| 39 | `civ-13-notice-app-001` | PASS | |
| 40 | `civ-13-stay-001` | PASS | |
| 41 | `civ-14-enf-contempt-001` | PASS | |
| 42 | `civ-14-enf-exam-001` | PASS | |
| 43 | `civ-16-notice-001` | PASS | |

**Civil Litigation:** 40 PASS · 2 FIXED · 1 HUMAN REVIEW REQUIRED · 0 REMOVE

---

### Criminal Law (43 questions)

| # | Question ID | Verdict | Notes |
|---|-------------|---------|-------|
| 1 | `crim-01-juris-005` | PASS | |
| 2 | `crim-01-juris-006` | PASS | |
| 3 | `crim-01-re-elect-001` | PASS | |
| 4 | `crim-03-bail-cond-001` | PASS | |
| 5 | `crim-03-bail-rev-002` | PASS | |
| 6 | `crim-03-surety-001` | PASS | |
| 7 | `crim-04-constr-poss-001` | PASS | |
| 8 | `crim-04-stinch-006` | PASS | |
| 9 | `crim-04-timing-001` | PASS | |
| 10 | `crim-04-tpr-004` | PASS | |
| 11 | `crim-04-tpr-005` | PASS | |
| 12 | `crim-05-commit-001` | PASS | |
| 13 | `crim-05-elect-003` | PASS | |
| 14 | `crim-05-plea-003` | PASS | |
| 15 | `crim-05-plea-barg-001` | PASS | |
| 16 | `crim-05-prelim-003` | PASS | |
| 17 | `crim-06-cea-s9-001` | PASS | |
| 18 | `crim-06-jury-001` | PASS | |
| 19 | `crim-06-jury-002` | PASS | |
| 20 | `crim-06-order-001` | PASS | |
| 21 | `crim-07-biz-rec-001` | PASS | |
| 22 | `crim-07-hearsay-002` | PASS | |
| 23 | `crim-07-prior-consist-001` | PASS | |
| 24 | `crim-07-prior-consist-002` | PASS | |
| 25 | `crim-07-s276-001` | PASS | |
| 26 | `crim-08-necessity-001` | PASS | |
| 27 | `crim-09-consec-001` | PASS | |
| 28 | `crim-09-credit-001` | PASS | |
| 29 | `crim-09-credit-002` | PASS | |
| 30 | `crim-09-disc-001` | PASS | |
| 31 | `crim-09-gladue-001` | PASS | |
| 32 | `crim-09-mand-min-001` | PASS | |
| 33 | `crim-09-mand-min-002` | PASS | |
| 34 | `crim-10-conf-001` | PASS | |
| 35 | `crim-10-records-002` | PASS | |
| 36 | `crim-11-crown-app-001` | PASS | |
| 37 | `crim-11-crown-sent-app-001` | PASS | |
| 38 | `crim-11-error-law-001` | FIXED | Typo "frounded" → "grounded" in call_of_question |
| 39 | `crim-11-ind-app-001` | PASS | |
| 40 | `crim-11-proviso-001` | PASS | |
| 41 | `crim-12-misc-001` | PASS | |
| 42 | `crim-12-misc-002` | PASS | |
| 43 | `crim-12-misc-003` | PASS | |

**Criminal Law:** 42 PASS · 1 FIXED · 0 HUMAN REVIEW REQUIRED · 0 REMOVE

---

### Family Law (39 questions)

| # | Question ID | Verdict | Notes |
|---|-------------|---------|-------|
| 1 | `fam-02-condo-001` | PASS | |
| 2 | `fam-02-da-prop-001` | PASS | |
| 3 | `fam-02-divorce-bar-002` | PASS | Minor cosmetic note: subtopic_id says "divorce_bars" but question tests effective date — not a legal error |
| 4 | `fam-02-divorce-grd-001` | PASS | |
| 5 | `fam-02-jurisdiction-001` | PASS | |
| 6 | `fam-02-petition-001` | PASS | |
| 7 | `fam-02-self-suff-001` | PASS | |
| 8 | `fam-02-var-coro-001` | PASS | |
| 9 | `fam-05-entitlement-001` | PASS | |
| 10 | `fam-05-lim-period-001` | PASS | |
| 11 | `fam-05-non-comp-001` | PASS | |
| 12 | `fam-05-review-var-001` | PASS | |
| 13 | `fam-05-self-suff-001` | PASS | |
| 14 | `fam-06-adult-child-001` | PASS | |
| 15 | `fam-06-cs-s7-002` | PASS | |
| 16 | `fam-06-dbs-001` | PASS | |
| 17 | `fam-06-income-cap-001` | PASS | |
| 18 | `fam-06-shared-cust-001` | PASS | |
| 19 | `fam-06-tax-001` | PASS | |
| 20 | `fam-07-bi-003` | PASS | Earlier fix confirmed: "16 enumerated factors" consistent throughout |
| 21 | `fam-07-foreign-order-001` | PASS | |
| 22 | `fam-07-grandpar-001` | PASS | |
| 23 | `fam-07-interim-001` | PASS | |
| 24 | `fam-07-reloc-003` | PASS | |
| 25 | `fam-07-superv-access-001` | PASS | |
| 26 | `fam-08-customary-001` | PASS | |
| 27 | `fam-08-duty-rep-002` | PASS | |
| 28 | `fam-09-dc-lim-001` | PASS | |
| 29 | `fam-09-setting-001` | PASS | |
| 30 | `fam-10-contempt-001` | FIXED | Erroneous CJA s.140 removed from source_reference |
| 31 | `fam-10-fro-arr-001` | PASS | |
| 32 | `fam-10-inter-prov-001` | PASS | |
| 33 | `fam-10-reg-susp-001` | PASS | |
| 34 | `fam-11-eq-lim-001` | PASS | |
| 35 | `fam-11-poss-lim-001` | PASS | |
| 36 | `fam-13-cl-def-001` | PASS | |
| 37 | `fam-13-jfv-001` | PASS | |
| 38 | `fam-13-res-trust-001` | PASS | |
| 39 | `fam-13-uje-001` | PASS | |

**Family Law:** 37 PASS · 1 FIXED · 0 HUMAN REVIEW REQUIRED · 0 REMOVE

---

### Public Law (35 questions)

| # | Question ID | Verdict | Notes |
|---|-------------|---------|-------|
| 1 | `pub-01-double-asp-001` | PASS | |
| 2 | `pub-01-iji-002` | PASS | |
| 3 | `pub-01-pith-001` | PASS | |
| 4 | `pub-01-pith-002` | PASS | |
| 5 | `pub-01-s91-27-001` | PASS | |
| 6 | `pub-01-s92-13-001` | PASS | |
| 7 | `pub-02-s10a-001` | PASS | |
| 8 | `pub-02-s12-001` | PASS | |
| 9 | `pub-02-s28-001` | PASS | |
| 10 | `pub-02-s33-001` | PASS | s.28 cannot be overridden by s.33 — correctly stated |
| 11 | `pub-02-s9-det-001` | PASS | |
| 12 | `pub-03-delegation-001` | PASS | |
| 13 | `pub-03-inst-bias-001` | FIXED | Matsqui Indian Band citation removed; replaced with Committee for Justice and Liberty |
| 14 | `pub-03-legit-exp-001` | PASS | |
| 15 | `pub-03-reasons-003` | PASS | |
| 16 | `pub-04-alt-remedy-001` | PASS | |
| 17 | `pub-04-delay-001` | PASS | |
| 18 | `pub-04-mootness-001` | PASS | |
| 19 | `pub-04-record-001` | PASS | |
| 20 | `pub-04-remedy-003` | PASS | |
| 21 | `pub-04-standing-001` | PASS | Option C cites a Federal Court case alongside SCC authority — not a legal error |
| 22 | `pub-05-sppa-app-001` | PASS | |
| 23 | `pub-05-sppa-excl-001` | PASS | |
| 24 | `pub-05-sppa-rec-002` | PASS | |
| 25 | `pub-05-sppa-sub-001` | PASS | |
| 26 | `pub-06-fippa-exc-002` | PASS | |
| 27 | `pub-06-fippa-rec-001` | PASS | |
| 28 | `pub-06-fippa-s20-001` | PASS | Question ID contains "s20" but tests FIPPA s.18 — ID is a system artifact only |
| 29 | `pub-06-pipeda-breach-001` | PASS | |
| 30 | `pub-06-pipeda-cons-001` | PASS | |
| 31 | `pub-07-neg-invest-001` | PASS | |
| 32 | `pub-07-sov-imm-001` | PASS | |
| 33 | `pub-07-vic-liab-001` | PASS | |
| 34 | `pub-08-prima-facie-001` | PASS | |
| 35 | `pub-08-undue-hard-001` | PASS | |

**Public Law:** 34 PASS · 1 FIXED · 0 HUMAN REVIEW REQUIRED · 0 REMOVE

---

## Methodology

- Each question reviewed against 2026 LSO Barrister licensing examination materials using internal knowledge only.
- Legal claims (statute citations, case holdings, test elements, thresholds) verified for accuracy.
- Correct answers verified to be definitively correct; distractors verified to be plausibly wrong for stated reasons.
- No web browsing, no outside law, no Brigham/Access the Bar imported exams used as legal authority.
- All `validation_status` fields remain `"draft"` pending individual source-check against LSO text.
- One question flagged HUMAN REVIEW REQUIRED for a potentially hallucinated subsection citation (`civ-02-demand-001` — s.5(3)). The substantive legal rule it tests is correct.

---

## Post-QA Reassembly

Five source files were modified before final assembly. After all fixes were applied, the compact E exam was rebuilt from the original 160 QA'd question IDs. (Pool growth from Phase 2H caused seed 3 to select different questions on re-run; the exam was locked to its original QA'd question set.)

**Post-fix payload:** 468,144 chars (was 467,732 before QA fixes — +412 chars)  
**Allocation confirmed:** CIV 43 · CRIM 43 · FAM 39 · PUB 35  
**Overlap:** E∩C=0 · E∩D=0 · E∩F=0 · C∪D∪E∪F=640 unique IDs  
**validate_html.py:** ✅ all 4 checks pass  
**validate_question.py:** ✅ 0 errors
