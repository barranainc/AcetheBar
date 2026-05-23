# Question Schema — LSO Barrister Practice Exam System

**Version:** 1.0  
**Last updated:** 2026-05-18  
**Status:** Canonical — all question JSON files must conform to this schema.

---

## Overview

Every question in `data/questions/{subject}/` is a single JSON object stored in a file named after its `id`. Questions are organized into subject folders and chapter files. Each chapter file contains an array of question objects.

**File naming:** `data/questions/{subject}/{chapter-slug}.json`  
**Example:** `data/questions/civil-litigation/ch03-discovery.json`

---

## Canonical Schema

```json
{
  "id": "string — see ID Convention below",

  "subject": "string — one of the five canonical subject keys",

  "chapter_number": "integer — LSO chapter number (1-indexed)",

  "chapter_title": "string — chapter title as labelled in LSO materials",

  "topic_id": "string — slug of the topic within the chapter",

  "topic_heading": "string — topic heading as it appears in LSO materials",

  "subtopic_id": "string — slug of the subtopic",

  "subtopic_heading": "string — subtopic heading",

  "difficulty": "string — one of: easy | medium | hard | exam_trap",

  "question_type": "string — must be: single_best_answer",

  "fact_pattern": "string — the scenario/fact situation presented to the student (may be empty string for pure law questions that have no scenario)",

  "call_of_question": "string — the specific question asked at the end (e.g. 'Which of the following is correct?')",

  "options": {
    "A": "string — option text, non-empty",
    "B": "string — option text, non-empty",
    "C": "string — option text, non-empty",
    "D": "string — option text, non-empty"
  },

  "correct_answer": "string — one of: A | B | C | D",

  "explanation": "string — why the correct answer is correct, citing the specific statute/rule/section. Must begin with the citation (e.g. 'Under r. 14.01(1) of the Rules of Civil Procedure...'). Minimum 2 sentences.",

  "why_A_wrong": "string — specific reason why option A is wrong. Must reference law, not just say 'this is incorrect'. Required even if A is the correct answer — in that case, write 'This IS the correct answer.'",

  "why_B_wrong": "string — same requirement as why_A_wrong",

  "why_C_wrong": "string — same requirement as why_A_wrong",

  "why_D_wrong": "string — same requirement as why_A_wrong",

  "source_reference": {
    "lso_material": "string — name of the LSO study material (e.g. 'LSO Barrister 2026 Study Materials')",
    "subject": "string — subject name within LSO materials",
    "chapter": "string — chapter reference as it appears in LSO materials",
    "heading": "string — section heading within the chapter",
    "page": "string — page number or range (e.g. '45' or '45-47'). Use 'N/A' only if the source is the statute itself without a page reference.",
    "rule_or_statute_reference": "string — primary statutory citation in standard legal format (e.g. 'Rules of Civil Procedure, r. 20.04(1)' or 'Criminal Code, s. 515(10)')"
  },

  "pr_angle": {
    "applicable": "boolean — true if this question involves a professional responsibility dimension even if the primary subject is not Professional Responsibility",
    "pr_issue_type": "string or null — if applicable is true, describe the PR issue (e.g. 'duty of candour', 'conflict of interest', 'confidentiality', 'withdrawal', 'trust accounting'). Null if applicable is false."
  },

  "exam_trigger_words": [
    "array of strings — key words or phrases that signal this type of question on the real exam (e.g. ['except', 'not required', 'must', 'shall not'])"
  ],

  "tested_concepts": [
    "array of strings — specific legal concepts tested (e.g. ['litigation privilege', 'dominant purpose test', 'duration of privilege'])"
  ],

  "estimated_time_seconds": "integer — expected time for a competent student to read, analyze, and answer. Typically 90–180 seconds. Use 90 for easy, 120 for medium, 150 for hard, 180 for exam_trap.",

  "validation_status": "string — one of: draft | source_checked | human_verified",

  "similarity_risk": "string — one of: low | medium | high. Assessment of how closely this question resembles a known paid practice exam question. Any question rated 'high' must be rewritten before use.",

  "created_at": "string — ISO 8601 date (YYYY-MM-DD)",

  "updated_at": "string — ISO 8601 date (YYYY-MM-DD)"
}
```

---

## ID Convention

```
{subject-code}-{chapter-number}-{subtopic-code}-{sequence}
```

| Part | Format | Example |
|---|---|---|
| subject-code | 3-letter abbreviation | `civ`, `crim`, `fam`, `pub`, `pr` |
| chapter-number | zero-padded 2-digit integer | `03` |
| subtopic-code | short slug, max 12 chars | `discov-exam` |
| sequence | zero-padded 3-digit integer | `001` |

**Full example:** `civ-03-discov-exam-001`

### Subject Codes

| Subject | Code |
|---|---|
| Civil Litigation | `civ` |
| Criminal Law | `crim` |
| Family Law | `fam` |
| Public Law | `pub` |
| Professional Responsibility | `pr` |

---

## Difficulty Levels

| Level | Description | Typical Time |
|---|---|---|
| `easy` | Single-rule recall. The statute directly answers the question. No ambiguity. | 90 s |
| `medium` | Requires applying a rule to a moderate fact pattern. One or two distractors are plausible. | 120 s |
| `hard` | Requires distinguishing between two similar rules, or applying an exception. Multiple plausible distractors. | 150 s |
| `exam_trap` | Designed around a common misconception or a rule with a counterintuitive result. The most common wrong answer is the most tempting. | 180 s |

---

## Explanation Requirements

The `explanation` field must:
1. Open with the statutory citation: `"Under [statute], [section]..."`
2. State what the law says, not just what the correct answer is
3. Be self-contained — a student who only reads the explanation should understand why the answer is correct
4. Minimum 2 sentences; recommended 3–5 sentences for `hard` and `exam_trap` questions

The `why_X_wrong` fields must:
1. Identify the specific legal error in the distractor
2. Reference the law where possible (e.g. "Option B misreads r. 20.04 — that rule governs summary judgment, not…")
3. Not simply say "this is wrong" or "this is not the law"

---

## PR Angle Integration

Professional Responsibility dimensions appear in all five subjects. When a question in Civil Litigation, Criminal Law, Family Law, or Public Law involves:

- A lawyer's duty to the court
- A conflict of interest
- Confidentiality obligations
- Withdrawal or termination of retainer
- Trust accounting issues
- Duties to opposing parties

…set `pr_angle.applicable = true` and describe the issue in `pr_angle.pr_issue_type`.

This enables PR-overlay exam mode (Phase 6).

---

## Source Reference Integrity

**Every question must have a complete `source_reference`.** The `rule_or_statute_reference` field is the most critical — it must name the specific provision that makes the correct answer correct.

Acceptable formats:
- `"Rules of Civil Procedure, r. 20.04(1)"`
- `"Criminal Code of Canada, s. 515(10)(c)"`
- `"Family Law Act, R.S.O. 1990, s. 5(6)"`
- `"Law Society Act, 1998, s. 49.37"`
- `"Rules of Professional Conduct, Rule 3.4-5, Commentary [2]"`
- `"Charter of Rights and Freedoms, s. 10(b)"`
- `"Federal Child Support Guidelines, SOR/97-175, s. 9"`

**Not acceptable:**
- `"Family Law Act"` (no section)
- `"Rules of Civil Procedure"` (no rule number)
- `"Common law"` (too vague)
- `""` (empty)

---

## Validation Status Workflow

```
draft
  └─► source_checked   (author has confirmed statute section exists and is correct)
        └─► human_verified  (a second person has read the question and confirmed accuracy)
```

Only `human_verified` questions are included in student-facing exam sessions.  
`source_checked` questions may be used in beta/review mode.  
`draft` questions are excluded from all student-facing sessions.

---

## Complete Example Question

```json
{
  "id": "civ-03-discov-exam-001",
  "subject": "civil_litigation",
  "chapter_number": 3,
  "chapter_title": "Discovery",
  "topic_id": "examination_for_discovery",
  "topic_heading": "Examination for Discovery",
  "subtopic_id": "scope_of_examination",
  "subtopic_heading": "Scope of Examination for Discovery",
  "difficulty": "medium",
  "question_type": "single_best_answer",
  "fact_pattern": "Priya is a defendant in a wrongful dismissal action. During her examination for discovery, plaintiff's counsel asks her to identify every performance review she received in the five years before her termination. Priya's lawyer objects, arguing the question calls for information that has no relevance to the pleaded issues.",
  "call_of_question": "Which of the following best describes the scope of questions permitted at an examination for discovery in Ontario?",
  "options": {
    "A": "A party may only be examined on facts directly pleaded in the statement of claim or statement of defence.",
    "B": "A party may be examined on any matter, whether or not it is related to the issues in the action, provided the question is not otherwise improper.",
    "C": "A party may be examined on any matter that is relevant to any matter in issue between or among the parties in the action.",
    "D": "A party may only be examined on documents that have already been produced in the party's Affidavit of Documents."
  },
  "correct_answer": "C",
  "explanation": "Under Rule 31.06(1) of the Rules of Civil Procedure, a party may on an examination for discovery be examined on any matter that is relevant to any matter in issue between or among the parties in the action. The standard is relevance to any issue in the action, which is broader than relevance only to the pleaded facts. The scope is not limited to documents already produced, and it is not unlimited — relevance remains the touchstone.",
  "why_A_wrong": "Option A is too narrow. Rule 31.06(1) does not confine examination to facts directly pleaded. A party may be examined on any matter relevant to any issue in the action, which is a broader standard.",
  "why_B_wrong": "Option B is too broad. An examination for discovery is not unlimited. Rule 31.06(1) requires that questions be relevant to a matter in issue in the action. Questions on wholly irrelevant matters are improper.",
  "why_C_wrong": "This IS the correct answer. Rule 31.06(1) permits examination on any matter relevant to any matter in issue.",
  "why_D_wrong": "Option D incorrectly conflates documentary discovery (Rule 30) with oral discovery (Rule 31). Examination for discovery is not limited to documents already produced in the Affidavit of Documents.",
  "source_reference": {
    "lso_material": "LSO Barrister 2026 Study Materials",
    "subject": "Civil Litigation",
    "chapter": "Chapter 3 — Discovery",
    "heading": "Examination for Discovery — Scope",
    "page": "78",
    "rule_or_statute_reference": "Rules of Civil Procedure, r. 31.06(1)"
  },
  "pr_angle": {
    "applicable": false,
    "pr_issue_type": null
  },
  "exam_trigger_words": ["scope", "permitted", "examination for discovery", "relevant"],
  "tested_concepts": ["scope of examination for discovery", "Rule 31.06(1)", "relevance standard"],
  "estimated_time_seconds": 120,
  "validation_status": "draft",
  "similarity_risk": "low",
  "created_at": "2026-05-18",
  "updated_at": "2026-05-18"
}
```
