# Copyright Safety Rules — LSO Barrister Practice Exam System

**Version:** 1.0  
**Last updated:** 2026-05-18  
**Status:** Mandatory — every contributor must read this before generating or reviewing questions.

---

## The Non-Negotiable Rule

> **Every question must originate from an official Ontario statute, rule, or regulation — not from a paid practice exam.**

If you cannot point to the specific statutory provision that makes the correct answer correct, the question must not be used.

---

## What "Official LSO Material" Means

Permitted sources of legal truth for generating questions:

| Source | Examples |
|---|---|
| Ontario statutes | *Courts of Justice Act*, *Family Law Act*, *Law Society Act, 1998*, *Limitations Act, 2002* |
| Ontario regulations | *Rules of Civil Procedure*, O. Reg. 258/98, Family Law Rules |
| Federal statutes | *Criminal Code*, *Divorce Act*, *Youth Criminal Justice Act*, *Canada Evidence Act* |
| Federal regulations | *Federal Child Support Guidelines*, *Federal Courts Rules* |
| Rules of Professional Conduct | Published by LSO on lso.ca |
| Law Society By-Laws | Published by LSO on lso.ca |
| Constitutional instruments | *Charter of Rights and Freedoms*, *Constitution Act, 1982* |
| LSO 2026 Barrister Study Materials | For chapter structure, emphasis, and page references — not for question text |

---

## What Paid Practice Exams May Be Used For

The following paid or third-party materials are **style references only**:

- AccessBarPrep practice exams
- Brigham Bar Prep materials
- Any other commercial Ontario bar prep provider

### Permitted uses of paid materials:
- Observing the **length** of fact patterns (how many sentences)
- Observing **option structure** (balanced vs. asymmetric, length of options)
- Observing **difficulty calibration** (how hard the questions feel)
- Observing **explanation style** (how citations are written, how wrong answers are explained)
- Observing **distractor logic** (what kinds of plausible-but-wrong options are used)

### Prohibited uses of paid materials:
- Copying a question scenario, even loosely
- Paraphrasing a fact pattern from a paid exam question
- Using the same cast of characters (same name + same legal problem)
- Using the same statutory issue in the same procedural posture as a paid question
- Using a paid exam's answer as the basis for writing your explanation
- Using a paid exam question as a starting point and then "changing it enough"

**There is no safe amount of paraphrasing. If the inspiration is a paid question, rewrite from the statute directly.**

---

## The Copyright Risk Tiers

Each question is assigned a `similarity_risk` field. The criteria are:

### `low` — Safe to use
- The scenario is original (not derived from any known practice exam)
- The statutory provision has been independently identified from LSO materials
- The distractor logic is your own invention, not borrowed from another exam

### `medium` — Review required before use
- The scenario touches a very common fact pattern that appears in many practice exams (e.g., a lawyer who forgets to file within a limitation period)
- The question has not been compared against paid materials
- One or more options feels similar to options you have seen in a paid exam

### `high` — Must be rewritten before any use
- The question was generated starting from a paid practice question
- The fact pattern uses the same names, roles, or legal posture as a known paid question
- The explanation quotes or closely paraphrases a paid exam's explanation

**Questions with `similarity_risk: high` must never appear in a student-facing session.**

---

## The "Independently Derived" Standard

A question is independently derived if:

1. You started with the statute or rule (not a practice exam question)
2. You identified the legal issue from the LSO study materials outline
3. You invented the fact pattern to illustrate that legal issue
4. You wrote the four options based on common misconceptions or related provisions — not based on options you read elsewhere

**Test:** If you were asked "Where did this question come from?", could you answer: "I read Rule X in the Rules of Civil Procedure, then wrote a scenario that would test whether a student knows Rule X"? If yes, the question is independently derived.

---

## Hallucinated Law Risk

AI-generated questions carry a specific risk: the model may confidently state an incorrect section number, attribute a rule to the wrong statute, or invent a legal principle that does not exist.

### Mandatory checks before setting `validation_status: source_checked`:

1. Open the actual statute or rule
2. Navigate to the section cited in `rule_or_statute_reference`
3. Confirm the section exists and says what the question claims it says
4. Confirm the section number has not been renumbered in recent amendments
5. Confirm the correct answer is unambiguously supported by that section

### Red flags that suggest hallucination:
- A section number that ends in a letter where the real act uses subsections (e.g., "s. 5A" instead of "s. 5(1)")
- A rule that sounds logical but cannot be found in the statute
- An explanation that says "courts have held" without a case citation when the rule is actually statutory
- A cross-reference to another section that does not exist

**If in doubt, the question fails source_checked. Do not guess. Find the provision or rewrite.**

---

## LSO Material Copyright

The LSO 2026 Barrister Study Materials are themselves copyrighted by the Law Society of Ontario. The following uses are prohibited:

- Reproducing the LSO study material text verbatim as question text
- Reproducing LSO practice questions (if any exist in the materials) in any form
- Copying LSO chapter summaries as explanations
- Presenting LSO examples or fact patterns as original questions

The LSO materials are used to identify:
- Which topics and subtopics are within scope
- Which statutes and rules are relevant
- Which page of the materials a student should consult to verify an answer

The `source_reference.page` field records the LSO page number so a student can verify the answer — it does not authorize reproduction of that content.

---

## Question Review Checklist

Before marking any question `human_verified`, the reviewer must confirm:

- [ ] The correct answer is supported by the specific provision in `rule_or_statute_reference`
- [ ] That provision exists in the current version of the statute/rule
- [ ] The section number and subsection are correct
- [ ] None of the four options was taken or adapted from a paid practice exam
- [ ] The fact pattern is original (no recognizable paid exam scenario)
- [ ] `similarity_risk` is accurately set
- [ ] `why_X_wrong` for each wrong option identifies a specific legal error
- [ ] `explanation` opens with the statutory citation
- [ ] `validation_status` is being promoted from `source_checked` (not directly from `draft`)

---

## Reporting a Concern

If you identify a question that may infringe copyright or contain incorrect law:

1. Set `validation_status: draft` (regression from any higher status)
2. Set `similarity_risk: high`
3. Add a note in `notes_for_generation` (if on the blueprint) or in a comment in the JSON file
4. Do not use the question in any session until it is re-reviewed

---

## Summary

| Action | Permitted |
|---|---|
| Write a question starting from a statute | ✅ |
| Use LSO study materials to find the right chapter | ✅ |
| Use paid exams to calibrate difficulty/length | ✅ |
| Copy a paid exam question and change names | ❌ |
| Paraphrase a paid exam fact pattern | ❌ |
| Use paid exam options as your distractors | ❌ |
| Cite a statute section without verifying it exists | ❌ |
| Reproduce LSO study material text as a question | ❌ |
