#!/usr/bin/env python3
"""Phase 2K-Improve-B5: Criminal Law IMPROVE questions."""
import json, os
from datetime import date

os.chdir('/Users/muhammad/Downloads/railway-deploy')
TODAY = date.today().isoformat()

# ── ch02-charter-arrest.json ───────────────────────────────────────────────
# crim-02-s10b-001  Weakness: Informational/implementational taxonomy stated
#   directly; single obvious fact (questions before informing of right) makes
#   answer mechanical.
#   Fix: enrich FP — police also fail to give reason for arrest (s.10(a)) and
#   start questioning. Now candidates must distinguish s.10(a) vs s.10(b) as
#   the PRIMARY breach. Correct: B (s.10(b)) — questioning without informing
#   of right to counsel is the core breach; failing to state reasons is
#   s.10(a), which is also breached but s.10(b) is most precisely on point
#   given the questions began before any counsel rights information.
#   Add s10a-vs-s10b Trap, s7-Catch-All Trap, s11c-Testimonial-Compulsion Trap.

with open('data/questions/criminal-law/ch02-charter-arrest.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['crim-02-s10b-001']
qs[i].update({
    'fact_pattern': (
        "Police arrest Kwame on reasonable grounds for fraud. At the moment of "
        "arrest, the arresting officer does not inform Kwame of the reason for his "
        "arrest. The officer immediately begins asking Kwame detailed questions "
        "about the alleged scheme. At no point before or during questioning does "
        "the officer say anything to Kwame about his right to retain and instruct "
        "counsel. Kwame makes incriminating statements during the questioning."
    ),
    'call_of_question': (
        "Which Charter right was most precisely and directly violated by the "
        "officer's conduct in questioning Kwame before informing him of his right "
        "to retain and instruct counsel?"
    ),
    'options': {
        'A': (
            "Section 10(a) — the right to be informed promptly of the reasons for "
            "arrest or detention, which was violated when the officer failed to "
            "state the reason for the arrest."
        ),
        'B': (
            "Section 10(b) — the right to retain and instruct counsel without delay "
            "and to be informed of that right, which was violated when the officer "
            "began questioning Kwame without first informing him of his right to "
            "counsel."
        ),
        'C': (
            "Section 7 — the right to life, liberty, and security of the person, "
            "because Kwame's liberty was infringed without respect for the principles "
            "of fundamental justice."
        ),
        'D': (
            "Section 11(c) — the right not to be compelled to be a witness against "
            "oneself in criminal proceedings, because the officer questioned Kwame "
            "before he could assert his right to silence."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Section 10(b) of the Charter guarantees that everyone arrested or detained "
        "has the right to retain and instruct counsel without delay and to be "
        "informed of that right. The Supreme Court in R v Manninen, [1987] 1 SCR "
        "1233, held that s. 10(b) imposes both an informational duty (tell the "
        "detained person of the right to counsel) and an implementational duty "
        "(provide a reasonable opportunity to exercise that right and hold off "
        "questioning until that opportunity is given). Here, the officer began "
        "questioning Kwame without first informing him of his s. 10(b) rights — "
        "a direct breach of s. 10(b). While s. 10(a) was also engaged (the officer "
        "did not state the reason for arrest), s. 10(b) is the most precisely "
        "applicable right given the specific conduct of questioning before informing "
        "of the right to counsel."
    ),
    'why_A_wrong': (
        "A identifies a genuine Charter breach (s. 10(a) was also violated when "
        "the officer did not state the reason for the arrest), but it is not the "
        "provision most precisely and directly violated by the act of questioning "
        "before informing of the right to counsel. The s.10(a)-vs-s.10(b) Trap: "
        "the call asks about the breach arising from questioning without informing "
        "of counsel rights — that is s. 10(b). Section 10(a) governs the right to "
        "be informed of the reasons for arrest, a distinct (though also violated) "
        "right. Candidates must identify which specific right corresponds to the "
        "specific conduct described."
    ),
    'why_B_wrong': (
        "B is correct. Section 10(b) requires that: (1) the person be informed of "
        "their right to retain and instruct counsel without delay; and (2) they be "
        "given a reasonable opportunity to exercise that right before police "
        "continue with the investigative purpose of the detention. The officer here "
        "did neither — no information was given about the right to counsel, and "
        "questioning began immediately. This is a textbook s. 10(b) breach "
        "confirmed in R v Manninen and R v Bartle, [1994] 3 SCR 173."
    ),
    'why_C_wrong': (
        "C is too broad. The s.7-Catch-All Trap: section 7 guarantees the right "
        "to life, liberty, and security of the person in accordance with the "
        "principles of fundamental justice. A breach of s. 10(b) will often also "
        "engage s. 7, but s. 7 is a residual provision. When a more specific "
        "Charter right directly addresses the conduct at issue — here, s. 10(b) "
        "for the failure to inform of the right to counsel before questioning — "
        "that specific provision governs. Courts analyze s. 7 when no more "
        "specific right applies."
    ),
    'why_D_wrong': (
        "D confuses distinct Charter rights. The s.11(c)-Testimonial-Compulsion "
        "Trap: section 11(c) protects an accused from being compelled to testify "
        "against themselves in criminal proceedings — it concerns the right not "
        "to be put on the witness stand against one's will at trial. It does not "
        "govern pre-trial police questioning. The right to silence during "
        "investigative detention arises under s. 7 (right to silence) and the "
        "right to counsel under s. 10(b) — not under s. 11(c), which is a "
        "trial-stage protection."
    ),
    'exam_trigger_words': [
        's.10(b)', 'right to counsel', 'informational duty', 'implementational duty',
        'arrest', 'questioning', 's.10(a)', 'Charter', 'Manninen', 'counsel without delay'
    ],
    'tested_concepts': [
        's.10(b) informational and implementational duties',
        's.10(a) vs s.10(b) distinction',
        's.11(c) trial-stage testimonial compulsion',
        's.7 as residual vs specific rights',
        's.10(a)-vs-s.10(b) Trap',
        's.7-Catch-All Trap',
        's.11(c)-Testimonial-Compulsion Trap'
    ],
    'updated_at': TODAY,
})

# crim-02-cit-arrest-003  Weakness: s.494(1)(a)/(b) distinction telegraphed;
#   distractor D (unlimited time, good faith) too obviously wrong.
#   Fix: replace D with a more sophisticated wrong answer about citizen's
#   authority to detain pending voluntary compensation agreement.
#   Add Voluntary-Settlement-Authority Trap.

i = id_map['crim-02-cit-arrest-003']
qs[i].update({
    'options': {
        'A': (
            "The arrest was valid under s. 494(1)(a) because Dimitri personally "
            "witnessed an indictable offence being committed, and there is no duty "
            "to deliver the arrested person to police if the citizen chooses to "
            "escort him to the owner of the property."
        ),
        'B': (
            "The arrest may be justified under s. 494(1)(b) if Dimitri reasonably "
            "believed the man committed an indictable offence and was freshly "
            "pursuing him; however, s. 494(3) requires Dimitri to deliver the "
            "arrested person to police forthwith."
        ),
        'C': (
            "The arrest is unlawful because s. 494 applies only to property owners "
            "and the car was not Dimitri's property."
        ),
        'D': (
            "The arrest is valid and Dimitri may detain the man at his residence "
            "until the man agrees to compensate the car owner, because s. 494 "
            "authorizes a citizen to take reasonable steps to recover stolen "
            "property on behalf of the victim."
        ),
    },
    'why_D_wrong': (
        "D invents an authority that s. 494 does not confer. The "
        "Voluntary-Settlement-Authority Trap: section 494 authorizes the arrest "
        "of a person and requires immediate delivery to police — it does not "
        "authorize the arresting citizen to detain the person indefinitely, "
        "negotiate compensation, or act as an enforcement agent for the victim. "
        "Detaining a person to coerce compensation would constitute unlawful "
        "confinement. The mandatory delivery obligation in s. 494(3) is immediate "
        "and unconditional; it cannot be suspended to pursue private resolution."
    ),
    'updated_at': TODAY,
})

# crim-02-sita-004  Weakness: distractor B ("phone was unlocked, removing privacy
#   expectation") too obviously wrong.
#   Fix: replace B with a more sophisticated wrong answer about SITA relatedness —
#   e.g., the shoplifting involved photographing store items on phone.
#   Add Post-Hoc-Rationalization Trap.

i = id_map['crim-02-sita-004']
qs[i].update({
    'options': {
        'A': (
            "The search is valid because SITA authorized the seizure of the phone, "
            "and any evidence found during a search of a lawfully seized item is "
            "admissible regardless of when or how the search was conducted."
        ),
        'B': (
            "The search is valid because the shoplifting offence involved Ingrid "
            "photographing store products on her phone to track them for resale, "
            "so the phone was directly related to the commission of the offence "
            "and its contents were properly subject to search incident to arrest."
        ),
        'C': (
            "The search violates s. 8 of the Charter on multiple grounds: it was "
            "not conducted promptly at the time of arrest, it was a full data "
            "review rather than a limited targeted search, and any evidence found "
            "was unrelated to shoplifting."
        ),
        'D': (
            "The search is valid because the evidence discovered, while relating "
            "to a different offence, was found during a lawful SITA search and "
            "is therefore admissible under the plain-view doctrine."
        ),
    },
    'why_B_wrong': (
        "B applies a post-hoc rationalization of relatedness that Fearon does not "
        "permit. The Post-Hoc-Rationalization Trap: under R v Fearon, 2014 SCC 77, "
        "a SITA search of a cell phone must be truly incidental to the arrest — "
        "meaning the purpose of the search must be genuinely connected to the "
        "reason for the arrest (officer safety, preventing evidence destruction, "
        "or discovering evidence related to the arrested offence). The relatedness "
        "assessment must be made at the time of and during the search, not "
        "constructed retrospectively. Here, the search was conducted two hours "
        "post-arrest at the police station — not at the scene — and was a full "
        "data review, not a targeted search for evidence of shoplifting. Even if "
        "the phone was hypothetically used in the shoplifting, these temporal and "
        "scope violations independently invalidate the search under Fearon."
    ),
    'updated_at': TODAY,
})

with open('data/questions/criminal-law/ch02-charter-arrest.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed crim-02-s10b-001, crim-02-cit-arrest-003, crim-02-sita-004")

# ── ch03-bail.json ─────────────────────────────────────────────────────────
# crim-03-rev-onus-001  Weakness: trafficking too clear a listed offence;
#   distractor D ("reverse onus for all serious charges") is too obviously wrong.
#   Fix: redesign FP — Fatima charged with possession for the purpose of
#   trafficking (s.5(2) CDSA), her counsel argues this is possession (s.4),
#   not trafficking, and reverse onus doesn't apply. Tests whether s.515(6)(d)
#   covers s.5(2) CDSA. Add Possession-vs-Trafficking Trap; replace D.

with open('data/questions/criminal-law/ch03-bail.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['crim-03-rev-onus-001']
qs[i].update({
    'fact_pattern': (
        "Fatima is charged with possession of a controlled substance for the "
        "purpose of trafficking contrary to s. 5(2) of the Controlled Drugs and "
        "Substances Act. She has no prior criminal record. At her bail hearing, "
        "her counsel argues that s. 515(6) reverse onus should not apply because "
        "her charge is possession-for-the-purpose, not trafficking per se under "
        "s. 5(1) CDSA, and the informational burden should therefore remain on "
        "the Crown. The justice disagrees and informs Fatima that she bears the "
        "burden of showing cause why her detention is not justified."
    ),
    'call_of_question': (
        "Is the justice correct that Fatima bears the burden at this bail hearing?"
    ),
    'options': {
        'A': (
            "No — the Crown always bears the burden of showing cause for detention "
            "in all criminal matters; the reverse onus provisions of s. 515(6) are "
            "constitutionally inapplicable because they violate s. 11(e) of the "
            "Charter."
        ),
        'B': (
            "Yes — under s. 515(6)(d) of the Criminal Code, a person charged with "
            "an offence under s. 5 of the CDSA — which includes both trafficking "
            "(s. 5(1)) and possession for the purpose of trafficking (s. 5(2)) — "
            "bears the burden of showing cause why their detention is not justified."
        ),
        'C': (
            "No — counsel is correct that reverse onus under s. 515(6)(d) applies "
            "only to the trafficking offence in s. 5(1) CDSA, not to possession "
            "for the purpose of trafficking in s. 5(2), because only trafficking "
            "per se involves an element of distribution."
        ),
        'D': (
            "Yes — the justice is correct, but only because Fatima has been charged "
            "with a serious drug offence; s. 515(6) reverse onus applies to all "
            "criminal offences where the Crown considers the accused a flight risk."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Section 515(6)(d) of the Criminal Code imposes reverse onus — requiring "
        "the accused to show cause why detention is not justified — where the "
        "accused is charged with an offence under s. 5 of the Controlled Drugs "
        "and Substances Act. Section 5 of the CDSA contains two subsections: "
        "s. 5(1) (trafficking in a controlled substance) and s. 5(2) (possession "
        "of a controlled substance for the purpose of trafficking). Both offences "
        "fall within 'an offence under s. 5 of the CDSA.' Fatima's counsel is "
        "wrong to argue that only s. 5(1) triggers s. 515(6)(d) — the reverse "
        "onus provision covers any offence under that section. Fatima must show "
        "cause why her detention is not justified."
    ),
    'why_A_wrong': (
        "A misstates the constitutional status of s. 515(6). The Supreme Court of "
        "Canada upheld the constitutionality of reverse onus bail provisions in "
        "R v Pearson, [1992] 3 SCR 665, and R v Morales, [1992] 3 SCR 711. "
        "Reverse onus in bail does not violate s. 11(e) of the Charter when "
        "connected to a substantial state interest such as drug trafficking offences. "
        "The Crown's general burden applies in ordinary bail hearings; the statutory "
        "exceptions in s. 515(6) are constitutionally valid."
    ),
    'why_B_wrong': (
        "B is correct. Section 515(6)(d) applies to any offence under s. 5 of the "
        "CDSA. Section 5 encompasses both s. 5(1) (trafficking) and s. 5(2) "
        "(possession for the purpose of trafficking). Fatima's counsel's argument "
        "that only trafficking per se under s. 5(1) triggers the reverse onus is "
        "incorrect — the statutory language refers to 'an offence under s. 5,' "
        "which covers both subsections. The justice is correct that Fatima bears "
        "the burden."
    ),
    'why_C_wrong': (
        "C adopts counsel's erroneous argument. The Possession-vs-Trafficking Trap: "
        "s. 515(6)(d) refers to 'an offence under s. 5' of the CDSA, not 'an "
        "offence under s. 5(1)' specifically. Both possession for the purpose of "
        "trafficking (s. 5(2)) and trafficking per se (s. 5(1)) are offences under "
        "s. 5. Courts have consistently applied the reverse onus to s. 5(2) charges "
        "on this basis. The fact that s. 5(2) involves possession rather than "
        "distribution does not exclude it from the s. 515(6)(d) reverse onus."
    ),
    'why_D_wrong': (
        "D correctly identifies that the justice is right but states the wrong "
        "reason. The All-Serious-Charges Trap: s. 515(6) does not apply to all "
        "serious criminal offences or whenever the Crown considers the accused a "
        "flight risk. It is triggered only by specific, enumerated circumstances "
        "in s. 515(6)(a)–(h). The Crown's subjective assessment of flight risk "
        "is irrelevant to whether s. 515(6) applies — the reverse onus is a "
        "statutory rule tied to the nature of the charge, not the Crown's "
        "characterization of the accused's risk level."
    ),
    'exam_trigger_words': [
        's.515(6)', 'reverse onus', 'bail', 'CDSA s.5', 'trafficking',
        'possession for purpose of trafficking', 'show cause', 'Crown burden'
    ],
    'tested_concepts': [
        's.515(6)(d) reverse onus for CDSA s.5 offences',
        'CDSA s.5(1) vs s.5(2) — both covered by s.515(6)(d)',
        'constitutional validity of reverse onus bail',
        'Possession-vs-Trafficking Trap',
        'All-Serious-Charges Trap',
        'Charter s.11(e) and bail reverse onus'
    ],
    'updated_at': TODAY,
})

with open('data/questions/criminal-law/ch03-bail.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed crim-03-rev-onus-001")

# ── ch08-defences.json ─────────────────────────────────────────────────────
# crim-08-colour-right-001  Weakness: rationale doesn't name distractor trap
#   types; FP (removing lumber as "collateral") too abstract.
#   Fix: enrich FP — oral promise by developer ("if I don't pay by Friday, take
#   the lumber"); tests whether oral promise grounds colour of right.
#   Add Valid-Security-Interest Trap, Moral-Claim Trap, Formality-Required Trap.

with open('data/questions/criminal-law/ch08-defences.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['crim-08-colour-right-001']
qs[i].update({
    'fact_pattern': (
        "Nathan is a contractor who completed renovation work for a developer, "
        "Victor. Victor did not pay Nathan by the agreed date. During a heated "
        "conversation, Victor said to Nathan: 'If I don't pay you by Friday, you "
        "can take the lumber I have stored on site.' Friday passed without payment. "
        "Relying on Victor's statement, Nathan went to the site and removed the "
        "lumber. Victor then reported the lumber missing. Nathan is charged with "
        "theft. Nathan testifies that he genuinely believed Victor's statement "
        "gave him a legal right to take the lumber, although he acknowledges the "
        "statement was oral and no formal agreement was documented."
    ),
    'call_of_question': (
        "Which of the following correctly states the colour of right doctrine as "
        "it applies to Nathan's situation?"
    ),
    'options': {
        'A': (
            "Colour of right is unavailable because Nathan did not have a legally "
            "valid right to the lumber — the oral statement by Victor is not a "
            "registered security interest, lien, or court order, and therefore "
            "cannot ground the defence."
        ),
        'B': (
            "Colour of right applies where the accused honestly believed he had a "
            "legal entitlement to the property taken — the belief need not be "
            "correct or legally reasonable, but it must be a belief in a legal "
            "right, not merely a moral claim; if Nathan genuinely believed "
            "Victor's statement conferred a legal right to take the lumber, "
            "the defence is available."
        ),
        'C': (
            "Colour of right is established because Victor owed Nathan money for "
            "completed work; a creditor who takes property to satisfy an unpaid "
            "debt has a recognized moral and legal right to do so, making the "
            "defence automatically available."
        ),
        'D': (
            "Colour of right is not available for property taken from commercial "
            "premises; it applies only to property found on public land or land "
            "to which the accused has a lawful right of access."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Colour of right under s. 322(1)(a) of the Criminal Code provides a defence "
        "to theft where the accused honestly believed he had a legal right or title "
        "to the property taken. The key elements are: (1) the accused had an honest "
        "belief in a legal entitlement to the property; (2) the belief need not be "
        "reasonable (the test is subjective); but (3) the belief must be in a legal "
        "right, not merely a moral claim such as believing one is owed money. Victor's "
        "oral statement — 'if I don't pay you by Friday, you can take the lumber' — "
        "could ground an honest belief in a legal right to the lumber if Nathan "
        "genuinely believed the statement conferred that right. The belief does not "
        "need to be legally correct (colour of right does not require a valid "
        "enforceable agreement); it requires only that the belief was honest and "
        "pertained to a legal entitlement."
    ),
    'why_A_wrong': (
        "A requires legal validity of the right, which colour of right does not. "
        "The Valid-Security-Interest Trap: colour of right does not require the "
        "accused to have a registered lien, security interest, or court order. "
        "The defence requires only an honest belief in a legal entitlement — not "
        "that the entitlement actually exists or is legally enforceable. An honest "
        "belief that an oral statement conferred the right to take property is "
        "sufficient to ground the defence, even if the agreement would not be "
        "enforceable as a security interest."
    ),
    'why_B_wrong': (
        "B is correct. Colour of right requires an honest, subjective belief in a "
        "legal entitlement to the property taken. That belief need not be correct "
        "in law, but it must be a belief in a legal right — not merely a moral "
        "grievance about being owed money. Victor's oral promise could ground such "
        "a belief if Nathan genuinely understood it as conferring a legal right to "
        "the lumber. The fact that the agreement was oral and informal does not "
        "prevent Nathan from honestly believing it gave him a legal entitlement."
    ),
    'why_C_wrong': (
        "C collapses the distinction between moral claims and legal rights. The "
        "Moral-Claim Trap: a creditor who is owed money has a contractual claim "
        "against the debtor — not a right to seize property as self-help. Being "
        "owed money does not automatically give a creditor a legal right to take "
        "the debtor's property. Colour of right requires a belief in a legal "
        "entitlement to the specific property taken, not merely a belief that one "
        "is owed money by the property owner. Automatic availability based on any "
        "debt relationship is not the law."
    ),
    'why_D_wrong': (
        "D invents a categorical restriction that does not exist. The "
        "Premises-Restriction Trap: colour of right is not limited by the type "
        "of premises on which the property is located. It applies to any property "
        "offence regardless of whether the property is on commercial premises, "
        "private land, or public land. The defence turns on the accused's honest "
        "belief in a legal entitlement to the specific property taken — not on "
        "where the property was located."
    ),
    'exam_trigger_words': [
        'colour of right', 's.322', 'theft', 'honest belief', 'legal entitlement',
        'subjective test', 'moral claim', 'oral promise', 'Criminal Code defence'
    ],
    'tested_concepts': [
        'colour of right — subjective honest belief in legal entitlement',
        'legal right vs moral claim distinction',
        'oral agreement as basis for colour of right',
        'Valid-Security-Interest Trap',
        'Moral-Claim Trap',
        'Premises-Restriction Trap'
    ],
    'updated_at': TODAY,
})

# crim-08-ncr-001  Weakness: "alien invader" FP unrealistic; distractor D
#   ("lacked motive") obviously wrong for any bar candidate.
#   Fix: realistic FP (paranoid schizophrenia, believed neighbour was threat);
#   replace D with NCR-vs-Self-Defence Trap.

i = id_map['crim-08-ncr-001']
qs[i].update({
    'fact_pattern': (
        "The accused, Raymond, is charged with assault causing bodily harm. "
        "Psychiatric evidence at trial establishes that Raymond has paranoid "
        "schizophrenia and that at the time of the assault, his disorder caused "
        "him to believe his neighbour was about to kill him. Acting on this "
        "delusion, Raymond struck his neighbour first, believing he was defending "
        "himself. Both the Crown and defence experts agree Raymond was suffering "
        "from a severe psychotic episode at the time and that his belief, though "
        "entirely delusional, was sincerely held."
    ),
    'call_of_question': (
        "Under s. 16(1) of the Criminal Code, on what ground is Raymond's NCR "
        "defence based?"
    ),
    'options': {
        'A': (
            "Raymond did not commit the physical act of the assault because his "
            "movements were controlled by the mental disorder, negating the actus "
            "reus."
        ),
        'B': (
            "Raymond is not criminally responsible because his mental disorder "
            "rendered him incapable of knowing that the act was wrong — he "
            "genuinely believed, by reason of his disorder, that he was acting "
            "in lawful self-defence."
        ),
        'C': (
            "Raymond acted in a dissociative automatism-like state and therefore "
            "lacked the voluntary act required for criminal liability."
        ),
        'D': (
            "Because Raymond sincerely believed he was acting in self-defence, "
            "the substantive defence of self-defence under s. 34 of the Criminal "
            "Code applies — the NCR defence is unnecessary and unavailable where "
            "a justification defence exists."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Section 16(1) of the Criminal Code provides that no person is criminally "
        "responsible for an act committed while suffering from a mental disorder "
        "that rendered them incapable of: (a) appreciating the nature and quality "
        "of the act; or (b) knowing that the act was wrong. Here, Raymond "
        "committed the physical act consciously (he chose to strike his neighbour) "
        "and appreciated its physical character (an assault). The operative NCR "
        "ground is (b): his disorder rendered him incapable of knowing the act "
        "was wrong, because he genuinely believed — by reason of his psychotic "
        "delusion — that he was acting in lawful self-defence. This is the "
        "'wrong' prong of s. 16(1)."
    ),
    'why_A_wrong': (
        "A misidentifies the basis of the NCR defence. The Actus-Reus-Negation "
        "Trap: the NCR defence does not operate by negating the actus reus. "
        "Raymond committed the physical act of the assault voluntarily and "
        "consciously — his mental disorder did not eliminate the voluntary act. "
        "The NCR defence operates at the level of criminal responsibility, not "
        "by denying that the act occurred. Automatism (which does negate the "
        "actus reus) is a distinct defence based on involuntary movement."
    ),
    'why_B_wrong': (
        "B is correct. Under s. 16(1)(b), the NCR defence applies where the "
        "mental disorder rendered the accused incapable of knowing that the act "
        "was wrong. Raymond's paranoid schizophrenia caused him to believe he "
        "was lawfully defending himself — he could not appreciate the wrongfulness "
        "of his conduct because his disorder displaced that appreciation entirely. "
        "This is the 'wrong' prong of the s. 16(1) NCR defence."
    ),
    'why_C_wrong': (
        "C conflates NCR with automatism. The Automatism-vs-NCR Trap: automatism "
        "involves an involuntary bodily act — the accused's body moves without "
        "conscious control, negating the voluntary act element of the actus reus. "
        "Raymond's act was not involuntary in this sense — he consciously decided "
        "to strike his neighbour. His mental disorder affected his perception of "
        "reality and his moral understanding of the act, not the voluntary "
        "character of his physical movement. These are distinct legal doctrines."
    ),
    'why_D_wrong': (
        "D confuses the NCR defence with the justification defence of self-defence. "
        "The NCR-vs-Self-Defence Trap: the s. 34 defence of self-defence applies "
        "where the accused's belief in the need to defend themselves was objectively "
        "reasonable in the circumstances. Raymond's belief was delusional — no "
        "objectively reasonable person would have perceived the neighbour as a "
        "threat. The defence of self-defence is unavailable on these facts. The "
        "NCR defence under s. 16(1)(b) is specifically designed for accused whose "
        "mental disorder caused a delusional belief that their act was justified "
        "— precisely Raymond's situation."
    ),
    'exam_trigger_words': [
        'NCR', 's.16(1)', 'mental disorder', 'not criminally responsible',
        'wrong prong', 'appreciation prong', 'paranoid schizophrenia',
        'delusional belief', 'self-defence', 'automatism'
    ],
    'tested_concepts': [
        's.16(1) NCR defence — two grounds: appreciate/know wrong',
        'wrong prong of NCR vs self-defence',
        'NCR vs automatism distinction',
        'Actus-Reus-Negation Trap',
        'Automatism-vs-NCR Trap',
        'NCR-vs-Self-Defence Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/criminal-law/ch08-defences.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed crim-08-colour-right-001 and crim-08-ncr-001")

# ── ch09-sentencing.json ────────────────────────────────────────────────────
# crim-09-rest-001  Weakness: rule-recall; distractors don't trap around
#   objectives interaction or whether restorative justice excludes other goals.
#   Fix: redesign call — Crown pushes for denunciation alongside restorative
#   process; test whether s.718 objectives are mutually exclusive.
#   Add Mutually-Exclusive-Objectives Trap, Incapacitation-as-Restorative Trap.

with open('data/questions/criminal-law/ch09-sentencing.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['crim-09-rest-001']
qs[i].update({
    'fact_pattern': (
        "A first-time offender pleads guilty to mischief. The defence proposes "
        "participation in a community conference and a restorative justice program "
        "under which the offender will meet with the victim, acknowledge the harm, "
        "and pay restitution. The Crown supports the restorative component but also "
        "argues that denunciation of the conduct remains appropriate and should be "
        "reflected in the sentence alongside the restorative measures. The defence "
        "objects, arguing that denunciation is incompatible with restorative "
        "justice and that including it would undermine the restorative process."
    ),
    'call_of_question': (
        "Under the Criminal Code sentencing framework, which of the following most "
        "accurately describes the relationship between restorative justice objectives "
        "and denunciation?"
    ),
    'options': {
        'A': (
            "Denunciation and restorative justice are incompatible sentencing "
            "objectives; once the court endorses a restorative process, it cannot "
            "also impose a sentence that denounces the conduct."
        ),
        'B': (
            "The sentencing objectives in s. 718 of the Criminal Code are not "
            "mutually exclusive; the court may pursue restorative objectives under "
            "s. 718(e) and (f) while also giving weight to denunciation under "
            "s. 718(a), depending on all the circumstances of the offence and "
            "the offender."
        ),
        'C': (
            "Restorative justice objectives in ss. 718(e) and (f) are subordinate "
            "to denunciation under s. 718(a); the Code requires that denunciation "
            "be prioritized before restorative measures are considered."
        ),
        'D': (
            "Restorative justice is not a recognized sentencing objective under "
            "the Criminal Code; the Code's enumerated objectives are limited to "
            "denunciation, deterrence, separation from society, rehabilitation, "
            "and restitution."
        ),
    },
    'correct_answer': 'B',
    'explanation': (
        "Section 718 of the Criminal Code sets out multiple sentencing objectives: "
        "(a) denunciation; (b) deterrence; (c) separation from society; (d) "
        "rehabilitation; (e) reparations for harm (restorative); and (f) promoting "
        "a sense of responsibility in the offender (restorative). These objectives "
        "are not mutually exclusive. Courts are directed under s. 718.1 to impose "
        "a proportionate sentence that addresses the relevant objectives, weighing "
        "them in accordance with the circumstances. A sentence may incorporate "
        "restorative elements (community conference, restitution) while also giving "
        "expression to denunciation — particularly where the offence caused tangible "
        "harm to an identifiable victim. The defence's argument that denunciation "
        "is incompatible with restorative justice has no basis in the Code."
    ),
    'why_A_wrong': (
        "A states a legal proposition that is incorrect. The "
        "Mutually-Exclusive-Objectives Trap: section 718 lists multiple sentencing "
        "objectives that courts must balance — they are not alternatives from which "
        "a court must choose only one. Restorative justice objectives (ss. 718(e) "
        "and (f)) are explicitly enumerated alongside denunciation (s. 718(a)). "
        "Courts routinely impose sentences that simultaneously pursue restorative "
        "and denunciatory goals, particularly in cases involving identifiable "
        "victims and community harm."
    ),
    'why_B_wrong': (
        "B is correct. Section 718 lists six sentencing objectives that courts "
        "must weigh together — none is automatically excluded by the presence of "
        "another. A sentence that includes restorative elements (meeting with "
        "the victim, restitution) may also carry a denunciatory component. The "
        "Crown's position is consistent with the Code: denunciation under "
        "s. 718(a) and restorative objectives under ss. 718(e)–(f) can coexist "
        "in a proportionate sentence."
    ),
    'why_C_wrong': (
        "C invents a hierarchy that the Code does not create. Section 718 does "
        "not establish a mandatory priority order among sentencing objectives — "
        "s. 718.1 requires only that the sentence be proportionate to the gravity "
        "of the offence and the degree of responsibility of the offender. Courts "
        "have interpreted this to require a balanced weighing of relevant "
        "objectives. No provision of the Code requires denunciation to be "
        "addressed before restorative measures are considered."
    ),
    'why_D_wrong': (
        "D misstates the contents of s. 718. The Code's sentencing objectives "
        "expressly include both reparations to victims or the community (s. 718(e)) "
        "and promoting a sense of responsibility in the offender and acknowledgment "
        "of the harm (s. 718(f)) — these are the statutory foundations of "
        "restorative justice in Canadian sentencing law. Section 718(f) was added "
        "specifically to incorporate restorative principles into the Code."
    ),
    'exam_trigger_words': [
        's.718', 'sentencing objectives', 'denunciation', 'restorative justice',
        's.718(e)', 's.718(f)', 'reparations', 'sense of responsibility',
        'sentencing balance', 'proportionality'
    ],
    'tested_concepts': [
        's.718 sentencing objectives — non-exclusive list',
        'restorative justice objectives ss.718(e) and (f)',
        'denunciation and restoration as compatible',
        'Mutually-Exclusive-Objectives Trap',
        'invented sentencing hierarchy trap',
        'restorative justice in Criminal Code'
    ],
    'updated_at': TODAY,
})

with open('data/questions/criminal-law/ch09-sentencing.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed crim-09-rest-001")

# ── ch10-ycja.json ─────────────────────────────────────────────────────────
# crim-10-records-001  Weakness: distractor C ("automatically destroyed 2 years")
#   too obviously invented; no trap around confusing sentence-type access periods.
#   Fix: replace C with a trap confusing the reprimand (3-month) period with the
#   conditional discharge (3-year) period. Add Sentence-Type-Confusion Trap.

with open('data/questions/criminal-law/ch10-ycja.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['crim-10-records-001']
qs[i].update({
    'options': {
        'A': (
            "The youth record remains accessible indefinitely because it was entered "
            "in the RCMP national repository at the time of conviction."
        ),
        'B': (
            "The youth record is sealed and inaccessible; the access period for a "
            "reprimand ends three months after the reprimand was pronounced, and "
            "Tariq has been offence-free for years beyond that."
        ),
        'C': (
            "The youth record's access period expired three years after the "
            "reprimand was pronounced because youth records for all youth sentences "
            "are accessible for a minimum of three years under the YCJA."
        ),
        'D': (
            "The youth record can only be sealed if Tariq makes a formal court "
            "application after turning 18 to have the record expunged."
        ),
    },
    'why_C_wrong': (
        "C confuses the access period for a reprimand with the access period for "
        "other, more serious youth sentences. The Sentence-Type-Confusion Trap: "
        "the YCJA establishes different access periods depending on the type of "
        "youth sentence imposed. Under s. 119(2)(a), the access period for a "
        "reprimand is only three months from the date it was pronounced — not "
        "three years. A three-year access period applies to conditional discharges "
        "(s. 119(2)(b)). Tariq received a reprimand, not a conditional discharge, "
        "so the three-month period applies and his record has been sealed for years."
    ),
    'updated_at': TODAY,
})

with open('data/questions/criminal-law/ch10-ycja.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed crim-10-records-001")

# ── ch11-appeals.json ──────────────────────────────────────────────────────
# crim-11-prerog-001  Weakness: definitional "is habeas corpus available?"
#   call; no application to test scope of review or exhaustion requirement.
#   Fix: redesign call — prison authorities argue internal grievance process
#   must be exhausted first; tests whether habeas corpus requires prior
#   exhaustion. Add Exhaustion-Required Trap, Deferential-Standard Trap,
#   No-Liberty-Deprivation Trap.

with open('data/questions/criminal-law/ch11-appeals.json') as f:
    qs = json.load(f)
id_map = {q['id']: i for i, q in enumerate(qs)}

i = id_map['crim-11-prerog-001']
qs[i].update({
    'fact_pattern': (
        "The accused is serving a federal penitentiary sentence. Prison authorities "
        "place him in administrative segregation, claiming it is a security measure. "
        "He has not had a hearing and has been in segregation for 45 days. He applies "
        "to the Ontario Superior Court for habeas corpus, arguing the conditions of "
        "his confinement are a distinct deprivation of liberty without legal "
        "justification. The federal Crown argues: (1) the inmate must exhaust the "
        "Correctional Service of Canada's internal grievance process before seeking "
        "habeas corpus; and (2) the Superior Court should defer to the CSC's "
        "administrative decision unless it was patently unreasonable."
    ),
    'call_of_question': (
        "Which of the following most accurately states the law governing the "
        "Crown's two arguments?"
    ),
    'options': {
        'A': (
            "Both arguments are correct — habeas corpus requires exhaustion of "
            "internal administrative remedies, and the Superior Court reviews "
            "administrative segregation decisions on a standard of patent "
            "unreasonableness."
        ),
        'B': (
            "The first argument is correct — habeas corpus requires exhaustion of "
            "internal grievance mechanisms — but the second is wrong; once "
            "exhausted, the Superior Court applies correctness review, not "
            "patent unreasonableness."
        ),
        'C': (
            "Both arguments are wrong — habeas corpus does not require prior "
            "exhaustion of internal grievance processes; and the Superior Court "
            "assesses the legality of the detention independently, not on a "
            "deferential standard of patent unreasonableness."
        ),
        'D': (
            "Both arguments are wrong — but only because administrative segregation "
            "does not constitute a deprivation of liberty; the inmate is already "
            "incarcerated, and a change in conditions of confinement cannot engage "
            "habeas corpus."
        ),
    },
    'correct_answer': 'C',
    'explanation': (
        "Following R v Miller, [1985] 2 SCR 613, the Supreme Court of Canada "
        "confirmed that provincial Superior Courts retain habeas corpus "
        "jurisdiction over federal inmates challenging the legality of a change "
        "in conditions of custody, including administrative segregation. Two "
        "points are clear from the case law: First, habeas corpus does not require "
        "exhaustion of internal prison grievance procedures as a prerequisite — "
        "it is an independent judicial remedy available as of right to any person "
        "whose liberty is unlawfully constrained. Second, the standard of review "
        "on habeas corpus is not patent unreasonableness; the court assesses "
        "independently whether the detention (or change in conditions) is lawful. "
        "Administrative segregation has been held to constitute a distinct and "
        "significant deprivation of residual liberty, engaging habeas corpus."
    ),
    'why_A_wrong': (
        "A accepts both Crown arguments, both of which are legally incorrect. The "
        "Exhaustion-Required Trap: habeas corpus is an independent judicial remedy "
        "that does not require prior exhaustion of administrative channels. Requiring "
        "exhaustion would undermine the fundamental purpose of habeas corpus — "
        "immediate judicial oversight of unlawful deprivation of liberty. The "
        "Deferential-Standard Trap: the Superior Court does not apply patent "
        "unreasonableness to habeas corpus — it independently assesses the "
        "lawfulness of the detention. Both Crown arguments would impermissibly "
        "restrict an established constitutional remedy."
    ),
    'why_B_wrong': (
        "B partially accepts the first Crown argument, which is incorrect. Habeas "
        "corpus does not require exhaustion of internal prison grievance processes. "
        "The Supreme Court in Miller expressly held that the Superior Court retains "
        "habeas corpus jurisdiction without requiring the inmate to first pursue "
        "internal administrative remedies. The Exhaustion-Required Trap is the "
        "error here."
    ),
    'why_C_wrong': (
        "C is correct. Both Crown arguments fail. Habeas corpus does not require "
        "prior exhaustion of internal grievance mechanisms (first argument wrong). "
        "The Superior Court does not apply a deferential standard of patent "
        "unreasonableness on habeas corpus — it independently assesses whether "
        "the deprivation of liberty has legal justification (second argument "
        "wrong). Administrative segregation for 45 days without a hearing is "
        "reviewable as a deprivation of the inmate's residual liberty."
    ),
    'why_D_wrong': (
        "D misstates the law on what constitutes a deprivation of liberty in the "
        "prison context. The No-Liberty-Deprivation Trap: the Supreme Court in "
        "Miller and subsequent cases confirmed that a change in the conditions of "
        "confinement — particularly placement in administrative segregation — "
        "constitutes a distinct deprivation of the prisoner's residual liberty "
        "beyond the sentence of imprisonment itself. The fact that the inmate is "
        "already incarcerated does not eliminate habeas corpus jurisdiction over "
        "unlawful changes to the conditions or terms of that confinement."
    ),
    'exam_trigger_words': [
        'habeas corpus', 'administrative segregation', 'federal inmate',
        'Superior Court jurisdiction', 'exhaustion of remedies',
        'standard of review', 'patent unreasonableness', 'Miller', 's.10(c)'
    ],
    'tested_concepts': [
        'habeas corpus — no prior exhaustion required',
        'standard of review on habeas corpus — independent not deferential',
        'administrative segregation as residual liberty deprivation',
        'Superior Court jurisdiction over federal inmates',
        'Exhaustion-Required Trap',
        'Deferential-Standard Trap',
        'No-Liberty-Deprivation Trap'
    ],
    'updated_at': TODAY,
})

with open('data/questions/criminal-law/ch11-appeals.json', 'w') as f:
    json.dump(qs, f, indent=2, ensure_ascii=False)
print("Fixed crim-11-prerog-001")

print("\nAll criminal law improvements applied.")
