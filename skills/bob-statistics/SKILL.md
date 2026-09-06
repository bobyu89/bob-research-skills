---
name: bob-statistics
description: >-
  審查、改寫或起草護理與健康科學論文（碩士論文、期刊投稿）的統計方法與結果報告，採 APA 第七版統計格式，
  涵蓋描述統計、t 檢定、ANOVA、卡方、相關、迴歸、信度（Cronbach's α）、效度（CVI、EFA／CFA）、GEE／混合模型、
  無母數、G*Power 樣本數、SUS 計分與詮釋、SPSS 報表轉 APA 表格。
  Audit, rewrite, or draft statistical reporting for nursing and health-science manuscripts in APA 7 style.
  觸發詞：統計方法怎麼寫、統計審查、統計分析小節、p 值、樣本數、G*Power、效果量、信度效度、Cronbach's α、
  CVI、SUS 分數、APA 統計格式、SPSS 報表轉表格、審稿人統計意見、統計結果怎麼報告、資料分析段落。
---

# bob-statistics：護理研究統計報告 skill

用這個 skill 讓論文的統計敘述透明、可複核、與研究設計一致。它是「報告與審查」skill，不是統計師的替身：除非使用者提供原始資料並明確要求計算，否則不做再分析。所有輸出用台灣繁體中文說明，可貼上的段落依使用者指定語言（中文碩論或英文投稿）產出。

## 預設立場

- 設計透明優先於漂亮的統計用語。
- 把三個問題分開：測了什麼、分析單位是什麼、宣稱了什麼推論。
- 以獨立的分析單位作為預設的 `n`。同一位受試者的多次作答、多個題項、多個情境、系統日誌的多筆事件、放聲思考的多個片段，不可未經說明就當成獨立樣本。
- 效果量、信賴區間、樣本數與確切的檢定定義，優先於「顯著／不顯著」的二分敘述。
- 缺少的資訊一律標 `AUTHOR_INPUT_NEEDED`，不捏造樣本數、檢定、軟體版本、校正方法、排除規則、隨機化、盲化或檢定力分析。
- 統計格式預設 APA 7（`references/apa7-statistics-format.md`）；目標期刊若有更具體規定，以期刊為準並註明來源。
- 遇到研究設計對應的報告準則（CONSORT、STROBE、COREQ、CHERRIES、TRIPOD+AI 等），先交由 `equator-guideline-finder` 決定準則，再套用其統計條目。

## 可接受的輸入

- 論文第三章「資料處理與分析」或投稿稿件的 Statistical analysis 段落
- 含檢定統計量或 p 值的結果段落、表格、圖說
- SPSS、R、jamovi 等軟體的原始輸出或截圖文字
- 量表信效度資料（Cronbach's α、CVI、因素負荷量）
- SUS 或其他問卷的原始作答與計分需求
- G*Power 輸入參數或樣本數論述
- 審稿人或口試委員關於統計的意見
- 使用者的中文或英文說明筆記

輸入不完整時，做有邊界的審查，並明確列出無法評估的部分。

## 工作流程

1. **判定任務類型**：審查、改寫、起草、回覆審稿意見、圖表統計對齊、SPSS 輸出轉表格、樣本數論述，或（僅在提供資料時）實際計算。
2. **抽出研究設計**：組別、介入、時間點、結果變項、配對或重複量數結構、隨機化、盲化、排除條件、遺漏值處理。DBR 或可用性研究要註明是哪一輪迭代、哪一批受試者。
3. **定義 `n` 與重複層級**：受試者、場次、題項、事件、片段，逐一釐清哪一層是獨立單位。
4. **把每個宣稱對應到分析**：比較或模型、檢定家族、假設檢查、多重比較校正、效果量、區間、p 值報告政策。
5. **檢查常見失誤**：`references/common-failure-modes.md`（巢狀資料、多重比較、交互作用誤推、相關過度詮釋、小樣本、只報顯著性）。
6. **檢查報告完整度**：`references/statistical-reporting.md`（方法段的最低資訊、段落順序、可貼上骨架）。
7. **套用 APA 7 統計格式**：`references/apa7-statistics-format.md`（斜體、小數位、p 值寫法、表格樣式）。
8. **依需求載入專題檔**：量表信效度與 SUS → `references/nursing-instruments-reporting.md`；SPSS 輸出 → `references/spss-output-to-apa-table.md`；樣本數與檢定力 → `references/sample-size-and-power.md`；圖說與誤差線 → `references/figure-statistics.md`。
9. **起草或改寫**：產出保守、可直接貼上的文字，宣稱不超出設計與證據。不把相關升級成因果，不把可用性分數升級成學習成效。
10. **最終 QA**：`references/reviewer-checklist.md`（嚴重度標籤、待作者確認事項、審稿風險）。同一統計量出現在多處時，跑 `../bob-shared/core/consistency-sweep.md`。

## 輸出格式

除非使用者另有指定，審查任務回傳：

```text
統計審查範圍
- 審查的輸入：
- 邊界／缺少的材料：
- 研究設計判讀：
- 分析單位與重複層級判讀：

主要統計問題
- [P0/P1/P2] 問題：
  原文證據：
  為何重要：
  修正方式：

可貼上的修訂版
[改寫後的資料分析段／結果段／表格／圖說]

AUTHOR_INPUT_NEEDED
- [只列簡短的事實問題]

審稿風險提示
- 統計審稿人仍可能質疑的點：
```

資訊充足的單純起草任務，略過問題清單，回傳：

```text
資料分析段草稿
[可貼上文字]

報告備註
- n 的定義：
- 檢定／模型：
- 多重比較：
- 軟體與版本：
- 未確認欄位：
```

SPSS 轉表格任務，回傳 APA 樣式表格（Markdown），並在表下列出「註」與需要補的欄位；需要 Word 或 Excel 檔時交給 `docx`／`xlsx` skill。

## 分工邊界

| 情境 | 交給 | 本 skill 保留的部分 |
|---|---|---|
| 研究設計本身要不要改（混合方法整合、DBR 迭代設計、質性取樣） | `mixed-methods-research` | 設計確定後的統計報告 |
| 決定適用哪個報告準則 | `equator-guideline-finder` → `consort-2025-master`／`strobe-v4-master`／`prisma-2020-master` | 準則裡的統計條目如何寫 |
| 表格輸出成 Word 或 Excel | `docx`／`xlsx` | 表格內容、欄位、註的文字 |
| 整章論文撰寫、APA 內文引用 | `academic-writing` | 「資料處理與分析」小節與結果段的統計句 |
| 參考文獻格式 | `apa7-master` | 不處理 |
| 單一資深審稿人深度批判 | `academic-peer-reviewer` | 統計條目的逐點審查 |
| 圖檔製作 | `bob-figure` | 圖說的統計文字與誤差線定義 |
| 回覆審稿意見全文 | `bob-response` | 統計類意見的回覆草稿與需補的分析 |

## 紅線

- 不捏造 p 值、樣本數、自由度、信賴區間、效果量、軟體版本、校正方法、預先註冊、排除規則或檢定力分析。
- 分析單位或設計不清楚時，不把任何檢定當成最終建議。
- 不接受「n = 題項數／事件數／片段數」為獨立重複，除非已確認資料階層。
- 不把「顯著」當成重要、大、因果或臨床有意義的同義詞。
- 不把不顯著或微弱的結果改寫成更強的宣稱；也不把 SUS 分數、滿意度或使用次數說成學習成效或臨床能力的證據。
- 不給臨床試驗設計、藥物劑量或法規層級的統計建議；只做論文報告層級的檢查。
- 不憑記憶引用期刊的字數或表格上限；寫到具體規定時標「以期刊官網為準，查核日期」。

## 相關檔案

| 檔案 | 何時開啟 |
|---|---|
| [references/source-basis.md](references/source-basis.md) | 需要來源階層，或要說明為何強調透明與設計報告 |
| [references/apa7-statistics-format.md](references/apa7-statistics-format.md) | 任何要寫成 APA 7 格式的統計數字、符號、表格或圖 |
| [references/statistical-reporting.md](references/statistical-reporting.md) | 起草或審查資料分析段、方法段、結果段 |
| [references/common-failure-modes.md](references/common-failure-modes.md) | 看到巢狀資料、多重比較、交互作用宣稱、相關／迴歸、離群值、小樣本或過強的 p 值語言 |
| [references/nursing-instruments-reporting.md](references/nursing-instruments-reporting.md) | 量表與問卷的來源、計分、信度、效度、翻譯、SUS 計分與詮釋、自編問卷專家效度 |
| [references/spss-output-to-apa-table.md](references/spss-output-to-apa-table.md) | 把 SPSS 輸出轉成 APA 表格，或檢查 p = .000 之類的常見錯誤 |
| [references/sample-size-and-power.md](references/sample-size-and-power.md) | G*Power 參數與報告句型、效果量慣例、質性與可用性研究的樣本數論述 |
| [references/figure-statistics.md](references/figure-statistics.md) | 檢查圖說、誤差線、星號、盒鬚圖、補充資料註 |
| [references/reviewer-checklist.md](references/reviewer-checklist.md) | 完成審查前的 QA，或準備審稿風險摘要與回覆草稿 |
| [../bob-shared/core/consistency-sweep.md](../bob-shared/core/consistency-sweep.md) | 同一統計量出現在摘要、正文、表格多處，或區間術語有疑義 |
| [../bob-shared/core/health-research-compliance.md](../bob-shared/core/health-research-compliance.md) | 需要對照 IRB、知情同意、EQUATOR 準則路由或生成式 AI 使用揭露 |

## 來源階層

1. 使用者提供的論文、資料、計畫書、統計分析計畫、審稿意見、期刊投稿須知。
2. APA 第七版《Publication Manual》的統計與數字呈現規範。
3. 研究設計對應的 EQUATOR 報告準則（CONSORT、STROBE、PRISMA、COREQ、CHERRIES、TRIPOD+AI）與 SAMPL 統計報告指引。
4. 保守的統計報告慣例（`references/source-basis.md`）。

材料不足以做出可辯護的統計建議時，先問缺少的設計事實，或給有邊界的措辭選項，不猜。
