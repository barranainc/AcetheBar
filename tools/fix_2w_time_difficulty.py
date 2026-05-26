#!/usr/bin/env python3
"""
Phase 2W — Fix estimated_time_seconds / difficulty mismatch warnings.

Validator ranges (from validate_question.py):
  easy      → 60–120 s
  medium    → 90–150 s
  hard      → 120–200 s
  exam_trap → 150–300 s

Fix: if estimated_time_seconds is BELOW the minimum for the difficulty,
raise it to the minimum. Never lower a value that is already in range.
"""
import json, re, sys
from pathlib import Path

REPO = Path(__file__).parent.parent

QUESTION_DIRS = [
    REPO / 'data' / 'questions' / 'civil-litigation',
    REPO / 'data' / 'questions' / 'criminal-law',
    REPO / 'data' / 'questions' / 'family-law',
    REPO / 'data' / 'questions' / 'public-law',
    REPO / 'data' / 'questions' / 'professional-responsibility',
]

DIFFICULTY_RANGES = {
    'easy':      (60,  120),
    'medium':    (90,  150),
    'hard':      (120, 200),
    'exam_trap': (150, 300),
}


def process_file(fp: Path, dry_run: bool = False) -> dict:
    qs = json.loads(fp.read_text(encoding='utf-8'))
    if not isinstance(qs, list):
        return {'file': fp.name, 'skipped_not_list': True}

    stats = {'file': fp.name, 'total': len(qs), 'fixed': 0}
    changed = False

    for q in qs:
        diff  = q.get('difficulty', '')
        secs  = q.get('estimated_time_seconds')
        if not diff or secs is None or diff not in DIFFICULTY_RANGES:
            continue

        lo, hi = DIFFICULTY_RANGES[diff]
        if secs < lo:
            old = secs
            if not dry_run:
                q['estimated_time_seconds'] = lo
            stats['fixed'] += 1
            changed = True
            if dry_run:
                print(f"  [DRY] {q['id']}: {old}s → {lo}s  (diff={diff})")
        elif secs > hi:
            # Too high — do NOT lower; this might be intentional
            pass

    if changed and not dry_run:
        fp.write_text(
            json.dumps(qs, ensure_ascii=False, indent=2) + '\n',
            encoding='utf-8'
        )

    return stats


def main(dry_run: bool = False):
    tag = '[DRY-RUN] ' if dry_run else ''
    print(f'{tag}Phase 2W — Time/difficulty mismatch fix')
    print('=' * 60)

    totals = {'total': 0, 'fixed': 0}

    for qdir in QUESTION_DIRS:
        for fp in sorted(qdir.glob('*.json')):
            if fp.name.startswith('_'):
                continue
            stats = process_file(fp, dry_run=dry_run)
            if stats.get('skipped_not_list'):
                continue
            totals['total'] += stats['total']
            totals['fixed'] += stats['fixed']
            if stats['fixed'] > 0:
                print(f"  {'[DRY] ' if dry_run else ''}✅  "
                      f"{fp.parent.name}/{fp.name}: +{stats['fixed']} fixed")

    print()
    print(f"  Total questions : {totals['total']}")
    print(f"  Fixed           : {totals['fixed']}")
    if not dry_run:
        print('\n✅ Files updated.')
    else:
        print('\n(Dry-run — no files modified.)')


if __name__ == '__main__':
    dry = '--dry-run' in sys.argv or '-n' in sys.argv
    main(dry_run=dry)
