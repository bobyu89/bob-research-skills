# `bob-shared/`：bob-* 科研 skill 集的共享參考包

這個目錄是一個可安裝、但**不應單獨觸發**的支援包。它保存多個 `bob-*` skill 共同依賴的定義與參考資料，避免在不同 skill 目錄中重複維護同一套內容。整套 skill 安裝時，它會與其他 skill 一起被發現與更新。

同級 skill 透過 `manifest.yaml` 中的相對路徑引用這裡的檔案，例如：

```yaml
always_load:
  - ../bob-shared/core/terminology-ledger.md
```

## 用途

- 提供護理與健康科學研究、國防醫學院 NP 組碩士論文語境下的寫作、審稿、統計、引文與排版共同守則。
- 語言為台灣繁體中文；上游保留的英文參考維持英文。
- 引用格式一律 APA 第七版；期刊規定不寫死數字，改為投稿前必查清單並要求記錄查核日期。

## 觸發語

無。本包沒有任何觸發詞，使用者不會直接呼叫它；只在其他 bob-* skill 指名時載入單一檔案。

## 目前內容

| 檔案 | 使用方 | 性質 |
|---|---|---|
| `core/reader-workflow.md` | bob-writing、bob-polishing、bob-reviewer | 讀者五問與各類讀者的重心 |
| `core/paper-type-taxonomy.md` | bob-writing、bob-polishing、bob-reviewer | 十種論文類型（含 qualitative、mixed-methods、dbr、scoping-review、quality-improvement）與判別規則 |
| `core/ethics.md` | 全部 | 引用歸屬、台灣 IRB 語境的倫理聲明、AI 使用紅黃綠燈、不得捏造守則 |
| `core/terminology-ledger.md` | bob-writing、bob-polishing、bob-reviewer、bob-figure | 含「中文定名」欄的術語帳 |
| `core/consistency-sweep.md` | bob-polishing、bob-reviewer、bob-response、bob-statistics | 多輪修訂後的漂移偵測（英文） |
| `core/main-text-discipline.md` | bob-writing、bob-polishing、bob-response | 主文精簡、結果分類、附錄／補充資料分配（英文） |
| `core/discussion-argument-language.md` | bob-writing、bob-polishing | 討論的功能鏈與語氣校準（英文） |
| `core/introduction-funnel.md` | bob-writing、bob-polishing、bob-reviewer | 前言的背景、重要性、缺口、目的漏斗；碩士論文第一章慣例 |
| `core/abstract-evidence-chain.md` | bob-writing、bob-polishing、bob-reviewer | 結構式與非結構式摘要、中英摘要並列 |
| `core/results-discussion-escalation.md` | bob-writing、bob-polishing、bob-reviewer | 結果的主張推進與討論的綜合；DBR、質性、混合方法的證據鏈原型 |
| `core/health-research-compliance.md` | bob-writing、bob-reviewer、bob-statistics、bob-response | IRB、個資、EQUATOR 準則路由表、DBR 報告要素、AI 揭露 |
| `core/zh-tw-academic-conventions.md` | 全部 | 台灣學術中文慣例與大陸用語對照表 |
| `journal-formats/generic-health.md` | bob-writing、bob-polishing、bob-reviewer | 健康科學期刊通用預設 |
| `journal-formats/nursing-journals.md` | bob-writing、bob-polishing | JAN、IJNS、NET、NEP、JNR、CIN 等的投稿前必查清單 |
| `journal-formats/jmir.md` | bob-writing、bob-polishing | JMIR 系列慣例 |
| `journal-formats/taiwan-nursing.md` | bob-writing、bob-polishing | 台灣中文護理期刊慣例 |
| `journal-formats/ndmc-thesis.md` | bob-writing、bob-polishing、bob-figure、bob-statistics | 國防醫學院碩士論文格式慣例 |
| `scripts/check_consistency.py` | bob-polishing、bob-reviewer、bob-response | 術語變體、數值精度、單位混用的機械初篩 |
| `tests/test_check_consistency.py` | 維護者 | 上述腳本的單元測試 |

`scripts/check_consistency.py` 只輸出待人工核對的風險提示，不會自動改稿。執行方式：

```bash
python skills/bob-shared/scripts/check_consistency.py manuscript.docx.txt tables.txt \
  --term-group '臨床推理=臨床推理|臨床推論|臨床思考' \
  --term-group 'SUS=System Usability Scale|系統可用性量表|系統易用性量表'
```

## 範例提示詞（透過其他 bob-* skill 間接使用）

1. 「用 bob-writing 幫我寫碩士論文第一章的研究背景，研究是專科護理師的臨床推理 AI 學習系統，設計本位研究。」→ bob-writing 會載入 `core/introduction-funnel.md`、`core/paper-type-taxonomy.md`（dbr）、`journal-formats/ndmc-thesis.md`、`core/zh-tw-academic-conventions.md`。
2. 「用 bob-reviewer 審這篇要投 JMIR Medical Education 的稿，裡面有 SUS 分數和訪談。」→ bob-reviewer 會載入 `core/health-research-compliance.md`（CHERRIES、COREQ 路由）、`journal-formats/jmir.md`、`core/results-discussion-escalation.md`。
3. 「用 bob-polishing 把這段中文討論潤到可以投護理雜誌，IRB 那句也幫我看。」→ bob-polishing 會載入 `core/zh-tw-academic-conventions.md`、`core/discussion-argument-language.md`、`journal-formats/taiwan-nursing.md`、`core/ethics.md`。

## 與既有 skill 的分工表

| 既有 skill | 負責 | bob-shared 的關係 |
|---|---|---|
| `academic-writing` | 整章撰寫、APA 內文引用、輸出 .docx | bob-shared 提供論證與格式守則；整章 .docx 交給它 |
| `apa7-master` | APA 7 參考文獻格式 | bob-shared 只在 `zh-tw-academic-conventions.md` 列中文慣例供一致性檢查；格式產生一律交給它 |
| `citation-verifier` | 引文真實性 | `ethics.md` 規定不得捏造引文；驗證交給它或 bob-citation |
| `equator-guideline-finder` 與各準則 master | 報告準則檢核 | `health-research-compliance.md` 的路由表指向它們 |
| `concept-analysis-master`、`scoping-review-master`、`prisma-2020-master` | 各自的方法學與全文 | `paper-type-taxonomy.md` 判型後直接轉交 |
| `mixed-methods-research` | 混合方法設計 | 本包只管寫法，設計問題轉交 |
| `speak-human-tw` | 口語化 | 本包的中文慣例是學術文體，不重疊 |
| `docx`、`pptx`、`xlsx`、`pdf` | 檔案輸出 | 本包不產檔 |
| `np-case-report`、`twna-ebhc-report`、`nursing-project-reviewer` | 護理專用報告 | `taiwan-nursing.md` 遇到對應文章類型時轉交 |

## 什麼時候把檔案放到這裡

只有當**兩個或更多** bob-* skill 需要複用同一份內容時，才把檔案放進 `bob-shared/`。只服務一個 skill 的內容，留在該 skill 自己的 `static/` 或 `references/`。

## 什麼時候保持 skill 內的局部內容

共享層只放**定義與參考資料**（論文類型、讀者工作流、倫理守則、術語帳、期刊慣例）。各 skill 如何診斷、起草、修改或輸出，仍留在各自的 `static/fragments/`。

## 與其他 skill 的關係

`bob-shared/` 不是獨立工作流，而是被其他 bob-* skill 按需讀取的公共依賴包。上游來源與逐檔變更見 `UPSTREAM.md`。
