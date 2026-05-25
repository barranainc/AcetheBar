# Generated Exam Register

**Project:** AcetheBar — LSO Barrister Licensing Examination Practice System  
**Last updated:** 2026-05-25

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
| **Legal review status** | Source-checked with flagged questions — see `docs/LEGAL_QA_GENERATED_BARRISTER_E.md` · 154 PASS · 5 FIXED · 1 HUMAN REVIEW REQUIRED (`civ-02-demand-001` — possible s.5(3) citation) · 0 REMOVE |
| **Baked into index.html** | Yes — `bare` base64 payload re-baked 2026-05-25 after QA fixes (length: 468,144 chars) |
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

### Generated Barrister F

| Field | Value |
|-------|-------|
| **Exam key** | `barf` |
| **Tab label** | Generated Barrister F |
| **Assembly file** | `data/exams/generated-barrister-f.json` |
| **Manifest** | `data/exams/generated-barrister-f-manifest.json` |
| **Assembled** | 2026-05-25 (Phase 2I) |
| **Assembly tool** | `tools/assemble_exam.py --exam-id generated-barrister-f --exam-label "Generated Barrister F" --seed 4 --exclude data/exams/generated-barrister-c-manifest.json --exclude data/exams/generated-barrister-d-manifest.json --exclude data/exams/generated-barrister-e-manifest.json` |
| **Seed** | 4 (deterministic — re-running with seed 4 and same exclusions produces identical selection) |
| **Total questions** | 160 |
| **Subject allocation** | Civil Litigation: 43 · Criminal Law: 43 · Family Law: 39 · Public Law: 35 |
| **PR treatment** | Embedded overlay (pr_angle.applicable) — PR is not a separate section |
| **PR-angle count** | 2 |
| **Validation status** | All 160 questions: `draft` |
| **Similarity risk** | All 160 questions: `low` |
| **Difficulty split** | Easy: 25 · Medium: 60 · Hard: 64 · Exam-trap: 11 |
| **Legal review status** | Source-checked with flagged questions — see `docs/LEGAL_QA_GENERATED_BARRISTER_F.md` · 153 PASS · 5 FIXED · 2 HUMAN REVIEW REQUIRED (`fam-08-review-001`, `fam-08-review-var-001`) · 0 REMOVE |
| **Baked into index.html** | Yes — `barf` base64 payload baked 2026-05-25 (length: 497,876 chars after QA fixes) |
| **Source question files** | See manifest `source_files` array (across 4 subjects) |
| **Overlap with C** | 0 questions — verified via set intersection of question_ids_used |
| **Overlap with D** | 0 questions — verified via set intersection of question_ids_used |
| **Overlap with E** | 0 questions — verified via set intersection of question_ids_used |
| **C + D + E + F combined** | 640 unique question IDs — verified |

#### Legal Source Constraints
- All questions draw exclusively from official 2026 LSO Barrister materials
- No questions are sourced from Access the Bar, Brigham, or any third-party prep provider
- Excluded all 160 questions used in Generated Barrister C (480 combined excluded IDs)
- Excluded all 160 questions used in Generated Barrister D
- Excluded all 160 questions used in Generated Barrister E

#### Phase 2I Assembly Notes (2026-05-25)
- Pool available after C+D+E exclusions: CIV 203 / CRIM 208 / FAM 184 / PUB 166
- F-readiness dry run passed in Phase 2H (55 CIV + 55 CRIM + 50 FAM + 45 PUB new questions generated)
- All 160 selected questions: validation_status=draft, similarity_risk=low
- Legal QA (Phase 2I-QA) not yet run — exam is draft only; do not present as study-ready
- Tab color: `#06b6d4` (cyan)

#### To Re-Assemble Exam F
```bash
python3 tools/assemble_exam.py \
  --exam-id generated-barrister-f \
  --exam-label "Generated Barrister F" \
  --seed 4 \
  --exclude data/exams/generated-barrister-c-manifest.json \
  --exclude data/exams/generated-barrister-d-manifest.json \
  --exclude data/exams/generated-barrister-e-manifest.json
```
Then bake the updated compact JSON into index.html (see GENERATION_WORKFLOW.md).

---

## Section 2B — Generated PR Drills

Generated PR drills draw exclusively from `data/questions/professional-responsibility/`. They use the same compact 8-field format and `assemble_pr_drill.py` tool. All questions remain `validation_status: draft`.

---

### Generated PR Drill A

| Field | Value |
|-------|-------|
| **Exam key** | `prdra` |
| **Tab label** | Generated PR Drill A |
| **Assembly file** | `data/exams/generated-pr-drill-a.json` |
| **Manifest** | `data/exams/generated-pr-drill-a-manifest.json` |
| **Assembled** | 2026-05-25 (Phase PR-2) |
| **Assembly tool** | `tools/assemble_pr_drill.py --exam-id generated-pr-drill-a --exam-label "Generated PR Drill A" --seed 101 --count 100` |
| **Seed** | 101 (deterministic — re-running with seed 101 produces identical selection) |
| **Total questions** | 100 |
| **Source folder** | `data/questions/professional-responsibility/` |
| **Chapter distribution** | Ch01:5 · Ch02:10 · Ch03:16 · Ch04:14 · Ch05:6 · Ch06:9 · Ch07:8 · Ch08:7 · Ch09:5 · Ch10:6 · Ch11:6 · Ch12:4 · Ch13:4 |
| **Difficulty split** | Easy:19 · Medium:40 · Hard:28 · Exam-trap:13 |
| **Validation status** | All 100 questions: `draft` |
| **Legal review status** | Not source-checked |
| **Similarity risk** | All 100 questions: `low` |
| **Overlap with Drill B** | 0 questions — verified |
| **Baked into index.html** | Yes — `prdra` base64 payload baked 2026-05-25 (length: 289,064 chars) |

#### To Re-Assemble Drill A
```bash
python3 tools/assemble_pr_drill.py \
  --exam-id generated-pr-drill-a \
  --exam-label "Generated PR Drill A" \
  --seed 101 \
  --count 100
```
Then bake the updated compact JSON into index.html (see GENERATION_WORKFLOW.md).

---

### Generated PR Drill B

| Field | Value |
|-------|-------|
| **Exam key** | `prdrb` |
| **Tab label** | Generated PR Drill B |
| **Assembly file** | `data/exams/generated-pr-drill-b.json` |
| **Manifest** | `data/exams/generated-pr-drill-b-manifest.json` |
| **Assembled** | 2026-05-25 (Phase PR-2) |
| **Assembly tool** | `tools/assemble_pr_drill.py --exam-id generated-pr-drill-b --exam-label "Generated PR Drill B" --seed 102 --count 100 --exclude data/exams/generated-pr-drill-a-manifest.json` |
| **Seed** | 102 (deterministic — re-running with seed 102 and same exclusion produces identical selection) |
| **Total questions** | 100 |
| **Source folder** | `data/questions/professional-responsibility/` |
| **Chapter distribution** | Ch01:7 · Ch02:9 · Ch03:11 · Ch04:12 · Ch05:14 · Ch06:14 · Ch07:5 · Ch08:5 · Ch09:7 · Ch10:5 · Ch11:2 · Ch12:4 · Ch13:5 |
| **Difficulty split** | Easy:19 · Medium:37 · Hard:29 · Exam-trap:15 |
| **Validation status** | All 100 questions: `draft` |
| **Legal review status** | Not source-checked |
| **Similarity risk** | All 100 questions: `low` |
| **Overlap with Drill A** | 0 questions — verified |
| **Baked into index.html** | Yes — `prdrb` base64 payload baked 2026-05-25 (length: 285,404 chars) |

#### To Re-Assemble Drill B
```bash
python3 tools/assemble_pr_drill.py \
  --exam-id generated-pr-drill-b \
  --exam-label "Generated PR Drill B" \
  --seed 102 \
  --count 100 \
  --exclude data/exams/generated-pr-drill-a-manifest.json
```
Then bake the updated compact JSON into index.html (see GENERATION_WORKFLOW.md).

---

### Generated PR Bank 200

| Field | Value |
|-------|-------|
| **Exam key** | `prb200` |
| **Tab label** | Generated PR Bank 200 |
| **Assembly file** | `data/exams/generated-pr-bank-200.json` |
| **Manifest** | `data/exams/generated-pr-bank-200-manifest.json` |
| **Assembled** | 2026-05-25 (Phase PR-2) |
| **Assembly tool** | `tools/assemble_pr_drill.py --exam-id generated-pr-bank-200 --exam-label "Generated PR Bank 200" --all-questions` |
| **Seed** | N/A — `--all-questions` mode; chapter-ordered, deterministic |
| **Total questions** | 200 |
| **Source folder** | `data/questions/professional-responsibility/` |
| **Chapter distribution** | Ch01:12 · Ch02:19 · Ch03:27 · Ch04:26 · Ch05:20 · Ch06:23 · Ch07:13 · Ch08:12 · Ch09:12 · Ch10:11 · Ch11:8 · Ch12:8 · Ch13:9 |
| **Difficulty split** | Easy:38 · Medium:77 · Hard:57 · Exam-trap:28 |
| **Validation status** | All 200 questions: `draft` |
| **Legal review status** | Not source-checked |
| **Similarity risk** | All 200 questions: `low` |
| **Ordering** | Grouped by chapter (Ch01→Ch13), then by question ID within each chapter |
| **Baked into index.html** | Yes — `prb200` base64 payload baked 2026-05-25 (length: 574,612 chars) |

#### To Re-Assemble PR Bank 200
```bash
python3 tools/assemble_pr_drill.py \
  --exam-id generated-pr-bank-200 \
  --exam-label "Generated PR Bank 200" \
  --all-questions
```
Then bake the updated compact JSON into index.html (see GENERATION_WORKFLOW.md).

---

## Section 3 — Future Generated Exams (Not Yet Built)

| Planned ID | Label | Target allocation | Seed | Status |
|------------|-------|-------------------|------|--------|
| `barg` | Generated Barrister G | 43/43/39/35 | 5 | Not yet generated — requires Phase 2J question generation and Phase 2I-QA completion |

**Note:** Exam G will exclude questions already used in Exams C, D, E, and F (four `--exclude` flags on `tools/assemble_exam.py`). It will require sufficient question bank depth beyond the current baseline. Legal QA on Generated Barrister F (Phase 2I-QA) should be completed before assembling Exam G.

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
