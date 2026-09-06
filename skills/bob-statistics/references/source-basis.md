# Source basis for `bob-statistics`

This file keeps the skill conservative. It is a local summary of the sources the agent should use to justify reporting checks; it is not a replacement for the target journal's current author instructions or the thesis office's current format rules.

## Primary source hierarchy

1. **User-supplied manuscript, protocol, data, reviewer or committee comments, and journal instructions**
   - Use these first when the user provides them.
   - If a reviewer comment, thesis committee comment, or statistical analysis plan gives a stricter requirement, follow that local constraint.

2. **APA Publication Manual, 7th edition (2020)**
   - Chapter 6 governs numbers and statistics: which symbols are italic, decimal places, the leading-zero rule, exact p values, confidence-interval brackets.
   - Chapter 7 governs tables and figures: number and title above, notes below, horizontal rules only, no vertical rules.
   - The local digest is `apa7-statistics-format.md`. When the manual and this digest disagree, the manual wins.

3. **Study-type reporting guidelines from the EQUATOR Network**
   - Use the guideline that matches the design; route through `equator-guideline-finder` when the design is not obvious.
   - CONSORT 2025 for randomised trials (statistical methods, sample size, outcomes, participant flow).
   - STROBE for observational studies (cohort, case-control, cross-sectional).
   - TREND for non-randomised interventions; SQUIRE for quality-improvement projects.
   - COREQ and SRQR for qualitative components; CHERRIES for web surveys; TRIPOD+AI for prediction models; PRISMA-ScR for scoping reviews.
   - Design-based research has no EQUATOR guideline; use the iteration-reporting elements in `../bob-shared/core/health-research-compliance.md` and state the limitation.
   - Source: https://www.equator-network.org/

4. **SAMPL guidelines (Lang & Altman, 2015)**
   - "Statistical Analyses and Methods in the Published Literature" gives item-level guidance for reporting each common analysis: describe the method enough to be reproduced, report effect sizes with confidence intervals, give exact p values, define n, state assumption checks, software, and missing-data handling.
   - Treat SAMPL as the checklist behind `statistical-reporting.md`.

5. **Instrument-reporting conventions used in nursing research**
   - Content validity index conventions (Polit & Beck; Lynn) for I-CVI and S-CVI/Ave.
   - Cohen's effect-size benchmarks and G*Power documentation for sample-size text.
   - Sauro & Lewis and Bangor et al. for System Usability Scale scoring and norms.
   - The local digest is `nursing-instruments-reporting.md` and `sample-size-and-power.md`; cite the original sources in the thesis, not this skill.

6. **Conservative statistical reporting practice**
   - If no specific rule applies, require enough information for a reader to identify the design, analysis unit, test or model, assumptions, correction strategy, sample size, effect size, uncertainty, and software.

## Implementation boundaries

The skill should not pretend that any journal has one universal statistical recipe. It enforces transparent reporting and identifies risks that reviewers and thesis committees commonly challenge.

Use careful language:

- Prefer: `The manuscript should define the independent unit of analysis.`
- Avoid: `The journal requires this exact test.` unless the journal instruction actually says so.
- Do not quote journal word or table limits from memory; write "以期刊官網為準，查核日期 YYYY-MM-DD" or mark the number as an example.

When the user supplies a target journal, a reporting-guideline checklist, or the thesis format rules, ask for or use that document before relying on generic guidance.

## Key reporting principles used by this skill

- Replication depends on the independent unit of analysis, not merely the number of measurements, items, or log events.
- Statistical tests are interpretable only relative to the design, assumptions, and data structure.
- P values should not carry the full evidential burden; effect estimates, confidence intervals, design quality, and reproducibility matter.
- Multiple testing changes interpretation and usually needs a declared correction or a clearly justified family of planned comparisons.
- Instrument reliability is a property of this sample; report it for the current study, not only from the original authors.
- Usability and satisfaction scores describe perception; they are not evidence of learning outcome or clinical competence.
- Figures and tables should expose the data structure: n, error-bar meaning, test or model, correction, and whether points represent participants or subsamples.
- Missing statistical details should be surfaced as author questions (`AUTHOR_INPUT_NEEDED`), not silently repaired.
