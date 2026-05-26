#!/usr/bin/env python3
"""
Phase 2W — Fix PR rules plural source_reference warnings.

Validator pattern: STATUTE_REF_PATTERN = re.compile(
    r'.*,\\s*(s\\.|r\\.|art\\.|Rule\\s|Part\\s|Schedule\\s|Sched\\.\\s)', re.IGNORECASE)

Problem: "Rules of Professional Conduct (LSO), Rules 3.3-3, 3.3-4, 3.3-5"
  fails because "Rules" (plural) does not match "Rule " (singular + space).

Fix: Change the first rule reference to singular; put remaining in parenthetical.
  "..., Rules 3.3-3, 3.3-4, 3.3-5"
  → "..., Rule 3.3-3 (see also Rules 3.3-4, 3.3-5)"

  "..., Rules 3.4-1, 3.4-5 (multiple co-accused — joint retainer)"
  → "..., Rule 3.4-1 (see also Rule 3.4-5; multiple co-accused — joint retainer)"

  "..., Rules 3.3-1, 5.1-2 (confidentiality and client dishonesty)"
  → "..., Rule 3.3-1 (see also Rule 5.1-2; confidentiality and client dishonesty)"

Only touches source_reference.rule_or_statute_reference.
Does NOT touch explanations, correct answers, or any other field.
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

# Matches the plural-rules suffix pattern we need to fix:
#   ", Rules X.X-Y, X.X-Z"
#   ", Rules X.X-Y, X.X-Z (some note)"
#   ", Rules X.X-Y, X.X-Z, X.X-W"
PLURAL_RULES_PAT = re.compile(
    r',\s*Rules\s+([\d]+\.[\d]+-[\d]+(?:\s*,\s*[\d]+\.[\d]+-[\d]+)*)'
    r'(?:\s+\(([^)]*)\))?$',
    re.IGNORECASE
)


def fix_pr_plural(sr: str) -> tuple[str, bool]:
    """
    Return (new_sr, changed).
    Converts ", Rules X.X-Y, X.X-Z" → ", Rule X.X-Y (see also Rules X.X-Z)"
    """
    m = PLURAL_RULES_PAT.search(sr)
    if not m:
        return sr, False

    rule_nums_str = m.group(1)   # e.g. "3.3-3, 3.3-4, 3.3-5"
    note = m.group(2)            # e.g. "confidentiality and client dishonesty" or None

    # Parse individual rule numbers
    rule_nums = [r.strip() for r in rule_nums_str.split(',') if r.strip()]
    if not rule_nums:
        return sr, False

    first_rule = rule_nums[0]
    rest_rules = rule_nums[1:]

    # Build the replacement suffix
    if rest_rules and note:
        if len(rest_rules) == 1:
            rest_str = f'Rule {rest_rules[0]}'
        else:
            rest_str = 'Rules ' + ', '.join(rest_rules)
        new_suffix = f', Rule {first_rule} (see also {rest_str}; {note})'
    elif rest_rules:
        if len(rest_rules) == 1:
            rest_str = f'Rule {rest_rules[0]}'
        else:
            rest_str = 'Rules ' + ', '.join(rest_rules)
        new_suffix = f', Rule {first_rule} (see also {rest_str})'
    elif note:
        new_suffix = f', Rule {first_rule} ({note})'
    else:
        new_suffix = f', Rule {first_rule}'

    new_sr = sr[:m.start()] + new_suffix
    return new_sr, True


def process_file(fp: Path, dry_run: bool = False) -> dict:
    qs = json.loads(fp.read_text(encoding='utf-8'))
    if not isinstance(qs, list):
        return {'file': fp.name, 'skipped_not_list': True}

    stats = {'file': fp.name, 'total': len(qs), 'fixed': 0}
    changed = False

    for q in qs:
        sr_obj = q.get('source_reference') or {}
        sr = sr_obj.get('rule_or_statute_reference', '')
        new_sr, did_fix = fix_pr_plural(sr)
        if did_fix:
            stats['fixed'] += 1
            if dry_run:
                print(f"  [DRY] {q['id']}:")
                print(f"    FROM: {sr}")
                print(f"    TO:   {new_sr}")
            else:
                q['source_reference']['rule_or_statute_reference'] = new_sr
            changed = True

    if changed and not dry_run:
        fp.write_text(
            json.dumps(qs, ensure_ascii=False, indent=2) + '\n',
            encoding='utf-8'
        )

    return stats


def main(dry_run: bool = False):
    tag = '[DRY-RUN] ' if dry_run else ''
    print(f'{tag}Phase 2W — PR rules plural source_reference fix')
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
