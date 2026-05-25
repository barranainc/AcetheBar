# Phase 2K-Improve-A — Rewrite Log

**Date:** 2026-05-25  
**Scope:** All REWRITE-status questions identified in the Phase 2K psychometric audit  
**Total rewrites:** 41 questions across 5 subjects  
**Legal flags excluded (untouched):** fam-04-mh-consent-003, fam-08-review-001, fam-08-review-var-001

---

## Summary

| Subject | Questions rewritten | Correct answer changed |
|---|---|---|
| Civil Litigation | 8 | 6 |
| Criminal Law | 9 | 2 (letter renumbering only) |
| Family Law | 6 | 2 |
| Public Law | 10 | 1 (letter renumbering only) |
| Professional Responsibility | 8 | 1 |
| **Total** | **41** | **~12** |

All rewrites: updated `fact_pattern`, `call_of_question`, `options`, `explanation`, `why_A/B/C/D_wrong`, `exam_trigger_words`, `tested_concepts`, `updated_at` = "2026-05-25". `validation_status` left unchanged per instructions.

---

## Civil Litigation (8 questions)

| question_id | file | correct_answer_changed | notes |
|---|---|---|---|
| civ-07-partial-sj-003 | ch07-summary-judgment.json | **Y** (C→A) | Intertwinement/inconsistent-findings risk as decisive Hryniak factor; forces application of partial-SJ discretion, not recall |
| civ-03-strike-001 | ch03-pleadings.json | **Y** (B→D) | Defendant files evidence on r.21.01(1)(b) motion; evidence inadmissible; novel but arguable claim survives; Misapplied Tool distractor (convert to SJ motion) |
| civ-04-exam-001 | ch09-examination-for-discovery.json | N | Reasonable-time standard governs; Wrong Timeline Trap is invented 60-day deadline |
| civ-08-cpa-001 | ch16-class-actions.json | N | CPA s.24(1)(c) aggregate assessment without individual proof; non-identifiability does not bar it; General Rule Trap |
| civ-02-susp-ext-001 | ch02-limitation-periods.json | **Y** (B→C) | Litigation guardian appointed while minor — s.6(2) "earlier of" rule triggers from appointment date, not 18th birthday; Wrong Timeline Trap reverses "earlier of" |
| civ-05-material-001 | ch05-striking-out.json | **Y** (C→A) | Four concrete pleading items across wrongful dismissal scenario; forces material fact / evidence / legal conclusion classification |
| civ-15-noting-002 | ch15-default.json | **Y** (B→C) | Missing affidavit of default and proof of service; three mandatory r.19.01 elements; both noting and judgment defective |
| civ-16-counsel-001 | ch16-class-actions.json | **Y** (B→A) | Class counsel partner holds defendant shares + undisclosed prior referral fee; full disclosure to rep plaintiff, class, and court required before s.29 hearing |

---

## Criminal Law (9 questions)

| question_id | file | correct_answer_changed | notes |
|---|---|---|---|
| crim-04-stinch-001 | ch04-disclosure.json | N | Informer privilege exception to Stinchcombe; scenario rebuilt around Crown resisting production |
| crim-02-sw-issu-001 | ch02-charter-arrest.json | N | s.487.1 telewarrant impracticability trigger; distractors redesigned |
| crim-09-purpose-001 | ch09-sentencing.json | N | Application: identify denunciation from specific judicial reasoning; reparations/separation traps added |
| crim-10-ycja-def-001 | ch10-ycja.json | N | Borderline scenario straddling 12th birthday; charge-by-charge age assessment under s.2(1) |
| crim-11-sum-app-001 | ch11-appeals.json | N | s.839 further appeal from Superior Court; leave vs. as-of-right distinction added |
| crim-03-surety-001 | ch03-bail.json | N (B→C renumber) | Ambiguous circumstances — actual knowledge of breach, reluctant surety; s.764(3) surrender right |
| crim-04-timing-001 | ch04-disclosure.json | N | Continuing duty scenario — newly obtained evidence disclosed 2 days before election; adjournment remedy |
| crim-05-plea-barg-001 | ch05-pre-trial.json | N (B→C renumber) | Counsel agreeing to adverse facts without client instruction; pr_angle set to true |
| crim-11-sum-sent-001 | ch11-appeals.json | N (C→B renumber) | Post-appeal-window; s.732(2) intermittent sentence variation; certiorari/late-appeal distractors |

---

## Family Law (6 questions)

| question_id | file | correct_answer_changed | notes |
|---|---|---|---|
| fam-03-deduct-marr-001 | ch03-nfp.json | N (B→C renumber) | Contested traceability dispute — commingled $120k investment; traceability analysis governs deduction |
| fam-06-cs-table-001 | ch06-child-support.json | N | Adult child (age 20, university) s.3(2)(b) scenario; appropriateness assessment required, not automatic table |
| fam-07-parplan-001 | ch07-parenting.json | N (B→C renumber) | Enforcement: incorporated parenting plan; DA s.16.2(4) — incorporated terms have order effect |
| fam-06-tax-001 | ch06-child-support.json | N | Commencement day: 1995 order varied in 2022 converts all payments to tax-neutral; Wrong Timeline/Misapplied Tool traps |
| fam-02-divorce-bar-002 | ch02-divorce.json | **Y** (B→C) | Fully rewritten: collusion vs condonation (DA s.11); condonation bars only adultery/cruelty grounds; DA s.11(4) excludes cooperation from collusion |
| fam-02-jurisdiction-001 | ch02-divorce.json | N | Exact-one-year simultaneous filing in two provinces; DA s.3(2) concurrent jurisdiction mechanism; no race-to-file rule |

---

## Public Law (10 questions)

| question_id | file | correct_answer_changed | notes |
|---|---|---|---|
| pub-02-oakes-test-001 | ch02-charter.json | N | Burden-shifting misconception scenario; government bears full Oakes burden throughout |
| pub-02-oakes-test-005 | ch02-charter.json | N | Failed minimal impairment → s.52(1) invalidity; reading down vs. striking down remedial choice |
| pub-03-baker-fair-001 | ch03-admin-law.json | N | Factor 1 vs Factor 3 tension + Factor 2 (no appeal right); holistic balancing conclusion |
| pub-04-correct-std-004 | ch04-judicial-review.json | N | WSIT/HRTO competing jurisdiction — Vavilov inter-tribunal correctness category |
| pub-04-div-court-001 | ch04-judicial-review.json | N (C→B renumber) | Multi-element: Divisional Court + leave + 30-day JRPA limit + certiorari/mandamus |
| pub-04-delay-001 | ch04-judicial-review.json | N | JRPA 30-day default vs enabling statute 60-day specific limit; specific displaces general |
| pub-05-sppa-app-001 | ch05-sppa.json | N | "may" vs "shall" hearing threshold; SPPA s.3(1) application distinction |
| pub-05-sppa-sub-001 | ch05-sppa.json | N | Contested relevance — 40,000 patients vs 3 named; "relevant to subject matter" limit on s.12 |
| pub-01-pith-001 | ch01-division-of-powers.json | N | Federal food packaging safety statute; s.91(27) vs s.91(2) vs s.92(13) characterization applied |
| pub-07-charter-dam-002 | ch07-crown-liability.json | N | Systemic strip-search policy; good faith/deterrence tension; Ward three-step; false alternative-remedy bar |

---

## Professional Responsibility (8 questions)

| question_id | file | correct_answer_changed | notes |
|---|---|---|---|
| pr-02-specialist-001 | ch02-competence.json | N | "Certified specialist" marketing + elevated standard of care; misleading advertising under Rule 4.2-1 |
| pr-03-govt-001 | ch03-confidentiality.json | **Y** (C content changed) | Ministry of Finance audit demand for Ministry of Health file; identity-of-client analysis; must seek Crown law officer direction |
| pr-04-wit-001 | ch04-conflicts.json | N | Contract-signing witness + 3-day trial + client consent trap (Ethics Override) + hardship exception analysis |
| pr-05-split-002 | ch05-duties.json | N | Thank-you payment to paralegal referrer; Rule 3.6-6 three conditions; Pragmatic Bluff + Overstatement traps |
| pr-06-short-003 | ch06-trust.json | N | Disputed trust funds on failed real estate closing; interpleader obligation; prohibition on unilateral disbursement |
| pr-08-unrp-002 | ch08-opposing.json | N | Limitation period question to self-represented plaintiff; information/advice line; Ethics Override Trap (direct question does not unlock advice) |
| pr-10-trust-cond-001 | ch10-undertakings.json | N | Client instructs use of document beyond trust condition scope; Ethics Override Trap; Wrong Forum + Pragmatic Bluff distractors |
| pr-13-solicit-001 | ch13-marketing.json | N | Nurse-provided contact + disaster victim; back-channel solicitation; client consent does not retroactively cure prohibited initiation |

---

## Payload Rebuild

All 7 generated exam payloads were rebuilt from existing manifest `question_ids_used` (no re-selection).

| Exam key | Old b64 length | New b64 length | Delta |
|---|---|---|---|
| barc | 381,984 | 393,248 | +11,264 |
| bard | 432,256 | 441,852 | +9,596 |
| bare | 468,144 | 483,992 | +15,848 |
| barf | 497,876 | 501,116 | +3,240 |
| prdra | 289,064 | 293,132 | +4,068 |
| prdrb | 285,404 | 288,532 | +3,128 |
| prb200 | 574,612 | 581,808 | +7,196 |

Imported exams unchanged: bar=191,500, sol=242,816, mini=171,132, abp=189,540, bar2=237,360.

Integrity checks passed:
- C+D+E+F = 640 unique IDs, zero overlap ✅
- PR Drill A∩B = 0, A∪B = Bank200 ✅
- `python3 tools/validate_question.py data/questions --summary` — 963 questions, 0 errors ✅
- `python3 tools/validate_html.py` — all checks pass ✅
