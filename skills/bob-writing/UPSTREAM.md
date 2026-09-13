# UPSTREAM：bob-writing 的來源與變更紀錄

- 上游 repo：`nature-skills`（袁一哲等，Apache-2.0）
- 上游 skill：`skills/nature-writing/`（manifest version 1.5.0）
- 上游共用層：`skills/nature-shared/`（本集改為 `skills/bob-shared/`，由另一任務建置）
- 上游穩定副本：`C:\Users\USER\ai-skills\nature-skills`
- commit：`28150f30f8b4017991fca8c7b2839f02c6586d2f`（2026-09-06）
- 改造規格：`ADAPTATION-SPEC.md` 第 1 到 7 節，特別是第 6 節「bob-writing」
- 改造日期：2026-09-06

## 逐檔紀錄

### 刪除

| 檔案 | 說明 |
|---|---|
| `agents/openai.yaml` | 規格要求刪除 |
| `README_EN.md` | 規格要求刪除 |
| `static/fragments/language/zh-to-en.md` | 由 `language/zh-tw-to-en.md` 取代 |
| `static/fragments/journal/generic.md` | 由 `journal/generic-health.md` 取代 |

### 改名

| 上游 | 本集 | 說明 |
|---|---|---|
| `references/nature-summary-paragraph.md` | `references/summary-paragraph-broad-audience.md` | 內容保留（英文），改名以避免 nature-* 路由；manifest 標為非預設 |

### 改寫（繁中重寫，保留上游精髓）

| 檔案 | 保留的精髓 | 主要變更 |
|---|---|---|
| `SKILL.md` | 五步路由協定、只載入需要的片段、references 按需 | frontmatter `name: bob-writing`、繁中 description 與觸發詞、新增「分工邊界」表、「投稿階段邊界」、「使用者脈絡」；所有共用層路徑改 `../bob-shared/` 且只引用規格第 5 節檔名 |
| `manifest.yaml` | 五軸結構、always_load、references.on_demand | 新增 task=thesis-chapter；paper_type 加 qualitative / mixed-methods / dbr；section 加 literature-review / results / thesis-ch1 到 ch5；language 改 en / zh-tw / zh-tw-to-en；journal 改 generic-health（預設）/ nursing / jmir / taiwan-nursing / ndmc-thesis，Nature 系列保留但註明非預設；detect 全部繁中；on_demand 加入共用層新檔與本地新檔 |
| `README.md` | 用途、典型請求、你需要提供、產出、邊界 | 全繁中；三個台灣情境範例提示詞；分工表 |
| `static/core/stance.md` | 作者證據優先、主張紀律、intake、術語帳、確認關卡 | 繁中；加健康科學的動詞校準（可用性不等於成效）、報告準則路由、與既有 skill 的邊界 |
| `static/core/workflow.md` | 九步驟、1b 術語帳、3a 結果配置、3b 確認關卡、9 逐段修訂 | 繁中；一句話論證加碩論變體；中文動詞校準表；口試後修訂提醒 |
| `static/core/output-format.md` | 六項預設輸出、主文紀律稽核、submission-package 格式 | 繁中；新增 thesis-chapter 輸出格式 |
| `static/fragments/task/manuscript.md` | 一般章節流程 | 繁中；加報告準則與交接 |
| `static/fragments/task/submission-package.md` | 九步核心流程、預設交付項目、就緒狀態 | 繁中；共用層改為 generic-health / nursing-journals / jmir / taiwan-nursing；投稿信改 Markdown／Word 版預設、LaTeX 選用；加台灣語境提醒 |
| `static/fragments/section/intro.md` | 漏斗、段落任務、變體 | 英文保留；Nature 專屬句改為健康科學語境並指向 `introduction-funnel.md` |
| `static/fragments/section/abstract.md` | 證據鏈、診斷、紀律 | 英文保留；標題去 Nature；加結構式摘要指向 `abstract-evidence-chain.md` |
| `static/fragments/section/experiments.md` | 證據階梯、失敗模式 | 英文保留；標題改為演算法／系統評估專用並指向 `section/results.md`；路徑改 bob-shared |
| `static/fragments/section/discussion.md` | 全部 | 只改共用層路徑 |
| `static/fragments/section/related-work.md` | 全部 | 一句改為健康科學與碩論語境 |
| `static/fragments/journal/nature.md`、`nature-family.md`、`nat-comms.md`、`nat-mach-intell.md` | 全部內容 | 檔首加「非預設、未驗證」註記；移除對 bob-shared 不存在的 Nature 格式檔的引用，改為「查期刊官網並註明查核日期」；其餘路徑改 bob-shared |
| `references/submission-package.md` | 全部 | 第 9 節改為「Markdown／Word 預設、LaTeX 選用」並加入 `templates/submission/cover-letter.md`；`nature-figure` → `bob-figure`、`nature-response` → `bob-response` |
| `references/chinese-author-workflow.md` | 全部 | s2twp 簡轉繁（2 字） |
| `references/nat-comms-2025-corpus.md` | 全部 | s2twp 簡轉繁（31 字）；大陸用語改台灣用語（現在式、具體數字、明確）；`nature-polishing` → `bob-polishing`；manifest 標為非預設 |

### 新增

| 檔案 | 內容 |
|---|---|
| `static/fragments/paper_type/qualitative.md` | 質性研究論證鏈、各節段落任務、可信賴性四準則作為、引文呈現規則、動詞校準、失敗模式 |
| `static/fragments/paper_type/mixed-methods.md` | 混合方法論證鏈、設計類型與整合點、joint display 寫法、後設推論、失敗模式 |
| `static/fragments/paper_type/dbr.md` | DBR 論證鏈（設計原則→迭代→評估→設計知識）、四階段、結果兩種組織方式、迭代紀錄最小欄位、失敗模式 |
| `static/fragments/section/literature-review.md` | 碩論第二章與期刊 Background 的分節原則、每節段落任務、理論框架段、小結、口試委員意見 |
| `static/fragments/section/results.md` | 健康科學結果章節（由 experiments.md 改寫）：依設計的證據階梯、APA 統計呈現、表圖、質性與混合資料、口試委員意見 |
| `static/fragments/task/thesis-chapter.md` | 國防醫學院碩論五章骨架、計畫書與完成本差異、每章段落任務與常見口試委員意見、全章對照檢查 |
| `static/fragments/language/zh-tw.md` | 學術中文撰寫規則：標點、術語、句法、段落、中文動詞校準表、章節慣用語、失敗模式 |
| `static/fragments/language/zh-tw-to-en.md` | 由上游 zh-to-en 改寫：台灣作者常見英文問題修法表、輸出慣例 |
| `static/fragments/journal/generic-health.md` | 健康科學通用預設：IMRaD、結構式摘要、字數預算做法、配套項目、退稿原因、撰寫前檢查 |
| `static/fragments/journal/nursing.md` | 國際護理期刊撰寫動作層 |
| `static/fragments/journal/jmir.md` | JMIR 系列撰寫動作層（AI 系統描述、形成性研究定位） |
| `static/fragments/journal/taiwan-nursing.md` | 台灣中文護理與醫學教育期刊撰寫動作層 |
| `static/fragments/journal/ndmc-thesis.md` | 國防醫學院碩論的期刊軸動作層 |
| `templates/submission/cover-letter.md` | Markdown／Word 版首次投稿信範本（英文與中文，護理期刊語境） |
| `README.md`、`UPSTREAM.md` | 本集要求 |

### 保留（未改或只改路徑）

- `static/fragments/paper_type/research.md`、`methods.md`、`hypothesis.md`、`algorithmic.md`、`review.md`（英文）
- `static/fragments/section/method.md`、`conclusion.md`、`title.md`（英文）
- `static/fragments/language/en.md`（英文）
- `references/abstract.md`、`article-architecture.md`、`conclusion.md`、`experiments.md`、`introduction.md`、`method.md`、`paper-review.md`、`paragraph-flow.md`、`related-work.md`、`examples/**`（英文）
- `templates/submission/*.tex`（四個 LaTeX 範本，標為選用）

## 假設

1. `bob-shared` 由另一任務同時建置；本 skill 只引用規格第 5 節清單中的檔名，驗收時以清單為準並同時記錄磁碟存在性。
2. 上游 references 內以 CS/AI 為主的範例（`references/examples/**`、`introduction.md`、`method.md`、`nat-comms-2025-corpus.md`）保留英文原文，manifest 註明「多為 CS/AI 範例，只借結構」。
3. journal 軸的 `nature-family` 等值名稱含「nature-」字樣，屬 manifest 鍵值而非 skill 名稱或路由；規格第 7 節第 4 項的 grep 清單不含它，故保留。
4. 期刊具體數字：本 skill 新寫內容一律不寫死，改為「以期刊官網為準，查核日期 YYYY-MM-DD」或標示例；上游保留的 Nature 系列片段檔首加註「所有數字以期刊官網為準」。
5. `section` 軸的 `thesis-ch1` 到 `thesis-ch5` 皆指向 `task/thesis-chapter.md`，配對的 section 片段由 SKILL.md 與 manifest detect 說明載入。
6. results.md 中「SUS 68 分以上為高於平均」為量表詮釋基準示例，來源需在方法章交代，非期刊規定。

## 驗收結果（規格第 7 節）

見下方由檢查腳本附加的結果。

執行日期：2026-09-06

### 1. SKILL.md frontmatter
- name = `bob-writing`（目錄名 bob-writing）：通過
- description 含繁中觸發詞：通過
- frontmatter 無 nature- 字樣：通過
- SKILL.md 行數：126（上限 250）：通過

### 2. manifest.yaml 路徑存在性
- 本地路徑 51 條，缺漏 0：通過
- bob-shared 路徑 17 條，全部在規格第 5 節清單內：通過
- bob-shared 路徑於磁碟存在（驗收當時）：全部存在

### 3. s2twp --check（所有 .md .yaml）
- 回傳 0：通過

### 4. 禁用字串 grep（只允許出現在 UPSTREAM.md）
- 僅 UPSTREAM.md 含上游名稱：通過

### 5. README.md 三個台灣情境範例
- README 含台灣情境關鍵詞的行數：4，三個範例提示詞分別涉及 DBR／Tanner／SUS、護理雜誌／結構式摘要、Nurse Education Today／醫院 IRB：通過

### 6. 硬編碼期刊數字
- 新寫檔案未寫死期刊字數或圖表上限；出現的比例與分數為示例並標示。上游保留的 Nature 系列片段（nature.md、nature-family.md、nat-comms.md、nat-mach-intell.md）與 references/summary-paragraph-broad-audience.md、nat-comms-2025-corpus.md 含上游原有數字，檔首或 manifest 已註明非預設、以期刊官網為準：通過（附條件）

### 補充：新 fragment 行數（規格要求 60 到 150）
- static/fragments/paper_type/qualitative.md：79 行
- static/fragments/paper_type/mixed-methods.md：83 行
- static/fragments/paper_type/dbr.md：87 行
- static/fragments/section/literature-review.md：81 行
- static/fragments/section/results.md：84 行
- static/fragments/task/thesis-chapter.md：94 行
- static/fragments/language/zh-tw.md：71 行
- static/fragments/language/zh-tw-to-en.md：76 行
- static/fragments/journal/generic-health.md：70 行
- static/fragments/journal/nursing.md：67 行
- static/fragments/journal/jmir.md：68 行
- static/fragments/journal/taiwan-nursing.md：65 行
- static/fragments/journal/ndmc-thesis.md：66 行
