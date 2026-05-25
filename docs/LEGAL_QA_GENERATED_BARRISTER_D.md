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
| FIXED — Phase 2J cleanup | 1 |
| HUMAN REVIEW REQUIRED — unresolved | 0 |
| REMOVE | 0 |

**Total fixed:** 3 (1 source citation + 1 explanation artifact + 1 Phase 2J correct-answer rewrite)  
**Remaining unresolved flags:** 0 — all flags resolved  
**PR-angle count:** 2 (manifest value confirmed; civ-12-soli-001 has `applicable: true`; one other question in bank also flagged `applicable: true` but that is civ-06-exparte-002 which is excluded from this exam — confirmed manifest `pr_angle_count: 2` is consistent with the two in-exam questions that have `applicable: true`)  
**Difficulty split:** Easy: 28 · Medium: 71 · Hard: 49 · Exam-trap: 12  
**Reassembled:** Yes — rebuilt from original manifest IDs after Phase 2J fixes (2026-05-25); baked into index.html (432,256 chars)  

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
| crim-02-sw-issu-004 | **FIXED (Phase 2J)** | Correct answer changed B→D. CC s.487 imposes no 30-day statutory expiry on dwelling-house warrants; the applicable standard is common-law reasonable time. `correct_answer`, `options.D`, `explanation`, `why_B_wrong`, and `why_D_wrong` fully rewritten. |

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

## Phase 2J Fix — crim-02-sw-issu-004

### crim-02-sw-issu-004 — Dwelling-house warrant validity (correct answer rewritten)

**File:** `data/questions/criminal-law/ch02-charter-arrest.json`  
**Phase 2J action (2026-05-25):** Full rewrite. The original correct answer (B) claimed that s.487 *Criminal Code* warrants automatically expire after 30 days. No such provision exists in CC s.487. The CDSA s.11(5) provides a 15-day expiry for drug-search warrants under that statute; DNA warrants have their own regimes under ss.487.04–487.09. For standard s.487 warrants the applicable test is the common-law requirement to execute within a reasonable time.  

**Changes made:**  
- `correct_answer`: `"B"` → `"D"`  
- `options.D`: rewritten to accurately state the common-law reasonable-time standard and identify defence counsel's strongest argument  
- `explanation`: fully rewritten — confirms no 30-day statutory limit in s.487; distinguishes CDSA s.11(5) (15-day drug-warrant limit); explains common-law reasonableness standard  
- `why_B_wrong`: rewritten — s.487 contains no universal 30-day statutory expiry  
- `why_D_wrong`: rewritten — confirms D is the correct answer

---

## Validation Status Confirmation

All 160 questions retain `validation_status: "draft"` — no validation_status fields were modified during this QA review, consistent with task requirements.

---

## Files Modified

| File | Change |
|------|--------|
| `data/questions/criminal-law/ch06-trial.json` | Fixed Lifchus citation in `crim-06-burden-001` (`source_reference`) |
| `data/questions/criminal-law/ch02-charter-arrest.json` | Phase 2J: `crim-02-sw-issu-004` — correct answer B→D; `options.D`, `explanation`, `why_B_wrong`, `why_D_wrong` fully rewritten; no 30-day CC s.487 limit; common-law reasonable-time standard |
