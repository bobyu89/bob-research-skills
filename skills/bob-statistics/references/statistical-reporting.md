# Statistical reporting checklist

Use this file when drafting or auditing a Statistical analysis (資料處理與分析) subsection, Methods, Results, or supplementary methods text. Number and symbol formatting follows `apa7-statistics-format.md`.

## Minimum information to extract

For each major analysis, identify:

- endpoint or response variable
- experimental groups / conditions
- independent experimental unit
- biological replicates and technical replicates
- repeated measures, paired observations, blocks, sites, wards, classes, patients, participants, or DBR iteration rounds
- inclusion / exclusion criteria
- missing-data handling
- randomization and blinding, if applicable
- transformation or normalization
- test or model name
- assumptions checked or rationale for robust / nonparametric approach
- multiple-comparison correction or planned-comparison rationale
- reported estimate, effect size, uncertainty interval, exact p value, and sample size
- software, package, and version when available

## Statistical analysis paragraph structure

A clean manuscript paragraph usually follows this order:

1. **Software and environment**
   - Name software and packages when supplied.
   - Do not invent versions.

2. **Data summary convention**
   - State whether values are mean ± SD, mean ± SE, median with interquartile range, box-plot convention, or another summary.

3. **Sample-size and replication definition**
   - Define `n` for each experiment class.
   - Distinguish independent samples from technical readings or submeasurements.

4. **Test/model choice**
   - State which comparisons used which tests or models.
   - Explain paired vs unpaired, parametric vs nonparametric, repeated-measures or mixed-effects models where relevant.

5. **Multiplicity strategy**
   - State the family of comparisons and correction method, or explain that tests were prespecified and limited.

6. **Thresholds and exact reporting**
   - Use exact p values where possible.
   - If thresholds are used, define them and avoid star-only reporting.

7. **Exclusions and robustness**
   - State pre-established exclusion rules or mark them as missing.
   - Do not add post-hoc exclusions unless the user supplied them.

## Results wording rules

Prefer:

- `Treatment A was associated with a higher response than control (mean difference ..., 95% CI ..., p = ...).`
- `The analysis used participants as the independent unit; item-level and session-level values are shown only to display within-participant variability.`
- `The evidence is consistent with an increase, although the small sample size limits precision.`

Avoid:

- `proved`, `demonstrated conclusively`, `confirmed the mechanism`, based only on a p value.
- `highly significant` without effect size or uncertainty.
- `n = 300 responses` or `n = 1,200 log events` when the study actually has 30 participants.
- `ns` as the only result.
- `data were normally distributed` without a clear basis, especially for very small samples.

## Missing-information labels

Use short factual labels:

- `AUTHOR_INPUT_NEEDED: define the independent unit for Table 4-3 (participants or sessions?).`
- `AUTHOR_INPUT_NEEDED: state whether comparisons were corrected for multiple testing.`
- `AUTHOR_INPUT_NEEDED: provide exact p values or the thresholding rule used by the journal.`
- `AUTHOR_INPUT_NEEDED: state software/package and version.`

## Ready-to-paste skeleton (English)

```text
Statistical analyses were performed using AUTHOR_INPUT_NEEDED. Data are presented as AUTHOR_INPUT_NEEDED unless otherwise stated. The independent experimental unit was AUTHOR_INPUT_NEEDED; technical replicates were averaged before inferential analysis where applicable. Comparisons between two groups were analysed using AUTHOR_INPUT_NEEDED. Comparisons among more than two groups were analysed using AUTHOR_INPUT_NEEDED, followed by AUTHOR_INPUT_NEEDED correction for multiple comparisons. Effect sizes with 95% confidence intervals, exact p values, test statistics and sample sizes are reported in the tables or figure notes following APA 7 conventions. No data were excluded unless specified in the relevant Methods section.
```

Use the skeleton only after filling supplied facts. Keep placeholders if facts are missing.

## Ready-to-paste skeleton (繁體中文碩論)

```text
本研究以 AUTHOR_INPUT_NEEDED（軟體與版本）進行資料分析。連續變項以平均數與標準差（M ± SD）呈現，類別變項以次數與百分比呈現。分析單位為 AUTHOR_INPUT_NEEDED（受試者／場次），同一受試者的多次測量以 AUTHOR_INPUT_NEEDED 處理。兩組比較採 AUTHOR_INPUT_NEEDED，三組以上採 AUTHOR_INPUT_NEEDED 並以 AUTHOR_INPUT_NEEDED 進行事後比較與多重比較校正。各檢定均報告效果量與 95% 信賴區間，顯著水準設為雙尾 α = .05，p 值報告至小數第三位。遺漏值處理方式為 AUTHOR_INPUT_NEEDED。除方法段另有說明外，未排除任何資料。
```
