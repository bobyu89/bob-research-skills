# 範本：異常紀錄（`type: anomaly`）

記錄研究過程中所有偏離預期的事件，供後續品質控管、IRB 通報判斷與論文限制段撰寫。可一事一檔，也可在專案的 `anomaly-log.md` 彙整檔中逐筆追加。

```markdown
---
log_id: {專案代碼}-AN-YYMMDD-001
date: YYYY-MM-DD
type: anomaly
project: {專案名稱}
version: V{n}
participants: [{相關人員或受試者代號}]
tags: [異常, {類型}]
status: open            # open / done / blocked
next_actions:
  - {處理措施}（負責：{人}，期限：YYYY-MM-DD）
related: [{對應的 iteration 或 test-session log_id}]
attachments: []
---

# 分類

- 類型：系統異常（幻覺、檢索失敗、回應中斷、token 成本異常）／資料事件（日誌遺失、問卷缺漏、檔案損毀）／受試者事件（中途退出、不適、要求刪除資料）／偏離計畫（流程與核准計畫書不符）／設備或環境
- 嚴重度：低／中／高
- 是否需通報 IRB：是／否／待確認（依核准計畫書與三軍總醫院 IRB 規定判斷，由使用者決定）

# 描述

客觀描述發生了什麼、何時、在哪個場景或版本、如何發現。

# 影響

對資料、受試者、系統版本或時程的影響評估。

# 處理

已採取的措施與時間。

# 後續

- 是否需要修改設計原則或系統版本（連到 iteration 日誌）
- 是否需要在論文限制段揭露
```

## 使用

- 每場測試、每輪迭代結束後檢查是否有異常，有則建檔或追加。
- 受試者事件一律去識別化；涉及不適或退出時，由使用者依 IRB 規定判斷通報，本 skill 只記錄事實與待辦。
- 定期檢視 `status: open` 的異常。
