# bob-citation

為論文段落找 PubMed 收錄的同儕審查支持文獻、逐筆查證參考文獻、把書目轉成 RIS／BibTeX／nbib。三個 workflow：**find-support**、**verify**、**export**。APA 第七版格式一律交給 `apa7-master`。

## 用途

| workflow | 做什麼 | 產出 |
|---|---|---|
| find-support | 把段落切成可引用句，用 PubMed MCP 找候選，讀摘要後保守評級（直接支持／部分支持／背景支持／相反） | 句子→文獻對照表、RIS 檔、風險與缺口 |
| verify | DOI 解析（Crossref）與 PMID 反查（PubMed），逐欄位比對標題、第一作者、年份、期刊、卷期、頁碼 | 🔴🟡🟢 比對表、✅⚠️❌❓ 總判定、JSON 與 Markdown |
| export | RIS、BibTeX、nbib 互轉，DOI／PMID／標題去重，作者完整性檢查 | 可匯入 EndNote 或 Zotero 的檔案與匯入說明 |

期刊範圍預設為 PubMed／MEDLINE 收錄之同儕審查期刊，可加「近 5 年」「護理／醫學教育／數位健康」等條件；不做出版社白名單。台灣中文期刊文獻改用 WebSearch 查華藝或官網，並標查核日期。

## 觸發語

找支持文獻、幫這段配文獻、補引用、這句有沒有文獻、查證引用、核對參考文獻、參考文獻驗證、DOI 檢查、這些引用是真的嗎、匯出 RIS、轉 BibTeX、EndNote 匯入、Zotero 匯入、nbib 轉檔、書目去重、PMID 反查。

## 範例提示詞

1. 「這是我碩論第二章談專科護理師臨床推理與 Tanner 模型的一段，幫這段配文獻，限近 5 年、護理與醫學教育期刊，每句 3 篇，最後給我 RIS 讓我匯進 EndNote。」
2. 「計畫書口試委員說參考文獻有幾筆 DOI 怪怪的，這是全部 42 筆（APA 7），幫我核對參考文獻，列出必須修正的，並把正確書目整理好讓 apa7-master 重排。」
3. 「我從 PubMed 匯了三個 nbib、Zotero 匯了一個 RIS，全部合併去重轉成一個 RIS，順便檢查有沒有作者只有姓氏的，投護理雜誌前要用。」

## 腳本

```bash
python skills/bob-citation/scripts/verify_dois.py --input refs.txt --mailto you@example.com --md verify.md --json verify.json
python skills/bob-citation/scripts/verify_dois.py --doi 10.1111/jan.15321
python skills/bob-citation/scripts/verify_dois.py --pmid 35696315
python skills/bob-citation/scripts/ris_tools.py convert a.nbib b.ris c.bib --to ris --dedupe -o merged.ris
python skills/bob-citation/scripts/ris_tools.py check merged.ris
python skills/bob-citation/scripts/ris_tools.py fetch --pmid 35696315 --to ris -o jan.ris
```

只用 Python 標準函式庫；完整參數見 `references/script-usage.md`。

## 與既有 skill 的分工

| 既有 skill | 負責 | bob-citation 的關係 |
|---|---|---|
| `apa7-master` | APA 7 參考文獻與內文引用格式 | 本 skill 只找到、驗證、匯出；格式產生與稽核全交它 |
| `citation-verifier` | 引文真實性深查 | verify 的 DOI 解析與欄位比對表是前置；需要逐篇確認內容時交它 |
| `pubmed-daily-bundle` | 文獻搜尋排程 | 本 skill 不做排程 |
| `scoping-review-master` | Scoping review 檢索策略、PCC、PRISMA-ScR | 本 skill 只為個別句子找支持文獻 |
| `academic-writing` | 整合文獻成段落、章節、.docx | 找到的文獻交它整合；論證架構交 `bob-writing` |
| `paper-analysis` | 單篇論文閱讀整理 | 不重疊 |
| `docx` | Word 抽文字與輸出 | 參考文獻段落抽文字時用 |

## 目錄

```text
bob-citation/
  SKILL.md                 router（繁中）
  manifest.yaml            workflow 軸、always_load、on_demand
  README.md / UPSTREAM.md
  static/core/             principles、zh-tw-mode、workflow
  references/workflows/    find-support、verify、export
  references/              search-strategy、field-comparison-matrix、common-patterns、
                           citation-parser、dedup-engine、ris-bibtex-format、
                           ris-endnote-zotero、script-usage
  scripts/                 verify_dois.py、ris_tools.py
  tests/                   test_ris_tools.py、samples/
```

## 邊界

- 不寫入 Zotero 或 EndNote 資料庫，只匯出檔案讓使用者手動匯入。
- 不假設 Scopus、ScienceDirect、Web of Science 可用。
- 沒讀摘要的候選不當支持；不捏造書目欄位。
- 具體期刊規定一律標「以期刊官網為準，查核日期」。
