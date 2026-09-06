# `bob-reviewer` 技能

`bob-reviewer` 從審稿人視角模擬健康科學、護理、醫學教育與數位健康期刊的投稿前同儕審查。
它一次產出三位互盲審稿人的報告與一份事後綜合，幫作者在投稿或口試前找出方法、報告、倫理與
論證上最可能被攻擊的地方。

## 用途

- 對稿件全文、摘要、單一章節、表格或碩士論文章節做投稿前壓力測試。
- 依五個評審軸評估：`originality`、`clinical-educational-significance`、`methodological-rigour`
  （依研究設計對應 EQUATOR 準則）、`ethics-reporting-transparency`、`interdisciplinary-clarity`。
- 三位審稿人在互不可見的獨立 context 中各自產出報告，全部凍結後才產生綜合；
  只有至少兩位獨立提出同一問題時才算共識。
- 意見分成 `Major Concerns` 與 `Minor Comments`；會阻斷核心論證的 Major 標 `Blocking Yes`。
- 每條實質意見都附穩定 ID、claim pointer 與可查證的 evidence pointer，找不到位置就明說。
- 依研究設計載入對應的檢查閘：量性（RCT、類實驗、橫斷、世代）、質性（COREQ、SRQR、
  可信賴性四準則）、混合方法（整合設計、joint display）、系統性與範疇性回顧（PRISMA、
  PRISMA-ScR）、教育介入與 DBR（設計原則、迭代證據、Kirkpatrick 層級）、AI／LLM 應用
  （TRIPOD+AI、CHART、評估集洩漏、提示詞揭露、幻覺與安全）、問卷與量表發展（CVI、信度、
  EFA／CFA）。
- 綜合段之後附「中文核對」區塊：繁中摘要、必須先處理的阻斷性問題、口試委員最可能追問的三點。
- 交叉核對稿件內部的數字、樣本數、術語與表格是否一致。
- 不憑記憶捏造期刊政策；提到期刊規定時標「以期刊官網為準」。

## 觸發語

模擬審稿、三位審稿人、投稿前自審、審稿意見模擬、幫我審這篇、口試前模擬提問、審稿人會怎麼看、
預審、找出審稿人最可能攻擊的點、reviewer report、mock peer review、pre-submission review。

## 範例提示詞

1. 「這是我碩論第三章與第四章（DBR，RAG 臨床推理學習系統，SUS 與放聲思考資料），
   用 bob-reviewer 模擬三位審稿人，最後給我口試委員最可能追問的三點。」
2. 「我要投 Nurse Education Today，稿件是專科護理師教育介入的類實驗研究，
   幫我投稿前自審，重點看方法嚴謹度和 TREND 該報告卻沒報告的項目。」
3. 「這篇是失樂感監測平台的問卷信效度研究（EFA、CFA、CVI），準備投護理研究，
   幫我審這篇，審稿人報告用英文，最後給我繁中摘要。」

## 你需要提供

- 稿件全文、摘要、關鍵章節、表格、圖說或作者說明（英文或繁中皆可）。
- 研究設計與目標期刊；若已知適用的報告準則也一併說明。
- 已有的補充資料，以及「不能再新增資料收集」之類的限制。
- 若要口試前模擬，說明口試委員的組成方向（例如兩位方法學、一位臨床）。

## 產出

- 三份英文審稿人報告（相同骨架，各自側重不同評審軸）。
- `Cross-review synthesis`：共識強項、共識阻斷性問題、其他共識 Major、分歧點、Minor 修訂清單。
- `中文核對`：繁中一段式摘要、阻斷性問題對應 ID、口試委員最可能追問的三點、建議交接。
- `Risk / unsupported claims`：從材料無法評估或無證據支持的項目。

## 分工表

| 需求 | 交給誰 | 本 skill 的關係 |
|---|---|---|
| 單一位資深審稿人的深度批判、Minerva 邏輯謬誤偵測 | `academic-peer-reviewer` | 本 skill 提供三位互盲審稿人與綜合；要單一深度審查時轉交 |
| 判定研究設計對應哪份 EQUATOR 準則 | `equator-guideline-finder` | 準則不確定時先問它，再由本 skill 依該準則審 |
| 準則全文與流程圖（CONSORT、STROBE、PRISMA、PRISMA-ScR） | `consort-2025-master`、`strobe-v4-master`、`prisma-2020-master`、`scoping-review-master` | 本 skill 只列審稿人最常追問的檢查點 |
| 訓練自己的批判性思考 | `critical-thinking-coach` | 綜合段可建議使用 |
| 統計設計與報告的深入檢查 | `bob-statistics` | 本 skill 指出疑點與解決判準 |
| 拿到真實審稿意見後寫回覆信 | `bob-response` | 本 skill 不寫 rebuttal |
| 依審稿風險重建稿件論證 | `bob-writing` | 本 skill 只評估，不改寫 |
| 單篇論文閱讀與整理 | `paper-analysis` | 本 skill 不做 reader |
| 混合方法的設計問題 | `mixed-methods-research` | 本 skill 只查整合是否有做到 |
| 輸出 Word 檔 | `docx` | 本 skill 產生文字後呼叫 |

## 邊界

- 不捏造審稿人身分、專長或編輯決定。
- 審稿人之間不能讀取、引用、同意或回應彼此的意見；綜合只在全部報告凍結後產生。
- 只根據使用者提供的材料與公開審稿原則（ICMJE、COPE、EQUATOR）做保守模擬。
- 不斷言稿件「屬於」某本期刊，也不憑記憶說出期刊的字數或圖表上限。
