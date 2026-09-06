# 研究日誌索引

放在 `{根目錄}/研究日誌/index.md`。用 Obsidian 加 Dataview 外掛時，下面的查詢會自動彙整；不用 Obsidian 時，維護最後一節的純 Markdown 表格。

## Dataview 查詢（選用）

全部日誌，最新在前：

```dataview
TABLE date, type, version, status, participants
FROM "研究日誌"
WHERE log_id
SORT date DESC
```

只看未完成的待辦：

```dataview
TABLE date, type, next_actions
FROM "研究日誌"
WHERE status = "open"
SORT date ASC
```

依系統版本看迭代與測試：

```dataview
TABLE date, type, status
FROM "研究日誌"
WHERE version = "V4"
SORT date ASC
```

異常清單：

```dataview
TABLE date, version, severity, status
FROM "研究日誌"
WHERE type = "anomaly"
SORT date DESC
```

## 純 Markdown 表格（不用 Obsidian 時）

每建一筆日誌就追加一列，最新在上。

| 日期 | log_id | type | version | 摘要 | status |
|---|---|---|---|---|---|
| YYYY-MM-DD | | | | | |

## 使用

1. 所有日誌檔都要有完整 frontmatter（`log_id`、`date`、`type`、`project`、`version`、`status` 至少齊全），Dataview 才抓得到。
2. 專案代碼與受試者代號規則寫在本檔最上方，供所有日誌沿用：
   - 專案代碼：{例如 NPCR}
   - 受試者代號：{例如 P01 起}
3. 每次指導教授會議前，用「未完成的待辦」查詢產生進度清單。
