# 欄位比對矩陣與嚴重度分級

沿用上游 ref-verifier 的三級制，案例改為護理與醫學文獻。`scripts/verify_dois.py` 已把下列規則寫進 `compare()`；人工核對時用同一套標準。

## 比對前的正規化

- 標題：小寫、去重音、統一各種連字號（‐ – — −）為空白、去標點、去英文停用詞。相似度取序列比對（difflib）與 Jaccard 的最大值；長標題若為另一方的前綴視為相同。
- 作者姓氏：小寫、去重音、去空白與連字號。`Chiew‐Jiat` 與 `Chiew-Jiat` 視為相同；`van Helden` 與 `Helden` 視為相同（後綴相符）。
- 期刊：去「Journal、of、the、and、&」；縮寫比對規則是每個縮寫 token 依序是全名 token 的前綴（`J Adv Nurs` ↔ `Journal of Advanced Nursing`）。
- 頁碼：統一連字號；文章號（`e12345`、`104654`）與頁碼分開處理。

## 🔴 Critical（必須修正）

| 檢查項 | 說明 | 護理文獻案例 |
|---|---|---|
| DOI 無法解析 | Crossref 回 404 | `10.1016/j.nedt.2020.999999` 不存在；正確為 `10.1016/j.nedt.2020.104654`（示例） |
| DOI 指向另一篇 | DOI 可解析，但標題相似度 < 0.60 | 引用寫「Clinical reasoning of nurse practitioners」，DOI `10.1111/jan.15321` 解析到 Lyu et al. 的乳癌恐懼復發系統性回顧 |
| 第一作者不符 | 姓氏完全不同 | 引用寫 Wang H，資料庫第一作者為 Lyu MM |
| 作者順序異常 | 引用的第一作者在資料庫排第 2 位以後 | 引用 Siah 為第一作者，實際第一作者 Lyu |
| 漏作者 | 引用作者數少於資料庫（常見於 5 人以上只錄前 3 至 4 人） | 4 位作者只列 3 位（APA 7 需列到 20 位） |
| 頁碼差 ≥ 5 | 頁碼完全不對 | `3069–3082` 寫成 `3169–3182` |
| 文章號字母誤判 | 文章號含字母被寫成形近數字（O/0、l/1、T/7） | JMIR 文章號 `e45321` 寫成 `45321` 或 `e453Z1` |
| 年份差 ≥ 2 | 非上線年與卷年的差異 | 寫 2019，資料庫 2022 |
| 撤稿或更正 | Crossref `update-to` 含 retraction、correction；或 PubMed 標 Retracted Publication | 已撤稿仍當支持文獻引用 |

## 🟡 Warning（建議核對）

| 檢查項 | 說明 | 護理文獻案例 |
|---|---|---|
| 上線年 ≠ 卷年 | 線上先行年與正式卷期年不同；APA 7 以正式卷期年為準 | 2022-06 上線，2022-10 正式出刊，卷年 2022；若寫 2021 或 2023 需核對 |
| Early Access 漂移 | 線上先行轉正式出版後卷、期、頁改變，以資料庫現值為準 | Nurse Education Today 先行版無卷期，正式版 `90, 104654` |
| 卷或期不符 | 卷對期錯，或缺期號 | `78(10)` 寫成 `78(9)`；`78` 缺 `(10)` |
| 頁碼差 ≤ 4 | 小幅偏差 | `3069–3080` vs. `3069–3082` |
| 期刊名不符 | 名稱差異超過縮寫層級 | `Journal of Nursing Research` vs. `Journal of Nursing Scholarship` |
| 作者中間名缺漏或多餘 | 一般不影響檢索，但 APA 7 要求縮寫一致 | `Cheng K F` vs. `Cheng K K F` |
| 作者數少於資料庫 | 可能原文用 et al.，需人工判斷 | 20 位以上作者依 APA 7 規則縮寫屬正常 |

## 🟢 Info（僅供參考）

| 檢查項 | 說明 |
|---|---|
| 標題大小寫 | Title Case vs. Sentence case（APA 7 用 sentence case） |
| 標點與連字號 | `meta‐analysis`（U+2010）vs. `meta-analysis` |
| 期刊縮寫 vs. 全名 | `J Adv Nurs` vs. `Journal of Advanced Nursing`（APA 7 用全名） |
| 連接詞 | `and` vs. `&` |

## 總判定

| 等級 | 條件 |
|---|---|
| ✅ Verified | 多來源一致，無 🔴🟡 |
| ⚠️ Check suggested | 有 🟡，需人工判斷 |
| ❌ Needs fix | 有任一 🔴 |
| ❓ Unverifiable | 所有來源都查不到（內部報告、舊學位論文、非 Crossref DOI 的中文期刊） |

## 多來源交叉驗證流程

```text
輸入（DOI／PMID／標題）
   → 欄位拆分（author / title / year / journal / vol / issue / pages）
   → Crossref（DOI）     PubMed esummary（PMID）     WebSearch 或華藝（無識別碼、台灣中文期刊）
   → 欄位級比對 + 嚴重度
   → ✅ ⚠️ ❌ ❓
```

## 報告用語（繁中）

- 「DOI 張冠李戴」：DOI 可解析但指向另一篇。
- 「上線年與卷年不一致」：不是錯誤，是要選對年份。
- 「Early Access 漂移」：以資料庫現值更新卷期頁。
- 「無法驗證」不等於「捏造」；要寫明查過哪些來源與查核日期。
