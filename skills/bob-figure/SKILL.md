---
name: bob-figure
description: >-
  規劃、繪製、稽核與匯出研究論文用的資料圖與示意圖，支援 Python（matplotlib／seaborn）或 R（ggplot2／patchwork／ComplexHeatmap），
  兩種交付目標：期刊投稿級（向量 PDF／SVG）與碩論 Word 插圖（300 dpi PNG／TIFF、中文字型）。
  Create, revise, audit, and export publication-grade research figures in Python or R for journal submission or a Word thesis.
  觸發詞：畫圖、論文圖、投稿圖、碩論插圖、多面板圖、matplotlib、ggplot、圖說、300 dpi、示意圖、研究架構圖、流程圖、
  圖表美化、匯出 PDF、SVG、TIFF、a/b/c 面板、對齊子圖、色盲友善配色。
  不用於互動式儀表板、純統計分析、資料清理、簡報投影片、純照片修圖。
---

# bob-figure：研究圖件路由器

本 skill 分成兩層：

- **靜態層**（`static/`）：版本化的可重用片段，包括圖件契約與預設立場（`static/core/`）、依交付目標分的規格片段（`static/fragments/target/`）、依繪圖後端分的快速起手式（`static/fragments/backend/`）。
- **動態層**（本檔加 `manifest.yaml`）：判斷交付目標與繪圖後端，只載入本次任務需要的片段。深度設計、API、版型與 QA 材料放在 `references/`，按需載入。

不要憑記憶或只憑本檔套用圖件邏輯，一律照下面的步驟從磁碟載入片段。

## 路由流程

每次被觸發都依序執行。

### 0. 判斷是否為 AI 示意圖路徑（選用，預設不走）

只有當使用者**明確**要求用 OpenRouter、GPT Image 或其他影像生成 API 產生圖形摘要、機制示意圖、概念圖草稿時，才進入此路徑；一般的「研究架構圖」「流程圖」「示意圖」預設仍用 Python／R 繪製（matplotlib patches、graphviz 產出的向量圖，或 R 的 DiagrammeR／ggplot），不主動建議走 AI 生圖。

若確實進入 AI 示意圖路徑：

1. 讀 `manifest.yaml` 與 `always_load` 檔案。
2. 讀 `references/ai-graphical-abstract-workflow.md`（訊息簡報、構圖、期刊政策、人工核驗、揭露與來源紀錄）。
3. 讀 `references/openrouter-image-generation.md`，需要真正呼叫 API 時用 `scripts/generate_openrouter_schematic.py`。
4. 產出一律視為草稿，不是定量資料圖；不得捏造數值、機構標誌或未經證實的機制。投稿前要另外查核目標期刊對 AI 生成圖像的最新政策（以期刊官網為準，並記錄查核日期）。
5. 此路徑不問 Python／R。

其餘繪圖、製圖、多面板組圖、圖件稽核與匯出任務，繼續往下。

### 1. 載入 manifest 與核心層

讀 `manifest.yaml`，它宣告 `target` 與 `backend` 兩個軸、允許值與對應的片段路徑。

同時讀 `always_load` 列出的每個檔案（`static/core/contract.md`、`static/core/stance.md`）。這兩份含圖件契約、後端閘門、缺少執行環境時的規則、隱私規則與預設操作立場，適用於每一個圖件任務。

### 2. 決定交付目標（`target`）

| 值 | 何時使用 | 片段 |
|---|---|---|
| `journal` | 期刊投稿、投稿修訂、審查回覆附圖、海報或英文稿件中的圖 | `static/fragments/target/journal.md` |
| `thesis-word` | 碩士論文、計畫書、口試簡報附圖、任何最終要貼進 Word 的中文圖 | `static/fragments/target/thesis-word.md` |

判斷線索：提到「碩論」「論文第三章」「圖 3-1」「Word」「口試」「所辦格式」「標楷體」走 `thesis-word`；提到「投稿」「期刊」「reviewer」「JAN」「JMIR」「護理雜誌」「雙欄寬」走 `journal`。都沒提時預設 `journal`，並在交付時提醒可以再產一份 `thesis-word` 版本（通常只需改字型、尺寸與匯出格式，不重畫）。同一張圖要兩種版本時，先完成一種，再以同一份繪圖程式碼切換片段匯出第二種。

當 `target` 為 `thesis-word` 且需要中文學術慣例（全形標點、圖表編號、標楷體）時，另載入 `../bob-shared/core/zh-tw-academic-conventions.md`；需要國防醫學院碩論圖表樣式時載入 `../bob-shared/journal-formats/ndmc-thesis.md`。

### 3. 決定繪圖後端（`backend`，一次詢問並記住）

後端選擇只適用於「要寫或改繪圖程式碼」的任務。同一任務與其後續訊息沿用已決定的後端，不因新訊息沒提語言就再問。純檢視圖片、與後端無關的資料檢查可以先做。決定順序：

1. 使用者本次明確指定 Python 或 R，用該後端並以 `python scripts/bob_figure_backend.py set python` 或 `set r` 存為預設。
2. 使用者提供的檔案或流程明顯屬於某一語言（例如 `.R` 腳本、`ggplot` 程式碼、`.ipynb`），用該後端並存檔。
3. 否則沿用本任務已建立的選擇；沒有的話執行 `python scripts/bob_figure_backend.py get`，回傳 `python` 或 `r` 就直接用。
4. 以上都沒有時，只問一句：**「用 Python 還是 R？我會記住當作你的預設。」** 然後暫停依賴後端的步驟，等使用者回答後先存檔再繼續。

- `python`：matplotlib／seaborn。
- `r`：ggplot2／patchwork／ComplexHeatmap。

不要憑美感替使用者決定後端。只有使用者明確要你推薦時，才依 `references/backend-selection.md` 說明理由、存檔、繼續。一旦選定，該後端對所有繪圖、預覽、匯出與視覺 QA **獨占**（見 `static/core/contract.md`），不得用另一種語言補畫預覽或替代匯出。

偏好檔預設位置 `~/.config/bob-research-skills/bob-figure.json`，可用環境變數 `BOB_FIGURE_CONFIG` 覆寫。

### 4. 載入對應片段

依序讀 `target` 片段（`journal.md` 或 `thesis-word.md`）與 `backend` 片段（`static/fragments/backend/python.md` 或 `r.md`）。**不要**載入另一個後端的片段。目標片段規定尺寸、解析度、字型、格式與圖說慣例；後端片段規定該語言的執行規則與出版級快速起手式。兩者衝突時以目標片段為準（例如 `thesis-word` 的中文字型設定覆蓋後端片段的 Arial 預設）。

### 5. 用載入的材料建圖

依這個順序套用：

1. **圖件契約**（`core/contract.md`）：先寫下這張圖要證明的一句話結論、證據鏈、原型分類、目標與匯出契約，再寫程式碼。
2. **多面板證據架構**：規劃、重組或稽核有 a/b/c 標籤的多面板圖時，載入 `references/multipanel-evidence-architecture.md`。一張圖回答一個結果層級的研究問題；每個面板承擔不同推論角色，不是同一結果換指標重畫。圖的順序要跟著論文論證走時，另載入 `../bob-shared/core/results-discussion-escalation.md`。
3. **預設立場**（`core/stance.md`）：原型優先、主面板加從屬面板、克制配色、統計與資料完整性是圖的一部分。
4. **目標片段與後端片段**：本次選定的規格與執行規則。
5. **模板改編**：重用內建範例、第三方素材或使用者自己的繪圖程式碼前，載入 `references/asset-adaptation.md`。
6. **渲染 QA 與交付前檢查**：載入 `references/qa-contract.md`。對每張多面板圖執行渲染時對齊閘門，對繪圖原始碼跑 `scripts/validate_figure.py`，對匯出的 PDF 跑 `scripts/audit_pdf_text.py` 與 `scripts/audit_figure_collisions.py`，最後以最終實體尺寸逐面板檢視。自動檢查不取代逐面板的不確定性、顯著性、間距與歧義稽核。

#### 多面板對齊閘門

兩個以上可比較面板的圖，在匯出前量測**最終渲染的繪圖區矩形**並保留對齊 JSON。Python 在最終版面繪製後呼叫 `scripts/audit_panel_alignment.py` 的 `require_matplotlib_panel_alignment()`；R／patchwork 先 `source("scripts/panel_alignment.R")`，以最終匯出尺寸寫出版面 manifest，再跑同一支後端中立的 JSON 稽核器。共用邊、寬、高、面板標籤錨點與重複溝槽的預設容差為 `1.5 pt`。`FIX BEFORE DELIVERY` 或 exit code `1` 阻擋匯出；`NOT AUDITABLE` 或 exit code `2` 阻擋任何「對齊已通過」的宣稱。橫排三或四個等跨度面板必須等寬等高等溝槽；刻意不等寬要記錄 `panel-width` 豁免與理由。巢狀網格、自由定位的主面板、inset 與 colorbar 只能透過明確的可比較群組或帶理由的豁免排除；不要放寬全域容差來掩蓋單一例外。

#### 碰撞稽核

每次產生或修改 Python／R 圖之後（資料幾何、文字、字型、圖例、註記、座標軸、誤差線、面板尺寸或版面任何一項改動，不只最終投稿），匯出最終 PDF 並重跑：

```bash
python skills/bob-figure/scripts/audit_figure_collisions.py figure.pdf \
  --json-out figure.collision-audit.json \
  --overlay-pdf figure.collision-audit.pdf
```

- `FIX BEFORE DELIVERY` 或 exit code `1`：修圖、用選定後端重新匯出、重跑全部渲染 QA。
- `REVIEW REQUIRED`：以最終實體尺寸逐一檢視 WARN，記錄為何刻意疊圖可接受；WARN 也要阻擋時加 `--strict`。
- `NOT AUDITABLE` 或 exit code `2`：回報相依套件或 PDF 的阻礙，不宣稱已完成碰撞驗證；缺 PyMuPDF 時安裝 `requirements.txt`。

碰撞稽核只讀 PDF 幾何，不重畫圖，也不授權跨後端繪圖；帶標記的 PDF 是 QA 診斷品，不能取代選定後端的原始檔或交付檔。

`thesis-word` 目標的 PNG／TIFF 交付檔，仍先匯出一份 PDF 供上述稽核，再由同一後端匯出點陣檔；不要只憑 PNG 目視。

圖服務於研究邏輯；美化、版型與複雜排版都從屬於「讓核心結論清楚、可辯護、可審查」。

### 6. 只在需要時開 references

`references/` 是深度參考，不是預設載入。依 manifest 的 `references.on_demand` 表按需開啟：`figure-contract.md` 建契約；`multipanel-evidence-architecture.md` 決定面板角色與圖序；`asset-adaptation.md` 安全重用模板；`template-catalog.md` 已驗證的 Python CSV 模板；`api.md` Python 調色盤與版面安全 helper；`r-workflow.md` R 流程；`design-theory.md` 色彩、字型與匯出原理；`common-patterns.md`、`chart-types.md` 版型與圖型配方；`figure-legend-conventions.md` 圖說寫法；`qa-contract.md` 交付前檢查；`tutorials.md`、`demos.md` 完整範例。`references/nature-article-requirements.md` 與 `references/nature-2026-observations.md` 只在投稿目標確實是 Nature 系列時才開，不是本 skill 的預設。

凡寫到具體期刊的尺寸、圖數、圖說字數，以期刊官網為準並標註查核日期；不憑記憶給硬數字。

## 分工邊界

| 情境 | 交給 | 本 skill 的角色 |
|---|---|---|
| 圖上要標的 p 值、效果量、信賴區間、SUS 分數如何計算與詮釋 | `bob-statistics` | 只負責把已確認的統計數字放進圖與圖說，不重算、不補檢定 |
| 把完成的圖插入 Word 論文、設定圖說樣式、更新圖目錄 | `docx` | 交付符合 `thesis-word` 規格的圖檔與圖說文字 |
| 要做成口試或課堂簡報 | `grad-lecture-to-slides`（或 `pptx`） | 提供高解析圖檔；不做簡報版面 |
| 圖的結論要寫回結果或討論段 | `bob-writing` | 提供圖件契約中的一句話結論與證據鏈 |
| 圖說要潤成期刊英文或學術中文 | `bob-polishing` | 提供符合 `figure-legend-conventions.md` 的初稿 |
| 用 AI 生成概念示意圖草稿 | 本 skill 第 0 步的選用路徑 | 只在使用者明確要求時走，產出標為草稿 |

## 為什麼這樣拆

- 靜態層可版本化、可審閱；目標與後端的閘門寫在 manifest，不藏在散文裡。
- 每次呼叫只載入一個目標片段與一個後端片段，兩千多行的參考深度只在需要的步驟進入上下文。
- 路由器刻意保持簡短；擴充範圍時更新片段與 references，不改本檔。
