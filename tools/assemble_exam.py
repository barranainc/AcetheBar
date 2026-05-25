#!/usr/bin/env python3
"""
tools/assemble_exam.py — Assemble a 160-question Barrister exam from the generated bank.

Usage:
    python tools/assemble_exam.py [options]

Options:
    --exam-id ID          Short identifier for the exam (default: generated-barrister-c)
    --exam-label LABEL    Human-readable label (default: "Generated Barrister C")
    --seed SEED           Integer seed for deterministic selection (default: 1)
    --exclude FILE        Path to a manifest JSON whose used_ids will be excluded
    --out-dir DIR         Output directory for exam and manifest files (default: data/exams)
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
QUESTIONS_DIR = REPO_ROOT / "data" / "questions"

ALLOCATION = {
    "civil_litigation": 43,
    "criminal_law":     43,
    "family_law":       39,
    "public_law":       35,
}

SUBJECT_DIR = {
    "civil_litigation":          "civil-litigation",
    "criminal_law":               "criminal-law",
    "family_law":                 "family-law",
    "public_law":                 "public-law",
    "professional_responsibility": "professional-responsibility",
}

SUBJECT_LABEL = {
    "civil_litigation":           "Civil Litigation",
    "criminal_law":               "Criminal Law",
    "family_law":                 "Family Law",
    "public_law":                 "Public Law",
    "professional_responsibility": "Professional Responsibility",
}

ANSWER_INDEX = {"A": 0, "B": 1, "C": 2, "D": 3}


# ── Loading ────────────────────────────────────────────────────────────────────

def load_subject(subject_key: str) -> list[dict]:
    """Load all questions for a subject from data/questions/{dir}/."""
    folder = QUESTIONS_DIR / SUBJECT_DIR[subject_key]
    if not folder.exists():
        return []
    questions = []
    for fpath in sorted(folder.glob("*.json")):
        if fpath.name.startswith("_"):
            continue
        try:
            data = json.loads(fpath.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"  ⚠️  JSON parse error in {fpath}: {e}", file=sys.stderr)
            continue
        if isinstance(data, list):
            questions.extend(data)
        elif isinstance(data, dict):
            questions.append(data)
    return questions


def load_bank(subjects: list[str] | None = None) -> dict[str, list[dict]]:
    """Load all questions grouped by subject key."""
    targets = subjects or list(ALLOCATION.keys())
    return {s: load_subject(s) for s in targets}


# ── Selection ──────────────────────────────────────────────────────────────────

def select_questions(
    bank: dict[str, list[dict]],
    allocation: dict[str, int],
    excluded_ids: set[str],
    rng: random.Random,
) -> dict[str, list[dict]]:
    """
    Select questions for each subject.
    - Excludes any question whose id is in excluded_ids.
    - Sorts by priority_weight desc, then shuffles within each priority tier
      using the seeded rng for determinism.
    - Returns dict mapping subject_key → selected question list.
    """
    selected = {}
    for subj_key, count in allocation.items():
        pool = [q for q in bank.get(subj_key, []) if q.get("id") not in excluded_ids]

        # Group by priority_weight, shuffle within each tier, then sort tiers desc
        by_priority: dict[int, list] = {}
        for q in pool:
            pw = q.get("priority_weight", 3)
            by_priority.setdefault(pw, []).append(q)

        ordered = []
        for pw in sorted(by_priority.keys(), reverse=True):
            tier = by_priority[pw]
            rng.shuffle(tier)
            ordered.extend(tier)

        if len(ordered) < count:
            print(
                f"❌ Not enough questions for {subj_key}: "
                f"need {count}, have {len(ordered)} (after exclusions).",
                file=sys.stderr,
            )
            sys.exit(1)

        selected[subj_key] = ordered[:count]
    return selected


# ── Conversion ─────────────────────────────────────────────────────────────────

def to_compact(q: dict, seq_id: int) -> dict:
    """Convert 28-field bank question to 8-field compact exam format."""
    fp  = (q.get("fact_pattern") or "").strip()
    coq = (q.get("call_of_question") or "").strip()
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
        "sec":     SUBJECT_LABEL.get(q.get("subject", ""), ""),
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
    selected: dict[str, list[dict]],
    excluded_ids: set[str],
    allocation: dict[str, int],
) -> dict:
    all_questions = [q for qs in selected.values() for q in qs]

    # Difficulty distribution
    diff_dist = Counter(q.get("difficulty", "unknown") for q in all_questions)

    # Validation status counts
    vs_counts = Counter(q.get("validation_status", "unknown") for q in all_questions)

    # PR-angle count
    pr_count = sum(
        1 for q in all_questions
        if isinstance(q.get("pr_angle"), dict) and q["pr_angle"].get("applicable")
    )

    # Similarity risk
    sim_risk = Counter(q.get("similarity_risk", "unknown") for q in all_questions)

    # Source files used
    source_files: list[str] = []
    for subj_key in allocation:
        folder = QUESTIONS_DIR / SUBJECT_DIR[subj_key]
        for fpath in sorted(folder.glob("*.json")):
            if fpath.name.startswith("_"):
                continue
            rel = str(fpath.relative_to(REPO_ROOT))
            if rel not in source_files:
                source_files.append(rel)

    return {
        "exam_id":           exam_id,
        "exam_label":        exam_label,
        "generated_at":      datetime.now(timezone.utc).isoformat(),
        "seed":              seed,
        "total_questions":   len(all_questions),
        "subject_allocation": {
            subj_key: {
                "label":    SUBJECT_LABEL[subj_key],
                "selected": len(selected[subj_key]),
                "target":   allocation[subj_key],
            }
            for subj_key in allocation
        },
        "question_ids_used": sorted(q["id"] for q in all_questions),
        "excluded_ids":      sorted(excluded_ids),
        "source_files":      source_files,
        "pr_angle_count":    pr_count,
        "difficulty_distribution": dict(diff_dist),
        "validation_status_counts": dict(vs_counts),
        "similarity_risk_counts":  dict(sim_risk),
        "status":            "draft",
        "notes": (
            "Generated Barrister exams are AI-assisted and assembled from the "
            "internal question bank. All questions carry validation_status='draft' "
            "until individually source-checked against official 2026 LSO materials "
            "by a qualified reviewer. Do not present as official LSO exam content."
        ),
    }


# ── Entry Point ────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--exam-id",    default="generated-barrister-c",  help="Short exam identifier")
    parser.add_argument("--exam-label", default="Generated Barrister C",   help="Human-readable label")
    parser.add_argument("--seed",       type=int, default=1,               help="RNG seed for deterministic selection")
    parser.add_argument("--exclude",    metavar="MANIFEST", action="append", help="Manifest file whose used_ids are excluded (repeatable)")
    parser.add_argument("--out-dir",    default="data/exams",              help="Output directory")
    parser.add_argument("--dry-run",    action="store_true",               help="Print summary, do not write files")
    args = parser.parse_args()

    # Excluded IDs — accumulate from all --exclude manifests
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

    rng = random.Random(args.seed)

    # Load
    print(f"Loading question bank…")
    bank = load_bank(list(ALLOCATION.keys()))
    for subj_key, qs in bank.items():
        if subj_key in ALLOCATION:
            print(f"  {SUBJECT_LABEL[subj_key]}: {len(qs)} questions")

    # Select
    print(f"\nSelecting questions (seed={args.seed})…")
    selected = select_questions(bank, ALLOCATION, excluded_ids, rng)
    for subj_key, qs in selected.items():
        print(f"  {SUBJECT_LABEL[subj_key]}: {len(qs)}/{ALLOCATION[subj_key]} selected")

    # Convert to compact format
    compact: list[dict] = []
    seq = 1
    for subj_key in ALLOCATION:
        for q in selected[subj_key]:
            compact.append(to_compact(q, seq))
            seq += 1

    # Build manifest
    manifest = build_manifest(
        exam_id=args.exam_id,
        exam_label=args.exam_label,
        seed=args.seed,
        selected=selected,
        excluded_ids=excluded_ids,
        allocation=ALLOCATION,
    )

    # Dry run
    if args.dry_run:
        print(f"\n── Dry run summary ──")
        print(f"  Exam ID:     {args.exam_id}")
        print(f"  Label:       {args.exam_label}")
        print(f"  Seed:        {args.seed}")
        print(f"  Total Q:     {len(compact)}")
        print(f"  PR-angle:    {manifest['pr_angle_count']}")
        print(f"  Difficulty:  {manifest['difficulty_distribution']}")
        print(f"  Status:      {manifest['validation_status_counts']}")
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

    # Base64 for baking into HTML
    b64 = base64.b64encode(
        json.dumps(compact, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).decode("ascii")

    print(f"\n── Output ──")
    print(f"  Exam file:     {exam_path.relative_to(REPO_ROOT)}")
    print(f"  Manifest file: {manifest_path.relative_to(REPO_ROOT)}")
    print(f"  Base64 length: {len(b64)} chars")
    print(f"  Total Q:       {len(compact)}")
    print(f"  PR-angle:      {manifest['pr_angle_count']}")
    print(f"  Difficulty:    {manifest['difficulty_distribution']}")
    print(f"  Val. status:   {manifest['validation_status_counts']}")
    print(f"  Sim risk:      {manifest['similarity_risk_counts']}")
    print(f"\n✅ Done. Exam assembled as '{args.exam_label}' with seed {args.seed}.")


if __name__ == "__main__":
    main()
