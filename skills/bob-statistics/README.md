# bob-statistics

護理與健康科學論文的統計報告 skill：審查、改寫或起草碩士論文與期刊投稿的「資料處理與分析」小節、結果段的統計句、APA 7 格式的表格與圖說，並處理量表信效度、SUS 計分、SPSS 報表轉表格、G*Power 樣本數論述。重點是透明、可複核、與研究設計一致，而不只是 p 值有沒有小於 .05。

## 用途

- 檢查「資料處理與分析」或 Statistical analysis 段是否寫齊：分析單位、檢定、假設檢查、多重比較、效果量、軟體版本。
- 把結果段的統計句改成 APA 7 格式：*t*(38) = 2.14，*p* = .039，*d* = 0.52，95% CI [0.21, 0.83]。
- 把 SPSS 輸出（t 檢定、ANOVA、卡方、相關、迴歸、信度、GEE、重複量數）轉成 APA 樣式表格，並抓 *p* = .000、漏報效果量、忽略 Levene、多重比較未校正等錯誤。
- 研究工具小節的信效度報告：Cronbach's α、KR-20、ICC、I-CVI 與 S-CVI/Ave、EFA／CFA 指標、翻譯回譯、自編問卷專家效度流程。
- SUS 計分公式、68 分基準、等第與形容詞量表的詮釋，以及「可用性不等於學習成效」的邊界。
- G*Power 各檢定的輸入參數與報告句型、失訪率加成、質性研究的資訊力與飽和論述、DBR 與可用性研究的樣本數依據。
- 針對審稿人或口試委員的統計意見，列出需要補的分析、可貼上的修改文字與回覆草稿。
- 跨摘要、正文、表格檢查同一統計量的數值與小數位是否一致。

## 觸發語

統計方法怎麼寫、統計審查、統計分析小節、資料分析段落、p 值、樣本數、G*Power、效果量、信度效度、Cronbach's α、CVI、SUS 分數、APA 統計格式、SPSS 報表轉表格、統計結果怎麼報告、審稿人統計意見、口試委員問樣本數。

## 範例提示詞

1. 「這是我碩論第三章的『資料處理與分析』草稿，研究是 DBR，量性資料有 SUS 與自編問卷的前後測（30 位專科護理師學生），質性有放聲思考。幫我審查統計敘述有沒有缺漏，缺的用 AUTHOR_INPUT_NEEDED 標出來。」
2. 「我貼 SPSS 的獨立樣本 t 檢定與 Levene 輸出給你，實驗組與對照組各 30 人，比較 SUS 總分。幫我轉成 APA 7 表格，並寫一句可以放進第四章的結果句。」
3. 「口試委員問：為什麼 SUS 只收 12 個人？請幫我寫一段樣本數依據，說明可用性研究的慣例、信賴區間的限制，以及 IRB 通過後正式研究要怎麼用 G*Power 估計。」

## 產出

- 統計審查報告：P0／P1／P2 問題、原文證據、修正方式、`AUTHOR_INPUT_NEEDED` 清單、審稿風險提示。
- 可貼上的資料分析段、結果句、圖說、APA 表格（Markdown；要 Word 或 Excel 檔時交 `docx`／`xlsx`）。
- 樣本數論述段落（中文碩論或英文投稿句型）。
- 統計類審稿意見與口試意見的逐點回覆草稿。

## 你需要提供

- 研究設計、組別、時間點、樣本數、分析單位（受試者、場次、事件）。
- 統計輸出、表格、圖說、結果段或審稿意見的原文。
- 哪些事實已確認、哪些要保守標註。

## 分工表

| 情境 | 交給 | bob-statistics 負責 |
|---|---|---|
| 研究設計要不要改、混合方法怎麼整合 | `mixed-methods-research` | 設計確定後的統計報告 |
| 用哪個報告準則 | `equator-guideline-finder` → `consort-2025-master`／`strobe-v4-master`／`prisma-2020-master` | 準則中統計條目的寫法 |
| 表格輸出成 Word／Excel | `docx`／`xlsx` | 表格內容與註 |
| 整章撰寫、APA 內文引用、去 AI 腔 | `academic-writing` | 統計小節與統計句 |
| 參考文獻格式 | `apa7-master` | 不處理 |
| 單一資深審稿人深度批判 | `academic-peer-reviewer` | 統計條目的逐點審查 |
| 三位互盲審稿模擬 | `bob-reviewer` | 統計軸的細部檢查 |
| 圖檔製作與解析度 | `bob-figure` | 圖說的統計文字與誤差線定義 |
| 回覆審稿意見全文 | `bob-response` | 統計類意見的回覆草稿 |
| 學術英文或中文潤飾 | `bob-polishing` | 統計句的正確性 |

## 邊界

- 不捏造樣本數、p 值、效果量、自由度、軟體版本、校正方法或檢定力分析。
- 不取代統計師或完整再分析；要重新建模時，需要原始資料與分析語法。
- 不從表格或圖片推斷分析單位；需要作者確認設計。
- 不把 SUS、滿意度或使用次數說成學習成效或臨床能力的證據。
- 不憑記憶引用期刊的字數或表格上限。

## 檔案結構

```text
bob-statistics/
  SKILL.md                                  router：立場、流程、輸出格式、分工邊界、紅線
  manifest.yaml                             always_load 與 on_demand 條件
  README.md
  UPSTREAM.md                               上游來源與逐檔清單
  references/
    apa7-statistics-format.md               APA 7 統計數字、符號、表格與圖樣式（繁中）
    nursing-instruments-reporting.md        量表信效度、翻譯回譯、SUS、自編問卷（繁中）
    spss-output-to-apa-table.md             SPSS 輸出→APA 表格對應與常見錯誤（繁中）
    sample-size-and-power.md                G*Power、效果量慣例、質性與 DBR 樣本數（繁中）
    statistical-reporting.md                方法段最低資訊與可貼上骨架（英文，附中文骨架）
    common-failure-modes.md                 P0/P1/P2 常見統計失誤（英文）
    figure-statistics.md                    圖說與誤差線檢查（英文）
    reviewer-checklist.md                   最終 QA 與回覆審稿結構（英文）
    source-basis.md                         來源階層：APA 7、EQUATOR、SAMPL（英文）
```
