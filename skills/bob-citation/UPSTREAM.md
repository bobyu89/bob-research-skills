# UPSTREAM：bob-citation 的上游來源與改造紀錄

- 上游專案：`nature-skills`（袁一哲等，Apache-2.0）
- 上游穩定副本：`C:\Users\USER\ai-skills\nature-skills`
- commit：`28150f30f8b4017991fca8c7b2839f02c6586d2f`（2026-09-06）
- 改造規格：`C:\Users\USER\Downloads\bob-research-skills\ADAPTATION-SPEC.md` 第 6 節「bob-citation」
- 改造日期：2026-09-06

bob-citation 合併三個上游 skill：

| 上游 | 路徑 | 取用範圍 |
|---|---|---|
| `nature-citation` | `skills/nature-citation/` | 全部（router、核心層、references、腳本概念） |
| `nature-ref-verifier` | `skills/nature-ref-verifier/` | 全部（欄位比對矩陣、嚴重度分級、常見錯誤型態） |
| `nature-academic-search` | `skills/nature-academic-search/` | 只取 `references/workflows/wf2-citation-verification.md`、`references/citation-parser.md`、`references/dedup-engine.md`、`references/ris-bibtex-format.md`、`scripts/converters.py`、`scripts/format-converter.py` |

## 逐檔清單

### 來自 nature-citation

| 上游檔案 | 處置 | 目標檔案 | 說明 |
|---|---|---|---|
| `SKILL.md` | 改寫 | `SKILL.md` | 繁中 router；`name: bob-citation`；觸發詞改繁中；加 workflow 軸與分工邊界段；刪除 CNS／Nature 系列範圍 |
| `manifest.yaml` | 改寫 | `manifest.yaml` | 新增 `workflow` 軸（find-support／verify／export）；on_demand 重列；引用 `../bob-shared/core/ethics.md` |
| `README.md` | 改寫 | `README.md` | 繁中；三個台灣情境範例；分工表 |
| `README_EN.md` | 刪除 | — | 規格第 3 節不需要 |
| `agents/openai.yaml` | 刪除 | — | 規格第 3 節不需要 |
| `evals/evals.json` | 刪除 | — | 內容綁 CNS 範圍與舊腳本旗標 |
| `static/core/principles.md` | 改寫 | `static/core/principles.md` | 繁中；期刊範圍改 PubMed／MEDLINE 同儕審查期刊；刪 CNS 白名單；來源階層改 Crossref／PubMed／官網；加「不做的事」 |
| `static/core/workflow.md` | 改寫 | `static/core/workflow.md` | 繁中；由七步單一流程改為三段 workflow 總覽 + 報告格式 + 長清單策略 |
| `static/core/chinese-mode.md` | 改寫 | `static/core/zh-tw-mode.md` | 台灣繁中模式：使用者繁中提問、檢索英文、報告繁中；用語規範；支持等級與嚴重度中文標籤 |
| `references/search-strategy.md` | 改寫 | `references/search-strategy.md` | 繁中；範例改護理與醫學教育的 PubMed 查詢；刪 CNS 相關失誤 |
| `references/journal-scope.md` | 刪除 | — | CNS／Nature Portfolio 白名單，規格明訂不做 |
| `references/ris-endnote.md` | 改寫 | `references/ris-endnote-zotero.md` | 繁中；保留 RIS 對應、作者完整性預檢、EndNote 匯入；刪 Zotero RDF；Zotero 只留手動匯入 |
| `references/script-usage.md` | 改寫 | `references/script-usage.md` | 改為兩支新腳本的參數表與實測結果；刪 `--scope`、`--with-artifacts`、HTML 瀏覽器 |
| `scripts/nature_citation.py` | 刪除（概念保留） | `scripts/ris_tools.py`、`scripts/verify_dois.py` | 2,356 行的 Crossref 檢索 + HTML 產生器整支刪除；保留的概念：作者完整性關卡（`check`）、DOI 正規化、PubMed 取全名作者（`fetch --pmid`）、`--mailto` polite pool |
| `tests/test_author_exports.py` | 刪除（概念保留） | `tests/test_ris_tools.py` | 重寫為新腳本的離線測試（作者正規化、只有姓氏偵測、往返轉檔、去重、欄位比對） |

### 來自 nature-ref-verifier

| 上游檔案 | 處置 | 目標檔案 | 說明 |
|---|---|---|---|
| `SKILL.md` | 改寫（拆分） | `references/workflows/verify.md`、`references/field-comparison-matrix.md` | Step 1–5 流程 → verify workflow；Step 3 的 🔴🟡🟢 矩陣與 Step 4 置信度 → 比對矩陣；案例由 IEEE／遙測改為護理文獻（JAN、NET、JMIR）；刪 IEEE Xplore、CNKI／萬方、kimi-datasource、kimi-webbridge、zotero-mcp、pyzotero 寫入、Zotero sqlite；多來源流程圖簡化為 Crossref／PubMed／WebSearch 或華藝 |
| `manifest.yaml` | 併入 | `manifest.yaml` | on_demand 條件併入 |
| `README.md` | 併入 | `README.md` | 用途與邊界併入 |
| `README_EN.md` | 刪除 | — | |
| `agents/openai.yaml` | 刪除 | — | |
| `references/common-patterns.md` | 改寫 | `references/common-patterns.md` | 繁中；保留卷年 vs. 上線年、作者名、頁碼、DOI、撤稿各節；新增華人姓名姓與名倒置、台灣中文期刊華藝 DOI、文章號、指引與網頁；刪 IEEE／IET 更名、會議論文、中文 `[D]`／`[Z]` 標記、CNKI／萬方 |

### 來自 nature-academic-search

| 上游檔案 | 處置 | 目標檔案 | 說明 |
|---|---|---|---|
| `references/workflows/wf2-citation-verification.md` | 併入 | `references/workflows/verify.md` | 抽取 → 解析 → 比對 → 分類 → 報告的骨架；解析工具改 Crossref／PubMed MCP；刪 arXiv、Semantic Scholar |
| `references/citation-parser.md` | 改寫 | `references/citation-parser.md` | 繁中；.docx 改為「貼文字或 docx skill 抽文字」；新增 `.txt` APA 7 行解析規則（對應 `verify_dois.py parse_text_line`）；刪 arXiv |
| `references/dedup-engine.md` | 改寫 | `references/dedup-engine.md` | 繁中；新增 PMID 次鍵；合併偏好對應 `ris_tools.py completeness()`；加「不該合併的情況」 |
| `references/ris-bibtex-format.md` | 改寫 | `references/ris-bibtex-format.md` | 繁中；範例改 JAN 文獻；刪 ENW 節（改在格式選擇表提及 RIS 可代替）；新增 nbib best-effort 輸出規格與 `FAU`→`AU` 推導；MEDLINE 對應表加 `FAU`、`CN`、`OT` |
| `scripts/converters.py` | 改寫 | `scripts/ris_tools.py` | 保留 `parse_medline_fields`、`ris_escape`（改名 `clean_text`）、LID／AID 掃全部值取 DOI、MEDLINE→RIS／BibTeX 對應；刪 arXiv 與 ENW 轉換；新增 RIS 與 BibTeX 解析器、統一紀錄模型、nbib 輸出、去重、`check`、CLI 子命令 |
| `scripts/format-converter.py` | 改寫（部分） | `scripts/ris_tools.py fetch` | 保留 efetch MEDLINE 與 Crossref works 取得；刪 arXiv、`--interactive`、`--query`、preflight、自我測試 |
| `references/pubmed-28344011.{bib,nbib,ris}` | 替換 | `tests/samples/pubmed-35696315.{nbib,ris}` | 樣本改為護理文獻（Lyu et al., 2022, JAN；PMID 35696315；DOI 10.1111/jan.15321），由 E-utilities 實際取得 |

### 新增（無上游對應）

| 目標檔案 | 說明 |
|---|---|
| `references/workflows/find-support.md` | 切句 → 主張 → PubMed MCP 檢索 → 讀摘要評級 → RIS → 對照表 |
| `references/workflows/export.md` | 轉檔、去重、完整性檢查、EndNote／Zotero 手動匯入、交接 apa7-master |
| `scripts/verify_dois.py` | 純標準函式庫；.bib／.ris／.nbib／.txt 輸入；Crossref 欄位比對；`--pmid` esummary 反查；`--mailto`；`--search-missing`；JSON 與 Markdown 輸出 |
| `tests/samples/refs-apa7.txt` | 5 筆 APA 7（1 筆正確、1 筆年份與頁碼漂移、1 筆 DOI 張冠李戴、1 筆 DOI 404、1 筆無 DOI） |
| `tests/samples/dedupe-mix.bib` | 去重與作者完整性測試樣本 |
| `tests/test_ris_tools.py` | 離線單元測試，可直接 `python` 執行或用 pytest |

## 依賴的共享層

- `../bob-shared/core/ethics.md`（規格第 5 節清單內；manifest on_demand）。其餘 bob-shared 片段本 skill 不引用。

## 假設與待確認

1. 台灣中文期刊的 DOI 前綴（華藝）在文件中標為示例，未查證每一本期刊的實際註冊機構。
2. EndNote 與 Zotero 匯入選單名稱依版本略有差異，文件中已標「以使用者版本為準」。
3. `verify_dois.py` 對 APA 7 文字行的欄位抽取為啟發式；抽不到的欄位不列入比對，不會誤判為錯誤。
4. `ris_tools.py` 的 nbib 輸出為 best-effort，不含 NLM 內部欄位（`STAT`、`MH`、`AD`）。
5. 上游 `citation-verifier` 與 `apa7-master` 為使用者環境既有 skill，本 skill 只做交接，未驗證其介面。

## 驗收結果（規格第 7 節，2026-09-06）

| # | 項目 | 結果 |
|---|---|---|
| 1 | `SKILL.md` frontmatter `name: bob-citation` 等於目錄名；description 含繁中觸發詞；無 `nature-` 字樣 | 通過 |
| 2 | `manifest.yaml` 每一個路徑真實存在（含 `../bob-shared/core/ethics.md`） | 通過（17 個路徑全部存在） |
| 3 | `python tools/s2twp.py --check` 掃 skill 內所有 .md .yaml | 通過（回傳 0，無簡體殘留） |
| 4 | 規格第 7 節第 4 項的 grep（上游 skill 名稱、中國大陸平台名稱、CNKI 等）只出現在 UPSTREAM.md | 通過（其他檔案零命中；Scopus／ScienceDirect 僅以「不假設可用」形式出現，符合規格第 4 節用語） |
| 5 | README 三個範例提示詞用台灣情境 | 通過（碩論第二章專科護理師臨床推理、計畫書口試委員意見、投護理雜誌前合併 RIS） |
| 6 | 無未標註查核日期的硬編碼期刊數字 | 通過（APA 7 的 20 位作者規則為格式規則非期刊規定；JMIR 文章號、NET 文章號皆標「示例」） |

腳本實測（2026-09-06，網路可用）：

- `verify_dois.py --doi 10.1111/jan.15321`：Crossref 回傳 Lyu, Meng‐Meng 等 4 位作者，Journal of Advanced Nursing，78(10)，3069-3082，issued 2022-06-13，print 2022-10 → ✅。
- `verify_dois.py --input tests/samples/refs-apa7.txt --search-missing`：✅ 1、⚠️ 1（年份 2021→2022 🟡、頁碼 3069-3080→3069-3082 🟡、期刊縮寫 🟢）、❌ 2（標題相似度 0.44 + 第一作者 Wang→Lyu 🔴；DOI 404 🔴）、❓ 1（無 DOI，Crossref 書目查詢候選 10.3928/01484834-20060601-04 相似度 1.0，Tanner 2006）。回傳碼 1。
- `verify_dois.py --pmid 35696315`：反查得 DOI 10.1111/jan.15321 與完整書目。
- `ris_tools.py convert dedupe-mix.bib pubmed-35696315.nbib --to ris --dedupe`：6 → 3 筆（同 DOI 大小寫不同 ×2、同標題無 DOI ×1 合併）。
- `ris_tools.py check dedupe-mix.bib`：抓出 `Chaudhuri`、`Schapira` 只有姓氏，回傳碼 1。
- `tests/test_ris_tools.py`：7 個測試全部 PASS。
