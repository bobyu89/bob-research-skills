# UPSTREAM：bob-statistics 的上游來源

- 上游專案：`nature-skills`（袁一哲等，Apache-2.0）
- 上游 skill：`skills/nature-statistics/`
- 本機副本路徑：`C:\Users\USER\ai-skills\nature-skills\skills\nature-statistics\`
- 上游 commit：`28150f30f8b4017991fca8c7b2839f02c6586d2f`（2026-09-06）
- 上游版本：manifest `version: 1.3.0`
- 改造規格：`ADAPTATION-SPEC.md` 第 6 節「bob-statistics」，並遵守第 2、3、4、5、7 節
- 改造日期：2026-09-06

## 改造摘要

上游是為 Nature／Nature Machine Intelligence 投稿設計的統計報告審查 skill，強調獨立實驗單位、生物與技術重複、圖說統計。本次改造保留其核心立場（分析單位、效果量優先、`AUTHOR_INPUT_NEEDED` 不捏造、P0/P1/P2 嚴重度、審稿風險措辭），移除所有 Nature／NMI 專屬要求，改為 APA 第七版統計格式與護理研究常見分析（t、ANOVA、卡方、相關、迴歸、信度、CVI、EFA／CFA、GEE／重複量數、無母數、G*Power、SUS），並新增四個繁中 references 讓使用者能直接照做。

## 逐檔清單

| 上游檔案 | 處置 | 目標檔案 | 說明 |
|---|---|---|---|
| `SKILL.md` | 改寫 | `SKILL.md` | 繁中 router。frontmatter `name: bob-statistics`，description 含繁中觸發詞。保留預設立場、workflow、輸出格式、紅線的骨架；刪除 Nature／NMI 步驟與檔案連結；`../nature-shared/` 改 `../bob-shared/`；新增「分工邊界」段與 SPSS 轉表輸出說明；來源階層改為 APA 7、EQUATOR、SAMPL |
| `manifest.yaml` | 改寫 | `manifest.yaml` | `name`、`version: 1.0.0`、繁中 description；always_load 加入 `apa7-statistics-format.md`；on_demand 條件全部改繁中；刪除 Nature Article 與 NMI 條目；新增四個新 references 與 `../bob-shared/core/health-research-compliance.md` 的條目 |
| `README.md`（簡中） | 改寫 | `README.md` | 全新繁中內容：用途、觸發語、3 個台灣情境範例、產出、分工表、邊界、檔案結構 |
| `README_EN.md` | 刪除 | — | 規格第 3 節規定不需要 |
| `agents/openai.yaml` | 刪除 | — | 規格第 3 節規定不需要 |
| `references/nature-article-requirements.md` | 刪除 | — | Nature 旗艦期刊專屬清單，與目標期刊無關 |
| `references/source-basis.md` | 改寫 | `references/source-basis.md` | 英文保留，來源階層改為 APA 7 第 6、7 章、EQUATOR（CONSORT 2025、STROBE、TREND、SQUIRE、COREQ、SRQR、CHERRIES、TRIPOD+AI、PRISMA-ScR）、SAMPL、護理量表慣例；刪除 Nature Portfolio 與 Statistics for Biologists 段；新增「不憑記憶引用期刊數字」與「可用性不等於學習成效」原則 |
| `references/statistical-reporting.md` | 保留（微調） | `references/statistical-reporting.md` | 英文保留；去 BOM；「Source Data」改為 tables／figure notes；細胞與動物的例子改為受試者、題項、日誌事件；s.d./s.e.m. 改 SD／SE；骨架加入效果量與 95% CI；新增繁中碩論版可貼上骨架 |
| `references/common-failure-modes.md` | 保留（微調） | `references/common-failure-modes.md` | 英文保留；去 BOM；偽重複的訊號改為題項、日誌事件、對話回合、放聲思考片段；多重比較例子改為分量表與題項；相關過度詮釋加入「可用性分數寫成學習成效」；模型建議加 GEE |
| `references/figure-statistics.md` | 保留（微調） | `references/figure-statistics.md` | 英文保留；去 BOM；「Source Data」改為 supplementary table；n 的定義改為受試者、場次、題項、事件；omics 面板改為 many-feature；指向 APA 7 圖的結構 |
| `references/reviewer-checklist.md` | 保留（微調） | `references/reviewer-checklist.md` | 英文保留；去 BOM；回覆結構加入口試意見的對應方式（章節與表號） |
| — | 新增 | `references/apa7-statistics-format.md` | 繁中。統計符號斜體規則、小數位與前導零表、p 值寫法、9 種檢定的中英報告句型、效果量與 CI、中文論文特殊慣例、APA 表格與圖的樣式（表題在上、註在下、無直線）、自查清單 |
| — | 新增 | `references/nursing-instruments-reporting.md` | 繁中。每個工具的必報欄位、信度指標（α、KR-20、ω、ICC、κ、再測）、效度（I-CVI、S-CVI/Ave、EFA、CFA、效標關聯）、Brislin 翻譯回譯、SUS 計分公式與常模表（68 分基準、等第、形容詞量表）、自編問卷專家效度流程、可貼上骨架、常見缺漏 |
| — | 新增 | `references/spss-output-to-apa-table.md` | 繁中。SPSS 欄名對 APA 符號的對應表、10 類分析（描述、獨立 t、配對 t、ANOVA 與事後、卡方、相關、線性迴歸、邏輯斯迴歸、信度、GEE 與重複量數）的表格欄位、16 條常見錯誤與修正、轉表工作流程與範例表 |
| — | 新增 | `references/sample-size-and-power.md` | 繁中。樣本數論述必報要素、Cohen 效果量慣例表與換算、G*Power 各檢定的 Test family／Statistical test／輸入欄位表、中英報告句型、失訪率除法加成、質性研究的資訊力與飽和論述、DBR 與可用性研究（SUS）的樣本數依據與限制、事後檢定力的問題與敏感度分析替代、審查清單 |
| — | 新增 | `UPSTREAM.md` | 本檔 |

## 對 bob-shared 的依賴

- `../bob-shared/core/consistency-sweep.md`（上游保留檔）
- `../bob-shared/core/health-research-compliance.md`（規格第 5 節新增檔；改造時已存在於目標 repo）

## 規格第 7 節驗收結果（2026-09-06 執行）

| # | 項目 | 結果 | 證據 |
|---|---|---|---|
| 1 | `SKILL.md` frontmatter：`name` 等於目錄名；`description` 含繁中觸發詞；無 `nature-` 字樣 | 通過 | `name: bob-statistics`；description 含「統計方法怎麼寫、統計審查、p 值、樣本數、G*Power、信度效度、Cronbach's α、CVI、SUS 分數、APA 統計格式、SPSS 報表轉表格、審稿人統計意見」；`grep -c "nature-" SKILL.md` = 0 |
| 2 | `manifest.yaml` 每一個路徑真實存在 | 通過 | 11 個路徑逐一檢查皆 OK，含 `../bob-shared/core/consistency-sweep.md` 與 `../bob-shared/core/health-research-compliance.md` |
| 3 | `python tools/s2twp.py --check` 對 skill 內所有 .md .yaml 回傳 0 | 通過 | exit = 0，無殘留簡體字 |
| 4 | 規格第 7 節第 4 項的 grep（上游 `nature-*` skill 名稱、CNKI，以及規格列出的中國大陸平台名稱）只出現在 `UPSTREAM.md` | 通過 | 排除 UPSTREAM.md 後 grep 無命中；額外以 `nature\|NMI` 不分大小寫掃描亦無命中。UPSTREAM.md 本身也不含簡體平台名稱，僅含上游 skill 名稱 |
| 5 | README 的三個範例提示詞用台灣情境 | 通過 | 範例含 DBR、專科護理師學生、SUS、放聲思考、口試委員、IRB、碩論第三章與第四章 |
| 6 | 不新增硬編碼期刊數字而未標註查核日期 | 通過 | 全 skill 無期刊字數或表格上限；`apa7-statistics-format.md` 的圖解析度寫「以期刊官網為準（查核日期由使用者填入）」，300 dpi 為規格第 6 節 bob-figure 的碩論 Word 插圖預設，非期刊規定；統計慣例門檻（α ≥ .70、CVI ≥ .78、SUS 68 分等）標為「慣例」或「示例」並附出處名稱 |

補充檢查：
- `SKILL.md` 141 行（規格上限 250 行）。
- 四個新 references 行數：apa7 166、nursing-instruments 151、spss 161、sample-size 139（規格要求 100 至 200）。
- 大陸用語掃描（軟件、信息、質量、優化、用戶、反饋、數據、項目、代碼、字段、網絡、視頻、導師、答辯、課題、開題）：無命中。
- 保留的英文 references 去 BOM，確認無 `Source Data`、`s.d.`、`s.e.m.`、動物或細胞例子殘留。

## 假設與待確認

1. 統計慣例門檻（Cronbach's α、CVI、CFA 適配指標、ICC、SUS 常模、Cohen 效果量）採文獻常見值並標示出處名稱（Polit & Beck、Koo & Li、Bangor et al.、Sauro & Lewis、Cohen），論文引用時仍需使用者查核原始文獻與年份。
2. G*Power 表中的「常見設定」人數為典型輸出的對照示例，已在檔內註明「實際數字以使用者自己執行的 G*Power 結果為準」。
3. SUS 常模表的分數切點依 Sauro & Lewis 的等第曲線整理，不同版本略有差異，檔內標為「示例」。
4. 保留的英文 references 未整篇翻譯（規格第 2 節允許），僅在 `statistical-reporting.md` 加了繁中碩論骨架。
5. 分工邊界所列的 `bob-figure`、`bob-response`、`bob-reviewer`、`bob-polishing` 為同一 repo 內其他子任務的目標名稱；改造當下這些目錄部分尚為上游原樣或尚未建立，名稱以規格第 6 節為準。
