# bob-research-log：研究日誌

把研究過程中零散的文字、白板照片、系統截圖、語音轉錄整理成格式固定、可追溯的 Markdown 研究日誌（含 YAML frontmatter）。改造自上游 nature-skills 的實驗日誌 skill（來源與逐檔異動見 `UPSTREAM.md`），把材料科學實驗語境換成設計本位研究（DBR）與護理教育研究語境。

## 用途

- DBR 迭代紀錄：設計原則、本輪變更、證據、下一輪。
- 系統版本紀錄（V1 到 V7 這類）：版本間變更與依據。
- 使用者測試場次：受試者代號、場景、SUS 原始作答、觀察、放聲思考摘錄、問題。
- 指導教授會議紀錄：討論、決議、待辦與期限。
- IRB 進度：送審、補件、核准、修正案等事件。
- 異常紀錄：系統幻覺、檢索失敗、token 異常、受試者退出、偏離計畫。
- 總索引：Dataview 查詢（選用）或純 Markdown 表格。

輸出一律是 Markdown，frontmatter 固定欄位：`log_id`、`date`、`type`、`project`、`version`、`participants`、`tags`、`status`、`next_actions`、`related`、`attachments`。存檔路徑由使用者指定；沒指定就先回傳內容，不擅自建檔。

## 觸發語

研究日誌、迭代紀錄、寫今天的研究紀錄、meeting 紀錄、指導教授會議紀錄、使用者測試紀錄、IRB 進度、版本紀錄、放聲思考紀錄、系統異常紀錄、研究索引。

不觸發：寫論文章節、統計分析、文獻整理。

## 範例提示詞

1. 「今天跟指導教授 meeting，這是我手機錄音的轉錄（附檔）和白板照片。幫我整理成指導教授會議紀錄，決議和待辦要分開列，期限沒講到的標出來問我。存到 D:\thesis\研究日誌\。」
2. 「V4 剛做完第一場使用者測試，受試者 P03，SUS 十題分數是 4,2,4,2,4,2,5,1,4,2，放聲思考逐字稿在這裡。幫我寫成測試場次紀錄，問題要對應到設計原則，先不要存檔給我看內容。」
3. 「IRB 今天收到醫院的補件通知，要補知情同意書第 3 版和招募海報。幫我開一筆 IRB 進度紀錄，連到上個月送審那筆，待辦期限設 9 月 20 日。」

## 工作方式

1. 讀取上傳材料或本地檔案，照片做視覺分析，語音轉錄先分段。
2. 判斷日誌類型並載入對應範本；一份材料含多種類型時分別建檔並互連。
3. 抽取欄位；缺漏或模糊處問使用者，不猜測，暫填 `AUTHOR_INPUT_NEEDED`。
4. 產生 `log_id`（`{專案代碼}-{類型代碼}-YYMMDD-{序號}`），套範本輸出。
5. 使用者指定路徑時存檔、歸檔附件並更新索引；否則回傳內容。

## 分工表

| 情境 | 交給 | bob-research-log 做什麼 |
|---|---|---|
| SUS 計分、信度、前後測比較 | `bob-statistics` | 記錄原始作答與「未經統計確認」的現場分數 |
| 把迭代紀錄寫成論文第三章 DBR 流程或第四章結果 | `bob-writing`；整章 .docx 交 `academic-writing` | 提供依日期排序的日誌與證據清單 |
| 放聲思考與訪談的質性編碼 | `mixed-methods-research` | 保留逐字稿路徑與觀察摘要 |
| 會議紀錄做成正式 Word 文件 | `docx` | 提供 Markdown 內容 |
| 日誌中的資料畫成論文圖 | `bob-figure` | 提供資料檔路徑與觀察重點 |
| IRB 文件撰寫或修正案內容 | 使用者依送審醫院 IRB 範本 | 只記事件、日期、待辦 |
| 文獻或單篇論文整理 | `paper-analysis`、`bob-citation` | 不做 |

## 內建材料

- `templates/iteration-log.md`、`meeting-log.md`、`test-session-log.md`、`anomaly-log.md`、`index.md`
- `references/example-dbr-iteration.md`（V3 到 V4 迭代示例）、`references/example-test-session.md`（NP 學生測試場次示例）；資料全為虛構。

## 邊界

- 不編造分數、日期、決議或受試者反應。
- 未指定路徑不建檔。
- 日誌不含可識別受試者的資訊；含受試者聲音或畫面的附件只存本機指定目錄。
- Obsidian 與 Dataview 是選用，不是必要。
