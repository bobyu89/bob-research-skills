# 檢索策略與支持等級

## 把主張拆成可檢索的概念

每句拆成：

- `phenomenon`：句子在主張什麼。
- `entity`：介入、工具、系統、量表、族群、疾病、教育方法。
- `relationship`：提升、降低、預測、相關、造成、改善、偵測、比較。
- `context`：族群（護理學生、專科護理師、腫瘤病人）、場域（加護病房、門診、模擬教室）、國家、時期、方法（RCT、質性、DBR）。
- `boundary`：「在新進護理師中」「在台灣」「在急診分流時」。

三層查詢：

1. `precise`：entity + relationship + outcome + context，MeSH 優先。
2. `synonym`：同義詞與縮寫（clinical reasoning／clinical judgment／diagnostic reasoning；nurse practitioner／advanced practice nurse／APRN；large language model／generative AI／ChatGPT）。
3. `broad`：找不到直接文獻時退到領域脈絡，並加年份限制。

中文主張翻譯的是科學概念而不是句子。縮寫與標準名詞（SUS、RAG、LLM、OSCE、Tanner、LQQOPERA）保持不變；台灣專屬名詞給英文對應（專科護理師 → nurse practitioner, Taiwan）。

## PubMed 查詢範例（護理與醫學教育）

| 主張 | 查詢 |
|---|---|
| 模擬教學提升護理學生臨床判斷 | `("Simulation Training"[Mesh] OR high-fidelity simulation) AND ("Clinical Reasoning"[Mesh] OR clinical judgment) AND ("Students, Nursing"[Mesh])` |
| 生成式 AI 用於臨床推理教學 | `(large language model* OR generative artificial intelligence OR ChatGPT) AND (clinical reasoning OR clinical judgment) AND (nursing education OR medical education)` |
| SUS 的信效度 | `"System Usability Scale" AND (psychometric* OR reliability OR validity)` |
| 專科護理師角色與病人結果 | `"Nurse Practitioners"[Mesh] AND ("Patient Outcome Assessment"[Mesh] OR outcomes) AND systematic review[pt]` |
| 放聲思考法用於推理研究 | `"think aloud" AND (clinical reasoning OR decision making) AND nurs*` |

常用限制：`2021:2026[dp]`、`english[la]`、`randomized controlled trial[pt]`、`systematic review[pt]`、`review[pt]`。

## 支持等級

用「最小可辯護」的等級：

| 等級 | 意思 | 適用 |
|---|---|---|
| direct | 直接檢驗同一關係，情境相近 | 實證、介入、量化主張 |
| partial | 支持一部分或較窄情境 | 加限定詞後的主張 |
| background | 建立領域脈絡或先前觀察 | 前言背景句 |
| contradictory | 相反或限縮 | 討論、限制；不當支持用 |
| metadata-only | 只看書目，未讀摘要 | 篩選中，不可引用 |

## 證據說明範本

```text
句子：S004 生成式 AI 輔助的臨床推理訓練可提升專科護理師學生的診斷準確度。
文獻：Lyu et al. (2022). J Adv Nurs. 10.1111/jan.15321
等級：partial
依據：摘要
理由：文獻為心理介入對乳癌存活者恐懼復發的系統性回顧，族群與結果都不同；只能支持「心理層面介入可改變臨床結果」的背景，不支持診斷準確度。
引用措辭：不建議用於此句；改找 nurse practitioner + clinical reasoning + AI 的原始研究。
```

## 常見誤引

- 文獻談同一疾病但不同介入。
- 文獻支持相關，句子寫因果。
- 族群不同：病人 vs. 護理人員、學生 vs. 執業者、台灣 vs. 美國。
- 用綜述當原始證據，而原始研究存在。
- 一句主張太寬，一篇文獻撐不起。
- 引用年份太舊卻寫「近年」。
- 把預印本（medRxiv）當同儕審查文獻，未標明。

## 更好的檢索動作

- 結果太寬：加方法或設計（randomized、qualitative、mixed methods、design-based research、scoping review）。
- 不相關結果太多：加族群、場域、結果指標（diagnostic accuracy、System Usability Scale、self-efficacy）。
- 主張可能過度自信：反向查（improves vs. no difference；risk vs. protective）。
- 找到一篇好文獻後用 `find_related_articles` 或它的參考文獻擴展。
- 快速變動領域（LLM）用近 3 年限制；找不到再放寬。
