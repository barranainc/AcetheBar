# Question Psychometric Quality Rubric

**Project:** AcetheBar — barranainc/AcetheBar  
**Version:** 1.0 (Phase 2K, 2026-05-25)  
**Purpose:** Evaluate whether generated questions match realistic LSO Ontario Barrister licensing exam quality.

---

## Overview

This rubric assesses ten quality dimensions. Each dimension is scored 1–5 except where marked as binary (pass/flag). An overall exam realism score summarises the holistic impression.

The goal is not legal accuracy (that is handled by legal QA). The goal is *exam realism*: would an Ontario licensing candidate at the Barrister level encounter a question of this type and quality on the actual LSO exam?

---

## Verdict Codes

| Code | Meaning |
|------|---------|
| **PASS** | Already meets quality standard. Suitable for exam use as written. |
| **IMPROVE** | Legally usable but should be upgraded: stronger facts, better call wording, more precise distractors, or better rationale. Can be used now; should be upgraded before next quality review. |
| **REWRITE** | Topic is worth testing. Current question is too index-like, too obvious, too vague, or structurally flawed. Should be rewritten rather than tweaked. |
| **REMOVE** | Question is legally unsafe, unsupported, duplicative, too close to imported wording, or not worth saving in any form. |
| **LEGAL FLAG** | Unresolved legal/source concern. Must not be improved until the legal issue is source-checked and resolved. Recorded from `docs/GENERATED_EXAM_HUMAN_REVIEW_FLAGS.md`. |

---

## Dimension 1 — Source Grounding (scored in legal QA; flagged here if relevant)

**What it tests:** Whether the rule is tied to a real statute, regulation, or authoritative case; whether there is any sign of invented authority.

Legal QA handles primary source verification. In psychometric review, note only if a question's fact pattern invokes a standard, test, or rule that feels implausibly specific or where the source reference is absent.

*Not scored 1–5. Captured in `legal_flag_status` field.*

---

## Dimension 2 — Scenario Realism (1–5)

**What it tests:** Does the fact pattern feel like something the LSO could realistically test? Is it concise but factually sufficient to generate a genuine choice?

| Score | Meaning |
|-------|---------|
| 5 | Realistic, well-grounded Ontario practice scenario with just enough facts to force a legal judgment |
| 4 | Solid scenario; minor implausibility or minor missing context |
| 3 | Serviceable but generic; lacks specificity that would ground the answer in Ontario practice |
| 2 | Artificial or contrived; facts exist only to set up the answer mechanically |
| 1 | Hypothetical so thin or implausible it cannot be taken seriously as exam content |

---

## Dimension 3 — Application over Lookup (anti-index score, 1–5)

**What it tests:** Can the question be answered purely by scanning for one keyword (the "index rule")? Or does it require applying a rule to specific facts?

| Score | Meaning |
|-------|---------|
| 5 | Cannot be answered by keyword scanning; requires applying the rule to distinguishing facts |
| 4 | Mostly application-based; one distractor might be catchable by index alone |
| 3 | Mixed; the correct answer is available by knowing the rule, but distractors require application |
| 2 | Mostly index; knowing the rule name or section number is sufficient |
| 1 | Pure index; answerable by anyone who has memorised the section number |

---

## Dimension 4 — Binary Statutory Logic (1–5)

**What it tests:** Does the question exploit mandatory vs permissive language, deadlines, thresholds, exceptions, exemptions, or procedural preconditions — the elements that make statutory questions hard?

| Score | Meaning |
|-------|---------|
| 5 | Pivots on mandatory vs permissive, a hard threshold, or a non-obvious exception/exemption |
| 4 | Uses statutory precision but the binary pivot is relatively easy to identify |
| 3 | Rule-based but does not exploit any hard statutory distinction |
| 2 | Does not require statutory precision; general principle is sufficient |
| 1 | No statutory logic required; the question could be answered from general legal knowledge |

---

## Dimension 5 — Call Clarity (1–5)

**What it tests:** Is the call-of-question direct, unambiguous, and free from artificial trick wording or double negatives?

| Score | Meaning |
|-------|---------|
| 5 | Crystal clear; one unambiguous question that maps directly to the options |
| 4 | Clear; minor stylistic issue that does not affect answer discrimination |
| 3 | Serviceable but wordy, slightly vague, or mildly leading |
| 2 | Confusing, double negative, or ambiguous as to what is actually being asked |
| 1 | Call contradicts options, contains multiple questions, or is not answerable as written |

---

## Dimension 6 — Distractor Quality (1–5)

**What it tests:** Are wrong answers plausible? Are they engineered around real exam traps? Can each distractor be labelled with a trap type?

### Distractor Trap Taxonomy

| Label | Description |
|-------|-------------|
| **General Rule Trap** | Distractor states the general rule correctly but ignores an applicable exception |
| **Exception Trap** | Distractor states an exception but the exception does not apply on these facts |
| **Wrong Timeline Trap** | Distractor uses the right procedure but the wrong time limit or deadline |
| **Wrong Forum / Wrong Procedure Trap** | Correct outcome, wrong court or procedural vehicle |
| **Premature Escalation Trap** | Distractor jumps to a later step before the earlier step is exhausted |
| **Misapplied Tool** | Distractor applies a real legal tool that is simply not the right one here |
| **Pragmatic Bluff** | Distractor sounds commercially sensible but is legally impermissible |
| **Ethics Override Trap** | Distractor prioritises client advantage over professional obligation |
| **Overstatement Trap** | Distractor overstates the breadth of a right or obligation |
| **Understatement Trap** | Distractor understates a mandatory obligation as merely permissive |

### Scoring

| Score | Meaning |
|-------|---------|
| 5 | All three wrong answers are genuinely plausible and map to identifiable trap types |
| 4 | Two of three wrong answers are trap-engineered; one is weaker |
| 3 | At least one strong distractor; the others are plausible but not trap-engineered |
| 2 | Wrong answers are obviously wrong to anyone with basic knowledge |
| 1 | Wrong answers are absurd or self-defeating; question has only one realistic choice |

---

## Dimension 7 — Rationale Quality (1–5)

**What it tests:** Does the explanation (a) identify why the correct answer is right, (b) explain why each wrong answer is wrong, and (c) name the trap each distractor sets?

| Score | Meaning |
|-------|---------|
| 5 | Explains correct answer with statute/section; names each trap; explains why each distractor fails on these facts |
| 4 | Correct answer explained well; at least two distractors explained; trap types mostly identified |
| 3 | Correct answer explained; distractors dismissed without naming traps |
| 2 | Explanation merely restates the correct rule without engaging the distractors |
| 1 | Explanation is absent, circular, or incorrect |

---

## Dimension 8 — Prose Cleanliness (1–5)

**What it tests:** Clear language, no bloated facts, no vague pronouns, no unnecessary complexity, no double negatives.

| Score | Meaning |
|-------|---------|
| 5 | Tight, clear prose throughout; every sentence serves a purpose |
| 4 | Minor wordiness or one unclear pronoun; does not affect answer discrimination |
| 3 | Noticeable bloat, a confusing sentence, or a vague pronoun that requires re-reading |
| 2 | Significant prose issues that create unnecessary cognitive load |
| 1 | Difficult to parse; multiple errors in grammar, structure, or clarity |

---

## Dimension 9 — Ethics Integration (1–5 or N/A)

**What it tests:** Where PR is implicated, does professional responsibility override tactical advantage? Is the ethics dimension visible in the fact pattern and options?

| Score | Meaning |
|-------|---------|
| 5 | PR obligation clearly stated; at least one distractor is a Pragmatic Bluff or Ethics Override Trap |
| 4 | PR obligation present; ethics dimension could be sharpened |
| 3 | PR is implicit but not foregrounded |
| 2 | Question touches a PR area but the ethical dimension is not tested |
| 1 | Question ignores a material PR obligation that is clearly implicated by the facts |
| N/A | No ethics dimension implied by the subject matter |

---

## Dimension 10 — Overall LSO Exam Realism (1–5)

**What it tests:** Does this feel like a real Ontario Barrister licensing question as a whole? Would a candidate encounter this on the actual LSO exam without feeling it was artificially constructed?

| Score | Meaning |
|-------|---------|
| 5 | Indistinguishable from a real LSO question; scenario, options, and rationale all at exam standard |
| 4 | Strong question; one dimension could be sharpened but overall highly credible |
| 3 | Serviceable question; usable for prep but perceptibly weaker than exam standard |
| 2 | Noticeably artificial; would not appear on an actual LSO exam in this form |
| 1 | Would not survive a basic item-review process; must be rewritten or removed |

---

## Score → Verdict Mapping

| Overall LSO Realism Score | Default Verdict | Override conditions |
|--------------------------|-----------------|---------------------|
| 5 | PASS | — |
| 4 | PASS | Downgrade to IMPROVE if one dimension ≤ 2 |
| 3 | IMPROVE | Downgrade to REWRITE if anti-index ≤ 2 or distractor quality ≤ 2 |
| 2 | REWRITE | Upgrade to IMPROVE only if easily fixable in one field |
| 1 | REMOVE | — |
| Any | LEGAL FLAG | If question is in `docs/GENERATED_EXAM_HUMAN_REVIEW_FLAGS.md` |

---

## Audit Format

Per-question table format for audit documents:

```
| question_id | subject | legal_flag | quality | anti_idx | scenario | bin_logic | distractor | rationale | prose | ethics | realism | weakness | action |
```

Abbreviations for column headers:
- `legal_flag`: `clear` / `legal flag`
- `quality`: PASS / IMPROVE / REWRITE / REMOVE / LEGAL FLAG
- `anti_idx`: anti-index score 1–5
- `scenario`: scenario realism 1–5
- `bin_logic`: binary statutory logic 1–5
- `distractor`: distractor quality 1–5
- `rationale`: rationale quality 1–5
- `prose`: prose cleanliness 1–5
- `ethics`: ethics integration 1–5 or N/A
- `realism`: overall LSO exam realism 1–5
- `weakness`: one-line summary of main weakness (blank if PASS)
- `action`: one-line recommended action (blank if PASS)

---

## How to Apply the Rubric

1. Read the question's `fact_pattern` and `call_of_question`.
2. Check `legal_flag_status` against `docs/GENERATED_EXAM_HUMAN_REVIEW_FLAGS.md`. If flagged, mark LEGAL FLAG and stop scoring.
3. Score each of Dimensions 2–9.
4. Assign `overall_exam_realism_score` (Dimension 10) holistically.
5. Apply the Score → Verdict mapping to assign quality verdict.
6. Note the main weakness (the dimension dragging the score most).
7. Write one-line recommended action.

---

*This rubric covers psychometric and exam-realism quality only. Legal accuracy is governed by the legal QA process (`docs/LEGAL_QA_GENERATED_BARRISTER_*.md`). If a question passes psychometric review but has an unresolved legal flag, it remains LEGAL FLAG until the legal issue is resolved.*
