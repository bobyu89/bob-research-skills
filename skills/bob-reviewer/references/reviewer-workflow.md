# Reviewer workflow

## Contents

- [Default execution order](#default-execution-order)
- [Input handling](#input-handling)
- [Immutable review-packet checklist](#immutable-review-packet-checklist)
- [Concern-ledger fields](#concern-ledger-fields)
- [Cross-review generation rule](#cross-review-generation-rule)
- [Failure-safe behaviour](#failure-safe-behaviour)


## Default execution order

1. Identify the input package.
   - Determine whether the user supplied a full manuscript, abstract-only draft, selected sections, figures, notes, thesis chapters, or a pre-submission concept summary.
   - Identify the study design and the applicable reporting guideline. If the guideline is uncertain, call `equator-guideline-finder` first.
2. Build an immutable review packet.
   - Include the supplied manuscript/source, verified source anchors, assessment boundary, the applicable guideline name, and the common review principles from `source-basis.md`.
   - Do not include suspected concerns, a shared interpretation, another report, or a draft synthesis.
3. Define all reviewer emphasis briefs before review begins.
   - Keep the source packet and report skeleton identical; vary only the declared emphasis.
4. Generate each reviewer report in an isolated context.
   - Give the reviewer only the immutable packet, common rules, report skeleton, and its own emphasis brief.
   - Within that context, independently extract the central claim, key evidence, stated significance, implied audience, visible limitations, and missing material.
   - Independently apply `originality`, `clinical-educational-significance`, `methodological-rigour` (against the applicable EQUATOR guideline), `ethics-reporting-transparency`, and `interdisciplinary-clarity`.
5. Build one private concern ledger per reviewer.
   - Load `technical-concern-taxonomy.md` and mark each axis `applicable`, `not applicable`, or `not assessable` without access to any other reviewer's ledger.
   - If the study design is clear, load only the matching section of `health-research-review-gates.md` inside the same isolated context.
   - Give every supported concern a reviewer-local issue key, `major` or `minor` severity, a blocking flag for Major Concerns, severity rationale, `claim_pointer`, `evidence_pointer`, and resolution test.
   - Keep the ledger private to that reviewer; expose only the fields needed to make emitted concerns traceable.
6. Freeze all reviewer reports.
   - Do not let reviewers read, cite, agree with, answer, or anticipate one another.
   - Do not redistribute, add, remove, or rephrase concerns after comparison merely to change overlap.
   - Render separate `Major Concerns` and `Minor Comments` sections. If a tier has no grounded item, write `None identified from the supplied material` rather than filling a quota.
7. Generate a post-review synthesis in a separate context.
   - Summarize consensus blocking concerns, other major concerns, the minor-revision checklist,
     points of emphasis divergence, and the most decision-relevant methodological and significance risks.
   - Reconcile reviewer-local issue keys only now. Treat an issue as consensus only when at least two frozen reports independently raise the same underlying concern.
   - After the English synthesis, write the `中文核對` block in Traditional Chinese (Taiwan): a one-paragraph summary, the blocking items with their Concern IDs, the three questions a thesis committee or editor is most likely to ask, and any recommended hand-off to `academic-peer-reviewer` or `critical-thinking-coach`. The block paraphrases the synthesis; it must not introduce concerns absent from the frozen reports.
8. Run final QA.
   - Check context isolation, locked-report status, evidence anchors, post hoc overlap mapping, groundedness, consistency, coverage, and non-invention.

## Input handling

- Acceptable inputs include:
  - manuscript draft
  - abstract or summary paragraph
  - introduction, results, discussion, or methods excerpts
  - figure legends or selected figures
  - author notes describing the claimed contribution
- If the input is thin, the skill should still provide a bounded review, but it must clearly state the assessment boundary.

## Immutable review-packet checklist

- Put only these common inputs into every isolated reviewer context:
  - supplied manuscript/source material
  - verified section, figure, table, equation, page, or block anchors
  - assessment boundary and missing-file inventory
  - common review principles, the applicable reporting guideline name, and the report skeleton
  - that reviewer's preassigned emphasis brief
- Do not put these into the shared packet:
  - extracted concerns or visible technical gaps
  - a shared claim-evidence interpretation
  - another reviewer report or ledger
  - overlap targets, consensus labels, or synthesis notes

## Concern-ledger fields

Use this internal shape before drafting reviewer prose:

```yaml
issue_key: experimental-design-control-selection
axis: experimental-design
review_axis: methodological-rigour
applicability: applicable
severity: major
blocking: yes
severity_rationale: Without a comparison group the pre-post gain in clinical reasoning scores cannot be separated from practice and Hawthorne effects.
claim_pointer: The improvement in clinical reasoning is attributed to the RAG-based learning system.
evidence_pointer: Results, "Learning outcomes"; Table 3
evidence_status: located
concern: The single-group pre-post design does not isolate the system's effect.
resolution_test: Add a comparison condition or restate the finding as preliminary within-group change.
reviewer_id: Reviewer 1
```

- `axis` is the internal 12-axis taxonomy key; `review_axis` is one of the five user-visible review axes. Emit only `review_axis` in the report under `Axis`.

- Use section headings and supplied figure/table identifiers before page or line numbers.
- Use `location not provided` or `not assessable from supplied material` when an exact pointer cannot be verified.
- Never infer an absent figure, analysis, control, or manuscript location.
- Use `blocking: yes` only for a grounded Major Concern that prevents the current manuscript from
  establishing its central case. Minor Comments always use `blocking: no` internally and do not
  need to display the field in the final report.

## Cross-review generation rule

- Run synthesis only after all individual reports are final and locked.
- Treat the synthesis as editor/author-facing; never send it back into any reviewer context.
- The cross-review synthesis should consolidate, not average away, reviewer differences.
- A consensus item must map post hoc to equivalent concerns raised by at least two reviewer reports.
- Preserve consequential single-reviewer concerns under weighting differences; do not drop them merely because they lack consensus.
- It must separate:
  - shared strengths
  - consensus blocking concerns
  - other shared major concerns
  - minor revision checklist
  - differences in significance weighting
  - differences in clarity or transparency judgment
- The `中文核對` block follows the synthesis and is derived from it only.

## Failure-safe behaviour

- If isolated contexts are unavailable, produce one reviewer report per invocation or disclose that mutual blindness cannot be guaranteed. Do not silently simulate independence inside a shared drafting context.
- When evidence is absent, say the case is not yet established from the supplied material.
- When significance is unclear, distinguish `potentially interesting` from `demonstrated broad importance`.
- When clarity is weak, describe the barrier to an adjacent-field reader instead of rewriting the manuscript unless asked.
- When the manuscript is in Traditional Chinese, keep the reviewer reports in English but cite locations using the manuscript's own headings and table numbering (for example `第四章，表 4-2`).
