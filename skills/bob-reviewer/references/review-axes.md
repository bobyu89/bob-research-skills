# Review axes

## Five core axes for health-science manuscripts

The axis values are ASCII identifiers used in concern records and the `Assessment against the five review axes` line. The descriptions are the working definitions.

- `originality`
  - Ask what the manuscript claims to add beyond the existing literature, and whether that distinction is explicit and credible in the supplied text.
  - Flag when novelty is asserted only in the abstract or conclusion but is not built in the introduction or literature review.
  - In nursing and health-professions education, originality often lies in population, setting, delivery mode, or integration of methods rather than in a new mechanism. Judge the claim the authors actually make, not a laboratory-science notion of novelty.
- `clinical-educational-significance`
  - Ask whether the findings could change clinical practice, patient outcomes, nursing education, curriculum design, or health-service delivery, and for whom.
  - Distinguish statistical significance from clinical or educational significance; ask for effect sizes, minimal important differences, or learning-outcome relevance when the manuscript reports only p values.
  - Distinguish local usefulness (one unit, one school, one cohort) from transferable significance.
- `methodological-rigour`
  - Ask whether the study design can answer the stated question, and whether the manuscript reports what the applicable EQUATOR guideline expects for that design.
  - Route by design: CONSORT (RCT), TREND or CONSORT extensions (non-randomised intervention), STROBE (observational), COREQ or SRQR (qualitative), PRISMA or PRISMA-ScR (reviews), CHERRIES (web surveys), TRIPOD+AI (prediction or AI models), COSMIN-informed reporting (instrument development). If the applicable guideline is uncertain, call `equator-guideline-finder` before assessing this axis.
  - Identify concrete methodological or reporting failings that must be addressed before the authors' case is established.
- `ethics-reporting-transparency`
  - Ask whether IRB approval, informed consent, data protection, trial or protocol registration, conflicts of interest, funding, authorship criteria, and generative-AI use are reported where applicable.
  - Ask whether data, code, instruments, prompts, or analysis scripts are available or their absence is justified.
  - Treat missing ethics reporting as a concern only when the study type requires it and the omission is visible in the supplied material.
- `interdisciplinary-clarity`
  - Ask whether a reader from an adjacent field (a clinician reading an education paper, an educator reading a digital-health paper, a statistician reading a qualitative paper) can follow the question, design, findings, and implications.
  - Flag unexplained abbreviations, undefined instruments, framework names used without a one-line definition, and results that cannot be interpreted without the discussion.

## Axis-specific prompts

- For `originality`:
  - What is the claimed advance, in one sentence?
  - Where in the supplied text is the gap established, and does the study design actually address that gap?
- For `clinical-educational-significance`:
  - Who would act differently after reading this, and on what evidence?
  - Are effect sizes, confidence intervals, or qualitative depth sufficient to support the implications section?
- For `methodological-rigour`:
  - Which guideline applies, and which of its items are visibly missing?
  - Which parts of the inferential chain (sampling, measurement, analysis, interpretation) are under-supported?
- For `ethics-reporting-transparency`:
  - Is the ethics statement present, specific (board name, approval number), and consistent with the described procedures?
  - Is any generative-AI use in the study or in manuscript preparation disclosed?
- For `interdisciplinary-clarity`:
  - Can the abstract stand alone?
  - Does the manuscript rely on jargon, compressed context, or field-specific assumptions without explanation?

## Weighting guidance for the three reports

- Assign these emphasis briefs before any reviewer receives the manuscript, and do not change them in response to another report.
- `Reviewer 1` should usually foreground `methodological-rigour` and the applicable reporting guideline.
- `Reviewer 2` should usually foreground `originality` plus `clinical-educational-significance`.
- `Reviewer 3` should usually foreground `interdisciplinary-clarity` plus `ethics-reporting-transparency`.
- All three reviewers should still cover all axes briefly; the difference is weight, not scope omission.
- The user may override the default emphasis briefs (for example, two methodological reviewers for a thesis defence rehearsal). Record the override in `Review setup`.

## Missing-evidence handling

- If the manuscript text or tables are incomplete, do not infer absent validations, ethics approvals, or prior-work distinctions.
- Use explicit markers such as:
  - `Not assessable from provided material`
  - `AUTHOR_INPUT_NEEDED`
  - `Evidence not shown in the supplied manuscript excerpt`

## Things this axis set must not do

- Do not replace these axes with a generic checklist copied from one journal's reviewer form; the axes summarise shared public principles, not any single journal's policy.
- Do not force exhaustive design-specific critique when the provided material does not support it.
- Do not convert clarity comments into copyediting line edits unless the user explicitly asks for that level of intervention.
- Do not treat a Chinese-language manuscript as less rigorous; apply the same axes and cite the manuscript's own section and table numbering (for example `第三章，表 3-1`).
