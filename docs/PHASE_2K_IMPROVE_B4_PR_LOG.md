# Phase 2K-Improve-B4 — PR IMPROVE Resolution Log

**Phase:** 2K-Improve-B4  
**Date:** 2026-05-25  
**Scope:** All 26 identifiable PR IMPROVE candidates across Drill A, Drill B, and PR Bank 200  
**Source audit:** `docs/PSYCHOMETRIC_AUDIT_PR_DRILLS.md`  
**Constraint:** No new questions generated; no manifests changed; no non-PR questions touched; no imported exams modified; no Barrister C/D/E/F questions touched

---

## Summary

| Metric | Value |
|--------|-------|
| PR IMPROVE items targeted | 26 |
| Drill B items improved | 13 |
| Drill A items improved | 13 |
| Chapter files modified | 12 of 13 (ch10-undertakings not in scope) |
| Correct answers changed | 0 |
| New question IDs added | 0 |
| Question IDs removed | 0 |
| Manifest files changed | 0 |
| Validation errors (post-improvement) | 0 |
| HTML validation | PASS |
| A∩B | 0 (confirmed) |
| A∪B = Bank200 | true (confirmed) |

---

## Trap Taxonomy Applied

| Trap name | Questions affected |
|-----------|-------------------|
| LPP-Scope-Restriction Trap | pr-01-class-lic-001 |
| Mandatory-Mentorship Trap | pr-01-class-lic-001 |
| ILA-Cures-Scope Trap | pr-01-ins-001 |
| Informal-Consent / Passive-Non-Objection Trap | pr-01-cpd-002, pr-03-cloud-001 |
| Non-Practising-Status Trap | pr-01-cpd-002 |
| Retroactive-Status Trap | pr-01-cpd-002 |
| Understatement Trap (monthly reconciliation = supervision) | pr-02-superv-005 |
| Residual-Warning-Duty Trap | pr-02-scope-001 |
| Public-Domain Trap | pr-03-confid-scope-001 |
| Public-Record-Confirmation Trap | pr-03-post-ret-001 |
| Retroactive-Consent Trap | pr-03-tech-conf-003 |
| Information-Barrier Trap | pr-04-former-cl-003 |
| Consent-as-Cure Trap | pr-04-estate-001 |
| Contract-Governs Pragmatic Bluff | pr-05-cont-003 |
| Licensee-Status Trap | pr-05-ref-fee-002 |
| Work-Done Trap (intake work ≠ proportional fee) | pr-05-ref-fee-002 |
| Post-Retirement Audit Jurisdiction Trap | pr-06-audit-001 |
| Record-Custodian Transfer Trap | pr-06-audit-001 |
| Limitation-Period Trap | pr-06-audit-001 |
| Same-Day Transfer Exception Trap | pr-06-bylaw-002 |
| Amount-Threshold Trap ($5M mandatory specific account) | pr-06-bylaw-002 |
| Third-Party Escrow Trap | pr-06-bylaw-002 |
| Self-Remedy Ethics Override Trap | pr-06-report-001 |
| Wait-to-Be-Asked Trap | pr-07-auth-001 |
| Subjective-Belief Trap | pr-07-unmerit-001 |
| Client-Instruction-Override Trap | pr-08-discrim-001 |
| Unilateral-Withdrawal Trap | pr-09-subs-001 |
| Internal-Transfer Trap | pr-09-subs-001 |
| 30-Day Minimum Trap | pr-09-time-001 |
| Implied-Termination Trap | pr-09-time-001 |
| Court-Approval-for-Transactional Trap | pr-09-time-001 |
| Partial-Truth-Penalty Trap | pr-11-penalty-001 |
| Party-Agreement-Binds-Tribunal Trap | pr-11-penalty-002 |
| Consent-Order-as-Floor Trap | pr-11-penalty-002 |
| Consent-Order-Binding Trap | pr-11-penalty-002 |
| Video-Call-Sufficient Trap | pr-12-verify-001 |
| Private-Company-Only Trap | pr-12-verify-001 |
| In-Person-Required Trap | pr-12-verify-001 |
| ID-Only Trap | pr-12-verify-002 |
| Independent-Source Trap | pr-12-verify-002 |
| Internal-HR-Policy-Satisfies-Rule Trap | pr-13-discrim-002 |

---

## Per-Question Change Notes

### ch01-licensing.json

#### pr-01-class-lic-001 (Drill B)
**Weakness:** Distractors A (services listed on call certificate) and D (2-year supervision) were obviously wrong to any prepared candidate.  
**Fix:** Enriched FP to add LPP pathway context. New A = LPP restricts scope to placement area (LPP-Scope-Restriction Trap). New D = must work under supervision for 12 months post-call as mandatory LPP mentorship condition (Mandatory-Mentorship Trap).  
**Correct answer:** B (unchanged)

#### pr-01-ins-001 (Drill B)
**Weakness:** Distractor D (referral fee sharing) was tangential to the core scope-of-practice ethics point.  
**Fix:** New D = if client obtains ILA from a barrister, client consent cures scope restriction (ILA-Cures-Scope Trap). Forces candidates to recognise that statutory scope limits cannot be waived by client consent or ILA.  
**Correct answer:** C (unchanged)

#### pr-01-cpd-002 (Drill A)
**Weakness:** Scenario was thin; distractors did not convincingly mimic real misconceptions about CPD rules.  
**Fix:** Enriched FP to add LSO Gazette reading element. New A = part-time < 3 days = non-practising status exemption (Non-Practising-Status Trap). New B = reading LSO Gazette = informal CPD credit (Informal-CPD Trap). New D = retroactive non-practising conversion excuses CPD default (Retroactive-Status Trap).  
**Correct answer:** C (unchanged)

---

### ch02-competence.json

#### pr-02-superv-005 (Drill B)
**Weakness:** Old distractor A (legal assistant exercised independent judgment on administrative task) was an unconvincing excuse.  
**Fix:** New A = Xavier conducts monthly trust reconciliations = adequate ongoing supervision (Understatement Trap). Forces candidates to recognise that reviewing results monthly is not the same as maintaining required supervisory control over the professional decision itself.  
**Correct answer:** C (unchanged)

#### pr-02-scope-001 (Drill A)
**Weakness:** Old distractor D (limited-scope retainer valid in litigation only, not transactional) was obviously wrong.  
**Fix:** New D = residual professional duty to identify and enumerate all excluded advice in writing; failure to list exclusions = cannot rely on scope limitation (Residual-Warning-Duty Trap).  
**Correct answer:** B (unchanged)

---

### ch03-confidentiality.json

#### pr-03-confid-scope-001 (Drill A)
**Weakness:** All three wrong options were transparent; no genuine application demand.  
**Fix:** Enriched FP — the acquisition deal later appeared in an industry publication. New A = once information enters the public domain through press reporting, confidentiality obligation is extinguished for those facts (Public-Domain Trap). Forces candidates to understand that the lawyer's knowledge arose from privileged access, not from the public report.  
**Correct answer:** B (unchanged)

#### pr-03-post-ret-001 (Drill B)
**Weakness:** Old distractor D (may disclose matters already in public regulatory filings) was partially correct as stated — too close to a real exception.  
**Fix:** New D = confirming public-record regulatory filing details is not "disclosure" under Rule 3.3-1; confirmation ≠ disclosure (Public-Record-Confirmation Trap). The trap is overbroad — Rule 3.3-1 does not contain a public-record confirmation exception.  
**Correct answer:** C (unchanged)

#### pr-03-tech-conf-003 (Drill A)
**Weakness:** Only distractor A (not responsible for employee disclosures) was strong; D (shared computer is the violation) was too narrow.  
**Fix:** New D = retroactive written consent from affected clients eliminates professional discipline consequence (Retroactive-Consent Trap). Forces candidates to understand that retroactive consent does not cure a prior breach of the duty to maintain safeguards.  
**Correct answer:** C (unchanged)

#### pr-03-cloud-001 (Drill A)
**Weakness:** Old distractor B (educational or professional context = permitted) was weak — an obvious "no" to prepared candidates.  
**Fix:** New B = client mentioned at outset that Dario writes blog posts and did not object = implicit consent = complete defence (Informal-Consent / Passive-Non-Objection Trap). Forces candidates to distinguish active informed consent from passive silence.  
**Correct answer:** C (unchanged)

---

### ch04-conflicts.json

#### pr-04-estate-001 (Drill B)
**Weakness:** Scenario underspecified — the conflict was not concrete enough to require genuine analysis. Old distractor A (no conflict in estate planning) was thin.  
**Fix:** Enriched FP — Marcus is now also Deanna's current client (business matters) and actively participated in the will instructions meeting, suggesting possible undue influence. New A = conflict is fully resolved by written consent from both testator and beneficiary (Consent-as-Cure Trap). Forces candidates to recognise that consent alone cannot resolve an active undue influence concern.  
**Correct answer:** B (unchanged)

#### pr-04-former-cl-003 (Drill A)
**Weakness:** Old distractor D (no retainer = no professional obligations to Hartley whatsoever) was obviously wrong — an overstatement no prepared candidate would endorse.  
**Fix:** New D = no formal retainer = any conflict automatically cured by implementing firm-level information barrier (Information-Barrier Trap). Forces candidates to understand that: (1) an information barrier does not automatically cure a former-client conflict; (2) the threshold question is whether confidential information was received, not whether a barrier is in place.  
**Correct answer:** B (unchanged)

---

### ch05-duties.json

#### pr-05-cont-003 (Drill A)
**Weakness:** Old distractor A (contingency fee only on trial verdicts, not settlements) was obviously wrong — contingency fees on settlements are standard.  
**Fix:** New A = signed contingency agreement is binding; client understood terms; signed agreement cannot constitute professional misconduct (Contract-Governs Pragmatic Bluff). Forces candidates to recognise that Rules of Professional Conduct impose independent obligations that override even a signed, understood client agreement.  
**Correct answer:** B (unchanged)

#### pr-05-ref-fee-002 (Drill A)
**Weakness:** Original scenario (financial advisor non-licensee receiving flat fee) was a pure rule-lookup; no genuine application demand.  
**Fix:** Entirely new scenario — Nicolas is a licensed paralegal who conducts 15-minute intake consultations and receives $500 flat per referral; Hana does not disclose the arrangement to referred clients. New A = LSO-licensee status = categorically exempt from referral fee rules (Licensee-Status Trap). New C = actual intake work = proportional fee-sharing, not referral fee (Work-Done Trap). New D = only need a written inter-firm agreement, no client disclosure required (Written-Agreement Trap). B (correct) = two violations: flat fee tied to referral = referral fee regardless of licensee status; and failure to disclose to clients.  
**Correct answer:** B (unchanged)

---

### ch06-trust.json

#### pr-06-audit-001 (Drill B)
**Weakness:** Original scenario was simple rule-recall on audit authority (SCP does not protect trust records). No novel application demand.  
**Fix:** Entirely new post-retirement scenario. Tamara retired 18 months ago, transferred records to Bertrand, surrendered licence. LSO notifies her of audit. New A = retired and licence surrendered = LSO has no jurisdiction (Post-Retirement Jurisdiction Trap). New B = records transferred to Bertrand = audit obligation passed to Bertrand (Record-Custodian Transfer Trap). New D = more than 12 months = LSO audit jurisdiction expired (Limitation-Period Trap). C (correct) = Law Society Act preserves audit authority over former licensees.  
**Correct answer:** C (unchanged)

#### pr-06-bylaw-002 (Drill B)
**Weakness:** Near-index on By-Law 9 enumeration; no disputed application fact.  
**Fix:** Added morning-of-closing timing element. CFO asks whether funds can arrive 6 hours before closing (same-day transfer) and whether specific account is available. New A = commercial transactions over $1M = same-day transfer exception (Same-Day Transfer Exception Trap). New C = deposits over $5M = specific account mandatory (Amount-Threshold Trap). New D = third-party escrow arrangement satisfies By-Law 9 (Third-Party Escrow Trap). B (correct) = no holding period, no pre-funding requirement, specific account optional, client consent → interest to client.  
**Correct answer:** B (unchanged)

#### pr-06-report-001 (Drill B)
**Weakness:** No Ethics Override Trap in distractor set; all wrong options were implausible regulatory interpretations.  
**Fix:** New A = conducted thorough self-audit, found no irregularities; clean self-audit satisfies spirit of reporting requirement; no further filing needed (Self-Remedy Ethics Override Trap). Forces candidates to recognise that the LSO reporting obligation is mandatory and exists to serve external accountability, not just problem detection.  
**Correct answer:** C (unchanged)

---

### ch07-court-duties.json

#### pr-07-auth-001 (Drill A)
**Weakness:** Old distractor D (decision issued 3 weeks ago = too recent to be binding) was obviously wrong — recency does not affect bindingness.  
**Fix:** New D = duty of candour does not require proactive disclosure; Yasmine must respond accurately if the tribunal asks but has no affirmative duty to volunteer the information (Wait-to-Be-Asked Trap). Forces candidates to understand that Rule 5.1-2 candour is proactive and affirmative, not reactive.  
**Correct answer:** B (unchanged)

#### pr-07-unmerit-001 (Drill A)
**Weakness:** Old distractor A (zealous advocacy = raising all possible defences) was a broad framing that didn't demand precise analysis.  
**Fix:** New A = client provided signed statement expressing good-faith belief in each defence raised; lawyer may rely on client's sworn good-faith statement (Subjective-Belief Trap). Forces candidates to recognise that Rule 5.1-2's "without merit" standard is objective (assessed by the lawyer), not subjective (the client's belief).  
**Correct answer:** C (unchanged)

---

### ch08-opposing.json

#### pr-08-discrim-001 (Drill B)
**Weakness:** Scenario was abstract; no grounding tension that would make the prohibited conduct seem defensible to a poorly-prepared candidate.  
**Fix:** Enriched FP — Arnav's client shares the plaintiff's South Asian cultural background and specifically instructed Arnav to raise cultural factors as part of the defence strategy. New A = client shares cultural background + specific instruction = complete defence to discrimination allegation under Rule 6.3-1 (Client-Instruction-Override Trap). Forces candidates to apply the principle that client instruction does not authorise otherwise prohibited discriminatory conduct.  
**Correct answer:** B (unchanged)

---

### ch09-withdrawal.json

#### pr-09-subs-001 (Drill A)
**Weakness:** Old distractor A (Notice of Change of Solicitor = immediate unilateral withdrawal) was confused with the incoming solicitor's notice; old D (must stay until new lawyer files) was correct only in a narrow circumstance.  
**Fix:** New A = Notice of Withdrawal of Lawyer (Form 15B) filed unilaterally; civil matter requires no court motion; effective on filing (Unilateral-Withdrawal Trap). New D = internal firm transfer + filing Notice of Change of Solicitor on client's behalf without client's signature = satisfies obligation (Internal-Transfer Trap). Forces candidates to recognise: (a) unilateral withdrawal without client consent or court order is not available when on record with trial date; (b) the client must consent to any substitution.  
**Correct answer:** C (unchanged)

#### pr-09-time-001 (Drill A)
**Weakness:** Scenario was too mechanical (pure non-payment grounds check); no time-pressure or competing obligation tension.  
**Fix:** Enriched FP — shareholders agreement scheduled to be finalised in 3 days; client has not retained replacement counsel. New A = 3-day window = material prejudice; transactional withdrawal prohibited within 30 days of scheduled transaction date (30-Day Minimum Trap). New C = non-payment requests unanswered = implied termination; no formal notice required (Implied-Termination Trap). New D = transactional matter with scheduled date = court approval required (Court-Approval-for-Transactional Trap).  
**Correct answer:** B (unchanged)

---

### ch11-discipline.json

#### pr-11-penalty-001 (Drill B)
**Weakness:** Old distractor C (only reprimand and fine available; suspension/revocation requires Criminal Code conviction) was implausible — a prepared candidate would recognise this as fiction.  
**Fix:** New C = trust supervision order is the appropriate response for a first offence with full repayment; revocation requires prior disciplinary record or concurrent criminal finding (Partial-Truth-Penalty Trap). The trap contains a partially correct observation (supervision orders are available and repayment is mitigating) but incorrectly restricts revocation to cases with prior record or criminal conviction.  
**Correct answer:** B (unchanged)

#### pr-11-penalty-002 (Drill B)
**Weakness:** Structural overlap with penalty-001 (both testing the range of available penalties after a misconduct finding).  
**Fix:** Entirely new scenario — penalty hearing for trust accounting record-keeping failure; LSO and Prest jointly propose consent order (3-month suspension, 2-year trust restriction, $15K costs); Tribunal must decide. New A = both parties agreed = Tribunal obligated to accept; limited to confirming proper form (Party-Agreement-Binds-Tribunal Trap). New C = Tribunal may accept or increase suspension only; cannot reduce any element below the joint proposal floor (Consent-Order-as-Floor Trap). New D = signed consent order binding on Tribunal; disagreement → refer back to parties (Consent-Order-Binding Trap). B (correct) = Tribunal has independent authority to accept, reject, or modify joint penalty proposals.  
**Correct answer:** B (unchanged)

---

### ch12-client-id.json

#### pr-12-verify-001 (Drill A)
**Weakness:** Scenario lacked a specific remote verification method to evaluate; question was about the missing corporate existence check, but without a concrete individual verification method to contrast.  
**Fix:** Enriched FP — Gwen verifies Marcus's ID via secure portal upload AND conducts a live video call confirming ID matches Marcus's appearance. New A = photo ID upload + video call visual confirmation = adequate verification of Marcus and, through him, corporate client (Video-Call-Sufficient Trap). New C = registry searches only required for private companies or high-risk transactions (Private-Company-Only Trap). New D = real property acquisition requires in-person verification; remote methods insufficient (In-Person-Required Trap).  
**Correct answer:** B (unchanged)

#### pr-12-verify-002 (Drill B)
**Weakness:** Old distractor C (only required if Oscar attends the transaction in person) and D (must obtain statutory declaration) were both weak.  
**Fix:** New C = only identification (name, address, occupation) required for beneficial principal who is not a signatory; verification through government ID not required for non-signatory principals (ID-Only Trap). New D = Helen can satisfy verification of Oscar by requesting Nina to provide Oscar's ID, since Nina is her agent-client with direct access to Oscar (Independent-Source Trap).  
**Correct answer:** B (unchanged)

---

### ch13-marketing.json

#### pr-13-discrim-002 (Drill B)
**Weakness:** Old distractor D (Vance only required to act if Wren files a formal written LSO complaint) was obviously wrong — waiting for an LSO complaint is not a recognized standard for management obligations.  
**Fix:** New D = Vance has satisfied Rule 6.3-2 by directing Xavier to comply with the firm's internal anti-harassment policy and initiating the HR process; once internal process is engaged, Rule 6.3-2 imposes no additional obligations (Internal-HR-Policy-Satisfies-Rule Trap). Forces candidates to recognise that engaging an internal HR process does not discharge the independent professional management obligation under Rule 6.3-2.  
**Correct answer:** C (unchanged)

---

## Payload Rebuild Verification

| Payload | Questions | Base64 length | Rebuilt from manifest |
|---------|-----------|--------------|----------------------|
| prdra (Drill A) | 100 | 299,784 | generated-pr-drill-a-manifest.json |
| prdrb (Drill B) | 100 | 293,448 | generated-pr-drill-b-manifest.json |
| prb200 (Bank 200) | 200 | 593,376 | generated-pr-bank-200-manifest.json |

**Integrity checks:**
- A ∩ B = 0 ✅
- |A ∪ B| = 200 ✅
- A ∪ B == Bank200 ✅
- bar, barc, bard, bare, barf payloads unchanged ✅
- HTML validation: PASS ✅
- Question validator: 0 errors ✅

---

## Files Modified

| File | Changes |
|------|---------|
| `data/questions/professional-responsibility/ch01-licensing.json` | pr-01-class-lic-001, pr-01-ins-001, pr-01-cpd-002 |
| `data/questions/professional-responsibility/ch02-competence.json` | pr-02-superv-005, pr-02-scope-001 |
| `data/questions/professional-responsibility/ch03-confidentiality.json` | pr-03-confid-scope-001, pr-03-post-ret-001, pr-03-tech-conf-003, pr-03-cloud-001 |
| `data/questions/professional-responsibility/ch04-conflicts.json` | pr-04-estate-001, pr-04-former-cl-003 |
| `data/questions/professional-responsibility/ch05-duties.json` | pr-05-cont-003, pr-05-ref-fee-002 |
| `data/questions/professional-responsibility/ch06-trust.json` | pr-06-audit-001, pr-06-bylaw-002, pr-06-report-001 |
| `data/questions/professional-responsibility/ch07-court-duties.json` | pr-07-auth-001, pr-07-unmerit-001 |
| `data/questions/professional-responsibility/ch08-opposing.json` | pr-08-discrim-001 |
| `data/questions/professional-responsibility/ch09-withdrawal.json` | pr-09-subs-001, pr-09-time-001 |
| `data/questions/professional-responsibility/ch11-discipline.json` | pr-11-penalty-001, pr-11-penalty-002 |
| `data/questions/professional-responsibility/ch12-client-id.json` | pr-12-verify-001, pr-12-verify-002 |
| `data/questions/professional-responsibility/ch13-marketing.json` | pr-13-discrim-002 |
| `index.html` | prdra, prdrb, prb200 payloads re-baked |
| `docs/QUESTION_IMPROVEMENT_BACKLOG.md` | PR Bank IMPROVE section marked ✅ RESOLVED |
| `docs/QUESTION_QUALITY_IMPROVEMENT_PLAN.md` | Phase B4 completion note added |
| `docs/PHASE_2K_IMPROVE_B4_PR_LOG.md` | Created (this file) |

---

*All improved questions carry `updated_at: "2026-05-25"`. No `validation_status` fields changed. No `correct_answer` fields changed. No question IDs added or removed. No manifests modified.*
