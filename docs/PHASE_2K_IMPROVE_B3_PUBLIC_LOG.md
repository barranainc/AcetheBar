# Phase 2K-Improve-B3 — Public Law Improvement Log

**Date:** 2026-05-25  
**Scope:** All remaining Public Law IMPROVE questions in Generated Barrister C and F  
**Total improved:** 5 questions across 2 exams  
**Payloads re-baked:** `barc` (393,248 → 398,740 chars), `barf` (501,116 → 506,124 chars)  
**Validation:** 963 questions, 0 errors ✅  
**HTML validation:** all checks pass ✅  
**Overlap:** C∩D=0, C∩E=0, C∩F=0, D∩E=0, D∩F=0, E∩F=0, C∪D∪E∪F=640 unique ✅  
**Imported payloads:** unchanged (bar=191,500, sol=242,816, mini=171,132, abp=189,540, bar2=237,360) ✅  
**D/E payloads:** unchanged (bard=455,904, bare=534,820) ✅  
**PR payloads:** unchanged (prdra=293,132, prdrb=288,532, prb200=581,808) ✅

---

## Context

**D public law:** All 35 D public law questions confirmed clean in Phase 2K-D-Reaudit (95% PASS, no REWRITE). No B3 work needed.

**E public law:** All 14 E public law IMPROVE items resolved in Phase 2K-Improve-B1. No B3 work needed.

**C public law IMPROVE candidates (2 questions):**
- pub-02-s15-equal-001: Andrews outcome recalled by headnote; anti_idx=2; no application of analogous grounds criteria to a novel situation
- pub-02-s7-fundjust-001: Definitional threshold; only tests whether liberty is engaged (obviously yes for any imprisonment); does not test whether mandatory minimum violates PFOJ

**F public law IMPROVE candidates (3 questions):**
- pub-02-s15-006: Formal vs substantive equality tested abstractly via definitional call; options C and D obviously wrong
- pub-02-s6-001: Call asks for "scope" of s.6(2)(b) — definitional; correct answer recites s.6(3)(a) verbatim; one obviously wrong distractor
- pub-02-s3-001: Binary yes/no call on s.33 override; candidate answering by knowing s.33's scope list need not apply two-step analysis

**Exclusions confirmed:**
- pub-02-oakes-test-001 (C): Already rewritten in Phase 2K-Improve-A (Improve-A log confirms)
- pub-07-charter-dam-002 (F): Already rewritten in Phase 2K-Improve-A (REWRITE, not IMPROVE)
- D/E public law: All resolved as above

---

## Summary

| Exam | Questions improved | Correct answer changed |
|------|-------------------|----------------------|
| Exam C — Public Law | 2 | 0 |
| Exam F — Public Law | 3 | 0 |
| **Total** | **5** | **0** |

All improvements: updated `fact_pattern` (where needed), `call_of_question`, `options`, `explanation`, `why_A/B/C/D_wrong`, `exam_trigger_words`, `tested_concepts`, `difficulty` (where elevated), `estimated_time_seconds` (where increased), `updated_at` = "2026-05-25". `validation_status` and `correct_answer` unchanged on all questions.

---

## Exam C — Public Law (2 questions)

| question_id | file | correct_answer_changed | difficulty_changed | weakness_addressed | trap_types_added |
|---|---|---|---|---|---|
| pub-02-s15-equal-001 | ch02-charter.json | No | easy → medium | Andrews headnote recall; no application of analogous grounds criteria to novel ground | Enumerated-Only Trap (A), Intent Trap (C), Immutability-Absolutist Trap (D) |
| pub-02-s7-fundjust-001 | ch02-charter.json | No | easy → medium | Threshold-only question; does not test whether mandatory minimum violates PFOJ | Rule Trap (A — Parliamentary authority ≠ Charter compliance), Wrong-Section Trap (C — s.7/s.12 conflated), Overstatement Trap (D — discretion elimination ≠ automatic s.7 breach) |

### pub-02-s15-equal-001 — Detail

**Old scenario:** Provincial law requires Canadian citizenship for an administrative position. Permanent resident denied. Call: "Is citizenship an enumerated or analogous ground?"

**New scenario:** Provincial regulation requires Canadian citizenship or permanent residence for a subsidized professional development grant. Rodrigo (temporary foreign worker, Ontario work permit) denied. Call: "Applying the Andrews criteria, should a court recognize temporary foreign worker status as an analogous ground under s.15(1)?"

**Key changes:**
- Moved from known landmark (Andrews confirmed citizenship) to novel ground requiring application of Andrews criteria
- Candidate must identify the test (immutable or changeable only at personal cost; discrete minority; political powerlessness) and apply it to a novel ground
- Option A reframes as Enumerated-Only Trap (s.15(1) grounds are exhaustive)
- Option C adds Intent Trap (s.15 requires discriminatory intent — wrong; it is effects-based)
- Option D adds Immutability-Absolutist Trap (analogous grounds require full immutability — wrong; test allows "changeable only at unacceptable cost")
- Explanation distinguishes immutability test from absolute-immutability misconception and explains effects-based analysis
- difficulty: easy → medium; estimated_time_seconds: 90 → 120

### pub-02-s7-fundjust-001 — Detail

**Old scenario:** Same mandatory minimum cannabis trafficking scenario. Call: "What threshold triggers s.7 analysis?" (answer: liberty interest engaged by imprisonment — obviously yes)

**New scenario:** Same fact pattern; added defence counsel making s.7 argument + Crown counter-argument on s.91(27) authority. Call: "Is the mandatory minimum likely to violate s.7, and if so, what PFOJ does it most directly engage?"

**Key changes:**
- Moved from threshold question (step 1 only) to full two-step s.7 analysis (step 1 = liberty engaged; step 2 = does deprivation violate PFOJ?)
- Correct answer B requires knowing: (1) liberty is engaged, AND (2) overbreadth/gross disproportionality under Bedford/Carter is the applicable PFOJ test
- Option A = Rule Trap (s.91(27) jurisdiction does not exempt from Charter)
- Option C = Wrong-Section Trap (s.7 and s.12 are independent; s.12 finding is not prerequisite for s.7)
- Option D = Overstatement Trap (discretion elimination ≠ automatic s.7 breach; test is PFOJ, not discretion alone)
- difficulty: easy → medium; estimated_time_seconds: 90 → 120

---

## Exam F — Public Law (3 questions)

| question_id | file | correct_answer_changed | difficulty_changed | weakness_addressed | trap_types_added |
|---|---|---|---|---|---|
| pub-02-s15-006 | ch02-charter.json | No | medium (unchanged) | Definitional call "why is formal equality insufficient?"; Options C and D obviously wrong | Comparator-Group Trap (A), Intent Trap (C), Absolute-Deprivation Trap (D) |
| pub-02-s6-001 | ch02-charter.json | No | easy → medium | Definitional scope call; correct answer recites s.6(3)(a) in full; one obviously wrong distractor | Overstatement/No-Exception Trap (A), Factual-Comparator Trap (C), Wrong-Scope Trap (D) |
| pub-02-s3-001 | ch02-charter.json | No | easy → medium | Binary yes/no on s.33; does not require two-step analysis (s.33 + s.1 + Sauve) | Wrong-Scope Trap (A), Overstatement Trap (C — s.33 failure = automatic strike-down), Wrong-Ground Trap (D — redirect to s.15) |

### pub-02-s15-006 — Detail

**Old call:** "Why is formal equality — treating similarly situated people the same — insufficient to avoid a s.15 violation?" (definitional)

**New call:** "Has the claimant established a prima facie s.15 violation, and if so, which element of the Fraser v Canada framework is most directly engaged?"

**Key changes:**
- Fact pattern retained (disability benefit structure; higher costs for partially-working disabled persons)
- Old options A (formal equality sufficient) and D (good intentions) replaced with substantive traps:
  - New A = Comparator-Group Trap: law distinguishes within the disability group, not between disabled/non-disabled → no s.15 (wrong; intra-group distinctions can perpetuate disadvantage post-Fraser)
  - New C = Intent Trap: Parliament intended to incentivize employment → no discriminatory intent → no s.15 (wrong; s.15 is effects-based)
  - New D = Absolute-Deprivation Trap: s.15 only engages where claimant proves inability to meet basic needs (wrong; perpetuation of disadvantage through disproportionate burden is sufficient)
- Correct answer B now identifies the specific Fraser framework element (disproportionate burden perpetuating historical disadvantage) rather than defining substantive equality abstractly

### pub-02-s6-001 — Detail

**Old call:** "Under s.6(2)(b), what is the scope of the right of Canadian citizens and permanent residents to pursue gainful employment in any province?" (definitional/scope)

**New call:** "Should the engineer's challenge under s.6(2)(b) succeed?"

**Key changes:**
- Scenario enriched: Elena (12 years Ontario engineer) relocates to B.C.; her counsel argues the licensing process creates a practical province-of-origin distinction because B.C.-trained engineers face an easier path
- New call forces candidate to: (1) know s.6(2)(b) scope, (2) apply s.6(3)(a) general application exception, (3) assess whether B.C. requirement discriminates based on prior province of residence
- Option A = Overstatement Trap (absolute right without s.6(3)(a) exception)
- Option C = Factual-Comparator Trap (practical burden from non-recognition ≠ discrimination based on prior province of residence; the requirement applies equally to all)
- Option D = Wrong-Scope Trap (s.6 covers gainful employment, not just physical movement)
- difficulty: easy → medium; estimated_time_seconds: 90 → 120

### pub-02-s3-001 — Detail

**Old call:** "Can a provincial legislature use the s.33 notwithstanding clause to override s.3 democratic rights to disenfranchise prisoners?" (binary yes/no)

**New call:** "How should counsel advise the imprisoned person regarding his s.3 challenge to the disenfranchisement law?"

**Key changes:**
- Scenario enriched: Ontario legislation; Attorney General makes two arguments — (1) s.33 invoked; (2) alternatively, law justified under s.1
- New call requires advising on both arguments: (1) s.33 inapplicable to s.3 (expressly outside ss. 2 and 7–15 scope), AND (2) law must survive s.1, and Sauve makes that unlikely
- Option A = Wrong-Scope Trap (s.33 validly overrides s.3 — wrong; s.3 is excluded from s.33)
- Option C = Overstatement Trap (s.33 failure = automatic unconstitutionality without s.1 — wrong; s.1 must still be tested)
- Option D = Wrong-Ground Trap (redirect to s.15 as better vehicle — wrong; s.3 is the established and direct vehicle from Sauve)
- Correct answer B explains the full two-step: s.33 inapplicable + s.1 scrutiny + Sauve makes s.1 justification very unlikely
- difficulty: easy → medium; estimated_time_seconds: 90 → 120

---

## Post-Improvement Pipeline

| Step | Result |
|------|--------|
| `python3 tools/validate_question.py data/questions --summary` | 963 questions, 0 errors ✅ |
| Rebuild `barc` compact JSON from manifest IDs | 160 questions ✅ |
| Rebuild `barf` compact JSON from manifest IDs | 160 questions ✅ |
| Re-bake `barc` payload in index.html | 393,248 → 398,740 b64 chars ✅ |
| Re-bake `barf` payload in index.html | 501,116 → 506,124 b64 chars ✅ |
| `python3 tools/validate_html.py` | All checks pass ✅ |
| C∩D = 0 | ✅ |
| C∩E = 0 | ✅ |
| C∩F = 0 | ✅ |
| D∩E = 0 | ✅ |
| D∩F = 0 | ✅ |
| E∩F = 0 | ✅ |
| C∪D∪E∪F = 640 unique IDs | ✅ |
| Imported payloads unchanged (bar/sol/mini/abp/bar2) | ✅ |
| D/E payloads unchanged (bard/bare) | ✅ |
| PR payloads unchanged (prdra/prdrb/prb200) | ✅ |
