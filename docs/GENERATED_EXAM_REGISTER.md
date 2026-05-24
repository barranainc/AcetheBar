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
| **Assembled** | 2026-05-24 (reassembled after Phase 2C Legal QA fixes; original: 2026-05-23T21:50:26 UTC) |
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
| **Baked into index.html** | Yes — `barc` base64 payload updated 2026-05-24 (length: 381,872 chars) |
| **Source question files** | See manifest `source_files` array (14 chapter files across 4 subjects) |

#### Legal Source Constraints
- All questions draw exclusively from official 2026 LSO Barrister materials
- No questions are sourced from Access the Bar, Brigham, or any third-party prep provider
- Flagged subtopics (Blueprint Audit Flags A–D) are included in this exam; their legal citations require reviewer confirmation before the exam is promoted beyond `draft`

#### Phase 2C Legal QA Summary (2026-05-24)
- **130 questions:** PASS — no legal content issues found
- **26 questions:** FIXED — legal content errors corrected (citation errors, wrong section numbers, pr_angle tags, chronology errors)
- **6 questions:** HUMAN REVIEW REQUIRED — flagged but not auto-fixed (FLA s.4(2) subsection letters; fam-03-deduct-marr-004; fam-04-mh-consent-003)
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

## Section 3 — Future Generated Exams (Not Yet Built)

| Planned ID | Label | Target allocation | Seed | Status |
|------------|-------|-------------------|------|--------|
| `bard` | Generated Barrister D | 43/43/39/35 | 2 | Not yet generated — requires Phase 2D question generation |
| `bare` | Generated Barrister E | 43/43/39/35 | 3 | Not yet generated |
| `barf` | Generated Barrister F | 43/43/39/35 | 4 | Not yet generated |

**Note:** Exams D, E, F will exclude questions already used in Exam C (via `--exclude` flag on `tools/assemble_exam.py`). Each will require sufficient question bank depth beyond the 185-question Phase 2A/2B baseline.

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
