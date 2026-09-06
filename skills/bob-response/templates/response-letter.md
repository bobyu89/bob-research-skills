# 逐點回覆表範本（Markdown／Word 版）

用途：每位審稿人各填一份。表格可直接貼進 Word（交 `docx` skill 轉檔時保留表格結構），或以 Markdown 交付。修訂後的文稿文字一律斜體。缺少的事實保留可見佔位符 `[to be supplied]`／「〔待補〕」，不要藏在註解裡。

隱私規則：本檔只放一位審稿人的意見與回覆。不得出現另一位審稿人的意見、編號、建議或回覆文字。多位審稿人重複同一問題時，在每一份檔案都完整回答。

欄位定義：

| 欄位 | 內容 |
|---|---|
| Reviewer／審稿人 | 該檔案對應的審稿人（對外檔案用中性標籤，例如 Reviewer 1；內部 ID 不外流） |
| Comment／審查意見 | 審稿意見原文，不改寫原意 |
| Response／回覆 | 直接回答，說明做了什麼與為什麼；不同意時先承認顧慮再給理由 |
| Location of change／修改處 | 頁、行、段；圖或表編號；附錄編號；沒有行號就寫章節與段落 |
| Status／狀態 | Revised／Clarified／Partially addressed／Not changed (with reason)／Pending author input |

---

## 英文版（English version）

```markdown
# Response to Reviewer 1

**Manuscript:** [Manuscript title to be supplied]
**Manuscript ID:** [ID to be supplied]
**Journal:** [Journal name to be supplied]
**Decision:** Major revision / Minor revision

Dear Reviewer,

We thank you for your careful evaluation of our manuscript. We have revised the manuscript to address
your comments and provide a point-by-point response below. Revised manuscript text is shown in italics;
page and line numbers refer to the marked revised manuscript.

| # | Reviewer comment | Response | Location of change | Status |
|---|---|---|---|---|
| 1 | The System Usability Scale (SUS) was administered to only 12 nurse practitioners. This sample is too small to support the claim that the system is "highly usable". | We agree that a sample of 12 cannot support a summative usability benchmark. The present study is the first iteration of a design-based research cycle in a single medical centre, and the SUS was used as formative evidence to guide the next design cycle. We have revised the Results to report the SUS mean with its 95% CI and the sample size explicitly, replaced "highly usable" with "acceptable usability for this iteration", and added the sample limitation to the Discussion. *Revised text (Results 3.2): "The mean SUS score was [value to be supplied] (SD [to be supplied]; 95% CI [to be supplied]; n = 12), which we interpret as formative evidence for the first design iteration rather than as a summative benchmark."* | Results 3.2, p. [x], lines [x–x]; Discussion 4.4, p. [x], para. [x] | Revised |
| 2 | How was data saturation determined for the think-aloud and semi-structured interview data? | We thank the reviewer for this question. The original Methods did not state the saturation criterion, which we agree was a gap in reporting. We have revised the Methods to state that interviews continued until two consecutive participants yielded no new codes, and that the think-aloud transcripts were analysed together with the interview transcripts using [analysis approach to be supplied]. *Revised text (Methods 2.5): "[Revised saturation paragraph to be supplied by the authors.]"* | Methods 2.5, p. [x], para. [x] | Revised |
| 3 | Generative AI systems produce hallucinations. The manuscript does not explain how hallucination risk was controlled or how it affects patient safety in a clinical reasoning tutor. | We agree that hallucination risk is central to any generative AI application in nursing education. In the revised Methods we describe the retrieval-augmented generation (RAG) pipeline, the curated source corpus from which responses are grounded, and the human review step performed by [role to be supplied] before cases were released to learners. We also clarify in the Discussion that the system is a learning tool used in a supervised educational setting and is not intended for use with real patients; we have added this boundary to the Abstract as well. We do not claim that hallucinations were eliminated; the revised Limitations state that [hallucination monitoring result or statement to be supplied]. *Revised text (Methods 2.3): "[Revised RAG safeguards paragraph to be supplied.]"* | Methods 2.3, p. [x]; Discussion 4.5, p. [x]; Abstract | Revised (pending author confirmation of monitoring result) |
| 4 | Please cite recent work on large language models in nursing education. | We agree that the Introduction should situate the study within recent work on this topic. We have added [citation(s) to be supplied and verified] to the Introduction. | Introduction, p. [x], para. [x]; Reference list | Pending author input |

Sincerely,
[Corresponding author name]
on behalf of all authors
```

---

## 繁中版（給中文期刊或內部核對用）

```markdown
# 審查委員一意見回覆表（修訂說明表）

稿件題目：〔待補〕
稿件編號：〔待補〕
期刊：〔待補〕
審查結果：修改後再審／修改後刊登

感謝審查委員對本稿的細心審閱。以下逐條說明修改情形；修訂後文字以斜體呈現，頁碼與行號以修改稿（紅字標示版）為準。

| 編號 | 審查委員意見 | 回覆說明 | 修改處（頁／行／段） | 狀態 |
|---|---|---|---|---|
| 1 | 系統可用性量表（SUS）僅施測 12 位專科護理師，樣本數過少，不足以支持「系統高度可用」的結論。 | 感謝委員指正。本研究為設計本位研究的第一輪迭代，於單一醫學中心進行，SUS 分數作為引導下一輪設計的形成性證據，而非總結性的可用性基準。已於結果一節明確報告樣本數、平均數、標準差與 95% 信賴區間，將「高度可用」改為「本輪迭代達可接受之可用性」，並於討論加入樣本數限制。*修訂後文字（結果 3.2）：「SUS 平均得分為〔待補〕分（SD =〔待補〕；95% CI〔待補〕；n = 12），本研究將其視為第一輪設計迭代之形成性證據，而非總結性基準。」* | 結果 3.2，第〔x〕頁第〔x〕行；討論 4.4，第〔x〕頁第〔x〕段 | 已修改 |
| 2 | 放聲思考與半結構式訪談的資料如何判定飽和？ | 感謝委員提問。原稿方法一節未說明飽和判準，確為報告上的疏漏。已於方法補充：訪談持續至連續兩位受訪者未再產生新編碼為止；放聲思考逐字稿與訪談逐字稿以〔分析方法待補〕合併分析。*修訂後文字（方法 2.5）：「〔作者補充修訂後段落〕」* | 方法 2.5，第〔x〕頁第〔x〕段 | 已修改 |
| 3 | 生成式 AI 會產生幻覺，稿件未說明如何控制幻覺風險及其對病人安全的影響。 | 感謝委員指出此關鍵問題。已於方法說明檢索增強生成（RAG）流程、回應所依據的經整理之知識來源，以及案例釋出給學習者前由〔角色待補〕進行的人工審核步驟；並於討論與摘要補充本系統為督導下之教學工具，不用於真實病人照護。本研究不宣稱幻覺已完全消除，研究限制已改為〔幻覺監測結果或說明待補〕。*修訂後文字（方法 2.3）：「〔作者補充修訂後段落〕」* | 方法 2.3，第〔x〕頁；討論 4.5，第〔x〕頁；中英文摘要 | 已修改（監測結果待作者確認） |
| 4 | 建議補充近年大型語言模型應用於護理教育之文獻。 | 感謝委員建議。已於前言補充〔文獻待補並查證〕，參考文獻同步更新。 | 前言，第〔x〕頁第〔x〕段；參考文獻 | 待作者補充 |
```

---

## 填表規則

1. 每一列只回答一條意見；審稿人把多個問題寫在同一段時，拆成 1a、1b。
2. 「回覆說明」先直接回答，再說做了什麼；「感謝」一句即可。
3. 「修改處」不可空白；沒有行號就寫章節與段落，並標「〔頁碼待補〕」。
4. 狀態為「未修改」時，回覆說明必須有研究設計或範圍的理由，並註明是否已在討論加限制。
5. 修訂後文字要與修改稿逐字一致；任何一方改了，另一方同步改。
6. 統計數字未經作者確認前不填數字，留「〔待補〕」。
7. 需要 Word 檔時，把本表交給 `docx` skill；表格欄寬建議 5／25／45／15／10（百分比）。
