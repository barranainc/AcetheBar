#!/usr/bin/env python3
"""
tools/assemble_pr_drill.py — Assemble Professional Responsibility drill exams.

Usage:
    python tools/assemble_pr_drill.py [options]

Options:
    --exam-id ID          Short identifier for the exam
    --exam-label LABEL    Human-readable label
    --seed SEED           RNG seed for deterministic selection (ignored with --all-questions)
    --count N             Number of questions to select (default: 100)
    --all-questions       Include all available questions, ordered by chapter (overrides --count/--seed)
    --exclude FILE        Manifest JSON whose question_ids_used are excluded (repeatable)
    --out-dir DIR         Output directory (default: data/exams)
    --dry-run             Print summary without writing files

Output files:
    data/exams/{exam-id}.json           — Compact 8-field question array (bake into index.html)
    data/exams/{exam-id}-manifest.json  — Full audit manifest

Exit codes:
    0 — success
    1 — not enough questions available
    2 — missing input files or parse error
"""

import argparse
import base64
import json
import random
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

# ── Constants ──────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent
PR_DIR    = REPO_ROOT / "data" / "questions" / "professional-responsibility"

ANSWER_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3}


# ── Loading ────────────────────────────────────────────────────────────────────

def load_pr_questions() -> list[dict]:
    """Load all questions from data/questions/professional-responsibility/."""
    questions = []
    for fpath in sorted(PR_DIR.glob("*.json")):
        if fpath.name.startswith("_"):
            continue
        try:
            data = json.loads(fpath.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"  ⚠️  JSON parse error in {fpath.name}: {e}", file=sys.stderr)
            continue
        if isinstance(data, list):
            questions.extend(data)
        elif isinstance(data, dict):
            questions.append(data)
    return questions


# ── Selection ──────────────────────────────────────────────────────────────────

def select_all_ordered(pool: list[dict]) -> list[dict]:
    """Return all questions sorted by chapter_number then id (for PR Bank 200)."""
    return sorted(pool, key=lambda q: (q.get("chapter_number", 99), q.get("id", "")))


def select_random(pool: list[dict], count: int, rng: random.Random) -> list[dict]:
    """Select `count` questions using priority-weight tiers + seeded shuffle."""
    by_priority: dict[int, list] = {}
    for q in pool:
        pw = q.get("priority_weight", 3)
        by_priority.setdefault(pw, []).append(q)

    ordered: list[dict] = []
    for pw in sorted(by_priority.keys(), reverse=True):
        tier = by_priority[pw]
        rng.shuffle(tier)
        ordered.extend(tier)

    if len(ordered) < count:
        print(
            f"❌ Not enough questions: need {count}, have {len(ordered)} after exclusions.",
            file=sys.stderr,
        )
        sys.exit(1)

    return ordered[:count]


# ── Conversion ─────────────────────────────────────────────────────────────────

def to_compact(q: dict, seq_id: int) -> dict:
    """Convert 28-field bank question to 8-field compact exam format."""
    fp   = (q.get("fact_pattern") or "").strip()
    coq  = (q.get("call_of_question") or "").strip()
    text = f"{fp}\n\n{coq}".strip() if fp else coq

    opts = [
        (q.get("options") or {}).get("A", ""),
        (q.get("options") or {}).get("B", ""),
        (q.get("options") or {}).get("C", ""),
        (q.get("options") or {}).get("D", ""),
    ]

    ans  = ANSWER_INDEX.get(q.get("correct_answer", "A"), 0)
    expl = (q.get("explanation") or "").strip()

    sr       = q.get("source_reference") or {}
    case_ref = (sr.get("rule_or_statute_reference") or "").strip()
    lso      = " | ".join(filter(None, [
        sr.get("lso_material", ""),
        sr.get("chapter", ""),
        sr.get("heading", ""),
    ]))

    return {
        "id":      seq_id,
        "sec":     "Professional Responsibility",
        "text":    text,
        "opts":    opts,
        "ans":     ans,
        "expl":    expl,
        "caseRef": case_ref,
        "lso":     lso,
    }


# ── Manifest ───────────────────────────────────────────────────────────────────

def build_manifest(
    exam_id: str,
    exam_label: str,
    seed: int,
    selected: list[dict],
    excluded_ids: set[str],
    all_questions_mode: bool,
) -> dict:
    diff_dist  = Counter(q.get("difficulty", "unknown") for q in selected)
    vs_counts  = Counter(q.get("validation_status", "unknown") for q in selected)
    sim_risk   = Counter(q.get("similarity_risk", "unknown") for q in selected)
    ch_dist    = Counter(q.get("chapter_number", 0) for q in selected)

    source_files = sorted(
        str(fpath.relative_to(REPO_ROOT))
        for fpath in sorted(PR_DIR.glob("*.json"))
        if not fpath.name.startswith("_")
    )

    return {
        "exam_id":           exam_id,
        "exam_label":        exam_label,
        "generated_at":      datetime.now(timezone.utc).isoformat(),
        "seed":              seed,
        "all_questions_mode": all_questions_mode,
        "total_questions":   len(selected),
        "question_ids_used": sorted(q["id"] for q in selected),
        "excluded_ids":      sorted(excluded_ids),
        "source_files":      source_files,
        "chapter_distribution": {str(k): v for k, v in sorted(ch_dist.items())},
        "difficulty_distribution":  dict(diff_dist),
        "validation_status_counts": dict(vs_counts),
        "similarity_risk_counts":   dict(sim_risk),
        "status":             "draft",
        "legal_review_status": "not source-checked",
        "notes": (
            "Generated PR drill exams are AI-assisted and assembled from the internal "
            "question bank. All questions carry validation_status='draft' until "
            "individually source-checked against official 2026 LSO Barrister materials "
            "by a qualified reviewer. Do not present as official LSO exam content."
        ),
    }


# ── Entry Point ────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--exam-id",       default="generated-pr-drill-a",  help="Short exam identifier")
    parser.add_argument("--exam-label",    default="Generated PR Drill A",   help="Human-readable label")
    parser.add_argument("--seed",          type=int, default=101,            help="RNG seed")
    parser.add_argument("--count",         type=int, default=100,            help="Questions to select")
    parser.add_argument("--all-questions", action="store_true",              help="Include all questions, chapter-ordered")
    parser.add_argument("--exclude",       metavar="MANIFEST", action="append",
                        help="Manifest whose question_ids_used are excluded (repeatable)")
    parser.add_argument("--out-dir",       default="data/exams",             help="Output directory")
    parser.add_argument("--dry-run",       action="store_true",              help="Print summary, do not write files")
    args = parser.parse_args()

    # Collect excluded IDs
    excluded_ids: set[str] = set()
    for exc_file in (args.exclude or []):
        exc_path = Path(exc_file)
        if not exc_path.exists():
            print(f"❌ Exclude manifest not found: {exc_path}", file=sys.stderr)
            sys.exit(2)
        exc_manifest = json.loads(exc_path.read_text(encoding="utf-8"))
        these_ids = set(exc_manifest.get("question_ids_used", []))
        excluded_ids |= these_ids
        print(f"  Excluding {len(these_ids)} IDs from {exc_path.name}")

    # Load
    print(f"Loading PR questions…")
    all_qs = load_pr_questions()
    print(f"  Loaded: {len(all_qs)} questions")

    pool = [q for q in all_qs if q.get("id") not in excluded_ids]
    print(f"  Pool after exclusions: {len(pool)}")

    # Select
    if args.all_questions:
        selected = select_all_ordered(pool)
        print(f"  Mode: all-questions — {len(selected)} questions, chapter-ordered")
    else:
        rng = random.Random(args.seed)
        selected = select_random(pool, args.count, rng)
        print(f"  Mode: random (seed={args.seed}, count={args.count})")

    # Convert
    compact = [to_compact(q, i + 1) for i, q in enumerate(selected)]

    # Validate: no duplicate source IDs
    source_ids = [q["id"] for q in selected]
    if len(source_ids) != len(set(source_ids)):
        dup = [sid for sid in source_ids if source_ids.count(sid) > 1]
        print(f"❌ Duplicate question IDs detected: {set(dup)}", file=sys.stderr)
        sys.exit(1)

    # Build manifest
    manifest = build_manifest(
        exam_id=args.exam_id,
        exam_label=args.exam_label,
        seed=args.seed,
        selected=selected,
        excluded_ids=excluded_ids,
        all_questions_mode=args.all_questions,
    )

    # Dry run
    if args.dry_run:
        print(f"\n── Dry run summary ──")
        print(f"  Exam ID:     {args.exam_id}")
        print(f"  Label:       {args.exam_label}")
        print(f"  Total Q:     {len(compact)}")
        print(f"  Chapters:    {manifest['chapter_distribution']}")
        print(f"  Difficulty:  {manifest['difficulty_distribution']}")
        print(f"  Val. status: {manifest['validation_status_counts']}")
        print(f"  Sim risk:    {manifest['similarity_risk_counts']}")
        return

    # Write files
    out_dir = REPO_ROOT / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    exam_path     = out_dir / f"{args.exam_id}.json"
    manifest_path = out_dir / f"{args.exam_id}-manifest.json"

    exam_path.write_text(
        json.dumps(compact, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    # Base64 (for baking into HTML)
    b64 = base64.b64encode(
        json.dumps(compact, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).decode("ascii")

    print(f"\n── Output ──")
    print(f"  Exam file:     {exam_path.relative_to(REPO_ROOT)}")
    print(f"  Manifest file: {manifest_path.relative_to(REPO_ROOT)}")
    print(f"  Base64 length: {len(b64)} chars")
    print(f"  Total Q:       {len(compact)}")
    print(f"  Chapters:      {manifest['chapter_distribution']}")
    print(f"  Difficulty:    {manifest['difficulty_distribution']}")
    print(f"  Val. status:   {manifest['validation_status_counts']}")
    print(f"  Sim risk:      {manifest['similarity_risk_counts']}")
    print(f"\n✅ Done. '{args.exam_label}' assembled with {len(compact)} questions.")


if __name__ == "__main__":
    main()
