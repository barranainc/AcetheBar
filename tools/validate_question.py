#!/usr/bin/env python3
"""
validate_question.py — LSO Barrister Practice Exam System
==========================================================
Validates one or more question JSON files against the canonical schema
defined in docs/QUESTION_SCHEMA.md.

Usage:
    python tools/validate_question.py <file_or_dir> [--strict] [--summary]

Examples:
    # Validate a single chapter file
    python tools/validate_question.py data/questions/civil-litigation/ch03-discovery.json

    # Validate all questions in a subject folder
    python tools/validate_question.py data/questions/civil-litigation/

    # Validate all questions in all subjects
    python tools/validate_question.py data/questions/

    # Strict mode: fail on similarity_risk=medium (not just high)
    python tools/validate_question.py data/questions/ --strict

    # Summary only (no per-question output)
    python tools/validate_question.py data/questions/ --summary

Exit codes:
    0 — all questions pass
    1 — one or more questions have errors
    2 — file/directory not found or JSON parse error
"""

import json
import os
import re
import sys
from datetime import date
from pathlib import Path


# ── Constants ─────────────────────────────────────────────────────────────────

VALID_SUBJECTS = {
    "civil_litigation",
    "criminal_law",
    "family_law",
    "public_law",
    "professional_responsibility",
}

SUBJECT_CODES = {
    "civil_litigation": "civ",
    "criminal_law": "crim",
    "family_law": "fam",
    "public_law": "pub",
    "professional_responsibility": "pr",
}

VALID_DIFFICULTIES = {"easy", "medium", "hard", "exam_trap"}
VALID_QUESTION_TYPES = {"single_best_answer"}
VALID_ANSWERS = {"A", "B", "C", "D"}
VALID_VALIDATION_STATUSES = {"draft", "source_checked", "human_verified"}
VALID_SIMILARITY_RISKS = {"low", "medium", "high"}

# Minimum character counts for text fields
MIN_EXPLANATION_CHARS = 150
MIN_WHY_WRONG_CHARS = 60
MIN_FACT_PATTERN_CHARS = 0  # may be empty for pure law questions
MIN_CALL_OF_QUESTION_CHARS = 15
MIN_OPTION_CHARS = 10

# ID pattern: {subject-code}-{chapter:02d}-{subtopic-slug}-{seq:03d}
ID_PATTERN = re.compile(
    r'^(civ|crim|fam|pub|pr)-\d{2}-[a-z][a-z0-9\-]{1,14}-\d{3}$'
)

# Acceptable statute reference format — must contain a comma and a section indicator
STATUTE_REF_PATTERN = re.compile(
    r'.*,\s*(s\.|r\.|art\.|Rule\s|Part\s|Schedule\s|Sched\.\s)',
    re.IGNORECASE
)


# ── Validation Logic ──────────────────────────────────────────────────────────

class ValidationError:
    def __init__(self, question_id: str, field: str, message: str, severity: str = "ERROR"):
        self.question_id = question_id
        self.field = field
        self.message = message
        self.severity = severity  # ERROR | WARNING

    def __str__(self):
        return f"  [{self.severity}] {self.field}: {self.message}"


def validate_question(q: dict) -> list[ValidationError]:
    """Validate a single question object. Returns list of ValidationErrors."""
    errors = []
    qid = q.get("id", "<unknown>")

    def err(field, msg, severity="ERROR"):
        errors.append(ValidationError(qid, field, msg, severity))

    # ── 1. Required top-level fields ─────────────────────────────────────────
    required_fields = [
        "id", "subject", "chapter_number", "chapter_title",
        "topic_id", "topic_heading", "subtopic_id", "subtopic_heading",
        "difficulty", "question_type", "fact_pattern", "call_of_question",
        "options", "correct_answer", "explanation",
        "why_A_wrong", "why_B_wrong", "why_C_wrong", "why_D_wrong",
        "source_reference", "pr_angle",
        "exam_trigger_words", "tested_concepts",
        "estimated_time_seconds", "validation_status", "similarity_risk",
        "created_at", "updated_at",
    ]
    for field in required_fields:
        if field not in q:
            err(field, f"Required field '{field}' is missing")

    # Stop here if critical fields are absent — subsequent checks will crash
    if "id" not in q or "options" not in q or "correct_answer" not in q:
        return errors

    # ── 2. ID format ─────────────────────────────────────────────────────────
    if not ID_PATTERN.match(qid):
        err("id", (
            f"ID '{qid}' does not match pattern "
            f"{{subject-code}}-{{chapter:02d}}-{{subtopic-slug}}-{{seq:03d}}. "
            f"Example: civ-03-discov-exam-001"
        ))

    # ── 3. Subject ───────────────────────────────────────────────────────────
    subject = q.get("subject", "")
    if subject not in VALID_SUBJECTS:
        err("subject", f"'{subject}' is not a valid subject. Must be one of: {sorted(VALID_SUBJECTS)}")
    else:
        # Cross-check: ID prefix must match subject code
        expected_code = SUBJECT_CODES[subject]
        if not qid.startswith(expected_code + "-"):
            err("id", f"ID prefix must be '{expected_code}' for subject '{subject}', got '{qid}'")

    # ── 4. Chapter number ────────────────────────────────────────────────────
    ch = q.get("chapter_number")
    if ch is not None:
        if not isinstance(ch, int) or ch < 1:
            err("chapter_number", f"Must be a positive integer, got: {ch!r}")

    # ── 5. Difficulty ────────────────────────────────────────────────────────
    difficulty = q.get("difficulty", "")
    if difficulty not in VALID_DIFFICULTIES:
        err("difficulty", f"'{difficulty}' is not valid. Must be one of: {sorted(VALID_DIFFICULTIES)}")

    # ── 6. Question type ─────────────────────────────────────────────────────
    qtype = q.get("question_type", "")
    if qtype not in VALID_QUESTION_TYPES:
        err("question_type", f"'{qtype}' is not valid. Must be: single_best_answer")

    # ── 7. Options A-D exist and are non-empty ───────────────────────────────
    options = q.get("options", {})
    if not isinstance(options, dict):
        err("options", "Must be an object with keys A, B, C, D")
    else:
        for letter in ["A", "B", "C", "D"]:
            opt = options.get(letter, "")
            if not opt or not isinstance(opt, str):
                err(f"options.{letter}", f"Option {letter} is missing or empty")
            elif len(opt.strip()) < MIN_OPTION_CHARS:
                err(f"options.{letter}", f"Option {letter} is too short ({len(opt.strip())} chars, minimum {MIN_OPTION_CHARS})")

    # ── 8. Correct answer is A, B, C, or D ───────────────────────────────────
    correct = q.get("correct_answer", "")
    if correct not in VALID_ANSWERS:
        err("correct_answer", f"'{correct}' is not valid. Must be one of: A, B, C, D")

    # ── 9. Call of question ──────────────────────────────────────────────────
    coq = q.get("call_of_question", "")
    if not coq or len(coq.strip()) < MIN_CALL_OF_QUESTION_CHARS:
        err("call_of_question", f"Too short or empty ({len(coq.strip()) if coq else 0} chars, minimum {MIN_CALL_OF_QUESTION_CHARS})")

    # ── 10. Explanation ──────────────────────────────────────────────────────
    expl = q.get("explanation", "")
    if not expl or len(expl.strip()) < MIN_EXPLANATION_CHARS:
        err("explanation", f"Too short ({len(expl.strip()) if expl else 0} chars, minimum {MIN_EXPLANATION_CHARS}). Must begin with statutory citation.")
    elif not re.match(r'^Under\s', expl.strip(), re.IGNORECASE):
        err("explanation", "Must begin with 'Under [statute], [section]...'", severity="WARNING")

    # ── 11. Why-wrong explanations ───────────────────────────────────────────
    for letter in ["A", "B", "C", "D"]:
        field = f"why_{letter}_wrong"
        why = q.get(field, "")
        if not why or len(why.strip()) < MIN_WHY_WRONG_CHARS:
            err(field, f"Too short ({len(why.strip()) if why else 0} chars, minimum {MIN_WHY_WRONG_CHARS}). Must explain the specific legal error.")
        # Check that the correct answer's why_wrong acknowledges it's correct
        if letter == correct and why and "correct answer" not in why.lower() and "correct" not in why.lower():
            err(field, (
                f"Option {letter} is the correct answer. "
                f"why_{letter}_wrong should state 'This IS the correct answer.' "
                f"followed by a brief restatement."
            ), severity="WARNING")

    # ── 12. Source reference completeness ────────────────────────────────────
    sr = q.get("source_reference", {})
    if not isinstance(sr, dict):
        err("source_reference", "Must be an object")
    else:
        sr_required = ["lso_material", "subject", "chapter", "heading", "page", "rule_or_statute_reference"]
        for field in sr_required:
            val = sr.get(field, "")
            if not val or not str(val).strip():
                err(f"source_reference.{field}", f"Required sub-field '{field}' is missing or empty")

        statute_ref = sr.get("rule_or_statute_reference", "")
        if statute_ref and not STATUTE_REF_PATTERN.match(statute_ref):
            err(
                "source_reference.rule_or_statute_reference",
                f"'{statute_ref}' — must include Act/Rule name AND specific section number "
                f"(e.g. 'Rules of Civil Procedure, r. 20.04(1)')",
                severity="WARNING"
            )

    # ── 13. PR angle ─────────────────────────────────────────────────────────
    pr = q.get("pr_angle", {})
    if not isinstance(pr, dict):
        err("pr_angle", "Must be an object with keys 'applicable' and 'pr_issue_type'")
    else:
        if "applicable" not in pr:
            err("pr_angle.applicable", "Required field 'applicable' (boolean) is missing")
        if pr.get("applicable") and not pr.get("pr_issue_type"):
            err("pr_angle.pr_issue_type", "Must be non-null when pr_angle.applicable is true")
        if not pr.get("applicable") and pr.get("pr_issue_type") is not None:
            err("pr_angle.pr_issue_type", "Should be null when pr_angle.applicable is false", severity="WARNING")

    # ── 14. Arrays ───────────────────────────────────────────────────────────
    for field in ["exam_trigger_words", "tested_concepts"]:
        val = q.get(field, [])
        if not isinstance(val, list):
            err(field, "Must be an array")
        elif len(val) == 0:
            err(field, "Array must not be empty — provide at least one entry", severity="WARNING")

    # ── 15. Estimated time ───────────────────────────────────────────────────
    est = q.get("estimated_time_seconds")
    if est is not None:
        if not isinstance(est, int):
            err("estimated_time_seconds", f"Must be an integer, got: {type(est).__name__}")
        elif not (60 <= est <= 300):
            err("estimated_time_seconds", f"{est}s is outside expected range 60–300 seconds", severity="WARNING")
        # Cross-check difficulty vs. estimated time
        difficulty_time_ranges = {
            "easy": (60, 120),
            "medium": (90, 150),
            "hard": (120, 200),
            "exam_trap": (150, 300),
        }
        if difficulty in difficulty_time_ranges:
            lo, hi = difficulty_time_ranges[difficulty]
            if not (lo <= est <= hi):
                err("estimated_time_seconds", (
                    f"{est}s is inconsistent with difficulty '{difficulty}' "
                    f"(expected {lo}–{hi}s)"
                ), severity="WARNING")

    # ── 16. Validation status ────────────────────────────────────────────────
    vstatus = q.get("validation_status", "")
    if vstatus not in VALID_VALIDATION_STATUSES:
        err("validation_status", f"'{vstatus}' is not valid. Must be one of: {sorted(VALID_VALIDATION_STATUSES)}")

    # ── 17. Similarity risk ──────────────────────────────────────────────────
    srisk = q.get("similarity_risk", "")
    if srisk not in VALID_SIMILARITY_RISKS:
        err("similarity_risk", f"'{srisk}' is not valid. Must be one of: {sorted(VALID_SIMILARITY_RISKS)}")
    elif srisk == "high":
        err("similarity_risk", "similarity_risk is 'high' — this question MUST be rewritten before use in any session")

    # ── 18. Dates ────────────────────────────────────────────────────────────
    for date_field in ["created_at", "updated_at"]:
        dval = q.get(date_field, "")
        if dval:
            try:
                date.fromisoformat(str(dval))
            except ValueError:
                err(date_field, f"'{dval}' is not a valid ISO 8601 date (YYYY-MM-DD)")

    return errors


def validate_file(path: Path, strict: bool = False) -> tuple[int, int, int]:
    """
    Validate all questions in a JSON file.
    Returns (total_questions, error_count, warning_count).
    """
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"\n❌ JSON PARSE ERROR in {path}: {e}")
        return 0, 1, 0
    except OSError as e:
        print(f"\n❌ FILE ERROR: {e}")
        return 0, 1, 0

    if isinstance(data, dict):
        questions = [data]  # single question object
    elif isinstance(data, list):
        questions = data
    else:
        print(f"\n❌ {path}: Root must be a JSON object or array")
        return 0, 1, 0

    total_errors = 0
    total_warnings = 0

    for q in questions:
        if not isinstance(q, dict):
            print(f"  ❌ Non-object entry in array: {q!r}")
            total_errors += 1
            continue

        issues = validate_question(q)
        errors = [i for i in issues if i.severity == "ERROR"]
        warnings = [i for i in issues if i.severity == "WARNING"]

        if strict:
            # In strict mode, similarity_risk=medium is also an error
            sr = q.get("similarity_risk", "")
            if sr == "medium":
                errors.append(ValidationError(q.get("id", "?"), "similarity_risk", "strict mode: medium risk requires review"))

        total_errors += len(errors)
        total_warnings += len(warnings)

        if errors or warnings:
            qid = q.get("id", "<no id>")
            print(f"\n  Question: {qid}")
            for e in errors:
                print(f"    ❌ {e.field}: {e.message}")
            for w in warnings:
                print(f"    ⚠️  {w.field}: {w.message}")

    return len(questions), total_errors, total_warnings


def collect_files(target: Path) -> list[Path]:
    """Collect all .json question files from a file or directory."""
    if target.is_file():
        return [target]
    elif target.is_dir():
        files = sorted(target.rglob("*.json"))
        # Exclude blueprint files and meta files
        return [f for f in files if not f.name.startswith("_") and "blueprint" not in str(f)]
    else:
        return []


# ── Entry Point ───────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(0)

    strict = "--strict" in args
    summary_only = "--summary" in args
    paths = [a for a in args if not a.startswith("--")]

    if not paths:
        print("Error: No file or directory specified.")
        sys.exit(2)

    target = Path(paths[0])
    if not target.exists():
        print(f"Error: '{target}' does not exist.")
        sys.exit(2)

    files = collect_files(target)
    if not files:
        print(f"No question JSON files found in '{target}'.")
        sys.exit(0)

    grand_total = 0
    grand_errors = 0
    grand_warnings = 0

    print(f"\n{'='*60}")
    print(f"LSO Barrister — Question Validator")
    print(f"Target: {target}")
    print(f"Files:  {len(files)}")
    print(f"Strict: {strict}")
    print(f"{'='*60}")

    for fpath in files:
        if not summary_only:
            print(f"\n📄 {fpath}")
        total, errors, warnings = validate_file(fpath, strict=strict)
        grand_total += total
        grand_errors += errors
        grand_warnings += warnings

        if not summary_only:
            status = "✅ PASS" if errors == 0 else f"❌ FAIL ({errors} errors)"
            print(f"   {status} — {total} questions, {warnings} warnings")

    print(f"\n{'='*60}")
    print(f"SUMMARY")
    print(f"  Files processed:  {len(files)}")
    print(f"  Total questions:  {grand_total}")
    print(f"  Total errors:     {grand_errors}")
    print(f"  Total warnings:   {grand_warnings}")

    if grand_errors == 0:
        print(f"\n✅ All questions pass validation.")
    else:
        print(f"\n❌ {grand_errors} error(s) found. Fix before use in exam sessions.")

    print(f"{'='*60}\n")
    sys.exit(0 if grand_errors == 0 else 1)


if __name__ == "__main__":
    main()
