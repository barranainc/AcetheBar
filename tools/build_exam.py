#!/usr/bin/env python3
"""
build_exam.py — LSO Barrister Practice Exam System
====================================================
Assembles question sets from the data layer for various exam modes.
Outputs a structured exam session object ready for the frontend to consume.

Usage (once implemented):
    python tools/build_exam.py --mode subject --subject civil-litigation
    python tools/build_exam.py --mode chapter --subject civil-litigation --chapter 3
    python tools/build_exam.py --mode topic --subject civil-litigation --chapter 3 --topic examination_for_discovery
    python tools/build_exam.py --mode mixed-barrister --count 160
    python tools/build_exam.py --mode weak-area --analytics data/analytics/user_default.json
    python tools/build_exam.py --mode pr-overlay --subject civil-litigation

Exit codes:
    0 — exam built successfully, output written to stdout or --output
    1 — not enough verified questions to meet requested count
    2 — invalid arguments or missing files

NOTE: This file contains stubs only. Full implementation is Phase 4.
      All function signatures, data contracts, and output formats are
      defined here so they can be implemented without redesigning the
      interface later.
"""

import json
import sys
import random
from pathlib import Path
from typing import Optional


# ── Path constants ─────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent
BLUEPRINTS_DIR = REPO_ROOT / "data" / "blueprints"
QUESTIONS_DIR = REPO_ROOT / "data" / "questions"
EXAMS_DIR = REPO_ROOT / "data" / "exams"
ANALYTICS_DIR = REPO_ROOT / "data" / "analytics"

SUBJECT_KEY_TO_DIR = {
    "civil_litigation": "civil-litigation",
    "criminal_law": "criminal-law",
    "family_law": "family-law",
    "public_law": "public-law",
    "professional_responsibility": "professional-responsibility",
}


# ── Output Schema ──────────────────────────────────────────────────────────────
#
# All exam modes produce an ExamSession object with this structure:
#
# {
#   "session_id": "string — unique ID for this session",
#   "mode": "subject_drill | chapter_drill | topic_drill | weak_area | mixed_barrister | pr_overlay",
#   "label": "string — human-readable description of this session",
#   "subject": "string or null",
#   "chapter_number": "integer or null",
#   "topic_id": "string or null",
#   "time_limit_seconds": "integer — 0 means untimed",
#   "question_count": "integer",
#   "questions": [
#     {
#       "id": "...",
#       "subject": "...",
#       "chapter_number": ...,
#       "chapter_title": "...",
#       "topic_heading": "...",
#       "subtopic_heading": "...",
#       "difficulty": "...",
#       "fact_pattern": "...",
#       "call_of_question": "...",
#       "options": { "A": "...", "B": "...", "C": "...", "D": "..." },
#       "correct_answer": "...",
#       "explanation": "...",
#       "why_A_wrong": "...",
#       "why_B_wrong": "...",
#       "why_C_wrong": "...",
#       "why_D_wrong": "...",
#       "estimated_time_seconds": ...,
#       "pr_angle": { "applicable": ..., "pr_issue_type": ... }
#     }
#   ],
#   "created_at": "ISO 8601 datetime",
#   "metadata": { ... }
# }


# ── Data Loading Utilities ─────────────────────────────────────────────────────

def load_json(path: Path):
    """Load a JSON file. Returns None on failure."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"  Warning: Could not load {path}: {e}", file=sys.stderr)
        return None


def load_all_questions(subject_dir: str, status_filter: str = "human_verified") -> list[dict]:
    """
    Load all questions from a subject folder, filtered by validation_status.

    Args:
        subject_dir: Directory name under data/questions/ (e.g. 'civil-litigation')
        status_filter: One of 'draft', 'source_checked', 'human_verified'.
                       Only questions at this status OR higher are returned.
                       Hierarchy: draft < source_checked < human_verified.

    Returns:
        List of question objects.
    """
    # TODO (Phase 4): Implement question loading with status filtering.
    # Use load_json() on each .json file in QUESTIONS_DIR / subject_dir.
    # Filter to questions where validation_status meets or exceeds status_filter.
    # Status hierarchy: draft=0, source_checked=1, human_verified=2
    raise NotImplementedError("load_all_questions — implement in Phase 4")


def load_analytics(analytics_path: Path) -> dict:
    """
    Load user attempt analytics for weak-area drill mode.

    Expected format: { subtopic_id: { accuracy: float, attempts: int, ... }, ... }
    """
    # TODO (Phase 5): Implement analytics loading from localStorage export
    # or from data/analytics/user_default.json.
    raise NotImplementedError("load_analytics — implement in Phase 5")


# ── Mode 1: Subject Drill ──────────────────────────────────────────────────────

def build_subject_drill(
    subject_key: str,
    count: int = 40,
    difficulty: Optional[str] = None,
    shuffle: bool = True,
    status_filter: str = "human_verified",
) -> dict:
    """
    Build a drill session covering one entire subject.

    Selects questions proportionally from all chapters in the subject,
    respecting the blueprint priority weights (higher-weight chapters
    contribute more questions).

    Args:
        subject_key:    e.g. 'civil_litigation'
        count:          Total number of questions in the session (default 40)
        difficulty:     Filter to a single difficulty level, or None for all
        shuffle:        Randomise question order
        status_filter:  Minimum validation_status to include

    Returns:
        ExamSession dict (see Output Schema above)

    Implementation notes (Phase 4):
        1. Load all questions for the subject via load_all_questions()
        2. Load the blueprint to get per-chapter priority weights
        3. Group questions by chapter_number
        4. Allocate `count` questions across chapters proportionally to priority_weight
        5. Within each chapter, sample randomly (preferring harder difficulty for variety)
        6. Return assembled ExamSession
    """
    # TODO (Phase 4)
    raise NotImplementedError("build_subject_drill — implement in Phase 4")


# ── Mode 2: Chapter Drill ──────────────────────────────────────────────────────

def build_chapter_drill(
    subject_key: str,
    chapter_number: int,
    count: Optional[int] = None,
    shuffle: bool = True,
    status_filter: str = "human_verified",
) -> dict:
    """
    Build a drill session covering one chapter of one subject.

    If count is None, uses ALL available verified questions in the chapter.
    If count is specified and fewer questions exist, raises ValueError.

    Args:
        subject_key:     e.g. 'civil_litigation'
        chapter_number:  e.g. 3
        count:           Number of questions, or None for all
        shuffle:         Randomise question order
        status_filter:   Minimum validation_status to include

    Returns:
        ExamSession dict

    Implementation notes (Phase 4):
        1. Load all questions for the subject
        2. Filter to chapter_number
        3. Apply status_filter and optional difficulty filter
        4. Sample or use all, apply shuffle
        5. Return ExamSession
    """
    # TODO (Phase 4)
    raise NotImplementedError("build_chapter_drill — implement in Phase 4")


# ── Mode 3: Topic Drill ────────────────────────────────────────────────────────

def build_topic_drill(
    subject_key: str,
    chapter_number: int,
    topic_id: str,
    subtopic_id: Optional[str] = None,
    shuffle: bool = True,
    status_filter: str = "human_verified",
) -> dict:
    """
    Build a drill session covering one topic (or subtopic) within a chapter.

    Args:
        subject_key:    e.g. 'civil_litigation'
        chapter_number: e.g. 3
        topic_id:       e.g. 'examination_for_discovery'
        subtopic_id:    Optional — if provided, drill only this subtopic
        shuffle:        Randomise question order
        status_filter:  Minimum validation_status to include

    Returns:
        ExamSession dict

    Implementation notes (Phase 4):
        1. Load all questions for subject
        2. Filter to chapter_number + topic_id (+ subtopic_id if provided)
        3. Return all matching questions (this is a focused drill, not sampled)
    """
    # TODO (Phase 4)
    raise NotImplementedError("build_topic_drill — implement in Phase 4")


# ── Mode 4: Weak Area Drill ────────────────────────────────────────────────────

def build_weak_area_drill(
    analytics_path: Path,
    count: int = 20,
    accuracy_threshold: float = 0.65,
    status_filter: str = "human_verified",
) -> dict:
    """
    Build a drill session targeting the student's weakest subtopics.

    A subtopic is 'weak' if the student's accuracy is below accuracy_threshold
    AND they have attempted at least 3 questions in that subtopic.

    Args:
        analytics_path:      Path to user analytics JSON file
        count:               Number of questions to include (default 20)
        accuracy_threshold:  Below this accuracy, a subtopic is flagged weak (default 0.65)
        status_filter:       Minimum validation_status to include

    Returns:
        ExamSession dict, labelled with the weak subtopics targeted

    Implementation notes (Phase 5):
        1. Load analytics via load_analytics()
        2. Find subtopics with accuracy < threshold and attempts >= 3
        3. Sort by accuracy ascending (worst first)
        4. Load questions from those subtopics — prefer questions not yet attempted
        5. If insufficient questions, backfill from next-weakest subtopics
        6. Return ExamSession with metadata listing targeted subtopics

    Weakness analytics shape (loaded from localStorage or analytics JSON):
    {
        "civ-03-scope-exam": {
            "attempts": 8,
            "correct": 4,
            "accuracy": 0.500,
            "avg_time_sec": 85,
            "last_attempted": "2026-05-18"
        },
        ...
    }
    """
    # TODO (Phase 5)
    raise NotImplementedError("build_weak_area_drill — implement in Phase 5")


# ── Mode 5: Mixed Barrister Exam ──────────────────────────────────────────────

def build_mixed_barrister_exam(
    count: int = 160,
    time_limit_seconds: int = 16200,
    status_filter: str = "human_verified",
    seed: Optional[int] = None,
) -> dict:
    """
    Build a full mixed Barrister exam session with questions across all five subjects.

    Questions are allocated proportionally to each subject's lso_weight_percent
    as defined in data/blueprints/barrister-subjects.json.

    Approximate distribution for 160 questions:
        Civil Litigation:        ~40 questions (25%)
        Criminal Law:            ~40 questions (25%)
        Family Law:              ~40 questions (25%)
        Public Law:              ~24 questions (15%)
        Professional Resp.:      ~16 questions (10%)

    Within each subject, questions are sampled proportionally to chapter priority_weight.

    Args:
        count:                Total questions (default 160 = real exam length)
        time_limit_seconds:   Session time limit (default 16200 = 4h 30m)
        status_filter:        Minimum validation_status ('human_verified' for production)
        seed:                 Optional random seed for reproducibility

    Returns:
        ExamSession dict

    Implementation notes (Phase 4):
        1. Load barrister-subjects.json for weight distribution
        2. Compute per-subject question counts from weights
        3. For each subject, call build_subject_drill() to sample questions
        4. Concatenate and shuffle across subjects
        5. Assign a session_id and timestamp
        6. Return ExamSession

    Note: If a subject has fewer verified questions than its allocated count,
    reduce that subject's count and log a warning. Do not silently pad with
    questions from other subjects — this would misrepresent the real exam distribution.
    """
    # TODO (Phase 4)
    raise NotImplementedError("build_mixed_barrister_exam — implement in Phase 4")


# ── Mode 6: PR Overlay ────────────────────────────────────────────────────────

def build_pr_overlay_exam(
    subject_key: Optional[str] = None,
    count: int = 40,
    status_filter: str = "human_verified",
) -> dict:
    """
    Build an exam session consisting exclusively of questions with pr_angle.applicable = true.

    This mode allows students to drill Professional Responsibility dimensions
    as they appear across all five subjects — not just in standalone PR questions.

    Args:
        subject_key:  If provided, limit to PR-angle questions from this subject only.
                      If None, draw from all subjects.
        count:        Number of questions
        status_filter: Minimum validation_status

    Returns:
        ExamSession dict

    Implementation notes (Phase 6):
        1. Load questions from all subjects (or filtered subject)
        2. Filter to questions where pr_angle.applicable == True
        3. Group by pr_issue_type for proportional sampling
        4. Return ExamSession with pr_overlay mode label

    PR issue types to sample from:
        - conflict_of_interest
        - confidentiality
        - duty_to_court
        - trust_accounting
        - withdrawal
        - communication_with_represented_party
        - competence
        - unauthorized_practice
    """
    # TODO (Phase 6)
    raise NotImplementedError("build_pr_overlay_exam — implement in Phase 6")


# ── Session ID Generation ──────────────────────────────────────────────────────

def generate_session_id(mode: str) -> str:
    """
    Generate a unique session ID.
    Format: sess_{mode_abbr}_{YYYYMMDD}_{random_4hex}

    Example: sess_civ_20260518_a3f2
    """
    import datetime
    import secrets
    today = datetime.date.today().strftime("%Y%m%d")
    rand = secrets.token_hex(2)
    abbr = mode.replace("_", "")[:8]
    return f"sess_{abbr}_{today}_{rand}"


# ── Question Sanitizer ─────────────────────────────────────────────────────────

def sanitize_for_session(question: dict) -> dict:
    """
    Strip internal metadata fields from a question before serving to the frontend.
    Removes: validation_status, similarity_risk, created_at, updated_at,
             source_reference (kept as source_label only), lso_dtoc_ref.
    Keeps: everything a student needs to answer and review the question.
    """
    # TODO (Phase 4): Implement field filtering.
    # The frontend should never see similarity_risk or validation_status.
    # source_reference can be summarised as a single string for display.
    raise NotImplementedError("sanitize_for_session — implement in Phase 4")


# ── Entry Point ────────────────────────────────────────────────────────────────

def main():
    """
    CLI entry point for build_exam.py.

    Parses --mode and mode-specific arguments, calls the appropriate builder,
    and writes the resulting ExamSession JSON to stdout or --output file.

    TODO (Phase 4): Implement argument parsing and dispatch.
    """
    args = sys.argv[1:]

    if not args or "--help" in args or "-h" in args:
        print(__doc__)
        sys.exit(0)

    print("build_exam.py: Full implementation is Phase 4.")
    print("Defined modes:")
    print("  --mode subject        build_subject_drill()")
    print("  --mode chapter        build_chapter_drill()")
    print("  --mode topic          build_topic_drill()")
    print("  --mode weak-area      build_weak_area_drill()")
    print("  --mode mixed-barrister build_mixed_barrister_exam()")
    print("  --mode pr-overlay     build_pr_overlay_exam()")
    sys.exit(0)


if __name__ == "__main__":
    main()
