# Phase 3A — Analytics, Attempt Tracking & Progress Dashboard Log

**Completed:** 2026-05-26
**Branch:** `feature/phase-3a-analytics`

---

## Summary

Phase 3A added a complete analytics system to the static HTML app using browser `localStorage` only. No backend, no external services. The app continues to work on static hosting without any server-side changes.

**Storage key:** `acethebar.analytics.v1`

---

## Files Created

| File | Purpose |
|---|---|
| `tools/build_question_metadata.py` | Scans all 963 question files, extracts slim per-question metadata, builds exam position maps |
| `data/analytics/question_metadata.json` | Output metadata (963 questions, 7 exam position maps, 1040 total positions) |
| `tools/patch_3a_analytics.py` | Injects analytics CSS, modals, JS module, and function patches into index.html |

## Files Modified

| File | Change |
|---|---|
| `index.html` | Added `var _META`, analytics CSS, modal HTML, analytics JS module, 6 function patches, nav button IIFE |

**No question files, manifests, or imported payloads were modified.**

---

## Metadata Format

`data/analytics/question_metadata.json` (240.3 KB raw, 320.4 KB base64):

```json
{
  "version": 1,
  "questions": {
    "civ-02-basic-lim-001": {
      "sub": "Civil Litigation",
      "ch": 2,
      "cht": "Limitation Periods",
      "top": "The Basic Two-Year Limitation Period",
      "dif": "easy",
      "ref": "Limitations Act, 2002, S.O. 2002, c. 24, Sched. B, s. 4"
    }
  },
  "examPositions": {
    "barc": {"1": "civ-02-basic-lim-001", "2": "...", ...},
    "bard": {...}, "bare": {...}, "barf": {...},
    "prdra": {...}, "prdrb": {...}, "prb200": {...}
  }
}
```

Fields: `sub` (subject), `ch` (chapter number), `cht` (chapter title), `top` (topic heading, ≤60 chars), `dif` (difficulty), `ref` (statute reference, ≤80 chars).

Imported exams (bar, sol, mini, abp, bar2) have **no** examPositions entries — analytics uses only `q.sec` (section name) for these exams.

---

## Analytics Data Schema (localStorage)

```json
{
  "attempts": {
    "barc:1": [
      {
        "questionId": "civ-02-basic-lim-001",
        "examKey": "barc",
        "examLabel": "Barrister C",
        "subject": "Civil Litigation",
        "chapterNumber": 2,
        "chapterTitle": "Limitation Periods",
        "topicHeading": "The Basic Two-Year Limitation Period",
        "startedAt": "2026-05-26T10:00:00.000Z",
        "answeredAt": "2026-05-26T10:01:30.000Z",
        "timeSeconds": 90,
        "selectedAnswer": "B",
        "correctAnswer": "B",
        "isCorrect": true,
        "difficulty": "easy",
        "attemptNumber": 0,
        "sessionId": "sess_1748260800000"
      }
    ]
  },
  "sessions": [
    {
      "id": "sess_1748260800000",
      "examKey": "barc",
      "startedAt": "2026-05-26T10:00:00.000Z",
      "endedAt": "2026-05-26T11:30:00.000Z",
      "keys": ["barc:1", "barc:2", ...]
    }
  ],
  "flaggedQuestions": {
    "barc:42": true
  }
}
```

---

## Features Added

### Attempt Recording
- Every answer triggers `anlRecord()` via patched `pick()` function
- Stores full attempt: exam, question, subject, chapter, topic, time, selected/correct answer, difficulty, session ID
- Time accumulates only while tab is visible (`visibilitychange` listener pauses timer when tab is hidden)
- Multiple attempts per question are stored as an array (full history preserved)

### Flag for Review
- "⚑ Flag" button added to each question panel via patched `buildPanel()`
- `anlToggleFlag()` toggles flagged state; button updates to "⚑ Flagged" (amber) when active
- Jump-grid buttons get `flagged` class (amber outline) for visual indicator
- Flagged state persists in localStorage across sessions

### Session Tracking
- Session starts when exam begins (`anlStartSession()` in patched `startExam()`)
- Session ends when "Finish & Review" is clicked (`anlEndSession()` in patched `finishExam()`)
- Session record stored in `sessions[]` array with exam key, timestamps, and question keys answered

### Post-Exam Buttons (after finishing)
Three buttons appear after "Finish & Review":
- **📋 Session Report** — opens Session Report modal for current exam
- **🔁 Review Wrong** — restarts exam filtered to wrong questions only
- **⚑ Review Flagged** — restarts exam filtered to flagged questions only

### Progress Dashboard (`📊 Progress` nav button)
Opens a modal with:
- **Overall stats:** total attempts, correct, wrong, accuracy %, avg time, flagged count
- **Subject accuracy bars** — colour-coded (green ≥70%, amber ≥50%, red <50%)
- **Weak chapters** — chapters below 70% accuracy with ≥2 attempts, sorted worst-first
- **Slow areas** — subjects with avg answer time >110s
- **Repeatedly wrong** — questions answered wrong ≥2 times in a row

### Session Report
Per-exam modal showing:
- Stats for the current session (or all attempts if no active session)
- Subject accuracy bars
- Slowest 5 questions
- Likely guessing (wrong in <45s)
- Recommendations (low-accuracy subjects, slow pace, guessing pattern, weak topics)

### Export / Import / Reset
- **Export** — downloads `acethebar-progress-YYYY-MM-DD.json`
- **Import** — loads a previously exported JSON file, merging into dashboard
- **Reset** — clears all localStorage data after confirmation

---

## Function Patches Applied

| Function | Patch | Purpose |
|---|---|---|
| `pick()` | After `s.answers[s.cur] = idx` | Call `anlRecord()` to store attempt |
| `buildJump()` | Before `b.className=cls2` | Add `flagged` class to jump buttons |
| `startExam()` | After `s.started = true` | Call `anlStartSession()` |
| `finishExam()` | Before `s.finished=true` | Call `anlEndSession()` |
| `finishExam()` | After result `forEach` | Inject post-exam action buttons |
| `renderQ()` | After `buildJump()` | Update flag button text and class |
| `buildPanel()` | Before "Finish & Review" button | Add "⚑ Flag" button |

---

## Payload Integrity Verification

All exam payloads verified unchanged (b64 character lengths):

| Payload | Type | b64 len |
|---|---|---|
| bar | imported | 191,500 |
| bar2 | imported | 237,360 |
| sol | imported | 242,816 |
| mini | imported | 171,132 |
| abp | imported | 189,540 |
| barc | generated | 417,840 |
| bard | generated | 456,836 |
| bare | generated | 537,976 |
| barf | generated | 517,940 |
| prdra | generated | 303,232 |
| prdrb | generated | 296,996 |
| prb200 | generated | 600,372 |

---

## Validation Results

```
HTML validation:      ✅ passes all checks
Question validator:   963 questions, 0 errors, 123 warnings (all accepted — same as Phase 2W)
Payload integrity:    ✅ all 12 payloads intact
Manifests:            ✅ unchanged
Question files:       ✅ unchanged
```

---

## Constraints Respected

- ✅ localStorage only — no backend, no external services
- ✅ Storage key: `acethebar.analytics.v1`
- ✅ Imported payloads untouched: bar, sol, mini, abp, bar2
- ✅ Generated payloads untouched: barc, bard, bare, barf, prdra, prdrb, prb200
- ✅ No question IDs changed
- ✅ No correct answers changed
- ✅ No manifests changed
- ✅ No re-randomization
- ✅ No outside law used
- ✅ No web browsing
- ✅ ES5 JavaScript (var, function declarations) to match existing codebase
- ✅ Metadata embedded as separate `var _META` — does not modify any exam payload
- ✅ Static hosting compatible
