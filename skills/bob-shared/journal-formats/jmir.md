# JMIR 系列期刊的投稿慣例（jmir）

當 `journal=jmir` 時使用。JMIR Publications 旗下期刊（Journal of Medical Internet Research、JMIR Medical Education、JMIR Nursing、JMIR Formative Research、JMIR Human Factors、JMIR AI、JMIR Research Protocols、JMIR mHealth and uHealth 等）共用一套作者須知，但各刊的範圍、文章類型與 APC 不同。此檔案只列**結構性特徵與必查清單**，**不寫死字數、圖表數或費用**；一律以 JMIR 官網為準（本檔整理日期 2026-09-06）。

## 1. 結構性特徵（長期穩定，仍以官網為準）

### 結構式摘要五段

JMIR 系列的原著論文摘要固定為五段，段名固定：

1. **Background**：已知現象與缺口
2. **Objective**：研究目的，通常一句，與正文 Introduction 末段的目的句一致
3. **Methods**：設計、場域、參與者、介入或系統、測量、分析
4. **Results**：主要發現與數字（JMIR 期待具體數字，含 n、效果量或 p 值）
5. **Conclusions**：意義與含意，不重複 Results

字數上限以官網為準。摘要策略見 `../core/abstract-evidence-chain.md`。

### Trial registration

- 有臨床試驗登錄號時，在摘要末尾以「Trial Registration:」列出登錄平台、編號與網址。
- 計畫書類文章（JMIR Research Protocols）要求 International Registered Report Identifier（IRRID），格式依官網。
- 非試驗研究不需此段，但若研究曾預先登錄（OSF 等）可在 Methods 說明。

### Multimedia Appendix

- JMIR 把補充資料稱為 **Multimedia Appendix**，依序編號（Multimedia Appendix 1、2……），在正文中引用。
- 報告準則檢核表（CONSORT-EHEALTH、CHERRIES、COREQ 等）通常以 Multimedia Appendix 上傳。
- 問卷全文、系統截圖、提示詞、知識庫清單、額外表格都適合放這裡。
- 每個附錄要有標題；檔案格式依官網。

### 報告準則

- 網路或行動裝置介入的試驗：**CONSORT-EHEALTH**（JMIR 自家發展的延伸，常被要求）
- 線上問卷：**CHERRIES**（JMIR 發展）
- 其他依設計：CONSORT、STROBE、COREQ、PRISMA、TRIPOD+AI 等
- 形成性或可用性研究（JMIR Formative Research、JMIR Human Factors）：依實際設計，常為 CHERRIES 或 COREQ；系統可用性測試常需描述任務、參與者與量表（SUS）

### 其他常見要求

- 關鍵詞：多數要求 MeSH 詞彙，數量以官網為準
- 參考文獻：JMIR 自有格式（Vancouver 變體），非 APA；投稿時用 EndNote 或 Zotero 的 JMIR 樣式，或由 `apa7-master` 以外的工具轉換；**不要用 APA 格式投 JMIR**
- 圖表：JMIR 對圖的格式與表的格式有明確規定（例如表格不用合併儲存格），以官網為準
- 作者貢獻、利益衝突、資料可用性、AI 使用揭露：依官網的 Declarations 順序
- JMIR 對生成式 AI 的使用有明確政策，投稿前查核並揭露
- JMIR 系列的審查流程含「Preprint」與「Open Peer Review」選項，投稿時要選擇

## 2. 適合的文章類型（依研究階段）

| 研究階段 | 可能的期刊與類型（以官網為準） |
|---|---|
| 系統原型與早期可用性、單輪測試 | JMIR Formative Research；JMIR Human Factors |
| 教育介入的評估 | JMIR Medical Education |
| 護理情境的數位介入 | JMIR Nursing |
| AI 或 LLM 應用與評估 | JMIR AI；JMIR Medical Informatics |
| 研究計畫書 | JMIR Research Protocols |
| 完整的介入試驗或大型評估 | Journal of Medical Internet Research |

DBR 研究可以拆成「形成性評估（早期迭代）」與「總結性評估（最終版本）」兩篇，但要在各稿件中揭露彼此的關係。

## 3. 投稿前必查清單

- [ ] 目標刊的 Aims and scope 與近兩年同主題文章
- [ ] 文章類型名稱與限制（字數、摘要字數、圖表數、參考文獻數）
- [ ] 摘要五段的段名與字數
- [ ] Trial registration 或 IRRID 的要求
- [ ] 關鍵詞數量與 MeSH 要求
- [ ] 參考文獻格式（JMIR 樣式）與 DOI／URL 要求
- [ ] Multimedia Appendix 的格式、命名與數量限制
- [ ] 報告準則檢核表（CONSORT-EHEALTH、CHERRIES 等）是否必附
- [ ] 表格與圖的格式規定
- [ ] AI 使用揭露政策與位置
- [ ] Declarations 順序與內容
- [ ] APC 金額與折扣（機構會員、國家折扣）
- [ ] 審查選項（Open peer review、Preprint）
- [ ] 投稿系統與帳號
- [ ] 官網 URL：______（使用者填寫）；查核日期：______

## 4. 寫作提醒（JMIR 讀者）

- 讀者跨臨床、資訊與教育；系統描述要讓臨床讀者理解，評估設計要讓方法學讀者信服。
- JMIR 期待 Results 段有具體數字，Conclusions 段有明確的實務含意。
- 系統論文要交代：技術架構（含 LLM 模型與版本、RAG 的檢索與知識庫）、資料流向與隱私、使用者訓練、系統日誌如何轉為使用量指標、成本（token）。
- 可用性研究要交代任務、參與者背景、施測環境、量表（SUS 等）的計分與詮釋依據。
- 限制要具體：原型系統、單一機構、小樣本、短期、無對照、自陳式測量。

## 5. 官方來源

- JMIR Publications 作者須知入口：<https://www.jmir.org/author-guidelines>（以官網現行內容為準；查核日期 2026-09-06）
- CONSORT-EHEALTH 與 CHERRIES 原始文獻與檢核表：由 `equator-guideline-finder` 提供
