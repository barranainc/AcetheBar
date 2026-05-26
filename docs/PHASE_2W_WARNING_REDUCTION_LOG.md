# Phase 2W — Validator Warning Reduction Log

**Completed:** 2026-05-25  
**Baseline:** 963 questions, 0 errors, **798 warnings**  
**Result:** 963 questions, 0 errors, **123 warnings** (85% reduction)

---

## Summary

Phase 2W reduced validator warnings from 798 to 123 through three categories of safe style fixes:

1. **Explanation opening format** — 610 fixes (657 warnings → 47 remaining)
2. **Time/difficulty mismatches** — 56 fixes (56 warnings → 0 remaining)
3. **PR rules plural source_ref** — 9 fixes (9 warnings → 0 remaining)

No correct answers were changed. No legal substance was altered. No question IDs were added or removed. No manifests were modified. No exam selections were changed.

---

## Fix Scripts Created

| Script | Purpose | Questions Fixed |
|---|---|---|
| `tools/fix_2w_pr_rules_plural.py` | Fix "Rules X.X-Y, X.X-Z" → "Rule X.X-Y (see also Rules X.X-Z)" | 9 |
| `tools/fix_2w_time_difficulty.py` | Raise `estimated_time_seconds` to minimum for difficulty | 56 |
| `tools/fix_2w_explanation_format.py` | Transform explanation openings to start with "Under " | 610 |

Scripts were run in this order: PR plural first (so fixed SRs are available for explanation prefix logic), then time/difficulty, then explanation format.

---

## Explanation Format Fix Details

The explanation validator checks: `re.match(r'^Under\s', expl.strip(), re.IGNORECASE)`

### Transform strategies applied (in priority order)

| Pattern | Count Fixed | Transformation |
|---|---|---|
| `^Rules?\s` | ~95 | Prepend "Under " |
| `^Section\s+\d` | ~90 | Replace "Section " with "Under s." |
| `^Sections\s+\d` | ~3 | Replace "Sections " with "Under ss." |
| `^By-Law\s\d` | ~27 | Prepend "Under " |
| `^FLA\b` | ~15 | Prepend "Under " |
| `^CYFSA\b` | ~11 | Prepend "Under " |
| `^Divorce Act\b` | ~13 | Prepend "Under the " |
| `^Family Law Act\b` | ~13 | Prepend "Under the " |
| `^Federal Child Support\b` | ~13 | Prepend "Under the " |
| `^FCSG\b` | ~1 | Prepend "Under the " |
| `^The [known statute]` | ~39 | Change "The " → "Under the " |
| `^The [other]` + valid statute SR | ~66 | Prepend "Under [SR], the ..." |
| `[other]` + valid statute SR | ~219 | Prepend "Under [SR], ..." |

### Accepted (SKIP) — 47 remaining
Explanations where the context is purely case-law (R v X, Stinchcombe, Kerr v Baranow, DBS v SRG, RJR-MacDonald, etc.) and there is no valid statute SR available as prefix. Changing these would require inserting a statutory citation not supported by the question's source_reference, which would change legal substance.

---

## Time/Difficulty Fix Details

Raised `estimated_time_seconds` to the minimum valid value for the difficulty level.

| Mismatch | Count | Fix |
|---|---|---|
| 90s / hard (expected 120–200s) | 33 | → 120s |
| 120s / exam_trap (expected 150–300s) | 9 | → 150s |
| 90s / exam_trap (expected 150–300s) | 7 | → 150s |
| 75s / medium (expected 90–150s) | 4 | → 90s |
| 80s / medium (expected 90–150s) | 3 | → 90s |

Files affected: ch04-service, ch10-offers-settlement, ch11-trial, ch12-costs, ch13-appeals, ch14-enforcement, ch15-default (civil); ch02-charter-arrest, ch05-pre-trial, ch07-evidence, ch08-defences, ch09-sentencing, ch10-ycja (criminal); ch02-divorce, ch05-spousal-support, ch06-child-support, ch07-parenting, ch08-child-protection, ch09-domestic-contracts, ch10-fro, ch13-common-law (family); ch05-duties, ch06-trust, ch07-court-duties, ch09-withdrawal, ch11-discipline (PR).

---

## PR Rules Plural Fix Details

Validator pattern requires `Rule\s` (singular Rule + space). "Rules" (plural) failed the check.

| Before | After |
|---|---|
| `..., Rules 3.3-3, 3.3-4, 3.3-5` | `..., Rule 3.3-3 (see also Rules 3.3-4, 3.3-5)` |
| `..., Rules 3.3-1, 3.4-10 (former joint client confidentiality)` | `..., Rule 3.3-1 (see also Rule 3.4-10; former joint client confidentiality)` |
| `..., Rules 3.3-1, 3.7-9 (confidentiality on withdrawal)` | `..., Rule 3.3-1 (see also Rule 3.7-9; confidentiality on withdrawal)` |
| `..., Rules 3.3-1, 5.1-2 (confidentiality and client dishonesty)` | `..., Rule 3.3-1 (see also Rule 5.1-2; confidentiality and client dishonesty)` |
| `..., Rules 3.4-1, 3.4-5 (multiple co-accused — joint retainer)` | `..., Rule 3.4-1 (see also Rule 3.4-5; multiple co-accused — joint retainer)` |

Questions fixed: pr-03-confid-excep-001 through 005, pr-03-jt-ret-conf-001, pr-03-withdraw-conf-001, pr-03-cl-dishon-001, pr-04-mult-def-001

---

## Accepted Warnings — 123 Remaining

All remaining warnings are classified ACCEPT — no fix possible without changing legal substance.

| Category | Count | Reason |
|---|---|---|
| Explanation format (case-law-only) | 47 | No statute SR; changing would alter substance |
| Source_ref case-law-only | 58 | Accurate citations; no statute section to add |
| Source_ref LSO By-Law no section | 16 | Accurate chapter-level citations |
| Source_ref Charter multi-section | 2 | Accurate multi-section citations |
| **Total** | **123** | |

---

## Payload Rebuild

All affected generated exam payloads were rebuilt from existing manifests (no re-randomization):

| Payload | Questions | Before (b64 len) | After (b64 len) |
|---|---|---|---|
| barc | 160 | 413,636 | 417,840 |
| bard | 160 | — | 456,836 |
| bare | 160 | — | 537,976 |
| barf | 160 | — | 517,940 |
| prdra | 100 | — | 303,232 |
| prdrb | 100 | — | 296,996 |
| prb200 | 200 | — | 600,372 |

Note: bard and bare were added to the rebuild script (`tools/rebuild_barc_barf_payloads.py`) during this phase.

---

## Integrity Verification

- ✅ Total questions: 963 (unchanged)
- ✅ Total errors: 0 (unchanged)
- ✅ Exam C: 160 unique IDs
- ✅ Exam D: 160 unique IDs
- ✅ Exam E: 160 unique IDs
- ✅ Exam F: 160 unique IDs
- ✅ C ∩ F = 0
- ✅ C ∪ D ∪ E ∪ F = 640 unique IDs
- ✅ PR Drill A: 100 questions
- ✅ PR Drill B: 100 questions
- ✅ PR Bank 200: 200 questions
- ✅ HTML validation: passes all checks

---

## Constraints Respected

- ✅ No correct_answer changes
- ✅ No legal rule or legal conclusion changes
- ✅ No statutory/rule citation changes (except pure formatting: Rules plural → Rule singular)
- ✅ No fact pattern substance changes
- ✅ No options substance changes
- ✅ No source_reference substance changes
- ✅ No new question IDs generated
- ✅ No question IDs removed
- ✅ No re-randomization
- ✅ No manifest changes
- ✅ Imported exam payloads untouched: bar, sol, mini, abp, bar2
- ✅ No outside law used
