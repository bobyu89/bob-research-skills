# Test: thesis committee response mode

## Input

```text
學位論文口試通過。委員意見（書面）：

委員一：
1. 第四章質性結果的主題與 Tanner 模型四面向的對應不清楚。

委員二：
1. 建議加做多中心驗證。

指導教授：
1. 表 4-2 標題移到表格上方。

筆記：
- 表 4-2 已改。
- 多中心我們做不到。
```

## Expected behavior

- Route to `committee-response` mode; do not ask the Major/Minor Revision question.
- Ask or confirm defense type (here: thesis defense) and the institute's submission requirements only if unknown.
- Assign IDs `C1.1`, `C2.1`, `A.1`.
- Produce one table with columns 委員／委員意見／修改內容／頁碼; no per-reviewer isolation.
- `C1.1`: `ACCEPT_TEXT` or `ACCEPT_FIGURE`, `TODO_TEXT`, propose a mapping table between themes and Tanner's four aspects.
- `C2.1`: `OUT_OF_SCOPE`, written as "經與指導教授討論……列為未來研究建議" with a design-based reason, not a time or budget excuse.
- `A.1`: `ACCEPT_TEXT`, `REPORTED_DONE_UNVERIFIED` until the revised table is supplied.
- Page numbers remain placeholders until the user supplies them.
- Readiness `needs_author_input`.

## Forbidden behavior

- Do not apply the mutually blind filter or split the table per committee member.
- Do not invent page numbers.
- Do not leave the `C2.1` cell blank or write only「不採納」.
- Do not use 大修／小修／返修／答辯 wording; use 主要修訂／次要修訂／退修／口試.

## Pass/fail checklist

- [ ] No Major/Minor gate question is asked.
- [ ] All three items appear with the correct IDs in one table.
- [ ] `C2.1` gives a design-based reason and points to the future-research section.
- [ ] `A.1` is not marked `VERIFIED_DONE`.
- [ ] All page numbers are placeholders.
