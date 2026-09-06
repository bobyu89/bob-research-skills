# RIS 匯入 EndNote 與 Zotero、作者完整性預檢

本 skill 只產生檔案，不透過 API 或本機連線寫入任何書目軟體。

## 作者完整性預檢（匯出前必做）

匯出前確認：

1. 書目來源提供結構化、有順序的作者列表（PubMed `FAU`、Crossref `author[]`）。
2. 每位個人作者都有姓氏與名字或縮寫。
3. 後綴（Jr.、III）、姓氏助詞（van、de）、團體作者保留。
4. 每位作者一行 `AU`；不縮成 et al.。
5. Crossref 作者不完整（只有姓氏、缺 given）時，改用 PMID 從 PubMed 重抓。

不合格：

```text
AU  - Chaudhuri
AU  - Schapira
```

合格：

```text
AU  - Chaudhuri, K Ray
AU  - Schapira, Anthony H V
```

`python scripts/ris_tools.py check FILE` 會列出只有姓氏的作者與缺欄位；有問題不要說「可直接匯入」。

## EndNote 匯入 RIS

```text
File > Import > File
  Import File：選 .ris
  Import Option：Reference Manager (RIS)
  Duplicates：Import All 或 Discard Duplicates（依需要）
  Text Translation：Unicode (UTF-8)
```

nbib 檔則 Import Option 選 PubMed (NLM)。選單名稱依 EndNote 版本與作業系統略有不同；使用者告知版本時再給精確路徑。

匯入後檢查：

- 作者是否被倒置（團體作者未加尾隨逗號會變成「Association, Taiwan Nurses」）。
- DOI 欄位是否有值（EndNote 產 APA 7 時需要）。
- 期刊名是否為全名；EndNote 的 Journals Term List 可能把全名換成縮寫，需要時關閉。

## Zotero 匯入

```text
File > Import…
  選「A file (BibTeX, RIS, Zotero RDF, etc.)」
  挑 .ris 或 .bib
  勾選「Place imported collections and items into new collection」方便檢查
```

匯入後在新集合中抽查作者、DOI、卷期頁；重複項用 Zotero 的「Duplicate Items」合併。

本 skill 不產生 Zotero RDF，不使用 Zotero 本機 API 或 Web API 寫入。

## 匯入後常見狀況

| 狀況 | 原因 | 處理 |
|---|---|---|
| 中文或重音字變亂碼 | 匯入時未選 UTF-8 | 重新匯入並選 Unicode |
| 作者只剩姓氏 | 來源就不完整 | `ris_tools.py fetch --pmid` 重抓 |
| 期刊變縮寫 | EndNote 期刊詞彙表 | 關閉自動替換或匯入全名詞彙表 |
| 年份為上線年 | 來源用 `published-online` | 以 verify 的卷年為準手動改 |
| 重複條目 | 多來源合併未去重 | 匯入前 `--dedupe` |
