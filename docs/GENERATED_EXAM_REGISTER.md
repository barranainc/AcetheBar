# Generated Exam Register

**Project:** AcetheBar — LSO Barrister Licensing Examination Practice System  
**Last updated:** 2026-05-24

---

## Purpose

This register tracks every exam available in the AcetheBar hub. It distinguishes:

- **Imported exams** — third-party or official practice exams ingested as-is. Never modified.
- **Generated exams** — assembled from the internal AI-assisted question bank. Must be treated as draft until source-checked by a qualified reviewer.

---

## Section 1 — Imported Exams (Frozen)

These exams were imported from external sources. Their question text, answer keys, and explanations are **never modified** by any generation or assembly pipeline. They are stored baked into `index.html` as base64.

| Exam Key | Tab Label | Questions | Subjects | Source | Status |
|----------|-----------|-----------|----------|--------|--------|
| `bar` | LSO Barrister — Practice Exam A | 160 | CIV / CRIM / FAM / PUB | Imported (3rd-party) | Frozen — do not modify |
| `sol` | LSO Solicitor — Practice Exam | Variable | Multiple solicitor subjects | Imported (3rd-party) | Frozen — do not modify |
| `mini` | Mini Barrister | Variable | Mixed | Imported (3rd-party) | Frozen — do not modify |
| `abp` | Access the Bar Practice | Variable | Mixed | Imported (3rd-party) | Frozen — do not modify |
| `bar2` | LSO Barrister — Practice Exam B | 160 | CIV / CRIM / FAM / PUB / PR | Imported (3rd-party) | Frozen — do not modify |

**Hard constraint:** No script, tool, or manual edit may alter the base64 payloads for `bar`, `sol`, `mini`, `abp`, or `bar2` in `index.html`.

---

## Section 2 — Generated Exams

Generated exams are assembled from `data/questions/` using `tools/assemble_exam.py`. Each generated exam has:

1. A compact JSON file at `data/exams/{exam-id}.json` — the 160-question array in hub-compact format
2. A manifest at `data/exams/{exam-id}-manifest.json` — full audit trail
3. A tab in `index.html` with base64 payload baked in from the compact JSON

### ⚠️ Draft Status Notice

> All generated exams carry **`validation_status: draft`** on every question until a qualified reviewer has source-checked each question against the official 2026 LSO Barrister Examination materials. Generated exams must **not** be presented as official LSO content. Tab labels must use "Generated" (not "LSO") to distinguish them from imported official exams.

---

### Generated Barrister C

| Field | Value |
|-------|-------|
| **Exam key** | `barc` |
| **Tab label** | Generated Barrister C |
| **Assembly file** | `data/exams/generated-barrister-c.json` |
| **Manifest** | `data/exams/generated-barrister-c-manifest.json` |
| **Assembled** | 2026-05-24 (reassembled after Phase 2C-HR human-review flag resolution; prior: Phase 2C 2026-05-24; original: 2026-05-23T21:50:26 UTC) |
| **Assembly tool** | `tools/assemble_exam.py --exam-id generated-barrister-c --exam-label "Generated Barrister C" --seed 1` |
| **Seed** | 1 (deterministic — re-running with seed 1 produces identical question selection) |
| **Total questions** | 160 |
| **Subject allocation** | Civil Litigation: 43 · Criminal Law: 43 · Family Law: 39 · Public Law: 35 |
| **PR treatment** | Embedded overlay (pr_angle.applicable) — PR is not a separate section |
| **PR-angle count** | 3 (civ-06-injunction-005, civ-07-sumj-ev-004, crim-02-s9-detent-004) |
| **Validation status** | All 160 questions: `draft` |
| **Similarity risk** | All 160 questions: `low` |
| **Difficulty split** | Easy: 28 · Medium: 58 · Hard: 47 · Exam-trap: 27 |
| **Legal review** | Phase 2C QA complete — 26 fixes applied, 6 questions flagged for human review. See `docs/LEGAL_QA_GENERATED_BARRISTER_C.md`. Remaining flags (A–D from BLUEPRINT_AUDIT_REPORT.md) must also be resolved before promoting to `source_checked`. |
| **Baked into index.html** | Yes — `barc` base64 payload updated 2026-05-24 after Phase 2C-HR (length: 381,984 chars) |
| **Source question files** | See manifest `source_files` array (14 chapter files across 4 subjects) |

#### Legal Source Constraints
- All questions draw exclusively from official 2026 LSO Barrister materials
- No questions are sourced from Access the Bar, Brigham, or any third-party prep provider
- Flagged subtopics (Blueprint Audit Flags A–D) are included in this exam; their legal citations require reviewer confirmation before the exam is promoted beyond `draft`

#### Phase 2C Legal QA Summary (2026-05-24)
- **130 questions:** PASS — no legal content issues found
- **26 questions:** FIXED — legal content errors corrected (citation errors, wrong section numbers, pr_angle tags, chronology errors)
- **6 questions:** originally flagged for HUMAN REVIEW

#### Phase 2C-HR Human-Review Resolution (2026-05-24)
- **5 of 6 flags resolved:** fam-03-excl-prop-001–004 (FLA s.4(2) numbered paragraphs confirmed; citations corrected) and fam-03-deduct-marr-004 (explanation corrected)
- **1 flag remaining:** fam-04-mh-consent-003 — substance confirmed correct; s. 21 subsection number (s.21(2) vs s.21(3)) unverifiable via online fetch; reviewer should confirm with direct statute access
- **Total fixes:** 31 (26 Phase 2C + 5 Phase 2C-HR)
- Full per-question table: `docs/LEGAL_QA_GENERATED_BARRISTER_C.md`

#### To Re-Assemble Exam C
```bash
python3 tools/assemble_exam.py \
  --exam-id generated-barrister-c \
  --exam-label "Generated Barrister C" \
  --seed 1
```
Then bake the updated compact JSON into index.html (see GENERATION_WORKFLOW.md).

---

### Generated Barrister D

| Field | Value |
|-------|-------|
| **Exam key** | `bard` |
| **Tab label** | Generated Barrister D |
| **Assembly file** | `data/exams/generated-barrister-d.json` |
| **Manifest** | `data/exams/generated-barrister-d-manifest.json` |
| **Assembled** | 2026-05-24 (reassembled after Phase 2E-QA fix to crim-02-sw-issu-004 explanation; original: 2026-05-25T01:25:52 UTC) |
| **Assembly tool** | `tools/assemble_exam.py --exam-id generated-barrister-d --exam-label "Generated Barrister D" --seed 2 --exclude data/exams/generated-barrister-c-manifest.json` |
| **Seed** | 2 (deterministic — re-running with seed 2 and same exclusion produces identical question selection) |
| **Total questions** | 160 |
| **Subject allocation** | Civil Litigation: 43 · Criminal Law: 43 · Family Law: 39 · Public Law: 35 |
| **PR treatment** | Embedded overlay (pr_angle.applicable) — PR is not a separate section |
| **PR-angle count** | 2 |
| **Validation status** | All 160 questions: `draft` |
| **Similarity risk** | All 160 questions: `low` |
| **Difficulty split** | Easy: 28 · Medium: 71 · Hard: 49 · Exam-trap: 12 |
| **Legal review** | Phase 2E QA complete — 1 fix applied, 1 question flagged for human review. See `docs/LEGAL_QA_GENERATED_BARRISTER_D.md`. |
| **Baked into index.html** | Yes — `bard` base64 payload updated 2026-05-24 after Phase 2E QA (length: 432,264 chars) |
| **Source question files** | See manifest `source_files` array (43 chapter files across 4 subjects) |
| **Overlap with C** | 0 questions — verified via set intersection of question_ids_used |

#### Legal Source Constraints
- All questions draw exclusively from official 2026 LSO Barrister materials
- No questions are sourced from Access the Bar, Brigham, or any third-party prep provider
- Excluded all 160 questions used in Generated Barrister C

#### Phase 2E Legal QA Summary (2026-05-24)
- **158 questions:** PASS — no legal content issues found
- **1 question:** FIXED — crim-06-burden-001 source_reference citation corrected ([1997] 3 SCR 320 → [1997] 2 SCR 1 for *R v Lifchus*)
- **1 question:** HUMAN REVIEW — crim-02-sw-issu-004: explanation cleaned of drafting artifact; core legal proposition (30-day s.487 warrant expiry) requires reviewer confirmation against 2026 LSO Criminal Law materials
- Full per-question table: `docs/LEGAL_QA_GENERATED_BARRISTER_D.md`

#### To Re-Assemble Exam D
```bash
python3 tools/assemble_exam.py \
  --exam-id generated-barrister-d \
  --exam-label "Generated Barrister D" \
  --seed 2 \
  --exclude data/exams/generated-barrister-c-manifest.json
```
Then bake the updated compact JSON into index.html (see GENERATION_WORKFLOW.md).

---

### Generated Barrister E

| Field | Value |
|-------|-------|
| **Exam key** | `bare` |
| **Tab label** | Generated Barrister E |
| **Assembly file** | `data/exams/generated-barrister-e.json` |
| **Manifest** | `data/exams/generated-barrister-e-manifest.json` |
| **Assembled** | 2026-05-24 (Phase 2G) |
| **Assembly tool** | `tools/assemble_exam.py --exam-id generated-barrister-e --exam-label "Generated Barrister E" --seed 3 --exclude data/exams/generated-barrister-c-manifest.json --exclude data/exams/generated-barrister-d-manifest.json` |
| **Seed** | 3 (deterministic — re-running with seed 3 and same exclusions produces identical selection) |
| **Total questions** | 160 |
| **Subject allocation** | Civil Litigation: 43 · Criminal Law: 43 · Family Law: 39 · Public Law: 35 |
| **PR treatment** | Embedded overlay (pr_angle.applicable) — PR is not a separate section |
| **PR-angle count** | 3 |
| **Validation status** | All 160 questions: `draft` |
| **Similarity risk** | All 160 questions: `low` |
| **Difficulty split** | Easy: 10 · Medium: 72 · Hard: 65 · Exam-trap: 13 |
| **Legal review** | Phase 2G-QA not yet started — all questions remain `draft` |
| **Baked into index.html** | Yes — `bare` base64 payload baked 2026-05-24 (length: 467,732 chars) |
| **Source question files** | See manifest `source_files` array (across 4 subjects) |
| **Overlap with C** | 0 questions — verified via set intersection of question_ids_used |
| **Overlap with D** | 0 questions — verified via set intersection of question_ids_used |

#### Legal Source Constraints
- All questions draw exclusively from official 2026 LSO Barrister materials
- No questions are sourced from Access the Bar, Brigham, or any third-party prep provider
- Excluded all 160 questions used in Generated Barrister C
- Excluded all 160 questions used in Generated Barrister D

#### Phase 2G Assembly Notes (2026-05-24)
- `tools/assemble_exam.py` updated to support multiple `--exclude` flags (`action='append'`)
- Pool available after C+D exclusions: 148 CIV / 153 CRIM / 134 FAM / 121 PUB
- All 160 selected questions: validation_status=draft, similarity_risk=low
- Legal QA (Phase 2G-QA) not yet run — exam is draft only; do not present as study-ready

#### To Re-Assemble Exam E
```bash
python3 tools/assemble_exam.py \
  --exam-id generated-barrister-e \
  --exam-label "Generated Barrister E" \
  --seed 3 \
  --exclude data/exams/generated-barrister-c-manifest.json \
  --exclude data/exams/generated-barrister-d-manifest.json
```
Then bake the updated compact JSON into index.html (see GENERATION_WORKFLOW.md).

---

## Section 3 — Future Generated Exams (Not Yet Built)

| Planned ID | Label | Target allocation | Seed | Status |
|------------|-------|-------------------|------|--------|
| `barf` | Generated Barrister F | 43/43/39/35 | 4 | Not yet generated — requires Phase 2H question generation |

**Note:** Exam F will exclude questions already used in Exams C, D, and E (three `--exclude` flags on `tools/assemble_exam.py`). Each will require sufficient question bank depth beyond the current baseline.

---

## Section 4 — Audit Checklist (per generated exam)

Before injecting any generated exam into index.html, confirm:

- [ ] Exam has exactly 160 questions
- [ ] Allocation is 43 CIV / 43 CRIM / 39 FAM / 35 PUB (or documented deviation)
- [ ] All selected question IDs exist in `data/questions/`
- [ ] No duplicate question IDs within the exam
- [ ] No question from this exam is copied from an imported exam (`bar`, `sol`, `mini`, `abp`, `bar2`)
- [ ] Exam JSON baked into index.html matches `data/exams/{id}.json` exactly (base64 round-trip)
- [ ] Manifest confirms `seed`, `generated_at`, and `source_files`
- [ ] Tab label uses "Generated" prefix (not "LSO")
- [ ] Existing imported exam data is unchanged (spot-check `bar` and `bar2` base64 lengths)

---

*This register is maintained manually. Update it whenever a new generated exam is added or an existing one is re-assembled.*
