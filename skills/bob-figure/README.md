# bob-figure：研究圖件

把資料、圖說草稿或論文結論做成可投稿或可貼進碩論 Word 的圖，支援 Python（matplotlib／seaborn）與 R（ggplot2／patchwork／ComplexHeatmap）。改造自上游 nature-skills 的圖件 skill（來源與逐檔異動見 `UPSTREAM.md`），去掉 Nature 系列預設，改為「期刊投稿級」與「碩論 Word 插圖」兩種交付目標。

## 用途

- 從資料或現有圖產生 Python／R 繪圖腳本與可編輯圖檔（PDF／SVG／PNG／TIFF）。
- 依「一張圖回答一個結果層級的研究問題」規劃多面板圖，讓各面板承擔主證據、對照、驗證、機制等不同推論角色。
- 畫研究架構圖、流程圖（例如 DBR 迭代流程、RAG 系統架構、Tanner 臨床判斷模型對應圖）與示意圖；AI 生圖路徑只在使用者明確要求時走，且標為草稿。
- 稽核面板標籤、配色與視覺層級、誤差線、最終 PDF 字級、統計註記、資料來源與匯出格式；多面板圖自動檢查對齊（1.5 pt 容差）與文字碰撞。
- 兩種交付目標：
  - `journal`：向量 PDF／SVG、Arial／Helvetica、色盲友善配色、尺寸與圖說字數以期刊官網為準並記錄查核日期。
  - `thesis-word`：300 dpi PNG／TIFF、寬度不超過 16 cm、標楷體或 Noto Sans TC、單色可讀、圖說在下表題在上、「圖 3-1」編號、插入 Word 後不縮放。

## 觸發語

畫圖、論文圖、投稿圖、碩論插圖、多面板圖、matplotlib、ggplot、圖說、300 dpi、示意圖、研究架構圖、流程圖、圖表美化、匯出 PDF／SVG／TIFF、a/b/c 面板、對齊子圖、色盲友善配色。

不觸發：互動式儀表板、純統計分析、資料清理、簡報投影片、純照片修圖。

## 工作方式

1. 判斷交付目標（`journal` 或 `thesis-word`，預設 `journal`）。
2. 決定繪圖後端：第一次問「用 Python 還是 R？」並記住（`scripts/bob_figure_backend.py`，偏好檔 `~/.config/bob-research-skills/bob-figure.json`），之後不再問；選定後該後端獨占繪圖、預覽、匯出與 QA。
3. 寫圖件契約：一句話結論、證據鏈、原型、目標與匯出契約。
4. 繪圖、渲染時對齊閘門、PDF 字級與碰撞稽核、最終尺寸逐面板檢視。
5. 交付圖檔、圖說文字、資料來源與排除紀錄、稽核 JSON。

## 範例提示詞

1. 「這是 30 位專科護理師學生在 V3 與 V5 兩個版本的 SUS 分數（CSV 附上），幫我畫一張碩論第四章用的成對比較圖，標楷體、300 dpi、寬 14 cm，圖說用『圖 4-3』格式。統計數字我已經用 bob-statistics 算好：*t*(29) = 3.21, *p* = .003。」
2. 「用 Python 畫我的研究架構圖：左邊 Tanner 臨床判斷模型四階段，中間 RAG 臨床推理學習系統，右邊 LQQOPERA 問診框架，要能貼進 Word 且黑白列印看得清楚。」
3. 「我要投 JMIR Medical Education，把系統日誌的 token 成本與每輪迭代（V1 到 V7）的回應正確率畫成雙面板圖，向量 PDF、色盲友善，圖說寫英文；期刊的圖寬規定請幫我列出要去官網查的項目。」

## 你需要提供

- 原始資料、現有圖、圖說或想表達的結論。
- 交付目標（期刊名稱或碩論章節）、需要的格式與尺寸。
- Python／R 偏好；沒有的話第一次會問一次並記住。

## 分工表

| 情境 | 交給 | bob-figure 做什麼 |
|---|---|---|
| 圖上的 p 值、效果量、CI、SUS 分數怎麼算與怎麼詮釋 | `bob-statistics` | 只放已確認的數字進圖與圖說 |
| 把圖插入 Word、套圖說樣式、更新圖目錄 | `docx` | 交付 `thesis-word` 規格的圖檔與圖說文字 |
| 做成口試或課堂簡報 | `grad-lecture-to-slides`／`pptx` | 提供高解析圖檔 |
| 圖的結論寫回結果與討論 | `bob-writing` | 提供圖件契約的一句話結論與證據鏈 |
| 圖說英文潤稿或學術中文潤稿 | `bob-polishing` | 提供符合圖說慣例的初稿 |
| 圖件的 APA 7 引用或授權標註 | `apa7-master` | 提供需要標註的來源 |
| 單篇論文的圖要拿來讀懂 | `paper-analysis` | 不做 |

## 相依套件

碰撞稽核需要 PyMuPDF：

```bash
python -m pip install -r skills/bob-figure/requirements.txt
```

## 內建材料

- `static/core/`：圖件契約與預設立場（每次載入）。
- `static/fragments/target/`：`journal.md`、`thesis-word.md`。
- `static/fragments/backend/`：`python.md`、`r.md`。
- `references/`：契約、多面板架構、模板改編、QA、API、版型、圖說、R 流程等深度參考（英文保留）。`nature-article-requirements.md` 與 `nature-2026-observations.md` 只在投稿 Nature 系列時開啟。
- `scripts/`：`bob_figure_backend.py`（後端偏好）、`validate_figure.py`、`audit_pdf_text.py`、`audit_panel_alignment.py`、`panel_alignment.R`、`audit_figure_collisions.py`、`figure_safety.py`、`plot_templates.py`、`generate_openrouter_schematic.py`（選用）。
- `assets/`：圖型 atlas、範例圖庫、第三方 figures4papers 參考腳本（版權見 `assets/figures4papers/THIRD_PARTY_NOTICES.md`）。

## 邊界

- 不把 AI 生成圖當作真實資料圖；不捏造統計檢定、樣本數或誤差線定義。
- 不為了渲染方便靜默抽樣或刪除觀測值。
- 自動稽核通過不等於視覺驗收；最終仍逐面板檢查。
- 不憑記憶寫死期刊的尺寸、圖數、字數；一律標「以期刊官網為準，查核日期」。
- 不在回覆中暴露私有模板路徑或檔名。
