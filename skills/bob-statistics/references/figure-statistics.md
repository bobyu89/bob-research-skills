# Figure statistics and legend alignment

Use this file when checking figure panels, captions/notes, star labels, error bars, supplementary data tables, or statistical annotations. APA 7 figure anatomy (figure number and title above, note below) is in `apa7-statistics-format.md` section 8.

## Legend information each quantitative panel should provide

For each panel or panel group, check whether the legend states:

- what points, bars, boxes, lines, or shaded regions represent
- the exact definition of `n`
- whether `n` is participants, sessions, items, log events, wards, classes, or repeated measurements
- summary convention: mean ± SD, mean ± SE, median with IQR, min-max, confidence interval, or model estimate
- test/model used
- paired/unpaired or repeated-measures status if relevant
- multiple-comparison correction if multiple contrasts are displayed
- exact p values or star thresholds
- whether a supplementary table provides the raw participant-level values or only summary values

## Plot-type checks

### Bar plots

Risk:
- Bars can hide sample size and distribution.

Fix:
- Prefer showing individual independent data points when feasible.
- If bars remain, require error-bar definition and panel-specific `n`.

### Box plots

Require:
- median line, box bounds, whisker rule, outlier display rule, and `n`.

### Violin plots

Require:
- what points represent, kernel/density caveat if relevant, and independent-unit definition.
- Avoid making dense item-level or event-level violins look like many independent participants.

### Time courses

Require:
- whether the same units are followed over time.
- Use repeated-measures or mixed models when inference uses all time points from the same unit.

### Heat maps / many-feature panels

Require:
- normalization, scaling, clustering distance/linkage if used, multiple-testing or FDR treatment for highlighted features, and whether rows/columns are selected post hoc.

### Regression / correlation panels

Require:
- correlation coefficient or model coefficient, uncertainty if available, sample size, independence of points, and whether the fit is descriptive or inferential.

## Star notation

Avoid legends that only say:

```text
*P < 0.05, **P < 0.01, ***P < 0.001
```

Prefer:

```text
Symbols indicate adjusted p values from AUTHOR_INPUT_NEEDED test with AUTHOR_INPUT_NEEDED correction for the comparisons shown: *p < 0.05, **p < 0.01, ***p < 0.001. Exact p values and sample sizes are provided in Supplementary Table AUTHOR_INPUT_NEEDED. n denotes independent AUTHOR_INPUT_NEEDED.
```

Only use this after the relevant facts are supplied.

## Supplementary-data notes

Ask whether a supplementary table or appendix should include:

- raw participant-level values behind summary panels
- exact p values and test statistics
- sample-size table per panel
- excluded-data notes if any
- the SPSS syntax, R script, or spreadsheet used to produce the panel, where central to the claims

## Figure audit output mini-format

```text
Figure statistics audit
- Panel:
- Current legend problem:
- Risk:
- Required fix:
- Suggested legend text:
```
