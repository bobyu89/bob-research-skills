# 台灣作者筆記對齊

使用者以繁體中文溝通、提供中文的修改筆記，或要求「中文核對」「中英對照」「回覆審稿意見」「逐點回覆」「退修信」「主要修訂回覆」「次要修訂回覆」「口試委員意見回覆」時，載入本檔。

## 預設行為

- 接受中文的審稿意見摘要、作者筆記、文稿修改筆記，以及中英夾雜的輸入。
- 投稿英文期刊時，最終逐點回覆信用英文；投稿中文期刊（護理雜誌、護理研究、台灣專科護理師學刊等）或口試委員回覆表時，用繁體中文，全形標點，統計符號與引用括號依 APA 第七版用半形。
- 每次輸出保留一段精簡的「中文核對」，列出需要作者決定或補充的事項。
- 翻譯意圖，不逐字翻譯。
- 把模糊的中文筆記轉成具體的「回覆證據需求」。
- 不使用中國大陸用語，也不用簡體字。本 skill 一律用：退修信或修訂（不用「返修」）、主要修訂（不用「大修」）、次要修訂（不用「小修」）、審稿人或審查委員、口試（不用「答辯」）、指導教授（不用「導師」）、資料、回饋、使用者、軟體、實驗室會議、計畫書口試。完整對照表見 `../bob-shared/core/zh-tw-academic-conventions.md`（完成後）。

## 台灣作者常見的回覆問題

以下是台灣護理與醫學教育領域作者在修訂回覆中最常出現的問題，審稿 `audit` 模式時逐一檢查：

| 常見問題 | 表現 | 為什麼有害 | 改法 |
|---|---|---|---|
| 過度道歉 | 每一條都以「非常抱歉」「深感歉意」「感謝審稿人不吝指正」開頭，回覆本體只有一句 | 讀起來像在求情而不是在說明；編輯要的是「改了什麼、在哪裡、為什麼」 | 一句感謝即可，接著直接回答。英文用 `We thank the reviewer for this comment.` 一次，不重複 |
| 全盤接受 | 對每一條都寫「已依審稿人意見修改」，包括彼此矛盾的意見或違反研究設計的要求 | 產生互相矛盾的承諾；把橫斷研究改寫成因果主張；讓審稿人懷疑作者沒有判斷 | 逐條判斷：`ACCEPT_*`、`PARTIAL`、`SOFTEN_CLAIM`、`OUT_OF_SCOPE`、`DISAGREE`。不同意時先承認顧慮，再給研究設計或範圍理由 |
| 回覆與修改不一致 | 回覆信說「已在討論加入限制」，但修改稿裡找不到；或回覆引的段落與修改稿文字不同 | 這是最容易被抓到、也最傷信任的失誤，看起來像捏造合規 | 每一條回覆都貼上修訂後的文字（斜體）並標頁、行、段；定稿前跑整包一致性稽核 |
| 把「已在文中說明」當回覆 | 「此點已在方法第二節說明」「原稿第 8 頁已提及」 | 等於指責審稿人沒讀；審稿人漏看代表呈現不夠清楚 | 用 `CLARIFY_EXISTING`：直接回答問題，承認原本位置或措辭不夠醒目，做小幅澄清或搬移，引用修訂後位置 |
| 用時間或經費當理由 | 「因研究時程限制無法補做」「因經費不足」 | 編輯不會接受方便與否作為主要理由 | 改用研究設計或範圍界限：橫斷設計沒有追蹤資料、DBR 單一場域不做多場域推論；同時軟化主張並加限制 |
| 「詳見正文」 | 不給位置 | 無法追溯 | 一律給章節、頁、行或段落；沒有行號就給章節與段落並標示佔位符 |
| 統計回覆沒有數字 | 「已重新分析，結果一致」 | 審稿人要看檢定名稱、樣本數、效果量、信賴區間 | 交 `bob-statistics` 產出 APA 7 格式的統計句，作者確認後貼回；沒有數字前標 `AUTHOR_INPUT_NEEDED` |
| 中英混用的回覆信 | 英文期刊的回覆信裡夾中文備註 | 送出後被審稿人看到 | 中文只放在「中文核對」區塊，對外檔案全英文 |
| 把總表寄給審稿人 | 一份文件列出所有審稿人意見與回覆 | 破壞互盲；洩露另一位審稿人的意見與建議 | 每位審稿人一份獨立檔案；除非期刊明確要求合併檔 |

## 中文筆記轉換表

| 中文筆記 | 問題 | 較好的處理 |
|---|---|---|
| 「我們已經改了」 | 太模糊 | 問改了什麼、出現在哪裡、有沒有修訂後文字 |
| 「依審稿人意見修改」 | 沒有動作對應 | 轉成 `AUTHOR_INPUT_NEEDED`，直到動作與位置確定 |
| 「我們補收了資料」 | 缺證據 | 要求收案期間、樣本數、場域、結果摘要、圖表位置、IRB 修正案是否已核准 |
| 「我們補了分析」 | 缺分析細節 | 要求分析方法、資料來源、主要結果、統計輸出、文稿位置 |
| 「這個問題不重要」 | 防禦且無依據 | 若學術上站得住，改寫為範圍、證據或主張界限的理由 |
| 「時間來不及所以沒做」 | 高風險藉口 | 只在屬實時改為研究設計或範圍界限；否則標風險 |
| 「審稿人誤解了」 | 指責 | 改寫為文稿清晰度問題並加澄清 |
| 「詳見正文」 | 無法追溯 | 要求章節、頁、行、段、圖、表或附錄 |
| 「我們認為這樣夠了」 | 無依據的充分性主張 | 說明哪些證據回應了顧慮，或標示剩餘限制 |
| 「老師說不用改」 | 依權威而非依據 | 記為 `PROPOSED_DISAGREEMENT`，要求指導教授的學術理由再寫進回覆 |

## 中文核對區塊

用精簡的繁中行動筆記：

```text
中文核對
- R1.1：請補充 SUS 得分的平均數與標準差、樣本數（n），以及結果第 3.2 節的頁碼。
- R1.2：請確認質性資料飽和的判準（例如連續兩位受訪者無新主題）與訪談人數。
- R2.1：目前不能宣稱「幻覺率為零」；建議改為說明 RAG 的檢索來源限制與人工審核流程，並在討論加限制。
```

## 雙語擬稿模式

使用者提供中文筆記時：

1. 審稿意見以提供的語言保留，除非要求翻譯。
2. 追蹤表用英文動作標籤。
3. 英文期刊的回覆信用精煉英文擬稿；中文期刊用繁中。
4. 「中文核對」只放決策、缺漏事實與高風險事項。

## 語氣修正範例

中文作者筆記：

```text
審稿人沒有看懂我們的方法。
```

回覆立場（英文期刊）：

```text
We agree that the original Methods description did not make this distinction sufficiently clear.
We have revised the Methods to clarify [specific distinction and location].
```

回覆立場（中文期刊）：

```text
感謝審查委員的提問。原稿方法一節對此區分的說明確實不夠清楚，已於第 X 頁第 X 段修改為：〔修訂後文字〕。
```

中文作者筆記：

```text
這個實驗我們做不到。
```

回覆立場（英文期刊）：

```text
We agree that this analysis would provide an additional test of [claim]. However, it would require
[a multi-site sample / longitudinal follow-up / a controlled comparison group], which is outside the
scope of the present design-based research study. We have therefore softened the claim and added a
limitation in [location].
```

中文作者筆記：

```text
審稿人要我們把 SUS 樣本數加到 30 人，但我們只有 12 位專科護理師。
```

回覆立場（英文期刊）：

```text
We agree that a larger sample would strengthen the usability evidence. The present study was designed
as a design-based research iteration in a single institution, and the SUS scores are reported as
formative usability evidence rather than as a summative benchmark. We have revised the Results and
Discussion to state the sample size explicitly, to present the SUS score with its 95% confidence
interval, and to add this limitation in [location].
```
