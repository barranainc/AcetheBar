# Generated Barrister Exams — Human Review Flags Register

**Last updated:** 2026-05-25  
**Scope:** Generated Barrister C · D · E · F (640 questions total)  
**Purpose:** Consolidated register of all questions that were flagged HUMAN REVIEW REQUIRED during AI-assisted QA, with resolution status.

---

## Status Summary

| Exam | Flag | Status |
|------|------|--------|
| C | fam-04-mh-consent-003 | **UNRESOLVED** — human reviewer required |
| D | crim-02-sw-issu-004 | **RESOLVED (Phase 2J)** — correct answer rewritten |
| E | civ-02-demand-001 | **RESOLVED (Phase 2J)** — citation corrected |
| F | fam-08-review-001 | **UNRESOLVED** — human reviewer required |
| F | fam-08-review-var-001 | **UNRESOLVED** — human reviewer required |

**Resolved:** 2 of 5 flags  
**Unresolved:** 3 of 5 flags (C×1, F×2)

---

## Resolved Flags

### D — crim-02-sw-issu-004

**File:** `data/questions/criminal-law/ch02-charter-arrest.json`  
**Exam:** Generated Barrister D (`bard`)  
**Flagged by:** Phase 2D-QA  
**Resolved:** Phase 2J (2026-05-25)

**Original issue:** The question's `correct_answer` was `"B"`, asserting that s.487 *Criminal Code* warrants for dwelling-houses automatically expire after 30 days. The question's own explanation admitted "The Criminal Code at s. 487 does not itself set a universal 30-day expiry for all warrants," making the correct answer internally inconsistent with the explanation. No universal 30-day expiry exists in CC s.487. The CDSA s.11(5) provides a 15-day limit for drug-search warrants under that statute. DNA warrant regimes under ss.487.04–487.09 have their own validity periods. For standard s.487 warrants, the applicable test is the common-law requirement to execute within a reasonable time.

**Resolution:** Full rewrite:
- `correct_answer`: `"B"` → `"D"`
- `options.D`: rewritten to accurately state the common-law reasonable-time standard
- `explanation`: fully rewritten — no 30-day limit in CC s.487; distinguishes CDSA s.11(5) (15-day drug-warrant limit); explains common-law reasonableness test
- `why_B_wrong`: rewritten — no 30-day universal expiry in CC s.487
- `why_D_wrong`: rewritten — confirms D is the correct answer

---

### E — civ-02-demand-001

**File:** `data/questions/civil-litigation/ch02-limitation-periods.json`  
**Exam:** Generated Barrister E (`bare`)  
**Flagged by:** Phase 2G-QA  
**Resolved:** Phase 2J (2026-05-25)

**Original issue:** Explanation cited `"s. 5(3) of the Limitations Act, 2002"` as the source of the demand-obligation discovery rule. The *Limitations Act, 2002* s.5 has only two subsections — s.5(1) (discovery rule) and s.5(2) (presumption of knowledge). There is no s.5(3). The demand-obligation rule derives from judicial interpretation of s.5(1)(a)(i): the limitation period runs from the day the person knew the injury/loss occurred, which for a demand debt is the date demand is made and refused.

**Resolution:** Corrected `"s. 5(3)"` → `"s. 5(1)"` in explanation (two occurrences). Substantive legal proposition unchanged.

---

## Unresolved Flags

### C — fam-04-mh-consent-003

**File:** `data/questions/family-law/ch04-matrimonial-home.json`  
**Exam:** Generated Barrister C (`barc`)  
**Flagged by:** Phase 2C-QA  
**Status:** UNRESOLVED — requires human source-check

**Issue:** The question's explanation cites `FLA s.21(3)` as the authority for bona fide purchaser (BFP) protection in matrimonial home dispositions. The FLA s.21 provision structure is:
- s.21(1): Prohibition on disposition without spousal consent  
- s.21(2): Exception for a transaction between spouses  
- s.21(3): Claimed to be BFP protection  

Some sources suggest the BFP protection may be in s.21(2) rather than s.21(3), or that the subsection numbering differs between editions. The substantive legal content (BFP who pays fair value and has no notice of spousal non-consent takes clear title) is plausible and consistent with general property law principles.

**Action required:** A qualified reviewer should check the current *Family Law Act*, R.S.O. 1990, c. F.3 text to confirm which subsection addresses BFP protection in matrimonial home transactions. If s.21(3) is incorrect, update `explanation`, `source_reference.rule_or_statute_reference`, and any `why_X_wrong` fields that cite this subsection.

---

### F — fam-08-review-001

**File:** `data/questions/family-law/ch08-child-protection.json`  
**Exam:** Generated Barrister F (`barf`)  
**Flagged by:** Phase 2I-QA  
**Status:** UNRESOLVED — requires human source-check

**Issue:** The question cites `CYFSA s.116(6)` as the authority governing status review applications. The substantive content (any party may apply for status review; court may vary, terminate, or extend a supervision or society wardship order; best interests standard applies) is plausible and consistent with the general CYFSA status review framework. However, the specific subsection `s.116(6)` could not be independently verified against official CYFSA text.

**Action required:** A qualified reviewer should check the current *Child, Youth and Family Services Act, 2017*, S.O. 2017, c. 14, Sched. 1 to confirm that s.116(6) governs the matters described in the question. If the subsection number is incorrect, update `explanation`, `source_reference.rule_or_statute_reference`, and any option text citing this provision.

---

### F — fam-08-review-var-001

**File:** `data/questions/family-law/ch08-child-protection.json`  
**Exam:** Generated Barrister F (`barf`)  
**Flagged by:** Phase 2I-QA  
**Status:** UNRESOLVED — requires human source-check

**Issue:** Same `CYFSA s.116(6)` citation issue as `fam-08-review-001` above. This is a separate question that also relies on s.116(6) for the status review variation framework. Both questions should be reviewed together.

**Action required:** Same as `fam-08-review-001`. If the subsection is wrong, update both questions.

---

## Resolution Checklist

- [x] D — crim-02-sw-issu-004 — correct answer and explanation fully rewritten (Phase 2J)
- [x] E — civ-02-demand-001 — citation corrected s.5(3)→s.5(1) (Phase 2J)
- [ ] C — fam-04-mh-consent-003 — FLA s.21 subsection to confirm against official statute text
- [ ] F — fam-08-review-001 — CYFSA s.116(6) to confirm against official statute text
- [ ] F — fam-08-review-var-001 — CYFSA s.116(6) to confirm against official statute text
