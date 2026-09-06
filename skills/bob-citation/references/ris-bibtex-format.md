# RIS、BibTeX 與 nbib 格式規格

## 目錄

- RIS
- BibTeX
- nbib（MEDLINE）
- 文字清理
- 格式選擇

## RIS

EndNote、Zotero 與多數書目軟體都能匯入 RIS。純文字、易檢查，作為預設交換格式。

### 期刊文章範本

```text
TY  - JOUR
AU  - Lyu, Meng-Meng
AU  - Siah, Rosalind Chiew-Jiat
AU  - Taiwan Nurses Association,
TI  - The effect of psychological interventions on fear of cancer recurrence in breast cancer survivors: A systematic review and meta-analysis
JO  - Journal of Advanced Nursing
T2  - Journal of Advanced Nursing
JA  - J Adv Nurs
PY  - 2022
VL  - 78
IS  - 10
SP  - 3069
EP  - 3082
DO  - 10.1111/jan.15321
UR  - https://doi.org/10.1111/jan.15321
SN  - 0309-2402
N2  - 摘要（可省略）
KW  - fear of cancer recurrence
AN  - PMID:35696315
DB  - PubMed
ER  - 
```

規則：

- 每位作者一行 `AU`，保留來源順序；個人作者用 `Family, Given` 或 `Family, Given, Suffix`。
- 團體作者尾隨逗號（`AU  - Taiwan Nurses Association,`），避免 EndNote 倒置。
- 只有姓氏的 `AU  - Chaudhuri` 是不完整紀錄，不可交付。
- 每筆以 `ER  - ` 結尾，後接空白行。
- 不捏造缺欄位；缺就不寫。
- DOI 寫在 `DO`，`UR` 可同時放 DOI 網址。
- PMID 寫在 `AN  - PMID:` 以便追溯。
- 摘要可長；要精簡檔案時用 `--no-abstract`。

### MEDLINE → RIS 對應

| MEDLINE | RIS | 說明 |
|---|---|---|
| `PMID-` | `AN  - PMID:` | |
| `TI  -` | `TI  -` | 去尾句點 |
| `FAU -`（優先）／`AU  -` | `AU  -` | 全名優先 |
| `CN  -` | `AU  - 名稱,` | 團體作者 |
| `JT  -` | `JO  -`、`T2  -` | 全名 |
| `TA  -` | `JA  -` | 縮寫 |
| `DP  -` | `PY  -` | 只取年 |
| `VI  -`／`IP  -` | `VL  -`／`IS  -` | |
| `PG  -` | `SP  -`／`EP  -` | 以連字號切 |
| `AB  -` | `N2  -` | |
| `MH  -`、`OT  -` | `KW  -` | |
| `LID -`／`AID -` 含 `[doi]` | `DO  -` | 掃全部值，PII 先出現時不會漏 |
| `IS  -`（Linking） | `SN  -` | |

## BibTeX

### 期刊文章範本

```bibtex
@article{pmid35696315,
  author   = {Lyu, Meng-Meng and Siah, Rosalind Chiew-Jiat and Lam, Alekzendr Sheen Loong and Cheng, Karis Kin Fong},
  title    = {{The effect of psychological interventions on fear of cancer recurrence in breast cancer survivors: A systematic review and meta-analysis}},
  journal  = {Journal of Advanced Nursing},
  year     = {2022},
  volume   = {78},
  number   = {10},
  pages    = {3069--3082},
  doi      = {10.1111/jan.15321},
  url      = {https://doi.org/10.1111/jan.15321},
  pmid     = {35696315},
}
```

鍵的慣例：有 PMID 用 `pmid35696315`；沒有用 `姓氏小寫 + 年份`（`tanner2006`）；重複加 `a`、`b`。來源檔已有鍵時沿用。

### 必填欄位

- `@article`：author、title、journal、year
- `@book`：author 或 editor、title、publisher、year
- `@inproceedings`：author、title、booktitle、year
- `@phdthesis`／`@mastersthesis`：author、title、school、year

### 清理規則

- 作者分隔一律 ` and `；`&` 轉 `\&`。
- 標題外層雙大括號保留大小寫。
- 摘要去 HTML 標籤。
- 頁碼用 `--`。

## nbib（MEDLINE）

PubMed 匯出的原生格式，EndNote 可直接匯入（Import Option 選 PubMed (NLM)）。由 `ris_tools.py` 從 RIS 或 BibTeX 產生時是 best-effort：有 `PMID-`、`TI`、`FAU`／`AU`、`JT`／`TA`、`DP`、`VI`、`IP`、`PG`、`LID [doi]`、`AB`、`OT`，沒有 `STAT`、`MH`、`AD` 等 NLM 內部欄位。標題與摘要依 MEDLINE 慣例在 80 字元換行並以 6 格縮排續行。

`AU` 由 `FAU` 推導：`Lyu, Meng-Meng` → `Lyu MM`。

## 文字清理

所有自由文字欄位（標題、作者、期刊、摘要、關鍵字）：

- 去 HTML 標籤（`<sup>1</sup>` → `1`）。
- 合併空白與換行。
- 去頭尾空白。
- 檔案用 UTF-8（無 BOM）、LF 換行。

## 格式選擇

| 使用者說 | 用 |
|---|---|
| EndNote | RIS（Import Option = Reference Manager (RIS)）；也可 nbib（PubMed (NLM)） |
| Zotero | RIS 或 BibTeX（File > Import…） |
| LaTeX、BibTeX、Overleaf | BibTeX |
| PubMed 格式、MEDLINE、nbib | nbib |
| APA 7 文字 | 不在此產生；交 apa7-master |
