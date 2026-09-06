# Workflow：find-support（找支持文獻）

目的：把使用者的段落切成可引用的句子，為每一句找到 PubMed 收錄的同儕審查文獻，保守評級後輸出「句子→文獻」對照表與 RIS 檔。

工具：PubMed MCP（`mcp__plugin_bio-research_pubmed__search_articles`、`get_article_metadata`、`get_full_text_article`、`find_related_articles`）、`scripts/ris_tools.py fetch`。Consensus 只當發現工具。

## 步驟 1：切句與編號

- 以空白行為段落界線；段落超過約 300 字或含多個主張時再切成句子。
- 每句給穩定編號 `S001`、`S002`。標題、轉折句（「綜上所述」）不編號。
- 一句若含兩個可獨立檢驗的主張，拆成 `S003a`、`S003b`。
- 保留原句原文，不改寫；改寫建議放在報告的「引用措辭」欄。

## 步驟 2：每句列出可檢索的主張

對每句寫一行英文主張，並標主張類型：

| 類型 | 例子（護理語境） | 檢索重點 |
|---|---|---|
| prevalence | 台灣專科護理師人數逐年增加 | 族群 + 指標 + 地區 |
| association | 臨床推理能力與病人安全事件相關 | 暴露 + 結果 + 族群 |
| intervention | 模擬教學能提升護理學生的臨床判斷 | 介入 + 對照 + 結果 + 設計 |
| method | SUS 是常用的系統可用性量表 | 工具名 + 心理計量特性 |
| definition | Tanner 將臨床判斷定義為…… | 原始出處優先 |
| background | 生成式 AI 在醫學教育的應用快速增加 | 領域 + 年份限制 + 綜述 |

再拆出：實體（entity）、關係（relationship）、族群或情境（context）、邊界（boundary，例如 in nurse practitioner students）。

## 步驟 3：檢索

每句 2 到 4 個查詢，由精確到寬鬆：

1. 精確：entity + relationship + outcome + context，MeSH 詞優先，例如 `"Clinical Reasoning"[Mesh] AND "Nurse Practitioners"[Mesh] AND simulation`。
2. 同義：換詞（clinical judgment／clinical reasoning／diagnostic reasoning；nurse practitioner／advanced practice nurse）。
3. 寬鬆：領域脈絡，加年份限制（近 5 年）與文獻類型（systematic review、randomized controlled trial）。
4. 方法或工具：量表名或方法名（System Usability Scale、think-aloud、design-based research）。

規則：

- 一句通常 2 到 5 篇候選即可；`search_articles` 的 `max_results` 設 10 到 20，再人工挑。
- 使用者指定「近 5 年」「護理期刊」「只要 RCT 或系統性回顧」時，寫進查詢或篩選條件，並在報告中重述。
- 主張太寬（例如「AI 改變了護理教育」）先拆成子主張再查，不要整句丟進去。
- 找到高度相關的一篇後，用 `find_related_articles` 擴展，比重新下關鍵字更有效。

## 步驟 4：讀摘要並保守評級

每篇候選都要讀摘要（`get_article_metadata` 或 `search_articles` 回傳的摘要）；需要看方法或結果細節時用 `get_full_text_article`（僅開放取用全文可取得）。

| 等級 | 條件 | 適合的句子 |
|---|---|---|
| direct（直接支持） | 直接檢驗同一關係、介入或方法，族群相近，結果一致 | 實證陳述、介入效果 |
| partial（部分支持） | 只支持一部分、族群不同（護理學生 vs. 專科護理師）、結果相鄰 | 加限定詞後的陳述 |
| background（背景支持） | 提供脈絡或先前觀察，不檢驗該主張 | 前言的背景句 |
| contradictory（相反或限縮） | 結果相反或限縮適用範圍 | 討論、研究限制 |
| metadata-only | 只看了標題，未讀摘要 | 不可引用，只能列入待讀 |

保守原則：

- 標題相關不等於支持。句子寫因果而文獻只有相關，最多給 partial，並在說明中指出。
- 綜述可以支持背景句；主張是實證效果時，優先找原始研究，綜述標為 review-context。
- 若同一句找不到 direct 等級的文獻，明說「無直接支持」，並建議改寫句子或降低宣稱強度。
- 撤稿、更正、關注聲明一律標出，不列為支持。

## 步驟 5：匯出 RIS

把選定的 PMID 交給腳本，不要手打書目：

```bash
python scripts/ris_tools.py fetch --pmid 35696315,12345678 --to ris -o support.ris --ncbi-email you@example.com
python scripts/ris_tools.py check support.ris
```

- `fetch` 由 PubMed efetch 取得 MEDLINE 紀錄，作者用 `FAU` 全名，DOI 自 `LID`／`AID` 取出。
- `check` 列出作者只有姓氏、缺 DOI、缺卷期頁的條目；有問題的先補（用 Crossref `fetch --doi`）再交付。
- 沒有 PMID 的文獻（台灣中文期刊）不要塞進 RIS；在報告中另列，欄位標「以官網為準」。

## 步驟 6：報告

```text
【偵測】workflow=find-support｜範圍=PubMed 同儕審查期刊，2020–2026｜檢索日期 2026-09-06

【結果摘要】
- 6 句中 4 句有直接支持、1 句只有部分支持、1 句無直接支持（建議改寫）

【句子→文獻對照表】
| 句 | 原句 | 文獻（第一作者，年份，期刊，DOI） | 等級 | 證據依據 | 插入建議 | 說明 |
|---|---|---|---|---|---|---|
| S001 | …… | Lyu et al., 2022, J Adv Nurs, 10.1111/jan.15321 | direct | 摘要 | 句尾 | 系統性回顧，族群為乳癌存活者 |

【匯出檔】
- C:\...\support.ris（8 筆，已通過 check）

【風險與缺口】
- S005 無直接支持：找到的都是護理學生族群，建議改寫為「在護理學生中……」
- 未讀全文的候選：S003 第 2 篇（僅摘要）
- 下一步：把 RIS 匯入 EndNote 或交 apa7-master 產 APA 7 條目
```

對照表中「證據依據」只能填：標題、摘要、全文、官網頁面。填「標題」的等級只能是 metadata-only。

## 常見失誤

- 文獻談的是同一疾病但不同介入。
- 文獻族群是病人，句子談的是護理人員或學生。
- 用一篇 2010 年的綜述支持「近年快速增加」。
- 一句塞五篇文獻卻沒有一篇直接支持。
- 把 Consensus 的摘要卡片當成讀過摘要。
