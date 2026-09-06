---
name: bob-response
description: >-
  擬稿、稽核或改寫期刊修訂回覆包：逐點回覆表（每位審稿人一份、互盲隔離）、rebuttal、修訂版
  cover letter、修改處標示（紅字或底線）的修改稿摘錄，以及碩士論文口試後的口試委員意見回覆表。
  先解析退修信、確認主要或次要修訂，再把意見編號（E.1／R1.1）、分類動作、建立追蹤表，
  防止回覆與修改不一致、防止文稿因審稿而累積贅文。語境為護理、醫學教育、數位健康期刊與
  台灣中文期刊；APA 第七版；輸出繁中或英文。
  Draft, audit, or revise point-by-point reviewer responses, rebuttals, revision cover letters,
  marked-change excerpts, and thesis committee response tables with mutually blind reviewer isolation.
  觸發詞：回覆審稿意見、審稿回覆、逐點回覆、rebuttal、修訂說明、修訂說明表、退修信、
  審查意見回覆、主要修訂、次要修訂、修改後再審、修改處標示、紅字標示、cover letter 修訂版、
  修訂版投稿信、口試委員意見回覆表、口試意見修改對照表、response to reviewers、point-by-point response。
---

# bob-response：審稿意見回覆 Router

本 skill 分成兩層：

- **靜態層** `static/`：預設立場與紅線（`stance.md`）、工作流程與輸出格式（`workflow.md`）。每次都載入。
- **動態層**（本檔加 `manifest.yaml`）：依步驟需要才載入 `references/` 與 `templates/` 的深度內容。

不要憑記憶或只憑本 router 執行回覆邏輯。一律依下列步驟從磁碟載入。

## 路由步驟

每次觸發都走完這五步。

### 1. 載入 manifest 與核心層

讀 [manifest.yaml](manifest.yaml)，再讀 `always_load` 列出的每個檔案：

- `static/core/stance.md`：目的、預設立場、紅線、來源優先順序。
- `static/core/workflow.md`：可接受的輸入、決定類型關卡、口試委員模式、二十步流程、輸出格式。

### 2. 辨識模式、決定類型與語言

本 skill 沒有內容軸（不像 bob-writing 有 paper_type／section），變化在執行期辨識：

- **任務模式**：`draft`／`audit`／`revise`／`triage-only`／`cover-letter`／`revision-package`／`latex-template`／`committee-response`／`appeal-like`。
- **決定類型**：`Major Revision`（主要修訂）／`Minor Revision`（次要修訂）／revise-and-resubmit／transfer after review／不明。中文期刊的「修改後再審」對應主要修訂，「修改後刊登」對應次要修訂。
- **語言**：投稿英文期刊時回覆信用英文並附「中文核對」；投稿中文期刊或口試委員回覆表用繁體中文。

決定類型是一般修訂工作的必經關卡。先從退修信擷取；仍不明時，問一句「這是主要修訂（Major Revision）還是次要修訂（Minor Revision）？如果退修信沒有明確寫，請把退修信貼給我，我幫你判斷。」然後暫停。不可從意見數量、語氣或工作量推測。

輸入是碩士論文口試後的委員意見時，走 `committee-response` 模式：不套互盲過濾、編號用 `C1.1`／`A.1`、不問主要或次要修訂，改問口試類型與所辦繳交要求。載入 `references/thesis-committee-response.md`。

用 `references/intake-and-routing.md` 決定任務模式、最少輸入與就緒狀態。申訴類案例另行路由，不預設寫申訴信。

### 3. 執行工作流程

依 `static/core/workflow.md` 執行：貼上期刊信件時先擷取稿件資訊、決定類型、編輯指示、審稿人報告邊界、要求的檔案、期限與可見性規則；通過決定類型關卡；套用主要或次要修訂策略但不降低個別意見的嚴重程度；先編輯指示（`E.1`）再審稿意見（`R1.1`、`R2.1`）；每條分類動作與獨立驗證的工作狀態；先建內部總策略與追蹤表；為每位互盲審稿人各擬一份隱私過濾的獨立回覆；審稿人漏看文中已有內容時視為清晰度問題，改呈現而不是回「文中已說明」；需要時擬 cover letter；每一項宣稱的修改都對應到頁、行、段或明確佔位符；修改文稿時在備份副本上以紅字或底線標示；回覆信中貼上的修訂文字用斜體；標示缺少的作者輸入；跑 QA；由逐項狀態推導整包就緒狀態。

回覆提議或執行主文修改時，同時載入 `../bob-shared/core/main-text-discipline.md`。回覆信裡完整回答，文稿只改讀者需要的最短文字；優先取代或壓縮，非中心的穩健性與調和細節移到附錄／補充資料。

絕不捏造實驗、分析、引用文獻、行號、圖版、附錄項目、編輯指示或文稿修改。作者必須補的事項標 `AUTHOR_INPUT_NEEDED`。

### 4. 按需載入 references 與 templates

`references/` 與 `templates/` 是深度資源，不是預設載入。依 manifest 的 `references.on_demand` 條件開啟：

- `references/comment-taxonomy.md`：意見分類與嚴重程度。
- `references/action-mapping.md`：動作標籤、工作狀態、追蹤表欄位、就緒狀態。
- `references/tone-and-stance.md`：建議句型、禁用句型、不同意的寫法。
- `references/difficult-cases.md`：做不到的實驗、審稿人事實錯誤、意見衝突、重複意見、統計批評、倫理、轉投、申訴類。
- `references/chinese-author-alignment.md`：台灣作者常見回覆問題（過度道歉、全盤接受、回覆與修改不一致、把「已在文中說明」當回覆）與中文筆記轉換。
- `references/taiwan-journal-norms.md`：護理雜誌、護理研究等中文期刊的修訂說明表、修改處標示、一稿一表慣例（以期刊官網為準，查核日期 2026-09-06）。
- `references/thesis-committee-response.md`：口試委員意見回覆表模式。
- `references/response-structure.md`：整包格式、回覆信結構、cover letter 結構。
- `templates/response-letter.md`、`templates/revision-cover-letter.md`、`templates/committee-response-table.md`：Markdown／Word 範本。
- `references/latex-templates.md` 與 `templates/*.tex`：LaTeX 範本，選用；使用者明確要 LaTeX 時才用。
- `references/package-consistency-audit.md` 與 `scripts/check_package_consistency.py`：同時修改了文稿、或整包要交付時的一致性稽核。Word 稿以人工核對頁碼與引句為主，腳本只支援 LaTeX。
- `references/qa-checklist.md`：定稿前 QA。
- `../bob-shared/core/consistency-sweep.md`：文稿內部數字與術語一致性掃描。
- `../bob-shared/core/health-research-compliance.md`：審稿人質疑 IRB、報告準則或 AI 揭露時的準則路由。
- `../bob-shared/core/zh-tw-academic-conventions.md`、`../bob-shared/journal-formats/taiwan-nursing.md`：繁中回覆表與台灣中文期刊修訂回覆的用語與格式慣例。

`qa-checklist.md` 與 `package-consistency-audit.md` 互補：前者問回覆是否完整、誠實、語氣得當；後者問修改稿、清稿、回覆信三者是否真的一致。任何一次文稿修改都會讓回覆信的引句與頁碼失效，所以稽核要重跑，不是最後做一次。

### 5. 分工邊界

bob-response 只負責「修訂回覆」這一段。下列工作交接給既有 skill，不在本 skill 內重做：

| 需求 | 交給 | 本 skill 的角色 |
|---|---|---|
| 投稿前模擬審稿、預測審稿人會問什麼 | `bob-reviewer`（三位互盲審稿人＋綜合）；要單一資深審稿人深度批判時用 `academic-peer-reviewer` | 收到真正的審稿意見後才由本 skill 接手 |
| 改寫或潤飾文稿段落、回覆信英文語氣 | `bob-polishing` | 本 skill 決定「改什麼、改在哪」；句子層級的潤飾交出去 |
| 統計相關的審稿意見（檢定選擇、效果量、樣本數、SUS 計分） | `bob-statistics` | 本 skill 標 `TODO_ANALYSIS`，把意見與現有分析交過去，拿回 APA 7 統計句再貼進回覆 |
| 參考文獻格式、新增文獻的 APA 7 格式 | `apa7-master` | 本 skill 只記「已新增文獻 X」與位置 |
| 找支持文獻、驗證審稿人要求的引文是否存在 | `bob-citation` | 本 skill 標 `ADD_CITATION` 與 `AUTHOR_INPUT_NEEDED` |
| 回覆表、cover letter、修改稿輸出成 Word | `docx` | 本 skill 產生 Markdown 表格與文字後交出 |
| 整章重寫（例如審稿人要求重寫討論） | `academic-writing`；論證架構先問 `bob-writing` | 本 skill 只給修改清單與段落任務 |
| 研究設計本身被質疑（混合方法整合、DBR 迭代設計） | `mixed-methods-research` 或指導教授討論 | 本 skill 記 `TODO_AUTHOR_CONFIRM` |
| 口語化、去 AI 腔的中文 | `speak-human-tw` | 本 skill 的中文回覆表是正式學術文體，不口語化 |

## 為什麼這樣切

- 靜態層有版本、可審閱；一般回覆只需要小小的核心。
- 動態層讓每次觸發都便宜：困難案例、分類、QA 的深度只在需要時載入。
- router 刻意短。要擴充範圍時改 fragments 與 references，不改本檔。
- 結構與 bob-writing、bob-polishing、bob-reviewer、bob-citation、bob-statistics、bob-figure 一致。
