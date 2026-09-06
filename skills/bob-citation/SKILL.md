---
name: bob-citation
description: >-
  為論文段落找 PubMed 收錄的同儕審查支持文獻、逐筆查證參考文獻的 DOI 與欄位、
  把書目轉成 RIS／BibTeX／nbib 供 EndNote 或 Zotero 手動匯入。三個 workflow：
  find-support（切句→找文獻→保守評級→對照表）、verify（Crossref／PubMed 欄位比對→
  🔴🟡🟢→報告）、export（轉檔、去重、完整性檢查）。APA 7 格式一律交 apa7-master。
  Find PubMed-indexed peer-reviewed support for manuscript claims, verify reference
  lists against Crossref and PubMed, and export RIS/BibTeX/nbib for reference managers.
  觸發詞：找支持文獻、幫這段配文獻、補引用、這句有沒有文獻、找引用、配文獻、
  查證引用、核對參考文獻、參考文獻驗證、DOI 檢查、這些引用是真的嗎、參考文獻有沒有錯、
  匯出 RIS、轉 BibTeX、EndNote 匯入、Zotero 匯入、nbib 轉檔、書目去重、PMID 反查。
metadata:
  author: 游明勳（Bob），改造自上游 skill 集（來源見 UPSTREAM.md）
---

# bob-citation：找到、驗證、匯出

本 skill 分兩層：

- **靜態層** `static/core/`：原則與範圍、台灣繁中作業模式、三段工作流程總覽。每次都載入。
- **動態層**（本檔 + `manifest.yaml`）：依 `workflow` 軸載入 `references/workflows/` 的流程檔，深度參考只在需要時開。

不要憑記憶或只憑本檔執行。每次啟用都照下面四步走。

## 分流步驟

### 1. 載入 manifest 與核心層

讀 [manifest.yaml](manifest.yaml)，然後讀 `always_load` 的三個檔：

- `static/core/principles.md`：交付物、期刊範圍（PubMed／MEDLINE 同儕審查期刊，不做出版社白名單）、來源階層、檢索品質規則、不做的事。
- `static/core/zh-tw-mode.md`：使用者以繁中提問、檢索用英文、報告用繁中；支持等級與嚴重度的中文用語。
- `static/core/workflow.md`：三段流程總覽、報告格式、長清單策略。

### 2. 決定 workflow 與執行期參數

`workflow` 軸可多選：

| 使用者說 | workflow |
|---|---|
| 找支持文獻、幫這段配文獻、補引用、這句有沒有文獻 | `find-support` |
| 查證引用、核對參考文獻、DOI 檢查、參考文獻驗證、這些引用是真的嗎 | `verify` |
| 匯出 RIS、轉 BibTeX、EndNote、Zotero 匯入、nbib、合併去重 | `export` |

執行期參數不是內容軸，用一行話向使用者確認即可：年份範圍（預設不限，常見「近 5 年」）、領域（護理、醫學教育、數位健康）、文獻類型、每句候選數（預設 3）、輸出格式（預設 RIS）、是否去重、是否保留摘要。

```text
偵測：workflow=find-support + export｜範圍=PubMed 同儕審查期刊，2021–2026，護理與醫學教育｜每句 3 篇｜輸出 RIS｜報告繁中
```

這是進度回報，不是批准關卡；除非缺少必要輸入（段落、清單、檔案），否則直接往下做。

### 3. 載入對應流程檔並執行

- `find-support` → `references/workflows/find-support.md`：切句編號 → 每句列英文主張 → PubMed MCP `mcp__plugin_bio-research_pubmed__search_articles` 找候選 → 讀摘要後給 direct／partial／background／contradictory → `scripts/ris_tools.py fetch --pmid` 產 RIS → 句子→文獻對照表。
- `verify` → `references/workflows/verify.md`：解析清單 → `scripts/verify_dois.py` 查 Crossref 與 PubMed → 無 DOI 用 `lookup_article_by_citation` 或標題檢索 → 🔴🟡🟢 → ✅⚠️❌❓ 報告；`--pmid` 可反查。
- `export` → `references/workflows/export.md`：`scripts/ris_tools.py convert --to ris|bib|nbib [--dedupe]` → `check` → 匯入說明 → 交 apa7-master。

硬性規則：

- 沒讀摘要的候選只能標 metadata-only，不可當支持。標題相關不等於支持。
- 不捏造任何書目欄位；缺就留空並標「待補」。
- 撤稿、更正、關注聲明一律寫進風險段。
- 匯出前跑 `ris_tools.py check`；作者只有姓氏或缺年份就不能說「可直接匯入」。
- 台灣中文期刊文獻多半不在 Crossref 與 PubMed；用 WebSearch 查華藝或官網，標「以官網為準，查核日期 YYYY-MM-DD」。
- 具體期刊規定（作者數上限、格式）一律標「以期刊官網為準，查核日期」或標為示例。

### 4. 只在需要時開深度參考

依 manifest 的 `references.on_demand`：

| 需要 | 開 |
|---|---|
| 把中文主張變成英文檢索式、支持等級、常見誤引 | `references/search-strategy.md` |
| 逐欄位比對規則、嚴重度矩陣、護理案例 | `references/field-comparison-matrix.md` |
| 錯誤根本原因（上線年 vs. 卷年、Early Access、作者名、文章號、撤稿） | `references/common-patterns.md` |
| 從 .docx／.txt／.bib／.tex 抽引用 | `references/citation-parser.md` |
| 去重鍵與合併偏好 | `references/dedup-engine.md` |
| RIS／BibTeX／nbib 欄位對應 | `references/ris-bibtex-format.md` |
| EndNote／Zotero 匯入、作者完整性預檢 | `references/ris-endnote-zotero.md` |
| 腳本完整參數與實測輸出 | `references/script-usage.md` |
| 引用倫理與 AI 揭露 | `../bob-shared/core/ethics.md` |

## 可用工具

- PubMed MCP：`mcp__plugin_bio-research_pubmed__search_articles`、`get_article_metadata`、`get_full_text_article`、`find_related_articles`、`convert_article_ids`、`lookup_article_by_citation`。
- Consensus：`mcp__plugin_bio-research_consensus__search`，只當發現工具。
- `WebSearch`、`WebFetch`：官網、華藝 Airiti、Crossref API。
- 本地腳本：`scripts/verify_dois.py`、`scripts/ris_tools.py`（純標準函式庫）。
- 不假設 Scopus、ScienceDirect、Web of Science 可用；不寫入 Zotero 或 EndNote 資料庫。

## 分工邊界

| 情境 | 交給 |
|---|---|
| 產生或稽核 APA 7 參考文獻與內文引用格式（中英文） | `apa7-master`。本 skill 只交付驗證過的書目與 RIS／BibTeX |
| 引文真實性深查（逐篇確認內容是否真的支持句子、疑似捏造） | `citation-verifier`；本 skill 的 verify 提供 DOI 解析與欄位比對表作為前置 |
| 文獻搜尋排程、每日推送 | `pubmed-daily-bundle` |
| Scoping review 的完整檢索策略、PCC、PRISMA-ScR 流程圖 | `scoping-review-master`；本 skill 只為個別句子找支持文獻 |
| 把找到的文獻整合成段落、寫章節、輸出 .docx | `academic-writing`；論證架構與證據鏈交 `bob-writing` |
| 單篇論文閱讀整理 | `paper-analysis` |
| Word 抽文字或輸出 | `docx` |

## 輸出

一律繁中報告，格式見 `static/core/workflow.md`：偵測行 → 結果摘要 → 對照表或比對表 → 匯出檔絕對路徑 → 風險與缺口與下一步。文獻的標題、作者、期刊名維持原文。

## 為什麼這樣切

- 三個 workflow 是線性流程，差異在步驟不在文體，所以只有一個內容軸。
- 腳本把可自動化的部分（DOI 解析、欄位比對、轉檔、去重）從對話中抽走，對話只處理需要判斷的部分（支持等級、無識別碼的文獻、台灣中文期刊）。
- 本檔刻意短；要加範圍時改 fragments 與 references，不改本檔。
