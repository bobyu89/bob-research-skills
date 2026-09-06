# UPSTREAM

## 來源

- 上游專案：`nature-skills`（袁一哲等，Apache-2.0）
- 上游 skill：`skills/nature-polishing/`
- 本機穩定副本：`C:\Users\USER\ai-skills\nature-skills\skills\nature-polishing\`
- commit：`28150f30f8b4017991fca8c7b2839f02c6586d2f`（2026-09-06）
- 改造規格：`ADAPTATION-SPEC.md` 第 3、4、5、6（bob-polishing）、7 節
- 改造日期：2026-09-06

上游所有指向 `../nature-shared/` 的路徑一律改為 `../bob-shared/`，且只引用規格第 5 節列出的檔案。上游依賴的 `nature-shared/core/nature-results-discussion.md`、`nature-introduction.md`、`nature-abstract.md` 分別對應到 bob-shared 的 `results-discussion-escalation.md`、`introduction-funnel.md`、`abstract-evidence-chain.md`；`nature-shared/journal-formats/nat-comms.md`、`nature-machine-intelligence.md` 在 bob-shared 沒有對應檔，相關引用已刪除。

## 逐檔清單

| 上游檔案 | 處置 | 目標檔案 | 說明 |
|---|---|---|---|
| `SKILL.md` | 改寫 | `SKILL.md` | frontmatter `name: bob-polishing`；description 改為繁中觸發詞；正文繁中 router，保留五步路由與「論文類型 → 章節任務 → 段落邏輯 → 主張／證據／邊界 → 句子潤飾」順序；新增去 AI 腔、Word 排版兩種特殊請求與分工邊界段 |
| `manifest.yaml` | 改寫 | `manifest.yaml` | `paper_type` 增 qualitative / mixed-methods / dbr；`language` 改為 en / zh-tw / zh-tw-to-en；`journal` 改為 generic-health / nursing / jmir / taiwan-nursing / ndmc-thesis / nature-family；`references.on_demand` 對應新的 bob-shared 與本地 references |
| `README.md` | 改寫 | `README.md` | 繁中；用途、觸發語、範例提示詞、分工表、邊界、目錄結構 |
| `README_EN.md` | 刪除 | | 規格要求 |
| `agents/openai.yaml` | 刪除 | | 規格要求 |
| `static/core/stance.md` | 改寫 | `static/core/stance.md` | 繁中；保留不捏造紅線、術語帳、em dash 規則；新增 APA 7 引用不動、台灣護理與健康科學語境預設 |
| `static/core/failure-modes.md` | 改寫 | `static/core/failure-modes.md` | 繁中；保留修正優先順序；新增中文稿、英文稿、AI 腔的毛病類別與「不能靠潤飾解決的問題」 |
| `static/core/output-format.md` | 改寫 | `static/core/output-format.md` | 繁中；新增中文標點慣例、去 AI 腔與排版時的輸出格式 |
| `static/fragments/paper_type/research.md` | 保留 | 同路徑 | 英文原樣 |
| `static/fragments/paper_type/methods.md` | 保留 | 同路徑 | 英文原樣 |
| `static/fragments/paper_type/hypothesis.md` | 保留 | 同路徑 | 英文原樣 |
| `static/fragments/paper_type/algorithmic.md` | 保留 | 同路徑 | 英文原樣 |
| `static/fragments/paper_type/review.md` | 保留 | 同路徑 | 英文原樣 |
| （無） | 新增 | `static/fragments/paper_type/qualitative.md` | 質性研究潤飾診斷：方法、主題與引文結構、可信賴性、常見毛病 |
| （無） | 新增 | `static/fragments/paper_type/mixed-methods.md` | 混合方法潤飾診斷：整合段、聯合呈現、收斂與分歧用語 |
| （無） | 新增 | `static/fragments/paper_type/dbr.md` | 設計本位研究潤飾診斷：迭代週期、設計原則、可用性與成效的區分 |
| `static/fragments/section/abstract.md` | 保留 | 同路徑 | 英文原樣 |
| `static/fragments/section/intro.md` | 保留 | 同路徑 | 英文原樣 |
| `static/fragments/section/results.md` | 改寫（局部） | 同路徑 | 共用路徑改為 `bob-shared/core/results-discussion-escalation.md`；去 Nature 專屬句；加 APA 7 與質性結果提示 |
| `static/fragments/section/discussion.md` | 改寫（局部） | 同路徑 | 共用路徑改為 bob-shared |
| `static/fragments/section/conclusion.md` | 保留 | 同路徑 | 英文原樣 |
| `static/fragments/section/title.md` | 保留 | 同路徑 | 英文原樣 |
| `static/fragments/section/methods.md` | 保留 | 同路徑 | 英文原樣 |
| `static/fragments/language/en.md` | 改寫（局部） | 同路徑 | 加拼法依期刊的說明 |
| `static/fragments/language/zh-to-en.md` | 改寫並改名 | `static/fragments/language/zh-tw-to-en.md` | 繁中；台灣作者常見英文問題（冠詞、時態、名詞堆疊、中式連接詞、which、保留語） |
| （無） | 新增 | `static/fragments/language/zh-tw.md` | 學術中文潤飾：贅字、翻譯腔、被動句、「進行……的動作」、「的」字串、術語、全形標點、數字與單位、APA 中文引用 |
| `static/fragments/journal/generic.md` | 改寫並改名 | `static/fragments/journal/generic-health.md` | 健康科學期刊通用預設 |
| `static/fragments/journal/nature.md` | 合併 | `static/fragments/journal/nature-family.md` | 三個 Nature 系列 fragment 合併為一個非預設檔；刪除所有寫死的字數與圖表數 |
| `static/fragments/journal/nat-comms.md` | 合併 | `static/fragments/journal/nature-family.md` | 同上 |
| `static/fragments/journal/nat-mach-intell.md` | 合併 | `static/fragments/journal/nature-family.md` | 同上 |
| （無） | 新增 | `static/fragments/journal/nursing.md` | 國際護理期刊潤飾動作 |
| （無） | 新增 | `static/fragments/journal/jmir.md` | JMIR 系列潤飾動作 |
| （無） | 新增 | `static/fragments/journal/taiwan-nursing.md` | 台灣中文護理期刊潤飾動作 |
| （無） | 新增 | `static/fragments/journal/ndmc-thesis.md` | 國防醫學院碩士論文潤飾動作 |
| `references/latex-layout.md` | 保留（局部改） | 同路徑 | 標題去 Nature 專屬；加「Word 為主、LaTeX 選用」提示；§3 改為一般期刊慣例 |
| `references/style-guardrails.md` | 保留（局部改） | 同路徑 | 拼法、圖說、標題長度改為「依期刊官網」；加 APA 7 統計符號 |
| `references/writing-strategy.md` | 保留 | 同路徑 | 英文原樣 |
| `references/section-moves.md` | 保留 | 同路徑 | 英文原樣 |
| `references/phrasebank-playbook.md` | 保留 | 同路徑 | 英文原樣 |
| `references/published-article-patterns.md` | 保留 | 同路徑 | 英文原樣；manifest 標為「只當型式參考」 |
| `references/nat-comms-2025-diction.md` | 保留（簡轉繁） | 同路徑 | 跑 `tools/s2twp.py`；第 7 節重寫為台灣用語；加「選用、只當直覺參考」提示 |
| （無） | 新增 | `references/word-layout.md` | Word 排版：字型混排、段落、表格跨頁與標題列重複、圖說、孤行、分節頁碼、目錄 F9、檢查清單 |
| （無） | 新增 | `references/ai-trace-reduction.md` | 學術英文與學術中文去 AI 腔清單；與 speak-human-tw、academic-writing 的分工 |
| （無） | 新增 | `UPSTREAM.md` | 本檔 |

## 假設

- `../bob-shared/` 由另一個子任務建立；本 skill 只引用規格第 5 節的檔名。驗收當下（2026-09-06）bob-shared 已存在且所有引用路徑都解析成功。
- 各期刊的字數、圖表、參考文獻上限一律不寫死；fragment 只說「以期刊官網為準」。
- 國防醫學院碩士論文的章節結構與格式細節以 `bob-shared/journal-formats/ndmc-thesis.md` 與所辦公告為準；本 skill 的 `ndmc-thesis.md` fragment 只列潤飾動作。
- 上游的英文 fragments 與 references 維持英文，僅去除 Nature 專屬句與失效的共用路徑。

## 驗收結果（規格第 7 節，2026-09-06）

| 項目 | 結果 | 說明 |
|---|---|---|
| 1. SKILL.md frontmatter | 通過 | `name: bob-polishing` 等於目錄名；description 含繁中觸發詞；frontmatter 無 `nature-` 字樣。正文僅出現本 skill 自己的 journal 軸值 `nature-family`（規格第 6 節允許保留、非預設） |
| 2. manifest.yaml 路徑 | 通過 | 53 個路徑（always_load、axes、references.on_demand）全部存在，含 17 個 `../bob-shared/...`；另掃描所有 .md 內的相對路徑引用，全部解析成功 |
| 3. `tools/s2twp.py --check` | 通過 | 對 skill 內全部 40 個 .md 與 .yaml 檔執行，回傳 0 |
| 4. grep 上游名稱與大陸平台 | 通過 | `nature-shared` 等上游 skill 名稱與飛書、微信、抖音、CNKI、萬方、知識星球只出現在 `UPSTREAM.md` |
| 5. README 範例提示詞 | 通過 | 四個範例分別用 DBR 迭代週期與 SUS、專科護理師學生投 JMIR Medical Education、護理雜誌審查意見去 AI 腔、碩論 Word 排版 |
| 6. 硬編碼期刊數字 | 通過 | Nature 系列 fragment 合併時刪除所有字數與圖表上限；style-guardrails 的圖說與標題長度改為「依期刊官網」；word-layout 的字級與解析度標為「示例」並註明以所方或期刊官網為準。保留的數字只有 en.md 的句長建議（寫作規則，非期刊規定）與 latex-layout 的排版量測值 |
| 附加：manifest 可解析 | 通過 | `yaml.safe_load` 成功；4 個軸、22 條 on_demand |
| 附加：SKILL.md 行數 | 通過 | 102 行（上限 250） |
| 附加：新 fragment 長度 | 通過 | qualitative 64 行、mixed-methods 64 行、dbr 63 行（要求 60–120） |
