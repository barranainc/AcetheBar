#!/usr/bin/env python3
"""Phase 2K-Improve-B5: Civil Litigation IMPROVE questions."""
import json, os
from datetime import date

os.chdir('/Users/muhammad/Downloads/railway-deploy')
TODAY = date.today().isoformat()

# ── ch02-limitation-periods.json ───────────────────────────────────────────
# civ-02-basic-lim-001  Weakness: "(assuming discovered on date of fall)" removes
#   discoverability analysis; anti_idx=2; arithmetic only.
#   Fix: redesign FP with delayed discovery; change correct_answer A→B; add
#   Incident-Date Trap, One-Year Trap, No-Period Trap.

with open('data/questions/civil-litigation/ch02-limitation-periods.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['civ-02-basic-lim-001']
qs[i].update({
    'fact_pattern': (
        "Takeshi slips and falls at a grocery store on March 10, 2023. He feels "
        "some knee soreness but attributes it to a recent gym workout and does not "
        "seek medical attention. On September 15, 2024, after persistent pain, a "
        "physician diagnoses him with a torn meniscus and informs him that the "
        "injury was caused by the fall in 2023. Takeshi immediately consults a "
        "lawyer."
    ),
    'call_of_question': (
        "What is the last day Takeshi may commence a proceeding against the grocery "
        "store under the Limitations Act, 2002?"
    ),
    'options': {
        'A': (
            "March 10, 2025 — two years after the date of the fall."
        ),
        'B': (
            "September 15, 2026 — two years after the date Takeshi discovered his "
            "claim, being the date a physician confirmed causation."
        ),
        'C': (
            "September 15, 2025 — one year after the date Takeshi discovered his claim."
        ),
        'D': (
            "There is no limitation period because Takeshi could not have discovered "
            "his claim on the date of the fall; the Limitations Act, 2002 does not "
            "apply to latent injury claims."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Under s. 4 of the Limitations Act, 2002, a proceeding must be commenced "
        "within two years of the day the claim was discovered. Under s. 5, a claim "
        "is discovered on the day the claimant first knew or ought to have known: "
        "(a) that the injury, loss, or damage occurred; (b) that it was caused by "
        "or contributed to by an act or omission; (c) that the act or omission was "
        "that of the person against whom the claim is made; and (d) that a proceeding "
        "would be an appropriate means to seek to remedy the injury. Takeshi could "
        "not reasonably have connected the grocery store fall to the knee injury until "
        "September 15, 2024, when a physician confirmed causation. The two-year "
        "limitation period therefore runs from September 15, 2024, and expires "
        "September 15, 2026."
    ),
    'why_A_wrong': (
        "A applies the two-year period to the wrong start date. The Incident-Date Trap: "
        "the limitation period does not automatically run from the date of the event. "
        "Under s. 5 of the Limitations Act, 2002, the period runs from the date of "
        "discovery — when the claimant knew or ought to have known of the act, the "
        "loss, and causation. Because Takeshi did not and could not reasonably have "
        "connected the fall to his knee injury until the September 2024 diagnosis, "
        "the clock did not start on March 10, 2023."
    ),
    'why_B_wrong': (
        "B is correct. Under s. 5 of the Limitations Act, 2002, the claim is "
        "discovered when the claimant first knew or ought to have known of the "
        "injury, the causation, and the identity of the defendant. Takeshi's "
        "physician confirmed on September 15, 2024 that the fall caused the torn "
        "meniscus; this is the date of discovery. The two-year basic limitation "
        "period under s. 4 therefore expires on September 15, 2026."
    ),
    'why_C_wrong': (
        "C correctly identifies the discovery date but applies a one-year limitation "
        "period. The One-Year Trap: no one-year personal injury limitation period "
        "exists in Ontario's general Limitations Act, 2002 framework. The basic "
        "limitation period under s. 4 is two years from discovery. A one-year period "
        "could arise under specific statutes (e.g., certain municipal notice "
        "requirements), but the Limitations Act, 2002 itself uses a two-year period."
    ),
    'why_D_wrong': (
        "D overstates the consequence of latent injury. The No-Limitation-Period Trap: "
        "the Limitations Act, 2002 does apply to latent injury claims. The "
        "discoverability principle in s. 5 delays the commencement of the period "
        "until the claimant knows or ought to know the essential facts — it does not "
        "eliminate the limitation period. The two-year period still runs; it merely "
        "starts later (from the date of discovery, not the incident)."
    ),
    'exam_trigger_words': [
        'limitation period', 'discoverability', 'Limitations Act 2002', 's.5',
        'latent injury', 'date of discovery', 'personal injury', 'slip and fall',
        'commencement deadline'
    ],
    'tested_concepts': [
        's.4 basic two-year limitation period',
        's.5 discoverability principle',
        'discovery date vs incident date distinction',
        'latent injury and delayed discoverability',
        'Incident-Date Trap',
        'One-Year Trap',
        'No-Limitation-Period Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/civil-litigation/ch02-limitation-periods.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed civ-02-basic-lim-001")

# ── ch03-pleadings.json ────────────────────────────────────────────────────
# civ-03-soc-form-001  Weakness: pure recall of r.14.03; no applied judgment.
#   Fix: redesign as applied scenario — lawyer drafts an endorsement with
#   evidence summary; ask whether it complies. Add Comprehensive-Endorsement Trap,
#   Witness-List Trap, Nullity-Overstatement Trap.

with open('data/questions/civil-litigation/ch03-pleadings.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['civ-03-soc-form-001']
qs[i].update({
    'fact_pattern': (
        "Elaine is preparing a statement of claim for her client in a commercial "
        "lease dispute. She drafts an endorsement that includes: (i) a statement "
        "that the defendant breached a commercial lease agreement; (ii) a claim "
        "for $275,000 in damages; and (iii) a two-page narrative summarizing all "
        "documentary evidence and witness accounts the plaintiff intends to rely on "
        "at trial. The defendant's counsel reviews the endorsement and objects."
    ),
    'call_of_question': (
        "Under r. 14.03 of the Rules of Civil Procedure, does the endorsement as "
        "drafted comply with the rule's requirements?"
    ),
    'options': {
        'A': (
            "Yes — r. 14.03 requires the endorsement to include a comprehensive "
            "statement of the facts and evidence supporting the claim so that the "
            "defendant is fully informed before filing a defence."
        ),
        'B': (
            "No — r. 14.03 requires only a concise statement of the nature of the "
            "claim and the relief sought; the two-page evidence narrative exceeds "
            "the endorsement's proper function and the evidence should not appear "
            "in the endorsement at all."
        ),
        'C': (
            "No — the endorsement is deficient because it does not include the names "
            "of the witnesses the plaintiff intends to call at trial, as required by "
            "r. 14.03."
        ),
        'D': (
            "No — the inclusion of the evidence narrative in the endorsement renders "
            "the entire statement of claim a nullity, and Elaine must recommence the "
            "proceeding from the beginning."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Under r. 14.03 of the Rules of Civil Procedure (R.R.O. 1990, Reg. 194), "
        "an originating process — including a statement of claim — shall be endorsed "
        "with a concise statement of the nature of the claim and the relief sought. "
        "The endorsement is a short-form summary, not a vehicle for evidence or "
        "detailed factual narratives. Evidence, witness lists, and supporting details "
        "belong in affidavits or at trial — not in the endorsement. Elaine's two-page "
        "evidence narrative is improper content for the endorsement and the "
        "endorsement as drafted does not comply with r. 14.03's conciseness "
        "requirement."
    ),
    'why_A_wrong': (
        "A inverts the rule. The Comprehensive-Endorsement Trap: r. 14.03 requires "
        "a concise statement of the nature of the claim and relief sought — not a "
        "comprehensive summary of facts and evidence. A pleading states facts, not "
        "evidence, and even the factual content of the statement of claim itself is "
        "distinct from evidence. Including a detailed evidence narrative in the "
        "endorsement goes beyond the rule's requirements and is improper."
    ),
    'why_B_wrong': (
        "B is correct. Rule 14.03 requires the endorsement to be a concise statement "
        "of the nature of the claim (identifying the legal basis) and the relief "
        "sought (the remedy). Items (i) and (ii) of Elaine's endorsement satisfy this "
        "requirement. Item (iii) — the two-page evidence narrative — exceeds the "
        "endorsement's proper function. Evidence is not to appear in a pleading or "
        "endorsement; it is adduced at trial or by affidavit."
    ),
    'why_C_wrong': (
        "C invents a requirement that does not exist under r. 14.03. The "
        "Witness-List Trap: rule 14.03 does not require the endorsement or the "
        "statement of claim to list witnesses the plaintiff intends to call. Witness "
        "lists are relevant at the pre-trial and trial stage, not as a required "
        "component of an originating process."
    ),
    'why_D_wrong': (
        "D overstates the consequence. The Nullity-Overstatement Trap: a deficiency "
        "in the content of an endorsement (including improper content) does not "
        "automatically render the entire statement of claim a nullity. Courts have "
        "discretion to permit amendments under r. 26.01. A procedural defect in the "
        "endorsement is a correctable irregularity, not a ground for treating the "
        "proceeding as void from the outset."
    ),
    'exam_trigger_words': [
        'endorsement', 'r.14.03', 'statement of claim', 'originating process',
        'concise statement', 'nature of the claim', 'relief sought', 'pleadings'
    ],
    'tested_concepts': [
        'r.14.03 endorsement requirements',
        'concise vs comprehensive endorsement',
        'improper content in endorsement',
        'Comprehensive-Endorsement Trap',
        'Witness-List Trap',
        'Nullity-Overstatement Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/civil-litigation/ch03-pleadings.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed civ-03-soc-form-001")

# ── ch06-motions.json ──────────────────────────────────────────────────────
# civ-06-injunction-004  Weakness: FP tells candidate both stages pass, asks
#   "which stage is next" — no application of balance factors.
#   Fix: inject competing balance-of-convenience facts; improve distractors to
#   test whether unequal balance favours status quo, and whether court must
#   automatically discharge if defendant shows strong countervailing harm.

with open('data/questions/civil-litigation/ch06-motions.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['civ-06-injunction-004']
qs[i].update({
    'fact_pattern': (
        "A defendant moves to discharge an interlocutory injunction previously "
        "granted ex parte. The plaintiff, a small technology vendor, established "
        "a serious question to be tried and that it would suffer irreparable harm "
        "if the injunction were refused (loss of its sole client contract). The "
        "defendant, a large publicly-traded corporation, argues that maintaining "
        "the injunction will delay a product launch by six weeks and cost it an "
        "estimated $4 million in lost revenue — a sum it quantifies precisely in "
        "affidavit evidence. The plaintiff offers an undertaking as to damages. "
        "The judge is now assessing the third branch of the RJR-MacDonald test."
    ),
    'call_of_question': (
        "Under the third branch of the RJR-MacDonald test, which of the following "
        "most accurately describes how the court should assess the balance of "
        "convenience in these circumstances?"
    ),
    'options': {
        'A': (
            "The injunction must be discharged because the defendant has quantified "
            "its harm precisely — once a moving party establishes greater "
            "quantifiable harm than the plaintiff, the balance of convenience "
            "automatically favours discharge."
        ),
        'B': (
            "The injunction must be maintained because satisfying the first two "
            "RJR-MacDonald elements — serious question and irreparable harm — creates "
            "a presumption in favour of maintaining the status quo that cannot be "
            "displaced on the balance of convenience alone."
        ),
        'C': (
            "The court weighs the relative harm to each party from granting or "
            "refusing the injunction, considering all relevant factors including the "
            "undertaking as to damages, the capacity of each party to absorb harm, "
            "and the public interest; where the balance is genuinely equal, courts "
            "generally favour the status quo."
        ),
        'D': (
            "The court must discharge the injunction because the defendant's harm "
            "is quantifiable in money and therefore, by definition, compensable — "
            "once a party's alleged harm is monetizable, irreparable harm is "
            "negated and the injunction cannot stand."
        ),
    },
    'correct_answer': 'C',
    'explanation': (
        "Under the third branch of the RJR-MacDonald test (RJR-MacDonald Inc. v. "
        "Canada (A.G.), [1994] 1 SCR 311), the court weighs which party would "
        "suffer greater harm from the grant or refusal of the injunction. This "
        "involves considering: the nature and quantifiability of each party's harm, "
        "whether the plaintiff's undertaking as to damages adequately protects the "
        "defendant, the relative financial capacity of the parties to absorb "
        "temporary harm, the public interest, and any other relevant factors. The "
        "fact that the defendant has quantified its loss at $4 million is not "
        "automatically determinative — courts weigh all factors holistically. The "
        "plaintiff's undertaking as to damages is directly relevant to the "
        "defendant's quantified loss. Where the balance is genuinely equal, courts "
        "tend to favour preserving the status quo."
    ),
    'why_A_wrong': (
        "A states a rule that does not exist. The Quantifiability-Determines-Balance "
        "Trap: the ability to quantify harm precisely does not automatically tip the "
        "balance of convenience toward discharge. Under RJR-MacDonald, the court "
        "weighs all relevant factors holistically. A defendant who can precisely "
        "quantify its loss may actually be better protected by the plaintiff's "
        "undertaking as to damages — precise quantification does not eliminate "
        "judicial discretion or automatically favour one party."
    ),
    'why_B_wrong': (
        "B misstates the law. The First-Two-Elements Presumption Trap: satisfying "
        "the first two branches of RJR-MacDonald creates no irrebuttable or "
        "presumptive entitlement to the injunction. All three branches must be "
        "weighed, and a strong showing on the balance of convenience against the "
        "plaintiff can outweigh success on the first two elements. The balance of "
        "convenience is an independent and substantive inquiry."
    ),
    'why_C_wrong': (
        "C is correct. Under the third branch of RJR-MacDonald, the court weighs "
        "the harm to each party from granting or refusing the injunction, "
        "considering all relevant factors: the plaintiff's undertaking as to "
        "damages (which may compensate the defendant's $4 million quantified loss), "
        "the parties' relative capacity to absorb harm, the public interest, and "
        "whether the harm on each side is truly irreparable or compensable. Equal "
        "balance favours the status quo, but an unequal balance may tip either way "
        "depending on the facts."
    ),
    'why_D_wrong': (
        "D conflates the second branch (irreparable harm) with the third branch "
        "balance of convenience analysis. The Monetizable-Harm-Negates-Injunction "
        "Trap: whether harm is quantifiable in money is relevant to the second "
        "branch (irreparable harm, which the court has already found here), not a "
        "ground to defeat the injunction at the third branch. The undertaking as "
        "to damages addresses monetizable harm directly — the defendant's "
        "$4 million figure is an argument for adequacy of the undertaking, not an "
        "automatic basis for discharge."
    ),
    'exam_trigger_words': [
        'RJR-MacDonald', 'interlocutory injunction', 'balance of convenience',
        'undertaking as to damages', 'serious question to be tried',
        'irreparable harm', 'ex parte', 'discharge injunction'
    ],
    'tested_concepts': [
        'RJR-MacDonald three-part test',
        'balance of convenience — holistic weighing',
        'undertaking as to damages as a factor',
        'quantifiability of harm vs irreparability',
        'Quantifiability-Determines-Balance Trap',
        'First-Two-Elements Presumption Trap',
        'Monetizable-Harm-Negates-Injunction Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/civil-litigation/ch06-motions.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed civ-06-injunction-004")

# ── ch07-summary-judgment.json ─────────────────────────────────────────────
# civ-07-summ-judg-005  Weakness: defendant's "always require trial" argument
#   is too obviously the pre-Hryniak rule; no applied scenario requiring judgment.
#   Fix: add nuance — motion judge ordered video cross-examination of affiants
#   under r.20.04(2.1); defendant argues judge still cannot assess credibility
#   from video. Tests Hryniak powers of the motion judge more precisely.

with open('data/questions/civil-litigation/ch07-summary-judgment.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['civ-07-summ-judg-005']
qs[i].update({
    'fact_pattern': (
        "On a summary judgment motion, both sides have filed conflicting affidavits "
        "about the central disputed issue of fact. The motion judge exercises her "
        "powers under r. 20.04(2.1) and directs that both affiants be cross-examined "
        "by video conference before her so that she may assess credibility. After "
        "conducting the cross-examinations, the motion judge concludes that one "
        "affiant is more credible and grants summary judgment in the plaintiff's "
        "favour. The defendant appeals, arguing that a motion judge can never make "
        "credibility findings — even after conducting cross-examinations — and that "
        "only a trial judge may resolve conflicting testimony."
    ),
    'call_of_question': (
        "After Hryniak v Mauldin, 2014 SCC 7, and under r. 20.04(2.1), is the "
        "defendant's argument on appeal correct?"
    ),
    'options': {
        'A': (
            "Yes — a motion judge's authority under r. 20.04(2.1) is limited to "
            "receiving additional evidence; making credibility findings based on "
            "cross-examination remains exclusively within the trial judge's province."
        ),
        'B': (
            "No — Hryniak v Mauldin expanded the motion judge's powers to include "
            "assessing credibility where doing so is necessary to decide the motion "
            "and where it is not unjust to do so; cross-examinations conducted under "
            "r. 20.04(2.1) are a proper basis for credibility findings."
        ),
        'C': (
            "Yes — using video conference cross-examination rather than in-person "
            "testimony denies the defendant the constitutional right to confront "
            "witnesses in person, rendering the credibility assessment procedurally "
            "invalid."
        ),
        'D': (
            "No — but only because the defendant waived the right to object by "
            "participating in the video cross-examination process without objecting "
            "to the motion judge's jurisdiction at the time."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "In Hryniak v Mauldin, 2014 SCC 7, the Supreme Court of Canada held that "
        "r. 20.04(2.1) grants motion judges specific enhanced powers — including "
        "hearing oral evidence and conducting cross-examinations — precisely to "
        "enable them to assess credibility where doing so is necessary and not "
        "unjust. The motion judge may weigh evidence, assess credibility, and draw "
        "reasonable inferences. A credibility dispute between affiants no longer "
        "automatically mandates a full trial. The defendant's argument that motion "
        "judges can never make credibility findings is the pre-Hryniak position "
        "that the Supreme Court expressly rejected. The motion judge here correctly "
        "exercised her r. 20.04(2.1) powers."
    ),
    'why_A_wrong': (
        "A misreads r. 20.04(2.1). The Powers-Are-Limited-to-Evidence Trap: rule "
        "20.04(2.1) does not merely authorize the reception of additional evidence — "
        "it expressly grants the motion judge the power to assess credibility, weigh "
        "evidence, and draw inferences. The purpose of Hryniak was precisely to "
        "remove the categorical bar on credibility findings at the summary judgment "
        "stage. A motion judge who directs cross-examination under r. 20.04(2.1) is "
        "permitted to act on the credibility assessment that flows from it."
    ),
    'why_B_wrong': (
        "B is correct. Under Hryniak v Mauldin and r. 20.04(2.1), a motion judge "
        "has the power to assess credibility where necessary to decide the motion "
        "and where doing so is not unjust. This is precisely the power the motion "
        "judge exercised by directing video cross-examinations and then making "
        "credibility findings based on them. The defendant's argument that "
        "credibility can only be assessed by a trial judge was the pre-Hryniak "
        "rule that Hryniak expressly abrogated."
    ),
    'why_C_wrong': (
        "C invents a constitutional right that does not exist in civil litigation. "
        "The Confrontation-Rights-in-Civil-Proceedings Trap: the right to confront "
        "witnesses in person is a principle drawn from criminal law (under s. 11(d) "
        "of the Charter). No equivalent constitutional guarantee of in-person "
        "confrontation exists in Ontario civil proceedings. The use of video "
        "conference for cross-examinations is expressly contemplated by the Rules "
        "and was further normalized post-pandemic."
    ),
    'why_D_wrong': (
        "D introduces a waiver doctrine that is not the basis for the motion "
        "judge's authority. The Waiver-Cures-Jurisdiction Trap: the motion judge's "
        "power to assess credibility under r. 20.04(2.1) and Hryniak flows from "
        "the statute and the Supreme Court's decision — it does not depend on "
        "whether the defendant waived an objection. Whether or not the defendant "
        "objected during cross-examination is irrelevant to the existence of the "
        "motion judge's jurisdiction."
    ),
    'exam_trigger_words': [
        'Hryniak', 'summary judgment', 'r.20.04(2.1)', 'credibility',
        'motion judge', 'cross-examination', 'affidavit conflict', 'trial mandatory'
    ],
    'tested_concepts': [
        'Hryniak v Mauldin credibility powers of motion judge',
        'r.20.04(2.1) enhanced powers',
        'credibility disputes post-Hryniak',
        'Powers-Are-Limited-to-Evidence Trap',
        'Confrontation-Rights-in-Civil-Proceedings Trap',
        'Waiver-Cures-Jurisdiction Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/civil-litigation/ch07-summary-judgment.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed civ-07-summ-judg-005")

# ── ch09-examination-for-discovery.json ────────────────────────────────────
# civ-09-ref-und-005  Weakness: "fourteen months" + "unreasonable delay" framing
#   in FP gives away the answer; distractor B invents a non-existent 60-day rule.
#   Fix: add procedural history context (no prior motion, discovery closed months
#   ago, trial set), remove "unreasonable" framing; replace B with a more
#   plausible rule-based trap; add Discovery-Never-Closes Trap.

with open('data/questions/civil-litigation/ch09-examination-for-discovery.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['civ-09-ref-und-005']
qs[i].update({
    'fact_pattern': (
        "Sobchak Industrial Supply Inc. completed examination for discovery of the "
        "defendant, Paradis Fabrication Ltd., fourteen months ago in a commercial "
        "negligence action. At the time, Paradis refused to answer eleven questions, "
        "undertook to produce certain documents, and delivered answers to undertakings "
        "nine months ago. Sobchak never followed up on the refused questions. The "
        "parties have since completed documentary discovery. A trial date has now "
        "been set for eight months from now. Sobchak's counsel advises that she "
        "intends to bring a motion to compel answers to the eleven refused questions."
    ),
    'call_of_question': (
        "What procedural risk does Sobchak face in bringing this motion to compel "
        "now, fourteen months after the examination for discovery?"
    ),
    'options': {
        'A': (
            "No risk — there is no time limit on motions to compel answers to "
            "refused questions; Sobchak may bring the motion at any point before "
            "the commencement of trial."
        ),
        'B': (
            "The motion will be dismissed as of right because Sobchak failed to "
            "bring it within 90 days of Paradis delivering its answers to "
            "undertakings, which is the deemed deadline under the Rules of "
            "Civil Procedure."
        ),
        'C': (
            "Sobchak risks the motion being dismissed or penalized in costs because "
            "courts expect motions to compel discovery refusals to be brought within "
            "a reasonable time after the examination; delay of this length, with no "
            "explanation and a trial date set, may result in the court exercising "
            "its discretion to deny the motion."
        ),
        'D': (
            "Sobchak must obtain leave of court to examine Paradis again; once a "
            "discovery examination is completed and undertakings answered, a party "
            "has no further right to pursue refused questions without a fresh "
            "examination order."
        ),
    },
    'correct_answer': 'C',
    'explanation': (
        "Ontario discovery practice imposes no absolute statutory deadline on "
        "motions to compel answers to discovery refusals. However, courts "
        "consistently hold that such motions must be brought within a reasonable "
        "time following the examination. Fourteen months — with no explanation, "
        "no prior follow-up, completed documentary discovery, and a trial date "
        "now set — will likely be found to be an unreasonable delay. The court "
        "retains discretion to dismiss the motion or award costs against Sobchak "
        "for bringing it so late. Conversely, the court may still grant the motion "
        "if the questions are material and Sobchak provides a satisfactory "
        "explanation. The risk is not automatic dismissal but a substantial "
        "likelihood of adverse procedural consequences."
    ),
    'why_A_wrong': (
        "A overstates Sobchak's position. The Discovery-Never-Closes Trap: while "
        "there is no hard statutory deadline, courts do not treat the right to "
        "bring motions to compel as open-ended. A motion to compel filed fourteen "
        "months after the examination, with no explanation and after a trial date "
        "has been set, is vulnerable to being dismissed on the basis that it was "
        "not brought within a reasonable time. Ignoring the reasonable-time "
        "requirement exposes Sobchak to adverse cost consequences or outright "
        "dismissal."
    ),
    'why_B_wrong': (
        "B invents a rule that does not exist. There is no 90-day deemed deadline "
        "or automatic right-of-dismissal triggered by the delivery of answers to "
        "undertakings under the Rules of Civil Procedure (R.R.O. 1990, Reg. 194). "
        "The timing of answers to undertakings may be relevant context — if "
        "Sobchak waited nine months after receiving undertaking answers to bring "
        "the motion, this supports a finding of unreasonable delay — but there is "
        "no fixed deadline that triggers automatic dismissal."
    ),
    'why_C_wrong': (
        "C is correct. There is no absolute deadline for motions to compel, but "
        "courts exercise their inherent and r. 1.04 proportionality jurisdiction "
        "to refuse relief where a party sat on its rights without reasonable "
        "explanation. With a trial date eight months away, documentary discovery "
        "complete, and no explanation for the fourteen-month delay, Sobchak faces "
        "a real risk of the motion being dismissed or of facing adverse costs — "
        "even if the court ultimately grants it on the merits."
    ),
    'why_D_wrong': (
        "D misstates the procedural pathway. Once a party refuses to answer "
        "questions at discovery, the moving party's remedy is a motion to compel "
        "those specific answers — not a fresh examination order. There is no rule "
        "requiring a new examination order simply because answers to undertakings "
        "have been delivered. The right to compel refused questions survives the "
        "completion of undertakings; it is constrained only by the reasonable-time "
        "expectation, not by any requirement to seek fresh examination leave."
    ),
    'exam_trigger_words': [
        'examination for discovery', 'refusals', 'motion to compel',
        'undertakings', 'reasonable time', 'discovery delay', 'trial date set'
    ],
    'tested_concepts': [
        'no absolute deadline for motions to compel discovery refusals',
        'reasonable time requirement for discovery motions',
        'consequences of delay in bringing discovery motions',
        'Discovery-Never-Closes Trap',
        'invented 90-day rule trap',
        'Fresh-Examination-Required Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/civil-litigation/ch09-examination-for-discovery.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed civ-09-ref-und-005")

# ── ch11-trial.json ────────────────────────────────────────────────────────
# civ-11-ev-003  Weakness: rule-recall; distractor D ("always inadmissible
#   because self-serving") too obviously wrong; distractors under-trap-engineered.
#   Fix: refocus call on which objection could succeed; add Hearsay-of-Demo Trap,
#   Prejudice-Equals-Exclusion Trap, Expert-Foundation-Always-Required Trap.

with open('data/questions/civil-litigation/ch11-trial.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['civ-11-ev-003']
qs[i].update({
    'fact_pattern': (
        "At trial in a construction defect case, the plaintiff's counsel seeks to "
        "introduce a computer-generated animation depicting how the roof collapse "
        "allegedly occurred. The animation was created by the plaintiff's forensic "
        "structural engineer, who will testify as an expert at trial and will be "
        "available for cross-examination. The defendant raises three objections: "
        "(1) the animation is hearsay because it is an out-of-court 'statement' "
        "made by the engineer; (2) its presentation of the plaintiff's theory of "
        "causation is prejudicial to the defendant; and (3) the animation presents "
        "only one possible version of events and must therefore be excluded."
    ),
    'call_of_question': (
        "Which of the following most accurately describes the admissibility of the "
        "animation in Ontario civil proceedings?"
    ),
    'options': {
        'A': (
            "The animation is inadmissible hearsay because it is an out-of-court "
            "'statement' prepared by the engineer, and its admission would deprive "
            "the defendant of the right to cross-examine the maker of the statement."
        ),
        'B': (
            "The animation is admissible if it is relevant, fairly and accurately "
            "represents the matters it depicts, and the trial judge is satisfied that "
            "its probative value is not substantially outweighed by the risk of "
            "unfair prejudice; the defendant's objections go to weight, not "
            "admissibility."
        ),
        'C': (
            "The animation must be excluded because it presents the plaintiff's "
            "theory of causation in a manner that could unfairly prejudice the "
            "defendant; civil trials require demonstrative evidence to present a "
            "neutral, agreed-upon account of events."
        ),
        'D': (
            "The animation is inadmissible unless the defendant stipulates that the "
            "animation accurately depicts the events; absent such consent, "
            "demonstrative reconstructions are categorically excluded as one-sided."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Demonstrative evidence — including computer-generated animations, models, "
        "charts, and diagrams — is admissible in Ontario civil trials if it meets "
        "the general admissibility criteria: it is relevant to a matter in issue; "
        "it fairly and accurately represents the subject matter; and its probative "
        "value is not substantially outweighed by the risk of unfair prejudice. "
        "None of the defendant's three objections is sufficient to exclude the "
        "animation. Demonstrative evidence is not hearsay in the traditional sense — "
        "hearsay rules apply to out-of-court statements adduced for the truth of "
        "their contents, not to demonstrative reconstructions that the sponsoring "
        "expert will explain under oath. Prejudice that is inherent in a party's "
        "theory of the case goes to weight, not admissibility. And the fact that "
        "the animation presents one version of events does not make it categorically "
        "inadmissible."
    ),
    'why_A_wrong': (
        "A misapplies hearsay doctrine. The Hearsay-of-Demonstrative Trap: "
        "demonstrative evidence such as an animation is not an out-of-court "
        "statement adduced for the truth of its contents in the way the hearsay "
        "rule contemplates. The expert will testify in court and be cross-examined "
        "about the animation's assumptions and accuracy. The animation is an "
        "illustrative tool for the expert's in-court opinion, not an out-of-court "
        "assertion offered independently of the witness."
    ),
    'why_B_wrong': (
        "B is correct. Demonstrative evidence is admissible if relevant, fair, "
        "accurate, and its probative value is not substantially outweighed by "
        "unfair prejudice. The forensic engineer will testify and be available for "
        "cross-examination about the animation's methodology and assumptions. None "
        "of the defendant's objections — hearsay, prejudice, or one-sidedness — is "
        "legally sufficient to require exclusion. These factors may go to the weight "
        "the trier of fact assigns to the animation, but not to its admissibility."
    ),
    'why_C_wrong': (
        "C misstates the law. The Prejudice-Equals-Exclusion Trap: the fact that "
        "demonstrative evidence presents the plaintiff's theory in a vivid or "
        "compelling way does not make it inadmissible. Courts balance probative "
        "value against the risk of unfair prejudice; prejudice that flows from "
        "persuasive and relevant evidence is not 'unfair' in the legal sense. "
        "There is no requirement in Ontario civil proceedings that demonstrative "
        "evidence be neutral or agreed to by both parties."
    ),
    'why_D_wrong': (
        "D invents a consent requirement. The Consent-Required-for-Demonstrations "
        "Trap: demonstrative evidence does not require the opposing party's "
        "stipulation or consent. Courts routinely admit demonstrative reconstructions "
        "over objection, provided the foundational criteria are met. The defendant's "
        "disagreement with the animation's depiction of events is explored through "
        "cross-examination of the expert and, if the defendant chooses, by "
        "introducing its own competing demonstrative evidence."
    ),
    'exam_trigger_words': [
        'demonstrative evidence', 'computer animation', 'reconstruction',
        'admissibility', 'probative value', 'prejudice', 'hearsay',
        'expert evidence', 'trial evidence', 'civil trial'
    ],
    'tested_concepts': [
        'admissibility of demonstrative evidence in civil proceedings',
        'hearsay rule inapplicable to demonstrative reconstructions',
        'probative value vs unfair prejudice balancing',
        'Hearsay-of-Demonstrative Trap',
        'Prejudice-Equals-Exclusion Trap',
        'Consent-Required-for-Demonstrations Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/civil-litigation/ch11-trial.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed civ-11-ev-003")

# ── ch12-costs.json ────────────────────────────────────────────────────────
# civ-12-repres-001  Weakness: distractor C ("full senior lawyer rate") too
#   obviously wrong for a prepared candidate.
#   Fix: replace C with a nuanced wrong answer about junior solicitor rate under
#   partial indemnity. Add Partial-Indemnity-Equivalence Trap.

with open('data/questions/civil-litigation/ch12-costs.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['civ-12-repres-001']
qs[i].update({
    'options': {
        'A': (
            "Self-represented litigants are not entitled to any costs; only parties "
            "who have retained legal counsel and paid legal fees may recover costs."
        ),
        'B': (
            "Under Fong v. Chan, self-represented litigants may be awarded costs for "
            "time spent on the litigation, but the costs are assessed at a reduced "
            "rate reflecting the value of their time and effort — not at the rate "
            "charged by a practicing lawyer."
        ),
        'C': (
            "Self-represented litigants are entitled to costs assessed at the "
            "partial indemnity rate applicable to a junior solicitor, because courts "
            "treat the time invested by a self-represented party as equivalent to "
            "services rendered by a junior lawyer."
        ),
        'D': (
            "Self-represented litigants may only recover disbursements (out-of-pocket "
            "expenses) but not any amount for their time; the concept of 'fees' does "
            "not apply to parties who are not paying for legal services."
        ),
    },
    'why_C_wrong': (
        "C overstates the entitlement and misstates the applicable rate. The "
        "Partial-Indemnity-Equivalence Trap: Fong v. Chan does not entitle "
        "self-represented litigants to costs at the partial indemnity rate for a "
        "junior solicitor. Courts assess the quantum of costs at a rate reflecting "
        "the actual value of the self-represented party's time and contribution to "
        "the litigation — which typically falls below the partial indemnity rate "
        "for a junior lawyer. The court exercises broad discretion and does not "
        "treat a self-represented party as a professional whose time is priced on "
        "the standard tariff."
    ),
    'updated_at': TODAY,
})

# civ-12-throwaway-001  Weakness: vocabulary-level; no application to borderline
#   facts. Fix: change FP to litigation conduct only (no transactional misconduct);
#   add Litigation-Conduct-Only Trap to test whether courts apply substantial
#   indemnity to in-court misconduct alone.

i = id_map['civ-12-throwaway-001']
qs[i].update({
    'fact_pattern': (
        "At trial in a shareholder oppression case, the trial judge finds that the "
        "defendant did not commit fraud in the underlying transaction. However, "
        "the judge finds that during the litigation the defendant deliberately "
        "withheld key documents in defiance of production orders, provided "
        "evasive and misleading answers at discovery, and filed a series of "
        "procedural motions for the purpose of driving up the plaintiff's costs. "
        "No offer to settle was made by either party. The plaintiff moves for "
        "substantial indemnity costs."
    ),
    'call_of_question': (
        "May the court award substantial indemnity costs based solely on the "
        "defendant's conduct during the litigation, where no offer to settle "
        "was made and the defendant did not engage in reprehensible conduct "
        "in the underlying transaction?"
    ),
    'options': {
        'A': (
            "No — substantial indemnity costs can only be awarded where a party has "
            "beaten an offer to settle under r. 49.10; absent an offer, only partial "
            "indemnity costs are available."
        ),
        'B': (
            "Yes — under r. 57.01, the court has discretion to award substantial "
            "indemnity costs based on reprehensible conduct in the litigation itself, "
            "even where the defendant did not engage in misconduct in the underlying "
            "transaction."
        ),
        'C': (
            "Substantial indemnity costs are only available upon motion under r. 57.07 "
            "for a personal costs order against the lawyer; they are not available "
            "against a party based on that party's litigation conduct."
        ),
        'D': (
            "No — only reprehensible conduct in the underlying transaction can "
            "justify substantial indemnity costs; misconduct during the litigation "
            "itself is addressed exclusively through contempt proceedings, not "
            "costs awards."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Under r. 57.01(1) of the Rules of Civil Procedure, the court has broad "
        "discretion in awarding costs and may award substantial indemnity costs "
        "based on reprehensible conduct — whether in the underlying transaction or "
        "in the litigation itself. Deliberately withholding documents in defiance "
        "of production orders, providing evasive discovery answers, and filing "
        "abusive procedural motions are paradigm examples of litigation misconduct "
        "that can ground a substantial indemnity costs award. An offer to settle "
        "under r. 49.10 is one trigger for substantial indemnity costs, but not "
        "the only one. Courts have consistently held that oppressive, vexatious, "
        "or scandalous litigation conduct, even without transactional misconduct, "
        "is a recognized basis for elevated costs."
    ),
    'why_A_wrong': (
        "A states a rule that does not exist. The Offer-to-Settle-Only Trap: "
        "r. 49.10 is one trigger for substantial indemnity costs (where a party "
        "beats its own offer), but it is not the only basis. Rule 57.01 grants the "
        "court broad discretion, expressly including the conduct of the parties — "
        "in the litigation and in the underlying transaction — as a relevant "
        "consideration. No offer to settle is required."
    ),
    'why_B_wrong': (
        "B is correct. Rule 57.01 gives the court discretion to award substantial "
        "indemnity costs based on reprehensible litigation conduct even without "
        "transactional misconduct. Deliberately withholding documents in defiance "
        "of production orders, providing evasive discovery answers, and filing "
        "abusive motions all fall within the category of conduct that can justify "
        "substantial indemnity. The absence of an offer to settle under r. 49.10 "
        "is irrelevant to this basis for elevated costs."
    ),
    'why_C_wrong': (
        "C misstates the scope of substantial indemnity costs. The Personal-Order "
        "Trap: r. 57.07 authorizes personal costs orders against lawyers in certain "
        "circumstances — it is not the exclusive pathway to substantial indemnity "
        "costs. Substantial indemnity costs under r. 57.01 can be awarded against "
        "a party (not just counsel) based on that party's own reprehensible conduct "
        "in the litigation."
    ),
    'why_D_wrong': (
        "D invents a categorical distinction that does not exist in the law. The "
        "Litigation-Conduct-Only Trap: the rule is the reverse of what D states — "
        "both transactional misconduct and litigation misconduct are recognized "
        "bases for substantial indemnity costs under r. 57.01. Courts have "
        "expressly awarded substantial indemnity based on litigation conduct alone "
        "(evasive discovery, abusive motions, document withholding), without "
        "requiring misconduct in the underlying transaction. Contempt and costs "
        "awards are also not mutually exclusive remedies."
    ),
    'exam_trigger_words': [
        'substantial indemnity costs', 'r.57.01', 'costs discretion',
        'reprehensible conduct', 'litigation misconduct', 'offer to settle r.49.10',
        'production order defiance', 'costs award'
    ],
    'tested_concepts': [
        'r.57.01 broad costs discretion',
        'substantial indemnity without offer to settle',
        'litigation conduct as basis for elevated costs',
        'Offer-to-Settle-Only Trap',
        'Personal-Order Trap',
        'Litigation-Conduct-Only Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/civil-litigation/ch12-costs.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed civ-12-repres-001 and civ-12-throwaway-001")

# ── ch14-enforcement.json ──────────────────────────────────────────────────
# civ-14-enf-garn-exam-001  Weakness: distractor A (re-issue notice only) and
#   distractor D (separate damages action) implausibly wrong; no oral-vs-affidavit
#   trap. Fix: add a Procedural-Notice-Required Trap and replace D with a more
#   plausible distractor about needing a production order first.

with open('data/questions/civil-litigation/ch14-enforcement.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['civ-14-enf-garn-exam-001']
qs[i].update({
    'options': {
        'A': (
            "The judgment creditor must first re-issue the notice of examination "
            "for a new date before any further steps can be taken; the failure to "
            "attend a first notice is not, by itself, a contempt of court."
        ),
        'B': (
            "The judgment creditor may move for a contempt order against the officer "
            "who failed to attend; failure to comply with a notice of examination "
            "in aid of execution is a contempt of court because the notice has the "
            "force of a court order."
        ),
        'C': (
            "Before contempt proceedings can be commenced, the judgment creditor "
            "must obtain a separate court order directing the officer to attend — "
            "a notice of examination alone is insufficient to ground a contempt "
            "finding."
        ),
        'D': (
            "The judgment creditor must first obtain a production order requiring "
            "the corporation to disclose its financial records before the officer "
            "can be examined; examining an officer without first securing the "
            "underlying financial documents is procedurally improper."
        ),
    },
    'why_A_wrong': (
        "A misstates the consequence of failing to attend. The Notice-Has-No-Force "
        "Trap: a notice of examination issued under r. 60.18 carries the force of "
        "a court order for the purposes of compelling attendance and for founding "
        "a contempt motion. Failure to attend is not merely a procedural irregularity "
        "that requires re-issuance of the notice — it is a contempt of court. The "
        "judgment creditor may proceed directly to a contempt motion."
    ),
    'why_D_wrong': (
        "D invents a prerequisite that does not exist under the Rules. The "
        "Production-Order-First Trap: there is no requirement to obtain a production "
        "order for financial records before an officer may be examined in aid of "
        "execution. The examination under r. 60.18 is itself the mechanism for "
        "discovering the judgment debtor's financial position; it is not contingent "
        "on prior document production. The officer's failure to attend the "
        "examination is independently remediable through contempt."
    ),
    'updated_at': TODAY,
})

# civ-14-enf-repl-001  Weakness: distractor A (new action) and D (unenforceable)
#   implausibly wrong; mandatory/permissive distinction unexploited.
#   Fix: replace D with a permissive/mandatory trap — "court may in its
#   discretion issue writ of delivery"; add Alternative-Remedy-Mandatory Trap.

i = id_map['civ-14-enf-repl-001']
qs[i].update({
    'options': {
        'A': (
            "The plaintiff's only remedy is to bring a new action claiming the "
            "monetary equivalent of the equipment; orders for specific personal "
            "property cannot be enforced directly in Ontario."
        ),
        'B': (
            "Under r. 60.10, the judgment creditor may issue a writ of delivery, "
            "which directs the sheriff to seize the specific property from the "
            "judgment debtor and deliver it to the plaintiff."
        ),
        'C': (
            "An order for delivery of specific personal property can only be enforced "
            "by contempt motion; there is no writ process available under the Rules "
            "for delivery of personal property."
        ),
        'D': (
            "Under r. 60.10, the court has discretion to issue a writ of delivery "
            "but may refuse to do so if the personal property could be replaced with "
            "a monetary award; the writ is available only for truly unique, "
            "irreplaceable items."
        ),
    },
    'why_D_wrong': (
        "D imposes a uniqueness requirement that r. 60.10 does not contain. The "
        "Uniqueness-Required Trap: rule 60.10 provides the writ of delivery as the "
        "enforcement mechanism for any court order requiring recovery or delivery "
        "of specific personal property — it does not require the property to be "
        "'truly unique' or 'irreplaceable' before the writ may issue. The "
        "availability of a monetary alternative does not bar the judgment creditor "
        "from enforcing the existing delivery order through the writ mechanism."
    ),
    'updated_at': TODAY,
})

with open('data/questions/civil-litigation/ch14-enforcement.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed civ-14-enf-garn-exam-001 and civ-14-enf-repl-001")

print("\nAll civil litigation improvements applied.")
