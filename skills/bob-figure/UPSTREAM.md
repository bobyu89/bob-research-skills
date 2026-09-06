# UPSTREAM：bob-figure 的上游來源與逐檔異動

- 上游 repo：nature-skills（袁一哲等，Apache-2.0）
- 上游穩定副本：`C:\Users\USER\ai-skills\nature-skills\skills\nature-figure\`
- 上游 commit：`28150f30f8b4017991fca8c7b2839f02c6586d2f`（2026-09-06）
- 上游 skill 名稱：`nature-figure`（僅在本檔出現）
- 改造日期：2026-09-06
- 改造規格：`ADAPTATION-SPEC.md` 第 2、3、4、5、6（bob-figure）、7 節

上游 126 檔 → 刪 2 檔（`agents/openai.yaml`、`README_EN.md`）→ 新增 2 檔（`static/fragments/target/journal.md`、`thesis-word.md`）→ 本 skill 126 檔（含本檔則 127 檔；`UPSTREAM.md` 為新增）。

## 逐檔清單

狀態說明：**保留** = 內容與上游逐位元相同；**改寫** = 重寫或大幅修改；**微改** = 只改路徑字串、skill 名稱或簡繁轉換，其餘不動；**新增**；**刪除**；**改名**。

### 根目錄

| 檔案 | 狀態 | 說明 |
|---|---|---|
| `SKILL.md` | 改寫 | 繁中 router；frontmatter `name: bob-figure`，觸發詞繁中；新增 `target` 軸（journal／thesis-word）；去 Nature／NMI 預設；OpenRouter AI 示意圖路徑標為選用且預設不走；`../nature-shared/` 改 `../bob-shared/`；新增分工邊界段 |
| `manifest.yaml` | 改寫 | 新增 `target` 軸（預設 journal，detect 繁中）；`backend` 軸 detect 繁中；`preference` 改指 `scripts/bob_figure_backend.py`、`BOB_FIGURE_CONFIG`、`~/.config/bob-research-skills/bob-figure.json`；刪除指向 nature-shared NMI 的 on_demand 項；新增 `shared` 區塊只引用 bob-shared 清單內檔案；Nature 專屬 references 標為非預設 |
| `README.md` | 改寫 | 繁中：用途、觸發語、3 個台灣情境範例提示詞、分工表、相依套件、邊界 |
| `README_EN.md` | 刪除 | 規格第 3 節 |
| `UPSTREAM.md` | 新增 | 本檔 |
| `.gitignore` | 保留 | |
| `requirements.txt` | 保留 | PyMuPDF |
| `agents/openai.yaml` | 刪除 | 規格第 3 節 |
| `evals/evals.json` | 微改 | `skill_name` 與句中的 skill 名稱改為 bob-figure；一則簡體提示詞經 s2twp 轉繁；測試情境內容未改 |

### static/

| 檔案 | 狀態 | 說明 |
|---|---|---|
| `static/core/contract.md` | 微改 | 後端腳本名稱改為 `bob_figure_backend.py`；其餘英文原文保留 |
| `static/core/stance.md` | 微改 | 移除 NMI pastel 與 Nature／Science／Cell 為預設投稿目標的敘述，改為護理／醫學教育／數位健康期刊與碩論；Nature 版面參考改為僅在明確投稿 Nature 系列時載入；其餘保留 |
| `static/fragments/backend/python.md` | 保留 | |
| `static/fragments/backend/r.md` | 微改 | `skills/nature-figure/` 路徑改 `skills/bob-figure/`；Nature 參考改為非預設 |
| `static/fragments/target/journal.md` | 新增 | 期刊投稿級：向量 PDF／SVG、欄寬以期刊為準、色盲友善、Arial／Helvetica、圖說字數以期刊為準並標查核日期、期刊查核項目表 |
| `static/fragments/target/thesis-word.md` | 新增 | 碩論 Word 插圖：300 dpi PNG／TIFF、寬 16 cm 內、標楷體或 Noto Sans TC、matplotlib 中文字型與負號設定片段、R showtext 對應、圖說在下表題在上、單色可讀、「圖 3-1」慣例、插入 Word 後不縮放 |

### references/（英文保留）

| 檔案 | 狀態 | 說明 |
|---|---|---|
| `references/ai-graphical-abstract-workflow.md` | 保留 | |
| `references/api.md` | 微改 | 指令範例路徑 `skills/nature-figure/` → `skills/bob-figure/` |
| `references/asset-adaptation.md` | 保留 | |
| `references/backend-selection.md` | 微改 | 後端腳本名稱改為 `bob_figure_backend.py` |
| `references/chart-types.md` | 保留 | |
| `references/common-patterns.md` | 保留 | |
| `references/demos.md` | 保留 | |
| `references/design-theory.md` | 保留 | |
| `references/figure-contract.md` | 保留 | |
| `references/figure-legend-conventions.md` | 微改 | 末段「中文圖注要點」經 s2twp 轉繁，改台灣用語（圖說、現在式、過去式、對應、回顧文章）與全形標點；英文部分保留 |
| `references/multipanel-evidence-architecture.md` | 微改 | `../../nature-shared/core/nature-results-discussion.md` → `../../bob-shared/core/results-discussion-escalation.md` |
| `references/nature-2026-observations.md` | 保留 | 檔名沿用上游；manifest 標為非預設，只在投稿 Nature 系列時載入 |
| `references/nature-article-requirements.md` | 微改 | `../../nature-shared/core/research-compliance.md` → `../../bob-shared/core/health-research-compliance.md`；檔名沿用上游；manifest 標為非預設 |
| `references/openrouter-image-generation.md` | 微改 | 指令範例路徑改 `skills/bob-figure/` |
| `references/qa-contract.md` | 微改 | 指令範例路徑改 `skills/bob-figure/` |
| `references/r-template-index.md` | 保留 | |
| `references/r-workflow.md` | 微改 | `source()` 路徑改 `skills/bob-figure/` |
| `references/template-catalog.md` | 微改 | 指令範例路徑改 `skills/bob-figure/` |
| `references/tutorials.md` | 保留 | |

### scripts/ 與 tests/

| 檔案 | 狀態 | 說明 |
|---|---|---|
| `scripts/nature_figure_backend.py` → `scripts/bob_figure_backend.py` | 改名＋微改 | 上游寫死 `NATURE_FIGURE_CONFIG` 與 `~/.config/nature-skills/nature-figure.json`；改為 `BOB_FIGURE_CONFIG` 與 `~/.config/bob-research-skills/bob-figure.json`，docstring 與錯誤訊息中的名稱同步；邏輯不變。已測試 `get`（未設定回傳 exit 1）、`set python`、`get`、`path`、`clear` 皆正常 |
| `scripts/audit_figure_collisions.py` | 微改 | 安裝提示字串中的 `skills/nature-figure/requirements.txt` → `skills/bob-figure/`；邏輯不變 |
| `scripts/audit_panel_alignment.py` | 保留 | |
| `scripts/audit_pdf_text.py` | 保留 | |
| `scripts/figure_safety.py` | 保留 | |
| `scripts/generate_openrouter_schematic.py` | 保留 | 選用路徑 |
| `scripts/panel_alignment.R` | 微改 | 預設 `audit_script` 路徑改 `skills/bob-figure/` |
| `scripts/plot_templates.py` | 微改 | docstring 中 skill 名稱改 bob-figure |
| `scripts/validate_figure.py` | 保留 | |
| `tests/test_figure_safety.py` | 保留 | 內部模組別名 `nature_figure_*` 不影響執行，未改 |

### assets/（85 檔，全部保留）

| 目錄 | 檔數 | 狀態 |
|---|---|---|
| `assets/chart-atlas/atlas-01…10-*.png` | 10 | 保留 |
| `assets/gallery/fig1…fig5-*-rich.png` | 5 | 保留 |
| `assets/figures4papers/THIRD_PARTY_NOTICES.md` | 1 | 保留（第三方版權聲明） |
| `assets/figures4papers/assets/*.png` | 8 | 保留 |
| `assets/figures4papers/figure_CellSpliceNet/`（3 py + 4 png） | 7 | 保留 |
| `assets/figures4papers/figure_Cflows/`（4 py + 7 圖） | 11 | 保留 |
| `assets/figures4papers/figure_Dispersion/`（2 py + 2 png） | 4 | 保留 |
| `assets/figures4papers/figure_FPGM/`（1 py + 1 png） | 2 | 保留 |
| `assets/figures4papers/figure_ImmunoStruct/`（2 py + 4 png） | 6 | 保留 |
| `assets/figures4papers/figure_RNAGenScape/`（4 py + 5 png） | 9 | 保留 |
| `assets/figures4papers/figure_VIGIL/`（4 py + 4 png） | 8 | 保留 |
| `assets/figures4papers/figure_brainteaser/`（5 py + 5 png） | 10 | 保留 |
| `assets/figures4papers/figure_ophthal_review/`（2 py + 2 png） | 4 | 保留 |

## 假設與待辦

- `references/nature-2026-observations.md` 與 `references/nature-article-requirements.md` 保留上游檔名（規格第 6 節「references 原則上不改」），在 manifest 與 SKILL.md 標為非預設；驗收第 4 項的 grep 字串不含這兩個檔名。
- 規格說「腳本一律不改」，但驗收第 4 項要求 `nature-figure` 字串只出現在本檔，因此對 `audit_figure_collisions.py`、`panel_alignment.R`、`plot_templates.py` 只做路徑與名稱字串替換，邏輯零改動。
- `evals/evals.json` 的測試提示詞仍含 "Nature style" 等字樣（測試情境，非路由），未重寫。
- `pytest` 未安裝於本機環境，`tests/test_figure_safety.py` 未執行；所有 `.py` 通過 `py_compile`。

## 驗收結果（規格第 7 節，2026-09-06）

| # | 項目 | 結果 |
|---|---|---|
| 1 | `SKILL.md` frontmatter `name: bob-figure` 等於目錄名；description 含繁中觸發詞；frontmatter 無 `nature-` | 通過（正文第 113 行提到兩個沿用上游檔名的 references，見假設） |
| 2 | `manifest.yaml` 每個路徑真實存在 | skill 內 27 個路徑與 `../bob-shared/` 4 個路徑（`core/results-discussion-escalation.md`、`core/health-research-compliance.md`、`core/zh-tw-academic-conventions.md`、`journal-formats/ndmc-thesis.md`）全部存在（bob-shared 由另一子任務同日產出，復查時已就位） |
| 3 | `python tools/s2twp.py --check` 掃描 skill 內全部 `.md` `.yaml` | exit 0 |
| 4 | 禁用字串 grep（規格第 7 節第 4 項所列的八個上游 skill 名稱與六個中國大陸平台名稱；為通過 s2twp 檢查，本檔不逐字重列） | 只出現在 `UPSTREAM.md` |
| 5 | README 三個範例提示詞用台灣情境 | 通過（專科護理師學生 SUS 成對比較圖、Tanner 與 LQQOPERA 研究架構圖、JMIR Medical Education 投稿雙面板圖） |
| 6 | 不新增未標查核日期的硬編碼期刊數字 | 通過；`journal.md` 的欄寬只給「示例值」並要求記錄查核日期；`thesis-word.md` 的 16 cm 與 300 dpi 為 Word 版面與所辦慣例，標「以所辦規範為準」 |
| 附 | `SKILL.md` 行數 ≤ 250 | 132 行 |
| 附 | `scripts/bob_figure_backend.py get／set／path／clear` | 可執行；未設定時 `get` 回傳 exit 1，`set python` 後 `get` 回傳 `python` |
| 附 | 檔案數 | 126（不含本檔） |
