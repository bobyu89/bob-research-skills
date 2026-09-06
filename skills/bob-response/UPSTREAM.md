# UPSTREAM

## 來源

- 上游專案：`nature-skills`（袁一哲等，Apache-2.0）
- 上游 skill：`skills/nature-response/`
- 本機穩定副本：`C:\Users\USER\ai-skills\nature-skills\skills\nature-response\`
- commit：`28150f30f8b4017991fca8c7b2839f02c6586d2f`（2026-09-06）
- 改造規格：`ADAPTATION-SPEC.md` 第 4、5、6（bob-response）、7 節
- 改造日期：2026-09-06

## 改造摘要

保留上游完整 workflow：解析退修信、主要／次要修訂決定關卡、`E.x`／`R1.x` 編號、互盲隱私過濾、行動分類、追蹤表、accretion 控制（主文精簡）、QA、整包一致性稽核與 `scripts/check_package_consistency.py`。核心層改寫為台灣繁體中文；語境改為護理、醫學教育、數位健康期刊與台灣中文期刊；預設交付格式改為 Markdown／Word，LaTeX 保留為選用；新增「口試委員意見回覆」模式。`../nature-shared/` 一律改為 `../bob-shared/`，且只引用 bob-shared 目前實際存在的檔案（`core/main-text-discipline.md`、`core/consistency-sweep.md`）；`health-research-compliance.md` 只以「完成後可用」的方式提及，不放進 manifest。

## 逐檔清單

| 檔案 | 處置 | 說明 |
|---|---|---|
| `SKILL.md` | 改寫 | 繁中 router；`name: bob-response`；description 含繁中觸發詞；新增分工邊界段與 `committee-response` 模式；99 行 |
| `manifest.yaml` | 改寫 | 版本 1.0.0；`nature-shared` → `bob-shared`；新增 taiwan-journal-norms、thesis-committee-response、三個 Markdown 範本的 on_demand 條目 |
| `README.md` | 改寫 | 繁中；用途、觸發語、3 個台灣情境範例、分工表、邊界、檔案結構 |
| `README_EN.md` | 刪除 | 規格第 3 節 |
| `agents/openai.yaml` | 刪除 | 規格第 3 節 |
| `static/core/stance.md` | 改寫 | 繁中；來源優先順序改為期刊須知／ICMJE／COPE／出版社建議；新增中文全形標點規則與口試模式說明 |
| `static/core/workflow.md` | 改寫 | 繁中；決定關卡問句改繁中；新增「口試委員意見回覆模式」段；流程 20 步保留並加入 Word／Markdown 範本路由；輸出格式繁中化 |
| `references/chinese-author-alignment.md` | 改寫 | 繁中台灣語境；新增「台灣作者常見的回覆問題」表（過度道歉、全盤接受、回覆與修改不一致、把「已在文中說明」當回覆等）；範例改為 SUS 樣本數、質性飽和、RAG 幻覺 |
| `references/taiwan-journal-norms.md` | 新增 | 護理雜誌、護理研究等中文期刊的修訂說明表、修改處標示、一稿一表慣例；不確定處標「以期刊官網為準（查核日期 2026-09-06）」 |
| `references/thesis-committee-response.md` | 新增 | 口試委員意見回覆模式：與期刊退修的差異、編號、流程、常見委員意見類型、輸出格式、語氣範例；格式以所辦最新規範為準 |
| `references/source-basis.md` | 改寫 | 刪除 Nature 專屬來源；改為 ICMJE、COPE、Springer Nature 公開建議、目標護理期刊與台灣中文期刊；每項標查核日期 |
| `references/intake-and-routing.md` | 修改 | 繁中決定關卡問句；接受「修改後再審／修改後刊登」用語；新增 `committee-response` 模式列與路由捷徑；去 Nature-style 字樣 |
| `references/comment-taxonomy.md` | 修改 | 移除 `nature-data` 交接，改指 bob-shared 合規檔（完成後） |
| `references/difficult-cases.md` | 修改 | `nature-response` → `bob-response`；做不到的實驗範例改為多場域、對照組（DBR 語境） |
| `references/package-consistency-audit.md` | 修改 | `nature-shared` → `../bob-shared`；加註腳本僅支援 LaTeX，Word 包改人工核對 |
| `references/response-structure.md` | 修改 | 新增 Markdown／Word 交付段；LaTeX 標為選用；新增 `committee-response` 模式；Word 修改稿標示規則 |
| `references/latex-templates.md` | 修改 | 標題與開頭標為選用 |
| `references/action-mapping.md` | 保留 | 英文原文 |
| `references/tone-and-stance.md` | 保留 | 英文原文 |
| `references/qa-checklist.md` | 保留 | 英文原文 |
| `templates/response-letter.md` | 新增 | Markdown／Word 逐點回覆表：Reviewer／Comment／Response／Location of change／Status；英文與繁中兩版；護理期刊示例（SUS 樣本數、質性飽和、AI 幻覺、補文獻） |
| `templates/revision-cover-letter.md` | 新增 | 修訂版 cover letter 英文與繁中兩版 |
| `templates/committee-response-table.md` | 新增 | 口試委員意見回覆表範本（委員／意見／修改內容／頁碼） |
| `templates/cover-letter.tex` | 保留（選用） | 英文原文 |
| `templates/response-to-reviewers.tex` | 保留（選用） | 英文原文 |
| `templates/revised-manuscript-redline.tex` | 保留（選用） | 英文原文 |
| `scripts/check_package_consistency.py` | 保留 | 未改動 |
| `examples/conflicting-reviewers.md` | 保留 | 英文合成範例 |
| `examples/major-revision-with-missing-evidence.md` | 保留 | 英文合成範例 |
| `examples/minor-revision.md` | 保留 | 英文合成範例 |
| `examples/thesis-committee-response.md` | 新增 | 口試模式合成範例（繁中） |
| `tests/test_package_consistency.py` | 保留 | 未改動 |
| `tests/test_response_instruction_contracts.py` | 改寫 | 斷言改為繁中核心層字串；新增口試模式路由、manifest 路徑存在、上游名稱殘留三項測試 |
| `tests/committee-response.md` | 新增 | 口試模式行為契約 |
| `tests/unclear-decision-type.md` | 修改 | 簡體改繁中；問句改為主要／次要修訂 |
| `tests/major-revision-missing-evidence.md` | 修改 | 去 Nature style 字樣 |
| `tests/rubric.md` | 修改 | `nature-response` → `bob-response`；Nature-fit → Journal-fit |
| `tests/evaluation-summary.md` | 修改 | 名稱更新；促進條件加入繁中與口試模式 |
| `tests/conflicting-reviewers.md`、`defensive-draft-audit.md`、`impossible-experiment.md`、`minor-revision.md`、`reviewer-visibility.md`、`task-status-tracking.md` | 保留 | 英文原文 |

## 假設

1. bob-shared 於改造當下（2026-09-06）只有 `core/reader-workflow.md`、`core/consistency-sweep.md`、`core/discussion-argument-language.md`、`core/main-text-discipline.md`、`scripts/check_consistency.py` 與 `tests/test_check_consistency.py`，尚無 SKILL.md、manifest 與規格第 5 節其餘檔案；manifest 只引用其中實際存在的 `main-text-discipline.md` 與 `consistency-sweep.md`。規格第 5 節其他檔案（`health-research-compliance.md`、`journal-formats/*`）完成後可補進 on_demand。
2. 台灣中文期刊的回覆表格式、修改處標示方式與繳交規定未逐一查核官網；`taiwan-journal-norms.md` 只寫慣例與查核方向，並統一標「以期刊官網為準（查核日期 2026-09-06）」。
3. 口試委員意見回覆表的欄位（委員／意見／修改內容／頁碼）與簽核流程依使用者敘述與一般做法設計，所辦實際格式以所辦最新規範為準。
4. 英文 references（action-mapping、tone-and-stance、qa-checklist、comment-taxonomy、difficult-cases、intake-and-routing、response-structure、package-consistency-audit、latex-templates）依規格第 2 節第 2 點維持英文，只做去 Nature 與去上游名稱的修改。
5. `scripts/check_package_consistency.py` 只支援 LaTeX；Word 修訂包的一致性核對改為人工步驟，寫在 `package-consistency-audit.md` 開頭。

## 規格第 7 節驗收結果（2026-09-06）

| # | 檢查項目 | 結果 |
|---|---|---|
| 1 | `SKILL.md` frontmatter `name: bob-response` 等於目錄名；description 含繁中觸發詞；檔內無 `nature-` 字樣；正文 99 行（≤250） | 通過 |
| 2 | `manifest.yaml` 21 個路徑全部存在（含 `../bob-shared/core/main-text-discipline.md`、`../bob-shared/core/consistency-sweep.md`） | 通過 |
| 3 | `python tools/s2twp.py --check` 掃描全部 `.md`、`.yaml`（需 `PYTHONIOENCODING=utf-8`，否則 Windows 主控台 cp950 會讓工具本身在列印時崩潰） | 回傳 0，通過 |
| 4 | grep 規格第 7 節第 4 項的禁用字串清單 | 只出現在 `UPSTREAM.md`，通過 |
| 5 | README 三個範例提示詞用台灣情境（Nurse Education Today 退修＋SUS 樣本數＋RAG 幻覺；護理雜誌修改後再審＋紅字稿；計畫書口試委員意見回覆表＋IRB 提醒） | 通過 |
| 6 | 未新增任何硬編碼期刊數字；`taiwan-journal-norms.md` 與 `source-basis.md` 中涉及期刊規定處皆標「以期刊官網為準（查核日期 2026-09-06）」 | 通過 |

附加測試：

- `python -m unittest tests.test_package_consistency`：7 tests OK（腳本未改動）。
- `tests/test_response_instruction_contracts.py` 七項契約測試全部通過（決定關卡、互盲隔離、漏看視為清晰度問題、標點守則、口試模式路由、manifest 路徑存在、上游名稱殘留）。環境未安裝 pytest，以自訂 runner 逐一呼叫執行。
- `scripts/check_package_consistency.py --help` 可執行。
