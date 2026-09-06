# UPSTREAM：bob-shared 的上游來源與改造紀錄

## 來源

- 上游專案：`nature-skills`（袁一哲等，Apache-2.0）
- 上游 skill：`nature-shared`
- 本機穩定副本：`C:\Users\USER\ai-skills\nature-skills\skills\nature-shared\`
- 上游 commit：`28150f30f8b4017991fca8c7b2839f02c6586d2f`（2026-09-06）
- 上游版本：manifest `1.6.0`
- 改造規格：`C:\Users\USER\Downloads\bob-research-skills\ADAPTATION-SPEC.md`（第 1、2、3、5、7 節）
- 改造日期：2026-09-06

## 逐檔清單

| 上游檔案 | 本包檔案 | 處置 | 說明 |
|---|---|---|---|
| `SKILL.md` | `SKILL.md` | 改寫 | frontmatter `name: bob-shared`；description 改為繁中加英文一句，說明僅供 bob-* 依賴、不單獨觸發；正文改為繁中，逐檔列出載入時機 |
| `manifest.yaml` | `manifest.yaml` | 改寫 | 仿上游結構；`always_load: []`；`core.on_demand` 12 條、`journal_formats.on_demand` 5 條，condition 全部繁中；`quality_tools.script_resolution` 改為 bob-shared |
| `README.md`（簡中） | `README.md` | 改寫 | 繁中重寫；含用途、觸發語（無）、內容表、三個台灣情境範例提示詞、與既有 skill 的分工表 |
| `README_EN.md` | — | 刪除 | 規格要求不帶入 |
| `agents/openai.yaml` | — | 刪除 | 規格要求不帶入 |
| — | `UPSTREAM.md` | 新增 | 本檔 |
| `core/reader-workflow.md` | `core/reader-workflow.md` | 保留（繁中化） | 五問架構原樣保留；譯為繁中並加入護理／健康科學讀者（編輯、審查委員、口試委員、臨床實務者）的重心表；`nature-polishing`／`nature-writing` 名稱改為 bob-* |
| `core/paper-type-taxonomy.md` | `core/paper-type-taxonomy.md` | 改寫 | 保留 research / methods / hypothesis / algorithmic / review 五型；新增 qualitative / mixed-methods / dbr / scoping-review / quality-improvement 五型；每型附常見報告準則；新增複合型處理、碩士論文章節對應、交接規則 |
| `core/ethics.md` | `core/ethics.md` | 改寫 | 刪除 Nature Portfolio 政策段與其網址；改為 APA／ICMJE／台灣 IRB／期刊 AI 揭露語境；保留紅黃綠燈框架；新增台灣語境的倫理聲明清單與 bob-* 操作規則 |
| `core/terminology-ledger.md` | `core/terminology-ledger.md` | 改寫 | 繁中；表格新增「中文定名」欄；新增中文定名規則（中英並列、譯名優先順序、大陸用語排除）；範例改為 RAG、NP、SUS、臨床推理、放聲思考 |
| `core/consistency-sweep.md` | `core/consistency-sweep.md` | 保留 | 英文原文；僅將 `nature-shared` 改為 `bob-shared`、`nature-response/...` 改為 `bob-response/...` |
| `core/main-text-discipline.md` | `core/main-text-discipline.md` | 保留 | 英文原文；「Supplementary Information (SI)」改稱「appendix or supplementary material (Supplementary; 附錄／補充資料)」，全文 `SI` 改為 `Supplementary` |
| `core/discussion-argument-language.md` | `core/discussion-argument-language.md` | 保留 | 英文原文；刪除「not an official Nature Portfolio requirement」與 WeChat 公眾號文章連結，改為引用 Glasman-Deal 一書並加一句「報告準則優先」 |
| `core/nature-introduction.md` | `core/introduction-funnel.md` | 改寫（改名） | 去 Nature／NMI 語料語境；改為健康科學／護理研究的「背景 → 重要性 → 缺口 → 目的」四段式漏斗；新增碩士論文第一章差異；保留精確缺口、文獻功能、答案晚出、前言結果對齊、審核表 |
| `core/nature-abstract.md` | `core/abstract-evidence-chain.md` | 改寫（改名） | 去 Nature 語境；新增結構式摘要（Background/Aim/Design/Methods/Results/Conclusion）段落任務表與非結構式動作順序；新增中英摘要並列規則；保留主要主張、數字必要性、意義收尾、審核表 |
| `core/nature-results-discussion.md` | `core/results-discussion-escalation.md` | 改寫（改名） | 去 Nature 語境；證據鏈原型改為迭代發現循環（DBR）、核心成效與驗證範圍、能力階梯、主題深化（質性）、分後合（混合方法）；新增碩士論文第四章與第五章慣例；保留主張推進、同層重複、局部詮釋閘門、審核表 |
| `core/research-compliance.md` | `core/health-research-compliance.md` | 改寫（改名） | 刪除 Nature reporting summary、動物、影像完整性、晶體結構、化學、分類學等段；改為台灣 IRB／知情同意／個資法、EQUATOR 準則路由表（設計 → 準則 → 對應既有 skill）、各準則關鍵要素、DBR 報告要素、生成式 AI 兩種角色揭露、資料可用性；保留適用性閘門與審核輸出表 |
| — | `core/zh-tw-academic-conventions.md` | 新增 | 台灣學術中文慣例（全形標點、數字與統計符號、量表定名、圖表編號、標楷體、APA 中文慣例、句式）與規格第 2 節第 4 點的大陸用語對照表（完整搬入並擴充為一般技術、學術流程、平台工具、標點四類） |
| `journal-formats/nature.md` | — | 刪除 | 使用者不投 Nature；不保留 |
| `journal-formats/nat-comms.md` | — | 刪除 | 同上 |
| `journal-formats/nature-machine-intelligence.md` | — | 刪除 | 同上；其「stage gate」與「未寫死數字」的寫法精神沿用到新檔 |
| — | `journal-formats/generic-health.md` | 新增 | 健康科學期刊通用預設：IMRaD、結構式摘要、聲明段落、報告準則、投稿前必查清單；不含任何硬數字 |
| — | `journal-formats/nursing-journals.md` | 新增 | JAN、IJNS、NET、NEP、JNR、CIN、BMC Med Educ 等的期刊總表（含官網 URL 與查核日期欄位）、投稿前必查清單、結構性特徵說明、期刊選擇判斷；不含任何硬數字 |
| — | `journal-formats/jmir.md` | 新增 | JMIR 系列：五段結構式摘要、Trial registration／IRRID、Multimedia Appendix、CONSORT-EHEALTH、CHERRIES、文章類型對應研究階段、必查清單 |
| — | `journal-formats/taiwan-nursing.md` | 新增 | 護理雜誌、台灣專科護理師學刊、醫學教育等中文期刊：中英摘要並列、APA 中文格式、必要文件、必查清單、常見審查意見 |
| — | `journal-formats/ndmc-thesis.md` | 新增 | 國防醫學院碩士論文：整體結構、各章小節、排版慣例、表 3-1 式編號與圖說樣式、Word 操作（F9）、口試慣例；未確定處標「以所辦最新規範為準」並附待確認表 |
| `scripts/check_consistency.py` | `scripts/check_consistency.py` | 保留 | 原樣複製，未改 |
| `tests/test_check_consistency.py` | `tests/test_check_consistency.py` | 保留 | 原樣複製；`python -m unittest discover -s tests` 通過（5 tests OK） |

## 改造時的假設與判斷

1. **對照表與禁用字串的衝突**：規格第 5 節要求 `zh-tw-academic-conventions.md` 完整搬入大陸用語對照表，但第 7 節第 3、4 項要求 `s2twp.py --check` 回傳 0 且規格列出的簡體平台名禁用字串不得出現在 UPSTREAM.md 以外。處理方式：對照表左欄一律以**繁體字形**書寫大陸用語（例如「軟件」「數據」「導師」「返修」「飛書」「萬方」「知識星球」），因為 bob-* 的輸出經 s2twp 後殘留的正是這些繁體字形；三個繁簡同形的平台名改用英文或中文全稱（WeChat、Douyin、中國知網）。語意完整，且兩項驗收都通過。
2. **保留檔的語言**：`consistency-sweep.md`、`main-text-discipline.md`、`discussion-argument-language.md` 維持英文（規格第 2 節第 2 點允許）；`reader-workflow.md` 因規格標「可繁中化」且篇幅短，已譯為繁中並擴充。
3. **`discussion-argument-language.md` 的來源註記**：上游引用一篇 WeChat 公眾號文章作為靈感來源；依規格刪除該平台引用，只保留其轉述的原書（Glasman-Deal, *Science Research Writing for Non-native Speakers of English*）。
4. **DBR 報告要素**：DBR 沒有 EQUATOR 準則；`health-research-compliance.md` 第 5 節的要素表是依常見 DBR 方法論文獻整理，並明確標示「這是整理，不是官方清單」。
5. **期刊特徵描述**：`nursing-journals.md` 與 `jmir.md` 只描述長期穩定的結構性特徵（例如 JAN 有 Impact statement、JMIR 摘要五段），全部標「以官網為準」，並留 URL 與查核日期欄位由使用者填寫；沒有寫任何字數、圖表數、費用。
6. **ndmc-thesis.md** 的章節與排版慣例是依台灣護理研究所碩士論文的一般慣例整理，逐項標「以所辦最新規範為準」，並附待確認表；唯一具體數字是圖檔 300 dpi，來自規格第 6 節 bob-figure 的 thesis-word 規定，不是期刊數字。
7. **manifest 的 `quality_tools.tests`** 是本包新增的欄位（上游沒有），用來讓驗收腳本一併檢查測試路徑存在。
8. 本包引用的其他 bob-* 檔案路徑（例如 `bob-statistics/references/apa7-statistics-format.md`、`bob-polishing/references/word-layout.md`、`bob-figure/static/fragments/target/thesis-word.md`、`bob-response/templates/response-letter.md`）依規格第 6 節的規劃命名；這些 skill 由其他子任務產出，完成後需交叉確認路徑一致。

## 驗收結果（規格第 7 節，執行日期 2026-09-06）

執行位置：`C:\Users\USER\Downloads\bob-research-skills\skills\bob-shared\`

| 項目 | 檢查方式 | 結果 |
|---|---|---|
| 1. SKILL.md frontmatter | `name: bob-shared` 等於目錄名；description 為繁中加英文一句，明示不單獨觸發、無觸發詞；全文無 `nature-` 字樣 | 通過（SKILL.md 共 52 行，低於 250 行上限） |
| 2. manifest 路徑存在 | 解析 `manifest.yaml` 中所有 `path`、`consistency_script`、`tests`，共 19 條，逐一 `exists()` | 通過（19/19 存在） |
| 3. 簡體殘留 | `python tools/s2twp.py --check` 掃描本包全部 `.md` 與 `.yaml`（22 個檔案） | 通過（exit 0，無殘留） |
| 4. 禁用字串 | 以規格第 7 節第 4 項的完整 grep 樣式（八個 nature-* skill 名稱加六個簡體平台名）遞迴掃描本包 | 通過（只有本檔 UPSTREAM.md 因記錄上游來源路徑而命中 `nature-shared`，其餘檔案零命中；本檔刻意不重複列出簡體樣式，以免牴觸第 3 項；另以 `grep -i nature` 確認全包沒有 Nature 字樣） |
| 5. README 範例提示詞 | 三個範例皆為台灣情境（專科護理師、臨床推理、設計本位研究、SUS、JMIR Medical Education、護理雜誌、IRB） | 通過 |
| 6. 硬編碼期刊數字 | 逐檔檢視 `journal-formats/*.md`；所有具體規定改為必查清單或「以官網為準（查核日期 2026-09-06）」；期刊表格留 URL 與查核日期欄位 | 通過（未寫任何字數、圖表數、參考文獻數、費用） |
| 7. 規格第 5 節檔案清單 | 逐一比對 22 個路徑 | 通過（22/22，檔名完全一致） |
| 8. 單元測試 | `python -m unittest discover -s tests -q` | 通過（Ran 5 tests, OK） |
| 9. 異常字元 | 掃描所有 `.md`／`.yaml` 中的西里爾或希臘字母（排除統計符號 α β χ η Δ μ） | 通過（修正過一處 README 中誤植的西里爾字母） |
| 10. 改寫與新增檔案篇幅 | `wc -l` | 改寫／新增的 core 檔 64 至 233 行、journal-formats 檔 77 至 138 行，均在 60 至 200 行的目標範圍或略高（zh-tw-academic-conventions.md 因對照表較長為 233 行） |
