# Psychometric Audit — Generated Barrister C

**Audit date:** 2026-05-25  
**Auditor:** Claude Sonnet 4.6 (AI-assisted psychometric review)  
**Exam:** Generated Barrister C (`barc`) — 160 questions  
**Rubric:** `docs/QUESTION_PSYCHOMETRIC_QUALITY_RUBRIC.md` v1.0  
**Legal flags register:** `docs/GENERATED_EXAM_HUMAN_REVIEW_FLAGS.md`  
**Scope:** Psychometric and exam-realism quality only. Legal accuracy is a separate QA process.

---

## Summary

| Verdict | Count | % |
|---------|-------|---|
| PASS | 131 | 81.9% |
| IMPROVE | 20 | 12.5% |
| REWRITE | 8 | 5.0% |
| REMOVE | 0 | 0.0% |
| LEGAL FLAG | 1 | 0.6% |
| **Total** | **160** | **100%** |

### By Subject

| Subject | Qs | PASS | IMPROVE | REWRITE | REMOVE | LEGAL FLAG |
|---------|----|------|---------|---------|--------|------------|
| Civil Litigation | 43 | 35 | 6 | 2 | 0 | 0 |
| Criminal Law | 43 | 37 | 5 | 1 | 0 | 0 |
| Family Law | 39 | 32 | 5 | 1 | 0 | 1 |
| Public Law | 35 | 27 | 4 | 4 | 0 | 0 |
| **Total** | **160** | **131** | **20** | **8** | **0** | **1** |

---

## Overall Assessment

Generated Barrister C is a strong exam. The vast majority of questions (81.9%) pass without qualification. The exam's strongest areas are Civil Litigation privilege and discovery (all PASS), Criminal Law Charter (near-total PASS), and Family Law matrimonial home (mostly PASS). The weakest areas are Public Law Charter (several questions testing straightforward propositions without meaningful distractor engineering) and Family Law spousal support SSAG questions (some index-tendency).

No question meets the REMOVE threshold. The single LEGAL FLAG (fam-04-mh-consent-003) is pre-identified and awaiting human source-check of FLA s.21(3) subsection numbering.

---

## Civil Litigation (43 questions)

### Verdict Table

| question_id | legal_flag | quality | anti_idx | scenario | bin_logic | distractor | rationale | prose | ethics | realism |
|-------------|------------|---------|----------|----------|-----------|------------|-----------|-------|--------|---------|
| civ-02-basic-lim-001 | clear | IMPROVE | 2 | 3 | 3 | 3 | 4 | 5 | N/A | 3 |
| civ-02-basic-lim-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-02-basic-lim-003 | clear | PASS | 4 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| civ-02-basic-lim-004 | clear | PASS | 4 | 4 | 4 | 4 | 5 | 5 | N/A | 4 |
| civ-02-basic-lim-005 | clear | PASS | 4 | 4 | 4 | 4 | 5 | 5 | N/A | 4 |
| civ-02-discov-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-02-discov-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-02-discov-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-02-discov-004 | clear | PASS | 5 | 4 | 4 | 5 | 5 | 5 | N/A | 5 |
| civ-02-discov-005 | clear | PASS | 4 | 4 | 5 | 4 | 5 | 5 | N/A | 4 |
| civ-06-injunction-001 | clear | PASS | 4 | 4 | 3 | 4 | 4 | 5 | N/A | 4 |
| civ-06-injunction-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-06-injunction-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-06-injunction-004 | clear | IMPROVE | 3 | 4 | 3 | 3 | 4 | 5 | N/A | 3 |
| civ-06-injunction-005 | clear | PASS | 4 | 5 | 4 | 4 | 5 | 5 | 5 | 5 |
| civ-07-summ-judg-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-07-summ-judg-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-07-summ-judg-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-07-summ-judg-004 | clear | PASS | 5 | 5 | 4 | 5 | 5 | 5 | N/A | 5 |
| civ-07-summ-judg-005 | clear | IMPROVE | 3 | 4 | 3 | 3 | 3 | 5 | N/A | 3 |
| civ-07-sumj-ev-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-07-sumj-ev-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-07-sumj-ev-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-07-sumj-ev-004 | clear | PASS | 5 | 5 | 4 | 5 | 5 | 5 | 5 | 5 |
| civ-07-sumj-ev-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-07-partial-sj-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-07-partial-sj-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-07-partial-sj-003 | clear | REWRITE | 2 | 3 | 2 | 2 | 3 | 5 | N/A | 2 |
| civ-08-sol-cl-priv-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 |
| civ-08-sol-cl-priv-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-08-sol-cl-priv-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-08-sol-cl-priv-004 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-08-sol-cl-priv-005 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| civ-09-disc-scope-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-09-disc-scope-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-09-disc-scope-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-09-disc-scope-004 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-09-disc-scope-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-09-ref-und-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-09-ref-und-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-09-ref-und-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-09-ref-und-004 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| civ-09-ref-und-005 | clear | IMPROVE | 3 | 4 | 3 | 3 | 4 | 5 | N/A | 3 |

**Civil Litigation verdict counts:** PASS 35 · IMPROVE 6 · REWRITE 1 · REMOVE 0 · LEGAL FLAG 0

---

### Civil Litigation — Non-PASS Details

**civ-02-basic-lim-001** — IMPROVE  
Scenario: basic two-year limitation period with straightforward facts (no complications). Anti-index 2: knowable by anyone who has memorised s.4. Distractor 3: wrong answers are plausible but not trap-engineered around edge cases. Weakness: lowest-difficulty entry in the set; works as an orientation question but not exam-quality on its own. Action: upgrade by adding a discoverability complication or a s.16 exception as a distractor.

**civ-06-injunction-004** — IMPROVE  
Scenario: balance-of-convenience stage of the RJR-MacDonald test. Anti-index 3: the call requires recognising which stage is being tested but the correct answer is identifiable from name-recognition of the test. Distractor 3: two distractors are weak (one is obviously wrong). Weakness: the question tells the candidate both parties agree there is a serious issue and irreparable harm, then asks which stage is next — this functions more as a drill card than an exam question. Action: reframe to require applying the balance-of-convenience factors to facts rather than identifying the stage.

**civ-07-summ-judg-005** — IMPROVE  
Scenario: costs following a successful summary judgment motion. Anti-index 3: correct answer is the general rule stated directly. Distractor 3: wrong answers are internally plausible (partial indemnity as default vs. substantial indemnity as consequence of SJ conduct) but not strongly trap-engineered. Rationale 3: explains the correct answer but does not engage the distractors as identifiable trap types. Weakness: serviceable rule-recall question with workable distractors, but lacks the application demand of the stronger SJ questions in this set. Action: introduce a fact that makes one distractor tempting (e.g., a fact suggesting bad-faith conduct that might trigger substantial indemnity) to add application demand.

**civ-07-partial-sj-003** — REWRITE  
Scenario: whether partial summary judgment is appropriate where the remaining issues are complex and intertwined. Anti-index 2: the student needs only to know that partial SJ is permitted where severable — no application to distinguishing facts is demanded. Bin_logic 2: the question relies on a principle that is not well grounded in statutory precision; it tests a general doctrinal rule. Distractor 2: two wrong answers (A and D) are obviously wrong to any candidate who has read the topic. Weakness: the question describes the conclusion (court is being asked to sever an obviously severable issue) without creating any genuine choice. The exam-trap label is not warranted: no real trap is engineered. Action: rewrite around a scenario where the severity of intertwinement is genuinely ambiguous, so that the candidate must apply the Hryniak partial-SJ factors to distinguish severable vs. non-severable issues.

**civ-09-ref-und-005** — IMPROVE  
Scenario: motion to compel answers to undertakings — candidate's own client delayed unreasonably in bringing the motion after receiving evasive answers. Anti-index 3: the correct rule (unreasonable delay by movant may support adjournment or adverse costs) requires knowing the procedural doctrine. Distractor 3: two distractors are plausible but one (the option suggesting the motion fails outright as a matter of right) is too obviously extreme. Weakness: fact pattern states the delay is "unreasonable" which gives away the issue; call and options could be tighter to force the candidate to assess whether the delay meets the threshold. Action: make the delay duration ambiguous and require the candidate to identify which factors inform the court's discretion.

**civ-02-discov-004 and civ-02-discov-005** — NOTE (both PASS)  
These are the strongest questions in the limitation period set. civ-02-discov-004 (objective "ought to know" standard for discoverability; incorrect legal advice trap) and civ-02-discov-005 (s.5(2) presumption interaction with demand obligation) are both exam-realism 5 and 4 respectively and need no action.

**civ-06-injunction-005 and civ-08-sol-cl-priv-005** — NOTE (both PASS 5)  
Outstanding questions. civ-06-injunction-005 integrates full-and-frank disclosure duty on ex parte motions with a Pragmatic Bluff distractor. civ-08-sol-cl-priv-005 distinguishes litigation privilege expiry from solicitor-client privilege and uses an Exception Trap and Overstatement Trap with precision.

---

## Criminal Law (43 questions)

### Verdict Table

| question_id | legal_flag | quality | anti_idx | scenario | bin_logic | distractor | rationale | prose | ethics | realism |
|-------------|------------|---------|----------|----------|-----------|------------|-----------|-------|--------|---------|
| crim-02-arrest-war-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-arrest-war-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-arrest-war-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-arrest-war-004 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| crim-02-arrest-war-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-cit-arrest-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-cit-arrest-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-cit-arrest-003 | clear | IMPROVE | 3 | 4 | 3 | 3 | 4 | 5 | N/A | 3 |
| crim-02-s10b-001 | clear | IMPROVE | 3 | 4 | 3 | 3 | 4 | 5 | N/A | 3 |
| crim-02-s10b-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-s10b-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-s10b-004 | clear | PASS | 5 | 5 | 4 | 5 | 5 | 5 | N/A | 5 |
| crim-02-s10b-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-s8-search-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-s8-search-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-s8-search-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-s8-search-004 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| crim-02-s8-search-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-s9-detent-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-s9-detent-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-s9-detent-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-s9-detent-004 | clear | PASS | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 |
| crim-02-sita-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-sita-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-02-sita-003 | clear | PASS | 5 | 5 | 4 | 5 | 5 | 5 | N/A | 5 |
| crim-02-sita-004 | clear | IMPROVE | 3 | 4 | 3 | 3 | 4 | 5 | N/A | 3 |
| crim-03-bail-grnds-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-03-bail-grnds-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-03-bail-grnds-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-03-bail-grnds-004 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| crim-03-bail-grnds-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-03-rev-onus-001 | clear | IMPROVE | 3 | 4 | 4 | 3 | 4 | 5 | N/A | 3 |
| crim-03-rev-onus-002 | clear | PASS | 4 | 4 | 5 | 4 | 4 | 5 | N/A | 4 |
| crim-03-rev-onus-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-03-rev-onus-004 | clear | PASS | 4 | 4 | 5 | 4 | 4 | 5 | N/A | 4 |
| crim-04-stinch-001 | clear | REWRITE | 2 | 3 | 2 | 2 | 3 | 5 | N/A | 2 |
| crim-04-stinch-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-04-stinch-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-04-stinch-004 | clear | PASS | 5 | 5 | 4 | 5 | 5 | 5 | N/A | 5 |
| crim-04-stinch-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-04-tpr-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-04-tpr-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| crim-04-tpr-003 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |

**Criminal Law verdict counts:** PASS 37 · IMPROVE 5 · REWRITE 1 · REMOVE 0 · LEGAL FLAG 0

---

### Criminal Law — Non-PASS Details

**crim-02-cit-arrest-003** — IMPROVE  
Scenario: citizen's arrest under s.494(1)(b) — fresh pursuit element. Anti-index 3: the call asks about the timing requirement for citizen's arrest, which is identifiable by knowing the provision. Distractor 3: two plausible distractors, but the obviously wrong option (D, unlimited time window) is too easy to eliminate. Weakness: the scenario is serviceable but thin — citizen's arrest by a shopkeeper on a thief who fled the premises. The distinction between s.494(1)(a) and (b) is the intended difficulty, but it is telegraphed by the fact pattern. Action: add a complication (e.g., delay in pursuit or third-party tip) to make the fresh-pursuit question genuinely ambiguous.

**crim-02-s10b-001** — IMPROVE  
Scenario: s.10(b) informational duty — basic statement of right to counsel. Anti-index 3: the question asks what s.10(b) requires on arrest, and the correct answer is the informational/implementational taxonomy stated directly. Distractor 3: one distractor is clearly too extreme (no right to counsel in any circumstance), bringing down the overall distractor quality. Weakness: this is an appropriate orientation question for s.10(b) but is too index-like for exam-level use. Action: upgrade by presenting a scenario where the officer gave the s.10(b) warning but in a way that was formally deficient (e.g., failed to provide access to a directory), requiring the candidate to identify which limb was breached.

**crim-02-sita-004** — IMPROVE  
Scenario: SITA for a weapon — cell phone incident. Anti-index 3: the correct answer (SITA limited to safety threat to officer, not general search for evidence) is reachable by knowing the Fearon limitations. Distractor 3: two distractors are moderately plausible but one (that SITA can extend to any digital device on arrestee's person) is too obviously wrong post-Fearon. Weakness: call is clear but the scenario has limited facts to distinguish a borderline SITA scenario — the phone presents as a straightforward evidence-search overreach. Action: complexify the scenario: give the officer a genuine safety rationale alongside the evidence motive and require the candidate to assess mixed-purpose SITA.

**crim-03-rev-onus-001** — IMPROVE  
Scenario: reverse onus under s.515(6) — knowledge that offence accused of is listed. Anti-index 3: the correct answer is: listed offence triggers reverse onus. Distractor 3: one distractor (prosecution must prove prior convictions to engage reverse onus) is plausible; the other two are weaker. Weakness: the scenario is straightforward (charged with firearms trafficking, clearly a listed offence). The deeper trap — the scope of the Crown's evidentiary burden even with reverse onus — is not tested. Action: introduce a scenario where the listed-offence threshold is genuinely ambiguous (e.g., conspiracy to commit a listed offence, or related offence) to add real application demand.

**crim-04-stinch-001** — REWRITE  
Scenario: basic statement of the Stinchcombe disclosure duty. Anti-index 2: the correct answer is a near-verbatim statement of the Stinchcombe rule ("all information relevant to the accused's ability to make full answer and defence") — answerable by keyword scanning. Bin_logic 2: no statutory threshold, exception, or mandatory/permissive distinction is exploited. Distractor 2: two of three wrong answers are obviously wrong to any candidate who has read the topic ("only exculpatory evidence" and "Crown may withhold until trial"). Weakness: pure index question — identifies the Stinchcombe standard without requiring any application. The topic is worth testing (as the stronger questions in this set demonstrate), but this entry should be the introductory drill card, not an exam question. Action: rewrite around a fact pattern where the disclosure issue is ambiguous — e.g., wiretap authorizations, informer privilege in tension with disclosure, or timing of disclosure relative to election.

---

## Family Law (39 questions)

### Verdict Table

| question_id | legal_flag | quality | anti_idx | scenario | bin_logic | distractor | rationale | prose | ethics | realism |
|-------------|------------|---------|----------|----------|-----------|------------|-----------|-------|--------|---------|
| fam-03-nfp-formula-001 | clear | IMPROVE | 2 | 3 | 3 | 3 | 4 | 5 | N/A | 3 |
| fam-03-nfp-formula-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-03-nfp-formula-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-03-nfp-formula-004 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| fam-03-nfp-formula-005 | clear | PASS | 4 | 4 | 5 | 4 | 4 | 5 | N/A | 4 |
| fam-03-deduct-marr-001 | clear | REWRITE | 1 | 2 | 1 | 2 | 3 | 5 | N/A | 2 |
| fam-03-deduct-marr-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-03-deduct-marr-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-03-deduct-marr-004 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| fam-03-deduct-marr-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-03-equal-paymnt-001 | clear | IMPROVE | 3 | 3 | 3 | 3 | 4 | 5 | N/A | 3 |
| fam-03-equal-paymnt-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-03-equal-paymnt-003 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| fam-03-equal-paymnt-004 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-03-excl-prop-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-03-excl-prop-002 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| fam-03-excl-prop-003 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| fam-03-excl-prop-004 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| fam-04-mh-possess-001 | clear | IMPROVE | 3 | 3 | 3 | 3 | 4 | 5 | N/A | 3 |
| fam-04-mh-possess-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-04-mh-possess-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-04-mh-possess-004 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| fam-04-mh-possess-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-04-mh-consent-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-04-mh-consent-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-04-mh-consent-003 | legal flag | LEGAL FLAG | — | — | — | — | — | — | — | — |
| fam-04-mh-consent-004 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| fam-04-mh-consent-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-04-excl-possess-001 | clear | IMPROVE | 3 | 3 | 3 | 3 | 4 | 5 | N/A | 3 |
| fam-04-excl-possess-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-04-excl-possess-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-04-excl-possess-004 | clear | PASS | 5 | 5 | 4 | 5 | 5 | 5 | N/A | 5 |
| fam-05-spse-supp-001 | clear | PASS | 4 | 5 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-05-spse-supp-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-05-spse-supp-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-05-spse-supp-004 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-05-spse-supp-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| fam-05-ssag-001 | clear | IMPROVE | 3 | 3 | 2 | 3 | 4 | 5 | N/A | 3 |
| fam-05-ssag-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |

**Family Law verdict counts:** PASS 32 · IMPROVE 5 · REWRITE 1 · REMOVE 0 · LEGAL FLAG 1

---

### Family Law — Non-PASS Details

**fam-04-mh-consent-003** — LEGAL FLAG  
Pre-identified unresolved flag from `docs/GENERATED_EXAM_HUMAN_REVIEW_FLAGS.md`. The question cites FLA s.21(3) as the authority for bona fide purchaser protection in matrimonial home dispositions. The correct subsection may be s.21(2); a qualified reviewer must check the current FLA text before psychometric review can proceed. No psychometric scoring assigned pending legal flag resolution.

**fam-03-nfp-formula-001** — IMPROVE  
Scenario: mechanical NFP calculation with three clean numbers. Anti-index 2: answerable by anyone who knows the formula NFP = assets − debts − marriage-date deduction; no facts force a judgment call. Distractor 3: the wrong answers each apply one error (missing deduction, missing debts, adding deduction instead of subtracting) — plausible arithmetic errors but not legal trap types. Weakness: this is a worked-example arithmetic drill, not a legal analysis question; appropriate for study materials but low exam-realism. Action: upgrade by introducing a complication that requires a legal judgment (e.g., one asset with a traceability dispute, or a marriage-date deduction ambiguity) rather than pure arithmetic.

**fam-03-deduct-marr-001** — REWRITE  
Scenario: why does the marriage-date deduction exist? Anti-index 1: the question asks for the purpose of the deduction — pure conceptual recall, no application to facts at all. Bin_logic 1: no statutory precision required. Distractor 2: wrong answers A and C are obviously wrong (punitive purpose; equalise NFPs at end of marriage). Weakness: this is a lecture-note comprehension question, not an exam question. It tests whether the candidate can state a legislative purpose, not whether they can apply it. Action: rewrite entirely as a scenario in which the marriage-date deduction is disputed (e.g., whether property qualifies for the deduction, or how to calculate it when the deduction is contested), requiring the candidate to identify the correct application of the deduction's rationale to a set of facts.

**fam-03-equal-paymnt-001** — IMPROVE  
Scenario: basic equalization payment calculation with clean numbers. Anti-index 3: requires applying the formula but all numbers are stated directly and no complications are introduced. Distractor 3: wrong answers include "Sonja pays Dimitri" (direction error) and "Dimitri pays full difference" (factor-of-2 error) — arithmetic errors rather than legal trap types. Weakness: workable for a beginner question but the scenario is too clean and the distractors are arithmetic errors rather than legally engineered traps. Action: introduce a complication (e.g., one spouse has excluded property or a marriage-date deduction) to require the candidate to first determine the NFPs before calculating the equalization payment.

**fam-04-mh-possess-001** — IMPROVE  
Scenario: wife asks if she has any right to remain in home where husband is sole registered owner. Anti-index 3: the answer (s.19(1) equal right of possession independent of ownership) is clearly stated as a general rule; no specific facts force a choice. Distractor 3: three plausible wrong answers (no right without ownership; right requires financial contribution; right requires court order) are solid conceptually but the call is so direct that knowing s.19 suffices. Weakness: appropriate orientation question but too index-like for exam use. Action: present a scenario with a competing factor (e.g., a domestic contract that arguably waived s.19 rights, or an argument that a property is not the matrimonial home) to require application.

**fam-04-excl-possess-001** — IMPROVE  
Scenario: court's power to grant exclusive possession. Anti-index 3: the question asks whether the court "can" grant exclusive possession — answer is obviously yes under s.24(1). Distractor 3: wrong answers (can't because he's the owner; only if violence; only in final order) are all clearly stated as wrong by the statutory provision. Weakness: the question is asking the candidate to recognise that s.24(1) is not limited by ownership — a correct and important point — but the level of abstraction is too high for exam realism; the scenario should present a motion with genuine ambiguity about whether the order is warranted. Action: upgrade with a scenario where the s.24(3) balancing factors are genuinely contested, not just asking whether the court "can" act.

**fam-05-ssag-001** — IMPROVE  
Scenario: SSAG advisory status — are the guidelines binding? Anti-index 3: the correct answer (SSAG are advisory only, not binding) is reachable by knowing one fact. Bin_logic 2: no mandatory/permissive statutory distinction is tested; the question is asking the candidate to know the status of a document. Distractor 3: two plausible wrong answers (binding under DA; binding in SCJ only) but the third (SSAG replace entitlement analysis) is obviously wrong to any candidate who has read the topic. Weakness: the question states the SSAG are "advisory only" in the correct answer in a way that is not well-disguised; a candidate who has seen that phrase once can get this right without understanding why. Action: reframe to test application — e.g., give a specific departure from the SSAG range and require the candidate to identify whether the court has jurisdiction to depart and on what basis, rather than just asking for the SSAG's legal status.

---

## Public Law (35 questions)

### Verdict Table

| question_id | legal_flag | quality | anti_idx | scenario | bin_logic | distractor | rationale | prose | ethics | realism |
|-------------|------------|---------|----------|----------|-----------|------------|-----------|-------|--------|---------|
| pub-02-oakes-test-001 | clear | IMPROVE | 2 | 3 | 3 | 3 | 4 | 5 | N/A | 3 |
| pub-02-oakes-test-002 | clear | PASS | 4 | 4 | 3 | 4 | 4 | 5 | N/A | 4 |
| pub-02-oakes-test-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-02-oakes-test-004 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-02-oakes-test-005 | clear | REWRITE | 1 | 2 | 1 | 2 | 3 | 5 | N/A | 2 |
| pub-02-s15-equal-001 | clear | IMPROVE | 3 | 3 | 3 | 3 | 4 | 5 | N/A | 3 |
| pub-02-s15-equal-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-02-s15-equal-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-02-s15-equal-004 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-02-s15-equal-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-02-s2-freedoms-001 | clear | PASS | 4 | 4 | 3 | 4 | 4 | 5 | N/A | 4 |
| pub-02-s2-freedoms-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-02-s7-fundjust-001 | clear | IMPROVE | 2 | 3 | 3 | 3 | 4 | 5 | N/A | 3 |
| pub-02-s7-fundjust-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-02-s7-fundjust-003 | clear | PASS | 5 | 5 | 4 | 5 | 5 | 5 | N/A | 5 |
| pub-02-s7-fundjust-004 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| pub-02-s7-fundjust-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-03-baker-fair-001 | clear | REWRITE | 2 | 2 | 2 | 2 | 3 | 5 | N/A | 2 |
| pub-03-baker-fair-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-03-baker-fair-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-03-baker-fair-004 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-03-baker-fair-005 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-03-right-reasons-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-03-right-reasons-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-03-right-reasons-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-03-right-reasons-004 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| pub-04-reason-stand-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-04-reason-stand-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-04-reason-stand-003 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-04-reason-stand-004 | clear | PASS | 5 | 5 | 4 | 5 | 5 | 5 | N/A | 5 |
| pub-04-reason-stand-005 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| pub-04-correct-std-001 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-04-correct-std-002 | clear | PASS | 4 | 4 | 4 | 4 | 4 | 5 | N/A | 4 |
| pub-04-correct-std-003 | clear | PASS | 5 | 5 | 5 | 5 | 5 | 5 | N/A | 5 |
| pub-04-correct-std-004 | clear | REWRITE | 2 | 3 | 3 | 2 | 3 | 5 | N/A | 2 |

**Public Law verdict counts:** PASS 27 · IMPROVE 4 · REWRITE 4 · REMOVE 0 · LEGAL FLAG 0

---

### Public Law — Non-PASS Details

**pub-02-oakes-test-001** — IMPROVE  
Scenario: who bears the burden of justification under s.1? Anti-index 2: the correct answer is a direct statement of a well-known rule (government bears burden on balance of probabilities). No application to facts is required. Distractor 3: wrong answers are plausible variants (shared burden; no burden; claimant bears burden) but none require the candidate to apply the standard to a situation. Weakness: appropriate as an orientation question in a study guide but too index-like for exam use; any candidate who has read one paragraph on s.1 will get this right. Action: replace with a question that requires the candidate to identify which party has failed to discharge their burden in a particular scenario, or identify where in the Oakes analysis the government's argument breaks down.

**pub-02-oakes-test-005** — REWRITE  
Scenario: what is the legal effect when the government successfully satisfies all elements of the Oakes test? Anti-index 1: the answer is "the law is saved and upheld" — pure recall. Bin_logic 1: no statutory precision is tested. Distractor 2: three wrong answers (strike down; refer to legislature; compensate) are all obviously wrong to anyone who has studied s.1. Weakness: this question tests whether the candidate knows that s.1 saves a law — a fact they would need to know just to be literate in Charter law. It is not a judgment question in any sense. Action: rewrite entirely. A possible replacement: a scenario where a court has found that Stage 1 (pressing and substantial) is satisfied but the law fails the minimal impairment branch — require the candidate to identify the consequence and the appropriate remedy (striking down, reading in, or reading down).

**pub-02-s15-equal-001** — IMPROVE  
Scenario: is citizenship an enumerated or analogous ground under s.15? Anti-index 3: the correct answer (Andrews recognises citizenship as analogous) is knowable by having read the Andrews headnote. Distractor 3: three plausible wrong answers but all can be eliminated by a candidate who knows citizenship is an analogous ground. Weakness: the question identifies the outcome of Andrews but does not require the candidate to apply the test for analogous grounds to a new situation. Action: upgrade by presenting a novel claimed analogous ground (e.g., housing status, socioeconomic status) and require the candidate to apply the criteria for recognising analogous grounds, rather than simply asking whether citizenship qualifies.

**pub-02-s7-fundjust-001** — IMPROVE  
Scenario: what threshold triggers s.7 analysis — mandatory minimum. Anti-index 2: the question asks what must be established before s.7 analysis, and the answer (the state action must deprive the person of life, liberty, or security) is a definitional threshold stated almost verbatim. Distractor 3: two wrong answers are obviously wrong (s.12 prerequisite; physical force required). Weakness: this is foundational recall. The mandatory minimum scenario is well chosen but the question only asks whether liberty is engaged — not whether the mandatory minimum is a principle of fundamental justice, which is where the real exam difficulty lies. Action: reframe to test whether the mandatory minimum meets the specific principles of fundamental justice (arbitrary, overbroad, or grossly disproportionate) by applying them to the specific facts of the mandatory minimum scenario.

**pub-03-baker-fair-001** — REWRITE  
Scenario: which Baker factor supports high procedural fairness for a licence-revocation decision? Anti-index 2: the answer (Factor 3 — importance to the individual/livelihood) is directly labelled in the option text ("Factor 3"). Bin_logic 2: no statutory threshold is tested; the question asks the candidate to name a numbered factor. Distractor 2: two wrong answers are internally inconsistent with their own descriptions (Factor 1 described as suggesting "minimal procedural requirements" for a licence-revocation decision — a contradiction that makes it obviously wrong). Scenario 2: the fact pattern is so thin (one-sentence administrative setup) that it functions as a caption, not a scenario. Weakness: answerable by any candidate who knows that "Factor 3 = importance of decision to individual" from a study table. Action: rewrite around a fact pattern where the Baker factors point in different directions — e.g., a mass administrative decision affecting many individuals (favours lower fairness on Factor 1) where each individual faces a significant impact (favours higher fairness on Factor 3) and the statute is silent on procedure (Factor 2) — requiring the candidate to weigh competing factors rather than identify the most obvious one.

**pub-04-correct-std-004** — REWRITE  
Scenario: whether exceeding statutory jurisdiction is a "jurisdictional" correctness category post-Vavilov. Anti-index 2: the correct answer is a statement of Vavilov's narrowing of the jurisdictional category — answerable by knowing the Vavilov rule. Distractor 2: Option A ("yes, any decision characterised as jurisdictional triggers correctness") is the pre-Vavilov answer that the question specifically refutes; a candidate who has read Vavilov once will eliminate it immediately. Option B ("Vavilov eliminated the jurisdictional correctness category entirely") is a plausible over-reading of Vavilov but the correct answer C states the nuance directly. Weakness: the question tests knowledge of a doctrinal change (Vavilov's narrowing) but does so in a way where both the question and the answer essentially announce the rule. There is no application demand. Action: rewrite around a concrete scenario where one party argues correctness applies because two administrative tribunals are disputing jurisdiction over the same matter, while another argues the challenge is really to the scope of a single tribunal's mandate; require the candidate to classify the jurisdictional dispute correctly under Vavilov.

---

## Legal Flag Section

### fam-04-mh-consent-003 — LEGAL FLAG (Unresolved)

**Status:** UNRESOLVED — human reviewer required  
**File:** `data/questions/family-law/ch04-matrimonial-home.json`  
**Issue:** The question's explanation and source_reference cite FLA s.21(3) as the authority for bona fide purchaser (BFP) protection in matrimonial home dispositions. The flags register notes that some sources suggest the BFP protection may be in s.21(2) rather than s.21(3), or that the subsection numbering differs between editions.  
**Substantive content:** The legal proposition tested (bona fide purchaser for value without notice of matrimonial home status is protected; wife's set-aside application fails) is substantively sound and consistent with general property law principles.  
**Psychometric note (conditional):** If the subsection number is confirmed correct, this question is a strong PASS candidate — the scenario is realistic, the BFP-without-notice trap is well-engineered, and the distractors are grounded in identifiable trap types (Overstatement Trap for option A; Exception Trap for option D). If the subsection number is wrong, the question requires a targeted update to explanation, source_reference, and any why_X_wrong fields.  
**Resolution required:** A qualified reviewer must check the current Family Law Act, R.S.O. 1990, c. F.3 text (current consolidation) to confirm which subsection addresses BFP protection in s.21.

---

## Quality Notes

### Pattern Observations

**1. Entry-level orientation questions present throughout all subjects.** Each topic cluster contains at least one "easy" question that functions as an orientation drill card rather than an exam-realism question. These uniformly score IMPROVE or REWRITE when they test a pure definitional recall (e.g., what is the purpose of X, or who bears the burden of Y). The most egregious instances are: `fam-03-deduct-marr-001` (purpose of marriage-date deduction), `pub-02-oakes-test-005` (effect of passing Oakes test), `crim-04-stinch-001` (basic Stinchcombe rule), and `pub-03-baker-fair-001` (which Baker factor supports high fairness). These should be upgraded to require application of the concept to facts.

**2. The hard/exam_trap questions are the exam's strength.** Questions rated difficulty=hard or difficulty=exam_trap almost uniformly pass with realism scores of 4 or 5. Standout examples: `fam-03-deduct-marr-004` (income on excluded gifts, donor expressly provides), `fam-04-mh-consent-004` (separation does not extinguish s.21 rights), `crim-02-arrest-war-004` (Storrey standard applied to borderline reasonable-and-probable-grounds scenario), `crim-04-stinch-004` (informer privilege exception to Stinchcombe), `civ-08-sol-cl-priv-005` (litigation privilege expiry), `pub-03-right-reasons-004` (SPPA s.17 timing hierarchy), and `pub-04-reason-stand-005` (standard of review determined by legislative framework not by court's view of correctness).

**3. Ethics integration is present but could be expanded.** The manifest reports 3 questions with PR angles. All three questions with ethics integration (`civ-06-injunction-005`, `civ-07-sumj-ev-004`, `crim-02-s9-detent-004`) are rated highly (realism 4–5). The exam would benefit from adding PR angles to 2–3 additional questions in the Family Law and Public Law subjects, which currently have no ethics-integrated questions.

**4. Distractor taxonomy strength.** The strongest distractors in the exam use: General Rule Trap (ignoring matrimonial home exception to deduction), Exception Trap (applying SITA beyond its scope), Pragmatic Bluff (proceeding with ex parte motion without full disclosure), Ethics Override Trap (choosing client tactical advantage over disclosure duty), and Premature Escalation Trap (jumping to exclusion of evidence before establishing the Charter breach). The weakest distractors are in the orientation questions and in some Public Law Charter questions where one of the four options is too obviously wrong to be a plausible distractor.

**5. Prose quality is consistently high.** No question received a prose score below 4. Fact patterns are tight and purposeful throughout. No vague pronouns or unnecessary complexity were identified. This is a genuine strength of the question pool.

### Subject-Level Quality Ranking

1. **Criminal Law** — strongest subject. Charter questions (arrest, s.8, s.10(b), s.9, SITA) and bail reverse-onus questions are consistently well-constructed. Only one REWRITE (stinch-001, a pure orientation question).
2. **Civil Litigation** — strong. Privilege and discovery questions are excellent. One REWRITE (partial-sj-003). The limitation period and injunction sets have serviceable orientation questions that should be upgraded.
3. **Family Law** — good overall. NFP formula and excluded property questions are strong. Matrimonial home questions are well-structured. Weaknesses are in the conceptual/purpose questions that avoid application. One LEGAL FLAG pending.
4. **Public Law** — weakest subject. Charter Oakes and s.15 questions include too many orientation entries. Baker fair-001 is a REWRITE. Vavilov questions (ch04) are strong and partially compensate.

---

*This document covers psychometric and exam-realism quality only. Legal accuracy is governed by the legal QA process. The single unresolved legal flag (fam-04-mh-consent-003) must be resolved by a qualified reviewer before that question may be included in a finalised exam.*
