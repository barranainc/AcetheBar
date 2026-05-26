#!/usr/bin/env python3
"""
Phase 2W — Fix explanation opening format warnings.

Transforms explanations to begin with 'Under [statute/rule]...' where safe.
Does NOT change legal substance, correct answers, or source_reference content.

Safe transforms applied:
  1. ^Rule(s)?\s    → prepend 'Under '
  2. ^By-Law\s      → prepend 'Under '
  3. ^CYFSA\b       → prepend 'Under '
  4. ^FLA\b         → prepend 'Under '
  5. ^FCSG\b        → prepend 'Under the '
  6. ^Family Law Act\b   → prepend 'Under the '
  7. ^Family Law Rules\b → prepend 'Under the '
  8. ^Divorce Act\b      → prepend 'Under the '
  9. ^Federal Child Support\b → prepend 'Under the '
 10. ^Section\s+\d  → replace 'Section ' with 'Under s.'
 11. ^Sections\s+\d → replace 'Sections ' with 'Under ss.'
 12. ^The [known-statute-keyword] → change 'The ' to 'Under the '
 13. ^The [other]  + valid statute SR → prepend 'Under [SR], the ...'
 14. [other]        + valid statute SR → prepend 'Under [SR], ...'
 15. Everything else → SKIP (case-law-only or no safe prefix)
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

# Validator pattern (from validate_question.py)
ALREADY_OK_PAT = re.compile(r'^Under\s', re.IGNORECASE)

# Source-ref pattern that indicates a proper statute citation
STATUTE_REF_PAT = re.compile(
    r'.*,\s*(s\.|r\.|art\.|Rule\s|Part\s|Schedule\s|Sched\.\s)',
    re.IGNORECASE
)

# Statute-like keywords that appear right after "The " in the explanation
# When matched, safe to change "The " → "Under the "
STATUTE_AFTER_THE_KWS = [
    'CYFSA',
    'Criminal Code',
    'Divorce Act',
    'FRSAEA',
    'Income Tax Act',
    'Interjurisdictional',
    'Judicial Review Procedure',
    'Legal Foundation',
    'Limitations Act',
    'Personal Information',
    'SPPA',
    'Solicitors Act',
    'Spousal Support Advisory',
    'LSO Rules',
    'LSO requires',
    "LSO's",
    "Law Society Act",
    "Children's Law",
    'Convention on',
    r'\d{4}\s+Criminal',   # "2019 Criminal Code..."
]
_THE_STATUTE_PAT = re.compile(
    r'^The\s+(' + '|'.join(STATUTE_AFTER_THE_KWS) + r')',
    re.IGNORECASE
)


def _get_first_sr(sr: str) -> str:
    """Return the first semicolon-delimited clause of the source_reference."""
    return sr.split(';')[0].strip()


def fix_explanation(expl: str, sr: str) -> tuple[str, str]:
    """
    Returns (new_explanation, fix_type).
    fix_type is one of: ALREADY_OK, DIRECT, SECTION, SECTIONS, THE_STATUTE,
                        SR_PREFIX_THE, SR_PREFIX_OTHER, SKIP.
    """
    if ALREADY_OK_PAT.match(expl):
        return expl, 'ALREADY_OK'

    # ── 1–9: Simple direct prepend ──────────────────────────────────────────
    DIRECT_PATTERNS = [
        (re.compile(r'^Rules?\s', re.IGNORECASE),           'Under '),   # Rule / Rules
        (re.compile(r'^By-Law\s\d', re.IGNORECASE),         'Under '),
        (re.compile(r'^CYFSA\b'),                            'Under '),
        (re.compile(r'^FLA\b'),                              'Under '),
        (re.compile(r'^FCSG\b'),                             'Under the '),
        (re.compile(r'^Family Law Act\b', re.IGNORECASE),    'Under the '),
        (re.compile(r'^Family Law Rules\b', re.IGNORECASE),  'Under the '),
        (re.compile(r'^Divorce Act\b', re.IGNORECASE),       'Under the '),
        (re.compile(r'^Federal Child Support\b', re.IGNORECASE), 'Under the '),
    ]
    for pat, prefix in DIRECT_PATTERNS:
        if pat.match(expl):
            return prefix + expl, 'DIRECT'

    # ── 10: Section N → Under s.N ────────────────────────────────────────────
    m = re.match(r'^Section\s+', expl, re.IGNORECASE)
    if m:
        return 'Under s.' + expl[m.end():], 'SECTION'

    # ── 11: Sections N → Under ss.N ──────────────────────────────────────────
    m = re.match(r'^Sections\s+', expl, re.IGNORECASE)
    if m:
        return 'Under ss.' + expl[m.end():], 'SECTIONS'

    # ── 12: "The [statute]..." → "Under the [statute]..." ───────────────────
    if _THE_STATUTE_PAT.match(expl):
        # Replace leading "The " with "Under the "
        return 'Under the ' + expl[4:], 'THE_STATUTE'

    # ── 13: "The [other]..." + valid SR → SR prefix ──────────────────────────
    if re.match(r'^The\s', expl) and STATUTE_REF_PAT.match(sr):
        first_sr = _get_first_sr(sr)
        # "The X..." → "Under [SR], the X..."
        lowered = expl[0].lower() + expl[1:]
        return f'Under {first_sr}, {lowered}', 'SR_PREFIX_THE'

    # ── 14: [other] + valid SR → SR prefix ───────────────────────────────────
    if STATUTE_REF_PAT.match(sr):
        first_sr = _get_first_sr(sr)
        return f'Under {first_sr}, {expl}', 'SR_PREFIX_OTHER'

    # ── 15: Cannot safely fix ─────────────────────────────────────────────────
    return expl, 'SKIP'


def process_file(fp: Path, dry_run: bool = False) -> dict:
    """Process one question file. Returns stats dict."""
    qs = json.loads(fp.read_text(encoding='utf-8'))
    if not isinstance(qs, list):
        return {'file': fp.name, 'skipped_not_list': True}

    stats = {'file': fp.name, 'total': len(qs), 'fixed': 0, 'skipped': 0, 'already_ok': 0}
    changed = False

    for q in qs:
        expl = (q.get('explanation') or '').strip()
        sr   = (q.get('source_reference') or {}).get('rule_or_statute_reference', '')

        new_expl, fix_type = fix_explanation(expl, sr)

        if fix_type == 'ALREADY_OK':
            stats['already_ok'] += 1
        elif fix_type == 'SKIP':
            stats['skipped'] += 1
        else:
            if new_expl != expl:
                stats['fixed'] += 1
                if not dry_run:
                    q['explanation'] = new_expl
                changed = True

    if changed and not dry_run:
        fp.write_text(
            json.dumps(qs, ensure_ascii=False, indent=2) + '\n',
            encoding='utf-8'
        )

    return stats


def main(dry_run: bool = False):
    tag = '[DRY-RUN] ' if dry_run else ''
    print(f'{tag}Phase 2W — Explanation format fix')
    print('=' * 60)

    totals = {'total': 0, 'fixed': 0, 'skipped': 0, 'already_ok': 0}

    for qdir in QUESTION_DIRS:
        for fp in sorted(qdir.glob('*.json')):
            if fp.name.startswith('_'):
                continue
            stats = process_file(fp, dry_run=dry_run)
            if stats.get('skipped_not_list'):
                continue
            for k in ('total', 'fixed', 'skipped', 'already_ok'):
                totals[k] += stats[k]
            if stats['fixed'] > 0:
                print(f"  {'[DRY] ' if dry_run else ''}✅  {fp.parent.name}/{fp.name}: "
                      f"+{stats['fixed']} fixed, {stats['skipped']} skipped")

    print()
    print(f"  Total questions : {totals['total']}")
    print(f"  Already OK      : {totals['already_ok']}")
    print(f"  Fixed           : {totals['fixed']}")
    print(f"  SKIP (accepted) : {totals['skipped']}")
    if not dry_run:
        print('\n✅ Files updated.')
    else:
        print('\n(Dry-run — no files modified.)')


if __name__ == '__main__':
    dry = '--dry-run' in sys.argv or '-n' in sys.argv
    main(dry_run=dry)
