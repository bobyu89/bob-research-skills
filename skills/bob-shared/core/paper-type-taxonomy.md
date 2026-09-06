# 論文類型分類（Paper-type taxonomy）

`bob-polishing`、`bob-writing`、`bob-reviewer` 與任何使用 `paper_type` 軸的 skill 共用的標準詞彙。此處只定義**類型與判別規則**；各 skill 在自己的 `static/fragments/paper_type/<type>.md` 加上動作層（要診斷什麼、要怎麼起草）。

## 十種類型

前五種沿用上游的通用科學論文分類；後五種是為護理與健康科學研究新增，對應使用者實際進行中的研究工作。

| 類型（axis 值） | 一句話定義 | 讀者的核心問題 | 常見報告準則 |
|---|---|---|---|
| **research** | 以初級觀察或實驗報告某個現象、關聯或效果（量性為主）。 | 發現了什麼？代表什麼？ | STROBE、CONSORT、TREND |
| **methods** | 提出新的測量工具、量表、流程或方案，並證明其信效度或優勢。 | 有效嗎？比既有的好嗎？可重複嗎？ | COSMIN、GRRAS |
| **hypothesis** | 針對一個明確的因果解釋設計證據，確立或排除它。 | 提出的機制是對的嗎？ | 依設計而定 |
| **algorithmic** | 提出程序、模型、系統或裝置，並證明其在公平比較下表現可靠。 | 在公平比較下表現如何？哪裡會失敗？ | TRIPOD+AI、CONSORT-AI、DECIDE-AI |
| **review** | 綜整某個領域的知識狀態，以論證而非逐篇排列文獻。 | 已知什麼？哪裡有分歧？哪裡還沒有答案？ | PRISMA 2020（系統性）、敘述性回顧無固定準則 |
| **qualitative** | 以訪談、焦點團體、觀察或文本，探索經驗、意義或歷程。 | 參與者的經驗是什麼？研究者如何確保可信賴性？ | COREQ、SRQR |
| **mixed-methods** | 在同一研究中整合量性與質性資料，並說明整合的邏輯與時點。 | 兩種資料如何互補？整合產生了什麼單一資料看不到的理解？ | GRAMMS、O'Cathain 等的 MMAT 面向 |
| **dbr** | 設計本位研究（Design-Based Research）：在真實情境中反覆設計、實施、評估與修正一個教育或系統介入，同時產出設計原則與理論貢獻。 | 每一輪迭代改變了什麼？設計原則是什麼？理論貢獻在哪裡？ | 無正式 EQUATOR 準則；見 `health-research-compliance.md` 的 DBR 報告要素 |
| **scoping-review** | 範疇性文獻回顧：以 JBI 方法系統性地描繪某主題的證據範圍、概念與缺口，不做效果合成。 | 這個領域有哪些證據？用了哪些概念與方法？缺口在哪裡？ | PRISMA-ScR、JBI 2020 |
| **quality-improvement** | 品質改善或實務改善專案：在單一單位或機構以 PDSA 等循環改善流程或結果指標。 | 改善了什麼？在什麼脈絡下？能不能持續？ | SQUIRE 2.0 |

## 判別規則

- 使用者指定類型時，直接採用。
- 使用者說「設計本位研究」「DBR」「迭代」「設計原則」「V1 到 V7」 → **dbr**。
- 資料主要來自訪談、放聲思考、焦點團體、開放式回應，且分析方法為主題分析、內容分析、紮根理論、現象學等 → **qualitative**。
- 同一研究同時有量性資料（問卷、量表、系統日誌）與質性資料（訪談、放聲思考），且作者明確說明整合方式 → **mixed-methods**。若只是「順便問了幾題開放式問題」而無整合設計，仍歸 research 或 qualitative。
- 明確使用 JBI 或 Arksey & O'Malley 框架、有 PCC、不做統合分析 → **scoping-review**；有效果量合成或 GRADE → **review**（並轉交 `prisma-2020-master`）。
- 以 PDSA、Lean、根本原因分析改善單位流程或指標，無對照組或隨機化 → **quality-improvement**。
- 提出新量表或翻譯量表並報告信效度 → **methods**。
- 提出系統、模型、聊天機器人、預測模型並報告效能比較 → **algorithmic**；若主要貢獻是「在真實教學情境中迭代設計」而非效能比較，改為 **dbr**。
- 有明確的機制假設並設計證據去驗證或排除 → **hypothesis**。
- 綜整既有文獻而無新初級資料 → **review**。
- 其餘 → **research**（預設）。

## 複合型論文的處理

一篇論文常同時符合兩型。處理原則：

1. 以**主要論證結構**決定 `paper_type`，不以資料種類決定。例如使用者的碩士論文「結合生成式 AI 與 RAG 的專科護理師臨床推理學習系統」：主要論證是 DBR 的迭代設計與設計原則，雖然含系統效能與 SUS 分數，仍以 **dbr** 為主，**mixed-methods** 為副。
2. 副類型的報告準則仍要套用。DBR 為主、含質性訪談的論文，質性部分仍要對照 COREQ 或 SRQR 的要素。
3. 在 `bob-writing` 的 fragments 中，主類型決定章節骨架，副類型只提供補充檢核表。

## 與碩士論文章節的對應

| 類型 | 第三章（方法）常見小節 | 第四章（結果）常見組織方式 |
|---|---|---|
| research | 研究設計、研究對象、研究工具、資料收集、資料分析、倫理考量 | 描述統計 → 推論統計，依研究問題順序 |
| qualitative | 研究設計、研究參與者、資料收集、資料分析、嚴謹性、倫理考量 | 依主題（themes）組織，附引文 |
| mixed-methods | 上述兩者加「整合策略」小節 | 先分後合，或依研究問題交錯 |
| dbr | 研究設計（DBR 階段圖）、研究場域與參與者、系統設計、各迭代的資料收集與分析、倫理考量 | 依迭代輪次或依 DBR 階段組織，每輪含「設計 → 實施 → 評估 → 修正」 |
| scoping-review | 依 JBI：PCC、納入排除、檢索策略、篩選、資料萃取、綜整方式 | PRISMA-ScR 流程圖 → 文獻特性表 → 依概念或主題綜整 |

## 舊詞彙對應

上游有些較長的分類（mechanism / method / resource / device / model / clinical / materials / computational / interdisciplinary），對應方式：

- mechanism、clinical、materials → **research** 或 **hypothesis**（視是否以因果主張為中心）
- method → **methods**
- model、device、computational → **algorithmic**
- resource → 通常為 **methods**（資料集或題庫論文）或 **research**
- interdisciplinary → 依主要論證結構決定，不以領域標籤決定

## 交接規則

- **概念分析**（Walker & Avant）不在本分類中，直接轉交 `concept-analysis-master`。
- **系統性回顧含統合分析**轉交 `prisma-2020-master`。
- **範疇性回顧**的方法設計與全文撰寫轉交 `scoping-review-master`；bob-* 只在潤飾、審稿、引文驗證時使用本分類。
- **混合方法的研究設計問題**（不是寫法問題）轉交 `mixed-methods-research`。
