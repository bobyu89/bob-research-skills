# 腳本用法

兩支腳本都只用 Python 標準函式庫（3.9 以上），不需安裝套件。Windows 主控台已強制 UTF-8 輸出。路徑一律用絕對路徑。

## verify_dois.py

```bash
python scripts/verify_dois.py --input refs.txt --mailto you@example.com --json verify.json --md verify.md
python scripts/verify_dois.py --input refs.bib
python scripts/verify_dois.py --input refs.ris --search-missing
python scripts/verify_dois.py --doi 10.1111/jan.15321 --doi 10.1016/j.nedt.2020.104654
python scripts/verify_dois.py --pmid 35696315
```

| 參數 | 說明 |
|---|---|
| `--input`, `-i` | `.txt`（每筆一行，APA 7 或 `[n] … DOI`）、`.bib`、`.ris`、`.nbib` |
| `--doi` | 直接指定 DOI，可重複 |
| `--pmid` | PMID 反查（E-utilities esummary），列出 DOI 與書目；可重複或逗號分隔 |
| `--mailto` | Crossref polite pool 的 email（User-Agent 與 `mailto` 參數） |
| `--ncbi-email` | E-utilities 的 `email` 參數；省略時沿用 `--mailto` |
| `--search-missing` | 無 DOI 的條目用 Crossref `query.bibliographic` 找候選（只列候選） |
| `--json` | 輸出 JSON |
| `--md` | 輸出 Markdown（省略則印到標準輸出） |
| `--quiet` | 不印 Markdown |

回傳碼：有 ❌ 時回 1，否則 0。

輸出 JSON 結構：

```json
{
  "checked_on": "2026-09-06",
  "results": [
    {
      "label": "[2]", "doi": "10.1111/jan.15321", "status": "check", "source": "Crossref",
      "checks": [
        {"field": "year", "given": "2021", "found": "2022", "level": "warn", "note": "年份差 1 年…"}
      ],
      "found": {"title": "...", "authors": ["Lyu, Meng-Meng", "..."], "journal": "...", "year": "2022", "volume": "78", "issue": "10", "start_page": "3069", "end_page": "3082", "doi": "10.1111/jan.15321"}
    }
  ]
}
```

`status`：`verified`／`check`／`fix`／`unverifiable`。`level`：`ok`／`info`／`warn`／`crit`／`na`（輸入未提供該欄位）。

實測（2026-09-06，DOI 10.1111/jan.15321）：Crossref 回傳 Lyu et al.，Journal of Advanced Nursing，78(10)，3069-3082，issued 2022-06-13、print 2022-10；正確引用判 ✅，年份寫 2021 判 🟡，DOI 錯一碼判 🔴 404，標題與作者不符判 🔴 張冠李戴。

## ris_tools.py

```bash
python scripts/ris_tools.py convert INPUT [INPUT ...] --to ris|bib|nbib [-o OUT] [--dedupe] [--no-abstract]
python scripts/ris_tools.py dedupe  INPUT [INPUT ...] [--to ris|bib|nbib] [-o OUT]
python scripts/ris_tools.py check   INPUT [INPUT ...]
python scripts/ris_tools.py fetch   --pmid 35696315,12345678 --to ris -o out.ris --ncbi-email you@example.com
python scripts/ris_tools.py fetch   --doi 10.1111/jan.15321 --to bib --mailto you@example.com
```

| 子命令 | 說明 |
|---|---|
| `convert` | 讀多個檔（格式可混合），輸出指定格式；`--dedupe` 合併時去重 |
| `dedupe` | 只去重；輸出格式預設同第一個輸入 |
| `check` | 列出作者只有姓氏、缺 DOI、缺年份、缺卷號、缺頁碼的條目；有問題回傳 1 |
| `fetch` | 由 PubMed efetch（MEDLINE）或 Crossref 取得書目後輸出 |

格式偵測：副檔名 `.ris`、`.bib`、`.nbib`；或內容開頭 `TY  - `、`@article{`、`PMID- `。

去重鍵：DOI → PMID → 標題正規化 + 第一作者姓氏（Jaccard ≥ 0.90）。合併保留較完整者，缺欄位互補。

實測（2026-09-06）：`dedupe-mix.bib`（5 筆，含同 DOI 大小寫不同、同標題無 DOI、只有姓氏的作者）+ `pubmed-35696315.nbib`（1 筆）→ 去重後 3 筆；`check` 抓出 `Chaudhuri`、`Schapira` 只有姓氏。

## 在 skill 中的使用時機

| workflow | 步驟 | 腳本 |
|---|---|---|
| find-support | 匯出 | `ris_tools.py fetch --pmid` → `check` |
| verify | 欄位比對 | `verify_dois.py --input` → 人工處理 ❌❓ |
| verify | PMID 反查 | `verify_dois.py --pmid` |
| export | 轉檔 | `ris_tools.py convert --dedupe` → `check` |

## 限速與錯誤

- 兩支腳本每次請求間隔 0.35 秒，失敗重試 2 次（404 不重試）。
- Crossref 429：等 30 秒；加 `--mailto`。
- E-utilities 未帶 email 時每秒最多 3 次請求；批次超過 100 筆時分批。
- 網路錯誤的條目標 ❓ 並在 `note` 寫出錯誤訊息，不會中斷整批。

## 測試樣本

`tests/samples/`：`pubmed-35696315.nbib`（JAN 2022 系統性回顧）、`pubmed-35696315.ris`、`refs-apa7.txt`（含 4 種故意錯誤）、`dedupe-mix.bib`。`tests/test_ris_tools.py` 為離線單元測試：

```bash
python skills/bob-citation/tests/test_ris_tools.py   # 或 python -m pytest skills/bob-citation/tests -q
```
