# Nature Communications 2025 — Diction & Connector Calibration

> Optional calibration data from a computer-science corpus. Bob's target
> journals are nursing, medical education, and digital health titles; use this
> file only for connector and hedge frequency intuition, never as a house rule.
> For APA-style statistical wording, `significantly` is acceptable when a test
> and *p* value back it.

Use this file during the sentence-level polish pass when you want **empirical,
quantified word-choice calibration** to back up `style-guardrails.md` and
`published-article-patterns.md`. The preferences below are measured from a 2025
reading set of 20 open-access *Nature Communications* computer-science / AI
articles. They are calibration data, not rules to apply blindly — a discipline
or a specific journal house style overrides them. **Do not copy source wording.**

## 1. Connectors — observed preference order

Sentence-initial connector frequency (5-article subset):
`However` **51** ≫ `Furthermore` 22 · `Therefore` 19 · `Overall`/`Notably` 16 · `In addition` 13 · `In contrast` 6 · `Moreover` 4 · `Importantly` 2.

- **However** carries turns, gap-opening, and surprises — do not scatter weaker
  alternatives where `However` is idiomatic.
- For addition, prefer **Furthermore** over **Moreover** (22 vs 4 here).
- Cause/close with **Therefore**; summarise a block with **Overall / In summary / In conclusion**.
- Reserve **Notably / Importantly / Interestingly / Surprisingly** for the
  paragraph's key finding, not as routine sentence openers.

## 2. Boosters — the `significantly` red line

- **`significantly` appears 0 times in the corpus.** When a draft leans on
  "significantly (better/higher/improved)", first check it is a *statistical*
  claim with a test behind it; otherwise replace with **notably /
  substantially / considerably / markedly**.
- This extends the `style-guardrails.md` overclaim list: treat blanket
  intensifiers as a smell, and attach every booster to a number or a test.

## 3. Hedges — concentrated, not sprinkled

- Primary hedges are **may** and **potential**; `might / could / likely` are
  secondary. They cluster in meaning/Discussion sentences, not in Results
  reporting. Pattern marker: *"Encoding these mechanisms **may** help further
  improve the performance."*
- Keep Results sentences assertive + numeric; move the hedge to the
  interpretation sentence.

## 4. Achievement verbs — the house vocabulary

Frequent, defensible when backed by data: **achieve · demonstrate · outperform
· superior · robust · generalizable · comparable**. When the result is *weaker*
than a baseline, state it honestly and reframe with **comparable** +
concession: *"**Despite the smaller scale** of our pre-training data …, the
**comparable** performance highlights the effectiveness."* Do not upgrade
`comparable` to `superior`.

## 5. Tense & voice (polish-pass checks)

- Background / property = present; specific operation = past; figure
  description = present. Flag accidental past-tense for a standing property
  (*"CataPro demonstrates…"* not *"demonstrated"* when stating a capability).
- Active **we** for narrative and claims; passive for apparatus/method only.
  Flag passive over-use that hides the agent in claim sentences.

## 6. Sentence-skeleton phrases (calibrated to 2025 corpus)

- Abstract hinge: `Here we show/present X (FULL NAME, abbr.), a … that …`
- Gap: `However, … remains a challenge` / `the scarcity of … hinders …` /
  `Without X, Y cannot be quantified`.
- Result close: `These findings collectively affirm/confirm that …`
- Significance (soft promise, not a guarantee): `promises to / offers
  potential / paves the way`.
- Title: no number, no result — keep digits for the abstract.

## 7. 中文潤飾要點（供學術中文稿參考）

- 連接詞：轉折與開啟缺口優先用「然而」；遞進用「此外／進一步」（對應 Furthermore）；因果用「因此」；收尾用「整體而言／綜合上述」。
- 慎用「顯著」。英文 `significantly` 在本語料為 0 次；沒有統計檢定支撐時改用「明顯／大幅／相當／尤其」。
- 保留語（可能／顯示／有望）集中在詮釋句；結果句保持帶數字的肯定陳述。
- 成效措辭（達到／證明／優於／穩健／可推論／相當）需有資料支撐；弱於對照時用「相當」加「儘管樣本較小」客觀化，不拔高為「優於」。
- 本節只談用詞頻率校準。學術中文的全形標點、贅字、翻譯腔等請看 `static/fragments/language/zh-tw.md`。
