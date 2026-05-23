# Blueprint Audit Report — Phase 1C

**Date:** 2026-05-23  
**Auditor:** Phase 1C automated + manual inspection  
**Scope:** All five Barrister subject blueprints + `data/blueprints/barrister-subjects.json`  
**Status:** ✅ FIXES APPLIED — GO for Phase 2 question generation (see § 10)

---

## 1. Summary Statistics (post-fix)

| Subject | Chapters | Topics | Subtopics | PR-angle subtopics | Target Q | Min Q |
|---------|----------|--------|-----------|-------------------|----------|-------|
| Civil Litigation | 17 | 20 | 63 | 32 (51%) | 250 | 135 |
| Criminal Law | 14 | 19 | 42 | 20 (48%) | 180 | 105 |
| Family Law | 16 | 17 | 44 | 24 (55%) | 181 | 104 |
| Public Law | 11 | 12 | 30 | 23 (77%) | 120 | 65 |
| Professional Responsibility | 13 | 14 | 37 | 34 (92%) | 159 | 87 |
| **TOTAL** | **71** | **82** | **216** | **133 (62%)** | **890** | **496** |

### Exam Assembly Targets (added to `barrister-subjects.json`)

| Mode | Questions | Notes |
|------|-----------|-------|
| Full Barrister mixed exam | 160 | CIV 43 + CRIM 43 + FAM 39 + PUB 35 |
| Subject drill (any subject) | 10–full bank | All 5 subjects available |
| PR standalone drill | 25 (recommended) | From PR bank only |
| PR overlay exam | 160 | Draws pr_angle.applicable=true questions preferentially |
| Weak-area drill | Variable | Requires Phase 4 analytics |

---

## 2. JSON Validity

All six blueprint files parse without error:

| File | Valid JSON | Chapters |
|------|-----------|---------|
| `barrister-subjects.json` | ✅ | — |
| `civil-litigation.json` | ✅ | 17 |
| `criminal-law.json` | ✅ | 14 |
| `family-law.json` | ✅ | 16 |
| `public-law.json` | ✅ | 11 |
| `professional-responsibility.json` | ✅ | 13 |

---

## 3. Required Schema Fields

Checked all chapters, topics, and subtopics against required field lists:

**Required chapter fields:** `chapter_number`, `chapter_title`, `chapter_slug`, `lso_dtoc_ref`, `priority_weight`, `topics`  
**Required topic fields:** `topic_id`, `topic_heading`, `subtopics`  
**Required subtopic fields:** `subtopic_id`, `subtopic_heading`, `target_question_count`, `minimum_question_count`, `difficulty_split`, `pr_angle_possible`, `priority_weight`, `primary_statute`, `key_sections`, `common_misconceptions`, `notes_for_generation`

**Result:** ✅ All required fields present across all 216 subtopics and 71 chapters.

---

## 4. Duplicate ID Check

All topic IDs and subtopic IDs tested for uniqueness within each subject file.

| Subject | Duplicate topic_ids | Duplicate subtopic_ids |
|---------|--------------------|-----------------------|
| Civil Litigation | None | None |
| Criminal Law | None | None |
| Family Law | None | None |
| Public Law | None | None |
| Professional Responsibility | None | None |

**Result:** ✅ No duplicate IDs found.

---

## 5. Target / Minimum Consistency

Verified that `total_target_questions` and `total_minimum_questions` at the root of each blueprint file equal the sum of all subtopic values.

**Pre-fix finding:** `professional-responsibility.json` had `total_minimum_questions = 70` but the computed sum was 87. The stale value was from before the Phase 1B augmentation script updated the blueprint.

**Fix applied:** `professional-responsibility.json → total_minimum_questions`: 70 → **87**  
**Fix applied:** `barrister-subjects.json` PR entry `total_minimum_questions`: 70 → **87**

**Post-fix result:** ✅ All five blueprints pass. Root totals match computed sums exactly.

---

## 6. Difficulty Split Sums

All 216 subtopics verified: `easy + medium + hard + exam_trap == target_question_count`.

**Result:** ✅ No split arithmetic errors. All 216 subtopic splits are internally consistent.

---

## 7. Priority Weight Values

All chapter-level and subtopic-level `priority_weight` values verified to be integers in {1, 2, 3, 4, 5}.

**Result:** ✅ No out-of-range priority weights.

---

## 8. Minimum ≤ Target Check

All 216 subtopics verified: `minimum_question_count ≤ target_question_count`.

**Result:** ✅ No violations.

---

## 9. Metadata Inconsistencies Found and Fixed

### 9.1 `total_exam_questions` — FIXED

**Pre-fix:** `barrister-subjects.json._meta.total_exam_questions = 220`  
**Problem:** The actual LSO Barrister exam is 160 questions. The value 220 was a placeholder from Phase 1A.  
**Fix applied:** 220 → **160**

### 9.2 `approximate_exam_questions` per subject — FIXED

The mixed Barrister exam breakdown provided by the user (Civil 43, Criminal 43, Family 39, Public 35 = 160 total):

| Subject | Pre-fix value | Post-fix value |
|---------|--------------|----------------|
| Civil Litigation | 55 | **43** |
| Criminal Law | 55 | **43** |
| Family Law | 55 | **39** |
| Public Law | 33 | **35** |
| Professional Responsibility | 22 | **removed** — replaced with `exam_mode` field explaining PR's two-mode treatment |

### 9.3 Exam Assembly Rules — ADDED

A new `exam_assembly_rules` block was added to `barrister-subjects.json` documenting all five exam modes: `full_barrister_exam`, `subject_drill`, `pr_standalone_drill`, `pr_overlay_exam`, `weak_area_drill`.

### 9.4 Statute Name Normalisation — FIXED

11 subtopics used abbreviated statute names without full citations. All normalised to standard form:

| Short form | Normalised to |
|-----------|--------------|
| `"Rules of Civil Procedure"` | `"Rules of Civil Procedure, R.R.O. 1990, Reg. 194"` |
| `"Criminal Code"` | `"Criminal Code, R.S.C. 1985, c. C-46"` |
| `"Children's Law Reform Act"` | `"Children's Law Reform Act, R.S.O. 1990, c. C.12"` |
| `"Family Law Act"` | `"Family Law Act, R.S.O. 1990, c. F.3"` |

Affected files: `civil-litigation.json` (2), `criminal-law.json` (5), `family-law.json` (4).

---

## 10. Suspicious Reference Flags (legal/source review required — NOT changed)

The following items were identified during the audit and flagged for human review before question generation begins. **None of these were silently changed.**

### Flag A — `Kerr v Baranow` as `primary_statute`

**Location:** `family-law.json`, Ch13, subtopic `unjust_enrichment_constructive_trust`  
**Current value:** `"primary_statute": "Common Law (Kerr v Baranow, 2011 SCC 10)"`  
**Issue:** The `primary_statute` field is intended for a statute, not a case citation. `Kerr v Baranow, 2011 SCC 10` is the leading SCC case on unjust enrichment between cohabitants; it is a valid source of law for this subtopic, but the field name is misleading.  
**Recommended fix:** Retain the case reference in `notes_for_generation` and `key_sections`, and either set `primary_statute = "Common Law — unjust enrichment"` or leave as is with this note.  
**Reviewer action required:** Confirm whether this subtopic should be kept; confirm that Kerr v Baranow is cited in the 2026 LSO Barrister materials for Family Law.

### Flag B — By-Law 7 vs By-Law 9 Naming in PR Blueprint

**Location:** `professional-responsibility.json`, Ch6 (all three trust accounting subtopics)  
**Current value:** `"primary_statute": "By-Law 9 (Financial Transactions and Records)"`  
**Issue:** The Law Society of Ontario currently structures its By-Laws as follows:
- **By-Law 9** — governs financial transactions and records (trust money, client funds, cash transactions)
- **By-Law 7** — governs financial statements for law firms (annual filings)  

The description "Financial Transactions and Records" attached to By-Law 9 appears correct for trust accounting purposes. However, the `barrister-subjects.json` index also lists `"By-Law 7 (Financial Transactions and Records)"` in the `primary_statutes` array for the PR subject — which duplicates the description and may confuse By-Law 7 (financial statements) with By-Law 9 (trust records).  
**Reviewer action required:** Confirm that By-Law 9 is the correct by-law for trust deposits, trust withdrawals, and trust records. Confirm By-Law 7's role (if any) in the Barrister exam scope. If By-Law 7 is not separately tested, remove it from the index `primary_statutes` list.

### Flag C — `lso_weight_percent` vs 43/43/39/35 allocation

**Location:** `barrister-subjects.json`, all four substantive subjects  
**Current values:** Civil 25%, Criminal 25%, Family 25%, Public 15%  
**Inconsistency:** The user-provided exam allocation (43+43+39+35=160) implies:
- Civil: 43/160 = 26.9% (vs stated 25%)
- Criminal: 43/160 = 26.9% (vs stated 25%)
- Family: 39/160 = 24.4% (vs stated 25%)
- Public: 35/160 = 21.9% (vs stated 15%)

**Note:** The `lso_weight_percent` values may reflect the LSO's officially stated percentage allocations from the 2026 materials, which may differ from the raw question count ratios due to rounding or a different LSO allocation formula. The values were **not changed** because altering officially stated LSO percentages requires confirmation from the source materials.  
**Reviewer action required:** Confirm the LSO's stated percentage allocations from the 2026 Barrister Examination Materials. Update `lso_weight_percent` if the percentages differ from the current values.

### Flag D — `Solicitors Act` in PR Blueprint

**Location:** `professional-responsibility.json`, Ch5 (Duties to Clients), subtopic `contingency_fee_arrangements`  
**Current value:** `"primary_statute": "Solicitors Act, R.S.O. 1990, c. S.15"`  
**Issue:** The Solicitors Act governs contingency fee agreements in Ontario (ss. 28.1 and 28.2 as amended). However, the LSO Rules of Professional Conduct Rule 3.6 (fees and disbursements) also speaks to contingency fees. Confirm that the Solicitors Act is within scope of the 2026 Barrister examination.  
**Reviewer action required:** Confirm the Solicitors Act is referenced in the 2026 LSO Barrister study materials. If not, revise the primary statute to `"Rules of Professional Conduct (LSO), Rule 3.6"`.

### Flag E — Over-Fragmented Chapters (deliberate — no change recommended)

Two chapters were flagged by the audit for having more than 6 subtopics:

| Chapter | Subject | Subtopics | Assessment |
|---------|---------|-----------|------------|
| Limitation Periods (Ch02) | Civil Litigation | 7 | Deliberate: covers basic period, discoverability, ultimate period, suspension, agreement to vary, no-limitation claims, demand obligations — each is a distinct exam-tested rule. Retain. |
| Charter Rights — Arrest, Detention, Search (Ch02) | Criminal Law | 7 | Deliberate: covers ss.9, 10(b), 8, 487, 495, 494, citizen's arrest — each is a high-frequency distinct exam topic. Retain. |

**Verdict:** Both are appropriate given the density of exam-tested rules in these areas. No action required. Flagged for awareness only.

---

## 11. Notes for Generation Completeness

All 216 `notes_for_generation` fields were checked for minimum length (≥ 20 characters) and content.

**Result:** ✅ All 216 subtopics have substantive notes (all exceed 80 characters). No empty or placeholder notes found.

---

## 12. Common Misconceptions Quality

All 216 subtopics verified: `common_misconceptions` is a non-empty list. All individual misconception entries exceed 30 characters with specific legal content.

**Result:** ✅ No generic or vague misconceptions detected. No "students may confuse" without specifics.

---

## 13. Coverage Report Results (post-fix)

All five coverage reports execute without errors:

```
civil-litigation:            OVERALL: 0/250 verified questions | 63 subtopics below minimum
criminal-law:                OVERALL: 0/180 verified questions | 42 subtopics below minimum
family-law:                  OVERALL: 0/181 verified questions | 44 subtopics below minimum
public-law:                  OVERALL: 0/120 verified questions | 30 subtopics below minimum
professional-responsibility: OVERALL: 0/159 verified questions | 37 subtopics below minimum
```

Zero verified questions and all subtopics below minimum is **expected** — no questions have been generated yet (Phase 2 pending). The coverage tool is functioning correctly; the 0/target values confirm the blueprint loads and counts match.

---

## 14. Files Changed in Phase 1C

| File | Change |
|------|--------|
| `data/blueprints/barrister-subjects.json` | Fixed `total_exam_questions` 220→160; fixed all `approximate_exam_questions`; added `exam_assembly_rules` block; fixed PR `total_minimum_questions` 70→87; updated `last_updated` date; added `_meta.notes` clarifying PR treatment |
| `data/blueprints/professional-responsibility.json` | Fixed `total_minimum_questions` 70→87 |
| `data/blueprints/civil-litigation.json` | Normalised 2 statute names |
| `data/blueprints/criminal-law.json` | Normalised 5 statute names |
| `data/blueprints/family-law.json` | Normalised 4 statute names |
| `docs/BLUEPRINT_AUDIT_REPORT.md` | **Created** (this file) |

**Files NOT touched:** `index.html`, `bar2.html`, `Dockerfile`, any existing exam data files.

---

## 15. Remaining Issues for Legal/Source Review

Before question generation begins for any flagged subtopic, a reviewer must confirm:

| Priority | Flag | Subtopic(s) | Action |
|----------|------|-------------|--------|
| 🔴 High | Flag B — By-Law 7 vs By-Law 9 naming | PR Ch6 trust accounting (3 subtopics) | Confirm By-Law numbers; update `barrister-subjects.json` primary_statutes if By-Law 7 is not separately tested |
| 🟡 Medium | Flag C — `lso_weight_percent` vs allocation | All 4 substantive subjects | Confirm official LSO percentages; update if needed |
| 🟡 Medium | Flag A — Kerr v Baranow as `primary_statute` | FAM Ch13 `unjust_enrichment_constructive_trust` | Normalise field; confirm case is in LSO 2026 materials |
| 🟢 Low | Flag D — Solicitors Act scope | PR Ch5 `contingency_fee_arrangements` | Confirm Solicitors Act is in Barrister scope |
| 🟢 Low | Flag E — Over-fragmented chapters | CIV Ch02, CRIM Ch02 | Flagged as deliberate. No change required. |

---

## 16. Final Go/No-Go Assessment

### ✅ GO — Phase 2 question generation may proceed

**Basis:**

1. **JSON validity:** All 6 blueprint files parse without error.
2. **Schema completeness:** All 216 subtopics contain every required field.
3. **No duplicate IDs** across any subject.
4. **Difficulty splits verified:** All 216 subtopics have splits that sum exactly to target.
5. **Total consistency verified:** Root `total_target_questions` and `total_minimum_questions` match computed sums in all 5 blueprints.
6. **Exam assembly corrected:** `barrister-subjects.json` now correctly reflects 160-question exam with 43/43/39/35 allocation.
7. **Coverage tool functional:** All 5 coverage reports execute cleanly.
8. **No non-LSO sources detected** in statute references or notes.
9. **Notes for generation** are substantive in all 216 subtopics.

**Condition on flagged items:** The four flagged issues (Flags A–D) are **not blockers** for Phase 2. They involve specific subtopics that can be held back from the first generation batch while the others proceed. The first-batch subtopics (all ★5 priority, anchored to clear statute sections) are unaffected by any flag.

**Recommended Phase 2 starting point:** Begin with the 25-question first-batch subtopics per subject (all ★5 priority, all from well-established statutes), as identified in the Phase 1B output. The flagged subtopics (Flag A: Ch13 unjust enrichment; Flag B: Ch6 trust accounting; Flag D: Ch5 contingency fees) should be generated only after the relevant reviewer confirms the source reference.

---

*Report generated by Phase 1C audit — barranainc/AcetheBar*
