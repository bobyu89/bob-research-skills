# Source basis

## What grounds this skill

This skill does not carry a single journal's editorial text. It grounds reviewer behaviour in publicly stated principles that health-science, nursing, medical-education, and digital-health journals commonly adopt. When a user asks for a specific journal's policy, state that the skill summarises shared principles and that the journal's own author and reviewer guidelines take precedence (以期刊官網為準).

The public sources summarised below are named so the user can verify them. Do not attribute specific numeric limits, turnaround times, or form wording to any journal from memory.

## Public principles converted into working rules

### ICMJE recommendations (conduct, reporting, editing, and publication of scholarly work in medical journals)

- Authorship rests on substantial contribution, drafting or critical revision, final approval, and accountability. Reviewers may flag when authorship or contribution statements are absent where the target journal expects them.
- Conflicts of interest and funding must be disclosed.
- Clinical trials should be registered before enrolment; reviewers may ask for the registration identifier when a manuscript describes a trial.
- Manuscripts should include an ethics statement covering approval and informed consent for human-subject research.
- Reviewers treat manuscripts as confidential and evaluate the work, not the authors.

### COPE (Committee on Publication Ethics) guidance for peer reviewers

- Review only within one's competence; state when a part of the manuscript cannot be assessed.
- Be objective and constructive; avoid hostile or personal comments.
- Declare conflicts; do not use the manuscript's content for personal advantage.
- Do not attempt to identify or contact authors; do not share the manuscript.
- Raise concerns about possible misconduct (plagiarism, image manipulation, data fabrication) to the editor rather than accusing authors in the report.

### EQUATOR Network reporting guidelines

- Reviewers should assess whether a manuscript reports what the guideline for its design requires. The relevant guideline depends on design, not on the journal.
- Common routes used in this skill: CONSORT (randomised trials), TREND and CONSORT extensions (non-randomised and pilot studies), STROBE (cohort, case-control, cross-sectional), COREQ and SRQR (qualitative), PRISMA 2020 and PRISMA-ScR (systematic and scoping reviews), CHERRIES (internet surveys), TRIPOD+AI (prediction models including machine learning), CHART (chatbot health advice research), SQUIRE (quality improvement), GRRAS (reliability and agreement studies).
- Missing checklist items are reporting concerns. They become Major Concerns only when the omission prevents the reader from evaluating validity or reproducing the study.
- When the applicable guideline is uncertain, defer to `equator-guideline-finder`.

### Typical nursing and health-professions-education reviewer forms (public reviewer guidance)

Most such journals publish reviewer guidance that asks reviewers to comment, in some form, on:

- relevance and importance of the question to nursing, education, or health services;
- originality relative to existing evidence;
- appropriateness and rigour of design, sampling, measurement, and analysis;
- ethical approval and consent;
- clarity of presentation, including whether the abstract reflects the paper;
- whether conclusions are supported by the results;
- whether the implications for practice, education, or policy are justified.

These items are the empirical basis for the five axes in `review-axes.md`. They are summarised generically; no journal's form is reproduced.

## Local rule summary

- Reviewer outputs evaluate the manuscript against the five axes only:
  - `originality`
  - `clinical-educational-significance`
  - `methodological-rigour`
  - `ethics-reporting-transparency`
  - `interdisciplinary-clarity`
- Reviewer outputs must not pretend to make the editor's decision.
- Reviewer outputs may comment on whether significance seems overstated or understated.
- Reviewer outputs must distinguish:
  - what is supported by manuscript evidence
  - what is missing or methodologically weak
  - what cannot be assessed from provided material
- When the manuscript packet is incomplete, the skill must use `AUTHOR_INPUT_NEEDED` or equivalent missing-evidence flags instead of inventing facts.

## Conservative implementation choices

- The skill returns exactly `3 mutually blind reviewer reports + 1 post-review synthesis` by default.
  - This is a repo-level implementation choice, not a claim about any journal's workflow; many journals use two reviewers.
- The three reviewers receive the same immutable source packet but work in mutually blind contexts with preassigned emphasis briefs; they do not receive shared concerns or other reports.
  - Mutual blindness is a simulation-integrity rule.
- Reviewer differences must not rely on invented identity, seniority, institution, demographic profile, or narrow specialty role.
- The output includes an explicit `Risk / unsupported claims` section and a `中文核對` block.
  - Both are local usability devices, not journal format requirements.
- The skill uses a 12-axis technical concern taxonomy as an internal coverage checklist.
  - This is a repo-level organisational device, not an official taxonomy.
- Each substantive concern carries a claim pointer and evidence pointer.
  - This is a local traceability rule; it must never cause the skill to invent locations or manuscript facts.
- Pairwise reviewer concern overlap is measured only after reports are frozen.
- The skill uses explicit section labels such as `Review setup`, `Reviewer 1`, `Cross-review synthesis (post-review; not shown to reviewers)`, and `中文核對`.

## Implementation implications

- If the user asks for an author rebuttal, route to `bob-response`, not this skill.
- If the user asks for one deep single-reviewer critique with logical-fallacy hunting, route to `academic-peer-reviewer`.
- If the user asks for simulated peer review, stay in reviewer mode:
  - assess claims
  - identify likely interested readership
  - identify methodological and reporting failings
  - avoid drafting editorial decision language as the default output
- If the manuscript seems methodologically sound but of limited significance, the reports may say so; the two judgements are separate.
- If the manuscript is significant but evidence is incomplete, the reports must still foreground methodological failings because they must be resolved before the authors' case is established.
- For a thesis-defence rehearsal, keep the same structure; the `中文核對` block carries the three questions the committee is most likely to ask.
