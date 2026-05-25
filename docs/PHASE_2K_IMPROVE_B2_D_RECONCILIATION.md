# Phase 2K-Improve-B2 — Exam D IMPROVE Reconciliation

**Date:** 2026-05-25  
**Purpose:** Verify that the "Exam D IMPROVE resolved" claim in Phase 2K-Improve-B2 is accurate by accounting for all 41 IMPROVE items from the Phase 2K psychometric audit.  
**Audit source:** `docs/PSYCHOMETRIC_AUDIT_GENERATED_BARRISTER_D.md`  
**Manifest source:** `data/exams/generated-barrister-d-manifest.json`

---

## 1. Structural Finding: Audit Chapter Tables Use Fabricated Question IDs

A critical prerequisite for this reconciliation: the per-chapter tables in the D audit use question IDs that **do not match the actual Exam D manifest**. The chapter question counts are correct (e.g., ch01 has 3 questions, ch04 has 6, ch08 has 3), but the IDs are wrong throughout:

| Audit chapter | Audit IDs (example) | Actual D manifest IDs (same chapter) |
|---|---|---|
| ch01 (3 q) | civ-01-commence-001, civ-01-rcp-001, civ-01-service-001 | civ-01-hier-001, civ-01-hier-002, civ-01-hier-003 |
| ch04 (6 q) | civ-04-discovery-001, civ-04-exam-001, … | civ-04-alt-001, civ-04-pers-001, civ-04-pers-002, … |
| ch08 (3 q) | civ-08-cert-001, civ-08-cert-002, civ-08-cpa-001 | civ-08-imp-und-001, civ-08-lit-priv-001, civ-08-lit-priv-002 |
| ch10 (5 q) | civ-10-appeal-001, civ-10-leave-001, … | civ-10-ots-001 … civ-10-ots-005 |
| ch12 (7 q) | civ-12-enforce-001, civ-12-writ-001, … | civ-12-appeal-001, civ-12-cost-001, … |

**Implication:** Individual quality verdicts from chapter tables cannot be reliably mapped to actual bank question IDs. The audit's summary statistics (PASS=109, IMPROVE=41, REWRITE=10) are assumed to reflect actual scoring; the chapter tables and consolidated IMPROVE list are unreliable for question-level identification.

---

## 2. Full Account of 41 IMPROVE Items

### 2a. Named items in the consolidated IMPROVE list (13 rows)

The audit names 13 question IDs in its "Questions Requiring IMPROVE" section:

| # | question_id | In D manifest? | In bank? | Disposition | Further action? |
|---|---|---|---|---|---|
| 1 | civ-03-strike-001 | ✅ Yes | ✅ Yes (ch03-pleadings.json) | Rewritten in Phase 2K-Improve-A (2026-05-25) | None |
| 2 | civ-04-exam-001 | ❌ No | ⚠️ Yes but wrong exam (ch09-examination-for-discovery.json; not in any exam manifest) | Rewritten in Phase 2K-Improve-A — improvement is in bank but orphaned (no exam payload affected) | Consider adding to a future exam manifest |
| 3 | civ-08-cpa-001 | ❌ No | ⚠️ Yes but wrong exam (ch16-class-actions.json; not in any exam manifest) | Rewritten in Phase 2K-Improve-A — improvement is in bank but orphaned (no exam payload affected) | Consider adding to a future exam manifest |
| 4 | civ-10-leave-001 | ❌ No | ❌ No (does not exist in bank) | Fully fabricated ID — no source question exists; unresolvable | None (no action possible) |
| 5 | civ-12-writ-001 | ❌ No | ❌ No (does not exist in bank) | Fully fabricated ID — no source question exists; unresolvable | None (no action possible) |
| 6 | crim-02-sw-issu-001 | ✅ Yes | ✅ Yes (ch02-charter-arrest.json) | Rewritten in Phase 2K-Improve-A (2026-05-25) | None |
| 7 | crim-09-purpose-001 | ✅ Yes | ✅ Yes (ch09-sentencing.json) | Rewritten in Phase 2K-Improve-A (2026-05-25) | None |
| 8 | crim-10-ycja-def-001 | ✅ Yes | ✅ Yes (ch10-ycja.json) | Rewritten in Phase 2K-Improve-A (2026-05-25) | None |
| 9 | crim-11-sum-app-001 | ✅ Yes | ✅ Yes (ch11-appeals.json) | Rewritten in Phase 2K-Improve-A (2026-05-25) | None |
| 10 | crim-06-burden-001 | ✅ Yes | ✅ Yes (ch06-trial.json) | Retained as foundational easy anchor per audit ("acceptable as easy anchor") | None — intentional |
| 11 | fam-06-cs-table-001 | ✅ Yes | ✅ Yes (ch06-child-support.json) | Rewritten in Phase 2K-Improve-A (2026-05-25) | None |
| 12 | fam-07-parplan-001 | ✅ Yes | ✅ Yes (ch07-parenting.json) | Rewritten in Phase 2K-Improve-A (2026-05-25) | None |
| 13 | pub-04-div-court-001 | ✅ Yes | ✅ Yes (ch04-judicial-review.json) | Rewritten in Phase 2K-Improve-A (2026-05-25) | None |

**Named-item summary:**
- 9 items confirmed in D manifest: 8 rewritten in A, 1 retained as anchor — all resolved
- 2 items in bank but not in D manifest (or any manifest): rewritten in A but as orphan work — no exam payload effect
- 2 items fully fabricated (not in bank): unresolvable

### 2b. Unnamed items (28 rows)

The audit's consolidated list names only 13 of the 41 IMPROVE items. The remaining **28 were scored as IMPROVE but not named anywhere in the audit document.**

Since the chapter tables use fabricated IDs, it is not possible to identify the 28 unnamed IMPROVE items by question ID from the audit documentation. The audit note states: "The total IMPROVE count of 41 includes all questions scoring realism 3."

**What B2 did to address unnamed items:**

Phase 2K-Improve-B2 took a systematic approach: it reviewed all easy-difficulty D questions not previously updated (upd=2026-05-24) and improved those assessed as genuinely weak. Of the 21 easy questions reviewed:
- **7 improved:** civ-01-hier-001, civ-10-ots-001, civ-12-cost-002, crim-05-plea-001, fam-07-bi-001, pub-03-bias-001, pub-06-fippa-acc-001
- **14 assessed as PASS and left unchanged:** civ-01-hier-002, civ-04-pers-001, civ-05-def-001, crim-01-juris-001, crim-06-burden-001, crim-07-hearsay-001, fam-02-coroll-001, fam-08-cwo-002, fam-09-dc-form-001, fam-09-dc-types-001, fam-10-fro-reg-001, fam-13-cl-prop-001, pub-07-crown-imm-001, pub-08-hr-grd-001

The 7 improved questions likely correspond to some of the unnamed IMPROVE items. The remaining 21 unnamed items (28 - 7) cannot be individually identified or verified without re-running the audit against the actual D manifest questions.

### 2c. Easy-anchor PASS items noted in audit but counted in IMPROVE statistics

The audit explicitly marks the following questions PASS but notes they have anti_idx=3 or distractor=3 (borderline scores). These may contribute to the 41 count depending on how the auditor applied the scoring boundary:

| question_id | Audit note | Updated in B2? |
|---|---|---|
| crim-07-hearsay-001 | "Easy-difficulty; appropriately so for foundational rule" | No — assessed PASS |
| fam-09-dc-types-001 | "Easy question; appropriate foundational anchor" | No — assessed PASS |
| pub-07-crown-imm-001 | "Easy question; appropriate foundational anchor; distractors serviceable" | No — assessed PASS |
| pub-08-hr-grd-001 | "Easy question; appropriate foundational anchor; distractors serviceable" | No — assessed PASS |

---

## 3. Verification Counts

| Category | Count | Notes |
|---|---|---|
| Total D IMPROVE items per audit statistics | 41 | PASS=109, IMPROVE=41, REWRITE=10; sum=160 ✓ |
| Named in consolidated IMPROVE list | 13 | Audit's "Questions Requiring IMPROVE" section |
| Of named items: in D manifest, addressed | 9 | 8 rewritten in A; 1 retained as anchor |
| Of named items: in bank but not in D manifest | 2 | civ-04-exam-001, civ-08-cpa-001; rewritten in A as orphan work |
| Of named items: fully fabricated ID (not in bank) | 2 | civ-10-leave-001, civ-12-writ-001; unresolvable |
| Unnamed items (cannot be identified by ID) | 28 | 41 − 13 = 28; no IDs available in audit |
| Of unnamed items: improved in B2 by systematic review | ≤7 | civ-01-hier-001, civ-10-ots-001, civ-12-cost-002, crim-05-plea-001, fam-07-bi-001, pub-03-bias-001, pub-06-fippa-acc-001 |
| Of unnamed items: remaining unverified | ≥21 | Cannot be individually confirmed without re-audit |
| Total improved in B2 | 7 | Systematic easy-question review |
| Total handled in Phase 2K-Improve-A (D questions) | 8 | Rewrites of D-manifest REWRITE items |
| Still unresolved (identifiable items) | 0 | All named in-manifest items are handled |
| Still unverified (unnamed items) | ≥21 | Cannot be resolved without re-audit |

---

## 4. Is "Exam D IMPROVE Resolved" Accurate?

**Partially accurate. The claim overstates resolution.**

**Accurate for:** The 9 named IMPROVE items that are in the D manifest. All are now resolved (8 rewritten, 1 accepted as anchor).

**Inaccurate for:**
1. **2 named items with wrong-exam IDs** (civ-04-exam-001, civ-08-cpa-001): These questions exist in the bank but are not in the D manifest or any exam manifest. Their improvement in Phase 2K-Improve-A was orphaned work — the bank has improved versions, but they are not deployed in any exam. These cannot be said to be "resolved for Exam D" since they were never Exam D questions.

2. **2 named items with fully fabricated IDs** (civ-10-leave-001, civ-12-writ-001): These do not exist in the bank. They cannot be resolved.

3. **28 unnamed IMPROVE items**: These are unidentifiable from the audit documentation. B2 improved 7 weak questions through systematic review, which may correspond to some of the unnamed items. The remaining ≥21 cannot be confirmed as resolved without a fresh audit of Exam D.

**Correct statement:** "All identifiable IMPROVE items in the Exam D manifest have been addressed. The audit's claimed total of 41 IMPROVE items cannot be fully reconciled because the chapter tables use fabricated question IDs, 2 named items don't exist in any exam, and 28 items were never named. A fresh re-audit of Exam D is needed to verify whether unaddressed IMPROVE items remain."

---

## 5. Validation

```
python3 tools/validate_question.py data/questions --summary
→ 963 questions, 0 errors ✅

python3 tools/validate_html.py
→ All checks pass ✅
→ bard=455,904 chars (correct post-B2)
```

---

## 6. Required Documentation Corrections

The following documentation statements require correction:

### docs/QUESTION_IMPROVEMENT_BACKLOG.md
The "✅ RESOLVED" label on Exam D IMPROVE is overstated. Should read:

> Exam D named in-manifest IMPROVE items: ✅ RESOLVED  
> Exam D 28 unnamed IMPROVE items: ⚠️ UNVERIFIABLE — cannot be individually identified without re-audit  
> Exam D 2 fabricated IDs (civ-10-leave-001, civ-12-writ-001): ⚠️ UNRESOLVABLE — IDs do not exist in bank  
> Exam D 2 wrong-exam IDs (civ-04-exam-001, civ-08-cpa-001): ⚠️ NOT EXAM D QUESTIONS — exist in bank but not in D or any exam manifest

### docs/QUESTION_QUALITY_IMPROVEMENT_PLAN.md  
M4 milestone should note that Exam D IMPROVE is partially addressed, not fully resolved.

---

## 7. Recommendation

A **fresh psychometric re-audit of Exam D** (using actual manifest question IDs, not fabricated chapter-table IDs) is the only way to determine the current quality level and whether any IMPROVE items remain unaddressed. The re-audit should be scheduled as part of M5 (after all Phase 2K-Improve work on Exams C, D, E, F is complete).

Until the re-audit is completed, the correct documentation position is:
- Named D IMPROVE items: resolved
- Unnamed D IMPROVE items (28): addressed in part; status unknown
