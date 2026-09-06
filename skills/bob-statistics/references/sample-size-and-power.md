# 樣本數與檢定力

適用於計畫書與論文方法段的「樣本數估計」小節、口試或審稿人問「為什麼是這個人數」時的回應。分量性（G*Power）、質性（資訊力與飽和）、DBR 與可用性研究三類。缺的參數標 `AUTHOR_INPUT_NEEDED`，不代填效果量。

## 目錄

- [一、樣本數論述的必報要素](#一樣本數論述的必報要素)
- [二、效果量慣例（Cohen）](#二效果量慣例cohen)
- [三、G*Power 各檢定的輸入參數](#三gpower-各檢定的輸入參數)
- [四、報告句型](#四報告句型)
- [五、失訪率加成](#五失訪率加成)
- [六、質性研究的樣本數論述](#六質性研究的樣本數論述)
- [七、DBR 與可用性研究的樣本數依據](#七dbr-與可用性研究的樣本數依據)
- [八、事後檢定力的問題](#八事後檢定力的問題)
- [九、審查清單](#九審查清單)

## 一、樣本數論述的必報要素

1. 對應的**主要假設或主要結果變項**（一個研究只以主要結果算一次）。
2. 統計檢定（與資料分析段一致）。
3. 效果量與**依據**：前導研究、文獻中類似介入的效果、或 Cohen 慣例（要說是哪一種）。
4. α（通常 .05，雙尾）與檢定力（通常 .80）。
5. 軟體與版本（例如 G*Power 3.1.9.7）。
6. 算出的最小樣本數。
7. 失訪率加成與最終目標人數。
8. 實際招募到的人數與差異說明（結果段或限制段）。

## 二、效果量慣例（Cohen）

| 檢定 | 效果量 | 小 | 中 | 大 |
|---|---|---|---|---|
| t 檢定 | *d* | 0.20 | 0.50 | 0.80 |
| ANOVA | *f* | 0.10 | 0.25 | 0.40 |
| ANOVA（另一種寫法） | η² | .01 | .06 | .14 |
| 相關 | *r* | .10 | .30 | .50 |
| 卡方 | *w* | 0.10 | 0.30 | 0.50 |
| 多元迴歸 | *f*² | .02 | .15 | .35 |
| 邏輯斯迴歸 | *OR*（近似） | 1.5 | 2.5 | 4.0 |

換算：*f* = √(η² / (1 − η²))；*d* = 2*f*（兩組時）；*r* = *d* / √(*d*² + 4)。
- Cohen 慣例是「沒有更好依據時的最後手段」；審稿人偏好從前導研究或文獻取得的效果量。
- 護理教育介入的效果量文獻上常見中度（*d* 約 0.5），但一定要引具體研究，不寫「一般而言」。
- 用中效果量算樣本數時要在限制中說明：若真實效果較小，研究檢定力不足。

## 三、G*Power 各檢定的輸入參數

G*Power 的 Test family → Statistical test → Type of power analysis（先驗用 A priori）。以下為常用組合的輸入欄位。

| 分析 | Test family | Statistical test | 需輸入 | 常見設定（示例） |
|---|---|---|---|---|
| 獨立樣本 t | t tests | Means: Difference between two independent means (two groups) | Tail(s)、Effect size *d*、α、Power、Allocation ratio N2/N1 | 雙尾、*d* = 0.50、α = .05、power = .80、比例 1 → 每組 64，共 128 |
| 配對樣本 t | t tests | Means: Difference between two dependent means (matched pairs) | Tail(s)、Effect size *d*z、α、Power | 雙尾、*d*z = 0.50 → 34 |
| 單因子 ANOVA | F tests | ANOVA: Fixed effects, omnibus, one-way | Effect size *f*、α、Power、Number of groups | *f* = 0.25、3 組 → 159 |
| 重複量數（組內） | F tests | ANOVA: Repeated measures, within factors | *f*、α、Power、Number of groups、Number of measurements、Corr among rep measures、Nonsphericity correction ε | *f* = 0.25、1 組、3 次測量、*r* = .50、ε = 1 → 28 |
| 重複量數（交互作用） | F tests | ANOVA: Repeated measures, within-between interaction | 同上加 Number of groups | 2 組 3 次測量 → 28 |
| 相關 | Exact | Correlation: Bivariate normal model | Tail(s)、Correlation ρ H1、α、Power、ρ H0 = 0 | 雙尾、ρ = .30 → 84 |
| 卡方（列聯表） | χ² tests | Goodness-of-fit tests: Contingency tables | Effect size *w*、α、Power、Df | *w* = 0.30、*df* = 1 → 88 |
| 多元迴歸 | F tests | Linear multiple regression: Fixed model, R² deviation from zero | Effect size *f*²、α、Power、Number of predictors | *f*² = .15、3 個預測變項 → 77 |
| 邏輯斯迴歸 | z tests | Logistic regression | Tail(s)、Odds ratio、Pr(Y=1|X=1) H0、α、Power、R² other X、X distribution | 依情境 |
| Mann–Whitney | t tests | Means: Wilcoxon-Mann-Whitney test (two groups) | 同獨立 t 加 Parent distribution | 通常比 t 多約 15% |

- 上表「常見設定」的人數是 G*Power 在該參數下的典型輸出，作為對照示例；**實際數字以使用者自己執行的 G*Power 結果為準**，本 skill 不代算。
- GEE 與混合模型 G*Power 不直接支援；可用「重複量數 ANOVA」近似並說明，或引用模擬與專門套件（例如 R 的 `longpower`、`simr`）並註明。
- 兩組人數不等時填 Allocation ratio。
- 螢幕上的 Protocol of power analyses 可直接複製到附錄，作為計算紀錄。

## 四、報告句型

**量性（獨立樣本 t，中文碩論）**
> 本研究以 G*Power 3.1.9.7 進行先驗樣本數估計。依 AUTHOR_INPUT_NEEDED（前導研究或文獻）之效果量 *d* = AUTHOR_INPUT_NEEDED，設定雙尾 α = .05、檢定力 = .80、兩組人數比 1:1，獨立樣本 t 檢定所需最小樣本數為每組 AUTHOR_INPUT_NEEDED 人，共 AUTHOR_INPUT_NEEDED 人；考量 20% 失訪率，預計招募 AUTHOR_INPUT_NEEDED 人。

**量性（英文）**
> An a priori power analysis using G\*Power 3.1.9.7 indicated that a total sample of AUTHOR_INPUT_NEEDED participants was required to detect a medium effect (*d* = 0.50; based on AUTHOR_INPUT_NEEDED) with 80% power at a two-tailed α of .05. Allowing for 20% attrition, AUTHOR_INPUT_NEEDED participants were recruited.

**重複量數**
> 以重複量數變異數分析（組內因子，3 次測量，測量間相關假設為 .50，ε = 1）、效果量 *f* = 0.25、α = .05、檢定力 .80 估計，所需樣本數為 AUTHOR_INPUT_NEEDED 人。

**相關或迴歸**
> 以多元迴歸（AUTHOR_INPUT_NEEDED 個預測變項）、效果量 *f*² = .15、α = .05、檢定力 .80 估計，所需樣本數為 AUTHOR_INPUT_NEEDED 人。

**沒有做先驗分析時（誠實寫法）**
> 本研究為前導性質，樣本數依 AUTHOR_INPUT_NEEDED（可行性、場域人數、DBR 慣例）決定，未進行先驗檢定力分析；本研究之推論統計以探索為目的，結果解讀以效果量與信賴區間為主。

## 五、失訪率加成

- 公式：最終招募數 = 最小樣本數 ÷ (1 − 預期失訪率)。**不是**乘以 (1 + 失訪率)。
  - 例：最小 64 人、失訪 20% → 64 ÷ 0.8 = 80 人（不是 64 × 1.2 = 77）。
- 失訪率依據：前導研究、同類介入文獻、場域經驗；常見 10% 至 20%，多時點追蹤可到 30%。
- 結果段要報實際流失人數與原因（CONSORT 流程圖或文字），並比較最終有效樣本是否仍達最小樣本數。
- 分析時說明遺漏值處理（完整個案分析、多重插補、GEE 的 MCAR 假設）。

## 六、質性研究的樣本數論述

質性研究不用檢定力，但審稿人仍要看到**人數的理由**。可用的論述框架：

**資訊力（Information power，Malterud et al., 2016）**：人數取決於五個面向，研究目的越窄、樣本越具特定性、理論基礎越強、對話品質越高、分析策略為個案深描時，所需人數越少。寫法：「本研究目的聚焦於專科護理師使用系統的臨床推理經驗，受訪者皆具 AUTHOR_INPUT_NEEDED 年以上臨床經驗且直接使用系統，訪談以 Tanner 模型為架構，具高度資訊力，故以 AUTHOR_INPUT_NEEDED 位受訪者為目標。」

**資料飽和（Saturation）**：說明判斷飽和的方式（連續 2 至 3 次訪談無新主題、編碼簿穩定），並報「第幾位受訪者後未再出現新主題」。不寫「達到飽和」而不說明如何判斷。

**經驗參考值（示例，引用時要附來源）**：
- 半結構式訪談的主題分析：文獻上常見 12 位左右出現多數主題（Guest et al., 2006），但取決於群體同質性。
- 放聲思考（think-aloud）：可用性領域慣例 5 至 10 位可發現多數問題（Nielsen 的估計基於問題偵測率，不是主題飽和）。
- 焦點團體：每場 5 至 8 人，3 至 4 場。

**混合方法**要分別說明量性與質性樣本，並說明兩者的關係（巢狀、平行、序列）。

## 七、DBR 與可用性研究的樣本數依據

**可用性測試（含 SUS）**：
- Nielsen 與 Landauer 的「5 位使用者可發現約 85% 的可用性問題」只適用於**問題發現**，不適用於 SUS 平均分的估計。
- 要報 SUS 平均分並與 68 基準比較時，樣本數影響信賴區間寬度。Sauro & Lewis 的經驗值：SUS 的 *SD* 約 17 至 21 分，若要 95% CI 半寬在 ±5 分內，約需 45 至 65 人；小樣本（10 至 20 人）的 CI 可達 ±10 分以上，要在限制中說明。
- 以 SUS 做前後或組間比較時，用 t 檢定的 G*Power 估計，效果量從前導研究取得。

**DBR**：
- 每輪迭代的樣本數依「這一輪要回答什麼設計問題」決定：早期迭代（原型可用性）5 至 10 位即可；後期迭代（成效初探）依量性檢定估計。
- 論文要列出**每一輪**的人數、身分（例如 NP 學生或臨床 NP）、是否重複參與、與前一輪的差異。
- 明確寫出 DBR 的推論限制：小樣本、無隨機分派、參與者可能重疊，結果為設計原則的形成性證據，不是成效的確證性證據。

**日誌與 token 成本資料**：
- 分析單位是「使用者」還是「對話回合」要說清楚；事件數不等於樣本數。
- 描述性統計（次數、中位數、四分位距）通常足夠，不需要檢定力論述。

## 八、事後檢定力的問題

- **事後檢定力（observed power）**用實際觀察到的效果量回算，與 *p* 值是同一件事的另一種表達，不能用來說明「不顯著是因為樣本不足」。審稿人常明確反對。
- 不顯著結果的正確處理：報效果量與 95% CI，說明區間包含哪些可能的效果；以「本研究能偵測的最小效果量（sensitivity analysis）」代替事後檢定力。
- G*Power 的 Sensitivity 模式：輸入 α、power、*N*，輸出「在此樣本數下能偵測的最小效果量」，可寫成「以本研究 *N* = AUTHOR_INPUT_NEEDED，α = .05、檢定力 .80，可偵測之最小效果量為 *d* = AUTHOR_INPUT_NEEDED」。

## 九、審查清單

- [ ] 樣本數對應主要假設與主要結果變項
- [ ] 效果量有來源，不只寫「中效果量」
- [ ] α、檢定力、單雙尾、軟體版本齊全
- [ ] 失訪率用除法加成
- [ ] 實際樣本與計畫樣本的差距有說明
- [ ] 質性部分有資訊力或飽和的具體判斷方式
- [ ] DBR 每輪人數與身分列清楚，推論限制寫在限制段
- [ ] 沒有用事後檢定力解釋不顯著
- [ ] SUS 小樣本的 CI 寬度有交代
