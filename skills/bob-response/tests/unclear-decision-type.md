# Test: unclear revision decision type

## Input

```text
Reviewer 1:
1. Please clarify the validation design.

Reviewer 2:
1. The Discussion should better explain the study limitations.

請幫我準備逐點回覆和文稿修改計畫。
```

## Expected behavior

- Recognize that this is normal revision-response work but the editorial decision type is missing.
- Ask one concise question before drafting: whether this is `Major Revision` or `Minor Revision`.
- If the user writes Chinese, ask: 「這是主要修訂（Major Revision）還是次要修訂（Minor Revision）？如果退修信沒有明確寫，請把退修信貼給我，我幫你判斷。」
- Pause substantive response strategy and response-letter drafting until the user answers or supplies the decision letter.

## Forbidden behavior

- Do not infer Major Revision from the validation comment.
- Do not infer Minor Revision from the small number of visible comments.
- Do not produce a generic point-by-point response that treats both decision types as equivalent.
- Do not ask again if a subsequently supplied editor letter explicitly states the decision type.

## Pass/fail checklist

- [ ] The decision-type question is asked before substantive drafting.
- [ ] No revision type is guessed.
- [ ] No Major/Minor strategy is selected prematurely.
- [ ] The user is invited to provide the decision letter if its wording is unclear.
