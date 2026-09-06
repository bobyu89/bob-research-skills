# Workflow：verify（查證引用）

目的：對參考文獻清單逐筆核對 DOI 能否解析、解析到的是不是同一篇、欄位是否一致，輸出 🔴🟡🟢 三級比對表與 ✅⚠️❌❓ 總判定。

工具：`scripts/verify_dois.py`（Crossref、PubMed esummary）、PubMed MCP（`lookup_article_by_citation`、`search_articles`、`convert_article_ids`）、`WebSearch`／`WebFetch`（官網與華藝）。真實性深查可搭 `citation-verifier`。

## 步驟 1：解析輸入

支援四種輸入；抽取規則見 `references/citation-parser.md`。

| 輸入 | 做法 |
|---|---|
| 整篇論文或計畫書的參考文獻段 | 每筆一行存成 `.txt`；保留 `[n]` 或 APA 7 原樣 |
| 單筆引用 | 直接寫 `--doi` 或存成一行 |
| `.bib`、`.ris`、`.nbib` | 直接餵給腳本，欄位由檔案解析 |
| Word 檔 | 請使用者貼出參考文獻段落，或用 `docx` skill 抽文字後存 `.txt` |

每筆抽出：DOI、PMID、第一作者姓氏、年份、標題、期刊、卷、期、頁碼或文章號。抽不到的欄位留空，不列入比對。

## 步驟 2：DOI 解析與欄位比對（最便宜，先做）

```bash
python scripts/verify_dois.py --input refs.txt --mailto you@example.com --json verify.json --md verify.md
python scripts/verify_dois.py --input refs.bib --search-missing
python scripts/verify_dois.py --doi 10.1111/jan.15321
```

腳本對每筆做：

1. `GET https://api.crossref.org/works/<DOI>`：404 → 🔴 DOI 錯誤；200 → 取回標題、作者、年份、期刊、卷期、頁碼。
2. 逐欄位比對（規則見 `references/field-comparison-matrix.md`）：標題相似度、第一作者、年份（含上線年 vs. 卷年）、期刊（含縮寫）、卷、期、頁碼或文章號。
3. 檢查 Crossref `update-to`（撤稿、更正）。
4. 無 DOI 但有 PMID → PubMed esummary 反查。
5. 無 DOI 也無 PMID → `--search-missing` 用 Crossref 書目查詢列候選（只當候選，不列為已驗證）。

一次 35 筆的實務經驗：最多的錯誤型態是「DOI 可解析但指向另一篇」，單靠標題比對就能抓到。

## 步驟 3：無 DOI 或 404 的條目

依序嘗試：

1. PubMed MCP `lookup_article_by_citation`（期刊、年、卷、頁、第一作者）。
2. PubMed MCP `search_articles` 以標題檢索，`max_results` 5；比對第一作者與年份。
3. `WebSearch` 標題 + 第一作者；台灣中文期刊優先查期刊官網與華藝 Airiti。
4. 都找不到 → ❓ 無法驗證，說明查過哪些來源與日期。

PMID 反查：

```bash
python scripts/verify_dois.py --pmid 35696315
```

回傳 PubMed 書目與 DOI，可用來補齊只有 PMID 的條目，或用 `convert_article_ids` 做 PMID↔DOI↔PMCID 轉換。

## 步驟 4：嚴重度與總判定

| 嚴重度 | 典型狀況 |
|---|---|
| 🔴 必須修正 | DOI 404、DOI 指向另一篇、第一作者不符或順序錯、漏作者、頁碼差 5 以上、文章號字母誤判、年份差 2 年以上、撤稿 |
| 🟡 建議核對 | 上線年 ≠ 卷年、Early Access 卷期頁漂移、卷期不符、頁碼差 4 以內、期刊名不符、作者中間名缺漏 |
| 🟢 僅供參考 | 大小寫、標點、連字號、期刊縮寫 vs. 全名 |

| 總判定 | 條件 |
|---|---|
| ✅ 已驗證 | 無 🔴🟡 |
| ⚠️ 建議核對 | 有 🟡 無 🔴 |
| ❌ 必須修正 | 有任一 🔴 |
| ❓ 無法驗證 | 所有來源都查不到（內部報告、舊學位論文、非 Crossref DOI） |

判斷年份時：APA 7 以正式卷期年份為準；只有線上先行（epub ahead of print）時用線上年，並標「advance online publication」交 apa7-master 處理。

## 步驟 5：報告

腳本已產生 Markdown；在回覆中補上繁中總結與下一步：

```text
【偵測】workflow=verify｜42 筆｜Crossref + PubMed｜查核日期 2026-09-06

【結果摘要】
- ✅ 31、⚠️ 6、❌ 4、❓ 1
- 4 筆必須修正：2 筆 DOI 指向別篇、1 筆 DOI 404、1 筆第一作者不符

【必須修正】
| # | 欄位 | 目前值 | 資料庫值 | 說明 |
| [7] | title | Clinical reasoning of nurse practitioners… | The effect of psychological interventions… | DOI 張冠李戴 |

【建議核對】
| # | 欄位 | 目前值 | 資料庫值 | 說明 |
| [18] | year | 2021 | 2022 | 上線年與卷年不一致，APA 7 以卷年為準 |

【無法驗證】
- [40] 護理雜誌中文文獻，無 Crossref DOI；已查華藝，欄位以官網為準（查核日期 2026-09-06）

【匯出檔】
- verify.md、verify.json 的絕對路徑

【下一步】
- 修正後的書目交 apa7-master 重新產生 APA 7 條目
- 需要確認文獻內容是否真的支持句子時，回到 find-support 或用 citation-verifier
```

## 批次策略

- 超過 40 筆：整批先跑腳本；人工只看 ❌ 與 ❓。
- 超過 100 筆：拆成每 40 筆一個 `.txt`，分批跑，最後合併 JSON。
- 腳本每次請求間隔 0.35 秒，並用 `--mailto` 進 Crossref polite pool；被限速（429）時等 30 秒再跑。

## 已知限制

| 限制 | 對應 |
|---|---|
| 台灣中文期刊 DOI 不在 Crossref | WebSearch 查華藝或官網，標「以官網為準」 |
| 學位論文無 DOI | 臺灣博碩士論文知識加值系統查標題、作者、年份 |
| 指引、政府報告、網頁 | 只確認來源可存取與版本日期，不比對卷期 |
| 同一篇有預印本與正式版 DOI | 以正式出版 DOI 為準 |
| 腳本抽取 APA 行的欄位可能不完整 | 缺的欄位不列入比對；人工補看資料庫書目 |
