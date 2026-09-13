# UPSTREAM：bob-research-log 的上游來源與逐檔異動

- 上游 repo：nature-skills（袁一哲等，Apache-2.0）；本 skill 上游作者 Jiahao8595（MIT）
- 上游穩定副本：`C:\Users\USER\ai-skills\nature-skills\skills\nature-experiment-log\`
- 上游 commit：`28150f30f8b4017991fca8c7b2839f02c6586d2f`（2026-09-06）
- 上游 skill 名稱：`nature-experiment-log`（僅在本檔出現）
- 改造日期：2026-09-06
- 改造規格：`ADAPTATION-SPEC.md` 第 2、3、4、6（bob-research-log）、7 節

上游 11 檔 → 本 skill 10 檔（不含本檔；含本檔 11 檔）。語境由材料科學實驗日誌（熔鹽腐蝕、電化學、熱穩定性）改為設計本位研究（DBR）與護理教育研究的研究日誌。

## 逐檔清單

| 上游檔案 | 本 skill 檔案 | 狀態 | 說明 |
|---|---|---|---|
| `SKILL.md` | `SKILL.md` | 改寫 | 繁中；frontmatter `name: bob-research-log`，觸發詞繁中；六種 `type`（iteration／version／test-session／meeting／irb／anomaly）；固定 frontmatter 欄位（date、type、project、version、participants、tags、status、next_actions 加 log_id、related、attachments）；路徑由使用者指定、未指定不建檔；刪除飛書 CLI 段與相關設定；Obsidian 保留為選用；圖片與語音附件歸檔規則保留並加受試者資料保護；設備代碼、樣品批次、體系代碼等材料科學規則刪除，改為 `log_id` 與受試者代號規則；新增分工邊界段 |
| `manifest.yaml` | `manifest.yaml` | 改寫 | `name: bob-research-log`；新增 `type` 軸對應範本；templates 與 references 的 on_demand 改為新檔案，條件繁中 |
| `README.md` | `README.md` | 改寫 | 繁中：用途、觸發語、3 個台灣情境範例提示詞、分工表、邊界 |
| `README_EN.md` | 無 | 刪除 | 規格第 3 節 |
| `agents/openai.yaml` | 無 | 刪除 | 規格第 3 節 |
| 無 | `UPSTREAM.md` | 新增 | 本檔 |
| `templates/anomaly-log.md` | `templates/anomaly-log.md` | 改寫 | 繁中；異常類型改為系統異常（幻覺、檢索失敗、token 異常）、資料事件、受試者事件、偏離計畫；加入「是否需通報 IRB」欄位並標明由使用者決定 |
| `templates/experiment-index.md` | `templates/index.md` | 改名＋改寫 | 繁中；Dataview 查詢改為依 type／status／version／anomaly；新增純 Markdown 表格版本供不用 Obsidian 者 |
| `templates/equipment-tracking.md` | 無 | 刪除 | 設備與試劑追蹤與研究語境無關 |
| 無 | `templates/iteration-log.md` | 新增 | DBR 迭代與版本紀錄：設計原則表、前後版本變更表、證據（量性與質性分開、標統計確認與否）、問題、下一輪 |
| 無 | `templates/meeting-log.md` | 新增 | 指導教授會議：討論、決議、待辦（負責、期限）、下次會議；`type: irb` 時替換為「進度事件」段 |
| 無 | `templates/test-session-log.md` | 新增 | 使用者測試：受試者代號與去識別化背景、場景表、SUS 十題原始作答、觀察、放聲思考摘錄、問題表對應設計原則、受試者建議 |
| `references/example-log.md` | 無 | 刪除 | 材料腐蝕浸泡示例 |
| `references/example-electrochemical.md` | 無 | 刪除 | 電化學示例 |
| `references/example-thermal-stability.md` | 無 | 刪除 | 熱穩定性示例 |
| 無 | `references/example-dbr-iteration.md` | 新增 | V3 → V4 的 DBR 迭代完整示例（NP 臨床推理學習系統、Tanner、LQQOPERA、RAG），資料虛構 |
| 無 | `references/example-test-session.md` | 新增 | NP 學生 V4 使用者測試場次完整示例（含 SUS 原始作答與放聲思考摘錄），資料虛構 |

## 假設

- 規格只列五個 templates，未指定 IRB 進度與版本紀錄的範本；本 skill 讓 `irb` 共用 `meeting-log.md`（替換為「進度事件」段）、`version` 共用 `iteration-log.md`（只填變更與證據），並在 SKILL.md 與 manifest 的 `type` 軸明示。
- frontmatter 在規格要求的八個欄位外加了 `log_id`、`related`、`attachments` 三個欄位，供索引、互連與附件追溯；規格說「可增」，故保留。
- 專案代碼與受試者代號規則由使用者自訂，示例用 `NPCR`、`P01` 起；SUS 總分只記「現場計得、未經統計確認」，計分與詮釋交 `bob-statistics`。
- LINE 群組不做即時讀取（上游飛書功能無對應），使用者需先匯出文字。

## 驗收結果（規格第 7 節，2026-09-06）

| # | 項目 | 結果 |
|---|---|---|
| 1 | `SKILL.md` frontmatter `name: bob-research-log` 等於目錄名；description 含繁中觸發詞；無 `nature-` 字樣 | 通過（全檔 0 處） |
| 2 | `manifest.yaml` 每個路徑真實存在 | 8 個路徑全部存在；本 skill 不引用 bob-shared |
| 3 | `python tools/s2twp.py --check` 掃描 skill 內全部 `.md` `.yaml` | exit 0 |
| 4 | 禁用字串 grep（規格第 7 節第 4 項所列的八個上游 skill 名稱與六個中國大陸平台名稱；為通過 s2twp 檢查，本檔不逐字重列） | 只出現在 `UPSTREAM.md` |
| 5 | README 三個範例提示詞用台灣情境 | 通過（指導教授 meeting 錄音轉錄、V4 使用者測試 P03 的 SUS 與放聲思考、醫院 IRB 補件） |
| 6 | 不新增未標查核日期的硬編碼期刊數字 | 通過；本 skill 不涉及期刊數字，SUS 未寫任何常模或切點 |
| 附 | `SKILL.md` 行數 ≤ 250 | 148 行 |
| 附 | 檔案數 | 10（不含本檔） |
