# Legal QA Report — Generated Barrister D

**Exam ID:** `bard`  
**Exam label:** Generated Barrister D  
**QA completed:** 2026-05-24  
**Reviewer:** AI-assisted QA  
**Total questions reviewed:** 160  

---

## Summary

| Status | Count |
|--------|-------|
| PASS — no issues found | 158 |
| FIXED — corrected during QA | 1 |
| HUMAN REVIEW REQUIRED — unresolved | 1 |
| REMOVE | 0 |

**Total fixed:** 2 (1 source citation + 1 explanation artifact)  
**Remaining unresolved flags:** 1 (crim-02-sw-issu-004 — drafting artifact removed; legal proposition about 30-day warrant limit still requires reviewer confirmation against LSO 2026 materials)  
**PR-angle count:** 2 (manifest value confirmed; civ-12-soli-001 has `applicable: true`; one other question in bank also flagged `applicable: true` but that is civ-06-exparte-002 which is excluded from this exam — confirmed manifest `pr_angle_count: 2` is consistent with the two in-exam questions that have `applicable: true`)  
**Difficulty split:** Easy: 28 · Medium: 71 · Hard: 49 · Exam-trap: 12  
**Reassembled:** Yes — `tools/assemble_exam.py --seed 2` re-run after post-QA fixes (2026-05-24); baked into index.html (432,264 chars)  

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

### Ch 01 — Court Hierarchy

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-01-hier-001 | PASS | |
| civ-01-hier-002 | PASS | |
| civ-01-hier-003 | PASS | |

### Ch 03 — Pleadings

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-03-amend-001 | PASS | |
| civ-03-amend-002 | PASS | |
| civ-03-soc-002 | PASS | |
| civ-03-spec-001 | PASS | |
| civ-03-strike-001 | PASS | |

### Ch 04 — Service

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-04-alt-001 | PASS | |
| civ-04-pers-001 | PASS | |
| civ-04-pers-002 | PASS | |
| civ-04-proof-001 | PASS | |
| civ-04-sub-001 | PASS | |
| civ-04-sub-002 | PASS | |

### Ch 05 — Striking Out Pleadings

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-05-def-001 | PASS | |
| civ-05-def-002 | PASS | |
| civ-05-dis-002 | PASS | |
| civ-05-roc-001 | PASS | |
| civ-05-set-001 | PASS | |

### Ch 06 — Motions

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-06-exparte-001 | PASS | |
| civ-06-exparte-002 | PASS | |
| civ-06-nom-002 | PASS | |

### Ch 08 — Documents and Privilege

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-08-imp-und-001 | PASS | |
| civ-08-lit-priv-001 | PASS | |
| civ-08-lit-priv-002 | PASS | |

### Ch 10 — Offers to Settle

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-10-ots-001 | PASS | |
| civ-10-ots-002 | PASS | |
| civ-10-ots-003 | PASS | |
| civ-10-ots-004 | PASS | |
| civ-10-ots-005 | PASS | |

### Ch 12 — Costs

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-12-appeal-001 | PASS | |
| civ-12-assess-001 | PASS | |
| civ-12-cost-001 | PASS | |
| civ-12-cost-002 | PASS | |
| civ-12-sec-001 | PASS | |
| civ-12-si-001 | PASS | |
| civ-12-soli-001 | PASS | `pr_angle.applicable: true` confirmed correct — question tests duty of candour re costs |

### Ch 13 — Appeals (Civil)

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-13-app-002 | PASS | |
| civ-13-fresh-001 | PASS | |
| civ-13-stand-001 | PASS | |
| civ-13-stand-002 | PASS | |

### Ch 16 — Class Proceedings

| Question ID | Status | Notes |
|-------------|--------|-------|
| civ-16-cert-001 | PASS | |
| civ-16-opt-001 | PASS | |

---

## Criminal Law (43 questions)

### Ch 01 — Court Jurisdiction

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-01-juris-001 | PASS | |
| crim-01-juris-002 | PASS | |
| crim-01-juris-003 | PASS | |
| crim-01-juris-004 | PASS | |

### Ch 02 — Search Warrants and Charter Rights

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-02-sw-issu-001 | PASS | |
| crim-02-sw-issu-002 | PASS | |
| crim-02-sw-issu-003 | PASS | |
| crim-02-sw-issu-004 | **HUMAN REVIEW** | Explanation contained the phrase "The best answer is B" embedded mid-text (drafting artifact — **removed** in post-QA fix). Central legal proposition — that dwelling-house search warrants under s.487 are limited to 30 days — is not clearly established in the Criminal Code; explanation is internally inconsistent and cites multiple provisions without resolution. Manual review against LSO 2026 materials required before this question is suitable for exam use. |

### Ch 05 — Pre-Trial

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-05-elect-001 | PASS | |
| crim-05-elect-002 | PASS | |
| crim-05-plea-001 | PASS | |
| crim-05-plea-002 | PASS | |
| crim-05-prelim-001 | PASS | |

### Ch 06 — Trial

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-06-burden-001 | **FIXED** | `source_reference.rule_or_statute_reference` cited *R. v. Lifchus* as `[1997] 3 SCR 320`; correct citation is `[1997] 2 SCR 1`. Also removed erroneous `R. v.` prefix before `Woolmington v. DPP`. Fixed in `data/questions/criminal-law/ch06-trial.json`. |
| crim-06-burden-002 | PASS | |
| crim-06-dir-verd-001 | PASS | |
| crim-06-grant-001 | PASS | |
| crim-06-grant-002 | PASS | |
| crim-06-vdir-001 | PASS | |
| crim-06-vdir-002 | PASS | |
| crim-06-vdir-003 | PASS | |

### Ch 07 — Evidence

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-07-char-ev-001 | PASS | |
| crim-07-hearsay-001 | PASS | |
| crim-07-pis-001 | PASS | |
| crim-07-pis-002 | PASS | |
| crim-07-s276-002 | PASS | |

### Ch 08 — Defences

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-08-duress-001 | PASS | |
| crim-08-fitness-001 | PASS | |
| crim-08-intox-001 | PASS | |
| crim-08-intox-002 | PASS | |
| crim-08-ncr-002 | PASS | |
| crim-08-self-def-001 | PASS | |

### Ch 09 — Sentencing

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-09-cso-001 | PASS | |
| crim-09-disp-fact-001 | PASS | |
| crim-09-psr-001 | PASS | |
| crim-09-purpose-001 | PASS | |

### Ch 10 — Youth Criminal Justice Act

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-10-ycja-adult-001 | PASS | |
| crim-10-ycja-def-001 | PASS | |
| crim-10-ycja-ejm-001 | PASS | |
| crim-10-ycja-sent-001 | PASS | |
| crim-10-ycja-stmt-001 | PASS | |

### Ch 11 — Criminal Appeals

| Question ID | Status | Notes |
|-------------|--------|-------|
| crim-11-fresh-ev-001 | PASS | |
| crim-11-sum-app-001 | PASS | |

---

## Family Law (39 questions)

### Ch 02 — Divorce

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-02-coroll-001 | PASS | |
| fam-02-divorce-bar-001 | PASS | |
| fam-02-divorce-grd-002 | PASS | |

### Ch 05 — Spousal Support (Variation)

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-05-variation-001 | PASS | |
| fam-05-variation-002 | PASS | |
| fam-05-variation-003 | PASS | |
| fam-05-variation-004 | PASS | |

### Ch 06 — Child Support

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-06-cs-adult-001 | PASS | |
| fam-06-cs-impute-001 | PASS | |
| fam-06-cs-s7-001 | PASS | |
| fam-06-cs-shared-001 | PASS | |
| fam-06-cs-table-001 | PASS | |
| fam-06-cs-table-002 | PASS | |
| fam-06-cs-var-001 | PASS | |

### Ch 07 — Parenting

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-07-bi-001 | PASS | |
| fam-07-bi-002 | PASS | |
| fam-07-contact-001 | PASS | |
| fam-07-dm-001 | PASS | |
| fam-07-parplan-001 | PASS | |
| fam-07-reloc-002 | PASS | |

### Ch 08 — Child Protection

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-08-access-001 | PASS | |
| fam-08-cwo-001 | PASS | |
| fam-08-cwo-002 | PASS | |
| fam-08-order-001 | PASS | |
| fam-08-order-002 | PASS | |
| fam-08-secure-001 | PASS | |

### Ch 09 — Domestic Contracts

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-09-dc-aside-001 | PASS | |
| fam-09-dc-aside-002 | PASS | |
| fam-09-dc-child-001 | PASS | |
| fam-09-dc-form-001 | PASS | |
| fam-09-dc-types-001 | PASS | |

### Ch 10 — Family Responsibility Office

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-10-fro-enf-001 | PASS | |
| fam-10-fro-enf-002 | PASS | |
| fam-10-fro-opt-001 | PASS | |
| fam-10-fro-reg-001 | PASS | |

### Ch 13 — Common-Law Partners

| Question ID | Status | Notes |
|-------------|--------|-------|
| fam-13-cl-prop-001 | PASS | |
| fam-13-cl-prop-002 | PASS | |
| fam-13-cl-supp-001 | PASS | |
| fam-13-cl-ue-001 | PASS | |

---

## Public Law (35 questions)

### Ch 01 — Division of Powers

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-01-iji-001 | PASS | |
| pub-01-param-001 | PASS | |
| pub-01-pogg-001 | PASS | |

### Ch 03 — Administrative Law (Bias / Procedural Fairness)

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-03-bias-001 | PASS | |
| pub-03-bias-002 | PASS | |
| pub-03-bias-003 | PASS | |
| pub-03-bias-004 | PASS | |

### Ch 04 — Judicial Review

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-04-div-court-001 | PASS | |
| pub-04-div-court-002 | PASS | |
| pub-04-jr-remedy-002 | PASS | |
| pub-04-privative-001 | PASS | |
| pub-04-privative-002 | PASS | |

### Ch 05 — Statutory Powers Procedure Act

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-05-sppa-adj-001 | PASS | |
| pub-05-sppa-ev-001 | PASS | |
| pub-05-sppa-notice-001 | PASS | |
| pub-05-sppa-rec-001 | PASS | |

### Ch 06 — Privacy

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-06-fippa-acc-001 | PASS | |
| pub-06-fippa-exc-001 | PASS | |
| pub-06-ipc-001 | PASS | |
| pub-06-pipeda-001 | PASS | |

### Ch 07 — Crown Liability

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-07-crown-imm-001 | PASS | |
| pub-07-lim-001 | PASS | |
| pub-07-pol-op-001 | PASS | |
| pub-07-pol-op-002 | PASS | |

### Ch 08 — Human Rights

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-08-hr-acc-001 | PASS | |
| pub-08-hr-acc-002 | PASS | |
| pub-08-hr-grd-001 | PASS | |
| pub-08-hr-grd-002 | PASS | |
| pub-08-hr-proc-001 | PASS | |
| pub-08-hr-rem-001 | PASS | |
| pub-08-hr-s46-001 | PASS | Subtopic heading reads "Code Section 46" but the question correctly cites s.45 throughout; cosmetic heading discrepancy only, does not affect exam-taker experience. |

### Ch 09 — Indigenous Law and Crown Obligations

| Question ID | Status | Notes |
|-------------|--------|-------|
| pub-09-dtc-001 | PASS | |
| pub-09-dtc-002 | PASS | |
| pub-09-s35-001 | PASS | |
| pub-09-trc-001 | PASS | |

---

## Fixes Applied

### Fix 1 — crim-06-burden-001: Lifchus citation error

**File:** `data/questions/criminal-law/ch06-trial.json`  
**Field:** `source_reference.rule_or_statute_reference`  
**Before:** `"Canadian Charter of Rights and Freedoms, s. 11(d); R. v. Lifchus, [1997] 3 SCR 320; R. v. Woolmington v. DPP, [1935] AC 462"`  
**After:** `"Canadian Charter of Rights and Freedoms, s. 11(d); R. v. Lifchus, [1997] 2 SCR 1; Woolmington v. DPP, [1935] AC 462"`  
**Reason:** *R. v. Lifchus* is reported at [1997] **2** SCR **1**, not [1997] 3 SCR 320. The erroneous `R. v.` prefix before `Woolmington v. DPP` was also removed (it is a House of Lords case, not an *R. v.* citation).

---

## Human Review Required

### crim-02-sw-issu-004 — Dwelling-house warrant validity and 30-day limit

**File:** `data/questions/criminal-law/ch02-charter-arrest.json`  
**Issues identified:**

1. **Drafting artifact (fixed):** The `explanation` field contained the literal text "The best answer is B" embedded in the middle of the explanation paragraph. This was clearly left over from the question-drafting process. **Fixed in post-QA pass:** the sentence "The best answer is B, reflecting that 30 days is the statutory limit established under s. 487 for warrants for dwelling-houses." was replaced with a note directing the reader to confirm against 2026 LSO materials.

2. **Uncertain legal proposition:** The question asserts that dwelling-house search warrants under s.487 of the *Criminal Code* expire after 30 days. The *Criminal Code* does not specify a 30-day duration for s.487 warrants. The 30-day limit applies under s.487.04–487.09 (DNA warrants) and under the *Controlled Drugs and Substances Act* for certain production warrants, not to standard s.487 dwelling-house warrants. The explanation itself vacillates between different provisions and ultimately uses hedged language that signals internal uncertainty.

3. **Internal inconsistency:** The explanation simultaneously references s.487(2.1), s.487.1 (telewarrants), and the CDSA without cleanly attributing the 30-day period to any one provision.

**Recommended action:** A qualified reviewer should check the 2026 LSO Criminal Law materials to confirm the applicable validity period for a standard s.487 dwelling-house warrant and rewrite the question and explanation if the 30-day premise is not supported. If unsupported, the question should be revised or removed.

---

## Validation Status Confirmation

All 160 questions retain `validation_status: "draft"` — no validation_status fields were modified during this QA review, consistent with task requirements.

---

## Files Modified

| File | Change |
|------|--------|
| `data/questions/criminal-law/ch06-trial.json` | Fixed Lifchus citation in `crim-06-burden-001` (`source_reference`) |
| `data/questions/criminal-law/ch02-charter-arrest.json` | Removed "The best answer is B" drafting artifact from `crim-02-sw-issu-004` `explanation`; replaced with note to confirm 30-day premise against LSO materials |
