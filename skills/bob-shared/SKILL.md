---
name: bob-shared
description: bob-* 科研 skill 集的共享參考包（僅供 bob-writing、bob-polishing、bob-reviewer、bob-response、bob-citation、bob-statistics、bob-figure、bob-research-log 依賴）。Internal shared-reference package for the bob-* research skills; never invoke it as a standalone workflow. 不會由使用者的任何觸發詞直接啟動；只在其他 bob-* skill 的 manifest 指名時，載入指定的單一檔案。
---

# bob-shared 共享參考

此包只作為其他 bob-* skill 的依賴使用。使用者不會直接呼叫它；沒有觸發詞。

## 使用規則

- 只載入被指名的那一個檔案，不預載整包。
- `core/` 與 `journal-formats/` 是共享定義與參考資料，不是獨立工作流。
- 讀完後回到請求的 skill，由它負責任務邏輯、輸出格式與最終品質檢查。
- 任何檔案都不得捏造期刊數字、IRB 編號、引文或統計值；遇到不確定的事實，輸出 `AUTHOR_INPUT_NEEDED` 或「以官網為準（查核日期）」。
- 所有 journal-formats 檔案都不含硬編碼的字數或圖表上限；它們提供「投稿前必查清單」與可填寫的官網 URL 欄位。

## core/ 各檔案的載入時機

| 檔案 | 何時載入 |
|---|---|
| `core/reader-workflow.md` | 起草或潤飾任何章節前，需要用「讀者五問」（相關、新穎、可信、可用、邊界）決定段落順序時 |
| `core/paper-type-taxonomy.md` | 套用 `paper_type` 軸之前，要判定稿件屬於 research、methods、hypothesis、algorithmic、review、qualitative、mixed-methods、dbr、scoping-review、quality-improvement 哪一型時 |
| `core/ethics.md` | 涉及引用歸屬、研究倫理聲明、生成式 AI 使用的紅黃綠燈判斷、或不得捏造的守則時 |
| `core/terminology-ledger.md` | 開始任何寫作、潤飾、審稿或製圖前，需要建立中英對照一致的術語帳時 |
| `core/consistency-sweep.md` | 審核已存在或多輪修訂過的稿件，找術語、單位、數字精度、主張與表格矛盾等累積漂移時；搭配 `scripts/check_consistency.py` |
| `core/main-text-discipline.md` | 起草、重組、壓縮或依審查意見修改主文（尤其結果）；把結果分類到主文、圖說、附錄／補充資料時 |
| `core/discussion-argument-language.md` | 起草或潤飾討論段；校準「顯示、支持、可能」等語氣強度；把限制寫成主張邊界時 |
| `core/introduction-funnel.md` | 起草或潤飾前言或碩士論文第一章；建立「背景 → 重要性 → 缺口 → 目的」的問題漏斗時 |
| `core/abstract-evidence-chain.md` | 起草或潤飾結構式或非結構式摘要、中英摘要並列時 |
| `core/results-discussion-escalation.md` | 起草或潤飾結果與討論、碩士論文第四章與第五章；依研究設計（DBR、介入、質性、混合方法）選證據鏈原型時 |
| `core/health-research-compliance.md` | 稿件涉及 IRB、知情同意、個資、報告準則（CONSORT、STROBE、COREQ、PRISMA-ScR、CHERRIES、TRIPOD+AI 等）、DBR 報告要素、AI 揭露、資料可用性時；含 EQUATOR 準則到既有 skill 的路由表 |
| `core/zh-tw-academic-conventions.md` | 產出或潤飾任何中文學術文本（全形標點、數字與統計符號、量表定名、圖表編號、標楷體、APA 中文慣例、大陸用語對照表）時 |

## journal-formats/ 各檔案的載入時機

| 檔案 | 何時載入 |
|---|---|
| `journal-formats/generic-health.md` | `journal=generic-health` 或目標期刊未指定；需要 IMRaD、結構式摘要、聲明段落、報告準則清單的通用預設時 |
| `journal-formats/nursing-journals.md` | `journal=nursing`；投 JAN、IJNS、NET、NEP、JNR、CIN、BMC Med Educ 等英文護理或醫學教育期刊時 |
| `journal-formats/jmir.md` | `journal=jmir`；投 JMIR 系列（五段結構式摘要、Trial registration、Multimedia Appendix、CONSORT-EHEALTH、CHERRIES）時 |
| `journal-formats/taiwan-nursing.md` | `journal=taiwan-nursing`；投護理雜誌、台灣專科護理師學刊、醫學教育等中文期刊（中英摘要並列、APA 中文格式）時 |
| `journal-formats/ndmc-thesis.md` | `journal=ndmc-thesis` 或 `task=thesis-chapter`；撰寫或排版國防醫學院碩士論文第一章至第五章時 |

## 工具

- `scripts/check_consistency.py`：術語變體、同值不同精度、等值長度單位混用的機械初篩。路徑相對於 bob-shared 目錄解析，不相對於使用者的工作目錄。
- `tests/test_check_consistency.py`：`python -m unittest discover -s skills/bob-shared/tests`。

## 分工邊界

bob-shared 不執行任何任務。與使用者既有 skill 的交接（`academic-writing`、`apa7-master`、`citation-verifier`、`equator-guideline-finder`、`scoping-review-master`、`concept-analysis-master` 等）由各 bob-* skill 的 SKILL.md 說明；本包只在 `core/` 檔案中標示「此處轉交 X」。
