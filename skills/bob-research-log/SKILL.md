---
name: bob-research-log
description: >-
  把零散的文字、照片、語音轉錄整理成帶 YAML frontmatter 的 Markdown 研究日誌，
  適用設計本位研究（DBR）迭代紀錄、系統版本（V1 到 V7）紀錄、使用者測試場次、IRB 進度、指導教授會議紀錄。
  Turn raw notes, images, and voice transcripts into structured Markdown research logs with YAML frontmatter.
  觸發詞：研究日誌、迭代紀錄、寫今天的研究紀錄、meeting 紀錄、指導教授會議紀錄、使用者測試紀錄、
  IRB 進度、版本紀錄、放聲思考紀錄、系統異常紀錄、研究索引。
  不用於論文章節撰寫、統計分析、文獻整理。
---

# bob-research-log：研究日誌

把研究過程中的原始材料（文字、照片、語音轉錄、系統截圖）整理成格式固定、可追溯、可用 Dataview 或純文字檢索的 Markdown 研究日誌。核心流程不依賴任何外部工具；Obsidian 是選用。

## 適用的日誌類型（`type`）

| `type` | 用途 | 範本 |
|---|---|---|
| `iteration` | DBR 一輪迭代：設計原則、本輪變更、證據、下一輪 | `templates/iteration-log.md` |
| `version` | 系統版本（V1、V2 …）的變更摘要；是 `iteration` 的精簡版，只填變更與證據 | `templates/iteration-log.md` |
| `test-session` | 一場使用者測試：受試者代號、場景、SUS、觀察、問題 | `templates/test-session-log.md` |
| `meeting` | 指導教授會議或研究小組會議：討論、決議、待辦、期限 | `templates/meeting-log.md` |
| `irb` | IRB 送審、補件、核准、修正案等進度事件 | `templates/meeting-log.md`（用「進度事件」段） |
| `anomaly` | 系統異常、偏離計畫、資料事件、受試者事件 | `templates/anomaly-log.md` |

一次會議或一天可能產生多種類型；各自成檔，用 `related` 欄位互連。

## 輸入方式

- **直接上傳**：在對話中貼文字、上傳照片（白板、手寫筆記、系統截圖）、語音轉錄。
- **本地檔案**：提供檔案或資料夾路徑，由本 skill 讀取整理。
- 不支援任何即時通訊平台的群組讀取；LINE 對話請先匯出成文字再提供。

## 輸出格式

Markdown，開頭為 YAML frontmatter，欄位固定如下（可增不可刪）：

```yaml
---
log_id: NPCR-IT-260906-001
date: 2026-09-06
type: iteration            # iteration / version / test-session / meeting / irb / anomaly
project: NP 臨床推理學習系統   # 專案名稱，同一專案保持一致
version: V4                # 系統版本；與版本無關時填 null
participants: [研究者, 指導教授]   # 出席者或受試者代號；受試者一律用代號
tags: [DBR, RAG, Tanner]
status: open               # open / done / blocked
next_actions:
  - 修改提示詞加入 LQQOPERA 追問順序（負責：游明勳，期限：2026-09-13）
related: []                # 其他 log_id
attachments: []            # 相對路徑
---
```

正文結構依 `type` 對應的範本。正文用台灣繁體中文與全形標點；系統名稱、量表名稱、統計符號照原文。

## 路徑規則（不擅自存檔）

- **使用者指定路徑**：寫入 `{根目錄}/研究日誌/{project}/{type}/{log_id}.md`，附件歸檔到 `{根目錄}/raw/{YYYY.MM.DD}_{簡述}_{log_id}/`。
- **未指定路徑**：先在對話中回傳完整 Markdown（含 frontmatter），並問要存到哪裡；**不要**自行挑選目錄或建立檔案。
- 使用者說「跟上次一樣」時沿用同一任務中已確認的根目錄。

## 處理流程

1. 收集材料：讀取上傳內容或本地檔案；照片用視覺分析抽出文字與重點，語音轉錄先分段。
2. 判斷 `type`，載入對應範本；同一材料含多種類型時分別建檔。
3. 抽取欄位：日期、出席者或受試者代號、版本、討論、決議、待辦與期限。
4. **缺漏或模糊處向使用者確認**（例如 SUS 分數記不清、版本號不明、誰負責哪件事），不猜測補寫；暫填 `AUTHOR_INPUT_NEEDED`。
5. 產生 `log_id`（規則見下），套用範本，寫出 frontmatter 與正文。
6. 使用者已指定路徑時存檔並歸檔附件，在日誌中以相對路徑引用；否則回傳內容。
7. 若專案有 `index.md`，追加一列；`type` 為 `anomaly` 或日誌中提到異常時，另建或追加異常紀錄。
8. 回報產生的檔案與附件位置，列出仍待確認的欄位。

## `log_id` 規則

```
{專案代碼}-{類型代碼}-YYMMDD-{序號}
  │          │          │       └─ 當日序號（001 起）
  │          │          └─ 日期
  │          └─ IT=iteration, VER=version, TS=test-session, MT=meeting, IRB=irb, AN=anomaly
  └─ 專案代碼，使用者自訂（例如 NPCR = NP 臨床推理學習系統、ANH = 失樂感監測平台）
```

受試者代號規則由使用者決定（例如 P01、P02），日誌中**不得**出現姓名、學號、員工編號或任何可識別資訊。

## 附件歸檔規則

- 照片與截圖：存到 `raw/{YYYY.MM.DD}_{簡述}_{log_id}/圖片/`，檔名保留原始名稱，日誌末尾以清單引用並各加一句說明。
- 語音：原始音檔存 `語音/`，轉錄文字存同目錄 `轉錄.md`；日誌只引用轉錄摘要，不貼全文。
- 系統日誌與資料匯出：存 `資料/`，日誌記錄檔名、筆數與擷取時間。
- 含受試者聲音或畫面的附件，只存在使用者指定的本機目錄，不上傳到任何雲端或第三方服務；IRB 規定的保存年限與銷毀方式由使用者依核准計畫書處理。

## 目錄結構（建議）

```
{根目錄}/
├── raw/                                  ← 原始層（歸檔）
│   └── 2026.09.06_V4迭代_NPCR-IT-260906-001/
│       ├── 圖片/
│       ├── 語音/
│       └── 資料/
└── 研究日誌/                              ← 標準層（產出）
    ├── index.md                          ← 總索引
    ├── anomaly-log.md                    ← 異常紀錄（彙整）
    └── NP臨床推理學習系統/
        ├── iteration/
        ├── version/
        ├── test-session/
        ├── meeting/
        └── irb/
```

## 選用的 Obsidian 整合

所有日誌都是純文字 Markdown，可直接放進 Obsidian vault。搭配 Dataview 外掛時，`templates/index.md` 提供依 `type`、`version`、`status` 篩選的查詢；不用 Obsidian 時，`index.md` 內附純 Markdown 表格版本。不要求安裝 Obsidian。

## 範本與示例

| 檔案 | 用途 |
|---|---|
| `templates/iteration-log.md` | DBR 迭代與版本紀錄 |
| `templates/meeting-log.md` | 指導教授會議與 IRB 進度 |
| `templates/test-session-log.md` | 使用者測試場次 |
| `templates/anomaly-log.md` | 異常紀錄 |
| `templates/index.md` | 總索引（Dataview 與純表格） |
| `references/example-dbr-iteration.md` | 完整示例：V3 到 V4 的一輪 DBR 迭代 |
| `references/example-test-session.md` | 完整示例：一場 NP 學生使用者測試 |

示例資料全為虛構，只示範格式。

## 分工邊界

| 情境 | 交給 | 本 skill 的角色 |
|---|---|---|
| SUS 總分計算、信度、前後測比較 | `bob-statistics` | 只記錄原始作答與現場計得的分數，標明「未經統計確認」 |
| 把迭代紀錄整理成論文第三章的 DBR 流程或第四章結果 | `bob-writing`（整章 .docx 交 `academic-writing`） | 提供按日期排序的日誌與證據清單 |
| 放聲思考與訪談的質性編碼 | `mixed-methods-research` 或使用者自行處理 | 只保留逐字稿路徑與現場觀察摘要 |
| 會議紀錄要做成正式 Word 文件 | `docx` | 提供 Markdown 內容 |
| 日誌中的圖要做成論文圖 | `bob-figure` | 提供資料檔路徑與觀察重點 |
| IRB 文件本身的撰寫或修正案內容 | 使用者依送審醫院 IRB 範本處理 | 只記錄送審事件、日期與待辦 |

## 邊界

- 不替使用者編造分數、日期、決議或受試者反應；不確定就問或標 `AUTHOR_INPUT_NEEDED`。
- 未指定路徑不建檔。
- 不在日誌中寫入可識別受試者的資訊。
- 不做統計、不寫論文章節、不整理文獻。
