#!/usr/bin/env python3
"""Phase 2K-Improve-B5: Family Law IMPROVE questions."""
import json, os
from datetime import date

os.chdir('/Users/muhammad/Downloads/railway-deploy')
TODAY = date.today().isoformat()

# ── ch03-nfp.json ──────────────────────────────────────────────────────────
# fam-03-nfp-formula-001  Weakness: arithmetic drill; distractors are arithmetic
#   errors. Fix: convert one distractor to a legal trap — one asset is an
#   inheritance received during marriage; test whether inherited property is
#   automatically excluded. Add Inherited-Property-Auto-Exclusion Trap.
#   Also add a debt-at-marriage complication to the FP.
#   Restructure: FP now has a gift of $20k received during marriage; correct
#   answer C remains $170k because gift is NOT excluded (no excluded property
#   designation asserted); D is replaced with inheritance-as-automatic-exclusion trap.

with open('data/questions/family-law/ch03-nfp.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['fam-03-nfp-formula-001']
qs[i].update({
    'fact_pattern': (
        "On the valuation date, a husband has total assets of $300,000 (which "
        "includes a $20,000 cash gift he received from his parents during the "
        "marriage) and debts of $50,000. On the date of marriage he owned "
        "property worth $80,000 (not the matrimonial home) and had no debts at "
        "that time. The husband has not designated the inherited gift as excluded "
        "property in any domestic contract."
    ),
    'call_of_question': (
        "What is the husband's net family property under the Family Law Act?"
    ),
    'options': {
        'A': (
            "The husband's NFP is $300,000 — his total assets on the valuation date "
            "before any deductions."
        ),
        'B': (
            "The husband's NFP is $250,000 — after subtracting the $50,000 in "
            "valuation-date debts from the $300,000 in assets."
        ),
        'C': (
            "The husband's NFP is $170,000 — calculated as $300,000 (assets) minus "
            "$50,000 (debts) minus $80,000 (marriage-date property), applying the "
            "full s. 4(1) FLA formula. The $20,000 gift during the marriage is "
            "included in the assets because it has not been validly excluded."
        ),
        'D': (
            "The husband's NFP is $150,000 — because the $20,000 gift received "
            "during the marriage is automatically excluded property under FLA s. 4(2) "
            "as a gift from a third party; the formula is $300,000 − $50,000 − "
            "$80,000 − $20,000 = $150,000."
        ),
    },
    'correct_answer': 'C',
    'explanation': (
        "Under FLA s. 4(1), net family property = (value of all assets on valuation "
        "date) − (debts on valuation date) − (value of property owned on date of "
        "marriage that is not the matrimonial home, minus debts at marriage). "
        "Here: $300,000 − $50,000 − $80,000 = $170,000. The $20,000 gift received "
        "during the marriage does NOT reduce the NFP unless it qualifies as "
        "'excluded property' under FLA s. 4(2). Excluded property includes property "
        "received as a gift or inheritance from a third party during the marriage — "
        "but only if that property or its traceable proceeds still exist on the "
        "valuation date. More importantly, the question states the husband has not "
        "designated the gift as excluded property in any domestic contract; the "
        "exclusion is not automatic merely because property was received as a gift. "
        "The husband must assert and prove the exclusion at the time of equalization. "
        "On the facts as given, the $20,000 is included in the $300,000 assets and "
        "has not been excluded."
    ),
    'why_A_wrong': (
        "A ignores both the valuation-date debts ($50,000) and the marriage-date "
        "property deduction ($80,000). Under FLA s. 4(1), both must be subtracted. "
        "Simply stating gross assets overstates the NFP by $130,000 and fails to "
        "apply the statutory formula."
    ),
    'why_B_wrong': (
        "B correctly subtracts the valuation-date debts ($50,000) but fails to "
        "apply the marriage-date property deduction ($80,000). Under FLA s. 4(1), "
        "the value of property owned at the date of marriage (other than the "
        "matrimonial home) is deducted from the NFP calculation. Ignoring this "
        "deduction overstates the NFP by $80,000."
    ),
    'why_C_wrong': (
        "C is correct. The full FLA s. 4(1) formula yields: $300,000 − $50,000 − "
        "$80,000 = $170,000. The $20,000 gift is included in the $300,000 assets "
        "and is not automatically excluded merely because it was a gift. FLA s. 4(2) "
        "creates an exclusion for gifts and inheritances received during marriage, "
        "but the exclusion must be claimed and proven — it does not arise "
        "automatically from the nature of the property."
    ),
    'why_D_wrong': (
        "D applies the exclusion incorrectly. The Inherited-Property-Auto-Exclusion "
        "Trap: FLA s. 4(2) permits exclusion of property received as a gift or "
        "inheritance during the marriage, but this exclusion is not automatic. The "
        "husband must assert the exclusion, prove the property qualifies under "
        "s. 4(2), and demonstrate that the property (or its traceable proceeds) "
        "still exists on the valuation date. The question states he has not "
        "designated it as excluded in any domestic contract and does not identify "
        "whether the $20,000 cash is still separately traceable. On these facts, "
        "the automatic deduction of $20,000 is not warranted."
    ),
    'exam_trigger_words': [
        'NFP', 'net family property', 'FLA s.4(1)', 'FLA s.4(2)', 'excluded property',
        'valuation date', 'marriage date deduction', 'gift during marriage',
        'equalization', 'matrimonial home exclusion'
    ],
    'tested_concepts': [
        'FLA s.4(1) NFP formula',
        'FLA s.4(2) excluded property — gifts and inheritances',
        'excluded property is not automatic — must be asserted and proven',
        'marriage-date property deduction',
        'Inherited-Property-Auto-Exclusion Trap'
    ],
    'updated_at': TODAY,
})

# fam-03-equal-paymnt-001  Weakness: all numbers given directly; distractors
#   are arithmetic errors. Fix: add a s.5(6) unconscionability trap as distractor;
#   test whether FLA s.5(1) gives a court discretion to award less than half.
#   Replace distractor C (equal property division) with unconscionability trap.

i = id_map['fam-03-equal-paymnt-001']
qs[i].update({
    'options': {
        'A': (
            "Sonja pays Dimitri $80,000 because she has the lower NFP and must "
            "contribute to equalization."
        ),
        'B': (
            "Dimitri pays Sonja $120,000, representing one-half of the difference "
            "between their net family properties under FLA s. 5(1)."
        ),
        'C': (
            "Dimitri pays Sonja $120,000 under FLA s. 5(1), but the court has "
            "discretion under FLA s. 5(6) to reduce this amount if the equalization "
            "payment would be unconscionable given the short duration of the marriage "
            "or other factors — even without any other exceptional circumstances on "
            "these facts."
        ),
        'D': (
            "Dimitri pays Sonja $160,000, representing the full difference between "
            "their net family properties."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Under FLA s. 5(1), the spouse with the lower NFP is entitled to one-half "
        "the difference between the spouses' NFPs. Here: (Dimitri's NFP $320,000 − "
        "Sonja's NFP $80,000) ÷ 2 = $120,000. Dimitri pays Sonja $120,000. "
        "FLA s. 5(6) permits the court to vary the equalization payment if the "
        "standard result would be unconscionable, taking into account factors such "
        "as a very short marriage, deliberate depletion, or other listed grounds. "
        "However, the question states there is no excluded property, no debt at "
        "marriage, and the parties agree on the NFP figures — there are no facts "
        "suggesting the standard equalization would be unconscionable. The s. 5(6) "
        "variation power requires a positive finding of unconscionability; it cannot "
        "be invoked merely because the court considers a departure more equitable."
    ),
    'why_A_wrong': (
        "A reverses the direction of the payment and misunderstands the formula. "
        "The equalization payment flows from the spouse with the higher NFP to the "
        "spouse with the lower NFP. Under FLA s. 5(1), Sonja (lower NFP) is "
        "entitled to equalization — she does not pay Dimitri."
    ),
    'why_B_wrong': (
        "B is correct. Under FLA s. 5(1), Dimitri pays Sonja ($320,000 − $80,000) "
        "÷ 2 = $120,000. The equalization payment is one-half the difference between "
        "the spouses' NFPs, paid by the spouse with the higher NFP to the spouse "
        "with the lower NFP. There are no facts on these numbers warranting a s. 5(6) "
        "variation."
    ),
    'why_C_wrong': (
        "C correctly calculates the s. 5(1) entitlement of $120,000 but then "
        "misstates the operation of s. 5(6). The S.5(6)-Available-Without-Facts "
        "Trap: FLA s. 5(6) is an exceptional provision that permits the court to "
        "vary equalization only where the standard result would be unconscionable "
        "— a high threshold. On the facts given (agreed NFP figures, no excluded "
        "property, no debt at marriage), there is nothing suggesting "
        "unconscionability. Section 5(6) cannot be invoked simply because a court "
        "prefers a different result; it requires specific factual grounds such as "
        "deliberate depletion of NFP, a very short marriage, or other enumerated "
        "circumstances producing an unconscionable outcome."
    ),
    'why_D_wrong': (
        "$160,000 equals the full difference between the two NFPs, not one-half. "
        "FLA s. 5(1) entitles the lower-NFP spouse to one-half the difference — "
        "not to equalize both spouses' NFPs entirely. Paying the full difference "
        "would leave both spouses with $240,000 each, which exceeds the FLA "
        "equalization entitlement."
    ),
    'exam_trigger_words': [
        'equalization payment', 'FLA s.5(1)', 'FLA s.5(6)', 'NFP difference',
        'unconscionability', 'one-half', 'higher NFP spouse', 'direction of payment'
    ],
    'tested_concepts': [
        'FLA s.5(1) equalization formula — one-half the difference',
        'FLA s.5(6) unconscionability variation — exceptional only',
        'direction of equalization payment (higher to lower NFP)',
        'S.5(6)-Available-Without-Facts Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/family-law/ch03-nfp.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed fam-03-nfp-formula-001 and fam-03-equal-paymnt-001")

# ── ch04-matrimonial-home.json ──────────────────────────────────────────────
# fam-04-mh-possess-001  Weakness: s.19(1) stated as general rule; no competing
#   factor. Fix: add multiple-residence complication — couple has a city house
#   AND a cottage. Husband argues city house is not the matrimonial home because
#   they use the cottage as their "primary" home. Tests the MH definition.
#   Add Multiple-Residence Trap, Primary-Residence-Required Trap.

with open('data/questions/family-law/ch04-matrimonial-home.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['fam-04-mh-possess-001']
qs[i].update({
    'fact_pattern': (
        "Sandra and her husband Leon have been married for eight years. Leon is the "
        "sole registered owner of the family home in Toronto, where the couple lives "
        "and has lived throughout the marriage. They also own a cottage in Muskoka "
        "(registered jointly) where they spend four to six weeks each summer. Leon "
        "argues that the Muskoka cottage — not the Toronto home — is the matrimonial "
        "home because they spend their most enjoyable time there and he considers "
        "it their 'real' home. He further argues that Sandra has no possession rights "
        "because her name does not appear on the Toronto home's title."
    ),
    'call_of_question': (
        "Under the Family Law Act, which of the following most accurately describes "
        "Sandra's rights with respect to the Toronto home?"
    ),
    'options': {
        'A': (
            "Sandra has no right to possession of the Toronto home because she is "
            "not a registered owner and has never been on title."
        ),
        'B': (
            "The Toronto home qualifies as a matrimonial home because it is ordinarily "
            "occupied by the spouses as their family residence; Sandra has an equal "
            "right to possession under FLA s. 19(1) regardless of which spouse holds "
            "title."
        ),
        'C': (
            "Sandra has no right to possession of the Toronto home because the Muskoka "
            "cottage, jointly owned by both spouses, is the matrimonial home — only "
            "one property can be designated a matrimonial home, and the cottage "
            "qualifies because both spouses prefer it."
        ),
        'D': (
            "Sandra's right to possession of the Toronto home depends on her having "
            "contributed to mortgage payments or household expenses during the "
            "marriage."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Under FLA s. 18(1), a 'matrimonial home' is every property in which a "
        "person has an interest and that is or, if the spouses have separated, "
        "was at the time of separation ordinarily occupied by the person and his "
        "or her spouse as their family residence. The Toronto home, occupied "
        "throughout the marriage, clearly qualifies. Importantly, under FLA s. 18, "
        "there can be more than one matrimonial home — both the Toronto home and "
        "the Muskoka cottage could qualify if both are ordinarily occupied as a "
        "family residence. Leon cannot exclude the Toronto home from matrimonial "
        "home status simply by asserting a preference for the cottage. Once the "
        "Toronto home is a matrimonial home, FLA s. 19(1) grants both spouses an "
        "equal right to possession — regardless of which spouse owns it or is "
        "on title."
    ),
    'why_A_wrong': (
        "A reflects the Ownership-Determines-Possession Trap. FLA s. 19(1) "
        "expressly grants both spouses an equal right to possession of every "
        "matrimonial home regardless of which spouse owns it or appears on title. "
        "Ownership and possession rights under the FLA are entirely distinct. "
        "Legal title in one spouse does not deprive the other spouse of the s. 19(1) "
        "equal right to possession."
    ),
    'why_B_wrong': (
        "B is correct. The Toronto home is a matrimonial home under FLA s. 18 "
        "because the spouses ordinarily occupy it as their family residence. FLA "
        "s. 19(1) grants Sandra an equal right to possession regardless of "
        "ownership. Leon's argument that the cottage is the 'real' home is "
        "irrelevant — a couple can have more than one matrimonial home, and the "
        "Toronto home's ordinary occupancy throughout the marriage qualifies "
        "it independently."
    ),
    'why_C_wrong': (
        "C applies two errors. The Multiple-Residence Trap: the FLA does not limit "
        "spouses to one matrimonial home. Both the Toronto home and the Muskoka "
        "cottage could qualify as matrimonial homes simultaneously if both are "
        "ordinarily occupied as family residences. The Primary-Residence-Required "
        "Trap: a property need not be the primary or preferred residence to qualify "
        "as a matrimonial home — ordinary occupancy as a family residence suffices. "
        "Even if the cottage is also a matrimonial home, this does not displace the "
        "Toronto home's status."
    ),
    'why_D_wrong': (
        "D invents a financial-contribution requirement. The Financial-Contribution "
        "Trap: FLA s. 19(1) grants the right to possession based on marriage and the "
        "property being a matrimonial home — not on whether the non-titled spouse "
        "contributed to mortgage payments or household expenses. The right arises "
        "by statute regardless of each spouse's financial contribution to the "
        "property."
    ),
    'exam_trigger_words': [
        'matrimonial home', 'FLA s.18', 'FLA s.19(1)', 'equal possession',
        'multiple matrimonial homes', 'ownership vs possession',
        'ordinarily occupied', 'family residence', 'title irrelevant'
    ],
    'tested_concepts': [
        'FLA s.18 matrimonial home definition — ordinary occupation',
        'multiple properties can qualify as matrimonial homes simultaneously',
        'FLA s.19(1) equal possession regardless of title',
        'Ownership-Determines-Possession Trap',
        'Multiple-Residence Trap',
        'Primary-Residence-Required Trap',
        'Financial-Contribution Trap'
    ],
    'updated_at': TODAY,
})

# fam-04-excl-possess-001  Weakness: "can the court grant exclusive possession?"
#   obviously yes; s.24(3) factors not tested.
#   Fix: redesign call to test s.24(3) factors — which factor is MOST relevant.
#   Keep correct answer B but restructure options around s.24(3) factors.
#   Add Violence-Prerequisite Trap, Ownership-Override Trap, Interim-Bars-Order Trap.

i = id_map['fam-04-excl-possess-001']
qs[i].update({
    'fact_pattern': (
        "Sylvie and her husband Bernard are separating. The matrimonial home is "
        "registered in Bernard's name only. Sylvie has two children, ages 7 and 10, "
        "who are enrolled in schools one block from the matrimonial home. Bernard "
        "has not committed any act of violence and has alternative accommodation "
        "available at his parents' home. Sylvie applies for exclusive possession "
        "of the matrimonial home on an interim motion."
    ),
    'call_of_question': (
        "Which of the following most accurately describes how a court should assess "
        "Sylvie's application for exclusive possession under FLA s. 24?"
    ),
    'options': {
        'A': (
            "Sylvie's application must be dismissed because Bernard has not committed "
            "any act of violence; the absence of violence is a precondition to "
            "bringing an exclusive possession application."
        ),
        'B': (
            "The court must weigh the s. 24(3) factors including the best interests "
            "of the children (school proximity and disruption), the availability of "
            "alternative accommodation for Bernard, and any other relevant "
            "circumstances; ownership by Bernard is not a bar to the order and "
            "violence is not a precondition."
        ),
        'C': (
            "Because Bernard is the registered owner and has not committed violence, "
            "the court must give significant weight to his ownership interest — "
            "exclusive possession orders must be limited to situations involving "
            "family violence or immediate safety risk."
        ),
        'D': (
            "Exclusive possession can only be granted as part of a final parenting "
            "order; it is not available on an interim motion where final custody "
            "has not yet been determined."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Under FLA s. 24(1), the court may order exclusive possession of the "
        "matrimonial home or any part of it to one spouse, regardless of which "
        "spouse owns it, for a period of time. Section 24(3) requires the court "
        "to consider: (a) the best interests of the children; (b) the financial "
        "position of the spouses; (c) any written agreement; (d) the availability "
        "of other suitable and affordable accommodation; (e) any order or right to "
        "possession of the home; and (f) any violence committed by a spouse against "
        "the other or the children. Violence is one factor — not a precondition. "
        "Here, the children's school proximity and the disruption to their routine "
        "are strong factors under s. 24(3)(a), and Bernard's availability of "
        "alternative accommodation weighs in Sylvie's favour under s. 24(3)(d). "
        "The order is available on an interim basis."
    ),
    'why_A_wrong': (
        "A states the Violence-Prerequisite Trap. FLA s. 24(3)(f) lists violence "
        "as one factor the court must consider — it is not a precondition for "
        "an exclusive possession order. Courts grant exclusive possession in the "
        "absence of violence where other s. 24(3) factors, such as the best "
        "interests of children and availability of alternative accommodation, "
        "support the order. Requiring violence as a threshold condition "
        "misreads the FLA."
    ),
    'why_B_wrong': (
        "B is correct. Under FLA s. 24(1) and (3), the court weighs multiple "
        "factors in assessing exclusive possession. Here, the children's proximity "
        "to school (s. 24(3)(a) — best interests), Bernard's access to alternative "
        "accommodation (s. 24(3)(d)), and the absence of a written agreement "
        "(s. 24(3)(c)) are all relevant. No single factor is determinative, and "
        "ownership by Bernard is not a bar — s. 24(1) expressly permits the "
        "order regardless of which spouse owns the home."
    ),
    'why_C_wrong': (
        "C states the Ownership-Override Trap. Under FLA s. 24(1), the court may "
        "grant exclusive possession regardless of which spouse owns the home. "
        "Bernard's registered ownership is not a significant factor under s. 24(3) "
        "and is not a bar to the order. FLA s. 26 specifically preserves the titled "
        "spouse's ownership rights while allowing the other spouse to have "
        "possession — exclusive possession and ownership are separate legal "
        "concepts under the FLA."
    ),
    'why_D_wrong': (
        "D states the Interim-Bars-Order Trap. FLA s. 24 does not limit exclusive "
        "possession to final orders. Courts routinely grant exclusive possession "
        "on an interim motion pending the determination of the matrimonial home "
        "and parenting arrangements. The interim nature of the application does "
        "not bar the court from making the order — it affects the duration and "
        "whether conditions apply."
    ),
    'exam_trigger_words': [
        'exclusive possession', 'FLA s.24', 'FLA s.24(3)', 'matrimonial home',
        'best interests of children', 'alternative accommodation',
        'violence factor', 'interim exclusive possession'
    ],
    'tested_concepts': [
        'FLA s.24(1) exclusive possession regardless of ownership',
        'FLA s.24(3) factors — multi-factor balancing',
        'violence as factor not precondition',
        'Violence-Prerequisite Trap',
        'Ownership-Override Trap',
        'Interim-Bars-Order Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/family-law/ch04-matrimonial-home.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed fam-04-mh-possess-001 and fam-04-excl-possess-001")

# ── ch05-spousal-support.json ──────────────────────────────────────────────
# fam-05-ssag-001  Weakness: SSAG advisory status reachable by one phrase;
#   distractor C ("binding in Superior Court only") and D ("replaces entitlement")
#   are good traps. The core weakness: bin_logic=2 (too easy) and the scenario
#   is abstract. Fix: add applied scenario — SSAG range calculated; judge departs
#   from range; party argues this requires written justification.
#   Replace distractor C with SSAG-Departure-Requires-Written-Reasons Trap.

with open('data/questions/family-law/ch05-spousal-support.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['fam-05-ssag-001']
qs[i].update({
    'fact_pattern': (
        "Patricia and her husband Colin separated after 11 years of marriage with "
        "no dependent children. The court determines that Patricia is entitled to "
        "compensatory spousal support. Counsel calculate the SSAG range for quantum "
        "and duration, which they present to the judge. The judge awards support at "
        "an amount below the SSAG low end, citing Patricia's failure to make "
        "meaningful efforts to achieve economic self-sufficiency. Colin argues "
        "that the judge was bound to stay within the SSAG range. Patricia's "
        "counsel argues that any departure from the SSAG range automatically "
        "requires written reasons explaining the departure."
    ),
    'call_of_question': (
        "Which of the following most accurately describes the legal status of the "
        "Spousal Support Advisory Guidelines and the judge's authority to depart "
        "from the SSAG range?"
    ),
    'options': {
        'A': (
            "The SSAG are binding on Ontario courts under the Divorce Act and the "
            "FLA; the judge was not permitted to award support below the SSAG "
            "low end without the parties' consent."
        ),
        'B': (
            "The SSAG are advisory only; courts consult them for guidance on "
            "quantum and duration but are not required to follow them. The judge "
            "may depart from the SSAG range — including below the low end — based "
            "on a party's failure to pursue economic self-sufficiency, without "
            "being bound to provide written justification for the departure."
        ),
        'C': (
            "The SSAG are advisory, but any judicial departure below the SSAG low "
            "end automatically requires the court to provide written reasons "
            "explaining the departure; absent written reasons, the award is "
            "appealable as of right."
        ),
        'D': (
            "The SSAG replace the entitlement analysis; once the SSAG range "
            "produces a non-zero result, the court must order at least the "
            "minimum of the range."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "The Spousal Support Advisory Guidelines are advisory only — they have not "
        "been enacted under the Divorce Act or the Family Law Act and carry no "
        "statutory authority. Courts consult the SSAG for guidance on quantum and "
        "duration but retain full discretion to depart from the SSAG range based "
        "on the circumstances of the case. A party's failure to make reasonable "
        "efforts toward economic self-sufficiency is a recognized basis for "
        "awarding support below the SSAG range. While some case law encourages "
        "courts to explain departures from the SSAG (particularly at the appellate "
        "level), there is no mandatory rule requiring written reasons specifically "
        "for SSAG departures; the general reasons obligation in civil proceedings "
        "applies. Colin's argument that the judge was bound by the SSAG is "
        "incorrect. Patricia's counsel's argument that written reasons are "
        "automatically required for any SSAG departure overstates the obligation."
    ),
    'why_A_wrong': (
        "A misstates the legal status of the SSAG. They have not been enacted under "
        "the Divorce Act or the FLA and are not binding on any Ontario court. "
        "Courts exercise independent discretion in determining quantum and duration "
        "of spousal support; the SSAG are a tool, not a constraint."
    ),
    'why_B_wrong': (
        "B is correct. The SSAG are advisory; courts may depart from the range "
        "based on the circumstances. A payee spouse's failure to pursue economic "
        "self-sufficiency is a recognized ground for departure. No mandatory written "
        "reasons requirement for SSAG departures exists under Ontario law. The "
        "judge's award below the SSAG low end is within the court's discretion."
    ),
    'why_C_wrong': (
        "C overstates the obligation. The SSAG-Departure-Requires-Written-Reasons "
        "Trap: while courts are encouraged to address SSAG departures in their "
        "reasons (and departures may be scrutinized on appeal), there is no "
        "automatic rule that written reasons are mandatory for every SSAG departure, "
        "or that the absence of such written reasons makes the award 'appealable as "
        "of right.' The general obligation to provide adequate reasons in civil "
        "proceedings applies, but an SSAG departure alone does not trigger an "
        "independent obligation beyond that general duty."
    ),
    'why_D_wrong': (
        "D misstates how the SSAG interacts with entitlement. The SSAG apply only "
        "after the court determines that entitlement to spousal support exists — "
        "the SSAG are used to calculate quantum and duration, not to establish "
        "entitlement. A non-zero SSAG result does not establish entitlement; "
        "entitlement must be determined through the compensatory, non-compensatory, "
        "or contractual analysis first."
    ),
    'exam_trigger_words': [
        'SSAG', 'Spousal Support Advisory Guidelines', 'advisory', 'binding',
        'quantum', 'duration', 'departure from SSAG', 'economic self-sufficiency',
        'entitlement'
    ],
    'tested_concepts': [
        'SSAG advisory status — not binding',
        'court discretion to depart from SSAG range',
        'economic self-sufficiency as ground for SSAG departure',
        'SSAG applies after entitlement established',
        'SSAG-Departure-Requires-Written-Reasons Trap',
        'SSAG-Replaces-Entitlement Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/family-law/ch05-spousal-support.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed fam-05-ssag-001")

# ── ch07-parenting.json ────────────────────────────────────────────────────
# fam-07-parcoord-001  Weakness: definitional "what does a PC do?" call.
#   Fix: redesign to applied — father wants to bypass PC and go to court on a
#   scheduling dispute within the PC's mandate. Tests whether parties can
#   bypass PC.
#   Add Escalation-Always-Available Trap, PC-Cannot-Decide-Parenting-Time Trap,
#   Consensus-Required Trap.

with open('data/questions/family-law/ch07-parenting.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['fam-07-parcoord-001']
qs[i].update({
    'fact_pattern': (
        "A court order appoints a parenting coordinator for high-conflict separated "
        "parents and provides that the PC's mandate includes resolving disputes "
        "about day-to-day schedules and vacation parenting time. A dispute arises "
        "about whether the children may accompany the father on a 10-day summer "
        "vacation — a scheduling matter expressly within the PC's mandate. The "
        "father, unhappy with the PC's preliminary facilitation attempts, files a "
        "motion seeking a court order on the vacation question. He argues he has "
        "the right to return to court at any time because the PC's decisions are "
        "not truly binding and the children's best interests must be determined "
        "by a judge."
    ),
    'call_of_question': (
        "Which of the following most accurately describes the father's right to "
        "bring the vacation dispute directly to court while the PC process is "
        "ongoing?"
    ),
    'options': {
        'A': (
            "The father may return to court at any time on any matter involving "
            "the children; a court order for parenting coordination does not "
            "prevent a parent from seeking immediate judicial relief on parenting "
            "issues because parenting arrangements are always subject to the court's "
            "supervisory jurisdiction."
        ),
        'B': (
            "For disputes within the PC's mandate, the father should first complete "
            "the PC process — including the determinative phase if facilitation fails; "
            "bypassing the PC to seek immediate court relief on a matter within "
            "the mandate undermines the court-ordered dispute resolution process."
        ),
        'C': (
            "The father is correct that the PC cannot make binding decisions about "
            "vacation parenting time; that type of decision affects the children's "
            "best interests and can only be made by a judge following a full hearing."
        ),
        'D': (
            "The PC's determinations on scheduling disputes are binding only if both "
            "parents agree with the outcome; either parent may automatically refer "
            "the matter to a judge if they are dissatisfied with the PC's "
            "facilitation efforts."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Parenting coordination in Ontario is a court-ordered dispute resolution "
        "process for high-conflict families. A parenting coordinator performs two "
        "functions within the defined mandate: (1) a facilitative function — "
        "assisting parents to resolve disputes through mediation-like discussions; "
        "and (2) a determinative function — if facilitation fails, making binding "
        "decisions on issues within the mandate. For matters within the PC's "
        "mandate (here, day-to-day scheduling and vacation parenting time), "
        "parties are expected to complete the PC process — including the "
        "determinative phase if needed — before returning to court. The court "
        "retains supervisory jurisdiction and parties may seek urgent relief in "
        "true emergencies, but bypassing the PC to seek routine court orders on "
        "matters squarely within the mandate undermines the court-ordered "
        "structure. The father's vacation dispute is within the mandate and "
        "must go through the full PC process."
    ),
    'why_A_wrong': (
        "A states the Escalation-Always-Available Trap. While the court retains "
        "supervisory jurisdiction and urgent or emergency relief may be sought "
        "directly, this does not mean parties may routinely bypass a court-ordered "
        "PC to litigate every dispute. For matters within the PC mandate, the "
        "court-ordered process must be followed. Allowing unfettered escalation "
        "to court would make the PC order meaningless."
    ),
    'why_B_wrong': (
        "B is correct. Parenting coordination involves facilitation followed, if "
        "necessary, by a binding determinative decision within the mandate. For "
        "the vacation scheduling dispute — squarely within the PC's mandate — "
        "the father must complete the PC process including the determinative "
        "phase before seeking a court order. The PC's authority to make binding "
        "decisions on mandate matters is the central feature of the determinative "
        "PC role in Ontario."
    ),
    'why_C_wrong': (
        "C states the PC-Cannot-Decide-Parenting-Time Trap. Parenting coordinators "
        "in Ontario have determinative authority within their defined mandate. A "
        "vacation scheduling dispute is a classic matter within the PC's mandate "
        "and the PC is specifically authorized to make binding decisions on such "
        "issues. The PC's authority is not limited to procedural or administrative "
        "matters — it extends to parenting time disputes as defined in the court "
        "order appointing the PC."
    ),
    'why_D_wrong': (
        "D states the Consensus-Required Trap. The PC's authority in the "
        "determinative phase is not consensual — the PC may make a binding decision "
        "even if one party (or both) disagrees with the outcome. The determinative "
        "PC function is binding precisely because it does not require consensus. "
        "If either parent's dissatisfaction could trigger automatic court "
        "escalation, the binding nature of the PC process would be entirely "
        "undermined."
    ),
    'exam_trigger_words': [
        'parenting coordinator', 'PC mandate', 'facilitative', 'determinative',
        'binding decision', 'high-conflict', 'bypass court', 'vacation parenting',
        'court-ordered dispute resolution'
    ],
    'tested_concepts': [
        'parenting coordinator hybrid role — facilitative and determinative',
        'PC mandate defines scope of binding authority',
        'parties cannot bypass PC for in-mandate disputes',
        'Escalation-Always-Available Trap',
        'PC-Cannot-Decide-Parenting-Time Trap',
        'Consensus-Required Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/family-law/ch07-parenting.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed fam-07-parcoord-001")

# ── ch13-common-law.json ───────────────────────────────────────────────────
# fam-13-cl-fla29-001  Weakness: definitional recall on 3-year threshold;
#   no borderline cohabitation facts.
#   Fix: add interrupted cohabitation facts — 2 years together, 5-month break,
#   then 2 more years. Tests whether "continuous" cohabitation is satisfied.
#   Add Interrupted-Cohabitation Trap; change scenario slightly so qualification
#   is genuinely uncertain, making entitlement grounds the secondary issue.
#   Actually: keep question about entitlement grounds (compensatory etc.) but
#   add a better FP with specific economic disadvantage facts rather than
#   pure definitional call.

with open('data/questions/family-law/ch13-common-law.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['fam-13-cl-fla29-001']
qs[i].update({
    'fact_pattern': (
        "Michelle cohabited continuously with Dan for four and a half years and "
        "qualifies as a 'spouse' under FLA s. 29. During the relationship, Michelle "
        "gave up a full-time marketing career to manage the household and support "
        "Dan's growing business — she worked unpaid in his business for two years. "
        "On separation, Michelle is unemployed and has diminished career prospects. "
        "Dan's counsel argues that because Michelle and Dan were not married, she "
        "is limited to needs-based support only and cannot claim compensatory "
        "entitlement, which counsel says is available only to married spouses "
        "under the Divorce Act."
    ),
    'call_of_question': (
        "Which of the following most accurately states the entitlement grounds "
        "available to Michelle in her spousal support claim under the Family Law "
        "Act?"
    ),
    'options': {
        'A': (
            "Common-law spousal support under the FLA is limited to needs-based "
            "(non-compensatory) grounds only; compensatory entitlement is available "
            "only under the Divorce Act for married spouses, not under the FLA "
            "for qualifying common-law partners."
        ),
        'B': (
            "As a qualifying spouse under FLA s. 29, Michelle's support claim is "
            "assessed under FLA Part III (s. 33) on the same substantive basis as "
            "for a married spouse — all three entitlement grounds (compensatory, "
            "non-compensatory, and contractual) are available; Dan's counsel's "
            "argument is incorrect."
        ),
        'C': (
            "Common-law spousal support under the FLA is always compensatory only; "
            "needs-based or non-compensatory entitlement is not available to "
            "qualifying FLA spouses."
        ),
        'D': (
            "FLA s. 29 qualifying spouses have access to all entitlement grounds, "
            "but compensatory support is limited to a maximum of three years to "
            "reflect the shorter duration of a typical unmarried relationship."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Once a person qualifies as a 'spouse' under FLA s. 29 (by continuous "
        "cohabitation for not less than three years), their spousal support claim "
        "is assessed under Part III of the FLA — specifically s. 33 — on the same "
        "substantive basis as for a married spouse. The FLA s. 33 support factors "
        "include the claimant's role in the relationship and any economic advantages "
        "or disadvantages arising from the relationship or its breakdown. Michelle's "
        "career sacrifice and unpaid work in Dan's business are paradigmatic "
        "compensatory entitlement facts under the Bracklow v Bracklow framework. "
        "All three entitlement grounds — compensatory (relationship-generated "
        "economic disadvantage), non-compensatory (financial need), and contractual "
        "(domestic contracts) — are available. Dan's counsel is wrong to assert "
        "that compensatory support is limited to the Divorce Act."
    ),
    'why_A_wrong': (
        "A misstates the law on entitlement grounds for FLA spouses. The "
        "Compensatory-Divorced-Spouses-Only Trap: compensatory spousal support "
        "entitlement is not limited to the Divorce Act or to formally married "
        "spouses. The FLA s. 33 support framework incorporates all three grounds "
        "developed in Bracklow v Bracklow — compensatory, non-compensatory, and "
        "contractual — and applies them to qualifying FLA spouses in the same way "
        "as to married spouses under the Divorce Act. Michelle's career sacrifice "
        "and economic disadvantage are exactly the type of facts that ground "
        "compensatory entitlement."
    ),
    'why_B_wrong': (
        "B is correct. Qualifying common-law spouses under FLA s. 29 have access "
        "to all three entitlement grounds under FLA Part III (s. 33). Michelle "
        "can assert compensatory entitlement based on her career sacrifice and "
        "unpaid work in Dan's business, non-compensatory entitlement based on "
        "economic need post-separation, or both. Dan's argument that compensatory "
        "support is limited to the Divorce Act is incorrect; the FLA applies the "
        "same framework."
    ),
    'why_C_wrong': (
        "C reverses the error in A. While non-compensatory (needs-based) support "
        "is available to FLA qualifying spouses, the claim is not limited to "
        "non-compensatory grounds. Compensatory support — addressing economic "
        "disadvantages arising from the relationship — is equally available. "
        "The FLA s. 33 framework does not privilege one entitlement ground over "
        "another; courts assess all applicable grounds on the facts."
    ),
    'why_D_wrong': (
        "D invents a three-year cap that does not appear anywhere in the FLA or "
        "case law. The Three-Year-Cap Trap: the duration of compensatory spousal "
        "support is determined by the circumstances of the relationship, the degree "
        "of economic disadvantage, and the claimant's pathway to self-sufficiency — "
        "not by a fixed maximum based on the form of the relationship. The FLA and "
        "the SSAG do not impose an automatic durational cap on compensatory support "
        "for common-law partners."
    ),
    'exam_trigger_words': [
        'FLA s.29', 'common-law spouse', 'compensatory support',
        'non-compensatory support', 'FLA Part III', 'FLA s.33',
        'Bracklow', 'entitlement grounds', 'career sacrifice', 'qualifying spouse'
    ],
    'tested_concepts': [
        'FLA s.29 qualifying spouses — same entitlement grounds as married spouses',
        'compensatory entitlement available under FLA s.33',
        'all three Bracklow grounds apply to FLA spouses',
        'Compensatory-Divorced-Spouses-Only Trap',
        'Three-Year-Cap Trap'
    ],
    'updated_at': TODAY,
})

# fam-13-cl-supp-002  Weakness: distractor C ("automatically reduced by 50%")
#   implausibly wrong; call slightly abstract.
#   Fix: replace C with a more sophisticated wrong answer about SSAG formula
#   selection — "courts apply only 'without children' formula for CL partners."
#   Add Wrong-Formula-for-CL-Partners Trap.

i = id_map['fam-13-cl-supp-002']
qs[i].update({
    'options': {
        'A': (
            "No — the SSAG are only applicable under the Divorce Act and cannot "
            "be used in FLA support proceedings for common-law partners."
        ),
        'B': (
            "Yes — the SSAG apply to spousal support claims under both the Divorce "
            "Act (for married spouses) and the Family Law Act (for qualifying "
            "common-law partners who meet the FLA s. 29 definition); Dan's "
            "counsel's argument is incorrect."
        ),
        'C': (
            "Yes — but for common-law partners, courts must apply only the 'without "
            "children' SSAG formula regardless of whether the couple had children, "
            "because the 'with children' formula was designed exclusively for "
            "married spouses under the Divorce Act."
        ),
        'D': (
            "No — common-law partners must apply a separate Ontario-specific formula "
            "developed for FLA spousal support claims, not the national SSAG "
            "developed for Divorce Act purposes."
        ),
    },
    'why_C_wrong': (
        "C misstates how the SSAG formula is selected. The Wrong-Formula-for-CL "
        "Partners Trap: the SSAG formulas — 'without children,' 'with children,' "
        "and 'custodial payor' — are selected based on the actual circumstances "
        "of the relationship and the arrangement of parenting responsibilities, "
        "not on the formal status (married vs. common-law) of the parties. "
        "If Lisa and Dan had dependent children whose care affected the economic "
        "interdependence of the relationship, the 'with children' formula would "
        "apply just as it would for married spouses. The SSAG explicitly extend "
        "to FLA support claims and make no distinction in formula selection based "
        "solely on marital status."
    ),
    'updated_at': TODAY,
})

with open('data/questions/family-law/ch13-common-law.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed fam-13-cl-fla29-001 and fam-13-cl-supp-002")

print("\nAll family law improvements applied.")
