# Report structure

## Contents

- [Default output contract](#default-output-contract)
- [Review setup](#review-setup)
- [Per-reviewer structure](#per-reviewer-structure)
- [Concern traceability and severity display](#concern-traceability-and-severity-display)
- [Cross-review synthesis structure](#cross-review-synthesis-structure)
- [Risk / unsupported claims section](#risk-unsupported-claims-section)
- [Style rules](#style-rules)


## Default output contract

- The default output should contain these sections in order:
  1. `Review setup`
  2. `Reviewer 1`
  3. `Reviewer 2`
  4. `Reviewer 3`
  5. `Cross-review synthesis (post-review; not shown to reviewers)`
  6. `中文核對`
  7. `Risk / unsupported claims`
- Reviewer reports and the synthesis are written in English. The `中文核對` block is written in Traditional Chinese (Taiwan) with full-width punctuation.

## Review setup

- Include:
  - `Input scope`
  - `Study design and applicable reporting guideline`
  - `Assessment boundary`
  - `Shared manuscript claim summary`
  - `Visible evidence base`
  - `Missing materials affecting confidence`, when applicable

## Per-reviewer structure

- Each reviewer report should use the same skeleton:
  - `Overall assessment`
  - `Who would be interested in the results, and why`
  - `Major strengths`
  - `Major Concerns`
  - `Minor Comments`
  - `Methodological or reporting failings that need to be addressed before the case is established`
  - `Assessment against the five review axes`
  - `Recommendation posture`
- `Assessment against the five review axes` should explicitly touch:
  - `originality`
  - `clinical-educational-significance`
  - `methodological-rigour` (name the applicable reporting guideline)
  - `ethics-reporting-transparency`
  - `interdisciplinary-clarity`
- `Recommendation posture` should stay reviewer-like, for example:
  - `supportive if methodological concerns are resolved`
  - `promising but the significance case for practice or education remains underdeveloped`
  - `currently not established from the provided evidence`
- Do not translate `Recommendation posture` into a journal decision category (accept, minor revision, major revision, reject) unless the user explicitly asks for a simulated decision and the output labels it as simulated.

## Concern traceability and severity display

- Give each substantive concern a stable local ID: `R1-M1`, `R1-M2`, `R1-m1`, and so on.
- Use this shape for each Major Concern:

```text
R1-M1 [experimental-design]
**Severity** Major
**Blocking** Yes / No
**Claim pointer** [faithful one-sentence paraphrase of the challenged claim or reporting element]
**Evidence pointer** [section / figure / table, or "location not provided"]
**Concern** [evidence-grounded critique]
**Why it matters** [effect on the central case, important inference, significance, or reproducibility]
**Resolution test** [evidence, analysis, clarification, or claim adjustment that would resolve it]
```

- Use this shorter shape for each Minor Comment:

```text
R1-m1 [writing-clarity]
**Severity** Minor
**Affected element** [claim or reporting element]
**Evidence pointer** [section / figure / table, or "location not provided"]
**Issue** [localized, evidence-grounded problem]
**Required correction** [specific correction that would close it]
```

- A `claim_pointer` is not a quotation unless the exact wording was supplied.
- An `evidence_pointer` may use a page or line number only when the number was supplied or directly verified.
- Minor presentation concerns may point to the affected reporting element instead of a scientific claim.
- The `Methodological or reporting failings that need to be addressed before the case is established` line is a
  short roll-up that cross-references `Blocking Yes` IDs; do not duplicate the full concern prose.
- The `Axis` field of each concern uses one of the five review-axis identifiers. The bracketed tag after the ID (for example `[experimental-design]`) is the internal taxonomy key and may be omitted from the user-facing report.
- Use uppercase `M` IDs for Major Concerns (`R1-M1`) and lowercase `m` IDs for Minor Comments
  (`R1-m1`). Do not change an ID's case after assignment.
- Every reviewer must show both section headings, but either section may say
  `None identified from the supplied material`. Do not force a minimum count.
- Do not emit the complete internal 12-axis coverage matrix.

## Cross-review synthesis structure

- Generate this section only after all individual reports have been frozen. It is part of the editor/author-facing package and is never shown to the simulated reviewers.
- Include:
  - `Consensus strengths`
  - `Consensus blocking concerns`
  - `Other consensus major concerns`
  - `Where emphasis differs across reviewers`
  - `Minor revision checklist`
  - `Clinical / educational significance readout`
  - `Most important issues to resolve before a strong case is established`
- List a concern under either consensus concern section only when at least two reviewer reports raise the same underlying issue.
- Keep meaningful single-reviewer concerns visible under `Where emphasis differs across reviewers`.
- Deduplicate repeated Minor Comments in the checklist and preserve their original IDs as cross-references.
- Do not edit the individual reports after deduplication or synthesis.

## 中文核對 block

- Write this block immediately after the synthesis, in Traditional Chinese (Taiwan). Use full-width punctuation in Chinese sentences; keep Concern IDs, axis identifiers, guideline names, and statistics in ASCII.
- Include, in order:
  - `一段式摘要`: one paragraph (about 150 characters) stating what the three reviewers agree on and where they differ.
  - `必須先處理的阻斷性問題`: each `Blocking Yes` concern as one line, with its Concern ID and a one-sentence restatement.
  - `口試委員最可能追問的三點`: exactly three questions phrased as a thesis committee member or handling editor would ask them, each followed by the Concern ID it derives from and a one-line preparation direction. Choose the three from the frozen reports by impact; when fewer than three grounded concerns exist, write fewer and say so.
  - `建議交接`: whether a single deep critique (`academic-peer-reviewer`), statistical deep-dive (`bob-statistics`), or reasoning practice (`critical-thinking-coach`) would help next; omit the line if none applies.
- The block is a faithful paraphrase of the synthesis. It must not add concerns, change severity, or soften a blocking judgement.
- Do not use Simplified Chinese characters or mainland-China terminology (use 資料, 軟體, 品質, 使用者, 回饋, 修訂, 指導教授, 口試).

## Risk / unsupported claims section

- Include explicit flags for:
  - unsupported novelty claims
  - significance claims not established by the supplied evidence
  - missing controls, validations, or comparisons
  - ethics or reporting items that cannot be verified from the supplied excerpt
  - clarity claims that cannot be assessed from the supplied excerpt
  - any place where the review necessarily relied on partial material

## Style rules

- Keep tone formal, direct, and evidence-based.
- Avoid em dashes, en dashes, and colons as routine prose punctuation. Prefer sentences, commas, semicolons, parentheses, or a short label followed by a new line. Keep necessary hyphens in compound terms and concern IDs. Preserve punctuation in faithful source text, formulas, identifiers, URLs, times, and required machine-readable syntax.
- Make the scientific criticism as direct as the evidence warrants, but never use ridicule,
  hostility, insinuation, or exaggerated language as a substitute for severity.
- Do not write as the authors.
- Do not write a rebuttal, action plan, or editorial decision letter unless the user explicitly asks for one.
- Do not invent line numbers, figure panels, datasets, prior studies, or missing analyses.
- Do not state a journal's word, table, or reference limits from memory; if a limit matters, write `以期刊官網為準` in the 中文核對 block or `check the journal's current author guidelines` in English.
