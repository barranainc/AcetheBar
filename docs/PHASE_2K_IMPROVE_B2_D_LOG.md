# Phase 2K-Improve-B2 — Generated Barrister D Improvement Log

**Date:** 2026-05-25  
**Scope:** All remaining IMPROVE-status questions in Generated Barrister D after Phase 2K-Improve-A  
**Total improved:** 7 questions across 4 subjects  
**Payload re-baked:** `bard` only (455,904 chars, was 441,852)  
**Validation:** 963 questions, 0 errors ✅  
**HTML validation:** all checks pass ✅  
**Overlap:** D∩C=0, D∩E=0, D∩F=0, C∪D∪E∪F=640 unique ✅  
**Imported payloads:** unchanged (bar=191,500, sol=242,816, mini=171,132, abp=189,540, bar2=237,360) ✅  
**C/E/F payloads:** unchanged (barc=393,248, bare=534,820, barf=501,116) ✅  
**PR payloads:** unchanged (prdra=293,132, prdrb=288,532, prb200=581,808) ✅

---

## Context

The Phase 2K audit of Exam D identified 41 IMPROVE and 10 REWRITE questions. All 10 REWRITE questions (7 unique: crim-02-sw-issu-001, crim-09-purpose-001, crim-10-ycja-def-001, crim-11-sum-app-001, fam-06-cs-table-001, fam-07-parplan-001, pub-04-div-court-001 — plus 3 civil rewritten in Phase 2K-Improve-A for other exams: civ-03-strike-001, civ-04-exam-001, civ-08-cpa-001) were resolved in Phase 2K-Improve-A.

Two audit IMPROVE items (civ-10-leave-001, civ-12-writ-001) used fabricated IDs not present in the bank; no corresponding source questions exist. One item (crim-06-burden-001) was explicitly accepted as a foundational easy anchor by the audit.

Phase 2K-Improve-B2 addressed the remaining weaknesses by systematically reviewing all easy-difficulty D questions with `updated_at=2026-05-24` and improving those with list-recall structure or thin distractors.

---

## Summary

| Subject | Questions improved | Correct answer changed |
|---|---|---|
| Civil Litigation | 3 | 0 |
| Criminal Law | 1 | 0 |
| Family Law | 1 | 0 |
| Public Law | 2 | 0 |
| **Total** | **7** | **0** |

All improvements: updated `fact_pattern`, `call_of_question`, `options`, `explanation`, `why_A/B/C/D_wrong`, `exam_trigger_words`, `tested_concepts`, `updated_at` = "2026-05-25". `validation_status` and `correct_answer` left unchanged on all questions.

Questions assessed as PASS and left unchanged: civ-01-hier-002, civ-04-pers-001, civ-05-def-001, crim-01-juris-001, fam-02-coroll-001, fam-08-cwo-002, fam-09-dc-form-001, fam-10-fro-reg-001, fam-13-cl-prop-001.

---

## Civil Litigation (3 questions)

| question_id | file | correct_answer_changed | weakness_addressed | trap_types_added |
|---|---|---|---|---|
| civ-01-hier-001 | ch01-court-hierarchy.json | No | Call was "which statement is correct" with no application scenario; Options A/C/D implausible to any knowledgeable candidate | Overstatement Trap (A, C), Wrong Forum/Procedure Trap (D) |
| civ-10-ots-001 | ch10-offers-settlement.json | No | Generic rule-recall call; Option A (judicial approval) obviously absurd; no scenario forcing application | Pragmatic Bluff (A), Wrong Forum/Procedure Trap (B), Wrong Timeline Trap (D) |
| civ-12-cost-002 | ch12-costs.json | No | Generic "what document" call; Option D (Court of Appeal) obviously wrong; no scenario distinguishing costs outline from bill of costs | Misapplied Tool (A), Wrong Forum/Procedure Trap (C, D) |

### Per-question detail

**civ-01-hier-001**
- Added named parties (Ramirez v. Northwood), a concrete adversarial motion to transfer to Small Claims Court, and a direct call asking whether the court should grant the motion
- Options A/C/D rebuilt as Overstatement Traps: A invents a $200K ceiling on SCJ monetary jurisdiction, C creates a $2M cap for commercial claims; D ("shares jurisdiction equally with Divisional Court") is a Wrong Forum trap
- Explanation applies s.11 of the Courts of Justice Act to the specific facts rather than restating the rule

**civ-10-ots-001**
- New scenario: Delacroix makes both an oral telephone proposal AND a written signed email offer for $95K; plaintiff later recovers $80K; call asks which proposal (if either) attracts r.49.10 cost consequences
- Option A (both qualify — genuine intent is enough) = Pragmatic Bluff
- Option B (neither — must be filed with court) = Wrong Forum/Procedure Trap
- Option D (neither — offers after discoveries are barred) = Wrong Timeline Trap
- Forces candidate to know that r.49.02 requires writing + signature; oral offers do not qualify

**civ-12-cost-002**
- New scenario: Vasquez v. Drummond; judge explicitly directs formal assessment rather than summary fixing; call asks what document the successful party must serve AND whether Drummond's consent matters
- Option A conflates costs outline (summary fixing) with bill of costs (formal assessment) = Misapplied Tool
- Option C directs the process to the trial judge with the wrong document = Wrong Forum/Procedure Trap
- Option D invents a Divisional Court leave requirement = Wrong Forum/Procedure Trap

---

## Criminal Law (1 question)

| question_id | file | correct_answer_changed | weakness_addressed | trap_types_added |
|---|---|---|---|---|
| crim-05-plea-001 | ch05-pre-trial.json | No | List-recall: candidate matched abstract option bundles to s.606(1.1) requirements; Options A/D obviously wrong | General Rule Trap (A), Overstatement Trap (B), Misapplied Tool (D) |

### Per-question detail

**crim-05-plea-001**
- Placed candidate in active plea hearing; three of four s.606(1.1) conditions clearly satisfied on record (voluntariness, understanding of charge, understanding of consequences), but factual sufficiency is thrown into doubt by an equivocal "I guess so" response
- Option A (three of four met, accept the plea) = General Rule Trap
- Option B (memory gap = not voluntary) = Overstatement Trap
- Option D (admissibility analysis substituted for factual sufficiency) = Misapplied Tool
- Difficulty raised easy → medium; estimated_time_seconds raised from 75 to 120

---

## Family Law (1 question)

| question_id | file | correct_answer_changed | weakness_addressed | trap_types_added |
|---|---|---|---|---|
| fam-07-bi-001 | ch07-parenting.json | No | Abstract call ("what is the primary consideration?") with no fact scenario; Option D (financial resources) obviously wrong | General Rule Trap (A), Exception Trap (C), Misapplied Tool (D) |

### Per-question detail

**fam-07-bi-001**
- Added Marco and Diane with eight-year-old daughter Sofia; psychologist's report documenting explosive anger and anxiety symptoms after parenting exchanges; competing requests (equal time vs. supervised every other weekend); Marco's counsel invoking maximum-contact principle
- Call changed from "what is the primary consideration?" to "how should the court approach the tension between the maximum contact principle and documented psychological harm concerns?" — forces application of the DA s.16 best-interests hierarchy
- Option A (maximum contact principle is primary; only physical harm restricts) = General Rule Trap using a real DA s.16.1 rule with wrong sub-rule
- Option C (equal parenting time is the starting presumption) = Exception Trap; confuses 2021 amendments with old case law
- Option D (continuity of care/status quo is paramount) = Misapplied Tool; real enumerated factor but not the primary consideration

---

## Public Law (2 questions)

| question_id | file | correct_answer_changed | weakness_addressed | trap_types_added |
|---|---|---|---|---|
| pub-03-bias-001 | ch03-admin-law.json | No | Call asked for the legal test (definition recall); distractors A and D were thin | Subjective Bias Trap (A), Overstatement Trap (C), Wrong Forum/Procedure Trap (D) |
| pub-06-fippa-acc-001 | ch06-privacy.json | No | Call asked for general rule and mandatory/discretionary distinction; all three wrong options obviously wrong to prepared candidates | Overstatement Trap (A), General Rule Trap (C), Exception Trap (D) |

### Per-question detail

**pub-03-bias-001**
- Kept OEB/rate-setting scenario; named economist Dr. Amara Singh with a specific prior policy paper against the "revenue-cap" method; call changed to "how should the OEB rule on the motion?" — forces application of Committee for Justice and Liberty objective test
- Option A (proof of subjective bias + absence of financial interest required) = Subjective Bias Trap; conflates objective test with subjective bias
- Option C (academic writing is categorically excluded) = Overstatement Trap; invents categorical carve-out
- Option D (proof of continuing prejudice required) = Wrong Forum/Procedure Trap; fabricates evidentiary requirement

**pub-06-fippa-acc-001**
- New scenario: Beatrice Fontaine (Québec resident) requests two categories of records — legal briefing note (s.19 discretionary) and patient names (s.21 mandatory); Ministry issues a blanket refusal with no exemption specified and no exercise of discretion
- Call asks which combination of legal errors correctly describes the Ministry's response — forces multi-step analysis
- Option A (residency bars access) = Overstatement Trap; FIPPA does not bar non-resident requesters
- Option C (blanket refusal valid) = General Rule Trap; fails to distinguish mandatory/discretionary exemptions
- Option D (s.19 requires no discretion) = Exception Trap; reverses the mandatory/discretionary distinction

---

## Post-Improvement Pipeline

| Step | Result |
|---|---|
| `python3 tools/validate_question.py data/questions --summary` | 963 questions, 0 errors ✅ |
| Rebuild `bard` compact JSON from manifest IDs | 160 questions, 43/43/39/35 ✅ |
| Re-bake `bard` payload in index.html | 441,852 → 455,904 chars ✅ |
| `python3 tools/validate_html.py` | All checks pass ✅ |
| D∩C = 0 | ✅ |
| D∩E = 0 | ✅ |
| D∩F = 0 | ✅ |
| C∪D∪E∪F = 640 unique IDs | ✅ |
| Imported payloads unchanged (bar/sol/mini/abp/bar2) | ✅ |
| C/E/F payloads unchanged (barc/bare/barf) | ✅ |
| PR payloads unchanged (prdra/prdrb/prb200) | ✅ |
