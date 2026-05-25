# Phase 2K-Improve-B1 — Generated Barrister E Improvement Log

**Date:** 2026-05-25  
**Scope:** All IMPROVE-status questions remaining in Generated Barrister E after Phase 2K-Improve-A  
**Total improved:** 35 questions across 4 subjects  
**Payload re-baked:** `bare` only (534,820 chars, was 483,992)  
**Validation:** 963 questions, 0 errors ✅  
**HTML validation:** all checks pass ✅  
**Overlap:** E∩C=0, E∩D=0, E∩F=0, C∪D∪E∪F=640 unique ✅  
**Imported payloads:** unchanged (bar=191,500, sol=242,816, mini=171,132, abp=189,540, bar2=237,360) ✅  
**C/D/F payloads:** unchanged (barc=393,248, bard=441,852, barf=501,116) ✅  
**PR payloads:** unchanged (prdra=293,132, prdrb=288,532, prb200=581,808) ✅

---

## Summary

| Subject | Questions improved | Correct answer changed |
|---|---|---|
| Civil Litigation | 3 | 0 |
| Criminal Law | 6 | 0 |
| Family Law | 12 | 0 |
| Public Law | 14 | 0 |
| **Total** | **35** | **0** |

All improvements: updated `fact_pattern`, `call_of_question`, `options`, `explanation`, `why_A/B/C/D_wrong`, `exam_trigger_words`, `tested_concepts`, `updated_at` = "2026-05-25". `validation_status` and `correct_answer` left unchanged on all questions.

---

## Civil Litigation (3 questions)

| question_id | file | correct_answer_changed | weakness_addressed | trap_types_added |
|---|---|---|---|---|
| civ-03-strike-002 | ch03-pleadings.json | No | Distractor set was predictable for r.25.11 strike motions | Premature Escalation Trap (r.20.04 SJ before pleadings close), Wrong Procedure Trap (r.26.01 amendment-first), Misapplied Tool |
| civ-11-trial-proc-001 | ch11-trial.json | No | Trial procedure was sequential recall; defendant's documentary-evidence motion added to force application | Overstatement Trap (absolute judicial discretion), General Rule Trap (defendant presents first as inversion trap), Wrong Procedure Trap |
| civ-13-notice-app-001 | ch13-appeals.json | No | Timing was mechanical; new entry-date vs order-date distinction engineering | Wrong Timeline Trap ×3 (entry date April 16 vs order date April 1; non-existent 15-day period; wrong 60-day period) |

### Per-question detail

**civ-03-strike-002**
- Fact pattern enriched to commercial lease dispute with three specific irrelevant criminal-conduct paragraphs in the defence
- Call reframed to ask which rule and remedy "most precisely addresses" the defect — forcing rule + procedure selection
- Option C replaced with r.20.04 summary judgment (Premature Escalation Trap); Option D recast as r.26.01 amendment-first (Wrong Procedure Trap)
- Explanation distinguishes r.25.11 surgical partial strike from r.21.01 whole-pleading strike

**civ-11-trial-proc-001**
- Added Bergman's specific motion to present first on documentary-evidence grounds
- Call requires both identifying who goes first AND whether judge may accede to motion
- Difficulty upgraded easy→medium reflecting added analytical demand
- Explanation explains why Bergman's rationale fails: inverts burden-of-proof dynamics

**civ-13-notice-app-001**
- New precise date-tracking scenario: judgment April 1, order entered April 16, notice filed May 14
- Candidates must identify which date starts the 30-day clock (order date, not entry date)
- Options A/B/D rebuilt as Wrong Timeline Traps: entry-date (April 16), 15-day (non-existent), 60-day (wrong)
- Explanation explicitly names the entry-date trap as the most common wrong-calendar error

---

## Criminal Law (6 questions)

| question_id | file | correct_answer_changed | weakness_addressed | trap_types_added |
|---|---|---|---|---|
| crim-07-biz-rec-001 | ch07-evidence.json | No | Business records exception was recall-based; regularity-of-keeping element now genuinely contested | Understatement Trap (denies s.30 timing requirement), General Rule Trap (electronic records excluded) |
| crim-07-prior-consist-002 | ch07-evidence.json | No | Fabrication-allegation vs recent-complaint exceptions required factual differentiation | Exception Trap (recent complaint — wrong exception), Misapplied Tool (principled hearsay), General Rule Trap (blanket admissibility) |
| crim-09-consec-001 | ch09-sentencing.json | No | Consecutive/concurrent rule was mechanical; totality cap now applied to three-victim 9-year total | Misapplied Tool (parity principle), Overstatement Trap (restraint principle), Understatement Trap (proportionality alone) |
| crim-09-disc-001 | ch09-sentencing.json | No | Discharge eligibility was recall; hybrid offence prosecuted by indictment now forces threshold analysis | Wrong Procedure Trap (discharge unavailable on indictment), General Rule Trap (categorical bar for violence), Overstatement Trap (clean-record requirement + Crown consent) |
| crim-10-conf-001 | ch10-ycja.json | No | Confession rule scenario repurposed to YCJA s.146 operating mind; 14-year-old with intellectual disability creates subjective-vs-objective tension | Understatement Trap (voluntariness only), Premature Escalation Trap (waiver satisfies all), Misapplied Tool (judicial pre-authorization) |
| crim-11-ind-app-001 | ch11-appeals.json | No | Generic jury-trial appeal routing converted to judge-alone Superior Court conviction; mode of trial does not expand fact grounds | Wrong Forum Trap ×2 (Ontario Court of Justice; Divisional Court), Overstatement Trap (full fact appeal as of right for judge-alone) |

### Per-question detail

**crim-07-biz-rec-001**
- Replaced generic bank logs with brokerage spreadsheets prepared weeks after month-end due to staff shortages — places regularity-of-keeping condition in issue
- Option D replaced: incorrect claim that s.30 has no timing requirement (Understatement Trap)

**crim-07-prior-consist-002**
- Entirely new sexual assault trial scenario: defence alleges fabrication after counselling, Crown seeks to admit text sent morning after assault
- Crown expressly disclaims recent complaint — forces fabrication-rebuttal vs recent-complaint distinction

**crim-09-consec-001**
- 3 separate robbery victims, 3×3-year sentences proposed = 9-year total; first-time offender with substance-abuse disorder
- Totality s.718.2(c) arithmetic step-back requirement now decisive

**crim-09-disc-001**
- s.267(b) assault causing bodily harm (hybrid, tried by indictment, 10-year max, no minimum) — borderline eligibility
- Mode of trial shown to be irrelevant to discharge eligibility threshold

**crim-10-conf-001**
- Topic changed from YCJA conferencing to YCJA s.146 statements / operating mind (directly responsive to audit recommendation)
- 14-year-old with intellectual disability functioning at ~10-year level; police waiver by nodding; psychologist testimony on comprehension
- Source reference updated to include R. v. L.T.H., 2008 SCC 49; difficulty raised medium→hard

**crim-11-ind-app-001**
- Straight indictable theft over $5,000 tried by judge alone in Superior Court
- Correct court is Court of Appeal for Ontario; leave requirement for fact questions applies regardless of mode of trial

---

## Family Law (12 questions)

| question_id | file | correct_answer_changed | weakness_addressed | trap_types_added |
|---|---|---|---|---|
| fam-02-divorce-grd-001 | ch02-divorce.json | No | Grounds were recall; 60-day reconciliation attempt added to force DA s.8(3) 90-day exception | General Rule Trap (any resumption restarts clock), Misapplied Tool, Wrong Procedure Trap |
| fam-02-petition-001 | ch02-divorce.json | No | Petition requirements were recall; DA s.21.1 barriers-to-remarriage affidavit added | Pragmatic Bluff (separation agreement alone suffices), Wrong Procedure Trap, Wrong Timeline/Exception Trap |
| fam-05-non-comp-001 | ch05-spousal-support.json | No | Non-compensatory entitlement was definitional; hybrid Moge + Bracklow scenario requires simultaneous application | Overstatement Trap (must elect single ground), Exception Trap (only non-comp applies), Misapplied Tool (election doctrine) |
| fam-06-adult-child-001 | ch06-child-support.json | No | Adult child rule was recall; father's termination motion at 18 + mother's cross-motion for actual expenses added | General Rule Trap ×2 (terminates at 18; mandatory table amount for all ages), Understatement Trap ($1,000/month cap) |
| fam-06-cs-s7-002 | ch06-child-support.json | No | s.7 formula was mechanical; $600 bursary deduction step added requiring correct FCSG s.7(2) sequencing | General Rule Trap (50/50 split), Wrong Sequencing Trap (ignores bursary deduction), Overstatement Trap (higher earner solely responsible) |
| fam-07-grandpar-001 | ch07-parenting.json | No | CLRA/DA forum distinction was not tested; mother raises both no-standing and wrong-statute arguments | Wrong Forum Trap (DA s.16.1(2) only), Overstatement Trap (automatic right), Exception Trap (standing limited to parental death/incapacity) |
| fam-07-interim-001 | ch07-parenting.json | No | Status quo principle was soft-rule recall; Philip's no-court-order argument and DA s.16(1)/(3) references added | General Rule Trap (no order = no status quo), Overstatement Trap (equal time presumed), Misapplied Tool (status quo = marriage breakdown date) |
| fam-07-superv-access-001 | ch07-parenting.json | No | Supervised access distractors were predictable; "active harm" red herring and DA s.17(5) reference added | Misapplied Tool + Overstatement (active harm required), General Rule Trap (no material change threshold), Wrong Procedure Trap (consent required) |
| fam-09-setting-001 | ch09-domestic-contracts.json | No | Domestic contract type distinction was index-like; Eleanor's mislabelled post-separation document creates concrete consequence | Exception Trap (FLA Part IV contracts interchangeable), Overstatement Trap (marriage contract invalid post-separation), Pragmatic Bluff (labels legally irrelevant) |
| fam-10-inter-prov-001 | ch10-fro.json | No | ISO Act existence was enough; conflict-between-orders scenario now requires ISO Act coordination process | General Rule Trap (most recent order prevails), Overstatement Trap ×2 (Ontario always prevails; orders additive) |
| fam-10-reg-susp-001 | ch10-fro.json | No | Corporate veil was undeveloped; corporate registration suspension now explicit General Rule Trap; s.34/s.35/s.37 tools distinguished | General Rule Trap (corporate assets fully exempt), Understatement Trap (driver's licence only), Wrong Procedure Trap (suspension exhausts all action) |
| fam-13-cl-def-001 | ch13-common-law.json | No | "3 years OR parenthood" disjunction was underexploited; 2y7m cohabitation + child born during relationship forces parenthood arm | General Rule Trap (2y7m fails — misses parenthood arm), Wrong Timeline Trap (5-year requirement), Overstatement Trap (any cohabitation qualifies) |

---

## Public Law (14 questions)

| question_id | file | correct_answer_changed | weakness_addressed | trap_types_added |
|---|---|---|---|---|
| pub-01-double-asp-001 | ch01-division-of-powers.json | No | Double aspect was conceptual recall; Ontario/federal replica firearms statute conflict forces actual characterization | General Rule Trap (paramountcy only), Overstatement Trap (provincial law automatically void) |
| pub-01-s92-13-001 | ch01-division-of-powers.json | No | s.92(13) vs s.91(2) distinction was weak; IJI vital-core analysis now required for federally incorporated insurer | Overstatement Trap (complete immunity), Misapplied Tool (IJI displaces paramountcy entirely), Wrong Threshold Trap (paramountcy requires identical provisions) |
| pub-02-s10a-001 | ch02-charter.json | No | Rule-statement; lawful detention + partial reasons scenario added | Understatement Trap (statutory citation alone satisfies s.10(a)), General Rule Trap (lawful detention = full compliance) |
| pub-02-s12-001 | ch02-charter.json | No | Reasonable hypothetical not tested; 19-year-old student as hypothetical on mandatory minimum facts added | General Rule Trap (actual offender only), Overstatement Trap (any minimum unconstitutional), Pragmatic Bluff (parliamentary deference) |
| pub-02-s28-001 | ch02-charter.json | No | s.28 was recall; physical fitness standard with 72% male / 38% female pass rate adds s.28 as interpretive lens on s.15 threshold | Overstatement Trap (standalone right), Understatement Trap (s.28 irrelevant to s.15), Wrong Procedure Trap (s.28 goes to Oakes, not threshold) |
| pub-02-s33-001 | ch02-charter.json | No | Which rights survive s.33 was recall; Amara's challenge under ss.3, 6, s.28 forces three-way analysis | Overstatement Trap (s.33 overrides all Charter rights), Wrong Threshold Trap (s.28 as free-standing right), Misapplied Tool (s.33 override cures s.15 argument) |
| pub-03-delegation-001 | ch03-admin-law.json | No | Sub-delegation was direct; partial statutory authorization (panels expressly authorized, non-member staff not) added | General Rule Trap (express authorization = all sub-delegation permitted), Pragmatic Bluff (efficiency justifies extension), Overstatement Trap (any sub-delegation invalid) |
| pub-03-reasons-003 | ch03-admin-law.json | No | Baker factors were clear-cut; SPPA inapplicability and Commissioner-only proposal as distractor added | Understatement Trap (no Baker duty exists), Overstatement Trap (full hearing required), Wrong Procedure Trap (SPPA s.17 statutory right confused with Baker) |
| pub-04-mootness-001 | ch04-judicial-review.json | No | Bilateral-agreement distractor was weak; full Borowski stage-two factor weighing now required (adversarial, scarce resources, guidance value) | General Rule Trap (moot = no discretion), Overstatement Trap (public importance alone sufficient), Wrong Procedure Trap (remedy only, not hearing) |
| pub-04-record-001 | ch04-judicial-review.json | No | Exception rule was recall; de novo review Misapplied Tool trap added for statutory rights; ex parte emails admissibility tested | Misapplied Tool ×2 (de novo for statutory rights; certified record is complete), Overstatement Trap (full discovery equivalent) |
| pub-04-standing-001 | ch04-judicial-review.json | No | Automatic-standing distractor was weak; genuine-stake nuance and no-other-willing-party scenario added | Overstatement Trap ×2 (automatic standing; test met without genuine stake), Wrong Procedure Trap (standing collapses into merits) |
| pub-06-pipeda-breach-001 | ch06-privacy.json | No | Distractor A (no obligation) was obviously wrong; replaced with Commissioner-only vs dual notification distinction | General Rule Trap (Commissioner-only notification satisfies obligation), Understatement Trap (30-day delay acceptable), Wrong Threshold Trap (data volume determines obligation) |
| pub-07-vic-liab-001 | ch07-crown-liability.json | No | Frolic Exception Trap was underdeveloped; 40-min personal errand detour forces frolic doctrine limits and resumption rule | Misapplied Tool (Crown can never be liable for personal acts), Exception Trap / Wrong Threshold (frolic continues on return leg), Overstatement Trap (frolic = blanket immunity) |
| pub-08-prima-facie-001 | ch08-human-rights.json | No | Prima facie was definitional; multi-causal Indigenous identity composite-scoring scenario tests Moore "contributing factor" standard | General Rule Trap (dominant cause required), Pragmatic Bluff (facially neutral = no discrimination), Overstatement Trap (any connection = prima facie) |

---

## Post-Improvement Pipeline

| Step | Result |
|---|---|
| `python3 tools/validate_question.py data/questions --summary` | 963 questions, 0 errors ✅ |
| Rebuild `bare` compact JSON from manifest IDs | 160 questions, 43/43/39/35 ✅ |
| Re-bake `bare` payload in index.html | 483,992 → 534,820 chars ✅ |
| `python3 tools/validate_html.py` | All checks pass ✅ |
| E∩C = 0 | ✅ |
| E∩D = 0 | ✅ |
| E∩F = 0 | ✅ |
| C∪D∪E∪F = 640 unique IDs | ✅ |
| Imported payloads unchanged (bar/sol/mini/abp/bar2) | ✅ |
| C/D/F payloads unchanged (barc/bard/barf) | ✅ |
| PR payloads unchanged (prdra/prdrb/prb200) | ✅ |
