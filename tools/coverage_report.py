#!/usr/bin/env python3
"""
coverage_report.py — LSO Barrister Practice Exam System
=========================================================
Compares blueprint targets against actual generated and verified question counts.
Identifies gaps, under-covered chapters, and missing PR-angle questions.

Usage:
    python tools/coverage_report.py [--subject SUBJECT] [--format FORMAT]

Options:
    --subject   Filter to one subject (e.g. civil-litigation, criminal-law).
                Omit to report on all subjects.
    --format    Output format: table (default) | json | gaps-only

Examples:
    # Full report for all subjects
    python tools/coverage_report.py

    # Report for civil litigation only
    python tools/coverage_report.py --subject civil-litigation

    # Show only subtopics below minimum_question_count
    python tools/coverage_report.py --gaps-only

    # Export coverage data as JSON (for analytics dashboard integration)
    python tools/coverage_report.py --format json

Exit codes:
    0 — all subjects meet minimum_question_count in all subtopics
    1 — one or more subtopics are below minimum_question_count
    2 — file/directory not found or parse error
"""

import json
import os
import sys
from pathlib import Path
from collections import defaultdict


# ── Path constants ─────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent
BLUEPRINTS_DIR = REPO_ROOT / "data" / "blueprints"
QUESTIONS_DIR = REPO_ROOT / "data" / "questions"
SUBJECTS_FILE = BLUEPRINTS_DIR / "barrister-subjects.json"

SUBJECT_KEY_TO_DIR = {
    "civil_litigation": "civil-litigation",
    "criminal_law": "criminal-law",
    "family_law": "family-law",
    "public_law": "public-law",
    "professional_responsibility": "professional-responsibility",
}

SUBJECT_DIR_TO_BLUEPRINT = {
    "civil-litigation": "civil-litigation.json",
    "criminal-law": "criminal-law.json",
    "family-law": "family-law.json",
    "public-law": "public-law.json",
    "professional-responsibility": "professional-responsibility.json",
}


# ── Data Loading ───────────────────────────────────────────────────────────────

def load_json(path: Path) -> dict | list | None:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        print(f"  ❌ JSON parse error in {path}: {e}", file=sys.stderr)
        return None


def load_questions_for_subject(subject_dir: str) -> list[dict]:
    """Load all question objects from all chapter files in a subject folder."""
    folder = QUESTIONS_DIR / subject_dir
    if not folder.exists():
        return []
    questions = []
    for fpath in sorted(folder.glob("*.json")):
        if fpath.name.startswith("_"):
            continue
        data = load_json(fpath)
        if isinstance(data, list):
            questions.extend(data)
        elif isinstance(data, dict):
            questions.append(data)
    return questions


def index_questions(questions: list[dict]) -> dict:
    """
    Build an index of questions keyed by (chapter_number, subtopic_id).
    Returns dict mapping that tuple to list of question objects.
    """
    index = defaultdict(list)
    for q in questions:
        ch = q.get("chapter_number")
        sub = q.get("subtopic_id", "")
        if ch is not None and sub:
            index[(ch, sub)].append(q)
    return index


# ── Coverage Computation ───────────────────────────────────────────────────────

class SubtopicCoverage:
    def __init__(self, subject_label, chapter_number, chapter_title, topic_heading,
                 subtopic_id, subtopic_heading, priority_weight,
                 target, minimum, difficulty_split):
        self.subject_label = subject_label
        self.chapter_number = chapter_number
        self.chapter_title = chapter_title
        self.topic_heading = topic_heading
        self.subtopic_id = subtopic_id
        self.subtopic_heading = subtopic_heading
        self.priority_weight = priority_weight
        self.target = target
        self.minimum = minimum
        self.difficulty_split = difficulty_split  # blueprint targets

        # Populated after loading questions
        self.total = 0
        self.draft = 0
        self.source_checked = 0
        self.human_verified = 0
        self.pr_angle_count = 0
        self.difficulty_counts = {"easy": 0, "medium": 0, "hard": 0, "exam_trap": 0}

    @property
    def is_exam_ready(self) -> bool:
        return self.human_verified >= self.minimum

    @property
    def coverage_pct(self) -> float:
        if self.target == 0:
            return 100.0
        return round(100.0 * self.human_verified / self.target, 1)

    @property
    def gap(self) -> int:
        return max(0, self.minimum - self.human_verified)

    def apply_questions(self, qs: list[dict]):
        self.total = len(qs)
        for q in qs:
            status = q.get("validation_status", "draft")
            if status == "draft":
                self.draft += 1
            elif status == "source_checked":
                self.source_checked += 1
            elif status == "human_verified":
                self.human_verified += 1
            diff = q.get("difficulty", "")
            if diff in self.difficulty_counts:
                self.difficulty_counts[diff] += 1
            pr = q.get("pr_angle", {})
            if isinstance(pr, dict) and pr.get("applicable"):
                self.pr_angle_count += 1


def compute_coverage(blueprint: dict, questions: list[dict]) -> list[SubtopicCoverage]:
    """Compute coverage for every subtopic in the blueprint."""
    q_index = index_questions(questions)
    subject_label = blueprint.get("subject_label", "")
    rows = []

    for chapter in blueprint.get("chapters", []):
        ch_num = chapter.get("chapter_number")
        ch_title = chapter.get("chapter_title", "")
        ch_priority = chapter.get("priority_weight", 3)

        for topic in chapter.get("topics", []):
            topic_heading = topic.get("topic_heading", "")

            for subtopic in topic.get("subtopics", []):
                sub_id = subtopic.get("subtopic_id", "")
                coverage = SubtopicCoverage(
                    subject_label=subject_label,
                    chapter_number=ch_num,
                    chapter_title=ch_title,
                    topic_heading=topic_heading,
                    subtopic_id=sub_id,
                    subtopic_heading=subtopic.get("subtopic_heading", ""),
                    priority_weight=subtopic.get("priority_weight", ch_priority),
                    target=subtopic.get("target_question_count", 0),
                    minimum=subtopic.get("minimum_question_count", 1),
                    difficulty_split=subtopic.get("difficulty_split", {}),
                )
                qs = q_index.get((ch_num, sub_id), [])
                coverage.apply_questions(qs)
                rows.append(coverage)

    return rows


# ── Reporting ──────────────────────────────────────────────────────────────────

RESET = "\033[0m"
RED = "\033[91m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
CYAN = "\033[96m"
BOLD = "\033[1m"
DIM = "\033[2m"


def color_pct(pct: float) -> str:
    if pct >= 100:
        return f"{GREEN}{pct}%{RESET}"
    elif pct >= 60:
        return f"{YELLOW}{pct}%{RESET}"
    else:
        return f"{RED}{pct}%{RESET}"


def priority_star(w: int) -> str:
    return "★" * w + "☆" * (5 - w)


def print_subject_report(subject_label: str, rows: list[SubtopicCoverage], gaps_only: bool):
    print(f"\n{BOLD}{'─'*80}{RESET}")
    print(f"{BOLD}{CYAN}  {subject_label.upper()}{RESET}")
    print(f"{'─'*80}")

    if not rows:
        print("  ⚠️  No blueprint loaded for this subject.")
        return

    # Aggregate totals
    total_subtopics = len(rows)
    ready_subtopics = sum(1 for r in rows if r.is_exam_ready)
    total_target = sum(r.target for r in rows)
    total_verified = sum(r.human_verified for r in rows)
    total_pr = sum(r.pr_angle_count for r in rows)

    print(f"  Subtopics: {ready_subtopics}/{total_subtopics} exam-ready")
    print(f"  Questions: {total_verified}/{total_target} verified ({round(100*total_verified/total_target, 1) if total_target else 0}%)")
    print(f"  PR-angle questions: {total_pr}\n")

    # Header
    col_w = [4, 32, 7, 7, 7, 7, 8]
    headers = ["Pri.", "Subtopic", "Target", "Verify", "Draft", "S.Chkd", "Status"]
    print("  " + " | ".join(h.ljust(w) for h, w in zip(headers, col_w)))
    print("  " + "-+-".join("-" * w for w in col_w))

    for r in sorted(rows, key=lambda x: (-x.priority_weight, x.chapter_number)):
        if gaps_only and r.is_exam_ready:
            continue
        stars = priority_star(r.priority_weight)
        label = f"Ch{r.chapter_number:02d} {r.subtopic_heading}"[:32]
        status = f"{GREEN}✅ READY{RESET}" if r.is_exam_ready else f"{RED}❌ GAP({r.gap}){RESET}"
        row = [
            stars[:4],
            label.ljust(32),
            str(r.target).ljust(7),
            str(r.human_verified).ljust(7),
            str(r.draft).ljust(7),
            str(r.source_checked).ljust(7),
        ]
        print("  " + " | ".join(row) + " | " + status)

    # Difficulty distribution
    all_diffs = {"easy": 0, "medium": 0, "hard": 0, "exam_trap": 0}
    bp_diffs = {"easy": 0, "medium": 0, "hard": 0, "exam_trap": 0}
    for r in rows:
        for d in all_diffs:
            all_diffs[d] += r.difficulty_counts[d]
            bp_diffs[d] += r.difficulty_split.get(d, 0)

    print(f"\n  Difficulty distribution (actual vs. blueprint target):")
    for d in ["easy", "medium", "hard", "exam_trap"]:
        actual = all_diffs[d]
        target = bp_diffs[d]
        bar = "█" * actual + "░" * max(0, target - actual)
        print(f"    {d:12s}: {actual:3d} actual / {target:3d} target  [{bar[:30]}]")


def print_gap_priority(all_rows: list[SubtopicCoverage]):
    """Print a prioritised list of subtopics that need more questions."""
    gaps = [r for r in all_rows if not r.is_exam_ready]
    if not gaps:
        print(f"\n{GREEN}✅ All subtopics meet minimum_question_count. No gaps.{RESET}")
        return

    gaps_sorted = sorted(gaps, key=lambda r: (-r.priority_weight, -r.gap))
    print(f"\n{BOLD}{'─'*80}{RESET}")
    print(f"{BOLD}{RED}  GENERATION PRIORITY LIST — {len(gaps)} subtopics below minimum{RESET}")
    print(f"{'─'*80}")
    print(f"  {'Pri.':<5} {'Subject':<22} {'Ch':>3} {'Subtopic':<30} {'Need':>5} {'Have':>5}")
    print(f"  {'─'*5} {'─'*22} {'─'*3} {'─'*30} {'─'*5} {'─'*5}")
    for r in gaps_sorted:
        subj = r.subject_label[:22]
        sub = r.subtopic_heading[:30]
        print(f"  {'★'*r.priority_weight:<5} {subj:<22} {r.chapter_number:>3}  {sub:<30} {r.gap:>5} {r.human_verified:>5}")


def format_json_output(subject_coverages: dict) -> str:
    """Serialize coverage data as JSON for dashboard integration."""
    out = {}
    for subject_dir, rows in subject_coverages.items():
        subject_data = []
        for r in rows:
            subject_data.append({
                "chapter_number": r.chapter_number,
                "chapter_title": r.chapter_title,
                "subtopic_id": r.subtopic_id,
                "subtopic_heading": r.subtopic_heading,
                "priority_weight": r.priority_weight,
                "target": r.target,
                "minimum": r.minimum,
                "total": r.total,
                "draft": r.draft,
                "source_checked": r.source_checked,
                "human_verified": r.human_verified,
                "pr_angle_count": r.pr_angle_count,
                "difficulty_counts": r.difficulty_counts,
                "is_exam_ready": r.is_exam_ready,
                "coverage_pct": r.coverage_pct,
                "gap": r.gap,
            })
        out[subject_dir] = subject_data
    return json.dumps(out, indent=2)


# ── Entry Point ────────────────────────────────────────────────────────────────

def main():
    args = sys.argv[1:]
    gaps_only = "--gaps-only" in args
    fmt = "table"
    subject_filter = None

    for i, arg in enumerate(args):
        if arg == "--format" and i + 1 < len(args):
            fmt = args[i + 1]
        if arg == "--subject" and i + 1 < len(args):
            subject_filter = args[i + 1]

    # Load subjects index
    subjects_data = load_json(SUBJECTS_FILE)
    if not subjects_data:
        print(f"❌ Cannot load {SUBJECTS_FILE}", file=sys.stderr)
        sys.exit(2)

    subjects = subjects_data.get("subjects", [])
    if subject_filter:
        subjects = [s for s in subjects if SUBJECT_KEY_TO_DIR.get(s["subject_key"]) == subject_filter]
        if not subjects:
            print(f"❌ Subject '{subject_filter}' not found. Valid: {list(SUBJECT_KEY_TO_DIR.values())}")
            sys.exit(2)

    all_rows = []
    subject_coverages = {}

    for subject in subjects:
        subject_key = subject["subject_key"]
        subject_dir = SUBJECT_KEY_TO_DIR.get(subject_key, "")

        # Load blueprint
        bp_path = BLUEPRINTS_DIR / SUBJECT_DIR_TO_BLUEPRINT.get(subject_dir, "")
        blueprint = load_json(bp_path) if bp_path.exists() else None

        # Load questions
        questions = load_questions_for_subject(subject_dir)

        if blueprint:
            rows = compute_coverage(blueprint, questions)
        else:
            # Blueprint not yet created — show placeholder
            rows = []
            print(f"\n  ⚠️  Blueprint not yet created for: {subject['subject_label']}")
            print(f"      Questions loaded: {len(questions)}")
            print(f"      Run: python tools/coverage_report.py after creating the blueprint")

        all_rows.extend(rows)
        subject_coverages[subject_dir] = rows

        if fmt == "table":
            print_subject_report(subject["subject_label"], rows, gaps_only=gaps_only)

    if fmt == "table":
        print_gap_priority(all_rows)
        total_verified = sum(r.human_verified for r in all_rows)
        total_target = sum(r.target for r in all_rows)
        gaps = sum(1 for r in all_rows if not r.is_exam_ready)
        print(f"\n{'─'*80}")
        print(f"OVERALL: {total_verified}/{total_target} verified questions | {gaps} subtopics below minimum")
        print(f"{'─'*80}\n")
    elif fmt == "json":
        print(format_json_output(subject_coverages))

    sys.exit(0 if all(r.is_exam_ready for r in all_rows) else 1)


if __name__ == "__main__":
    main()
