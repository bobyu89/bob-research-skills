# 核心原則（bob-citation）

本 skill 只做三件事：**找到**（find-support）、**驗證**（verify）、**匯出**（export）。
APA 第七版的格式產生與稽核一律交給 `apa7-master`；本 skill 交付的是「可追溯的書目與證據說明」，不是格式化後的參考文獻表。

## 交付物

- 句子（或主張）→ 文獻的對照表，每一筆都附保守的支持等級與插入位置建議。
- 欄位比對表（標題、第一作者、年份、期刊、卷期、頁碼、DOI），附 🔴🟡🟢 嚴重度與 ✅⚠️❌❓ 總判定。
- 一個可匯入書目管理軟體的檔案（預設 `.ris`；也可 `.bib`、`.nbib`），交由使用者自行匯入 EndNote 或 Zotero。

## 期刊範圍（預設）

- 預設範圍是 **PubMed／MEDLINE 收錄之同儕審查期刊**。不做出版社白名單，不以影響因子篩選。
- 使用者可加條件：年份（例如「近 5 年」）、領域（護理、醫學教育、數位健康、腫瘤護理）、文獻類型（RCT、系統性回顧、質性研究、指引）。
- 台灣中文期刊（護理雜誌、護理研究、台灣專科護理師學刊、醫學教育）多數不在 PubMed；若使用者需要，改用 `WebSearch` 搜尋華藝 Airiti 或期刊官網，並在報告中標「非 PubMed 來源，欄位以官網為準」。
- Consensus（`mcp__plugin_bio-research_consensus__search`）只當發現工具；被它找到的文獻仍須回 PubMed 或 Crossref 取結構化書目。

## 來源階層

依序採信：

1. 結構化書目 API：Crossref（DOI）、PubMed E-utilities／PubMed MCP（PMID）。
2. 出版社或期刊官網頁面（Wiley、Elsevier、JMIR、SLACK、Springer 等）。
3. 摘要或全文（PubMed MCP `get_full_text_article` 可拿 PMC 開放取用全文）。
4. Google Scholar、Semantic Scholar、Consensus 只當發現工具，不能作為唯一依據。

結構化 API 與官網不一致時，保留 DOI 與官網事實，並在報告中標出差異，不要自行合併。

## 檢索品質規則

- 精確優先於數量。一句話通常 2 到 5 篇候選就夠，不是 30 篇鬆散相關的文獻。
- 用概念詞與同義詞檢索，只有專有名詞才用精確片語。MeSH 詞優先於自由詞。
- 引用次數只當同分時的參考，不代表支持力。
- Crossref 或 PubMed 若標記撤稿（retraction）、更正（erratum）或關注聲明（expression of concern），一律寫進風險段。
- 臨床、安全、劑量相關的主張要註明檢索日期，並提醒引用文獻不能取代臨床指引或系統性回顧。
- 不憑記憶捏造書目。任何欄位（卷、期、頁碼、DOI）缺失就留空，並在報告中標「待補」。

## 不做的事

- 不產生 APA 7 格式（交 `apa7-master`）。
- 不寫入 Zotero 或 EndNote 資料庫；只匯出檔案讓使用者手動匯入。
- 不做文獻搜尋排程（交 `pubmed-daily-bundle`）。
- 不設計 scoping review 的完整檢索策略（交 `scoping-review-master`）。
- 不假設 Scopus、ScienceDirect、Web of Science 等資料庫可用。

## 來源說明

本 skill 依據公開的書目 API 與匯入文件：Crossref REST API、NCBI E-utilities 與 PubMed MCP、EndNote 的 Reference Manager (RIS) 匯入選項、Zotero 的檔案匯入功能。匯入介面的選單名稱隨版本略有差異，回覆使用者時避免過度具體的 UI 描述。
