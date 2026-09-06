# 語言：中翻英（台灣作者的學術中文 → 學術英文）

來源是中文或帶有明顯中文結構的英文時，不逐句翻譯。先抽命題，再重建邏輯，最後才寫英文句子。輸出預設只有英文；使用者要求時才附中英對照。

## 工作順序

1. 抽出每段的核心命題，先用簡單英文條列。
2. 補回中文常省略的邏輯連接：對比、因果、推論、限制。但不要每句都加連接詞。
3. 對照原文檢查術語、因果強度、保留語強度。中文說「可能」不能翻成 `demonstrates`；中文說「證實」而設計只是相關，要在翻譯時降為 `suggests` 並在修訂說明標記。
4. 術語、量表名稱、模型名稱、統計名詞保持標準英文，不自行意譯。台灣常見的量表要用原始英文名稱（System Usability Scale，不是 System Availability Scale）。
5. 邏輯重建完成後，才套 `en.md` 的句子與段落規則。

## 台灣作者常見的英文問題

### 冠詞

- 可數單數名詞第一次出現用 `a/an`，之後用 `the`；泛指複數不加冠詞；抽象名詞泛指不加冠詞。
- 常見錯誤：`The nurse practitioners in Taiwan` 泛指時應為 `Nurse practitioners in Taiwan`；`we developed system` 應為 `we developed a system`。
- 專有名詞與量表：`the System Usability Scale`、`the Tanner model`；縮寫後 `the SUS`、`SUS scores`（複合名詞前不加）。

### 時態

- 方法與結果用過去式（`Participants completed`、`The mean score was`）。
- 已確立的知識、圖表指引、本文主張用現在式（`Table 2 shows`、`These findings suggest`）。
- 文獻回顧：描述某篇研究的作法用過去式或現在完成式；描述領域共識用現在式。
- 常見錯誤：整篇一律過去式，把 `This study suggests` 寫成 `suggested`；或摘要中結果用現在式。

### 名詞堆疊

- 中文的定語前置直譯成三個以上名詞相連時，讀者無法解析。`nurse practitioner clinical reasoning learning system usability evaluation` 要拆成 `usability evaluation of a clinical reasoning learning system for nurse practitioners`。
- 用介系詞片語或關係子句打開堆疊，三個名詞是上限。

### 中式連接詞與句型

- `Firstly, ... Secondly, ... Thirdly, ... Finally, ...` 全段排比：改為主題名詞承接，或最多留 `First` 與 `Second`。
- `On the one hand ... on the other hand`：只在真正對比時用。
- `In recent years, with the rapid development of ...`：套話開頭，刪除或改成具體的問題句。
- `It is well known that`、`As we all know`、`There is no doubt that`：刪除。
- `Besides`、`What's more` 當學術連接詞：改 `In addition` 或刪除。
- `So` 開頭：改 `Therefore` 或重組。
- `Through ... , we ...`、`By using ..., we ...` 開頭連續出現：改為主動主詞開頭。
- `respectively` 濫用：只在兩組對應清楚時用。
- 「本研究」直譯 `This study` 每句都出現：改用 `we` 或省略。

### which 與關係子句

- `, which` 一句接一句的鏈式關係子句是中文長定語的殘留；一句最多一個關係子句，其餘拆句。
- 用 `which` 指涉整句話（`..., which means that`）在多數期刊視為模糊；改為 `This finding indicates that` 或 `This`加名詞。
- 限定用法用 `that` 不加逗號，非限定用法用 `, which`。

### 保留語（hedging）

- 過弱：`might possibly suggest`、`it seems that it may be`；一層保留語即可。
- 過強：`prove`、`confirm`、`definitely`、`obviously`、`significantly` 沒有統計檢定支撐時。單組前後測、橫斷相關、可用性測試都不能用 `demonstrate effectiveness`。
- 對應表：中文「證實」→ `showed`/`confirmed`（只有設計允許時）；「顯示」→ `showed`/`indicated`；「可能」→ `may`；「有助於」→ `may help`/`may facilitate`；「提升」在無對照時→ `was associated with higher`。
- 「顯著」只有在報告統計檢定時翻成 `significantly`，其餘翻 `substantially`/`markedly`。

### 其他常見錯誤

- 單複數：`data were`、`research` 不可數（`studies` 可數）、`feedback` 不可數、`literature` 不可數。
- `research` 當動詞、`analysis` 與 `analyses` 混用。
- 中文「等」直譯 `etc.` 出現在學術正文：改 `such as` 或列完整。
- `obvious`、`very`、`quite`、`a lot of`：刪除或換精確用語。
- 中文「以及」「和」對應 `and`，不要譯成 `as well as` 堆疊。
- 台灣特有的名詞：`nurse practitioner (NP)` 在台灣脈絡下要在首次出現說明制度差異（例如受訓中的 NP 學生），避免讀者以美國 NP 的定義理解。
- 機構名稱用官方英文（National Defense Medical Center、Tri-Service General Hospital）。
- 引用格式維持 APA 7：作者年份不翻譯、不重新排序；中文文獻在英文稿中的寫法交給 `apa7-master`。

## 交接

- 翻譯完成後若使用者要「去 AI 腔」，載入 `references/ai-trace-reduction.md`（本 skill 根目錄） 的英文清單。
- 使用者要口語化、講人話版本（例如給病人看的衛教文字）時，轉交 `speak-human-tw`。
