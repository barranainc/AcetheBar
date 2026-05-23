# Question Generation Workflow — LSO Barrister Practice Exam System

**Version:** 1.0  
**Last updated:** 2026-05-18  
**Status:** Canonical — follow this workflow for every question generation session.

---

## Overview

Questions are generated subject by subject, chapter by chapter, subtopic by subtopic. The workflow has six stages. A question does not advance to the next stage until the current stage is complete.

```
Stage 1 — Blueprint gap analysis
Stage 2 — Statute identification
Stage 3 — Question authoring
Stage 4 — Structural validation (automated)
Stage 5 — Source checking (human)
Stage 6 — Human verification (second reviewer)
```

---

## Stage 1 — Blueprint Gap Analysis

**Tool:** `tools/coverage_report.py`  
**Input:** `data/blueprints/{subject}.json` + `data/questions/{subject}/`  
**Output:** List of subtopics under target, sorted by priority weight descending

**Steps:**
1. Run `python tools/coverage_report.py --subject civil-litigation`
2. Identify subtopics with `verified < minimum_question_count`
3. Sort by `priority_weight` (5 first)
4. Pick the top 3–5 subtopics as the target for this generation session

**Do not generate questions for subtopics that are already at or above `target_question_count` in verified questions.**

---

## Stage 2 — Statute Identification

Before writing a single word of a question, locate and open the governing law.

**Steps:**
1. Read the subtopic's `primary_statute` and `key_sections` from the blueprint
2. Navigate to those sections in the actual statute (e.g., open the current *Rules of Civil Procedure* from ontario.ca/laws)
3. Read the section text verbatim
4. Identify the rule the section establishes — in one sentence
5. Identify the most common way students misapply this rule — this becomes the basis for the exam_trap distractor

**Do not proceed to Stage 3 until you have the statute text open in front of you.**

---

## Stage 3 — Question Authoring

Write the question following the schema in `docs/QUESTION_SCHEMA.md`.

### Fact Pattern Guidelines

- Use Ontario-specific names, cities, and professional contexts
- Give the lawyer character a clear role (senior partner, articling student, sole practitioner)
- State the relevant facts precisely — do not embed the legal issue in the fact pattern
- The call of the question should isolate a single legal point
- Fact pattern length:
  - `easy`: 1–3 sentences
  - `medium`: 3–6 sentences
  - `hard`: 5–10 sentences
  - `exam_trap`: 5–10 sentences with a misleading detail that makes the wrong answer more tempting

### Option Writing Guidelines

- All four options must be the same approximate length (within 40% of each other)
- The correct answer must be unambiguously correct — not "the best of several correct answers"
- Distractors must be plausible — they should represent real misconceptions, not obviously wrong statements
- Avoid options that are negations of each other (if B says "X is required" and C says "X is not required", they're too easy to narrow down)
- One distractor should exploit the most common misconception identified in the blueprint
- One distractor should reference a related-but-wrong provision (e.g., a rule from a different chapter that sounds similar)

### Explanation Writing Guidelines

- Open with the statutory citation: `"Under [statute], [section], ..."`
- State what the provision says, not just that option X is correct
- Explain why the distractors are wrong in `why_X_wrong`
- For the correct option's `why_X_wrong`, write: `"This IS the correct answer. [Brief restatement of why.]"`
- Minimum 2 sentences in `explanation`; 4–6 sentences for `hard` and `exam_trap`

### Source Reference Completion

Fill all fields in `source_reference`:
- `lso_material`: Always `"LSO Barrister 2026 Study Materials"`
- `rule_or_statute_reference`: Must be specific (Act name + section number)
- `page`: Page in LSO study materials where this topic is covered; write `"statute"` if referencing directly from legislation without a study materials page

### ID Assignment

Use the convention: `{subject-code}-{chapter-num}-{subtopic-id}-{sequence}`

Check existing questions in the chapter file to find the next available sequence number.

---

## Stage 4 — Structural Validation (Automated)

**Tool:** `tools/validate_question.py`  
**Command:** `python tools/validate_question.py data/questions/civil-litigation/ch03-discovery.json`

The tool checks all structural requirements (see `validate_question.py` for full list).

**A question must pass all validation checks before proceeding to Stage 5.**

Fix any failures and re-run the validator.

---

## Stage 5 — Source Checking (Human)

The author (or another person) confirms:

1. Open the statute at the section cited in `rule_or_statute_reference`
2. Read the section — does it say what the explanation claims? If not, rewrite.
3. Is the correct answer unambiguously correct under that section? If not, rewrite.
4. Do the wrong-answer explanations accurately describe the error? If not, rewrite.
5. Is the fact pattern original? (See `docs/COPYRIGHT_SAFETY.md`) If not, rewrite.

If all five checks pass: set `validation_status: source_checked`

---

## Stage 6 — Human Verification (Second Reviewer)

A second person (not the author) reads the question cold and:

1. Answers the question without looking at `correct_answer`
2. If their answer matches: confirms the question is unambiguous
3. If their answer does not match: investigate whether the question is ambiguous or the reviewer was wrong
4. Reads the explanation and `why_X_wrong` fields — are they accurate and clear?
5. Checks `similarity_risk` — does this question feel similar to any known paid exam question?

If all checks pass: set `validation_status: human_verified` and `updated_at` to today

Only `human_verified` questions appear in student exam sessions.

---

## Session Workflow Summary

```
Before starting:
  1. Run coverage_report.py — pick top 5 uncovered subtopics
  2. Open LSO materials and relevant statutes

For each subtopic (repeat per session):
  3. Read primary_statute + key_sections from blueprint
  4. Write 3–5 questions following Stage 3 guidelines
  5. Add to chapter JSON file
  6. Run validate_question.py — fix failures
  7. Do source check — set source_checked
  8. Mark calendar for second reviewer

After session:
  9. Run coverage_report.py again — see new coverage %
  10. Commit to git with message: "Add N questions: {subject} Ch{X} — {subtopic_heading}"
```

---

## Chapter File Management

Each chapter's questions are stored in a single JSON file:

```
data/questions/{subject}/{chapter-slug}.json
```

The file contains a JSON array of question objects:

```json
[
  { "id": "civ-03-scope-exam-001", ... },
  { "id": "civ-03-scope-exam-002", ... }
]
```

When adding new questions, append to the array. Do not change existing question IDs.

**Git commit convention:**
```
Add {N} questions: {Subject} Ch{chapter_number} — {subtopic_heading}

Source: {rule_or_statute_reference}
Status: {draft|source_checked|human_verified}
Coverage: {X}/{Y} verified for this subtopic
```

---

## Quality Standards

| Metric | Minimum Standard |
|---|---|
| Explanation length | ≥ 50 words |
| Each why_wrong length | ≥ 15 words |
| Correct answer | Unambiguously supported by cited provision |
| Distractors | Must represent real misconceptions — not obviously wrong |
| fact_pattern | Must be original — not derived from paid materials |
| similarity_risk | Must not be `high` for any verified question |
| Statute citation | Must be specific (Act + section number) |

---

## Prioritisation Order for Generation Sessions

When choosing which subject and chapter to work on next, use this order:

1. **Highest priority_weight subtopics** that are below `minimum_question_count`
2. **Subtopics with `pr_angle_possible: true`** that have zero PR-angle questions
3. **Subtopics with `exam_trap` target > 0** that have zero exam_trap questions
4. **Chapters approaching exam-ready** (close to `minimum_question_count` across all subtopics)
5. **Subjects with lowest overall verified question count**

---

## Anti-Patterns to Avoid

| Anti-Pattern | Why It Fails |
|---|---|
| Starting from a paid exam question | Copyright risk; creates `similarity_risk: high` |
| Writing explanation before finding the statute | Explanation may not match the law |
| Generating many questions in one subject while others have none | Leaves coverage gaps in weak areas |
| Using only `easy` difficulty | Does not prepare students for actual exam difficulty |
| Writing `why_X_wrong` as "this option is incorrect" | Provides no educational value |
| Skipping Stage 4 validation | Structural errors accumulate in data files |
| Setting `human_verified` without a second reviewer | Defeats the purpose of the two-stage review |
| Citing a statute without confirming the section number | High hallucination risk |
