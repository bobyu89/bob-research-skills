# 首次投稿信範本（Markdown／Word 版）

用途：第一次投稿給護理、醫學教育、數位健康期刊的編輯信。修訂後的回覆信不用此範本（交 `bob-response`）。

規則：

- 只填作者確認的事實；未確認處保留 `[AUTHOR_INPUT_NEEDED: …]`。
- 不重複摘要；不用「首次」「前所未有」等無範圍的優先性主張。
- 期刊要求的聲明才寫；先確認該刊是否需要投稿信以及有無指定內容。
- 長度以一頁內為原則（以期刊規定為準）。

---

## 英文版

```text
[Date]

[Editor-in-Chief name, or "Dear Editors,"]
[Journal name]

Dear [Editor name / Editors],

Please consider our manuscript entitled "[AUTHOR_INPUT_NEEDED: full title]" for publication as a[n] [AUTHOR_INPUT_NEEDED: article type, e.g. original research article] in [Journal name].

[One to two sentences: the problem addressed and the principal finding. Example pattern: "Nurse practitioner trainees in Taiwan have limited opportunities to practise clinical reasoning with timely feedback. We developed and iteratively evaluated a generative-AI learning system grounded in Tanner's Clinical Judgment Model, and report its usability and learners' experiences across [N] design iterations."]

[One to two sentences: what is specifically new and which evidence supports it. Example pattern: "The study contributes [design principles / evaluation evidence] derived from [data sources], rather than a single-version usability report."]

[One sentence: why the finding matters to this journal's readership. Example pattern: "We believe the work will interest [Journal name] readers concerned with [nurse education / digital health / clinical reasoning]."]

[Required declarations only, as applicable:]
- This manuscript is original, has not been published previously, and is not under consideration elsewhere.
- All authors have read and approved the manuscript and agree to its submission.
- [The manuscript is based on the first author's master's thesis at National Defense Medical Center (Taiwan); the thesis is/is not publicly available at …] [AUTHOR_INPUT_NEEDED]
- The study was approved by [AUTHOR_INPUT_NEEDED: IRB name and approval number].
- [Preprint / related manuscript disclosure, or "none."]
- [Competing interests statement.]
- [Generative AI disclosure, if required by the journal.]
- [Reporting guideline used, e.g. "The study is reported in accordance with [COREQ / SRQR / CONSORT / STROBE / CHERRIES]; the completed checklist is submitted as a supplementary file."]

Thank you for your consideration.

Sincerely,

[AUTHOR_INPUT_NEEDED: corresponding author name, degree]
[AUTHOR_INPUT_NEEDED: position, department, institution]
[AUTHOR_INPUT_NEEDED: postal address]
[AUTHOR_INPUT_NEEDED: email; ORCID]
On behalf of all authors
```

---

## 中文版（台灣中文期刊）

```text
［日期］

［期刊名稱］主編／編輯委員會　鈞鑒：

茲檢附拙作「［AUTHOR_INPUT_NEEDED：全名］」一文，擬投稿　貴刊［AUTHOR_INPUT_NEEDED：文章類型，例如研究論文／原著］，敬請審查。

［一到兩句：研究問題與主要發現。例：本研究針對專科護理師培訓中臨床推理練習與即時回饋不足的問題，以設計本位研究發展結合生成式 AI 與檢索增強技術之學習系統，並報告其在［N］輪迭代中的可用性與學習者經驗。］

［一到兩句：新在哪裡、證據為何。］

［一句：為何適合貴刊讀者。］

本文謹聲明如下（依貴刊規定擇用）：
一、本文為原創著作，未曾發表，亦未同時投稿其他刊物。
二、全體作者均已閱讀並同意投稿。
三、本研究經［AUTHOR_INPUT_NEEDED：IRB 機構全名］審查核准（案號：［AUTHOR_INPUT_NEEDED］）。
四、本文改寫自第一作者之國防醫學院護理學研究所碩士論文［AUTHOR_INPUT_NEEDED：是否適用］。
五、作者間無利益衝突［或依實際情形填寫］。
六、［生成式 AI 使用揭露，依貴刊規定］。
七、本研究依［報告準則名稱］撰寫，檢核表如附件。

　　耑此　敬頌
撰安

［AUTHOR_INPUT_NEEDED：通訊作者姓名］　敬上
［AUTHOR_INPUT_NEEDED：職稱、單位］
［AUTHOR_INPUT_NEEDED：通訊地址、電話、電子郵件］
［日期］
```

---

## 填寫後的檢查

- 標題、作者、機構與稿件標題頁完全一致。
- 主要發現的敘述與摘要結論一致，不誇大。
- IRB 案號與方法章一致。
- 每一條聲明都是期刊實際要求的。
- 所有 `[AUTHOR_INPUT_NEEDED]` 都已解決或列入待辦。

LaTeX 版（`initial-cover-letter.tex`）為選用，只在使用者要求 .tex 時使用。
