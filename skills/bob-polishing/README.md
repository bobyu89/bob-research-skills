# bob-polishing

潤飾、重組或翻譯護理與健康科學領域的學術文字。適用於碩士論文章節、期刊投稿稿、摘要、標題、審查後修訂稿。在不改動事實、證據邊界、術語與 APA 7 引用意圖的前提下，讓文字更清楚、論證更站得住。

改造自上游 `nature-skills` 的潤飾 skill（來源見 [UPSTREAM.md](UPSTREAM.md)），目標讀者從 Nature 系列改為護理、醫學教育、數位健康期刊與台灣中文期刊、國防醫學院碩士論文。

## 用途

- 學術中文潤飾：去贅字、翻譯腔、被動句濫用、「進行……的動作」、「的」字串；統一術語；全形標點與 APA 中文引用格式。
- 中翻英：從台灣作者的學術中文改寫成投稿可用的學術英文，處理冠詞、時態、名詞堆疊、中式連接詞、which 濫用、保留語強弱。
- 學術英文潤色：句子與段落層次的清楚度，保留語與證據強度匹配，術語一致。
- 結構診斷：論文類型（含質性、混合方法、DBR）、章節任務、主張／證據／邊界，先修結構再修文字。
- 結果段精簡與主文配置：什麼留主文、什麼進附錄或圖說，防止修訂稿堆積。
- 去 AI 腔：學術英文與學術中文各一份清單，維持學術體。
- 排版：Word（表格跨頁、圖說、標楷體與 Times New Roman、目錄 F9、分節頁碼、孤行）與 LaTeX。

## 觸發語

潤稿、潤飾、潤色、英文潤色、改寫成學術英文、中翻英、學術英文、去 AI 腔、太像 AI 寫的、精簡結果段、主文太長、排版、Word 排版、表格跨頁、目錄更新、翻譯腔、贅字、摘要潤飾、標題建議、語言編輯。

## 範例提示詞

1. 「這是我碩論第四章第二節，DBR 第三個迭代週期的結果，含 SUS 分數與訪談引文。幫我潤飾成所辦要的學術中文，全形標點，引用格式不要動。」
2. 「把這段討論改寫成學術英文，投 JMIR Medical Education。我們是專科護理師學生的臨床推理學習系統，沒有對照組，不要寫成有效提升能力。」
3. 「這段前言要投護理雜誌，審查委員說太像 AI 寫的。幫我去 AI 腔，維持學術體，順便檢查有沒有大陸用語。」
4. 「我的 Word 論文表格跨頁時標題列不會重複，圖說一直跑到下一頁，目錄頁碼也不對。告訴我怎麼修。」

## 你需要提供

- 原文、目標章節、論文類型、希望保留的術語。
- 不能改變的事實、數字、引用與專有名詞。
- 目標期刊或所方規範（沒有就用健康科學期刊通用預設）。
- 期望輸出：只給改寫版，還是附修改說明與需要作者確認的清單。

## 產出

- 可直接貼進 Word 的潤飾版（中文或英文）；使用者要求時給對照版。
- `修訂說明`：3 到 5 條結構與文字調整。
- `請作者確認`：不能靠潤飾解決的事實、數字、引用位置問題。
- 觸發主文精簡時附 `主文精簡稽核`；觸發去 AI 腔時附處理摘要；排版時給「問題 → 操作步驟」清單。

## 與既有 skill 的分工

| 既有 skill | 負責 | bob-polishing 的關係 |
|---|---|---|
| `academic-writing` | 整章撰寫、整合文獻成段、輸出 .docx、撰寫時的 humanize | 本 skill 只潤飾既有文字；要從零寫或要整章 .docx 時交過去 |
| `speak-human-tw` | 台灣口語化、講人話 | 本 skill 的去 AI 腔維持學術體；要口語版本時轉交 |
| `docx` | 直接操作 Word 檔 | 本 skill 的 `references/word-layout.md` 說明要做什麼；實際改檔交給 docx |
| `apa7-master` | APA 7 參考文獻格式 | 本 skill 不動 reference list，只保持內文引用不被改壞 |
| `bob-writing` | 論證架構與章節規劃 | 需要重建整章論證時交過去 |
| `bob-response` | 審查意見回覆 | 回覆信語言交過去 |
| `bob-statistics` | 統計文字與表格 | 本 skill 只修統計句子的文字，不改數字與檢定 |
| `concept-analysis-master` / `scoping-review-master` / `mixed-methods-research` | 各自的方法論 | 設計問題轉交；本 skill 只管怎麼寫 |
| `academic-peer-reviewer` | 單一深度審稿 | 使用者要審稿意見而非潤飾時轉交 |

## 邊界

- 不替作者新增結果、機轉、統計顯著性或未提供的引用。
- 不為了「更像期刊文章」而誇大新穎性、因果或推論範圍。
- 不憑記憶引用期刊的字數與圖表上限；需要時請使用者提供官網規定並標註查核日期。
- 不對付 AI 偵測器；只處理文字品質。

## 目錄結構

```
bob-polishing/
  SKILL.md                 router（繁中）
  manifest.yaml            軸、always_load、references.on_demand
  README.md                本檔
  UPSTREAM.md              上游來源與逐檔清單、驗收結果
  static/core/             stance、failure-modes、output-format（繁中）
  static/fragments/
    paper_type/            research、methods、hypothesis、algorithmic、review、qualitative、mixed-methods、dbr
    section/               abstract、intro、results、discussion、conclusion、title、methods
    language/              en、zh-tw、zh-tw-to-en
    journal/               generic-health、nursing、jmir、taiwan-nursing、ndmc-thesis、nature-family
  references/              word-layout、ai-trace-reduction、latex-layout、section-moves、
                           phrasebank-playbook、style-guardrails、writing-strategy、
                           published-article-patterns、nat-comms-2025-diction
```
