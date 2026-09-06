# 任務：期刊稿件（manuscript）

用一般的章節撰寫流程：建立論文論證、載入要求的 section fragment、從證據往外寫、回傳草稿與主張證據對照。

- 依 `paper_type` 載入類型 fragment，依 `journal` 載入期刊 fragment，最後套 `language`。
- 研究設計明確時，先呼叫 `equator-guideline-finder` 決定報告準則，再對照 `../../../../bob-shared/core/health-research-compliance.md` 把準則項目分配到各節。
- 使用者沒要求時，不加投稿表單或編輯信函。
- 整章要輸出 .docx 時交 `academic-writing`；參考文獻格式交 `apa7-master`。
