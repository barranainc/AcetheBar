# Phase 3A QA Log — Browser Behavior Verification

**Date:** 2026-05-26
**Branch:** `feature/phase-3a-analytics`
**Method:** Automated browser testing via Claude Preview (Chromium headless), JS eval in live page context

---

## Environment

- Static server: `python3 -m http.server 8787`
- URL: `http://localhost:8787/`
- localStorage key: `acethebar.analytics.v1`

---

## Check 1 — App Load

**Result: ✅ PASS**

- App loaded at `http://localhost:8787/` with no errors
- "📊 Progress" nav button visible in top-right corner
- `_META` variable loaded: 963 questions, 7 exam position maps
- `ANALY_KEY` defined: `acethebar.analytics.v1`

All 12 exam buttons confirmed present in nav:

| Exam | Label | Questions |
|---|---|---|
| bar   | LSO Barrister A        | 160 |
| sol   | LSO Solicitor A        | 160 |
| mini  | ABP Mini Exam          | 80  |
| abp   | ABP Full Barrister     | 160 |
| bar2  | LSO Barrister B        | 160 |
| barc  | Generated Barrister C  | 160 |
| bard  | Generated Barrister D  | 160 |
| bare  | Generated Barrister E  | 160 |
| barf  | Generated Barrister F  | 160 |
| prdra | Generated PR Drill A   | 100 |
| prdrb | Generated PR Drill B   | 100 |
| prb200| Generated PR Bank 200  | 200 |

---

## Check 2 — Metadata Lookup

**Result: ✅ PASS**

Verified `examPositions` maps real question IDs for barc, barf, prdrb:

| Exam | Position | Resolved ID | Subject |
|---|---|---|---|
| barc | 1 | `civ-02-basic-lim-001` | Civil Litigation |
| barc | 2 | `civ-02-basic-lim-002` | Civil Litigation |
| barf | 1 | `civ-02-ult-lim-001`   | Civil Litigation |
| barf | 5 | `civ-08-aod-form-002`  | Civil Litigation |
| prdrb| 1 | `pr-01-class-lic-001`  | Professional Responsibility |
| prdrb| 3 | `pr-01-ins-001`        | Professional Responsibility |

Full metadata verified for each (sub/ch/cht/top/dif/ref all populated).

**Bug found and fixed:** `questionId` in attempt records was storing `barc:1` instead of `civ-02-basic-lim-001` because `anlRecord` checked for `meta.id` which doesn't exist in the slim metadata schema. Fixed by looking up directly from `examPositions`. See [Bug 1](#bug-1--questionid-stored-exam-key-instead-of-canonical-id).

After fix: `questionId` correctly stores `civ-02-basic-lim-001`, `civ-02-basic-lim-002`, etc.

---

## Check 3 — Attempt Persistence

**Result: ✅ PASS**

- Answered 3 questions on Generated Barrister C (Q1 correct, Q2 wrong, Q3 correct)
- Pre-reload: `{keys: ['barc:1','barc:2','barc:3'], q1_isCorrect: true, q2_isCorrect: false, q1_time: 38, q2_time: 75}`
- Post-reload: **identical** — all keys and values persisted exactly
- `attemptNumber` starts at 0 for first attempt, increments on re-attempt
- `sessionId` links attempts to the active session

---

## Check 4 — Wrong-Answer Review

**Result: ✅ PASS**

- Q2 (answered wrong) identified as wrong in `d.attempts['barc:2'][0].isCorrect === false`
- `anlReviewWrong('barc')` computes `wrongIdxs = [1]` (index of Q2 in the question array)
- `restartExam` + `setTimeout` sets `s2.filteredIdx = [1]`, `s2.cur = 1`
- App's existing `filteredIdx` system (`indexOf`, `.length`, `[np]`) is fully compatible with this array format
- Jump grid button for Q2: class `jb bad flagged` (correct — both wrong and flagged)

---

## Check 5 — Flagged-Question Persistence

**Result: ✅ PASS**

- Flagged Q2: `d.flaggedQuestions['barc:2'] = true` — confirmed saved
- After page reload: `flagPersisted: true`, `flaggedKeys: ['barc:2']`, `anlIsFlagged('barc', 2): true`
- Flag button: shows "⚑ Flagged" with `.flagged` class when question is flagged; reverts to "⚑ Flag" when not
- `anlToggleFlag` toggles correctly: add → remove → add cycle verified
- Jump grid: `q2btn.className = 'jb bad flagged'` — amber outline applied when flagged
- `anlReviewFlagged` computes `flaggedIdxs` from `d.flaggedQuestions` correctly

---

## Check 6 — Session Report

**Result: ✅ PASS**

Session of 5 questions (3 correct, 2 wrong, avg ~61s):

| Field | Present | Correct |
|---|---|---|
| Attempted count | ✅ | 5 (not 7 — history excluded) |
| Correct count   | ✅ | 3 |
| Wrong count     | ✅ | 2 |
| Accuracy %      | ✅ | rendered |
| Avg Time        | ✅ | rendered |
| Subject bars    | ✅ | rendered |
| Slowest questions | ✅ | rendered |
| Recommendations  | ✅ | rendered |

**Session scoping confirmed:** added 2 historical attempts from a different session; report showed 5 (current session only), not 7 (all time). `anlSess.keys` correctly scopes to current session.

---

## Check 7 — Progress Dashboard

**Result: ✅ PASS**

Opened dashboard with 7 total attempts across two sessions:

| Section | Present |
|---|---|
| Total attempts     | ✅ (7) |
| Correct count      | ✅ |
| Wrong count        | ✅ |
| Accuracy %         | ✅ (43%) |
| Avg Time           | ✅ |
| Flagged count      | ✅ |
| Subject accuracy bars | ✅ |
| Weak chapters (< 70%) | ✅ |
| Slow areas (avg > 110s) | ✅ |
| Repeatedly wrong   | ✅ (conditional — only shown when ≥2 wrong attempts exist) |

Dashboard open/close: `display:flex` → `display:none` — works correctly. Clicking backdrop closes overlay (onclick on `.anl-overlay`).

---

## Check 8 — Export / Import / Reset

**Result: ✅ PASS**

| Step | Result |
|---|---|
| Export (JSON serialization) | ✅ |
| Reset (localStorage.removeItem) | ✅ — attempts cleared to 0, flags cleared |
| Import (anlSave with parsed JSON) | ✅ |
| Attempts after import | ✅ 7 (matches pre-reset) |
| Flags after import | ✅ 0 (matches pre-reset) |
| Sessions after import | ✅ 1 (matches pre-reset) |
| Attempt keys match | ✅ exact match |

---

## Check 9 — Imported Exam Limitations

**Result: ✅ DOCUMENTED (expected behavior)**

Tested `bar` (imported LSO Barrister A):

| Capability | Imported (bar) | Generated (barc) |
|---|---|---|
| Attempt tracking | ✅ Works | ✅ Works |
| Appears in reports | ✅ Yes | ✅ Yes |
| Subject (`q.sec`) | ✅ Populated | ✅ Populated |
| Chapter number/title | ❌ Empty | ✅ Populated |
| Topic heading | ❌ Empty | ✅ Populated |
| Difficulty | ❌ Empty | ✅ Populated |
| Statute reference | ❌ Empty | ✅ Populated |
| Subject/chapter recommendations | ❌ Subject only | ✅ Full |
| `examPositions` map | ❌ Not present | ✅ 7 exams mapped |

**Root cause:** Metadata was generated from `data/questions/` source files. Imported payloads (bar, sol, mini, abp, bar2) were assembled externally and their questions are not in `data/questions/`. Analytics can only provide deep metadata for questions that exist in the question bank.

**Impact:** For imported exams, analytics still tracks attempt count, correct/wrong, time, and subject (from `q.sec`). Chapter/topic/difficulty analysis is unavailable.

**This is by design.** No fix is possible without access to the source question data for imported exams.

---

## Check 10 — Console Error Check

**Result: ✅ PASS — zero errors throughout**

Tested across:
- App initial load
- Answering questions (pick, anlRecord)
- Opening Progress Dashboard (anlDashboard)
- Opening Session Report (anlReport)
- Flag toggle (anlToggleFlag)
- Export/import/reset

No JavaScript errors at any point.

---

## Bugs Found

### Bug 1 — `questionId` stored exam key instead of canonical ID

**Severity:** Minor (attempt lookup key `barc:1` was still correct; only the display field was wrong)

**Root cause:** `anlRecord` computed `actualId` by checking `meta.id`, but the slim metadata schema `{sub, ch, cht, top, dif, ref}` has no `id` field. The fallback `examId + ':' + q.id` was always used.

**Fix applied:**
```javascript
// Before (buggy):
var actualId = (meta && meta.id) ? meta.id : (examId + ':' + q.id);

// After (fixed):
var posMap = (anlGetMeta().examPositions || {})[examId] || null;
var actualId = posMap ? (posMap[String(q.id)] || (examId + ':' + q.id)) : (examId + ':' + q.id);
```

**Verification:** After fix, `d.attempts['barc:1'][0].questionId === 'civ-02-basic-lim-001'` ✅

**Files fixed:** `index.html` (line 897), `tools/patch_3a_analytics.py` (matching line in `ANALYTICS_JS` constant)

---

## Known Limitations

1. **Imported exam metadata** — bar, sol, mini, abp, bar2 have no chapter/topic/difficulty metadata. Analytics tracks attempts and subject only.

2. **Visibility timer** — Time pauses when tab is hidden (`visibilitychange`). If user switches away mid-question, that time is excluded. This is intentional behavior to measure active reading time.

3. **`attemptNumber`** — Increments only when the same question is answered again (review mode). First attempt is always `attemptNumber: 0`.

4. **Session report scope** — Shows current active session only. Historical sessions are visible only in the dashboard aggregate view.

---

## Files Modified (Phase 3A QA)

| File | Change |
|---|---|
| `index.html` | Fixed Bug 1: `anlRecord` `actualId` lookup via `examPositions` |
| `tools/patch_3a_analytics.py` | Same fix in `ANALYTICS_JS` source constant |

---

## Validation Results

```
build_question_metadata.py:   963 questions, 0 duplicates, 7 exam maps, 240.3 KB ✅
validate_html.py:             JavaScript OK, payloads intact, all checks pass ✅
validate_question.py:         963 questions, 0 errors, 123 warnings (all accepted) ✅
```

---

## Phase 3A Status

**✅ Phase 3A is ready for use.**

All 10 required checks pass. One bug was found and fixed during QA. No legal content, correct answers, question IDs, manifests, or exam payloads were modified.

**Phase 3B may begin.**
