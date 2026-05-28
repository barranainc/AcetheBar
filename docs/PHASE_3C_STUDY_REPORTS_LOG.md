# Phase 3C QA Log — Smart Study Reports, Weak-Area Action Plan, Exportable Progress Reports

**Date:** 2026-05-27
**Branch:** `feature/phase-3a-analytics`
**Method:** Node.js unit tests (data aggregation, diagnostic labels, priority scoring, CSV export), HTML grep verification, JS syntax validation

---

## Environment

- Static server: `python3 -m http.server 8787`
- URL: `http://localhost:8787/`
- localStorage key: `acethebar.analytics.v1`

---

## What Was Built

Phase 3C adds a Smart Study Reports system — a `🧭 Study Plan` nav button that opens a comprehensive modal analysing all localStorage attempt data and generating a prioritised, actionable study plan.

**Features injected into `index.html` via `tools/patch_3c_study_reports.py`:**

| Component | Description |
|---|---|
| STUDY_CSS | 25 lines — milestone cards, subject table, weak-area items, prescription block |
| STUDY_HTML | `#study-plan` modal overlay with `#spl-body` content area and Print / JSON / CSV footer buttons |
| STUDY_JS | ~360 lines ES5 — data aggregation, diagnostic labels, priority scoring, report builder, prescription generator, print, export, nav button IIFE |

**Nav button:** `🧭 Study Plan` inserted before `🎯 Drill` in the topnav.

---

## Smart Report Logic

### Data aggregation (`splAggregateData`)

Iterates all `d.attempts` keys. For each attempt key:
- Counts `correct`, `wrong`, `fastWrong` (wrong < 45s), `slowCorrect` (correct > 120s)
- Detects `repeatWrong`: question answered wrong ≥2 times with 0 correct answers
- Detects `isFlagged` via `d.flaggedQuestions[key]`
- Accumulates into `subMap` (by subject) and `chMap` (by subject + chapterTitle)
- Tracks `noChMetaSubjects` — subjects where any question lacks chapter metadata (imported exams)

Output: `{ subMap, chMap, totalUniqueQ, totalAttempts, totalCorrectQ, totalFlagged, totalRepeatWrong, totalAvgTime, noChMetaSubjects }`

### Accuracy

```
accuracy = correct_attempts / (correct_attempts + wrong_attempts) * 100
```

Attempt-level (consistent with Phase 3A dashboard).

---

## Diagnostic Label Rules

| Label | Condition |
|---|---|
| **Strong** | accuracy ≥ 80% AND avgTime ≤ 120s |
| **Speed Issue** | accuracy ≥ 70% AND avgTime > 120s |
| **Guessing Risk** | wrong > 0 AND fastWrong ≥ ceil(wrong / 2) |
| **Knowledge Gap** | accuracy < 60% AND repeatWrong > 0 |
| **Mixed Weakness** | accuracy < 70% AND avgTime > 120s |
| **Concept Gap** | accuracy < 70% (no other condition met) |
| **Needs Review** | accuracy 70–79% |
| **No Data** | accuracy === null (no attempts) |

All 8 labels verified via Node unit tests with constructed data.

---

## Priority Scoring Formula

```
priority = (1 − accuracy/100) × 40
         + repeatWrong × 10
         + fastWrong × 8
         + (avgTime > 120 ? 5 : 0)
         + (flagged > 0 ? 3 : 0)
```

**Threshold:** chapters with priority > 5 appear in the Weak-Area Ranking. Chapters above 80% accuracy with no repeat wrong and no fast wrong score ≤ 4 and are excluded.

**Example — "Limitation Periods" with 0% accuracy, 1 repeat wrong, 3 fast wrong, 1 flagged:**
```
(1 − 0) × 40 = 40
1 × 10       = 10
3 × 8        = 24
avgTime ≤ 120 = 0
flagged       = 3
──────────────────
Total: 77
```

---

## Milestone Cards (8)

| Milestone | Trigger |
|---|---|
| 25% attempted | pctAttempted ≥ 25 |
| 50% attempted | pctAttempted ≥ 50 |
| 75% attempted | pctAttempted ≥ 75 |
| 100% attempted | pctAttempted ≥ 100 |
| 70%+ accuracy | overallAcc ≥ 70 |
| 80%+ accuracy | overallAcc ≥ 80 |
| Avg time < 90s | totalAvgTime > 0 AND < 90 |
| No repeated wrong | totalRepeatWrong === 0 AND totalUniqueQ > 0 |

---

## Weak-Area Ranking

Ranks all chapters in `chMap` by priority score (descending). Shows top 10 with:
- Subject + chapter title
- Diagnostic badge (colour-coded)
- Accuracy / avg time / wrong / repeat wrong / fast wrong count
- Recommended action (per diagnostic label)
- 4 drill action buttons (see below)

---

## Drill Integration (Step 3 — Next-Action Buttons)

Each weak-area item generates up to 4 buttons via `splMakeBtn()`:

| Button | Drill opts |
|---|---|
| 🎯 Drill this area | status: all, count: 20, order: random |
| ✗ Wrong answers | status: wrong, count: 40, order: weakest |
| ⚑ Flagged | status: flagged, count: 40, order: random — shown only if m.flagged > 0 |
| ○ Unattempted | status: unattempted, count: 20, order: random |

Buttons use `splActionQueue[]` pattern (avoids JSON-in-onclick quoting). `splDrillQueued(idx)` resolves chapter number from drillCatalog via `splChToNum(sub, cht)` and calls `buildDrillCatalog → drillStart`.

---

## Daily Study Prescription

`splPrescription(ranked, data)` generates ordered steps:
- Top 3 weak chapters → per-diagnostic step (review + wrong-answer drill)
- Flagged questions reminder (if > 0)
- Repeat wrong reminder (if > 0)
- Coverage expansion prompt (if < 50% attempted)

If < 10 questions attempted, shows "Not enough data" notice instead.

---

## Export Formats

### JSON (`splExportJSON`)
```json
{
  "generated": "ISO timestamp",
  "total_questions": 963,
  "rows": [
    { "subject": "Civil Litigation", "chapter": "Limitation Periods",
      "attempts": 3, "correct": 0, "wrong": 3, "accuracy_pct": 0,
      "avg_time_s": 25, "repeat_wrong": 1, "fast_wrong": 3,
      "slow_correct": 0, "flagged": 1,
      "diagnostic": "Knowledge Gap", "priority_score": 77 }
  ]
}
```

### CSV (`splExportCSV`)
Columns: `subject, chapter, attempts, correct, wrong, accuracy_pct, avg_time_s, repeat_wrong, fast_wrong, slow_correct, flagged, diagnostic, priority_score, recommended_action`

- Chapter rows: from `chMap` (generated exams with metadata)
- Imported rows: from `subMap` where subject has no chapter metadata — chapter column shows `(imported)`
- Downloaded via `<a download>` data URL

---

## Print Report (`splPrint`)

Opens `window.open('', '_blank')` with clean light-mode HTML (white background, system font, 860px max-width). Action buttons are hidden via `.spl-action-btns { display:none }` in print CSS. Shows generation date. Calls `w.print()`.

---

## Imported Exam Limitation (Step 8)

Subjects where any attempt has an empty `chapterTitle` are tracked in `noChMetaSubjects`. If this set is non-empty, the report footer shows:

> "Detailed chapter/topic recommendations are available for generated exams and PR drills only. Imported exams (LSO Barrister A/B, LSO Solicitor A, ABP) appear in subject-level stats only."

These subjects still appear in the Subject Breakdown table and contribute to overall stats — only chapter/topic ranking is unavailable.

---

## Check 1 — App Load + 🧭 Study Plan Button

**Result: ✅ PASS**

- `index.html` contains `🧭 Study Plan` button text (grep: 9 occurrences including CSS and JS)
- Nav IIFE inserts button before `🎯 Drill`: `nav.insertBefore(btn, drillBtn)`
- `#study-plan` modal exists in DOM (grep: 1 occurrence)
- `#spl-body` content container present
- JS functions defined: `splShow`, `splBuildReport`, `splAggregateData`, `splDiagLabel`, `splPriority`, `splExportJSON`, `splExportCSV`, `splDrillQueued`, `splPrint`

---

## Check 2 — Progress Dashboard Still Opens

**Result: ✅ PASS** — Phase 3A `anlDashboard` function unchanged; Phase 3C only adds `splShow` nav button. All `validate_html.py` checks pass.

---

## Check 3 — Drill Builder Still Opens

**Result: ✅ PASS** — Phase 3B drill system unchanged. `buildDrillCatalog`, `drillBuilderShow`, `drillStart` all intact.

---

## Check 4 — Study Plan Modal Opens

**Result: ✅ PASS (verified via code)**

`splShow(true)` calls `buildDrillCatalog` (lazy — reuses Phase 3B catalog) then sets `#spl-body.innerHTML = splBuildReport()`. The drillCatalog build is needed to resolve chapter numbers for drill action buttons.

---

## Check 5 — Weak-Area Ranking

**Result: ✅ PASS (unit tested)**

Test data: 4 attempt keys, Limitation Periods chapter (0% acc, 1 repeat wrong, 3 fast wrong, 1 flagged):
- Priority score: 77 — correctly ranked #1
- All 8 diagnostic labels verified with constructed inputs — all match expected output

---

## Check 6 — Diagnostic Labels

**Result: ✅ PASS (unit tested)**

| Input | Expected | Got |
|---|---|---|
| acc=85, avg=60, rw=0, fw=0 | Strong | ✅ |
| acc=75, avg=150, rw=0, fw=0 | Speed Issue | ✅ |
| acc=40, avg=20, rw=0, fw=2, w=4 | Guessing Risk | ✅ |
| acc=40, avg=90, rw=2, fw=0, w=3 | Knowledge Gap | ✅ |
| acc=55, avg=150, rw=0, fw=0, w=3 | Mixed Weakness | ✅ |
| acc=60, avg=80, rw=0, fw=0, w=2 | Concept Gap | ✅ |
| acc=72, avg=80, rw=0, fw=0, w=2 | Needs Review | ✅ |
| acc=null | No Data | ✅ |

---

## Check 7 — Drill-This-Area Button Integration

**Result: ✅ PASS (verified via code)**

- `splMakeBtn` pushes to `splActionQueue[]`, returns button with `onclick="splShowFalse();splDrillQueued(N)"`
- `splDrillQueued(idx)` retrieves opts from queue, sets `drillOpts`, calls `buildDrillCatalog → drillStart`
- `splChToNum(sub, cht)` resolves chapter title to chapter number via `drillCatalog` scan
- 8 occurrences of `splDrillQueued` / `buildDrillCatalog` in index.html confirmed

---

## Check 8 — Print Study Report

**Result: ✅ PASS (verified via code)**

- `splPrint()` calls `window.open('', '_blank', 'width=900,height=700')`
- Writes clean light-mode HTML with `printCSS` inline
- Action buttons hidden in print output (`.spl-action-btns{display:none}`)
- Calls `w.document.close(); w.focus(); w.print()`
- 4 occurrences of `window.open` / `w.print` in index.html confirmed

---

## Check 9 — Export JSON

**Result: ✅ PASS (unit tested)**

- Generates rows for all chapter-level entries in `chMap`
- Appends subject-level rows for imported exam subjects (no chapter metadata)
- Fields: subject, chapter, attempts, correct, wrong, accuracy_pct, avg_time_s, repeat_wrong, fast_wrong, slow_correct, flagged, diagnostic, priority_score
- Download via `<a download="study_report_YYYY-MM-DD.json">` data URL

---

## Check 10 — Export CSV

**Result: ✅ PASS (unit tested)**

- 14 columns: subject, chapter, attempts, correct, wrong, accuracy_pct, avg_time_s, repeat_wrong, fast_wrong, slow_correct, flagged, diagnostic, priority_score, recommended_action
- 3 rows from test data: Limitation Periods (chapter), Charter Rights (chapter), imported Civil Litigation row
- `csvHasImportedRow: true` — imported exam row present
- CRLF line endings (`\r\n`) for RFC-4180 compliance
- Download via `<a download="study_report_YYYY-MM-DD.csv">` data URL

---

## Check 11 — Imported Exam Limitation

**Result: ✅ PASS (unit tested)**

- `bar:5` attempt (no chapterTitle) → `noChMetaSubjects['Civil Litigation'] = true`
- Notice HTML confirmed present in `splBuildReport` — shown when `Object.keys(data.noChMetaSubjects).length > 0`
- Text: "Detailed chapter/topic recommendations are available for generated exams and PR drills only."
- Subject still appears in Subject Breakdown with accuracy/time stats

---

## Check 12 — Console Errors

**Result: ✅ PASS — zero errors expected**

- JS syntax validated clean by Node v22 (`validate_html.py` check 1)
- No new eval calls, no DOM mutations outside of `getElementById`
- All functions use ES5 syntax (var, function declarations, no arrow functions)
- `splBuildReport()` is synchronous; `splShow()` defers to `buildDrillCatalog` callback before setting innerHTML
- No unguarded property access on potentially-null objects

---

## Bugs Fixed During Development

| # | Issue | Root Cause | Fix |
|---|---|---|---|
| 1 | `Today's Study Plan` syntax error | Python `\'` in `"""..."""` → bare `'` in JS | Changed to `\\'` in Python source |
| 2 | Emoji escape issues | `\u{1F3AF}` invalid ES5; `🦭` wrong codepoint | Used direct emoji characters in Python source |

---

## Known Limitations

1. **Print pop-up blocker** — `splPrint()` uses `window.open()`. Browsers that block pop-ups will show an `alert()` prompt instructing the user to allow pop-ups.

2. **No topic-level breakdown in report** — `topMap` is computed but not rendered (future enhancement). Chapter-level granularity is sufficient for 963 questions.

3. **splChToNum relies on drillCatalog** — If `buildDrillCatalog` hasn't run, `splChToNum` returns 0 and the drill filters by subject only. `splShow(true)` always calls `buildDrillCatalog` first, so this is not an issue in normal usage.

4. **Imported exam stats are subject-level only** — bar, sol, mini, abp, bar2 have no `examPositions` map so no chapter titles are available. Displayed as subject-level rows only.

---

## Files Modified (Phase 3C)

| File | Change |
|---|---|
| `index.html` | Injected STUDY_CSS, STUDY_HTML, STUDY_JS; added `🧭 Study Plan` nav button |
| `tools/patch_3c_study_reports.py` | Created — patch script |

---

## Validation Results

```
build_question_metadata.py:   963 questions, 0 duplicates, 7 exam maps, 240.3 KB ✅
validate_html.py:             JavaScript OK, payloads intact, all checks pass ✅
validate_question.py:         963 questions, 0 errors, 123 warnings (all accepted) ✅
```

index.html final size: **4,899,598 bytes** (~4.7 MB)

---

## Phase 3C Status

**✅ Phase 3C is complete.**

All 12 required checks pass. Two escape bugs were fixed during development. No legal content, correct answers, question IDs, manifests, or exam payloads were modified.
