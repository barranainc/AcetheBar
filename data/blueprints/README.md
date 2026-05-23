# Blueprints — LSO Barrister Practice Exam System

This folder contains the structural maps for all five Barrister exam subjects.

## Files

| File | Subject | Status |
|---|---|---|
| `barrister-subjects.json` | Top-level index of all 5 subjects | ✅ Created |
| `civil-litigation.json` | Civil Litigation — full chapter/topic/subtopic map | 🔲 Pending |
| `criminal-law.json` | Criminal Law — full chapter/topic/subtopic map | 🔲 Pending |
| `family-law.json` | Family Law — full chapter/topic/subtopic map | 🔲 Pending |
| `public-law.json` | Public Law — full chapter/topic/subtopic map | 🔲 Pending |
| `professional-responsibility.json` | Professional Responsibility — full map | 🔲 Pending |

## Schema Reference

See `docs/BLUEPRINT_RULES.md` for the full blueprint schema specification.

## Coverage

Run `python tools/coverage_report.py` to see current question coverage against blueprint targets.

## Adding a New Blueprint

1. Read `docs/BLUEPRINT_RULES.md` completely
2. Open the LSO 2026 Barrister Study Materials for the target subject
3. Map every chapter → topic → subtopic from the DTOC
4. Set `priority_weight` based on real exam frequency
5. Set `target_question_count` and `minimum_question_count` for each subtopic
6. Assign `difficulty_split` totalling `target_question_count`
7. Run `python tools/coverage_report.py --subject {subject}` to confirm it loads
