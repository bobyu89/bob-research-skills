# 期刊：健康科學通用預設（generic-health）

使用者未指定期刊，或目標期刊不在其他 fragment 範圍時使用。這是預設值。

## 先讀共用事實

開啟 `../../../../bob-shared/journal-formats/generic-health.md`：IMRaD、結構式摘要、關鍵字、報告準則清單、資料可用性、利益衝突的通用要求。本檔是其上的撰寫動作層。

## 讀者

健康科學、護理、醫學教育、數位健康的跨領域讀者：臨床人員、教育者、研究者。假設讀者懂研究方法，但不熟你的場域（例如台灣專科護理師制度、國防醫學院培訓流程）；場域特殊之處要在緒論或方法用一兩句交代。

## 撰寫優先順序

- 結構：IMRaD 為預設；Background 段可含簡短文獻回顧，不另立 Literature Review（除非期刊要求）。
- 摘要：預設結構式（Background / Aim / Design / Methods / Results / Conclusion 或期刊指定標題）；撰寫依 `../../../../bob-shared/core/abstract-evidence-chain.md`。
- 緒論：問題漏斗依 `../../../../bob-shared/core/introduction-funnel.md`；最後一段是研究目的與研究問題，不是結果預告。
- 方法：依研究設計對應報告準則（先問 `equator-guideline-finder`），逐項有落點。
- 結果：依 `section/results.md`；統計依 APA 第七版。
- 討論：依 `../../../../bob-shared/core/discussion-argument-language.md`；多數健康科學期刊要求獨立的 Limitations 段與 Implications for practice 或 Relevance to clinical practice 段。
- 結論：一段，回答目的，不引新資料。

## 撰寫前的字數預算

不憑記憶寫死上限。做法：

1. 請使用者提供期刊作者須知的字數與圖表上限，或標「以期刊官網為準，查核日期 YYYY-MM-DD」。
2. 依上限分配：緒論約 15%、方法約 25%、結果約 30%、討論約 25%、結論約 5%（示例比例，依論文類型調整；質性與 DBR 的結果通常更長）。
3. 已有草稿時先估現況，超出的節在起草前就指出。

## 早期就要規劃的配套項目

- 報告準則檢核表與流程圖（CONSORT、STROBE、COREQ、SRQR、PRISMA-ScR、CHERRIES、TRIPOD+AI 等）。
- IRB 核准機構與案號、知情同意方式。
- 資料可用性聲明（多數健康科學期刊接受「因涉及個資，資料於合理要求下提供」，但要寫清楚聯絡方式與條件；以期刊政策為準）。
- 生成式 AI 使用揭露：研究中使用（系統本身）與撰寫中使用（語言協助）分開聲明。
- 作者貢獻（CRediT）、利益衝突、經費。
- 關鍵字：依 MeSH 或 CINAHL 標題選 3 到 6 個。

## 可選脈絡

有提供就用，沒提供就以通用預設進行並註明假設；只在缺漏會改變科學意義或必要交付項目時才問：

- 目標期刊與文章類型（原著、簡報、方案描述、質性研究專欄）。
- 摘要格式（結構式標題名稱）。
- 是否需要 highlights、key points、what is already known / what this paper adds 方框。
- 讀者範圍（次領域或跨領域）。

## 常見退稿原因（撰寫層面）

- 緒論太長、缺口不清，研究目的出現在第五段以後。
- 方法對不上報告準則項目，或準則檢核表未附。
- 結果只有 *p* 值沒有效果量；表格與正文重複。
- 討論重述結果，沒有與文獻比較，也沒有具體的實務意涵。
- 限制籠統（「樣本數小」）而沒有說明對結論的影響。
- 摘要結論超出結果；關鍵字沒有用標準詞彙。
- 可用性、滿意度、自陳學習被寫成成效或能力提升。

## 撰寫前檢查

- 研究目的 → 研究問題 → 分析 → 結果小節 → 討論小節一一對應。
- 術語帳鎖定：理論、量表、系統名、變項、縮寫。
- 報告準則已決定，且每個項目在稿件有落點。
- 倫理、資料可用性、AI 揭露、作者貢獻的事實已向作者確認。

## 期刊層級的提醒

- 使用者後來指定期刊時，改載入對應 fragment；只有修訂範圍實質含糊時才問。
- 護理期刊：`journal/nursing.md`；JMIR 系列：`journal/jmir.md`；台灣中文期刊：`journal/taiwan-nursing.md`；碩論：`journal/ndmc-thesis.md`。
- Nature 系列 fragment 仍保留（`nature.md`、`nature-family.md`、`nat-comms.md`、`nat-mach-intell.md`），但非預設且未經本集驗證，只在使用者明確指定時載入。
