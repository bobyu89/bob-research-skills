# 任務：首次投稿材料包（submission-package）

只用於第一次編輯決定之前。完整交接契約、範本與就緒清單見 `references/submission-package.md`。修訂後的回覆信、逐點回覆、申訴交 `bob-response`。

## 核心流程

1. 確認目標期刊、文章類型、稿件標題、通訊作者、要求的交付項目。
2. 需要精確規定時，查期刊當前的作者須知；期刊規定優先於本 skill 的預設。引用具體數字時標「以期刊官網為準，查核日期 YYYY-MM-DD」。
3. 記錄投稿階段（首次投稿／修訂／接受後製作），不把接受後的製作規定當首次投稿的阻擋條件。
4. 依 `journal` 軸載入對應的共用格式檔：
   - `../../../../bob-shared/journal-formats/generic-health.md`
   - `../../../../bob-shared/journal-formats/nursing-journals.md`
   - `../../../../bob-shared/journal-formats/jmir.md`
   - `../../../../bob-shared/journal-formats/taiwan-nursing.md`
   涉及人體研究、AI 使用揭露、報告準則時加載 `../../../../bob-shared/core/health-research-compliance.md`。
5. 建立交付項目矩陣：必要／選用／不適用／需作者輸入。
6. 只用作者提供的事實起草。不捏造作者身分、機構、ORCID、計畫編號、IRB 案號、資料庫連結、利益衝突、審稿人身分或授權。
7. 投稿信簡短、面向編輯：研究顯示什麼、新在哪裡、為何適合這本期刊的讀者、期刊要求的聲明。
8. 每個聲明與稿件、標題頁內部一致。
9. 回傳就緒狀態：`ready`、`ready_with_author_checks`、`blocked`。

## 預設交付項目

- 首次投稿信（Word 或純文字；範本 `templates/submission/cover-letter.md`）。
- 標題頁：作者順序、機構、通訊作者、ORCID、字數、關鍵字、文章類型。
- 三到五條 highlights 或 key points（期刊接受時）。
- CRediT 作者貢獻聲明。
- 資料可用性、程式碼可用性（若有系統或分析程式）。
- 利益衝突、經費、致謝、倫理核准（IRB 案號與機構）、知情同意。
- 生成式 AI 使用揭露（若研究使用或撰寫過程使用，依期刊政策）。
- 報告準則檢核表（CONSORT、STROBE、COREQ、SRQR、PRISMA-ScR、CHERRIES 等）與流程圖；準則先問 `equator-guideline-finder`。
- 推薦與迴避審稿人表（期刊要求時）。
- 相關稿件、預印本、原創性、授權提示。
- 投稿完整性矩陣。
- LaTeX 範本（`templates/submission/*.tex`）為選用，只在使用者要求 .tex 時使用。

## 台灣語境提醒

- 護理雜誌、護理研究等中文期刊多要求中英文摘要並列、作者中英文姓名與職稱；見 `../../../../bob-shared/journal-formats/taiwan-nursing.md`。
- IRB 核准機構寫全名（例如○○醫院人體試驗審議委員會）與案號。
- 碩論改投期刊時，投稿信要說明與學位論文的關係（多數期刊不視為重複發表，但需揭露；以期刊政策為準）。

圖形摘要交 `bob-figure`；修訂信與逐點回覆交 `bob-response`。
