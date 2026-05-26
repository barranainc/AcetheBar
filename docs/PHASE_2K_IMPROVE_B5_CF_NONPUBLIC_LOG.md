# Phase 2K-Improve-B5 — Generated Barrister C & F Non-Public IMPROVE Log

**Date:** 2026-05-25  
**Scope:** All non-Public IMPROVE questions in Generated Barrister C and F  
**Files modified:** 10 question chapter files, index.html  
**Questions improved:** 27 (13 in C, 14 in F)  
**Correct answers changed:** 1 (civ-02-basic-lim-001: A → B, justified by fact-pattern redesign)  
**Validation:** 963 questions, 0 errors, ✅ all pass  
**Payloads rebuilt:** barc (398,740 → 413,636 b64 chars), barf (506,124 → 513,328 b64 chars)  
**Integrity:** C=160, F=160, C∩F=0, C∪D∪E∪F=640, all other payloads unchanged  

---

## Summary by Subject

| Subject | Exam C | Exam F | Total |
|---------|--------|--------|-------|
| Civil Litigation | 4 | 6 | 10 |
| Criminal Law | 4 | 5 | 9 |
| Family Law | 5 | 3 | 8 |
| **Total** | **13** | **14** | **27** |

---

## Exam C Improvements (13 questions)

### civ-02-basic-lim-001 — Civil Limitations
**Weakness:** FP stated "(assuming discovered on date of fall)" — removes all discoverability analysis; arithmetic-only; anti_idx=2.  
**Fix:** Redesigned with delayed-discovery scenario. Takeshi slips March 10, 2023 but attributes soreness to gym workout; diagnosed with torn meniscus September 15, 2024. Discovery occurs at diagnosis, not at incident.  
**Correct answer changed:** A → B (September 15, 2026 — two years from discovery)  
**Traps added:**
- **Incident-Date Trap** (A): limitation period runs from incident not discovery  
- **One-Year Trap** (C): wrong period length applied to correct discovery date  
- **No-Limitation-Period Trap** (D): latent injury eliminates period entirely (wrong)  
**Core teaching:** s.5 Limitations Act — discovery = knew/ought to know act, loss, causation, identity

---

### civ-06-injunction-004 — Civil Injunctions (RJR-MacDonald)
**Weakness:** FP told candidates both first stages pass then asked "what stage is next" — no application of balance-of-convenience factors.  
**Fix:** FP enriched with competing quantified harm ($4M defendant loss + plaintiff's undertaking as to damages); call asks how court applies third RJR-MacDonald branch.  
**Correct answer:** C (unchanged)  
**Traps added:**
- **Quantifiability-Determines-Balance Trap** (A): precise quantification automatically tips balance toward discharge  
- **First-Two-Elements Presumption Trap** (B): satisfying first two branches creates irrebuttable presumption  
- **Monetizable-Harm-Negates-Injunction Trap** (D): quantifiable harm re-engages irreparable harm analysis  
**Core teaching:** RJR-MacDonald third branch — holistic weighing; undertaking as to damages is a factor; equal balance favours status quo

---

### civ-07-summ-judg-005 — Civil Summary Judgment (Hryniak)
**Weakness:** Defendant's "always require trial" argument too obviously the pre-Hryniak rule; no applied scenario.  
**Fix:** FP redesigned — motion judge directed video cross-examinations under r.20.04(2.1), then made credibility findings; defendant argues motion judges can never assess credibility even after conducting cross-examinations.  
**Correct answer:** B (unchanged)  
**Traps added:**
- **Powers-Are-Limited-to-Evidence Trap** (A): r.20.04(2.1) authorizes evidence-reception only, not credibility assessment  
- **Confrontation-Rights-in-Civil-Proceedings Trap** (C): constitutional right to confront witnesses in person (criminal law concept misapplied)  
- **Waiver-Cures-Jurisdiction Trap** (D): participation without objecting creates the authority  
**Core teaching:** Hryniak + r.20.04(2.1) give motion judges full credibility-assessment power where not unjust

---

### civ-09-ref-und-005 — Civil Discovery (Compel Refusals)
**Weakness:** "Fourteen months" + context gave away answer as "unreasonable"; distractor B invented non-existent 60-day rule.  
**Fix:** FP enriched with procedural history (undertakings answered 9 months ago, documentary discovery complete, trial date set); removed editorial framing; replaced invented-rule distractor with more plausible 90-day deemed-deadline trap.  
**Correct answer:** C (unchanged)  
**Traps added:**
- **Discovery-Never-Closes Trap** (A): no time limit exists at all  
- Replaced 60-day distractor with **invented-90-day-deadline Trap** (B)  
- **Fresh-Examination-Required Trap** (D): must obtain new examination order once undertakings answered  
**Core teaching:** No absolute deadline to compel discovery refusals; reasonable-time requirement; late motion risks dismissal or adverse costs

---

### crim-02-s10b-001 — Criminal Charter s.10(b)
**Weakness:** Single fact (questions before informing of right to counsel) made answer mechanical; informational/implementational taxonomy stated directly.  
**Fix:** FP enriched — officer also failed to state reason for arrest (s.10(a)) AND started questioning without informing of s.10(b). Call asks which right was "most precisely and directly" violated by questioning without counsel information.  
**Correct answer:** B (unchanged — s.10(b) is the most precisely applicable right)  
**Traps added:**
- **s.10(a)-vs-s.10(b) Trap** (A): s.10(a) was also violated (failure to state reason) but it is not the right most directly on point for the questioning conduct  
- **s.7-Catch-All Trap** (C): s.7 is residual when a more specific right directly applies  
- **s.11(c)-Testimonial-Compulsion Trap** (D): s.11(c) protects against being put on witness stand at trial, not pre-trial questioning  
**Core teaching:** s.10(b) informational duty (tell of right) and implementational duty (hold off questioning); distinguish from adjacent Charter rights

---

### crim-02-sita-004 — Criminal Charter SITA (Fearon)
**Weakness:** Distractor B ("phone was unlocked, removing privacy expectation") too obviously wrong.  
**Fix:** Replaced B with a sophisticated Post-Hoc-Rationalization Trap — police claim the shoplifting involved photographing store products on phone so phone was "related to the offence."  
**Correct answer:** C (unchanged)  
**Trap replaced:**
- Old B (unlocked phone) → **Post-Hoc-Rationalization Trap** (B): relatedness must be genuine and assessed contemporaneously, not constructed retrospectively after station-house full data review  
**Core teaching:** Fearon SITA requirements — prompt, limited, truly incidental to arrest; relatedness is assessed at time of search not post-hoc

---

### crim-02-cit-arrest-003 — Criminal Citizen Arrest (s.494)
**Weakness:** Distractor D (unlimited time, good faith) too obviously wrong.  
**Fix:** Replaced D with Voluntary-Settlement-Authority Trap — citizen may detain until suspect agrees to compensate the victim.  
**Correct answer:** B (unchanged)  
**Trap replaced:**
- Old D (unlimited good-faith authority) → **Voluntary-Settlement-Authority Trap** (D): s.494 authorizes arrest then mandatory delivery to police; it does not authorize detention for private dispute resolution  
**Core teaching:** s.494(3) mandatory delivery forthwith; citizen arrest authority does not extend to coercive private negotiation

---

### crim-03-rev-onus-001 — Criminal Bail (Reverse Onus)
**Weakness:** CDSA s.5(1) trafficking too obviously a listed offence; distractor D ("all serious charges") too obviously wrong.  
**Fix:** Redesigned — Fatima charged with s.5(2) CDSA (possession for purpose of trafficking), not s.5(1) trafficking per se; defence counsel argues s.515(6)(d) covers only s.5(1). Tests whether s.515(6)(d) extends to s.5(2).  
**Correct answer:** B (unchanged — yes, s.515(6)(d) covers all of s.5 CDSA including s.5(2))  
**Traps added:**
- Dropped constitutional challenge distractor → **s.515(6)-Constitutionality Trap** (A): crown's reverse onus argued to violate s.11(e) Charter (incorrect — upheld in Pearson/Morales)  
- **Possession-vs-Trafficking Trap** (C): s.515(6)(d) covers "an offence under s.5" which includes s.5(2) — not only trafficking per se  
- **All-Serious-Charges Trap** (D): reverse onus applies to enumerated offences only, not all serious charges  
**Core teaching:** s.515(6)(d) applies to any s.5 CDSA offence (ss.5(1) and 5(2)); constitutional validity established

---

### fam-03-nfp-formula-001 — Family NFP Formula
**Weakness:** Pure arithmetic drill; all distractors were arithmetic errors.  
**Fix:** FP adds $20,000 gift received during marriage (included in $300,000 assets). Distractor D redesigned as Inherited-Property-Auto-Exclusion Trap — the gift is automatically excluded as FLA s.4(2) property. (It is not — exclusion must be asserted and proven.)  
**Correct answer:** C (unchanged — $170,000)  
**Trap added:**
- Replaced arithmetic distractor D → **Inherited-Property-Auto-Exclusion Trap** (D): gift/inheritance during marriage auto-deducted from NFP; FLA s.4(2) exclusion is not automatic  
**Core teaching:** FLA s.4(1) formula; FLA s.4(2) excluded property (gifts/inheritances) requires claim and proof — not automatic

---

### fam-03-equal-paymnt-001 — Family NFP Equalization Payment
**Weakness:** All numbers given directly; distractors were arithmetic errors.  
**Fix:** Replaced distractor C (equal property division misstatement) with S.5(6)-Available-Without-Facts Trap — court can reduce equalization below $120,000 under s.5(6) unconscionability even on these plain facts.  
**Correct answer:** B (unchanged — $120,000)  
**Trap added:**
- **S.5(6)-Available-Without-Facts Trap** (C): s.5(6) variation available without specific unconscionability facts  
**Core teaching:** FLA s.5(1) — one-half the difference; s.5(6) unconscionability variation is exceptional and fact-specific, not discretionary on clean facts

---

### fam-04-mh-possess-001 — Family Matrimonial Home Possession (s.19)
**Weakness:** s.19(1) stated as pure general rule with no competing factor; no multiple-property complexity.  
**Fix:** FP redesigned with two properties (Toronto home + Muskoka cottage); husband argues cottage is the "real" matrimonial home so Toronto home is excluded. Tests multiple-matrimonial-home rule.  
**Correct answer:** B (unchanged — s.19(1) equal possession regardless of ownership)  
**Traps added:**
- **Ownership-Determines-Possession Trap** (A): only titled spouse has possession rights  
- **Multiple-Residence Trap** (C): only one property can be the matrimonial home — cottage designation excludes Toronto home  
- **Primary-Residence-Required Trap** (C): must be "primary" or "preferred" residence to qualify as MH  
- **Financial-Contribution Trap** (D): possession right depends on mortgage contribution  
**Core teaching:** FLA s.18 — multiple properties can simultaneously be matrimonial homes; ordinary occupation as family residence suffices; s.19(1) possession is independent of ownership

---

### fam-04-excl-possess-001 — Family Exclusive Possession (s.24)
**Weakness:** "Can the court grant?" obviously yes; s.24(3) factors not tested.  
**Fix:** Call redesigned to ask how court applies s.24(3) factors on these facts (children's school proximity, Bernard's alternative accommodation, absence of violence). Tests multi-factor balancing, not binary power question.  
**Correct answer:** B (unchanged — courts weigh s.24(3) factors; violence is factor not precondition)  
**Traps added:**
- **Violence-Prerequisite Trap** (A): violence required before any exclusive possession order  
- **Ownership-Override Trap** (C): Bernard's ownership status significantly weighs against order; exclusive possession limited to violence/safety situations  
- **Interim-Bars-Order Trap** (D): only available as part of final parenting order, not interim motion  
**Core teaching:** FLA s.24(1) power regardless of ownership; s.24(3) factors — best interests of children, alternative accommodation, violence (as one factor), financial position; available on interim motion

---

### fam-05-ssag-001 — Family SSAG Advisory Status
**Weakness:** SSAG advisory status reachable by knowing one phrase; binary_logic=2; scenario abstract.  
**Fix:** FP enriched — SSAG range calculated; judge awards below the low end citing Patricia's failure to pursue economic self-sufficiency; Colin argues bound by SSAG; Patricia's counsel argues departure requires mandatory written reasons.  
**Correct answer:** B (unchanged — SSAG advisory; court may depart; no mandatory written-reasons obligation)  
**Traps added/replaced:**
- **SSAG-Binding-on-Departure Trap** (A): binding and cannot award below low end  
- **SSAG-Departure-Requires-Written-Reasons Trap** (C): replaced "binding in Superior Court" with mandatory-written-reasons-for-departure rule (overstates the obligation)  
- **SSAG-Replaces-Entitlement Trap** (D): non-zero SSAG result = entitlement established  
**Core teaching:** SSAG advisory — no statutory authority; departure permitted; self-sufficiency basis for below-range award; general reasons duty applies, not SSAG-specific mandatory reasons

---

## Exam F Improvements (14 questions)

### civ-03-soc-form-001 — Civil Pleadings (r.14.03 Endorsement)
**Weakness:** Pure recall of r.14.03 requirement; no applied judgment.  
**Fix:** Redesigned as applied scenario — lawyer's endorsement includes: (i) nature of claim, (ii) relief sought, and (iii) two-page evidence narrative. Ask whether this complies with r.14.03.  
**Correct answer:** B (unchanged — non-compliant; evidence narrative improper in endorsement)  
**Traps added:**
- **Comprehensive-Endorsement Trap** (A): r.14.03 requires comprehensive statement of facts and evidence  
- **Witness-List Trap** (C): endorsement must include names of proposed witnesses  
- **Nullity-Overstatement Trap** (D): excess content in endorsement renders entire claim a nullity  
**Core teaching:** r.14.03 — concise statement of nature of claim and relief sought; evidence does not belong in endorsement; defects correctable by amendment, not nullity

---

### civ-11-ev-003 — Civil Trial Evidence (Demonstrative Evidence)
**Weakness:** Rule-recall; distractor D ("always inadmissible as self-serving") too obviously wrong.  
**Fix:** FP enriched with specific opposing objections: (1) hearsay, (2) prejudice, (3) one-sided reconstruction. Call asks which objection, if any, could succeed.  
**Correct answer:** B (unchanged — admissible if relevant, fair, accurate, probative value not substantially outweighed)  
**Traps added/replaced:**
- **Hearsay-of-Demonstrative Trap** (A): animation is out-of-court statement → hearsay rule  
- **Prejudice-Equals-Exclusion Trap** (C): civil trials require neutral demonstrative evidence  
- **Consent-Required-for-Demonstrations Trap** (D): replaced "always inadmissible" with "requires opposing consent"  
**Core teaching:** Demonstrative evidence not hearsay; prejudice that is persuasive and relevant is not "unfair"; no consent requirement; foundational accuracy + expert available for cross-examination

---

### civ-12-repres-001 — Civil Costs (Self-Represented Litigants, Fong v. Chan)
**Weakness:** Distractor C ("full senior lawyer rate") too obviously wrong for prepared candidates.  
**Fix:** Replaced C with Partial-Indemnity-Equivalence Trap — costs at partial indemnity rate applicable to junior solicitor because courts treat self-represented party's time as equivalent to junior lawyer services.  
**Correct answer:** B (unchanged — reduced rate reflecting value of time and effort, not professional rate)  
**Trap replaced:**
- Old C (full senior rate) → **Partial-Indemnity-Equivalence Trap** (C): self-represented litigant recovers at junior solicitor partial indemnity rate  
**Core teaching:** Fong v. Chan — reduced rate reflecting actual value of self-represented party's time; not professional hourly rate

---

### civ-12-throwaway-001 — Civil Costs (Substantial Indemnity, r.57.01)
**Weakness:** Vocabulary-level question; distractor D incorrectly claimed only transactional misconduct grounds substantial indemnity.  
**Fix:** FP redesigned to litigation-conduct-only scenario (no transactional misconduct; deliberate document withholding, evasive discovery, abusive procedural motions). Tests whether litigation conduct alone suffices.  
**Correct answer:** B (unchanged — yes, r.57.01 discretion extends to reprehensible litigation conduct)  
**Traps added:**
- **Offer-to-Settle-Only Trap** (A): substantial indemnity only where offer beaten under r.49.10  
- **Personal-Order Trap** (C): substantial indemnity only as r.57.07 personal order against lawyer  
- **Litigation-Conduct-Only Trap** (D): inverts the rule — transactional misconduct required; litigation conduct only grounds contempt  
**Core teaching:** r.57.01 broad costs discretion; both transactional and litigation misconduct can ground substantial indemnity; r.49.10 offer is one trigger, not the only one

---

### civ-14-enf-garn-exam-001 — Civil Enforcement (Examination in Aid of Execution, r.60.18)
**Weakness:** Distractor A (re-issue notice only) and D (separate damages action) implausibly wrong.  
**Fix:** Replaced D with Production-Order-First Trap — must first obtain production order for financial records before examining officer.  
**Correct answer:** B (unchanged — contempt motion available directly)  
**Traps replaced:**
- Distractor A refined with **Notice-Has-No-Force Trap**: failure to attend first notice not a contempt; must re-issue  
- Old D (damages action) → **Production-Order-First Trap** (D): financial records must be obtained by separate production order before examination can proceed  
**Core teaching:** r.60.18 notice has force of court order; failure to attend = contempt; no prerequisite production order required; re-issuance not the only remedy

---

### civ-14-enf-repl-001 — Civil Enforcement (Writ of Delivery, r.60.10)
**Weakness:** Distractor D ("orders for personal property unenforceable in Ontario") implausibly wrong.  
**Fix:** Replaced D with Uniqueness-Required Trap — writ of delivery only available for truly unique, irreplaceable items; court may refuse if monetary award would suffice.  
**Correct answer:** B (unchanged — writ of delivery under r.60.10)  
**Trap replaced:**
- Old D (unenforceable) → **Uniqueness-Required Trap** (D): writ of delivery requires property to be irreplaceable; court may decline if monetary alternative exists  
**Core teaching:** r.60.10 writ of delivery available for any court order for recovery of specific personal property; no uniqueness requirement; monetary availability does not bar the writ

---

### crim-08-colour-right-001 — Criminal Defences (Colour of Right)
**Weakness:** FP (removing lumber as "collateral") abstract; trap types not named in explanation.  
**Fix:** FP redesigned — developer made oral promise to Nathan ("if I don't pay you by Friday, you can take the lumber"); Nathan relies on this promise. Tests whether oral promise can ground honest belief in legal entitlement.  
**Correct answer:** B (unchanged — honest belief in legal entitlement required; need not be legally valid)  
**Traps added:**
- **Valid-Security-Interest Trap** (A): must have registered lien or court order  
- **Moral-Claim Trap** (C): being owed money = recognized legal right to take property  
- **Premises-Restriction Trap** (D): colour of right limited to public land or land with lawful access  
**Core teaching:** Colour of right — subjective honest belief in legal entitlement; belief need not be correct in law; must be belief in legal right not merely moral grievance; oral promise may ground the belief

---

### crim-08-ncr-001 — Criminal Defences (NCR, s.16(1))
**Weakness:** "Alien invader" FP cartoonish/unrealistic; distractor D ("lacked motive") obviously wrong.  
**Fix:** FP redesigned — Raymond has paranoid schizophrenia causing him to believe neighbour was about to kill him; struck neighbour in delusional self-defence. Realistic paranoid schizophrenia scenario. Replaced motive distractor with NCR-vs-Self-Defence Trap.  
**Correct answer:** B (unchanged — s.16(1)(b) wrong prong; mental disorder rendered incapable of knowing act was wrong)  
**Traps replaced/added:**
- **Actus-Reus-Negation Trap** (A): mental disorder eliminated voluntary act  
- **Automatism-vs-NCR Trap** (C): automatism (involuntary bodily movement) conflated with NCR  
- Old D (motive) → **NCR-vs-Self-Defence Trap** (D): s.34 self-defence applies where belief was sincere; NCR unnecessary where justification defence exists  
**Core teaching:** NCR s.16(1)(b) — incapacity to know act was wrong; distinct from automatism; delusional self-defence belief cannot meet objective self-defence standard; NCR is the correct vehicle

---

### crim-09-rest-001 — Criminal Sentencing (Restorative Justice, s.718)
**Weakness:** Pure rule-recall identifying s.718(e) and (f); distractors don't test whether objectives are mutually exclusive.  
**Fix:** FP redesigned — Crown supports restorative component AND wants denunciation; defence argues denunciation incompatible with restorative justice. Tests whether s.718 objectives can coexist.  
**Correct answer:** B (unchanged — s.718 objectives are not mutually exclusive; denunciation and restoration can coexist)  
**Traps added:**
- **Mutually-Exclusive-Objectives Trap** (A): court cannot pursue both restorative and denunciatory objectives simultaneously  
- Invented **mandatory hierarchy** trap (C): denunciation must be addressed before restorative measures  
- **Restorative-Justice-Not-in-Code Trap** (D): restorative justice not a recognized sentencing objective  
**Core teaching:** s.718 objectives are non-exclusive; courts balance all relevant objectives; s.718(e) and (f) explicitly include restorative justice goals; denunciation and restoration may coexist

---

### crim-10-records-001 — Criminal YCJA (Youth Records)
**Weakness:** Distractor C ("automatically destroyed two years after sentence") too obviously invented.  
**Fix:** Replaced C with Sentence-Type-Confusion Trap — access period for all youth sentences is three years minimum, confusing reprimand (3-month) with conditional discharge (3-year) period.  
**Correct answer:** B (unchanged — access period for reprimand ends 3 months after pronouncement)  
**Trap replaced:**
- Old C (2-year destruction) → **Sentence-Type-Confusion Trap** (C): three-year access period for all youth sentences regardless of type  
**Core teaching:** YCJA s.119(2)(a) — reprimand access period = 3 months; different sentences have different access periods; conditional discharge = 3 years; indictable = 5 years after completion

---

### crim-11-prerog-001 — Criminal Appeals (Habeas Corpus)
**Weakness:** Definitional "is habeas corpus available?" binary call; no application to exhaustion or standard of review.  
**Fix:** Redesigned — Crown raises two arguments: (1) must exhaust internal CSC grievance process first; (2) Superior Court reviews on patent unreasonableness. Call asks whether both arguments are correct.  
**Correct answer:** C (unchanged — both arguments wrong)  
**Traps added:**
- **Exhaustion-Required Trap**: habeas corpus requires prior exhaustion of internal grievance mechanisms  
- **Deferential-Standard Trap**: Superior Court applies patent unreasonableness on habeas corpus  
- **No-Liberty-Deprivation Trap** (D): administrative segregation is not a deprivation of liberty because inmate already incarcerated  
**Core teaching:** Habeas corpus — no prior exhaustion requirement; independent standard of review (not patent unreasonableness); administrative segregation = distinct deprivation of residual liberty (Miller); Superior Court retains jurisdiction over federal inmates

---

### fam-07-parcoord-001 — Family Parenting Coordination
**Weakness:** Definitional "what does a PC do?" call; no application to when/how the process works.  
**Fix:** Redesigned as applied scenario — father wants to bypass PC on a scheduling dispute within the PC's mandate and go directly to court. Tests whether parties can bypass the court-ordered PC process.  
**Correct answer:** B (unchanged — complete PC process including determinative phase before returning to court)  
**Traps added:**
- **Escalation-Always-Available Trap** (A): parties may return to court at any time on any children's matter  
- **PC-Cannot-Decide-Parenting-Time Trap** (C): PC cannot make binding decisions affecting parenting time — only judges can  
- **Consensus-Required Trap** (D): PC's determination binding only if both parents agree; either may escalate if dissatisfied  
**Core teaching:** PC has hybrid facilitative/determinative role; mandate defines scope; parties must complete PC process (including determinative phase) before returning to court for in-mandate disputes; PC authority is binding, not consensual

---

### fam-13-cl-fla29-001 — Family Common Law Entitlement Grounds
**Weakness:** Definitional — "do common-law spouses get compensatory support?" with obvious answer; FP thin.  
**Fix:** FP enriched with specific economic disadvantage facts — Michelle gave up full-time career to manage household and work unpaid in Dan's business; concrete compensatory entitlement facts. Dan's counsel still argues compensatory support limited to Divorce Act. Tests entitlement grounds.  
**Correct answer:** B (unchanged — all three grounds available to FLA s.29 qualifying spouses)  
**Traps added/sharpened:**
- **Compensatory-Divorced-Spouses-Only Trap** (A): compensatory entitlement available only under Divorce Act for married spouses  
- **Always-Compensatory Trap** (C): common-law FLA claims are always compensatory only; needs-based not available  
- **Three-Year-Cap Trap** (D): compensatory support for common-law partners capped at three years  
**Core teaching:** FLA s.29 qualifying spouses assessed under FLA s.33 on same basis as married spouses; Bracklow compensatory/non-compensatory/contractual grounds all available; no cap on duration based on marital status alone

---

### fam-13-cl-supp-002 — Family Common Law SSAG Applicability
**Weakness:** Distractor C ("50% automatic reduction for common-law partners") implausibly wrong.  
**Fix:** Replaced C with Wrong-Formula-for-CL-Partners Trap — courts must apply only "without children" SSAG formula for common-law partners regardless of actual circumstances.  
**Correct answer:** B (unchanged — SSAG apply equally to FLA claims by qualifying common-law partners)  
**Trap replaced:**
- Old C (50% reduction) → **Wrong-Formula-for-CL-Partners Trap** (C): common-law claims use "without children" formula only; "with children" formula limited to Divorce Act married spouses  
**Core teaching:** SSAG apply to both Divorce Act and FLA qualifying common-law partner claims; formula selection based on actual circumstances (with/without children, custodial payor) not on marital status

---

## Payload Rebuild Summary

| Key | Before (b64 chars) | After (b64 chars) | Questions |
|-----|-------------------|-------------------|-----------|
| barc | ~398,740 | 413,636 | 160 |
| barf | ~506,124 | 513,328 | 160 |

All other payloads (bard, bare, prdra, prdrb, prb200, bar, bar2, sol, mini, abp) unchanged.

## Distractor Trap Types Introduced in Phase B5

**Civil Litigation (10 traps):**
- Incident-Date Trap, One-Year Trap, No-Limitation-Period Trap
- Quantifiability-Determines-Balance Trap, First-Two-Elements Presumption Trap, Monetizable-Harm-Negates-Injunction Trap
- Powers-Are-Limited-to-Evidence Trap, Confrontation-Rights-in-Civil-Proceedings Trap, Waiver-Cures-Jurisdiction Trap
- Discovery-Never-Closes Trap, Fresh-Examination-Required Trap
- Hearsay-of-Demonstrative Trap, Prejudice-Equals-Exclusion Trap, Consent-Required-for-Demonstrations Trap
- Partial-Indemnity-Equivalence Trap
- Offer-to-Settle-Only Trap, Personal-Order Trap, Litigation-Conduct-Only Trap
- Notice-Has-No-Force Trap, Production-Order-First Trap, Uniqueness-Required Trap
- Comprehensive-Endorsement Trap, Witness-List Trap, Nullity-Overstatement Trap

**Criminal Law (11 traps):**
- s.10(a)-vs-s.10(b) Trap, s.7-Catch-All Trap, s.11(c)-Testimonial-Compulsion Trap
- Post-Hoc-Rationalization Trap
- Voluntary-Settlement-Authority Trap
- Possession-vs-Trafficking Trap, All-Serious-Charges Trap
- Valid-Security-Interest Trap, Moral-Claim Trap, Premises-Restriction Trap
- NCR-vs-Self-Defence Trap, Automatism-vs-NCR Trap, Actus-Reus-Negation Trap
- Mutually-Exclusive-Objectives Trap
- Sentence-Type-Confusion Trap
- Exhaustion-Required Trap, Deferential-Standard Trap, No-Liberty-Deprivation Trap

**Family Law (10 traps):**
- Inherited-Property-Auto-Exclusion Trap
- S.5(6)-Available-Without-Facts Trap
- Multiple-Residence Trap, Primary-Residence-Required Trap, Financial-Contribution Trap, Ownership-Determines-Possession Trap
- Violence-Prerequisite Trap, Ownership-Override Trap, Interim-Bars-Order Trap
- SSAG-Departure-Requires-Written-Reasons Trap
- Escalation-Always-Available Trap, PC-Cannot-Decide-Parenting-Time Trap, Consensus-Required Trap
- Compensatory-Divorced-Spouses-Only Trap, Three-Year-Cap Trap
- Wrong-Formula-for-CL-Partners Trap
