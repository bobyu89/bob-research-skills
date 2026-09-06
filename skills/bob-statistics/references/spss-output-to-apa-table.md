# SPSS 輸出轉 APA 表格

使用者貼上 SPSS（或 jamovi、R）的輸出時，用本檔決定哪些數字進表格、欄名怎麼寫、註要放什麼。表格樣式規則見 `apa7-statistics-format.md` 第七節。缺的欄位標 `AUTHOR_INPUT_NEEDED`，不從其他數字反推。

## 目錄

- [一、通用轉換規則](#一通用轉換規則)
- [二、各分析的欄位對應](#二各分析的欄位對應)
- [三、常見錯誤與修正](#三常見錯誤與修正)
- [四、轉表工作流程](#四轉表工作流程)

## 一、通用轉換規則

| SPSS 顯示 | APA 寫法 |
|---|---|
| Sig. (2-tailed) = .000 | *p* < .001 |
| Sig. = .039 | *p* = .039 |
| Sig. = .0391（4 位） | *p* = .039（3 位） |
| Std. Deviation | *SD* |
| Std. Error Mean | *SE* |
| Mean | *M* |
| N（樣本數） | *n*（各組）或 *N*（全體） |
| df = 58 | *t*(58) 或 *df* 欄 |
| Mean Difference | 平均差（*M*diff）或 Δ*M* |
| 95% Confidence Interval Lower / Upper | 95% CI [下限, 上限] |
| Partial Eta Squared | ηp² |
| Pearson Correlation | *r* |
| Spearman's rho | *r*s |
| Standardized Coefficients Beta | β |
| Unstandardized B | *B* |
| Exp(B) | *OR* |
| Cronbach's Alpha | α |
| Wald | Wald χ² |

- SPSS 輸出中的 *p* 值要看清楚是雙尾還是單尾；預設雙尾。
- SPSS 給的效果量常不完整：t 檢定的 *d*（SPSS 27 以後才有）、卡方的 φ 或 Cramér's *V*（在 Symmetric Measures 表）、無母數的 *r* 要自己算（*r* = *z* / √*N*）。缺的效果量標 `AUTHOR_INPUT_NEEDED`，可附計算公式讓使用者算。
- 表格的數字小數位統一為 2 位（*p* 為 3 位），SPSS 的 3 至 4 位要四捨五入。

## 二、各分析的欄位對應

### 描述統計（Descriptives、Frequencies）

APA 表欄位：變項、*n*、*M*、*SD*、範圍（或 Min–Max）、偏態、峰度（要檢驗常態時）。
類別變項：變項、類別、*n*、%。
- 連續與類別變項可合併成「表 1 受試者基本資料」，連續變項報 *M* (*SD*)，類別報 *n* (%)。
- 偏態與峰度絕對值 < 2（或 < 1，依所引慣例）可視為近似常態；引用時標來源。

### 獨立樣本 t 檢定（Independent-Samples T Test）

SPSS 給兩張表：Group Statistics 與 Independent Samples Test。
- 先看 **Levene's Test**：Sig. ≥ .05 用「Equal variances assumed」那一列；Sig. < .05 用「Equal variances not assumed」（Welch），*df* 會是小數。
- 欄位：變項、組 1 *M* (*SD*)、組 2 *M* (*SD*)、*t*、*df*、*p*、*d*、95% CI（平均差）。
- 註要寫：Levene 檢定結果與採用的列；*d* 的計算方式。

### 配對樣本 t 檢定（Paired-Samples T Test）

- 欄位：變項、前測 *M* (*SD*)、後測 *M* (*SD*)、平均差 *M*diff (*SD*diff)、*t*、*df*、*p*、*d*z、95% CI（平均差）。
- Paired Samples Correlations 表的 *r* 可在註中報。
- *d*z = *M*diff / *SD*diff（配對差的標準差）；要註明用的是 *d*z 還是以前測 *SD* 為分母的 *d*。

### 單因子 ANOVA 與事後比較（One-Way ANOVA）

- Test of Homogeneity of Variances（Levene）顯著時，改報 Welch ANOVA 並用 Games–Howell 事後比較；不顯著時用 Tukey HSD 或 Bonferroni。
- ANOVA 表欄位：來源（組間、組內、總和）、*SS*、*df*、*MS*、*F*、*p*、η² 或 ηp²。
- SPSS 的 One-Way ANOVA 不直接給 η²，需 η² = *SS*between / *SS*total；用 GLM Univariate 才有 ηp²。
- 事後比較表欄位：比較組別、平均差、*SE*、*p*（校正後）、95% CI；註寫校正方法。
- 也可在描述表中用上標字母標示同質子集（a、b），註寫「不同上標字母代表事後比較 *p* < .05」。

### 卡方檢定（Crosstabs）

- 欄位：變項、類別、組 1 *n* (%)、組 2 *n* (%)、χ²、*df*、*p*、φ 或 Cramér's *V*。
- 看 Chi-Square Tests 表：2 × 2 用 Pearson Chi-Square（有些期刊要求 Continuity Correction）；期望次數 < 5 的格超過 20% 時（表下方會提示）改報 Fisher's Exact Test。
- 效果量在 Symmetric Measures 表；沒勾選時標 `AUTHOR_INPUT_NEEDED`。
- 註要寫 *N*：χ²(1, *N* = 120)。

### Pearson 與 Spearman 相關（Correlations）

- 相關矩陣表：變項編號為列與欄，只列下三角或上三角，對角線放「—」或 α。
- 每格報 *r*，星號標 *p* 門檻（\* *p* < .05，\*\* *p* < .01，\*\*\* *p* < .001），註寫 *N*。
- 表題或註說明用的是 Pearson 還是 Spearman；混用時在註中標。
- SPSS 的 Sig. 列不進表格，改用星號。
- 多組相關要考慮多重比較；探索性分析要在註中說明未校正。

### 線性迴歸（Linear Regression）

看三張表：Model Summary（*R*、*R*²、Adjusted *R*²）、ANOVA（*F*、*df*、*p*）、Coefficients。
- 表欄位：預測變項、*B*、*SE B*、β、*t*、*p*、95% CI（*B*）；表下報 *R*²、調整後 *R*²、*F*(*df*1, *df*2)、*p*。
- 階層迴歸：每個模型一區塊，加報 Δ*R*² 與 Δ*F* 的 *p*。
- 共線性：Coefficients 表的 VIF（< 10，嚴格 < 5）與 Tolerance 在註中說明；Durbin–Watson 在 Model Summary。
- 類別預測變項要說明虛擬編碼的參照組。

### 邏輯斯迴歸（Binary Logistic）

看 Omnibus Tests（模型 χ²）、Model Summary（Nagelkerke *R*²）、Hosmer–Lemeshow（*p* > .05 表示適配可接受）、Classification Table（正確分類率）、Variables in the Equation。
- 表欄位：預測變項、*B*、*SE*、Wald χ²、*df*、*p*、*OR*（Exp(B)）、95% CI（*OR*）。
- 表下報：模型 χ²(*df*, *N*)、*p*、Nagelkerke *R*²、Hosmer–Lemeshow *p*、正確分類率。
- *OR* 的 CI 不含 1 才顯著；報 *OR* 時要說明類別變項的參照組。

### 信度分析（Reliability Analysis）

- 表欄位：分量表、題數、*M* (*SD*)、Cronbach's α、題項間平均相關（Inter-Item Correlations 需勾選）。
- Item-Total Statistics 表的「Cronbach's Alpha if Item Deleted」只用來說明刪題決策，不整表貼入論文。
- 修正題項總分相關（Corrected Item-Total Correlation）< .30 的題項在註中說明處理。

### GEE 與重複量數（Generalized Estimating Equations、GLM Repeated Measures）

**重複量數 ANOVA**：
- Mauchly's Test of Sphericity 顯著（*p* < .05）時，報 Greenhouse–Geisser（ε < .75）或 Huynh–Feldt（ε ≥ .75）校正的 *F* 與 *df*（小數）。
- 表欄位：效果（時間、組別、時間 × 組別）、*F*、*df*（校正後）、*p*、ηp²。
- 事後比較用 Estimated Marginal Means 的 Pairwise Comparisons（Bonferroni），欄位：時間點比較、平均差、*SE*、*p*、95% CI。

**GEE**：
- 方法段必報：分布與連結函數（例如常態與 identity、二元與 logit）、工作相關矩陣（exchangeable、AR(1)、unstructured）與選擇依據（QIC）、穩健標準誤。
- 表欄位：參數（截距、組別、時間、組別 × 時間）、*B*、*SE*、Wald χ²、*df*、*p*、95% CI；二元結果加 *OR*。
- 描述性：各組各時間點的 *M* (*SD*) 或 *n* (%) 另做一表。
- 遺漏值：GEE 假設 MCAR；要報每個時間點的 *n* 與流失數。

## 三、常見錯誤與修正

| 錯誤 | 為何錯 | 修正 |
|---|---|---|
| 把 Sig. = .000 寫成 *p* = .000 或 *p* = 0 | *p* 不可能為 0；SPSS 只顯示 3 位 | *p* < .001 |
| 只報 *p*，沒報效果量 | 讀者無法判斷大小與實務意義 | 每個檢定補 *d*、η²、φ、*r* 或 *OR* |
| 沒看 Levene 就用 Equal variances assumed | 變異數不等時 *t* 與 *df* 錯 | 報 Levene 結果，必要時改 Welch |
| 多組兩兩比較都用獨立 t 檢定 | 家族型錯誤率膨脹 | 用 ANOVA 加校正的事後比較，或 Bonferroni 校正 α |
| 重複量數用獨立樣本 t 檢定 | 忽略配對結構 | 用配對 t、重複量數 ANOVA 或 GEE |
| 相關矩陣貼 SPSS 整表（含 Sig. 與 N 列） | 不是 APA 樣式 | 只留 *r*，用星號與註 |
| 把 SPSS 的直線表格直接截圖進論文 | APA 無直線、圖片不可編輯 | 重製為文字表格 |
| *p* 值報到 4 位或報 .0000 | APA 規定最多 3 位 | 四捨五入到 3 位，小於 .001 寫 < .001 |
| 卡方在期望次數不足時仍報 Pearson χ² | 近似不成立 | 報 Fisher 精確檢定並註明原因 |
| 迴歸只報 β 不報 *B* 與 CI | 無法還原原始尺度的效果 | 同時報 *B*、*SE B*、β、95% CI |
| 邏輯斯迴歸報 *B* 當效果 | 讀者要的是 *OR* | 報 *OR* 與 95% CI |
| 重複量數不報球形檢定 | *F* 可能高估 | 報 Mauchly 與校正法 |
| 表題寫「t 檢定結果」 | 應描述內容不是方法 | 「兩組 SUS 分數之比較」 |
| 表中同欄小數位不一 | 版面不整 | 統一 2 位 |
| 表格數字與內文不一致 | 一致性錯誤，審稿人最先抓 | 跑 `../bob-shared/core/consistency-sweep.md` |

## 四、轉表工作流程

1. 辨認使用者貼的是哪個程序的輸出（看表名：Group Statistics、Tests of Between-Subjects Effects、Variables in the Equation 等）。
2. 依第二節抓需要的欄位，其他數字不進表。
3. 檢查前提檢定（Levene、Mauchly、Hosmer–Lemeshow、期望次數），決定用哪一列。
4. 補效果量；SPSS 沒給的標 `AUTHOR_INPUT_NEEDED` 並附公式。
5. 套用 APA 格式：符號斜體、小數位、前導零、*p* 寫法、表題在上、註在下、無直線。
6. 寫對應的內文句（`apa7-statistics-format.md` 第四節）。
7. 需要 Word 表格時交 `docx` skill，並提醒「表格用 Word 表格工具重製，不貼 SPSS 截圖」。

輸出範例（配對 t 檢定）：

```text
表 3
系統使用前後臨床推理自評分數之比較（N = 30）

變項          前測 M (SD)    後測 M (SD)    Mdiff (SD)    t(29)    p       dz    95% CI
注意          3.21 (0.64)    3.87 (0.58)    0.66 (0.71)   5.09    < .001   0.93  [0.39, 0.93]
詮釋          3.08 (0.70)    3.72 (0.61)    0.64 (0.80)   4.38    < .001   0.80  [0.34, 0.94]
反應          2.95 (0.75)    3.55 (0.66)    0.60 (0.85)   3.87     .001    0.71  [0.28, 0.92]
反思          3.10 (0.68)    3.60 (0.63)    0.50 (0.77)   3.56     .001    0.65  [0.21, 0.79]

註：dz = Mdiff / SDdiff。95% CI 為平均差之信賴區間。四個構面對應 Tanner 臨床判斷模型。p 值未經多重比較校正。
```
