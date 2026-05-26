# Phase 2W — Validator Warning Audit

**Date:** 2026-05-25  
**Baseline:** 963 questions, 0 errors, **798 warnings**

---

## Warning Categories and Classification

| # | Category | Count | Classification | Rationale |
|---|---|---|---|---|
| 1 | explanation: Must begin with 'Under...' | 657 | SAFE STYLE FIX | Purely formatting; legal content unchanged |
| 2 | estimated_time_seconds/difficulty mismatch | 56 | SAFE STYLE FIX | Adjust seconds to minimum valid for difficulty |
| 3 | source_ref: case_law_only | 58 | IGNORE/ACCEPT | These questions test case law; no statute section to cite |
| 4 | source_ref: lso_bylaw_no_section | 16 | IGNORE/ACCEPT | By-Laws cited at chapter level; no subsection available |
| 5 | source_ref: PR rules plural ("Rules X.X-Y") | 9 | SAFE STYLE FIX | Change "Rules X.X-Y, X.X-Z" → "Rule X.X-Y (see also Rules X.X-Z)" |
| 6 | source_ref: Charter multi-section | 2 | IGNORE/ACCEPT | Multi-section Charter citations are accurate and intentional |

**Total SAFE STYLE FIX:** 722 warnings  
**Total IGNORE/ACCEPT:** 76 warnings  

---

## Category 1 — Explanation Format (657 warnings)

Validator check: `re.match(r'^Under\s', expl.strip(), re.IGNORECASE)`

### Fix strategy by opening pattern

| Opening Pattern | Count | Fix Strategy |
|---|---|---|
| `^Rule\s` or `^Rules\s` | 95 | Prepend "Under " |
| `^Section\s+\d` | 90 | Replace "Section " with "Under s." |
| Other + valid statute SR | 219 | Prepend "Under [SR], " |
| `^The [non-statute]` + valid SR | 66 | Prepend "Under [SR], the..." |
| `^The [statute name]` | 39 | Change "The " to "Under the " |
| `^By-Law\s` | 27 | Prepend "Under " |
| `^Family Law Act\b` | 13 | Prepend "Under the " |
| `^FLA\b` | 15 | Prepend "Under " |
| `^Divorce Act\b` | 13 | Prepend "Under the " |
| `^Federal Child Support\b` | 13 | Prepend "Under the " |
| `^CYFSA\b` | 11 | Prepend "Under " |
| `^Sections\s+\d` | 3 | Replace "Sections " with "Under ss." |
| `^FCSG\b` | 1 | Prepend "Under the " |
| Case-law/no SR — SKIP | 52 | ACCEPT — cannot fix without legal change |

**Fixable explanations:** ~605  
**Accepted explanation warnings:** ~52 (pure case-law contexts)

### Known SKIP explanations (case-law-only, no statute prefix available)
These explanations legitimately discuss case-law principles (R v X, Stinchcombe, Kerr v Baranow, DBS v SRG, etc.) and have case-law-only source_references. Fixing would require inserting a statute citation that is not supported by the fact pattern.

---

## Category 2 — Time/Difficulty Mismatches (56 warnings)

| Mismatch | Count | Fix |
|---|---|---|
| 90s but difficulty=hard (expected 120–200s) | 33 | Set to 120 |
| 120s but difficulty=exam_trap (expected 150–300s) | 9 | Set to 150 |
| 90s but difficulty=exam_trap (expected 150–300s) | 7 | Set to 150 |
| 75s but difficulty=medium (expected 90–150s) | 4 | Set to 90 |
| 80s but difficulty=medium (expected 90–150s) | 3 | Set to 90 |

**All 56 fixable** by adjusting `estimated_time_seconds` to the minimum valid value for the difficulty.

---

## Category 3 — Source Ref Case Law Only (58 warnings) — ACCEPT

Questions that test specific case-law holdings (R v cases, SCR citations, etc.) with no applicable statute section. These are correct and intentional.

Examples: RJR-MacDonald, Hryniak, Fong v Chan, Kerr v Baranow, DBS v SRG, R v Stinchcombe, R v Mohan, R v Lifchus, etc.

---

## Category 4 — LSO By-Law No Section (16 warnings) — ACCEPT

Questions citing LSO By-Law 9, By-Law 6, By-Law 7.1 at chapter level. No specific subsection available without external law research.

---

## Category 5 — PR Rules Plural (9 warnings) — SAFE STYLE FIX

Validator pattern: `Rule\s` (singular + space). "Rules 3.3-3, 3.3-4, 3.3-5" fails because "Rules" ≠ "Rule ".

**Fix:** Change first rule reference to singular; put rest in parenthetical.

| Before | After |
|---|---|
| `Rules of Professional Conduct (LSO), Rules 3.3-3, 3.3-4, 3.3-5` | `Rules of Professional Conduct (LSO), Rule 3.3-3 (see also Rules 3.3-4, 3.3-5)` |
| `Rules of Professional Conduct (LSO), Rules 3.4-1, 3.4-5 (multiple co-accused...)` | `Rules of Professional Conduct (LSO), Rule 3.4-1 (see also Rule 3.4-5; multiple co-accused...)` |
| `Rules of Professional Conduct (LSO), Rules 3.3-1, 5.1-2 (...)` | `Rules of Professional Conduct (LSO), Rule 3.3-1 (see also Rule 5.1-2; ...)` |
| `Rules of Professional Conduct (LSO), Rules 3.3-1, 3.7-9 (...)` | `Rules of Professional Conduct (LSO), Rule 3.3-1 (see also Rule 3.7-9; ...)` |
| `Rules of Professional Conduct (LSO), Rules 3.3-1, 3.4-10 (...)` | `Rules of Professional Conduct (LSO), Rule 3.3-1 (see also Rule 3.4-10; ...)` |

---

## Category 6 — Charter Multi-Section (2 warnings) — ACCEPT

Two questions citing multiple Charter sections (e.g., "Canadian Charter of Rights and Freedoms, ss. 8, 24(2)"). These are accurate multi-section citations and should not be reduced to a single section.

---

## Projected Warning Reduction

| Category | Before | After Fix | Remaining |
|---|---|---|---|
| Explanation format | 657 | fix ~605 | ~52 |
| Time/difficulty mismatch | 56 | fix 56 | 0 |
| Case-law source_ref | 58 | ACCEPT | 58 |
| LSO By-Law source_ref | 16 | ACCEPT | 16 |
| PR rules plural source_ref | 9 | fix 9 | 0 |
| Charter multi-section source_ref | 2 | ACCEPT | 2 |
| **TOTAL** | **798** | | **~128** |

**Expected reduction: ~84%** (798 → ~128)

Note: "under 50" ideal target not achievable without modifying 76 ACCEPT source_ref citations (case-law only, LSO By-Law, Charter) or 52 SKIP explanation openings (case-law-only explanations). These require legal interpretation and are out of scope per Phase 2W constraints.
