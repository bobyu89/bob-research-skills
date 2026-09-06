# 引用抽取規則（Citation Parser）

verify workflow 用來從各種輸入抽出引用與識別碼。`scripts/verify_dois.py` 內建 `.txt`、`.bib`、`.ris`、`.nbib` 的抽取；`.docx` 與 `.tex` 需先轉成文字。

## 依來源格式抽取

### .docx

方法：請使用者貼出參考文獻段落，或用 `docx` skill 抽出段落文字後存成 `.txt`（每筆一行）。

前處理：

- 跳過 EndNote 欄位碼段落（文字符合 `ADDIN EN\.\w+`）。
- 跳過 Zotero 欄位碼（`\{[|]?\|[^}]+\}`）。
- 去掉行內 Zotero 標記 `\{citation:\d+\}`。

識別碼正規表示式：

| 樣式 | 目標 | 例子 |
|---|---|---|
| `10\.\d{4,9}/[^\s"<>]+` | DOI | `10.1111/jan.15321` |
| `PMID:?\s*\d{6,9}` | PMID | `PMID: 35696315` |
| `PMCID:?\s*PMC\d+` | PMCID | `PMCID: PMC9540000` |

### .txt（APA 7 每筆一行）

腳本的 `parse_text_line()` 做法：

1. 去掉行首 `[n]` 或 `n.` 標籤。
2. 抽 DOI、PMID。
3. 找 `(年份)`：前面是作者段，後面第一個句號前是標題。
4. 標題後的 `期刊, 卷(期), 頁碼` 用正規表示式抽；抽不到就只保留期刊。
5. 作者段以 `, ` 與 `&` 切分；每個作者轉成 `Family, Given`。

換行折斷的 DOI：前一行無結尾標點且下一行以小寫或數字開頭時接回。

抽不到的欄位留空，不列入比對；報告中的「－」代表輸入未提供。

### .bib

| 樣式 | 目標 |
|---|---|
| `@article{key,` | 條目與鍵 |
| `doi = {…}` | DOI |
| `pmid = {…}` | PMID |
| `author = {A and B}` | 作者列表 |

`.tex` 內的 `\cite{key}`、`\citep`、`\citet`、`\textcite` 只能給鍵；要對照 `.bib` 才能解析。沒有 `.bib` 的 `.tex` 標 `manual_needed`。

### .ris、.nbib

由 `ris_tools.py` 解析：RIS 的 `DO`、`AN  - PMID:`；nbib 的 `LID`／`AID ... [doi]`、`PMID-`。

## 解析優先順序

1. DOI → Crossref `works/<DOI>`。
2. PMID → PubMed esummary，或 PubMed MCP `get_article_metadata`。
3. 標題 + 第一作者 → PubMed MCP `search_articles`、`lookup_article_by_citation`，或 Crossref `query.bibliographic`（腳本 `--search-missing`）。
4. 只有 BibTeX 鍵而無 `.bib` → `manual_needed`。

## 分類標籤

| 標籤 | 條件 | 對應總判定 |
|---|---|---|
| `verified` | 取回的書目與輸入一致（標題、期刊、年份都符） | ✅ |
| `mismatch` | 取回書目存在但欄位衝突 | ⚠️ 或 ❌，依嚴重度 |
| `not_found` | 所有資料庫都查不到 | ❓ |
| `suspicious` | 找到但書目不完整（無 DOI、標題只有部分相符） | ⚠️ |
| `manual_needed` | 無法轉成資料庫查詢（無識別碼、標題太泛） | ❓，附人工檢查建議 |
