#!/usr/bin/env python3
"""
Phase 3A — Build question metadata for analytics.

Scans all data/questions/**/*.json and extracts per-question metadata.
Also builds exam-position maps from manifests (sequential position → question ID).

Output: data/analytics/question_metadata.json

Metadata structure:
  {
    "version": 1,
    "questions": {
      "civ-02-basic-lim-001": {
        "subject": "Civil Litigation",
        "chapter_number": 2,
        "chapter_title": "Limitation Periods",
        "topic_id": "",
        "topic_heading": "The Basic Two-Year Limitation Period",
        "subtopic_id": "",
        "subtopic_heading": "",
        "difficulty": "easy",
        "rule_or_statute_reference": "...",
        "lso_material": "...",
        "exam_trigger_words": [...],
        "tested_concepts": [...]
      }, ...
    },
    "examPositions": {
      "barc": {"1": "civ-02-basic-lim-001", "2": "...", ...},
      "bard": {...},
      "bare": {...},
      "barf": {...},
      "prdra": {...},
      "prdrb": {...},
      "prb200": {...}
    }
  }
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

# Manifests that provide exam-position → question-ID mappings
EXAM_MANIFESTS = {
    'barc':   REPO / 'data' / 'exams' / 'generated-barrister-c-manifest.json',
    'bard':   REPO / 'data' / 'exams' / 'generated-barrister-d-manifest.json',
    'bare':   REPO / 'data' / 'exams' / 'generated-barrister-e-manifest.json',
    'barf':   REPO / 'data' / 'exams' / 'generated-barrister-f-manifest.json',
    'prdra':  REPO / 'data' / 'exams' / 'generated-pr-drill-a-manifest.json',
    'prdrb':  REPO / 'data' / 'exams' / 'generated-pr-drill-b-manifest.json',
    'prb200': REPO / 'data' / 'exams' / 'generated-pr-bank-200-manifest.json',
}

OUT_FILE = REPO / 'data' / 'analytics' / 'question_metadata.json'


def chapter_number_from_filename(filename: str) -> int:
    """Extract chapter number from filename like 'ch02-limitation-periods.json'."""
    m = re.match(r'^ch(\d+)-', filename)
    return int(m.group(1)) if m else 0


def chapter_title_from_filename(filename: str) -> str:
    """Extract human-readable chapter title from filename."""
    name = re.sub(r'^ch\d+-', '', filename)
    name = name.replace('.json', '').replace('-', ' ')
    return name.title()


def extract_metadata(q: dict, filepath: Path) -> dict:
    """Extract analytics metadata from a question dict."""
    sr = q.get('source_reference') or {}
    pr = q.get('pr_angle') or {}

    # Prefer source_reference chapter info over filename
    chapter_raw = sr.get('chapter', '')
    if chapter_raw:
        # "Chapter 2 — Limitation Periods" → "Limitation Periods"
        chapter_title = re.sub(r'^Chapter\s+\d+\s*[—\-:]+\s*', '', chapter_raw).strip()
        # Also try "Chapter 2: Title"
        chapter_title = re.sub(r'^Chapter\s+\d+\s*', '', chapter_title).strip(' :—-')
        if not chapter_title:
            chapter_title = chapter_title_from_filename(filepath.name)
    else:
        chapter_title = chapter_title_from_filename(filepath.name)

    chapter_num = chapter_number_from_filename(filepath.name)

    # PR angle
    pr_applicable = False
    pr_issue_type = None
    if isinstance(pr, dict):
        pr_applicable = bool(pr.get('applicable', False))
        pr_issue_type = pr.get('pr_issue_type') or None
    elif isinstance(pr, str) and pr:
        pr_applicable = True
        pr_issue_type = pr

    # Abbreviate the statute reference to first 60 chars (for recommendations display)
    rule_ref = (sr.get('rule_or_statute_reference') or '')[:80]

    return {
        'sub': sr.get('subject', ''),           # subject
        'ch': chapter_num,                       # chapter number
        'cht': chapter_title,                    # chapter title
        'top': (sr.get('heading') or '')[:60],   # topic heading
        'dif': q.get('difficulty', ''),          # difficulty
        'ref': rule_ref,                         # statute reference (abbrev)
    }


def build_questions_metadata() -> dict:
    """Scan all question files and build the questions metadata dict."""
    questions = {}
    duplicates = []

    for qdir in QUESTION_DIRS:
        for fp in sorted(qdir.glob('*.json')):
            if fp.name.startswith('_'):
                continue
            try:
                qs = json.loads(fp.read_text(encoding='utf-8'))
            except Exception as e:
                print(f'  ⚠️  Parse error: {fp}: {e}', file=sys.stderr)
                continue
            if not isinstance(qs, list):
                continue
            for q in qs:
                qid = q.get('id')
                if not qid or not isinstance(qid, str):
                    continue   # skip questions without string IDs (imported exams)
                if qid in questions:
                    duplicates.append(qid)
                questions[qid] = extract_metadata(q, fp)

    if duplicates:
        print(f'  ⚠️  Duplicate question IDs found: {duplicates[:10]}', file=sys.stderr)
        sys.exit(1)

    return questions


def build_exam_positions() -> dict:
    """
    Build examPositions: maps exam key → {sequential_pos: question_id}.
    Sequential position is 1-based (matching q.id in compact format).
    """
    positions = {}
    for exam_key, manifest_path in EXAM_MANIFESTS.items():
        if not manifest_path.exists():
            print(f'  ⚠️  Missing manifest: {manifest_path}', file=sys.stderr)
            continue
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
        ids = manifest.get('question_ids_used', [])
        # Position 1 = first question (q.id=1 in compact format)
        positions[exam_key] = {str(i + 1): qid for i, qid in enumerate(ids)}

    return positions


def main():
    print('Phase 3A — Build question metadata')
    print('=' * 50)

    questions = build_questions_metadata()
    print(f'  Scanned: {len(questions)} questions')

    # Validate no duplicate IDs
    print(f'  Duplicate IDs: 0')

    exam_positions = build_exam_positions()
    total_positions = sum(len(v) for v in exam_positions.values())
    print(f'  Exam position maps: {len(exam_positions)} exams, {total_positions} total positions')

    metadata = {
        'version': 1,
        'questions': questions,
        'examPositions': exam_positions,
    }

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(
        json.dumps(metadata, ensure_ascii=False, separators=(',', ':')),
        encoding='utf-8'
    )

    size_kb = OUT_FILE.stat().st_size / 1024
    print(f'\n  ✅  Written: {OUT_FILE.relative_to(REPO)}')
    print(f'      Size: {size_kb:.1f} KB')
    print(f'      Questions: {len(questions)}')
    print(f'      Exam position maps: {list(exam_positions.keys())}')


if __name__ == '__main__':
    main()
