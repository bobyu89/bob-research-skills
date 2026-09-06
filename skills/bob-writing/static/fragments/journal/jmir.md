# 期刊：JMIR 系列（jmir）

使用者指定 Journal of Medical Internet Research、JMIR Medical Education、JMIR Nursing、JMIR Human Factors、JMIR Formative Research、JMIR AI、JMIR mHealth and uHealth 或其他 JMIR Publications 期刊時使用。

## 先讀共用事實

開啟 `../../../../bob-shared/journal-formats/jmir.md`：結構式摘要五段、Trial registration、Multimedia appendix、CHERRIES 與 CONSORT-EHEALTH 等 JMIR 特有要求。本檔是撰寫動作層；具體字數與格式以期刊官網為準並註明查核日期。

## 讀者與立場

- 讀者是數位健康、醫學資訊、健康專業教育的跨領域研究者與開發者。他們同時要看得懂技術與評估設計。
- JMIR 對「介入描述」與「評估嚴謹度」要求並重：系統怎麼做的要能重現，評估怎麼做的要能被檢驗。
- 形成性研究（formative research）、可用性研究、原型評估在 JMIR 系列有明確的位置；不要把可用性研究包裝成成效試驗，選對子刊與文章類型比誇大更重要。

## 摘要

- 結構式五段：Background、Objective、Methods、Results、Conclusions（試驗類另加 Trial Registration）。
- Objective 用一句話，與正文研究目的字面一致。
- Results 段要有主要數字（樣本數、主要指標與統計量、或主要主題數與名稱）。
- Conclusions 不超出 Results；一句話說明對數位健康實務或設計的意涵。
- 撰寫依 `../../../../bob-shared/core/abstract-evidence-chain.md`。

## 緒論

- Background 與 Objective 常用小標題分開；Background 依問題漏斗（`../../../../bob-shared/core/introduction-funnel.md`），Objective 一段。
- 技術背景（例如 RAG、LLM）只寫到讀者理解設計理由所需的程度；詳細技術移方法或附錄。
- 前導研究或先前版本要揭露並引用。

## 方法

- 介入或系統描述：常用小節 System design、Architecture、Content 或 Knowledge base、Development process；建議附架構圖與介面截圖（Multimedia Appendix）。
- AI 系統要交代：模型名稱與版本、提示設計、知識庫來源與更新日期、幻覺與安全處理、評估集來源與洩漏控制。報告準則先問 `equator-guideline-finder`（可能為 TRIPOD+AI、CONSORT-AI、CHART 或 CONSORT-EHEALTH），再對照 `../../../../bob-shared/core/health-research-compliance.md`。
- 網路問卷用 CHERRIES；使用者測試用 System Usability Scale 等標準工具並交代計分與詮釋基準。
- 倫理：IRB 機構與案號、知情同意方式（線上同意要說明）、資料儲存與去識別化。
- 迭代開發（DBR 或敏捷）要有版本表，見 `paper_type/dbr.md`。

## 結果

- 依 `section/results.md`；依研究目的順序分小節。
- 可用性、使用紀錄（日誌）、成本（token、延遲）與學習或臨床指標分開報告，不混在同一段。
- 質性結果依主題與引文。

## 討論

- 常見結構：Principal Findings → Comparison With Prior Work → Strengths and Limitations → Future Directions 或 Implications → Conclusions。
- Principal Findings 開場一段重述主要發現（不重列數字）。
- 限制含技術層面（模型版本更新、知識庫時效）與研究層面（樣本、場域、自陳）。

## 常見退稿原因（撰寫層面）

- 系統描述不足以重現；或反之，論文變成產品說明書。
- 可用性研究宣稱成效。
- 文章類型選錯（形成性研究投原著）。
- AI 使用未揭露或評估集可能洩漏。
- 摘要 Conclusions 超出 Results。

## 撰寫前檢查

- 文章類型與子刊已確認（原著、formative research、可用性研究、方案描述）。
- 系統描述可重現：模型版本、提示、知識庫、更新日期、安全機制。
- 評估設計與主張相稱：可用性研究不宣稱成效。
- 報告準則已決定且檢核表在附件。
- Multimedia Appendix 已編號並在正文引用。
- 摘要五段與正文小標題一一對應。

## 投稿材料

`task=submission-package` 時，依 `../../../../bob-shared/journal-formats/jmir.md` 的清單建立交付矩陣，注意 Multimedia Appendix 的編號與引用、Trial registration（若適用）、報告準則檢核表。投稿信用 `templates/submission/cover-letter.md`。
