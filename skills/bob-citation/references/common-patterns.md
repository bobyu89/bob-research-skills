# 參考文獻常見錯誤型態與根本原因

補充 `field-comparison-matrix.md`：說明錯誤從哪裡來，以及該用哪個值。

## 1. 上線年與卷年不一致

根本原因：DOI 或線上先行的年份是收稿或上線年，正式引用要用期刊卷期年。

| 型態 | 說明 | 處理 |
|---|---|---|
| 上線年 < 卷年 | 年底上線、次年出刊 | 引用卷年 |
| 上線年 > 卷年 | 少見；補刊或延遲上線 | 以官網卷期頁為準 |
| 只有上線版 | 尚未排入卷期 | APA 7 標 Advance online publication，交 apa7-master |

判斷規則：有卷號以卷年為準；無卷號以上線年為準。

## 2. 作者名

### 2.1 第一作者完全不同

生成式 AI 產生的引用最常見的「幻覺」：DOI 真實但作者對不上，或作者真實但 DOI 指向別篇。用 DOI 查 Crossref 比對第一作者姓氏即可發現。

### 2.2 順序顛倒

從書目軟體匯出或手動整理時把通訊作者放到第一位。以出版社頁面順序為準。

### 2.3 華人姓名的姓與名

- Crossref 有時把中文姓名的姓與名倒置（`given: Lyu, family: Meng-Meng`）；比對時看兩個欄位都比。
- 台灣作者英文名可能有連字號（`Chien-Mei`）或無（`Chien Mei`）；正規化時去連字號。
- 中文文獻作者的形近字（廷／延、健／建、浩／皓）以期刊官網或華藝紀錄為準。

### 2.4 西班牙語、葡萄牙語雙姓

`Álvarez López Y`、`López Y Á`、`Alvarez Lopez Y` 都算正確；不要因為腳本拆錯就標 🔴。

### 2.5 團體作者

`WHO`、`Taiwan Nurses Association` 這類團體作者在 RIS 用 `AU  - Taiwan Nurses Association,`（尾隨逗號）避免被倒置。

## 3. 頁碼與文章號

- 線上先行版與正式版頁碼不同。
- 期刊改用文章號（JMIR `e45321`、Nurse Education Today `104654`）後，舊格式頁碼欄會被填錯。
- 手動輸入時上一行頁碼串到下一行。
- 字母與數字形近：`O/0`、`l/1`、`T/7`。

以期刊官網或 Crossref 為準，不輕信書目軟體匯出。

## 4. DOI

### 4.1 指向另一篇

DOI 格式正確但錯一位（`jan.15321` 寫成 `jan.15231`），解析到同期刊另一篇。比對標題即可發現。

### 4.2 404

- 打錯、多了尾隨標點（`.`、`)`），腳本已自動去尾。
- 非 Crossref 註冊：台灣中文期刊常用華藝 DOI（`10.6224/JN.xxx` 這類前綴，示例），Crossref 查不到不代表不存在；用 WebSearch 查華藝或官網。
- 舊文獻沒有 DOI：查 PubMed，有 PMID 就用 PMID 驗證。

### 4.3 同一篇多個 DOI

預印本（medRxiv）、正式版、開放取用版本各有 DOI；以正式出版 DOI 為準，並在報告中註明曾引用預印本。

## 5. 期刊名

- 期刊改名（`Journal of Nursing Research` 早期名稱不同）；以該篇出版時的名稱為準。
- 縮寫與全名混用；APA 7 用全名。
- 同名或近名期刊（`Nurse Education Today` vs. `Nurse Education in Practice`；`Journal of Nursing Research` vs. `Journal of Nursing Scholarship`）。

## 6. 學位論文

- 台灣碩博士論文在臺灣博碩士論文知識加值系統可查標題、作者、年份、校系；多數沒有 DOI。
- APA 7 學位論文格式交 apa7-master；本 skill 只確認存在與欄位。

## 7. 指引、政府報告、網頁

- 不比對卷期頁，只確認來源可存取、版本或發布日期、機構名稱。
- 標「查核日期 YYYY-MM-DD」。

## 8. 撤稿與更正

- Crossref `update-to` 會列 `retraction`、`correction`、`expression-of-concern`。
- PubMed 標 `Retracted Publication` 或附 `Retraction in` 連結。
- 撤稿文獻不可當支持；若必須提及（例如討論撤稿本身），在句中明說。
