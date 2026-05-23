# Blueprint Rules — LSO Barrister Practice Exam System

**Version:** 1.0  
**Last updated:** 2026-05-18  
**Status:** Canonical — all blueprint JSON files must conform to this schema.

---

## Overview

A blueprint is the structural map of an exam subject. It defines every chapter, topic, and subtopic that must be covered, along with question count targets and generation guidance. Blueprints live in `data/blueprints/`.

**One blueprint file per subject:**
```
data/blueprints/
  barrister-subjects.json         ← top-level index of all 5 subjects
  civil-litigation.json
  criminal-law.json
  family-law.json
  public-law.json
  professional-responsibility.json
```

The blueprint drives the coverage report (`tools/coverage_report.py`) and the exam builder (`tools/build_exam.py`).

---

## Blueprint Node Schema

A blueprint is a JSON object with a `subject` key and a `chapters` array. Each chapter contains `topics`, and each topic contains `subtopics`.

### Top-Level Subject Object

```json
{
  "subject_key": "string — snake_case, matches question subject field",
  "subject_label": "string — display name",
  "subject_code": "string — 2-4 char abbreviation matching question ID prefix",
  "lso_weight_percent": "number — approximate % of real exam from this subject (informational only)",
  "total_target_questions": "integer — total questions to generate across all chapters",
  "total_minimum_questions": "integer — minimum needed before subject is considered exam-ready",
  "chapters": [ "...see Chapter Object below..." ]
}
```

### Chapter Object

```json
{
  "chapter_number": "integer — 1-indexed, matches question schema",
  "chapter_title": "string — chapter title",
  "chapter_slug": "string — kebab-case slug, matches question file name prefix",
  "lso_dtoc_ref": "string — reference to DTOC location (e.g. 'DTOC p. 12, Section 2')",
  "priority_weight": "integer from 1 to 5 — 5 = most heavily tested on real exam, 1 = rarely tested",
  "topics": [ "...see Topic Object below..." ]
}
```

### Topic Object

```json
{
  "topic_id": "string — snake_case, matches question topic_id field",
  "topic_heading": "string — heading as it appears in LSO materials",
  "subtopics": [ "...see Subtopic Object below..." ]
}
```

### Subtopic Object — the atomic unit of the blueprint

```json
{
  "subtopic_id": "string — snake_case slug, used in question ID construction",
  "subtopic_heading": "string — heading",

  "target_question_count": "integer — ideal number of questions for this subtopic",
  "minimum_question_count": "integer — minimum before this subtopic is exam-ready (must be ≥ 1)",

  "difficulty_split": {
    "easy": "integer — target count at this difficulty",
    "medium": "integer — target count at this difficulty",
    "hard": "integer — target count at this difficulty",
    "exam_trap": "integer — target count at this difficulty"
  },

  "pr_angle_possible": "boolean — true if a professional responsibility dimension is realistic for this subtopic",

  "priority_weight": "integer from 1 to 5 — granular priority at subtopic level",

  "primary_statute": "string — the governing statute or rule for this subtopic (e.g. 'Rules of Civil Procedure, r. 20')",

  "key_sections": [
    "array of strings — specific sections/rules most likely to be tested (e.g. ['r. 20.04(1)', 'r. 20.05', 'r. 20.06'])"
  ],

  "common_misconceptions": [
    "array of strings — known student errors for this subtopic. Used to guide exam_trap question design."
  ],

  "notes_for_generation": "string — freeform guidance for whoever writes the questions. Include tone, typical fact-pattern structure, tricky areas, and what the LSO materials emphasize."
}
```

---

## Priority Weight Scale

| Weight | Meaning | Expected Questions |
|---|---|---|
| 5 | Core — appears on virtually every real exam | Target ≥ 5 questions |
| 4 | High — commonly tested | Target ≥ 4 questions |
| 3 | Moderate — tested regularly | Target ≥ 3 questions |
| 2 | Low — occasionally tested | Target ≥ 2 questions |
| 1 | Rare — edge topics, tested infrequently | Target ≥ 1 question |

---

## Difficulty Split Rules

The four difficulty levels must be present in every subtopic object. Zero is allowed (meaning no questions at that level are targeted for this subtopic). The sum of the four values must equal `target_question_count`.

**Recommended distribution by priority weight:**

| Priority | easy | medium | hard | exam_trap |
|---|---|---|---|---|
| 5 | 1 | 2 | 1 | 1 |
| 4 | 1 | 2 | 1 | 0 |
| 3 | 0 | 2 | 1 | 0 |
| 2 | 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 | 0 |

---

## Chapter Priority Assignment Guide

Use these criteria when assigning `priority_weight` to chapters:

1. **Frequency on past LSO exams** — if the subject is strongly tested in the real exam, weight higher
2. **LSO emphasis in study materials** — chapters with more pages in the LSO materials generally have higher exam weight
3. **Professional responsibility crossover** — chapters that also test PR are higher priority because they appear in two modes
4. **Student error rate** — topics that consistently produce low pass rates warrant more coverage
5. **Statutory complexity** — chapters with multiple exceptions, time limits, and procedural steps are higher priority

---

## Blueprint Validation Rules

The `coverage_report.py` tool enforces these rules:

1. Every subtopic in the blueprint must have at least `minimum_question_count` questions in `validation_status: human_verified` before the chapter is marked "exam-ready"
2. The difficulty split in actual questions must be within ±1 of the blueprint target for `hard` and `exam_trap` questions
3. No subject may be flagged as exam-ready unless it has at least `total_minimum_questions` verified questions
4. Every subtopic with `pr_angle_possible: true` must have at least 1 question with `pr_angle.applicable: true`
5. No subtopic may have more than 50% of its questions at `easy` difficulty

---

## Blueprint File Example (excerpt)

```json
{
  "subject_key": "civil_litigation",
  "subject_label": "Civil Litigation",
  "subject_code": "civ",
  "lso_weight_percent": 25,
  "total_target_questions": 200,
  "total_minimum_questions": 80,
  "chapters": [
    {
      "chapter_number": 3,
      "chapter_title": "Discovery",
      "chapter_slug": "ch03-discovery",
      "lso_dtoc_ref": "DTOC p. 22, Section 3",
      "priority_weight": 5,
      "topics": [
        {
          "topic_id": "examination_for_discovery",
          "topic_heading": "Examination for Discovery",
          "subtopics": [
            {
              "subtopic_id": "scope_of_examination",
              "subtopic_heading": "Scope of Examination",
              "target_question_count": 5,
              "minimum_question_count": 2,
              "difficulty_split": {
                "easy": 1,
                "medium": 2,
                "hard": 1,
                "exam_trap": 1
              },
              "pr_angle_possible": true,
              "priority_weight": 5,
              "primary_statute": "Rules of Civil Procedure, r. 31.06",
              "key_sections": ["r. 31.06(1)", "r. 31.06(2)", "r. 31.06(3)"],
              "common_misconceptions": [
                "Students confuse 'relevant to any matter in issue' with 'directly pleaded'",
                "Students think discovery is limited to documents already produced"
              ],
              "notes_for_generation": "Focus on the scope distinction: broader than pleadings, bounded by relevance. Good fact patterns involve a lawyer's attempt to limit scope — the distractor logic should exploit the 'directly pleaded' misconception. One exam_trap question should involve a third-party record request (r. 31.10)."
            }
          ]
        }
      ]
    }
  ]
}
```

---

## Relationship Between Blueprint and Questions

```
blueprint subtopic
    │
    ├─ target_question_count  ──►  actual question files in data/questions/
    │                                  (matched by subject + chapter_number + subtopic_id)
    │
    ├─ difficulty_split        ──►  questions sorted by difficulty field
    │
    ├─ pr_angle_possible       ──►  at least 1 question with pr_angle.applicable = true
    │
    └─ minimum_question_count  ──►  at least N questions with validation_status = human_verified
```

The coverage report computes the gap between blueprint targets and actual verified questions for every subtopic in the system.

---

## Notes on LSO Source Alignment

The chapter structure in each blueprint must follow the LSO 2026 Barrister study materials chapter numbering, not a generic law school curriculum. When in doubt:

1. Open the LSO study materials for the subject
2. Use the table of contents chapter numbers exactly
3. Use the DTOC (Detailed Table of Contents) for topic and subtopic headings
4. Record the DTOC page reference in `lso_dtoc_ref`

The goal is that any question in the system can be traced directly back to a specific page in the LSO materials, via the question's `source_reference` field.
