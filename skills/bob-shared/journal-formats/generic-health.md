# 健康科學期刊通用預設（generic-health）

當 `journal=generic-health`，或目標期刊尚未指定、或目標期刊不在本目錄的其他檔案中時，作為 `bob-writing`、`bob-polishing`、`bob-reviewer` 的預設格式假設。此檔案只列**多數健康科學、護理與醫學教育期刊共有的結構性要求**；**不寫任何具體的字數、圖表數或參考文獻數上限**。實際限制一律以目標期刊的作者須知為準，並在稿件檢核表記錄查核日期。

> 查核提醒：本檔案內容整理於 2026-09-06；任何具體規定都以期刊官網為準（查核日期 2026-09-06）。

## 1. 文章類型

多數期刊區分以下類型；投稿前先確認目標期刊對該類型的定義與限制：

- Original research / Original article（原著）
- Review（系統性回顧、範疇性回顧、敘述性回顧、統合分析，常各有不同限制）
- Protocol（研究計畫書，部分期刊接受）
- Brief report / Short communication / Research letter
- Discussion paper / Commentary / Editorial（多為邀稿）
- Methodology paper（量表發展、方法學）
- Case report（護理期刊較少）

## 2. IMRaD 結構

原著論文的預設結構：

1. Title
2. Abstract（結構式或非結構式，依期刊）
3. Keywords（多數要求 3 到 6 個，優先 MeSH；以期刊為準）
4. Introduction（背景、重要性、缺口、目的；見 `../core/introduction-funnel.md`）
5. Methods（設計、場域與參與者、介入或工具、資料收集、資料分析、倫理）
6. Results
7. Discussion（含 Limitations；部分期刊要求獨立的 Strengths and limitations、Implications、Conclusion）
8. Conclusion
9. Declarations（見第 4 節）
10. References（APA 7 或期刊指定格式；由 `apa7-master` 產生）
11. Tables、Figures（依期刊：嵌入正文、置於文末、或分開上傳）
12. Supplementary material（附錄／補充資料）

質性研究常把 Methods 拆為 Design、Participants、Data collection、Data analysis、Rigour（或 Trustworthiness）、Ethical considerations。混合方法另加 Integration。

## 3. 結構式摘要

多數健康科學期刊要求結構式摘要，常見段落組合：

- Background / Aim(s) / Design / Methods / Results / Conclusion(s)（JAN、IJNS 系列常見）
- Background / Objectives / Design / Settings / Participants / Methods / Results / Conclusions（IJNS 常見）
- Background / Objective / Methods / Results / Conclusions（JMIR 系列；見 `jmir.md`）
- Objective / Methods / Results / Conclusions（醫學教育期刊常見）

段落名稱、順序與字數以期刊官網為準。摘要的內容策略見 `../core/abstract-evidence-chain.md`。

## 4. 必要聲明（Declarations）

投稿前逐項確認目標期刊要求哪些，缺少者標 `AUTHOR_INPUT_NEEDED`：

| 聲明 | 常見要求 |
|---|---|
| Ethics approval | 審查單位名稱與編號；免審的依據 |
| Consent to participate | 取得方式 |
| Consent for publication | 若有可識別資料或影像 |
| Trial registration | 前瞻性介入試驗的登錄號與日期 |
| Data availability | 資料可否取得、限制與程序 |
| Code availability | 若有自製程式碼 |
| Conflict of interest / Competing interests | 每位作者 |
| Funding | 經費來源與計畫編號；無經費亦要聲明 |
| Author contributions | CRediT 分類或期刊格式 |
| Acknowledgements | 非作者的貢獻者、AI 工具（依期刊政策） |
| AI use declaration | 依期刊政策；見 `../core/ethics.md` |
| Reporting guideline | 所用準則名稱與檢核表（常要求上傳） |
| Patient and public involvement | 部分期刊要求 |

## 5. 報告準則清單

投稿時多數期刊要求附上對應 EQUATOR 準則的檢核表，並在 Methods 中提及。路由表見 `../core/health-research-compliance.md` 第 3 節。

## 6. 投稿前必查清單

以下每一項都要到期刊官網確認，並在檢核表填上查核日期：

- [ ] 文章類型與其限制（字數、摘要字數、圖表數、參考文獻數、關鍵詞數）
- [ ] 摘要是否結構式、段落名稱
- [ ] 參考文獻格式（APA 7、Vancouver、期刊自訂）與 DOI 呈現方式
- [ ] 標題頁要求（作者、機構、ORCID、通訊作者、字數統計、致謝與利益衝突是否放標題頁以利盲審）
- [ ] 是否雙盲審查；稿件本文需去識別化的程度
- [ ] 圖表放置方式與檔案格式、解析度（見 `bob-figure`）
- [ ] 補充資料的檔案格式與命名
- [ ] 必要聲明清單（第 4 節）
- [ ] 報告準則檢核表是否須上傳
- [ ] 封面信是否必要、內容要求（例如新穎性聲明、未一稿多投聲明）
- [ ] 推薦或迴避審查委員的規定
- [ ] 開放取用與 APC；機構或國科會是否有補助
- [ ] 預印本政策
- [ ] 語言編修證明是否要求（非英語母語作者）
- [ ] 期刊官網 URL：______（使用者填寫）；查核日期：______

## 7. 常見退稿原因（通用）

- 前言沒有精確缺口，只有領域重要性
- 研究設計與研究問題不對應；沒有引用報告準則
- 方法段缺少倫理審查編號或知情同意說明
- 結果只有 p 值沒有效果量與信賴區間；表格與正文數字不一致
- 討論重述結果、限制寫成通用清單、含意與發現無關
- 摘要與正文的數字或結論不一致
- 參考文獻格式錯誤、過時、或有無法查證的條目
- 英文品質未達審查門檻（交 `bob-polishing`，必要時建議專業編修）
- 稿件超出範圍（scope）：投稿前先讀期刊 Aims and scope 與近兩年同主題文章
