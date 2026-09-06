---
name: bob-polishing
description: 潤飾、重組或翻譯護理與健康科學領域的學術文字（碩士論文章節、期刊投稿稿、摘要、標題），在不改動事實、證據邊界、術語與引用意圖的前提下提升清楚度與論證力；支援學術中文潤飾、中翻英、學術英文潤色、結果段精簡、去 AI 腔、Word 與 LaTeX 排版。Polish, restructure, or translate academic prose for nursing, medical education, and digital health manuscripts while preserving facts, evidence boundaries, terminology, and APA 7 citation intent. 觸發詞：潤稿、潤飾、潤色、英文潤色、改寫成學術英文、中翻英、學術英文、去 AI 腔、太像 AI 寫的、精簡結果段、主文太長、排版、Word 排版、表格跨頁、目錄更新、翻譯腔、贅字、摘要潤飾、標題建議、語言編輯。
---

# bob-polishing：學術文字潤飾（router）

本 skill 分兩層：

- **靜態層** `static/`：可版本化、可重用的內容片段（核心立場、論文類型、章節任務、語言規則、期刊風格）。
- **動態層**（本檔加 `manifest.yaml`）：判斷這次請求落在哪些軸上，只載入需要的片段。

不要憑記憶或只靠本檔套潤飾規則。每次都依下面的步驟從磁碟載入片段。

## 路由流程

每次觸發都跑完這五步。

### 1. 載入 manifest 與核心層

讀 [manifest.yaml](manifest.yaml)。它宣告四個軸（`paper_type`、`section`、`language`、`journal`）、允許的值、每個值對應的檔案。

同時讀 `always_load` 列出的每個檔案：預設立場、毛病診斷、輸出格式，以及 bob-shared 的讀者流程、論文類型分類、倫理、術語帳。

### 2. 判斷這次請求的軸值

依 manifest 的 `detect:` 提示與使用者輸入決定：

- `paper_type`：research / methods / hypothesis / algorithmic / review / qualitative / mixed-methods / dbr。預設 research。Bob 的碩論是 dbr；訪談與放聲思考的章節是 qualitative；量性加質性談整合是 mixed-methods。
- `section`：abstract / intro / results / discussion / conclusion / title / methods。可多選。碩論章節對應見 manifest。模糊且影響潤飾時先問。
- `language`：en / zh-tw / zh-tw-to-en。從草稿與使用者要的成品語言判斷。
- `journal`：generic-health / nursing / jmir / taiwan-nursing / ndmc-thesis / nature-family。預設 generic-health；nature-family 只在使用者明確指定時用。

用一行話向使用者說明判斷出的軸值，讓對方能低成本糾正。這是進度回報，不是核准關卡；除非有必要的決定未解，否則直接繼續。

### 3. 載入對應片段

每個軸值各讀 manifest 對應的那一個檔案。只有在使用者給的是沒有章節脈絡的零散文字時才跳過 `section`。

不要把 `static/` 全部讀進來。只載入第 2 步選到的。

### 4. 用載入的材料潤飾

依 `core/failure-modes.md` 的順序套用：

`論文類型 → 章節任務 → 證據配置 → 段落必要性 → 主張／證據／邊界 → 句子潤飾`

1. 論文類型的架構與寫作順序。
2. 章節任務與該章節的常見毛病。
3. 期刊的框架與限制。
4. 語言層的句子與段落規則（最後套用）。
5. 核心立場與倫理貫穿全程。

段落的結構問題若不捏造內容就修不好，標記出來，不要用文字蓋過去。這是紅線：不新增資料、引用、機轉、統計結果、新穎性宣稱。

結果段、整篇主文壓縮、主文與附錄的配置、修訂稿追加的文字：先載入 `../bob-shared/core/main-text-discipline.md`，分類每個結果、留最短的充分證據鏈、每次新增都觸發刪除或替換檢查。

結果段像分析清單時，載入 `../bob-shared/core/results-discussion-escalation.md` 重組為主張遞進。

任何討論段：載入 `../bob-shared/core/discussion-argument-language.md`，用功能標籤刪除結果複述、修復從具體發現到有邊界意涵的移動、校準情態動詞、讓限制對應具體主張。

前言或整篇敘事：載入 `../bob-shared/core/introduction-funnel.md`。摘要：載入 `../bob-shared/core/abstract-evidence-chain.md`。

方法段涉及 IRB、知情同意、報告準則、生成式 AI 揭露：載入 `../bob-shared/core/health-research-compliance.md` 對照必要元素，缺項只標記不補寫。

學術中文潤飾（`zh-tw`）需要完整的標點、數字、統計符號、圖表編號規範時，載入 `../bob-shared/core/zh-tw-academic-conventions.md`。

### 5. 需要時才開 references

`references/` 是深度參考，不是預設。依 manifest 的 `references.on_demand` 表按需開啟。

整篇手稿或多輪修改稿：載入 `../bob-shared/core/consistency-sweep.md`。逐段潤飾看不到累積的漂移：同一個變項有三種名稱、同一個量在兩種單位、同一個指標兩種精度、主張與自己的表格矛盾。先掃再修句子，掃到沒有新發現為止。

## 三種特殊請求

**去 AI 腔。** 使用者說「太像 AI 寫的」「去 AI 腔」「降 AI 感」且要維持學術體時，載入 `references/ai-trace-reduction.md`。先刪沒有資訊的句子、把泛稱換成具體事實、把排比拆成論證，再處理用詞。輸出在修訂說明附一條「AI 腔處理」摘要。若使用者要的是口語、講人話、給病人或大眾看的版本，轉交 `speak-human-tw`。

**排版（Word）。** 使用者要修的是 **位置與格式** 而非文字：表格跨頁、標題列重複、圖說跑掉、標楷體與 Times New Roman 混排、段落間距、目錄沒更新、頁碼不對、標題落在頁尾、孤行。跳過四個潤飾軸，直接載入 `references/word-layout.md`。輸出「問題 → 操作步驟」清單；需要直接改 .docx 檔時交給 `docx` skill 執行。

**排版（LaTeX）。** 稿件用 LaTeX 時載入 `references/latex-layout.md`。該檔自含診斷流程（編譯 → 縮圖總覽 → 讀 log）、float 設定、`[H]` 與 `\clearpage` 的用法、「寬圖在來源端重畫得更高」的規則。改前改後都要編譯並目視檢查頁面，不從 `.tex` 判斷版面。

## 分工邊界

本 skill 只做「潤飾既有文字」。以下情況交接：

| 情況 | 交給 |
|---|---|
| 從零撰寫整章、整合多篇文獻成段、輸出整章 .docx | `academic-writing`（其 humanize 流程處理撰寫時的 AI 痕跡；本 skill 的去 AI 腔只處理既有文字） |
| 台灣口語化、講人話、衛教文、社群文字 | `speak-human-tw` |
| 直接操作 .docx（批次改字型、插表格、產生目錄） | `docx`；本 skill 的 `word-layout.md` 負責說明要做什麼 |
| 參考文獻清單格式 | `apa7-master`；本 skill 不動 reference list，只保持內文引用不被改壞 |
| 論證架構重建、章節從頭規劃 | `bob-writing` |
| 審查意見回覆信 | `bob-response` |
| 統計文字與表格的正確性 | `bob-statistics`；本 skill 只修統計句子的文字，不改數字與檢定 |
| 概念分析、範疇性文獻回顧、混合方法的研究設計 | `concept-analysis-master`、`scoping-review-master`、`mixed-methods-research` |
| 單一深度審稿 | `academic-peer-reviewer` |

## 為什麼這樣拆

- 靜態層可版本化、可審閱。新增一種期刊或論文類型是一個新檔加一行 manifest。
- 動態層讓每次呼叫便宜：只有與這份草稿相關的片段進入上下文。
- router 刻意短。擴充範圍時改片段，不改本檔。
