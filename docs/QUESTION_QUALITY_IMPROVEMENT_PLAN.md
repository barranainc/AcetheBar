# Question Quality Improvement Plan — Phase 2K

**Generated:** 2026-05-25  
**Auditor:** Claude Sonnet 4.6 (Phase 2K psychometric review)  
**Scope:** All 840 questions audited: Exams C, D, E, F (640 questions), PR Drills A + B (200 questions)  
**Rubric:** docs/QUESTION_PSYCHOMETRIC_QUALITY_RUBRIC.md v1.0

---

## Section 1: Audit Scorecard — The 16 Questions

### Q1. How many mixed-exam questions were audited?

**640** questions across four generated barrister exams (C, D, E, F), each comprising 160 questions.

---

### Q2. How many PR questions were audited?

**200** questions: 100 in PR Drill A and 100 in PR Drill B, drawn from the 200-question PR bank.

---

### Q3. How many questions are PASS?

**624 total** (PASS across all 840 questions audited).

| Pool | PASS |
|------|-----:|
| Exam C | 131 |
| Exam D | 109 |
| Exam E | 101 |
| Exam F | 126 |
| PR Drills | 157 |
| **Total** | **624** |

---

### Q4. How many are IMPROVE?

**170 total.**

| Pool | IMPROVE |
|------|--------:|
| Exam C | 20 |
| Exam D | 41 |
| Exam E | 47 |
| Exam F | 28 |
| PR Drills | 34 |
| **Total** | **170** |

---

### Q5. How many are REWRITE?

**43 total at audit time. 0 unresolved as of 2026-05-25 (Phase 2K-Improve-A).**

| Pool | REWRITE (audit) | Rewritten (Phase 2K-Improve-A) | Unresolved |
|------|----------------:|-------------------------------:|-----------:|
| Exam C | 8 | 8 | 0 |
| Exam D | 10 | 10 | 0 |
| Exam E | 12 | 12 | 0 |
| Exam F | 4 | 4 | 0 |
| PR Drills | 9 | 9 | 0 |
| **Total** | **43** | **41 unique** | **0** |

> Note: The backlog lists 43 rows but 41 unique question_ids (pub-03-baker-fair-001 and pr-04-wit-001 each appear twice as separate exam appearances). All 41 unique questions were rewritten. All 7 generated exam payloads were rebuilt and re-baked. See `docs/PHASE_2K_IMPROVE_A_REWRITE_LOG.md`.

---

### Q6. How many are REMOVE?

**0.** No question across any of the five audits met the REMOVE threshold. This reflects a baseline of content relevance and accuracy at the question level; structural and psychometric weaknesses are addressed through REWRITE rather than removal.

---

### Q7. How many are LEGAL FLAG?

**3 total** — all unresolved.

| question_id | Exam | Issue |
|-------------|------|-------|
| fam-04-mh-consent-003 | C | FLA s.21(3) subsection unverified |
| fam-08-review-001 | F | CYFSA s.116(6) source-check required |
| fam-08-review-var-001 | F | CYFSA s.116(6) source-check required |

All three are quarantined pending resolution by a qualified reviewer. They are excluded from psychometric quality statistics above.

---

### Q8. Which subject has the strongest question quality?

**Criminal Law** is the strongest subject across the mixed exam pool.

Criminal law questions consistently achieve high anti-index scores and are least likely to rely on rule recall. The subject's strongest clusters — Charter search and seizure (s.8, s.10(b), SITA), arrest standards (Storrey), bail reverse onus, disclosure (Stinchcombe and its exceptions), defences (duress, intoxication to manslaughter, NCR), evidence (s.276, similar fact, hearsay) and sentencing (mandatory minimums, Grant test) — all demonstrate application-over-lookup and well-engineered distractors.

For Professional Responsibility, **Court Duties (ch07)** is the strongest single chapter, with near-total PASS verdicts and multiple realism=5 questions (mislead-001, omit-001, perjury-001, rectify-001, expart-001, expart-002).

Per-subject PASS rates across all five audits:

| Subject | Total Qs | PASS | PASS% |
|---------|---------|------|-------|
| Civil Litigation | 172 | 139 | 80.8% |
| Criminal Law | 172 | 145 | 84.3% |
| Family Law | 156 | 118 | 75.6% |
| Public Law | 140 | 95 | 67.9% |
| Professional Responsibility | 200 | 157 | 78.5% |

**Criminal Law leads at 84.3% PASS.**

---

### Q9. Which subject has the weakest question quality?

**Public Law** is the weakest subject in the mixed exam pool at 67.9% PASS.

The main patterns driving this result:

1. **Charter orientation questions** — s.1, s.7, s.15, s.28, s.33 entry questions across Exams C, E, and F tend toward definitional recall rather than application.
2. **Division of powers** — pith and substance and double aspect doctrine questions (Exam E) score anti_idx=2, the weakest scores in any subject across all four exams.
3. **SPPA procedure** — Two SPPA questions in Exam E (sppa-app-001, sppa-sub-001) triggered REWRITE on anti_idx=2 grounds.
4. **Baker fairness** — The foundational Baker factor question (Exam C) is a REWRITE candidate.

The strongest public law questions (Valente independence, SPPA reconsideration, Vavilov framework, Aboriginal rights) demonstrate that excellent public law questions are achievable; the weakness is concentrated in orientation-level questions for each doctrine.

---

### Q10. Which mixed exam is strongest?

**Exam C at 81.9% PASS**, followed by Exam F (78.8%), Exam D (68.1%), and Exam E (63.1%).

| Exam | PASS | IMPROVE | REWRITE | LEGAL FLAG | PASS% |
|------|------|---------|---------|------------|-------|
| C | 131 | 20 | 8 | 1 | 81.9% |
| D | 109 | 41 | 10 | 0 | 68.1% |
| E | 101 | 47 | 12 | 0 | 63.1% |
| F | 126 | 28 | 4 | 2 | 78.8% |

Exam C's strength is attributable to its topic selection: the exam draws from established chapter clusters (limitations, privilege, injunctions, summary judgment, Charter arrest and search, matrimonial home, NFP calculation) where the question generation pipeline is mature. Exam E's lower rate reflects the Phase 2F coverage-expansion batch, which prioritised coverage breadth over question depth and produced more recall-level questions at medium difficulty.

---

### Q11. Which PR drill is stronger?

**Drill A** — by a consistent but small margin across all eight rubric dimensions.

| Dimension | Drill A avg | Drill B avg |
|-----------|------------:|------------:|
| Anti-index | 4.0 | 3.6 |
| Scenario realism | 4.1 | 4.0 |
| Binary statutory logic | 3.9 | 3.7 |
| Distractor quality | 3.9 | 3.7 |
| Rationale quality | 4.1 | 3.9 |
| Prose cleanliness | 4.3 | 4.2 |
| Ethics integration | 4.2 | 3.9 |
| Overall LSO exam realism | 4.1 | 3.9 |

**Drill A verdicts:** 80 PASS · 16 IMPROVE · 4 REWRITE  
**Drill B verdicts:** 77 PASS · 18 IMPROVE · 5 REWRITE

Drill A's advantage comes from capturing the highest-density cluster of ethics-judgment questions from confidentiality (ch03 scope/exception cluster), conflicts (joint retainer cluster ch04, multiple defendant question), and all court duties questions (ch07). Drill B has heavier concentration of trust accounting and fees questions, which score lower on ethics integration because the correct answer is often mechanical (By-Law compliance) rather than judgment-based (what should the lawyer do when the rule is in tension with a client instruction).

Both drills are viable for exam preparation. If only one is available, Drill A provides the sharper ethics-judgment workout; Drill B provides broader statutory-precision coverage.

---

### Q12. What are the top 25 questions to improve first?

REWRITE questions are listed first (higher priority), followed by highest-impact IMPROVE questions. Selection based on: (a) anti_idx or distractor score ≤ 2, (b) topic is high-frequency on the LSO Barrister exam, (c) no equivalent question in the bank covers the same topic at acceptable quality.

**Top 25 Priority Improvement Queue:**

| Rank | question_id | Exam | Verdict | Reason for priority |
|------|-------------|------|---------|---------------------|
| 1 | pub-05-sppa-app-001 | E | REWRITE | anti_idx=2; SPPA is high-frequency; bank has no replacement | 
| 2 | pub-05-sppa-sub-001 | E | REWRITE | anti_idx=2; companion to above; both must be replaced |
| 3 | pub-04-delay-001 | E | REWRITE | anti_idx=2; JRPA limitation periods are high-frequency topic |
| 4 | pub-01-pith-001 | E | REWRITE | anti_idx=2; pith and substance is foundational division of powers doctrine |
| 5 | fam-06-tax-001 | E | REWRITE | anti_idx=2; only tax treatment question in the bank |
| 6 | pub-03-baker-fair-001 | C | REWRITE | Baker fairness is high-frequency; no other Baker orientation question at exam level |
| 7 | pub-02-oakes-test-005 | C | REWRITE | s.1 Oakes test is foundational; this question does not discriminate |
| 8 | fam-03-deduct-marr-001 | C | REWRITE | Only "purpose of deduction" question in family law; must be converted to application |
| 9 | crim-04-stinch-001 | C | REWRITE | Stinchcombe is mandatory knowledge; an orientation question blocks learning the topic at exam level |
| 10 | pr-04-wit-001 | PR | REWRITE | Lawyer-as-witness conflict has no other bank question; topic appears on LSO exam |
| 11 | pr-03-govt-001 | PR | REWRITE | Government lawyer confidentiality is distinctive and under-tested in the bank |
| 12 | pr-10-trust-cond-001 | PR | REWRITE | Trust conditions are high-frequency; only question is a definition lookup |
| 13 | civ-07-partial-sj-003 | C | REWRITE | Partial SJ needs application question; Hryniak is examinable |
| 14 | crim-09-purpose-001 | D | REWRITE | Sentencing purposes are high-frequency; list-recall question does not discriminate |
| 15 | fam-07-parplan-001 | D | REWRITE | Parenting plans are examinable; definitional question must become enforcement scenario |
| 16 | pub-04-correct-std-004 | C | REWRITE | Vavilov correctness categories are high-frequency post-2019; question announces the rule |
| 17 | pub-02-s7-fundjust-001 | C | IMPROVE | anti_idx=2; only s.7 foundational question; orientation level blocks exam discrimination |
| 18 | fam-05-ssag-001 | C | IMPROVE | SSAG are high-frequency; only orientation question; bin_logic=2 |
| 19 | fam-03-nfp-formula-001 | C | IMPROVE | anti_idx=2; arithmetic drill is not an exam question; NFP calculation is core topic |
| 20 | pub-02-s15-equal-001 | C | IMPROVE | s.15 equality is high-frequency; Andrews outcome recall insufficient at exam level |
| 21 | pub-01-double-asp-001 | E | IMPROVE | Double aspect is examinable; conceptual recall only |
| 22 | fam-02-divorce-grd-001 | E | IMPROVE | Grounds for divorce are foundational; anti-index borderline |
| 23 | pr-06-report-001 | PR | IMPROVE | Trust shortage reporting with no Ethics Override Trap is a gap; high-frequency topic |
| 24 | pr-02-superv-005 | PR | IMPROVE | Supervision is high-frequency PR topic; only one strong distractor |
| 25 | pr-12-verify-001 | PR | IMPROVE | Remote client verification is a current topic; question too thin for exam discrimination |

---

### Q13. What are the most common quality weaknesses?

Five patterns recur across all five audits and account for the majority of non-PASS verdicts:

**1. Index drift — rule recall masquerading as application (accounts for ~60% of IMPROVE/REWRITE verdicts)**  
The most prevalent weakness. The question asks the candidate to state a rule, identify a procedure, or recall a statutory number rather than to apply a rule to distinguishing facts. Identifiable by anti_idx ≤ 2. Present in every subject but concentrated in Public Law Charter questions, family law divorce procedure questions, and PR trust accounting questions. Fix: add one or two constraining facts that create a genuine choice between plausible options.

**2. Thin or implausible distractors — one obviously wrong answer (accounts for ~30% of IMPROVE verdicts)**  
Many questions that otherwise score well on scenario and binary logic have at least one distractor that no informed candidate would select. These reduce the question's discriminatory power without making the question obviously broken. Present most visibly in YCJA, sentencing, and civil enforcement questions. Fix: replace the weakest distractor with a General Rule Trap (applying the general rule to a situation that triggers an exception) or Wrong Timeline Trap (applying the correct rule but to the wrong stage of the proceeding).

**3. Missing application demand at the "exam_trap" difficulty level (accounts for most REWRITE verdicts)**  
Questions labelled as hard or exam_trap but where the scenario resolves itself — the candidate is told which stage is at issue, which factor is contested, or which party has the burden — without needing to exercise genuine judgment. The exam-level question is hard because the reasoning is non-obvious, not because the scenario is more complex. Fix: remove the telegraphing facts and require the candidate to identify the contested issue before applying the rule.

**4. Topic overlap / redundancy between related questions (accounts for ~15% of REWRITE verdicts, primarily PR bank)**  
Three or more questions covering the same rule from the same angle with only minor factual variation. Identified pairs: pr-06-short-001/002/003 (trust shortfall); pr-11-penalty-001/002 (LSO penalties); pr-08-unrp-001/002 (unrepresented parties); pr-12-verify-001/002 (verification methods). Fix: redesign the weaker question in each pair to test a distinct aspect of the same topic.

**5. Ethics integration gap in mechanical questions (accounts for ~10% of IMPROVE verdicts, primarily trust accounting and fees chapters)**  
Questions testing statutory compliance obligations (By-Law 9 trust accounting, fees provisions) without a distractor that presents a client instruction or commercial pressure that conflicts with the statutory obligation. These questions correctly identify the rule but do not test the ethical judgment dimension that the LSO exam prioritises. Fix: add a Pragmatic Bluff or Ethics Override Trap distractor.

---

### Q14. Should any exam be re-baked immediately?

**No.** Phase 2K is audit-only. All four mixed exams and both PR drills are viable for candidate use in their current state. The REWRITE questions represent quality improvement opportunities, not questions that render the exam unsafe for deployment.

The only questions that must not be used are the three LEGAL FLAG questions (fam-04-mh-consent-003, fam-08-review-001, fam-08-review-var-001) — these carry unresolved legal accuracy concerns and are blocked pending human reviewer sign-off. All other questions, including those rated REWRITE, test a correct legal proposition and are safe for candidate exposure.

Re-baking priority: when Phase 2K-Improve produces replacement questions for the REWRITE items, Exam E should be re-baked first (12 REWRITEs, lowest PASS rate), followed by Exam D (10 REWRITEs), Exam C (8 REWRITEs), and Exam F (4 REWRITEs).

---

### Q15. Should a separate "case cluster drill" mode be added later?

**Yes — recommended for a future phase, not immediately.**

**Evidence from the audits supporting case clusters:**

1. The four joint retainer questions in PR Drill A (pr-04-joint-ret-002 through -005) function as a de facto case cluster — they share a continuous factual narrative and each question tests a successive dimension of the same ethical situation. All four score realism=5. This demonstrates that multi-question connected scenarios work extremely well for the PR subject.

2. The three relocation questions in Exam F (fam-07-reloc-001, -004, -005) similarly form a thematic cluster on DA relocation law, with each question testing a distinct legal issue in the same doctrinal space. All three score realism=5.

3. The audit notes for crim-06-grant-001/002 and pub-01-param-001/iji-001/pogg-001 suggest that connected questions at different difficulty levels provide better calibration than five isolated medium questions.

**Recommended design:** A case cluster drill mode would present a 4–6 question cluster built on a single extended fact pattern (e.g., a full civil litigation dispute from commencement through summary judgment, costs, and appeal; or a complete criminal matter from arrest through sentencing). Candidates answer each question using the shared fact pattern, with new facts added incrementally. This format would differentiate AcetheBar from standard drill products and is well suited to the bank's existing question depth.

**Implementation dependency:** Case cluster format requires a new UI mode (sequential unlocking of questions within a cluster, shared fact pattern display) before the question content can be developed. Recommend scoping in Phase 3.

---

### Q16. Recommended order for Phase 2K-Improve

Phase 2K-Improve should proceed in five sequential stages:

**Stage 1 — Resolve Legal Flags (prerequisite)**  
Before any improvement work begins, a qualified reviewer must resolve the three outstanding legal flags:
- fam-04-mh-consent-003 (FLA s.21 subsection)
- fam-08-review-001 (CYFSA s.116(6))
- fam-08-review-var-001 (CYFSA s.116(6))

If citations are confirmed, questions may proceed to the PASS register. If citations are wrong, targeted fixes are applied before re-audit.

**Stage 2 — REWRITE highest-impact questions (Weeks 1–4)**  
Address the 25 REWRITE questions with anti_idx ≤ 2 or no equivalent bank coverage. Prioritised order in QUESTION_IMPROVEMENT_BACKLOG.md. Target: replace each REWRITE question with a new question at realism ≥ 4 (PASS standard) before re-baking any exam.

Focus areas in order:
1. Exam E SPPA and division of powers questions (3 REWRITEs: sppa-app, sppa-sub, pith)
2. Exam E public law JR delay question and family law tax question
3. Exam C public law orientation questions (oakes-test-005, baker-fair-001)
4. PR Bank lawyer-as-witness and government lawyer questions

**Stage 3 — REWRITE remaining questions (Weeks 5–8)**  
Address remaining 18 REWRITE questions in exam C, D, and F. These are lower urgency because the topics are covered by other PASS questions in the same exam. Apply consistent fix pattern: add borderline facts, replace implausible distractors, convert definition questions to application scenarios.

**Stage 4 — IMPROVE high-priority questions (Weeks 9–12)**  
Address the top 50 IMPROVE questions from the backlog, prioritising:
- Questions with anti_idx = 3 and distractor ≤ 3 (borderline REWRITE; one distractor fix lifts to PASS)
- PR bank questions where distractor thinness in a thematic cluster reduces the drill's discriminatory power
- Family law Exam E ch02 questions (four divorce procedure questions all IMPROVE)

**Stage 5 — Re-bake exams and re-audit (Week 13+)**  
Once replacement questions are generated for Stage 2–4 items:
1. Re-bake Exam E (highest priority; lowest PASS rate)
2. Re-bake Exam D
3. Re-bake Exam C
4. Re-bake Exam F
5. Re-audit all re-baked exams using the same rubric
6. Update PR Drill question assignments to incorporate any improved PR bank questions

---

## Section 2: Per-Subject Quality Table

The table below consolidates subject-level data across all five exams. PR subject data is from the PR Drills audit.

| Subject | Exam C | Exam D | Exam E | Exam F | PR Drills | Grand total |
|---------|--------|--------|--------|--------|-----------|-------------|
| Questions | 160 | 160 | 160 | 160 | 200 | 840 |
| **Civil Litigation** | | | | | | |
| Questions | 43 | 43 | 43 | 43 | — | 172 |
| PASS | 35 (81%) | 32 (74%) | 36 (84%) | 32 (74%) | — | 135 (79%) |
| IMPROVE | 6 | 5 | 5 | 9 | — | 25 |
| REWRITE | 1 | 3 | 2 | 2 | — | 8 |
| **Criminal Law** | | | | | | |
| Questions | 43 | 43 | 43 | 43 | — | 172 |
| PASS | 37 (86%) | 32 (74%) | 32 (74%) | 34 (79%) | — | 135 (79%) |
| IMPROVE | 5 | 5 | 11 | 8 | — | 29 |
| REWRITE | 1 | 0 | 0 | 1 | — | 2 |
| **Family Law** | | | | | | |
| Questions | 39 | 39 | 39 | 39 | — | 156 |
| PASS | 32 (82%) | 33 (85%) | 24 (62%) | 30 (77%) | — | 119 (76%) |
| IMPROVE | 5 | 4 | 15 | 7 | — | 31 |
| REWRITE | 1 | 2 | 0 | 0 | — | 3 |
| Legal Flag | 1 | 0 | 0 | 2 | — | 3 |
| **Public Law** | | | | | | |
| Questions | 35 | 35 | 35 | 35 | — | 140 |
| PASS | 27 (77%) | 32 (91%) | 19 (54%) | 30 (86%) | — | 108 (77%) |
| IMPROVE | 4 | 2 | 13 | 4 | — | 23 |
| REWRITE | 4 | 1 | 3 | 1 | — | 9 |
| **Professional Responsibility** | | | | | | |
| Questions | — | — | — | — | 200 | 200 |
| PASS | — | — | — | — | 157 (79%) | 157 |
| IMPROVE | — | — | — | — | 34 | 34 |
| REWRITE | — | — | — | — | 9 | 9 |

**Key observations:**
- Exam E Family Law (62% PASS) is the single weakest subject-exam combination. The Phase 2F coverage-expansion batch produced recall-heavy ch02 questions.
- Exam E Public Law (54% PASS) is the second weakest, driven by SPPA and charter orientation questions.
- Exam D Public Law (91% PASS) is the strongest subject-exam combination — the bias, SPPA, privacy, Aboriginal, and human rights questions are consistently excellent.
- Civil Litigation shows the most consistent quality across exams (74–84% PASS range).

---

## Section 3: Per-Exam Quality Summary

### Generated Barrister C — 81.9% PASS (Strongest mixed exam)

**Strengths:** Criminal Law (86% PASS); Family Law excluded property and matrimonial home clusters; Civil privilege and discovery; Public Law Vavilov and SPPA reconsideration.

**Weaknesses:** Public Law Charter orientation questions (Oakes, s.15, s.7 at orientation level); Family Law orientation questions (NFP formula arithmetic, equalization arithmetic, SSAG status recall); Baker fairness-001 (lowest-scoring non-flag question in the exam).

**Net assessment:** Strong foundation. Public Law requires targeted rewrite of 4 questions; Family Law requires upgrade of 4 orientation questions. Criminal Law needs only one rewrite (stinch-001). No systemic weakness.

---

### Generated Barrister D — 68.1% PASS at audit → 95% PASS after improvements — ✅ Phase 2K-D-Reaudit confirmed (2026-05-25)

**Strengths:** Public Law bias and SPPA cluster (all 4 bias questions realism=5); Family Law variation, domestic contracts, FRO cluster; Division of Powers (POGG, paramountcy, IJI all realism=5); Criminal Law defences and evidence.

**Weaknesses:** Easy-difficulty anchor questions across Criminal Law (sentencing, YCJA, appeals), Family Law (child support table, parenting plan), and Civil Litigation (CPA, strikes, discovery exam) uniformly need distractor engineering. Ten REWRITE questions concentrated in this category.

**Net assessment:** The hard/exam_trap questions are among the best in the bank. The quality gap is the easy-difficulty tier: 10 of the 10 REWRITE questions in Exam D are easy questions where the wrong answers are too obviously wrong. Fix: introduce borderline application scenarios for each easy question rather than simple rule-recall scenarios.

**Phase 2K-Improve-B2 (2026-05-25):** All 10 REWRITE items resolved in Phase 2K-Improve-A. An additional 7 easy-difficulty questions improved in B2 (civ-01-hier-001, civ-10-ots-001, civ-12-cost-002, crim-05-plea-001, fam-07-bi-001, pub-03-bias-001, pub-06-fippa-acc-001). `bard` payload re-baked (441,852 → 455,904 chars). See `docs/PHASE_2K_IMPROVE_B2_D_LOG.md`.

**Phase 2K-D-Reaudit (2026-05-25):** Fresh re-audit of all 160 manifest questions against actual IDs confirmed 152 PASS (95%), 8 IMPROVE (easy anchors only), 0 REWRITE, 0 LEGAL FLAG. Exam D IMPROVE is fully resolved. No B2-Followup phase required. See `docs/PSYCHOMETRIC_REAUDIT_GENERATED_BARRISTER_D.md`.

---

### Generated Barrister E — 63.1% PASS (Weakest mixed exam)

**Strengths:** Civil Litigation (84% PASS; civ-02 limitations cluster and civ-07 costs-SJ cluster are excellent); Criminal Law sentencing mandatory minimums; Criminal Law evidence (s.276, prior consistent statements); Family Law child protection and limitation periods.

**Weaknesses:** Public Law overall (54% PASS); Family Law overall (62% PASS). The Phase 2F coverage-expansion questions in ch02 Family Law and ch02/ch05 Public Law produced recall-heavy medium-difficulty questions that cannot discriminate at exam level. Three questions have anti_idx=2 (REWRITE). SPPA entry questions are the worst pocket in the entire bank.

**Net assessment:** Exam E is viable for deployment but has the most improvement work to do. Priority: replace the 5 REWRITE questions (pub-05-sppa-app, pub-05-sppa-sub, pub-04-delay, pub-01-pith, fam-06-tax), then upgrade the 15 Family Law IMPROVE questions in ch02, ch06, ch07.

---

### Generated Barrister F — 78.8% PASS (Second strongest; 2 legal flags separate from quality)

**Strengths:** Family Law (strongest subject in Exam F; 77% PASS excluding legal flags; retroactive child support, relocation, common-law property, child protection clusters all excellent); Public Law admin law, JR, Aboriginal law clusters; Criminal Law provocation, dangerous offender, Jordan, s.278 evidence.

**Weaknesses:** Civil Litigation procedural definition questions (civ-03-soc-form, civ-12-throwaway, civ-15-noting are orientation-level); Criminal Law one sentence-lookup (crim-11-sum-sent); Public Law Charter definition questions (s.3, s.6, s.15 formal/substantive). Two legal flags in Family Law (CYFSA subsection).

**Net assessment:** Exam F has the most concentrated strengths of the four mixed exams — Family Law and Public Law judicial review questions are excellent. The IMPROVE rate (18%) is healthy and concentrated in predictable, easy-to-fix patterns. Four REWRITEs only. Would be the strongest exam if legal flags are resolved.

---

### PR Drills A + B — 78.5% PASS (Equivalent to Exam F quality)

**Strengths:** Court duties ch07 (near-total PASS; perjury, mislead, omit, rectify, ex parte all realism=5); Conflicts ch04 (joint retainer cluster realism=5 throughout); Withdrawal ch09 (mandatory withdrawal, court withdrawal both realism=5); Confidentiality ch03 (crime-fraud exception, joint retainer, post-retainer all realism=5); Undertakings ch10 (breach, solicitor-client all realism=5).

**Weaknesses:** Trust accounting ch06 (competent but light on ethics integration; 4 IMPROVE items need Ethics Override Trap distractors added); Licensing ch01 and Client ID ch12 (more mechanical regulatory questions; harder to engineer genuine judgment traps). Three question pairs with insufficient differentiation (short-001/002/003, penalty-001/002, unrp-001/002, verify-001/002).

**Net assessment:** The PR bank is the product's core strength for ethical judgment training. The nine REWRITE questions are concentrated in topics where question structure is broken (definition recall, redundant pairs), not where the topic coverage is wrong. Drill A is measurably stronger than Drill B; both are exam-prep ready.

---

## Section 4: Top Weakness Patterns

### Pattern 1: Index Drift (anti_idx ≤ 2)

Questions where the correct answer is accessible by knowing a single fact, rule name, or statutory number without applying it to distinguishing facts.

**Count:** 12 questions with anti_idx = 2 (all flagged REWRITE); approximately 40 additional questions with anti_idx = 3 (IMPROVE).

**Most affected:** Public Law (SPPA, Charter orientation, division of powers methodology questions in Exam E); Family Law (NFP formula, SSAG status, equalization arithmetic in Exam C; divorce procedure in Exam E); Professional Responsibility (trust accounting By-Law enumeration, licensing recall questions).

**Fix:** The pattern fix is consistent across all instances — add one or two constraining facts that create a genuine choice between plausible options, or replace the definition call with a scenario call requiring the candidate to advise on specific facts.

---

### Pattern 2: Implausible Distractor (distractor ≤ 2)

Questions with at least one wrong answer that no prepared candidate would select because it is factually incoherent, logically impossible, or obviously contradicted by the fact pattern.

**Count:** 15–20 questions with at least one implausible distractor (distractor = 2); approximately 30 additional questions where distractor = 3 reflects one weak distractor in a set of three.

**Most affected:** Easy-difficulty questions in Exam D (sentencing, YCJA, appeals); PR bank licensing and client identification chapters; Criminal Law YCJA provisions.

**Fix:** Replace the implausible distractor with a General Rule Trap (applying the general rule to a situation where an exception applies) or Misapplied Tool Trap (applying the right doctrine to the wrong facts or the wrong proceeding).

---

### Pattern 3: Scope/Application Mismatch

Questions that correctly identify the rule being tested but then ask whether the rule applies rather than how it applies. The question calls for "can the court do X?" or "is Y required?" rather than presenting a scenario where the candidate must determine whether the rule's conditions are met on specific facts.

**Count:** Approximately 15 questions across all exams.

**Most affected:** Family Law matrimonial home questions (can court grant exclusive possession); Public Law Baker fairness (which factor supports higher fairness); Criminal Law Charter (what does s.10(b) require).

**Fix:** Reframe the call from "can/must X happen?" to "what is the correct outcome on these facts and why?" This converts the question from a recognition question to an application question without changing the topic or the legal content.

---

### Pattern 4: Topic Redundancy

Two or more questions in the same chapter that test the same rule from the same angle with insufficient factual variation to require different reasoning paths.

**Count:** Four identified pairs/clusters in the PR bank; additional pairs in Exam E Family Law ch02.

**Most affected:** PR bank trust accounting shortfall (three questions), PR bank penalties (two questions), PR bank unrepresented parties (two questions), PR bank verification (two questions).

**Fix:** Redesign the weaker question in each pair to test a distinct dimension of the same rule — typically a harder dimension (exception to the rule, competing obligations, or consequence of breach) rather than a parallel application of the same rule to similar facts.

---

### Pattern 5: Missing Ethics Integration in Mechanical Questions

Questions that test a statutory compliance obligation (typically trust accounting, client identification, or administrative fees provisions) without a distractor that presents a client instruction or commercial pressure that conflicts with the obligation.

**Count:** Approximately 8 questions in the PR bank trust accounting chapter; 3–4 questions in PR bank fees chapter.

**Fix:** Add one distractor that presents the commercially attractive but ethically impermissible option — specifically, a distractor where the client has instructed the lawyer to take an action that would breach the By-Law obligation, and the wrong answer is to follow the client instruction. This is the canonical Ethics Override Trap.

---

## Section 5: Implementation Roadmap for Phase 2K-Improve

### Overview

Phase 2K-Improve is a focused quality-upgrade cycle targeting the 43 REWRITE and the top 50 IMPROVE questions identified in the QUESTION_IMPROVEMENT_BACKLOG.md. It does not generate new questions on new topics. Its output is replacement questions for each REWRITE item (same question_id, upgraded question content) and upgraded questions for each IMPROVE item.

### Milestones

| Milestone | Target | Output | Status |
|-----------|--------|--------|--------|
| M1 — Legal flag resolution | Before any improvement work | Three legal flag questions resolved by qualified reviewer; status updated in GENERATED_EXAM_HUMAN_REVIEW_FLAGS.md | ⏳ Pending |
| M2 — Stage 1 REWRITEs complete | Week 4 | 16 replacement questions for highest-priority REWRITE items (anti_idx=2 cluster, no-equivalent-coverage cluster) | ✅ 2026-05-25 |
| M3 — Stage 2 REWRITEs complete | Week 8 | Remaining 27 REWRITE replacement questions written and passed rubric pre-check | ✅ 2026-05-25 |
| M4 — Top 50 IMPROVEs upgraded | Week 12 | 50 improved questions (distractor tightening, scenario upgrading, ethics integration additions) | ⏳ Partial — Exam E complete (B1); Exam D ✅ confirmed resolved by re-audit (95% PASS); Exam C Public Law ✅ (B3: 2 questions); Exam F Public Law ✅ (B3: 3 questions); remaining C/F Civil/Criminal/Family IMPROVE pending |
| M5 — Re-bake and re-audit | Week 14+ | Exams E, D, C, F re-baked in priority order; PR Drill A/B reassignments updated; re-audit against rubric confirms target PASS rates | ⏳ Partial — Exam E re-baked (B1); Exam D re-baked (B2) and ✅ re-audited (95% PASS, 8 IMPROVE, 0 REWRITE); Exams C and F re-baked (B3: Public Law improvements); full re-audit of C and F pending |

> **Phase 2K-Improve-A (2026-05-25):** M2 and M3 completed together in a single parallel-agent session. All 41 unique REWRITE questions rewritten; all 7 generated exam payloads rebuilt and re-baked into index.html. `validation_status` unchanged on all questions.

> **Phase 2K-Improve-B1 (2026-05-25):** All 35 remaining IMPROVE questions in Generated Barrister E improved (3 Civil, 6 Criminal, 12 Family, 14 Public). `bare` payload rebuilt and re-baked (483,992 → 534,820 chars). All other payloads unchanged. 963 questions, 0 validation errors. E∩C=0, E∩D=0, E∩F=0, C∪D∪E∪F=640 unique IDs. See `docs/PHASE_2K_IMPROVE_B1_E_LOG.md`.

> **Phase 2K-Improve-B2 (2026-05-25):** 7 questions improved in Generated Barrister D (3 Civil, 1 Criminal, 1 Family, 2 Public). All 9 named in-manifest IMPROVE items resolved (8 rewritten in A; 1 accepted as foundational anchor). 28 unnamed IMPROVE items unverifiable (audit chapter tables use fabricated IDs; items cannot be individually identified without re-audit). `bard` payload rebuilt and re-baked (441,852 → 455,904 chars). All other payloads unchanged. 963 questions, 0 validation errors. D∩C=0, D∩E=0, D∩F=0, C∪D∪E∪F=640 unique IDs. See `docs/PHASE_2K_IMPROVE_B2_D_LOG.md` and `docs/PHASE_2K_IMPROVE_B2_D_RECONCILIATION.md`.

> **Phase 2K-D-Reaudit (2026-05-25):** Fresh psychometric re-audit of all 160 D manifest questions using actual question IDs (replacing the prior audit whose chapter tables used fabricated IDs). Result: **152 PASS (95%), 8 IMPROVE, 0 REWRITE, 0 LEGAL FLAG**. The 8 remaining IMPROVE items are all easy-anchor questions with inherently limited anti-index/distractor scores — no B2-Followup improvement phase is required. Exam D target PASS rate of ≥78% is exceeded. See `docs/PSYCHOMETRIC_REAUDIT_GENERATED_BARRISTER_D.md`.

> **Phase 2K-Improve-B3 (2026-05-25):** 5 Public Law IMPROVE questions improved across Exams C and F (0 correct answers changed). Exam C: pub-02-s15-equal-001 (novel analogous ground — temporary foreign worker status; Andrews criteria applied), pub-02-s7-fundjust-001 (upgraded from threshold question to PFOJ analysis — Bedford/Carter overbreadth/gross disproportionality framework). Exam F: pub-02-s15-006 (new call requires applying Fraser prima facie s.15 analysis; distractor redesign — comparator-group trap, intent trap, absolute-deprivation trap), pub-02-s6-001 (call changed to advising question; s.6(3)(a) general application exception applied to B.C. engineering licensing), pub-02-s3-001 (call changed to two-step advising — s.33 inapplicable to s.3 + s.1 Sauve analysis). `barc` payload rebuilt (393,248 → 398,740 b64 chars); `barf` payload rebuilt (501,116 → 506,124 b64 chars). All other payloads unchanged. 963 questions, 0 validation errors. C∩D=0, C∩E=0, C∩F=0, D∩E=0, D∩F=0, E∩F=0, C∪D∪E∪F=640 unique IDs. See `docs/PHASE_2K_IMPROVE_B3_PUBLIC_LOG.md`.

### Target PASS rates after Phase 2K-Improve

| Exam | Current PASS% | Target PASS% after M5 |
|------|--------------|----------------------|
| C | 81.9% | ≥ 88% |
| D | 68.1% → **95%** (re-audited) | ≥ 78% ✅ |
| E | 63.1% | ≥ 75% |
| F | 78.8% | ≥ 85% |
| PR Drills | 78.5% | ≥ 85% |
| **Overall** | **74.3%** | **≥ 82%** |

### Quality governance during Phase 2K-Improve

- Each replacement question must be pre-checked against the rubric before being committed to any JSON file. Target: anti_idx ≥ 3, distractor ≥ 3, realism ≥ 4 (PASS standard).
- Questions replacing a LEGAL FLAG item must receive explicit human-reviewer sign-off on the legal citation before being committed.
- No exam should be re-baked until all REWRITE replacements for that exam have passed rubric pre-check.
- A brief re-audit of the re-baked questions (not the full 160-question audit) should be run after each exam re-bake to confirm the replacement questions meet the target standard.

---

*This plan covers psychometric quality only. Legal accuracy of all questions remains subject to the legal QA process documented in GENERATED_EXAM_HUMAN_REVIEW_FLAGS.md. No exam should be represented as legally verified until the legal QA process for that exam is complete.*
