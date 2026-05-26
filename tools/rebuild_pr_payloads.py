#!/usr/bin/env python3
"""
Rebuild PR exam payloads from existing manifests and bake into index.html.
Preserves exact question order from manifest question_ids_used.
Does NOT re-randomize or update manifests.
"""
import base64, json, re, sys
from pathlib import Path

REPO = Path(__file__).parent.parent
PR_DIR = REPO / 'data' / 'questions' / 'professional-responsibility'
HTML = REPO / 'index.html'

ANSWER_INDEX = {'A': 0, 'B': 1, 'C': 2, 'D': 3}

EXAMS = [
    ('prdra',  REPO / 'data' / 'exams' / 'generated-pr-drill-a-manifest.json'),
    ('prdrb',  REPO / 'data' / 'exams' / 'generated-pr-drill-b-manifest.json'),
    ('prb200', REPO / 'data' / 'exams' / 'generated-pr-bank-200-manifest.json'),
]


def load_all_pr_questions() -> dict:
    """Return {id: question_dict} from all PR chapter files."""
    bank = {}
    for fp in sorted(PR_DIR.glob('*.json')):
        if fp.name.startswith('_'):
            continue
        qs = json.loads(fp.read_text(encoding='utf-8'))
        if isinstance(qs, list):
            for q in qs:
                bank[q['id']] = q
    return bank


def to_compact(q: dict, seq: int) -> dict:
    fp  = (q.get('fact_pattern') or '').strip()
    coq = (q.get('call_of_question') or '').strip()
    text = f'{fp}\n\n{coq}'.strip() if fp else coq
    opts = [
        (q.get('options') or {}).get('A', ''),
        (q.get('options') or {}).get('B', ''),
        (q.get('options') or {}).get('C', ''),
        (q.get('options') or {}).get('D', ''),
    ]
    ans  = ANSWER_INDEX.get(q.get('correct_answer', 'A'), 0)
    expl = (q.get('explanation') or '').strip()
    sr   = q.get('source_reference') or {}
    case_ref = (sr.get('rule_or_statute_reference') or '').strip()
    lso  = ' | '.join(filter(None, [
        sr.get('lso_material', ''),
        sr.get('chapter', ''),
        sr.get('heading', ''),
    ]))
    return {'id': seq, 'sec': 'Professional Responsibility',
            'text': text, 'opts': opts, 'ans': ans,
            'expl': expl, 'caseRef': case_ref, 'lso': lso}


def build_b64(manifest_path: Path, bank: dict) -> tuple[str, int]:
    manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    ids = manifest['question_ids_used']
    compact = []
    missing = []
    for seq, qid in enumerate(ids, start=1):
        if qid not in bank:
            missing.append(qid)
            continue
        compact.append(to_compact(bank[qid], seq))
    if missing:
        print(f'  ⚠️  Missing question IDs: {missing}', file=sys.stderr)
    b64 = base64.b64encode(
        json.dumps(compact, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    ).decode('ascii')
    return b64, len(compact)


def main():
    bank = load_all_pr_questions()
    print(f'Loaded {len(bank)} PR questions from bank.')

    html = HTML.read_text(encoding='utf-8')

    for key, manifest_path in EXAMS:
        b64, count = build_b64(manifest_path, bank)
        # Pattern: key: "BASE64"
        pattern = rf'({re.escape(key)}: )"[A-Za-z0-9+/=]+"'
        replacement = rf'\g<1>"{b64}"'
        new_html, n = re.subn(pattern, replacement, html)
        if n == 0:
            print(f'  ❌ Could not find payload injection point for {key}!', file=sys.stderr)
            sys.exit(1)
        html = new_html
        print(f'  ✅ {key}: {count} questions, b64 len={len(b64)}, replacements={n}')

    HTML.write_text(html, encoding='utf-8')
    print(f'\nindex.html updated successfully.')


if __name__ == '__main__':
    main()
