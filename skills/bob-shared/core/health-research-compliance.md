# 健康科學研究的合規路由（Health research compliance）

當稿件涉及人體研究、臨床或教育介入、AI 系統、問卷調查、質性訪談或文獻回顧時使用的條件式參考。它是**投稿與口試前的準備度篩檢**，不是法律、臨床或倫理委員會的意見。供 `bob-writing`、`bob-reviewer`、`bob-statistics`、`bob-response` 依需要載入。

## 目錄

1. 適用性閘門
2. IRB、知情同意與個資保護（台灣語境）
3. EQUATOR 準則路由表
4. 各準則的關鍵報告要素
5. 設計本位研究（DBR）的報告要素
6. 生成式 AI 的兩種角色與揭露
7. 資料與程式碼可用性
8. 審核輸出格式
9. 官方來源

## 1. 適用性閘門

把每一個項目分類為 `required`、`not applicable` 或 `AUTHOR_INPUT_NEEDED`。**絕對不要推測**核准、同意、登錄、豁免、編號或日期。

只打開相關的區塊。不要用臨床試驗的要求去審一篇範疇性回顧，也不要用 COREQ 去審一篇純量性的橫斷研究。一篇論文可能同時適用兩個以上的準則（例如 DBR 主體加 COREQ 的訪談部分，或 CONSORT-EHEALTH 加 CHERRIES 的線上問卷）。

## 2. IRB、知情同意與個資保護（台灣語境）

檢查稿件的方法段或方法章是否陳述：

- 審查單位名稱與核准編號（例如「本研究經三軍總醫院人體試驗審議委員會審查通過，編號 ______」）；若為免審或簡易審查，說明依據
- 知情同意的取得方式（書面、線上、口頭錄音）與時點；是否有撤回機制
- 若參與者為學生、下屬或病人，如何確保自願性、避免權力關係影響（例如由非授課教師招募、不影響成績）
- 個資的去識別化、保存方式、保存期限與銷毀，對應《個人資料保護法》與《人體研究法》
- 若研究使用 AI 系統：參與者輸入的內容是否傳送到第三方服務（例如雲端 LLM API）、是否含病人可識別資料、是否已去識別化或使用虛擬個案
- 若有錄音、錄影、螢幕錄製或系統日誌：參與者是否知情並同意
- 補償或誘因（禮券等）的說明
- 前瞻性介入試驗的登錄號（ClinicalTrials.gov 或其他 WHO 認可登錄平台），並在摘要與方法段都寫出

期刊常要求的聲明段落（Ethics approval、Consent to participate、Consent for publication、Availability of data、Competing interests、Funding、Authors' contributions）依目標期刊的清單逐一確認；缺少即標 `AUTHOR_INPUT_NEEDED`。

## 3. EQUATOR 準則路由表

依研究設計選擇準則；再由對應的既有 skill 執行逐項檢核。不確定時先呼叫 `equator-guideline-finder`。

| 研究設計 | 準則 | 對應 skill | 備註 |
|---|---|---|---|
| 隨機對照試驗 | CONSORT 2025 | `consort-2025-master` | 教育介入若有隨機分派亦適用；群集隨機用 cluster 延伸 |
| 非隨機介入（類實驗、前後測） | TREND | `equator-guideline-finder` | 無專用 skill；以 TREND 清單逐項檢核 |
| 觀察性研究（橫斷、世代、病例對照） | STROBE | `strobe-v4-master` | 問卷調查式的橫斷研究亦適用 |
| 系統性回顧與統合分析 | PRISMA 2020 | `prisma-2020-master` | 含 PRISMA-S 檢索報告 |
| 範疇性回顧 | PRISMA-ScR、JBI 2020 | `scoping-review-master` | 不做效果合成 |
| 質性研究（訪談、焦點團體） | COREQ 或 SRQR | `equator-guideline-finder` | COREQ 適用訪談與焦點團體；SRQR 較通用 |
| 混合方法研究 | GRAMMS；MMAT 面向 | `mixed-methods-research`（設計）、`equator-guideline-finder`（報告） | 需說明整合時點與方式 |
| 線上問卷調查 | CHERRIES | `equator-guideline-finder` | 回覆率、去重、資料完整性 |
| 網路或行動裝置介入 | CONSORT-EHEALTH | `equator-guideline-finder`；投 JMIR 時另見 `../journal-formats/jmir.md` | 介入描述要到可複製 |
| 介入描述（任何設計） | TIDieR | `equator-guideline-finder` | 12 項介入描述，教育介入格外重要 |
| 預測模型或 AI 模型 | TRIPOD+AI | `equator-guideline-finder` | 開發與驗證分開報告 |
| AI 介入的臨床試驗 | CONSORT-AI、SPIRIT-AI | `consort-2025-master` 加 AI 延伸 | |
| AI 早期臨床評估 | DECIDE-AI | `equator-guideline-finder` | 適用原型系統在真實情境的早期評估 |
| 量表發展與心理計量 | COSMIN | `equator-guideline-finder` | 信度、效度、反應性 |
| 品質改善專案 | SQUIRE 2.0 | `nursing-project-reviewer`（護理專案）或 `equator-guideline-finder` | |
| 個案報告 | CARE | `np-case-report` | |
| 診斷準確性研究 | STARD | `equator-guideline-finder` | |
| 設計本位研究（DBR） | 無正式 EQUATOR 準則 | 見本檔第 5 節 | 副類型（質性、問卷、系統）仍套用對應準則 |
| 德菲法 | ACCORD 或 CREDES | `equator-guideline-finder` | |
| 經濟評估 | CHEERS 2022 | `equator-guideline-finder` | token 成本分析若上升為成本效益分析時考慮 |

準則版本會更新；在稿件中引用準則時寫出版本與年份，並以 EQUATOR Network 官網為準。

## 4. 各準則的關鍵報告要素

以下只列審稿與口試最常抓的項目，完整清單由對應 skill 提供。

- **CONSORT 2025：** 流程圖（納入、分派、追蹤、分析人數）、隨機方法與分派隱匿、盲法、樣本數估算、主要與次要結果的預先定義、傷害事件、試驗登錄號、計畫書取得方式。
- **STROBE：** 研究設計在標題或摘要中明示、場域與期間、參與者的納入排除與來源、變項定義、偏誤處理、樣本數依據、統計方法（含遺漏值處理）、參與者流程、未調整與調整後的估計值與 CI。
- **COREQ：** 研究團隊（訪談者背景、與參與者的關係）、方法論取向、取樣與人數、飽和、訪談指引、錄音與逐字稿、編碼者人數、編碼樹、參與者回饋、引文標示、主題與資料的一致性。
- **SRQR：** 研究者反身性、取樣策略的理由、資料收集工具的變動、資料處理與分析的透明、可信賴性技術（三角檢證、成員檢核、稽核軌跡）。
- **CHERRIES：** 問卷發展與預試、平台、開放或封閉調查、聯繫方式、廣告、回應率的定義與計算、去重與 cookie、完成率、資料驗證。
- **CONSORT-EHEALTH：** 介入的技術細節（平台、版本、人機互動）、使用者訓練、使用量與依從性資料（系統日誌）、對照組的說明、退出與技術問題。
- **TRIPOD+AI：** 資料來源與時間、結果定義、預測變項處理、樣本數、遺漏值、模型類型與超參數、評估集與訓練集的分離、校準與區辨力、公平性分析、模型可用性。
- **PRISMA-ScR：** 計畫書登錄（OSF 等）、PCC、資訊來源與檢索策略全文（附錄）、篩選流程與人數、資料萃取表、綜整方式、結果依概念呈現、限制含證據品質未評估的說明。
- **TIDieR：** 介入名稱、理由、材料、程序、提供者、方式、地點、時間與劑量、調整、依從性。

## 5. 設計本位研究（DBR）的報告要素

DBR 沒有正式的 EQUATOR 準則。以下要素整理自 DBR 方法論文獻（例如 Design-Based Research Collective, 2003；McKenney & Reeves 的通用模型；Anderson & Shattuck, 2012 的檢核）常見的期待，供審稿與口試準備。**這是整理，不是官方清單**，撰寫時應引用原始方法論文獻。

| 要素 | 要說清楚的內容 |
|---|---|
| 真實情境 | 場域（課程、單位、學程）、參與者角色（學員、教師、臨床導師）、研究者在情境中的角色與反身性 |
| 理論框架 | 指導設計的理論（例如 Tanner 臨床判斷模型）如何轉譯為設計決策；問診框架（LQQOPERA）如何嵌入 |
| 迭代結構 | 幾輪、每輪的時間、每輪的參與者人數、每輪的設計目標；版本（V1 到 V7）與迭代輪次的對應表 |
| 每輪的資料 | 各輪收集了哪些量性（SUS、自編問卷、系統日誌、token 成本）與質性（放聲思考、半結構式訪談）資料，以及各自回答哪個研究問題 |
| 設計決策軌跡 | 每輪的證據如何導致下一輪的具體修改；用表格呈現「發現 → 設計修改 → 理論依據」 |
| 設計原則 | 研究最終產出的、可遷移的設計原則，與證據的對應 |
| 理論貢獻 | 對指導理論的支持、修正或延伸 |
| 混合方法整合 | 若同時有量性與質性資料，整合的時點與方式（見 GRAMMS） |
| 品質準則 | 可信賴性（質性部分）、信效度（量性工具）、迭代之間的一致性、研究者偏誤的控制 |
| 限制 | 單一場域、研究者兼設計者、樣本小、無對照組、短期成效 |
| 倫理 | 學生參與的自願性；AI 系統的資料流向；虛擬個案而非真實病人資料 |

DBR 論文中的 AI 系統若有效能評估（回答正確率、幻覺率、檢索命中率），該部分另對照 TRIPOD+AI 或 DECIDE-AI 的相關項目；訪談部分對照 COREQ；問卷部分若為線上施測對照 CHERRIES。

## 6. 生成式 AI 的兩種角色與揭露

分清楚並在方法段分別描述：

1. **作為研究介入或研究對象的 AI**（例如 RAG 學習系統）：模型名稱與版本、供應商、提示詞設計、知識庫來源與更新日期、檢索方式、安全機制、資料流向、成本；評估方式與評估集的獨立性；洩漏風險（評估題目是否在知識庫或訓練資料中）。
2. **作為寫作或分析輔助的 AI**：工具、版本、用途（潤飾、翻譯、編碼建議）、人類驗證方式；依目標期刊政策決定放在 Methods、Acknowledgements 或 Declarations。AI 不得列為作者。

紅黃綠燈框架見 `ethics.md`。

## 7. 資料與程式碼可用性

- 多數健康科學期刊要求 Data Availability statement。人體研究資料若因倫理限制無法公開，要說明限制與取得程序，不要只寫「available upon request」而不說明條件。
- 自製系統或分析程式碼若為結論核心，說明取得方式（GitHub、OSF、Zenodo）與授權；不能公開時說明原因。
- 問卷或量表若為自編，附在附錄或補充資料；使用他人量表要說明授權取得。
- 不得捏造儲存庫網址、DOI 或授權條款。

## 8. 審核輸出格式

回傳精簡表格：

| 要求 | 適用？ | 稿件或檔案中的證據 | 狀態 | 需要的行動 |
|---|---|---|---|---|

狀態用 `ok`、`blocked`、`AUTHOR_INPUT_NEEDED`。缺少 IRB 編號、同意程序、試驗登錄、必要的準則項目、資料可用性聲明時用 `blocked`。適用性或行政事實未知時用 `AUTHOR_INPUT_NEEDED`。

## 9. 官方來源

以下網址為準則的入口，內容以官網現行版本為準（查核日期由使用者在投稿時更新）：

- EQUATOR Network：<https://www.equator-network.org/>
- ICMJE Recommendations：<https://www.icmje.org/recommendations/>
- CONSORT：<https://www.consort-statement.org/>
- STROBE：<https://www.strobe-statement.org/>
- PRISMA：<https://www.prisma-statement.org/>
- JBI Manual for Evidence Synthesis：<https://jbi-global-wiki.refined.site/>
- TRIPOD：<https://www.tripod-statement.org/>
- 台灣《人體研究法》、《個人資料保護法》：<https://law.moj.gov.tw/>
- 衛生福利部人體研究倫理相關公告：<https://www.mohw.gov.tw/>
