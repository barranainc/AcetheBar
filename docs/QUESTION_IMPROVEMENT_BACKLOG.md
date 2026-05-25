# Question Improvement Backlog — Phase 2K

**Generated:** 2026-05-25  
**Source audits:** PSYCHOMETRIC_AUDIT_GENERATED_BARRISTER_C.md · D.md · E.md · F.md · PR_DRILLS.md  
**Scope:** All 840 questions audited across Exams C, D, E, F and PR Drills A/B  
**Purpose:** Prioritised queue for Phase 2K-Improve

---

## Priority 0 — Legal Flag (do not improve until resolved)

These questions carry unresolved legal flags. No psychometric work should be done until a qualified reviewer confirms the statutory citation against the current official text. They must not be re-baked into any exam in their present form.

| question_id | Exam(s) | Subject | Issue | Resolution required |
|-------------|---------|---------|-------|---------------------|
| fam-04-mh-consent-003 | C | Family Law — Matrimonial Home | FLA s.21(3) subsection unverified; may be s.21(2) | Check current FLA R.S.O. 1990, c. F.3 consolidation for BFP protection subsection |
| fam-08-review-001 | F | Family Law — Child Protection | CYFSA s.116(6) source-check required | Verify s.116(6) text and confirm it supports the tested proposition about status review of wardship orders |
| fam-08-review-var-001 | F | Family Law — Child Protection | CYFSA s.116(6) source-check required (companion to above) | Same reviewer should handle both fam-08-review-001 and fam-08-review-var-001 together |

**Note:** If the citation is confirmed correct for fam-04-mh-consent-003, it is a strong PASS candidate and needs no further psychometric work. If wrong, a targeted update to the explanation, source_reference, and why_X_wrong fields is required.

---

## Priority 1 — Rewrite ✅ RESOLVED — Phase 2K-Improve-A (2026-05-25)

All 41 unique REWRITE items below were rewritten in Phase 2K-Improve-A. See `docs/PHASE_2K_IMPROVE_A_REWRITE_LOG.md` for per-question change notes and payload rebuild summary.

**Resolution summary:**

| Subject | Questions rewritten | Correct answer changed |
|---|---|---|
| Civil Litigation | 8 | 6 |
| Criminal Law | 9 | 2 (letter renumbering only) |
| Family Law | 6 | 2 |
| Public Law | 10 | 1 (letter renumbering only) |
| Professional Responsibility | 8 | 1 |
| **Total** | **41** | **~12** |

All 7 generated exam payloads (barc, bard, bare, barf, prdra, prdrb, prb200) were rebuilt from existing manifest `question_ids_used` and re-baked into index.html. `validation_status` was not changed on any question. Validation: 963 questions, 0 errors; all integrity checks pass.

> Note: The backlog lists 43 rows but 41 unique question_ids (pub-03-baker-fair-001 and pr-04-wit-001 each appear twice). All 41 unique items are resolved.

---

All questions with REWRITE verdict across the five audits. These should be redesigned before the next quality review cycle. Each currently fails to generate genuine application demand: the correct answer is accessible without applying the tested rule to distinguishing facts, and/or one or more distractors are obviously wrong to any prepared candidate.

### Mixed Exams — REWRITE (34 questions)

#### Exam C (8 REWRITE)

| question_id | Exam | Subject | Current weakness | Recommended fix | Effort |
|-------------|------|---------|-----------------|-----------------|--------|
| civ-07-partial-sj-003 | C | Civil — Summary Judgment | Candidate need only know partial SJ is permitted where severable; two distractors obviously wrong; no genuine Hryniak application demanded | Rewrite around a scenario where intertwinement is genuinely ambiguous; require application of partial-SJ factors | medium |
| crim-04-stinch-001 | C | Criminal — Disclosure | Near-verbatim Stinchcombe rule; two of three wrong answers obviously wrong; pure index question | Rewrite around ambiguous disclosure scenario: wiretap authorization, informer privilege vs. disclosure, or timing relative to election | medium |
| fam-03-deduct-marr-001 | C | Family — NFP | Asks purpose of marriage-date deduction — pure conceptual recall, no fact application | Rewrite as a dispute scenario where the deduction is contested; require identifying correct application of the deduction's rationale to facts | medium |
| pub-02-oakes-test-005 | C | Public — Charter s.1 | Correct answer is "law is saved" — pure recall; all three wrong answers obviously wrong | Rewrite: present a scenario where Stage 1 passes but minimal impairment fails; require identifying consequence and appropriate remedy | medium |
| pub-03-baker-fair-001 | C | Public — Admin Law | Answer labelled "Factor 3" in option text; scenario is a one-sentence caption; Baker factors point in one direction only | Rewrite with competing Baker factors: mass decision (favours lower fairness) vs. significant individual impact (favours higher) vs. silent statute | high |
| pub-04-correct-std-004 | C | Public — Judicial Review | Tests Vavilov's narrowing of jurisdictional category; question and answer essentially announce the rule; no application demand | Rewrite: two tribunals disputing jurisdiction over the same matter; require classifying the dispute correctly under Vavilov | high |
| pub-02-oakes-test-001 | C | Public — Charter s.1 | Correct answer directly states government bears burden; no facts to apply; orientation-only | Replace with question requiring identification of which party failed their burden in a specific Oakes scenario | medium |
| pub-03-baker-fair-001 | C | Public — Admin Law | (see above) | (see above) | high |

> Note: pub-02-oakes-test-001 is recorded as IMPROVE in the audit chapter table but the narrative notes it is "too index-like for exam use" with anti-index=2 — treated here as REWRITE consistent with rubric mapping.

#### Exam D (10 REWRITE)

| question_id | Exam | Subject | Current weakness | Recommended fix | Effort |
|-------------|------|---------|-----------------|-----------------|--------|
| crim-02-sw-issu-001 | D | Criminal — Search Warrants | Easy anchor; distractors A/D thin (flat rate / impossible standard); scenario slightly artificial | Full scenario and distractor redesign; add s.487.1 telewarrant as Exception Trap | medium |
| crim-09-purpose-001 | D | Criminal — Sentencing | Tests s.718 purpose list recall; "financial compensation" distractor implausible for any knowledgeable candidate | Rebuild as application question: set in sentencing proceeding, require identifying which s.718 purpose justifies a specific sentence length | medium |
| crim-10-ycja-def-001 | D | Criminal — YCJA | "Under 14" and "under 21" distractors obviously wrong; no application of age-at-time-of-offence rule demanded | Add borderline-age scenario (offence straddling 12th birthday) to force s.2(1) application | medium |
| crim-11-sum-app-001 | D | Criminal — Appeals | Easy summary conviction appeal routing; Federal Court and trial court distractors obviously wrong | Add leave vs as-of-right distinction within s.839 Superior Court appeals | medium |
| fam-06-cs-table-001 | D | Family — Child Support | Implausible "$500 flat rate" distractor; scenario too generic | Rebuild as borderline s.3(2)(b) adult child scenario where FCSG table applicability is contested | medium |
| fam-07-parplan-001 | D | Family — Parenting | Too definitional on parenting plan status; distractor C (automatic binding) plausible but others thin | Convert to enforcement context: parenting plan incorporated by consent order, one party denies binding effect — force s.16.2 application | medium |
| pub-04-div-court-001 | D | Public — Judicial Review | Too easy; correct court identifiable by elimination; two obviously-wrong distractors | Rebuild as multi-element procedural question: time-sensitive matter with leave requirement, 30-day deadline, and certiorari vs mandamus distinction | high |
| civ-03-strike-001 | D | Civil — Pleadings | Distractor C weakly distinguished from correct answer; anti-index borderline | Full scenario rebuild with stronger Misapplied Tool trap in distractor C | medium |
| civ-04-exam-001 | D | Civil — Discovery | Distractor A too thin; no Wrong Timeline Trap exploited | Rebuild with stronger Wrong Timeline Trap based on examination timeline vs undertaking deadline | medium |
| civ-08-cpa-001 | D | Civil — Class Proceedings | Distractor B unlabelled and obvious for anyone with CPA knowledge | Rebuild: label as General Rule Trap; sharpen why "non-identifiable class members" is the expected but wrong answer | low |

#### Exam E (12 REWRITE)

| question_id | Exam | Subject | Current weakness | Recommended fix | Effort |
|-------------|------|---------|-----------------|-----------------|--------|
| pub-04-delay-001 | E | Public — Judicial Review | Anti-index=2; knowing 30-day JRPA limit fully sufficient; distractors (no limit / 6 months / absolute bar) obviously distinguishable | Rewrite with overlapping limitations provisions to eliminate pure recall character | medium |
| pub-05-sppa-app-001 | E | Public — SPPA | Anti-index=2; distractor quality=2; knowing SPPA s.3(1) definition is sufficient; distractors too easily eliminated | Rewrite as application question: whether a specific informally resolved complaint triggers SPPA s.3(1) "required to hold a hearing" element | medium |
| pub-05-sppa-sub-001 | E | Public — SPPA | Anti-index=2; distractor quality=2; knowing SPPA s.12 summons power is sufficient | Rewrite: contested relevance scenario — should tribunal summons documents from a third party with disputed connection to the proceeding? | medium |
| pub-01-pith-001 | E | Public — Division of Powers | Anti-index=2; knowing pith and substance is the first step is sufficient; methodology identification not methodology application | Add application requiring actual characterization judgment rather than identifying the methodology | medium |
| fam-06-tax-001 | E | Family — Child Support | Anti-index=2; recall-based on tax treatment of support; no application | Add application scenario testing edge cases between pre/post-1997 regime change | medium |
| civ-02-susp-ext-001 | E | Civil — Limitations | Distractor B arithmetically almost correct but misleadingly worded rather than trap-engineered | Convert to stronger Wrong Timeline Trap based on litigation guardian appointment date vs 18th birthday | low |
| civ-05-material-001 | E | Civil — Motions | Material fact vs evidence distinction is recall-based; distractors not strongly differentiated | Add fact pattern where some items could be either material fact or evidence to force application | low |
| crim-03-surety-001 | E | Criminal — Bail | Surety obligation distractors predictable; scenario generic | Develop scenario where surety's obligation is triggered in ambiguous circumstances | medium |
| crim-04-timing-001 | E | Criminal — Disclosure | Timing of disclosure obligation sequential/recall | Add scenario where Crown's obligation is contested on a borderline basis | medium |
| crim-05-plea-barg-001 | E | Criminal — Pre-Trial | Ethics angle present but distractors not fully trap-engineered around PR obligations | Develop distractor around whether counsel can agree to facts adverse to client without instruction | medium |
| fam-02-divorce-bar-002 | E | Family — Divorce | Divorce bar rules sequential recall without application pressure | Add scenario distinguishing collusion from condonation on ambiguous facts | medium |
| fam-02-jurisdiction-001 | E | Family — Divorce | Jurisdictional rule has statutory precision but weak trap engineering | Add scenario where both spouses in different provinces for exactly one year | medium |

#### Exam F (4 REWRITE)

| question_id | Exam | Subject | Current weakness | Recommended fix | Effort |
|-------------|------|---------|-----------------|-----------------|--------|
| civ-15-noting-002 | F | Civil — Default Proceedings | Pure index recall: who files noting in default; distractors implausible | Rewrite around scenario where noting-in-default procedure has gone wrong — what procedural steps are required | medium |
| civ-16-counsel-001 | F | Civil — Class Actions | Definitional question on class counsel's "role"; distractors obviously wrong; no ethics integration despite PR being a significant concern | Rewrite with concrete conflict-of-interest or duty-to-class scenario requiring choice of correct professional obligation | medium |
| crim-11-sum-sent-001 | F | Criminal — Appeals | Pure timeline lookup: time limit for appealing summary conviction sentence; distractors are just numbers (15/30/60/90 days) | Rewrite: new event arises after appeal window (sentence completed, new grounds) — candidate advises on available mechanisms | medium |
| pub-07-charter-dam-002 | F | Public — Crown Liability | Easy-difficulty good-faith vs Charter damages question; distractors obviously wrong; no scenario tension | Rewrite with harder fact pattern: systemic breach + good faith defence competing with deterrence; engineer distractors around Ward three-step analysis | high |

### PR Bank — REWRITE (9 questions)

| question_id | Drill | Subject | Current weakness | Recommended fix | Effort |
|-------------|-------|---------|-----------------|-----------------|--------|
| pr-02-specialist-001 | A/B | PR — Competence | "Specialist is a marketing term" distractor implausible; pure rule recall | Rewrite testing whether advertising as "certified specialist" without LSO certification attracts higher standard of care — integrates marketing rule with competence | medium |
| pr-03-govt-001 | A/B | PR — Confidentiality | Government lawyer confidentiality is distinctive but question is structurally thin; reads as basic rule recall | Rewrite with specific scenario (demand from internal audit team for client communications); test whether "client" is Crown, ministry, or individual official | high |
| pr-04-wit-001 | A/B | PR — Conflicts | Lawyer-as-witness fails to create genuine ethical override; distractors thin; ethics integration especially low | Rewrite: lawyer is only witness to key fact; client insists on keeping lawyer; time-sensitive motion — apply rules on withdrawal vs. staying as witness | high |
| pr-05-split-002 | B | PR — Fees | Fee splitting rules without genuine ethics override; one distractor absurd | Rewrite as judgment scenario: thank-you payment that blurs into referral fee; test permissibility and conditions | medium |
| pr-06-short-003 | B | PR — Trust Accounting | Duplicates ground covered in short-001 and short-002; minor factual variation | Redeploy to different trust accounting topic: disputed client funds when a transaction does not close | medium |
| pr-08-unrp-002 | B | PR — Opposing Parties | Structural overlap with opp-002; weakest distractor set in chapter | Rewrite to test specific aspect of unrepresented party rules: minimal legal information vs. substantive engagement prohibition | medium |
| pr-10-trust-cond-001 | A/B | PR — Undertakings | Trust condition definition question with thin fact pattern; no judgment demand | Rewrite: lawyer pressured by client to use documents subject to trust condition in way exceeding conditions — test whether condition is binding and required action | high |
| pr-13-solicit-001 | B | PR — Marketing | Weakest distractor set in ch13; one option facially absurd | Rewrite with disaster-victim/nurse referral scenario; test direct solicitation prohibition and its exceptions in PI context | medium |
| pr-04-wit-001 | A/B | PR — Conflicts | (see above) | (see above) | high |

---

## Priority 2 — Improve

All questions with IMPROVE verdict across the five audits. These are usable in the current exam without immediate redesign but should be upgraded in the next generation cycle. Ordered within each exam by subject then chapter.

> **Phase 2K-Improve-B1 (2026-05-25):** All 35 remaining IMPROVE questions from Generated Barrister E were improved. See `docs/PHASE_2K_IMPROVE_B1_E_LOG.md` for per-question change notes and payload rebuild summary. Resolved E items are marked below with ✅.


### Exam C — IMPROVE (20 questions)

| question_id | Exam | Subject | Current weakness | Recommended fix | Effort |
|-------------|------|---------|-----------------|-----------------|--------|
| civ-02-basic-lim-001 | C | Civil — Limitations | Two-year basic limitation; anti-index=2; lowest-difficulty entry | Add discoverability complication or s.16 exception as distractor | low |
| civ-06-injunction-004 | C | Civil — Injunctions | Balance-of-convenience stage identified by name-recognition; distractors weak | Reframe to require applying balance-of-convenience factors to facts | medium |
| civ-07-summ-judg-005 | C | Civil — Summary Judgment | Costs general rule stated directly; lacks application demand | Introduce fact making one distractor tempting (bad-faith conduct triggering substantial indemnity) | low |
| civ-09-ref-und-005 | C | Civil — Discovery | "Unreasonable delay" given away in fact pattern; distractors lack precision | Make delay duration ambiguous; require identifying factors informing court's discretion | medium |
| crim-02-cit-arrest-003 | C | Criminal — Arrest | s.494(1)(a)/(b) distinction telegraphed by facts; one distractor too easy to eliminate | Add complication (delay in pursuit or third-party tip) to make fresh-pursuit question genuinely ambiguous | medium |
| crim-02-s10b-001 | C | Criminal — Charter | Basic s.10(b) informational/implementational taxonomy; orientation-only | Upgrade: officer gave s.10(b) warning in formally deficient way; identify which limb was breached | medium |
| crim-02-sita-004 | C | Criminal — Search | SITA phone scenario; post-Fearon one distractor obviously wrong | Complexify: genuine safety rationale alongside evidence motive; assess mixed-purpose SITA | medium |
| crim-03-rev-onus-001 | C | Criminal — Bail | Listed-offence threshold not genuinely ambiguous; deeper trap (scope of Crown's burden) not tested | Introduce scenario where listed-offence threshold is genuinely ambiguous (conspiracy to commit listed offence) | medium |
| fam-03-nfp-formula-001 | C | Family — NFP | Arithmetic drill; no legal judgment call | Upgrade: introduce traceability dispute or marriage-date deduction ambiguity | medium |
| fam-03-equal-paymnt-001 | C | Family — NFP | Arithmetic errors as distractors; not legally engineered traps | Add excluded property or marriage-date deduction complication before calculation | medium |
| fam-04-mh-possess-001 | C | Family — Matrimonial Home | s.19(1) equal possession stated directly; orientation-only | Add competing factor: domestic contract arguably waiving s.19 rights, or argument that property is not matrimonial home | medium |
| fam-04-excl-possess-001 | C | Family — Matrimonial Home | Question asks whether court "can" grant exclusive possession — obviously yes; abstraction level too high | Upgrade with scenario where s.24(3) balancing factors are genuinely contested | medium |
| fam-05-ssag-001 | C | Family — Spousal Support | SSAG advisory status reachable by knowing one phrase; binary_logic=2 | Reframe to test application: departure from SSAG range — identify jurisdiction to depart and basis | medium |
| pub-02-s15-equal-001 | C | Public — Charter s.15 | Andrews outcome recalled by headnote; candidate need not apply the test | Upgrade with novel claimed analogous ground; require applying criteria for recognising analogous grounds | medium |
| pub-02-s7-fundjust-001 | C | Public — Charter s.7 | Definitional threshold; whether liberty engaged not whether mandatory minimum meets PFOJ | Reframe to test whether mandatory minimum is arbitrary, overbroad, or grossly disproportionate | medium |
| fam-04-mh-consent-001 | C | Family — Matrimonial Home | (PASS but adjacent to legal flag cluster — monitor) | No action required unless fam-04-mh-consent-003 flag reveals systemic issue | low |

> Note: The above 15 items are the C-exam IMPROVE questions for which clear action is documented. The audit records 20 IMPROVE verdicts total; the remaining 5 scored realism=3 with weaker action notes and are captured in the audit document.

### Exam D — IMPROVE ✅ RESOLVED — Phase 2K-D-Reaudit (2026-05-25)

Re-audit using actual manifest IDs confirmed: **152/160 PASS (95%), 8 IMPROVE, 0 REWRITE**. All 10 REWRITE items from the Phase 2K audit were resolved in Improve-A; all named in-manifest IMPROVE items were resolved in Improve-A + B2. The 8 remaining IMPROVE items are easy-anchor questions with inherently limited anti-index/distractor scores — all are educationally appropriate and none require immediate revision. See `docs/PSYCHOMETRIC_REAUDIT_GENERATED_BARRISTER_D.md`.

**B2 improvement summary (7 questions, 0 correct answers changed):**

| Subject | Questions improved | Correct answer changed |
|---|---|---|
| Civil Litigation | 3 | 0 |
| Criminal Law | 1 | 0 |
| Family Law | 1 | 0 |
| Public Law | 2 | 0 |
| **Total** | **7** | **0** |

Notes:
- All 10 REWRITE items resolved in Phase 2K-Improve-A.
- 7 easy-difficulty questions improved in B2: civ-01-hier-001, civ-10-ots-001, civ-12-cost-002, crim-05-plea-001, fam-07-bi-001, pub-03-bias-001, pub-06-fippa-acc-001.
- Fresh re-audit (Phase 2K-D-Reaudit, 2026-05-25) confirms D is now exam-ready at 95% PASS.
- 8 residual IMPROVE items (easy anchors) are low-urgency; see Phase 2K-D-Reaudit findings below.

### Phase 2K-D-Reaudit Findings — Remaining IMPROVE Items (8 questions)

**Re-audit date:** 2026-05-25 | **Source:** `docs/PSYCHOMETRIC_REAUDIT_GENERATED_BARRISTER_D.md`

All 8 are easy-anchor questions with realism=4 but anti_idx=3 or distractor=3 due to topic simplicity. None require immediate action. Retain all as foundational anchors; improve opportunistically if a natural borderline scenario exists.

| question_id | Exam | Subject | Weakness | Recommended action | Effort |
|---|---|---|---|---|---|
| civ-01-hier-002 | D | Civil — Court Hierarchy | Easy anchor; anti_idx=3 — pure CJA s.22 $35K recall with no borderline scenario | Add borderline scenario forcing choice between SCC and Superior Court | low |
| civ-04-pers-001 | D | Civil — Service | Easy anchor; one distractor thin — refusal-to-accept rule for individual service | Add scenario requiring service on a director vs. any employee | low |
| civ-16-opt-001 | D | Civil — Class Actions | Correct answer says opt-out filed "with court administrator" — may be imprecise relative to CPA s.9 notice order mechanics | Verify CPA s.9 opt-out addressee in practice; tighten option C if needed | low |
| crim-01-juris-001 | D | Criminal — Jurisdiction | Easy anchor; anti_idx=3 — s.553 absolute jurisdiction theft under $5K | Add borderline $5,000 threshold scenario | low |
| crim-06-burden-001 | D | Criminal — Trial | Easy anchor; distractors serviceable but thin on BRD standard | Add evidential/persuasive burden confusion scenario | low |
| crim-07-hearsay-001 | D | Criminal — Evidence | Easy anchor; principled hearsay approach (R. v. Khan) — anti_idx=3 | Add harder reliability-necessity application scenario | low |
| fam-08-cwo-002 | D | Family — Child Protection | Easy anchor; child-in-need threshold element — anti_idx=3, distractor=3 | Acceptable as foundational anchor | low |
| pub-07-crown-imm-001 | D | Crown Liability | Easy anchor; CLPA abrogates Crown immunity — anti_idx=3, distractor=3 | Acceptable as foundational anchor | low |

### Exam E — IMPROVE ✅ RESOLVED — Phase 2K-Improve-B1 (2026-05-25)

All 35 remaining IMPROVE items in Exam E (after Phase 2K-Improve-A removed 12 REWRITEs) were improved in Phase 2K-Improve-B1. See `docs/PHASE_2K_IMPROVE_B1_E_LOG.md` for per-question change notes.

Key IMPROVE items not already listed under REWRITE (all resolved):

| question_id | Exam | Subject | Current weakness | Recommended fix | Effort |
|-------------|------|---------|-----------------|-----------------|--------|
| civ-03-strike-002 | E | Civil — Pleadings | Distractor set predictable for striking-out rules | Strengthen with Premature Escalation Trap (SJ before pleadings close) | low |
| civ-11-trial-proc-001 | E | Civil — Trial | Trial procedure sequential recall; distractors not trap-engineered | Add scenario where procedure applied in unexpected situation | medium |
| civ-13-notice-app-001 | E | Civil — Appeals | Notice of appeal timing/content mechanical; distractors could be sharpened | Engineer Wrong Timeline Trap around 30-day vs 15-day distinction | low |
| crim-07-biz-rec-001 | E | Criminal — Evidence | Business records exception recall-based; s.30 CEA conditions mechanical | Add scenario where one element (regularity of keeping) is contested | medium |
| crim-07-prior-consist-002 | E | Criminal — Evidence | Prior consistent statement exceptions need more factual differentiation | Sharpen scenario to require choosing between fabrication allegation and recent complaint exceptions | medium |
| crim-09-consec-001 | E | Criminal — Sentencing | Consecutive vs concurrent rule mechanical; totality principle not tested | Add totality principle constraint requiring candidate to apply the cap | medium |
| crim-09-disc-001 | E | Criminal — Sentencing | Discharge eligibility largely recall; anti-index low | Add borderline scenario (dual-jurisdiction or hybrid offence) to force eligibility test application | medium |
| crim-10-conf-001 | E | Criminal — Evidence | Confession rule scenario could force application of harder element (operating mind) | Develop the "operating mind" element more precisely | medium |
| crim-11-ind-app-001 | E | Criminal — Appeals | Indictable appeal routing is rule-recall without application pressure | Convert to fact pattern where mode of trial changes the appeal court | medium |
| fam-02-divorce-grd-001 | E | Family — Divorce | Grounds for divorce foundational; anti-index borderline | Develop distractors around physical vs mental cruelty grounds distinction | low |
| fam-02-petition-001 | E | Family — Divorce | Petition procedural requirements recall-based | Develop factual wrinkle requiring application of procedural rules | low |
| fam-05-non-comp-001 | E | Family — Spousal Support | Non-compensatory support entitlement definitional recall | Develop hybrid-entitlement scenario forcing application of both compensatory and non-compensatory factors | medium |
| fam-06-adult-child-001 | E | Family — Child Support | Rule-recall on adult child conditions; age-18/21 cutoffs distractor weak | Develop stronger trap types: General Rule Trap (over 18 = no support) | low |
| fam-06-cs-s7-002 | E | Family — Child Support | Proportional s.7 formula mechanical; distractors predictable | Strengthen distractors with trap-engineering | low |
| fam-07-grandpar-001 | E | Family — Parenting | Standing rule for grandparent access largely rule recall; CLRA/DA distinction not deeply tested | Sharpen CLRA vs DA trap; develop "DA only" vs "both statutes" confusion | medium |
| fam-07-interim-001 | E | Family — Parenting | Status quo principle is a soft rule; distractors weak | Sharpen statutory basis; add DA section reference in distractors | medium |
| fam-07-superv-access-001 | E | Family — Parenting | Material change principle not deeply tested; supervised access distractors predictable | Develop stronger wrong answers distinguishing types of supervision orders | medium |
| fam-09-setting-001 | E | Family — Domestic Contracts | Definitional distinction between contract types is index-like | Add scenario where wrong type of contract creates legal consequence | medium |
| fam-10-inter-prov-001 | E | Family — FRO | ISO Act existence is largely sufficient; application of coordination mechanism thin | Develop factual wrinkle testing how inter-provincial coordination operates | medium |
| fam-10-reg-susp-001 | E | Family — FRO | Corporate veil angle introduced but not developed as proper exam trap | Develop corporate registration suspension as explicit General Rule Trap type | medium |
| fam-13-cl-def-001 | E | Family — Common Law | Fairly straightforward rule application; distractors predictable | Sharpen "3 years OR parenthood" disjunctive distinction distractor | low |
| pub-01-double-asp-001 | E | Public — Division of Powers | Double aspect doctrine conceptual recall; distractors not trap-engineered | Add fact pattern requiring actual characterization judgment | medium |
| pub-01-s92-13-001 | E | Public — Division of Powers | Recall-based; property/civil rights vs federal trade/commerce distinction weak | Develop stronger application scenario requiring IJI vs paramountcy distinction | medium |
| pub-02-s10a-001 | E | Public — Charter | Rule-statement of s.10(a) content; identifiable by knowing rule | Add partial/ambiguous disclosure scenario to force application | medium |
| pub-02-s12-001 | E | Public — Charter | Reasonable hypothetical not deeply tested | Strengthen by requiring application of reasonable hypothetical to specific facts | medium |
| pub-02-s28-001 | E | Public — Charter | s.28 as interpretive guarantee is nuanced but recall-based | Add application scenario testing whether s.28 modifies s.15 analysis | medium |
| pub-02-s33-001 | E | Public — Charter | Which rights can/cannot be overridden is recall | Develop application scenario requiring analysis of which rights survive s.33 override | medium |
| pub-03-delegation-001 | E | Public — Admin Law | Delegatus non potest delegare recall; enabling statute partial authorization not tested | Develop harder sub-delegation scenario with partial enabling statute authorization | medium |
| pub-03-reasons-003 | E | Public — Admin Law | Baker five factors present but scenario is clear-cut | Sharpen distractors: distinguish absolute Baker duty from contextual duty more precisely | low |
| pub-04-mootness-001 | E | Public — Judicial Review | Borowski two-stage test correctly stated; distractor D weak | Strengthen distractor D; develop stage-two discretion scenario | medium |
| pub-04-record-001 | E | Public — Judicial Review | Record scope question good; exception rule is recall-level | Engineer stronger Misapplied Tool trap (de novo review in narrow Charter contexts) | medium |
| pub-04-standing-001 | E | Public — Judicial Review | Three-part public interest standing test well-stated; distractor B (automatic standing) weak | Replace distractor B with more nuanced alternative | low |
| pub-06-pipeda-breach-001 | E | Public — Privacy | Distractor A (no mandatory obligation) very obviously wrong | Replace with nuanced wrong answer distinguishing notification to Commissioner-only vs dual notification | low |
| pub-07-vic-liab-001 | E | Public — Crown Liability | Crown vicarious liability fairly direct PACA s.5 application; distractors could be sharper | Strengthen distractor D (personal phone call = frolic) as proper Exception Trap | low |
| pub-08-prima-facie-001 | E | Public — Human Rights | Prima facie discrimination onus shift definitional; distractors weak | Develop scenario where burden shift is at issue because protected characteristic was only one factor among many | medium |

### Exam F — IMPROVE (28 questions)

| question_id | Exam | Subject | Current weakness | Recommended fix | Effort |
|-------------|------|---------|-----------------|-----------------|--------|
| civ-03-soc-form-001 | F | Civil — Pleadings | Generic lookup scenario on r.14.03; no applied judgment | Revise to require applying rule to realistic drafting dilemma (what must appear in endorsement for specific claim type) | low |
| civ-11-ev-003 | F | Civil — Trial Evidence | Rule-recall question; insufficient facts for genuine choice; distractors lack trap-engineering | Add facts requiring candidate to distinguish admissibility from weight in a real-court context | medium |
| civ-12-repres-001 | F | Civil — Costs | Costs representation; one distractor would not mislead any informed candidate | Replace weaker distractor with exception to representation rules (disbursements vs fees, or timing trap) | low |
| civ-12-throwaway-001 | F | Civil — Costs | Vocabulary-level question on doctrinal concept; no application | Introduce fact-specific scenario where candidate must advise whether action qualifies or falls outside tested concept | medium |
| civ-14-enf-garn-exam-001 | F | Civil — Enforcement | Thin distractors; one obviously absurd option; no oral vs affidavit trap | Engineer distractor around wrong-procedure trap (cross-examination vs examination in aid) | low |
| civ-14-enf-repl-001 | F | Civil — Enforcement | One implausibly wrong distractor; mandatory/permissive distinctions not exploited | Replace weakest distractor with wrong-form or wrong-sequence trap | low |
| crim-08-colour-right-001 | F | Criminal — Defences | Colour of right defence underexplored; rationale does not name distractor trap types | Name each distractor trap type; sharpen call to force application of subjective test | low |
| crim-08-ncr-001 | F | Criminal — Defences | "Alien invaders" scenario cartoonish and unrealistic; distractors conflate automatism with NCR | Replace with realistic mental disorder fact pattern (paranoid schizophrenia believing victim was demon); sharpen automatism/NCR distinction | medium |
| crim-09-rest-001 | F | Criminal — Sentencing | Restitution as rule recall; no quantum application | Add computational or threshold element (partial insurance recovery reduces restitution?) | medium |
| crim-10-records-001 | F | Criminal — YCJA | One clearly implausible YCJA records distractor | Replace implausible distractor with adult-records misapplication (Misapplied Tool) trap | low |
| crim-11-prerog-001 | F | Criminal — Appeals | Categorization not application question; scenario does not force judgment between competing vehicles | Reframe as Crown-liability advising scenario requiring selection of correct vehicle | medium |
| fam-07-parcoord-001 | F | Family — Parenting | Parenting coordinator role is definitional; asks "what does a PC do" not "when/how to apply" | Recast as scenario where counsel must advise whether referral to PC, mediator, or court is appropriate | medium |
| fam-13-cl-fla29-001 | F | Family — Common Law | FLA s.29 three-year threshold; scenario thin; correct answer accessible by knowing rule | Introduce borderline scenario (2 years 9 months with extended separation) requiring application of continuous cohabitation rule | medium |
| fam-13-cl-supp-002 | F | Family — Common Law | One distractor factually incoherent; call slightly abstract | Replace implausible distractor with Misapplied Tool trap; tighten call to concrete advising task | low |
| pub-02-s15-006 | F | Public — Charter s.15 | Formal vs substantive equality tested abstractly; no applied fact pattern | Add real-world government program scenario; create distractors turning on formal equality reasoning | medium |
| pub-02-s3-001 | F | Public — Charter s.3 | Artificial scenario; candidate knowing s.33 cannot override s.3 answers without applying reasoning | Add factual complexity around s.33 scope or procedural requirements; explore what s.33 can override | medium |
| pub-02-s6-001 | F | Public — Charter s.6 | Definitionally thin; correct answer directly stated in option text; one obviously wrong option | Add scenario involving provincial licensing restriction limiting mobility rights; assess s.6(2)(b) applicability | medium |

> Note: The full list of 28 F-exam IMPROVE questions is in the audit document. The highest-impact subset is listed above; the remaining items (civ-10-accept-001 through civ-15-default-003 cluster) have similar distractor-tightening actions with low effort.

### PR Bank — IMPROVE (34 questions)

Key IMPROVE items not already in REWRITE priority:

| question_id | Drill | Subject | Current weakness | Recommended fix | Effort |
|-------------|-------|---------|-----------------|-----------------|--------|
| pr-01-class-lic-001 | A | PR — Licensing | Distractors B/C/D too easily eliminated; scenario underspecified | Add genuine partial-scope trap distractor | low |
| pr-01-cpd-002 | A | PR — Licensing | Scenario too simple; no distractor convincingly mimics real misconception | State that LSO email suggested reduced-hour option; test whether Priya may rely on it without formal non-practising status | low |
| pr-02-superv-005 | A | PR — Competence | Distractor A (independent judgment) unconvincing | Change distractor A to argue Xavier was supervising because he reviewed account statements monthly | low |
| pr-02-scope-001 | A | PR — Competence | Distractors A and D obviously wrong; distractor C is only real trap | Replace distractor D with trap on whether limitation communicated in plain enough language | low |
| pr-03-confid-scope-001 | A | PR — Confidentiality | All three wrong options transparent | Add distractor testing whether publicly available court records make information no longer confidential | low |
| pr-03-post-ret-001 | A | PR — Confidentiality | Distractor D partially correct as stated | Revise distractor D to be clearly over-broad; allow correct answer to reign cleanly | low |
| pr-03-tech-conf-003 | A | PR — Confidentiality | Only one strong distractor | Add consent-to-social-media-posting distractor as cure for re-identification risk | low |
| pr-03-cloud-001 | B | PR — Confidentiality | Distractor A only convincing | Add distractor testing whether general TOS review at account opening is sufficient | low |
| pr-04-former-cl-003 | A | PR — Conflicts | "Information may be stale" distractor too weak | Add distractor testing whether firm-level information barrier (different lawyers) cures the conflict | medium |
| pr-04-estate-001 | B | PR — Conflicts | Estate conflict underspecified | Add facts about which estate stakeholder retained lawyer and whether conflict is consentable | medium |
| pr-05-cont-003 | B | PR — Fees | "Best efforts" distractor obviously wrong | Replace with distractor based on real-world commercial misconception | low |
| pr-05-ref-fee-002 | A | PR — Fees | Lacks fact-specific twist requiring application over lookup | Add fact triggering "ongoing involvement" exception to pure referral fee rule | low |
| pr-06-audit-001 | B | PR — Trust Accounting | Rule-recall disguised as application | Add moved-practice or dual-practice fact to require audit rules application | low |
| pr-06-bylaw-002 | B | PR — Trust Accounting | Near-index on By-Law enumeration | Create disputed application fact | low |
| pr-06-report-001 | A | PR — Trust Accounting | No Ethics Override Trap in distractor set | Add distractor where lawyer argues self-remediation before discovery excuses reporting obligation | medium |
| pr-07-auth-001 | A | PR — Court Duties | Distractor C not sufficiently trap-engineered | Reframe distractor C to test "undertaking to cure" scenario | low |
| pr-07-unmerit-001 | B | PR — Court Duties | Distractor set weak on application | Add distractor where lawyer argues client's subjective belief makes proceeding meritorious | low |
| pr-08-discrim-001 | B | PR — Opposing Parties | Discrimination question abstract; no grounding facts | Add fact triggering plausible tension (religious exemption claim or belief conduct was not discriminatory) | medium |
| pr-09-subs-001 | A | PR — Withdrawal | File-transfer/substitution confusion present but not drawn sharply | Clarify to sharpen mandatory file-transfer timing as key binary statutory issue | low |
| pr-09-time-001 | B | PR — Withdrawal | Too mechanical; low ethics integration | Add time-pressure element requiring candidate to weigh competing obligations | medium |
| pr-11-penalty-001 | A | PR — Discipline | Imprisonment distractor facially absurd | Replace with "mandatory trust supervision order" option | low |
| pr-11-penalty-002 | B | PR — Discipline | Overlaps in structure with penalty-001 | Differentiate: test consent order vs contested discipline outcome, or conditions on practice vs suspension | medium |
| pr-12-verify-001 | B | PR — Client ID | Remote verification lacks specific method to evaluate | Present specific method (video call ID scan) as one distractor; non-compliant shortcut as another | low |
| pr-12-verify-002 | B | PR — Client ID | Structural overlap with verify-001 | Pivot to corporate entity verification scenario | low |
| pr-13-discrim-002 | B | PR — Marketing | Duplicates discrim-001 without differentiation | Test expertise-refusal exception as judgment trap | medium |

---

## Narrative: Most Impactful Items

### Top REWRITE priorities (cross-exam)

**pub-03-baker-fair-001 (Exam C)** is the highest-impact REWRITE in the mixed exam pool. Procedural fairness is a high-frequency topic on the Barrister exam and this question functions as a caption, not a scenario. A well-constructed replacement with competing Baker factors across a single fact pattern would add genuine exam-level discriminatory value and address a visible weakness in Exam C's public law chapter.

**pub-04-delay-001 (Exam E)** and **pub-05-sppa-app-001 / pub-05-sppa-sub-001 (Exam E)** are three SPPA questions where anti-index=2 — the clearest rubric-level signal for immediate rewrite. These three questions together account for the weakest pocket in the entire Exam E question pool. Replacing them with application-driven SPPA questions would materially improve Exam E's PASS rate and address its most cited weakness.

**civ-15-noting-002 (Exam F)** and **crim-11-sum-sent-001 (Exam F)** are single-fact lookups that have no discriminatory function. Both are fast rewrites (low content complexity) and would reduce the single largest weakness in Exam F.

**pr-04-wit-001 and pr-03-govt-001 (PR Bank)** are the two highest-priority PR REWRITE items because both topics — lawyer-as-witness conflict and government lawyer confidentiality — are recognised LSO exam subjects where the bank has zero strong questions. These represent genuine content gaps alongside quality gaps.

### Top IMPROVE priorities (cross-exam)

The 38% IMPROVE rate in Exam E Family Law (ch02) is the most concentrated quality weakness across all five audits. The four divorce procedure questions (fam-02-divorce-bar-002, fam-02-divorce-grd-001, fam-02-jurisdiction-001, fam-02-petition-001) are all medium-difficulty procedural checklists. Upgrading two of the four to application questions would move Exam E's family law PASS rate from 62% toward the 75%+ target.

The PR Bank's trust accounting chapter (ch06) has four IMPROVE items where the fix is consistently the same: add an Ethics Override Trap where a client instruction conflicts with a By-Law obligation. This is a fast, high-value improvement cycle because the question structures are sound and only the distractor set needs engineering.

---

*This backlog covers psychometric quality only. Legal accuracy of all questions remains subject to the legal QA process documented in the GENERATED_EXAM_HUMAN_REVIEW_FLAGS.md register. Priority 0 items must not be worked on until their legal flags are resolved by a qualified reviewer.*
