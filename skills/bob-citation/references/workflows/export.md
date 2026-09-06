# Workflow：export（匯出與轉檔）

目的：把來源書目轉成使用者需要的匯入檔（RIS 預設；BibTeX、nbib 可選），去重、檢查完整性，並說明如何手動匯入 EndNote 或 Zotero。APA 7 文字格式不在此產生，交 `apa7-master`。

工具：`scripts/ris_tools.py`。不寫入任何書目軟體的資料庫。

## 步驟 1：判斷來源

| 使用者給的 | 處理 |
|---|---|
| `.ris`、`.bib`、`.nbib` 檔 | 直接轉檔 |
| PMID 清單 | `fetch --pmid` 由 PubMed 取 MEDLINE 後轉 |
| DOI 清單 | `fetch --doi` 由 Crossref 取後轉；沒 PMID 的會缺 MeSH |
| find-support 的結果 | 用選定的 PMID 走 `fetch` |
| verify 後修正的清單 | 以資料庫回傳的 DOI／PMID 重新 `fetch`，不要沿用有錯的欄位 |

格式偵測靠副檔名，或內容開頭（`TY  - `、`PMID- `、`@article{`）。

## 步驟 2：轉檔與去重

```bash
# RIS → BibTeX
python scripts/ris_tools.py convert refs.ris --to bib -o refs.bib

# 多檔合併、去重、輸出 RIS（不含摘要，檔案較小）
python scripts/ris_tools.py convert pubmed-a.nbib zotero.ris refs.bib --to ris --dedupe --no-abstract -o merged.ris

# 只去重，格式同第一個輸入
python scripts/ris_tools.py dedupe merged.ris -o merged.dedup.ris

# 由 PMID／DOI 取得
python scripts/ris_tools.py fetch --pmid 35696315,30000000 --to ris -o new.ris --ncbi-email you@example.com
python scripts/ris_tools.py fetch --doi 10.1111/jan.15321 --to bib --mailto you@example.com
```

去重鍵（見 `references/dedup-engine.md`）：DOI 正規化 → PMID → 標題正規化 + 第一作者姓氏（Jaccard ≥ 0.90）。合併時保留欄位較完整的一筆，缺的欄位由另一筆補。

## 步驟 3：完整性檢查（匯出前必跑）

```bash
python scripts/ris_tools.py check merged.ris
```

列出：

- 作者只有姓氏（例如 `AU  - Chaudhuri`）：EndNote 匯入後會變成不完整作者，必須用 `fetch --pmid` 重抓。
- 缺 DOI、缺年份、缺卷號、缺頁碼或文章號。

有 🔴 級缺漏（作者不完整、缺年份）就不要說「可直接匯入」；先補再交付。

## 步驟 4：格式對應（摘要）

| 內部欄位 | RIS | BibTeX | nbib |
|---|---|---|---|
| 作者（Family, Given） | `AU` | `author = {A and B}` | `FAU` + `AU`（姓 縮寫） |
| 標題 | `TI` | `title = {{...}}` | `TI` |
| 期刊全名／縮寫 | `JO`、`T2`／`JA` | `journal` | `JT`／`TA` |
| 年份 | `PY` | `year` | `DP` |
| 卷／期 | `VL`／`IS` | `volume`／`number` | `VI`／`IP` |
| 頁碼 | `SP`／`EP` | `pages = {a--b}` | `PG` |
| DOI | `DO` + `UR` | `doi` + `url` | `LID ... [doi]`、`AID` |
| PMID | `AN  - PMID:` | `pmid` | `PMID-` |
| 關鍵字 | `KW` | `keywords` | `OT`（MeSH 原為 `MH`） |
| 摘要 | `N2` | `abstract` | `AB` |

完整規格見 `references/ris-bibtex-format.md`。nbib 由非 PubMed 來源產生時是 best-effort，缺 `MH`、`STAT` 等 NLM 欄位。

## 步驟 5：告訴使用者怎麼匯入

EndNote（桌面版）：

```text
File > Import > File，選 .ris，Import Option 選 Reference Manager (RIS)，Text Translation 選 Unicode (UTF-8)。
```

Zotero：

```text
File > Import…，選「A file (BibTeX, RIS, Zotero RDF, etc.)」，挑 .ris 或 .bib；匯入後在新建的集合中檢查作者與 DOI。
```

選單名稱依版本略有差異；使用者提供版本時再給精確路徑。本 skill 不透過 API 寫入 Zotero 或 EndNote 資料庫。

## 步驟 6：交接 apa7-master

使用者要 APA 7 參考文獻表時：

1. 先用本 workflow 產生乾淨的 RIS 或 BibTeX（去重、check 通過）。
2. 把檔案或資料庫回傳書目（verify 報告末段）交給 `apa7-master`，說明語言（中文或英文文獻）與用途（碩論、護理雜誌、JAN 投稿）。
3. 回收 apa7-master 的輸出後，不再改動欄位內容；若發現欄位錯誤，回到 verify。

## 報告

```text
【偵測】workflow=export｜來源=refs.bib 42 筆 + pubmed.nbib 6 筆｜目標=RIS

【結果摘要】
- 合併 48 筆，去重後 41 筆（7 筆重複：5 筆同 DOI、2 筆同標題）
- check：2 筆作者只有姓氏（已用 PMID 重抓）、1 筆缺 DOI（[33] 護理雜誌中文文獻，保留）

【匯出檔】
- C:\...\merged.ris（41 筆）

【匯入方式】
- EndNote：File > Import > File，Import Option = Reference Manager (RIS)
- Zotero：File > Import…

【下一步】
- 要 APA 7 參考文獻表：交 apa7-master
```

## 常見問題

- BibTeX 的 `author` 用「Family, Given and Family, Given」；自然序（Given Family）會被轉成 Family, Given，但雙姓（西班牙語、葡萄牙語）可能拆錯，匯出後抽查。
- RIS 的 `PY` 只保留年份；需要月份時看 nbib 的 `DP`。
- 摘要含 HTML 標籤（`<sup>`）會被清掉。
- 檔案一律 UTF-8 無 BOM、LF 換行；EndNote 匯入時選 Unicode。
