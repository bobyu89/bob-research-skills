---
name: bob-writing
description: 依作者提供的主張、結果、圖表、筆記或中文草稿，起草、重組或規劃健康科學／護理／醫學教育／數位健康論文的章節、碩士論文各章與首次投稿材料；負責論證架構、段落任務、證據鏈、主文精簡與投稿信。Draft, restructure, or plan manuscript sections, thesis chapters, and first-submission materials for health-science and nursing research from author-provided evidence. 觸發詞：幫我寫緒論、寫討論、寫結論、寫摘要、結構式摘要、研究目的怎麼寫、論證架構、段落安排、證據鏈、碩論第一章、碩論第三章、計畫書前三章、文獻探討怎麼組織、結果章節、討論與結論、標題怎麼下、投稿信、cover letter、標題頁、作者貢獻、資料可用性聲明、推薦審稿人、首次投稿、投稿材料、主文太長怎麼精簡、這段流不流暢。
---

# bob-writing：健康科學論文撰寫 router

本 skill 分兩層：

- **靜態層** `static/`：版本化、可重用的內容片段（核心立場與流程、論文類型手冊、各章節撰寫規則、任務規則、語言規則、期刊風格）。
- **動態層**（本檔加 `manifest.yaml`）：偵測請求的軸值，只載入本次需要的片段。

不要憑記憶或只憑本檔套用撰寫邏輯。一律依下列步驟從磁碟載入片段。

## 路由協定

每次觸發都走這五步。

### 1. 載入 manifest 與核心層

讀 [manifest.yaml](manifest.yaml)。它宣告五個軸（`task`、`paper_type`、`section`、`language`、`journal`）、允許值與對應檔案。

同時讀 `always_load` 的每個檔案：共用層的讀者流程、論文類型分類、倫理、術語帳，以及本地的立場、流程、輸出格式。

### 2. 偵測本次請求的軸值

依 manifest 的 `detect:` 提示與使用者輸入決定：

- `task`：manuscript / submission-package / thesis-chapter。碩論章節用 thesis-chapter；首次投稿材料用 submission-package；修訂回覆屬 `bob-response`。
- `paper_type`：research / methods / hypothesis / algorithmic / review / qualitative / mixed-methods / dbr。預設 research。DBR 論文可同時載入 qualitative 或 mixed-methods。
- `section`：abstract / intro / literature-review / related-work / method / results / experiments / discussion / conclusion / title / thesis-ch1 到 thesis-ch5。可多選；含糊且影響草稿時先問。thesis-chN 要同時載入對應的 section 片段（ch1 intro、ch2 literature-review、ch3 method、ch4 results、ch5 discussion 加 conclusion）。
- `language`：en / zh-tw / zh-tw-to-en。依「輸出語言」決定；台灣中文期刊與碩論預設 zh-tw。
- `journal`：generic-health（預設）/ nursing / jmir / taiwan-nursing / ndmc-thesis；nature、nature-family、nat-comms、nat-mach-intell 為上游保留、非預設，只在使用者明確指定時載入。

起草前用一行向使用者陳述偵測到的軸值，讓對方能低成本糾正。這是進度回報，不是核准關卡；除非有必要決定未解決，否則繼續。

### 3. 載入對應片段

每個軸值各讀 manifest 對應的檔案。`task=submission-package` 或使用者只要一段不屬任何章節的論證段落時，跳過 `section` 軸。

不要讀完 `static/` 全部；只載入步驟 2 選到的。

### 4. 依載入的材料起草

套用順序：

1. 核心立場與交接（`core/stance.md`）：先找出缺漏的主張、證據、邊界，建立術語帳。
2. 論文類型手冊：論證鏈、起草順序。
3. 章節撰寫規則與結構。
4. 任務規則（thesis-chapter 或 submission-package）。
5. 期刊框架與限制。
6. 語言規則（最後套用）。

`task=manuscript` 與 `task=thesis-chapter` 都要完整跑 `core/workflow.md`：一句話論證、術語帳、段落地圖、**確認關卡（3b）**、起草、動詞校準、段落流暢檢查、回傳草稿與註記、**逐段修訂不整篇重寫（步驟 9）**。使用者要求直接給文字也不跳過規劃。

研究設計明確時，先呼叫 `equator-guideline-finder` 決定報告準則，再依 `../bob-shared/core/health-research-compliance.md` 把準則項目分配到各節。

撰寫或重組結果章節、或壓縮整篇主文時，加載 `../bob-shared/core/main-text-discipline.md`：先把每個結果依功能分類，配置到主文、表格、附錄，再寫最短充分證據鏈。完整的分析紀錄不等於完整的主文。

依章節加載共用層：

- 緒論或整篇敘事 → `../bob-shared/core/introduction-funnel.md`
- 摘要 → `../bob-shared/core/abstract-evidence-chain.md`
- 結果或討論 → `../bob-shared/core/results-discussion-escalation.md`
- 任何討論 → `../bob-shared/core/discussion-argument-language.md`
- 學術中文輸出 → `../bob-shared/core/zh-tw-academic-conventions.md`

這些是撰寫指引，不是期刊官方規定；目標期刊的現行規定優先。凡寫到具體期刊數字，標「以期刊官網為準，查核日期 YYYY-MM-DD」或標為示例。

`task=submission-package` 時依 `static/fragments/task/submission-package.md` 與 `references/submission-package.md`：建立交付矩陣與就緒稽核，投稿信用 `templates/submission/cover-letter.md`（Markdown／Word 版；LaTeX 為選用）。不要把稿件段落架構硬套到行政材料上。

關鍵證據或邊界缺漏時，寫佔位符並列在 `假設或缺漏輸入：`，不要捏造。

### 5. 只在需要時開 references

`references/` 是深度參考與範例庫，不是預設。依 manifest 的 `references.on_demand` 表按需開啟。典型觸發：

- 要具體範例或範本 → `references/examples/index.md`（多為 CS/AI 範例，只借結構）。
- 章節草稿有結構問題且片段解釋不了 → 對應的 `references/<section>.md`。
- 「這段流不流暢」 → `references/paragraph-flow.md`。
- 自我審查或退稿風險 → `references/paper-review.md`；要單一資深審稿人深度批判交 `academic-peer-reviewer`，要三位互盲審稿交 `bob-reviewer`。
- 完整首次投稿包或就緒稽核 → `references/submission-package.md`。
- 中文筆記轉英文的更多修法 → `references/chinese-author-workflow.md`。
- 期刊格式細節 → `../bob-shared/journal-formats/` 對應檔。

## 分工邊界

本 skill 負責 **論證架構、段落任務、證據鏈、主文精簡、首次投稿材料**。下列工作交接給既有 skill，不重複做：

| 需求 | 交給 |
|---|---|
| 整章輸出 .docx、多篇文獻整合成段、APA 內文引用、AI 痕跡消除 | `academic-writing` |
| 參考文獻清單格式（APA 第七版）產生與稽核 | `apa7-master` |
| 含系統性檢索的範疇性回顧（PCC、檢索策略、PRISMA-ScR） | `scoping-review-master` |
| 概念分析（Walker 與 Avant） | `concept-analysis-master` |
| 決定報告準則（CONSORT、STROBE、COREQ、SRQR、CHERRIES、TRIPOD+AI…） | 先問 `equator-guideline-finder`，再套對應的 *-master |
| 混合方法的研究設計（而非撰寫） | `mixed-methods-research` |
| 已有英文或中文草稿只需句子層潤飾 | `bob-polishing` |
| 找支持文獻、驗證 DOI、匯出 RIS | `bob-citation` |
| 統計呈現、APA 統計格式、SPSS 輸出轉表 | `bob-statistics` |
| 圖表製作、碩論 Word 插圖規格、圖形摘要 | `bob-figure` |
| 修訂信、逐點回覆、口試意見修改對照表 | `bob-response` |
| 投稿前模擬三位審稿人 | `bob-reviewer` |
| DBR 迭代紀錄、指導教授會議紀錄 | `bob-research-log` |
| 單篇論文閱讀整理 | `paper-analysis` |
| 講人話版本、口語化 | `speak-human-tw` |
| 檔案輸出 | `docx` / `pptx` / `xlsx` / `pdf` |

## 投稿階段邊界

- 本 skill 負責 **首次投稿前** 的稿件與材料。
- `bob-response` 負責編輯決定後的修訂信、逐點回覆、標記稿、申訴，以及碩論口試後的意見回覆表。
- 圖形摘要與 TOC 圖交 `bob-figure`；投稿前模擬審稿交 `bob-reviewer`。

## 使用者脈絡（預設假設，可被覆蓋）

- 國防醫學院護理學研究所專科護理師組碩士生；碩論為 DBR 設計的生成式 AI 加 RAG 臨床推理學習系統，理論框架 Tanner 臨床判斷模型，問診框架 LQQOPERA，資料含 SUS、自編問卷、系統日誌、token 成本、放聲思考、半結構式訪談。
- 投稿目標多為護理、醫學教育、數位健康期刊與台灣中文期刊；引用格式 APA 第七版；Word 為主要交付格式。
- 溝通與中文正文用台灣繁體中文；不用簡體與大陸用語。

## 為何這樣切分

- 靜態層可版本化、可審閱。新增一個期刊、論文類型或章節，就是一個新檔加一行 manifest。
- 動態層讓每次觸發便宜：只有相關片段進入脈絡。
- router 本身刻意短。擴充範圍時改片段，不改本檔。
- 結構與 `bob-polishing` 對稱，共用內容放在 `../bob-shared/`。
