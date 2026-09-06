# 工作流程總覽

每次啟用先做「分流」，再依 `workflow` 軸載入 `references/workflows/` 下對應的檔案。三個 workflow 可以串接（例如先 find-support 再 export），但每一段都要獨立交付。

## 0. 分流與確認

用一行話向使用者確認偵測到的參數，不要等待批准，除非缺少必要資訊：

```text
偵測：workflow=verify｜輸入=.bib 42 筆｜來源=Crossref + PubMed｜報告=繁中
```

必要資訊：

| workflow | 必要 | 可選 |
|---|---|---|
| find-support | 待引用的段落或主張 | 年份範圍、領域、文獻類型、每句候選數（預設 3） |
| verify | 參考文獻清單（文字、.bib、.ris、.docx 貼上文字） | 是否只查有 DOI 的、是否對無 DOI 的做標題檢索 |
| export | 來源檔或 DOI／PMID 清單 | 目標格式（預設 RIS）、是否去重、是否保留摘要 |

## 1. find-support（找支持文獻）

1. 切句：段落 → 可引用句，編號 `S001`、`S002`。
2. 抽主張：每句寫出一行英文主張，標主張類型（background／association／intervention／method／definition／prevalence）。
3. 檢索：PubMed MCP `search_articles`，每句 2 到 4 個查詢。
4. 評級：讀摘要（必要時 `get_full_text_article`），給 direct／partial／background／contradictory；沒讀摘要的只能標 metadata-only。
5. 匯出：用 `scripts/ris_tools.py fetch --pmid ...` 產生 RIS。
6. 報告：句子→文獻對照表 + 風險與缺口。

細節見 `references/workflows/find-support.md`。

## 2. verify（查證引用）

1. 解析輸入，抽出每筆的 DOI、PMID、第一作者、年份、標題、期刊、卷期頁。
2. 先跑 `scripts/verify_dois.py`（Crossref／PubMed 欄位比對）。
3. DOI 404 或無 DOI 的條目，用 PubMed MCP `lookup_article_by_citation` 或 `search_articles` 以標題檢索。
4. 依比對矩陣給 🔴🟡🟢，彙整成 ✅⚠️❌❓。
5. 報告：摘要計數 → 必須修正表 → 建議核對表 → 資料庫書目（給 apa7-master）。

細節見 `references/workflows/verify.md`。

## 3. export（匯出與轉檔）

1. 判斷來源格式（RIS／BibTeX／nbib／DOI 清單／PMID 清單）。
2. `scripts/ris_tools.py convert ... --to ris|bib|nbib [--dedupe]`。
3. 匯出前跑 `ris_tools.py check`，作者只有姓氏或缺 DOI 的條目要列出。
4. 告訴使用者怎麼匯入 EndNote 或 Zotero；要 APA 7 文字時交 `apa7-master`。

細節見 `references/workflows/export.md`。

## 報告格式（預設繁中）

```text
【偵測】workflow / 範圍 / 檢索日期

【結果摘要】
- 一到三行，先講結論（幾句有直接支持、幾筆要修）

【對照表 或 比對表】
（Markdown 表格）

【匯出檔】
- 絕對路徑（.ris / .bib / .nbib / .json / .md）

【風險與缺口】
- 沒讀到摘要的候選、找不到支持的句子、撤稿或更正、DOI 404、非 PubMed 來源
- 下一步建議（交 apa7-master 產格式；需要深查真實性可用 citation-verifier）
```

## 長清單策略

- verify 超過 40 筆：先整批跑 `verify_dois.py`（批次 API，不需人工），只對 ❌ 與 ❓ 逐筆人工檢視。
- find-support 超過 10 句：每 10 句一批，先給精簡對照表（句號 → 最佳候選 → 等級），只對「找不到」或「矛盾」的句子詳述。
- 在報告中說明用了哪種批次策略。
