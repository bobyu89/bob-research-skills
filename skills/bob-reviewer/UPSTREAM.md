# UPSTREAM

## 來源

- 上游專案：`nature-skills`（袁一哲等，Apache-2.0）
- 上游 skill：`skills/nature-reviewer/`
- 本機副本：`C:\Users\USER\ai-skills\nature-skills\skills\nature-reviewer\`
- commit：`28150f30f8b4017991fca8c7b2839f02c6586d2f`（2026-09-06）
- 改造依據：`ADAPTATION-SPEC.md` 第 6 節「bob-reviewer」，以及第 4、5、7 節

## 逐檔清單

| 上游檔案 | 處置 | 目標檔案 | 說明 |
|---|---|---|---|
| `SKILL.md` | 改寫 | `SKILL.md` | 繁中 router；name 改 `bob-reviewer`；評審軸改為五個健康科學軸；新增準則判定步驟、中文核對區塊、分工邊界段；去 Nature 專屬句；`../nature-shared/` 改 `../bob-shared/` |
| `manifest.yaml` | 改寫 | `manifest.yaml` | 移除 `editorial criteria and processes.md`；always_load 改為 source-basis 與 review-axes；新增 `study_design` 與 `language` 軸；on_demand 改指 `health-research-review-gates.md`、`../bob-shared/core/consistency-sweep.md`、`../bob-shared/core/health-research-compliance.md` |
| `README.md` | 改寫 | `README.md` | 繁中；用途、觸發語、3 個台灣情境範例、分工表 |
| `README_EN.md` | 刪除 | （無） | 規格第 3 節 |
| `agents/openai.yaml` | 刪除 | （無） | 規格第 3 節 |
| `references/editorial criteria and processes.md` | 刪除 | （無） | Nature 原文不保留 |
| `references/source-basis.md` | 改寫 | `references/source-basis.md` | 改引 ICMJE、COPE、EQUATOR 與典型護理期刊審稿表的公開原則；保留「本地實作選擇」段 |
| `references/review-axes.md` | 改寫 | `references/review-axes.md` | 五軸改為 originality、clinical-educational-significance、methodological-rigour、ethics-reporting-transparency、interdisciplinary-clarity；側重配置對應更新 |
| `references/domain-specific-review-gates.md` | 改寫並改名 | `references/health-research-review-gates.md` | 繁中；七類健康研究設計的檢查閘（量性、質性、混合方法、系統性與範疇性回顧、教育介入與 DBR、AI／LLM 應用、問卷與量表發展） |
| `references/reviewer-workflow.md` | 保留（局部改寫） | `references/reviewer-workflow.md` | 英文；五軸名稱更新；新增準則判定、設計別閘門載入、中文核對產生步驟；ledger 範例改為護理教育情境 |
| `references/report-structure.md` | 保留（局部改寫） | `references/report-structure.md` | 英文；輸出契約新增 `Study design and applicable reporting guideline` 與 `中文核對` 區塊；去 Nature-style 字樣 |
| `references/role-boundaries.md` | 保留（局部改寫） | `references/role-boundaries.md` | 英文；側重模式與安全措辭範例改為五軸；新增 COPE 的不指控原則 |
| `references/qa-checklist.md` | 保留（局部改寫） | `references/qa-checklist.md` | 英文；落地來源改為 source-basis 的公開原則；新增中文核對、準則命名、期刊數字、分工檢查 |
| `references/technical-concern-taxonomy.md` | 保留（局部改寫） | `references/technical-concern-taxonomy.md` | 英文；新增 12 軸到五軸的對應表；`ethical-governance` 與 `clinical-validity` 說明擴到 IRB、個資、AI 揭露與教育效用 |
| `tests/punctuation-style.md` | 保留 | `tests/punctuation-style.md` | 未改 |
| `tests/reviewer-independence.md` | 保留 | `tests/reviewer-independence.md` | 未改 |
| `tests/severity-tiering.md` | 保留 | `tests/severity-tiering.md` | 未改 |
| `tests/traceable-review.md` | 保留 | `tests/traceable-review.md` | 未改 |
| `tests/test_reviewer_instruction_contracts.py` | 改寫 | `tests/test_reviewer_instruction_contracts.py` | 斷言改對應繁中 router；新增 name、五軸、中文核對、manifest 路徑存在性測試 |
| （無） | 新增 | `UPSTREAM.md` | 本檔 |

## 驗收結果（規格第 7 節）

驗收日期：2026-09-06

| # | 項目 | 結果 | 說明 |
|---|---|---|---|
| 1 | `SKILL.md` frontmatter：`name` 等於目錄名；description 含繁中觸發詞；無 `nature-` 字樣 | 通過 | `name: bob-reviewer`；觸發詞含「模擬審稿、三位審稿人、投稿前自審、審稿意見模擬、幫我審這篇、口試前模擬提問」；`grep -c "nature-" SKILL.md` 為 0；正文 211 行（≤250） |
| 2 | `manifest.yaml` 每個路徑真實存在（含 `../bob-shared/...`） | 通過 | 10 個路徑全部存在，含 `../bob-shared/core/consistency-sweep.md` 與 `../bob-shared/core/health-research-compliance.md`（後者由 bob-shared 子任務產出，驗收時已存在） |
| 3 | `python tools/s2twp.py --check` 對 skill 內所有 `.md` `.yaml` 回傳 0 | 通過 | exit 0，無殘留簡體字 |
| 4 | 規格第 7 節第 4 項的 grep（上游 `nature-*` skill 名稱與中國大陸平台名稱）只出現在 `UPSTREAM.md` | 通過 | UPSTREAM.md 以外零命中；另以 `grep -rn "Nature"` 複查，UPSTREAM.md 以外零命中。本檔為通過第 3 項檢查，不逐字複述該 grep 模式 |
| 5 | README.md 三個範例提示詞用台灣情境 | 通過 | 範例含 DBR／RAG 臨床推理學習系統／SUS／放聲思考／口試委員、Nurse Education Today／專科護理師／TREND、失樂感監測平台／護理研究 |
| 6 | 不新增未標註查核日期的硬編碼期刊數字 | 通過 | 全 skill 無任何期刊字數、圖表或參考文獻上限；SKILL.md 紅線與 report-structure.md 明定提到期刊規定時標「以期刊官網為準」 |
| 附 | `tests/test_reviewer_instruction_contracts.py` | 通過 | 7 個測試全部通過（環境無 pytest，以獨立 runner 逐一執行） |
| 附 | `health-research-review-gates.md` 每類 40–80 行 | 通過 | 量性 44、質性 40、混合方法 42、系統性與範疇性回顧 44、教育介入與 DBR 48、AI／LLM 42、問卷與量表 43 |

## 假設與待確認

- 審稿人報告與綜合段維持英文（模擬真實投稿情境），只有 `中文核對` 區塊用繁中；若使用者投台灣中文期刊或口試前模擬時想要全繁中報告，可在提示詞中指定，SKILL.md 的「除非使用者另有指定」條款已允許。
- `references/reviewer-workflow.md`、`report-structure.md`、`role-boundaries.md`、`qa-checklist.md`、`technical-concern-taxonomy.md` 保留英文（規格允許），只做局部改寫；未整篇翻譯。
- `tests/*.md` 四個行為 fixture 未改，因其內容（診斷模型跨院推廣、治療 X 與結果 Y）與健康科學情境相容且不含 Nature 專屬句。
- `references/health-research-review-gates.md` 只列審稿人最常追問的檢查點，不重製各準則的完整項目；完整清單交由 `equator-guideline-finder` 與各 `*-master` skill。
- 量表信效度的數值門檻（CVI、因素負荷、適配指標）刻意不寫死，要求審稿人引用稿件所引的心理計量文獻，避免捏造截斷值。
