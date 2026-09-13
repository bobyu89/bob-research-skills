# bob-research-skills 改造規格（給每個子任務的共同契約）

本文件是把上游 `nature-skills`（袁一哲等，Apache-2.0）改造成 **游明勳（Bob）個人科研 skill 集** 的共同規格。
每個 skill 的改造者都必須先讀完本文件，再讀上游對應 skill 的全部檔案，然後在目標目錄產出成品。

- 上游穩定副本：`C:\Users\USER\ai-skills\nature-skills`（commit `28150f30f8b4017991fca8c7b2839f02c6586d2f`，2026-09-06）
- 目標 repo：`C:\Users\USER\Downloads\bob-research-skills`
- 目標 skill 目錄：`C:\Users\USER\Downloads\bob-research-skills\skills\<skill-name>\`
- 簡轉繁工具：`python tools/s2twp.py FILE...`（就地轉換，OpenCC s2twp）；`python tools/s2twp.py --check FILE...`（掃描殘留簡體字，有殘留回傳 1）

---

## 1. 使用者是誰（所有內容都為這個人服務）

- 游明勳（Bob），國防醫學院護理學研究所 **專科護理師（NP）組** 碩士生，有指導教授指導（姓名略）。臨床背景為腫瘤／內科護理。
- 碩士論文：**結合生成式 AI 與檢索增強技術（RAG）之專科護理師臨床推理學習系統**。研究設計為 **設計本位研究（Design-Based Research, DBR）**，理論框架 Tanner 臨床判斷模型，問診框架 LQQOPERA；資料含量性（SUS 系統可用性量表、自編問卷、系統日誌、token 成本）與質性（放聲思考、半結構式訪談）。已通過計畫書口試（2026-08-12），IRB 送至醫學中心審查。
- 其他進行中的科研工作：範疇性文獻回顧（scoping review，JBI／PRISMA-ScR）、概念分析（Walker & Avant）、失樂感（anhedonia）監測平台的問卷資料與 SPSS 分析、護理師國考題庫、腫瘤衛教機器人、iThome 鐵人賽「研究生的論文工具箱」系列。
- 投稿目標多為 **護理／醫學教育／數位健康** 期刊（例如 Journal of Advanced Nursing、International Journal of Nursing Studies、Nurse Education Today、Nurse Education in Practice、JMIR 系列、Journal of Nursing Research、BMC Medical Education、Computers, Informatics, Nursing）以及台灣期刊（護理雜誌、護理研究、台灣專科護理師學刊、醫學教育）。**不是** Nature／Science／Cell。
- 引用格式一律 **APA 第七版**。論文正文用全形標點（，：（）），引用括號用半形；內文字型標楷體；表格與圖說有固定樣式；Word 為主要交付格式。
- 溝通語言：**台灣繁體中文**。使用者不寫簡體字，也不用中國大陸用語。

## 2. 語言與用語規範（硬性）

1. 所有 **新寫** 的 SKILL.md、README.md、static fragments、manifest 的 detect 說明，一律用台灣繁體中文撰寫；技術欄位名稱（frontmatter `name`、axis 值、檔名）保持 ASCII kebab-case。
2. 上游保留下來的英文 references 可以維持英文，不必翻譯；但檔案中若含簡體中文，必須跑 `tools/s2twp.py` 轉成繁體，再人工把大陸用語改為台灣用語。
3. frontmatter `description` 用「中文說明 + 英文一句 + 觸發詞列表」，觸發詞只放 **繁體** 用語，不放簡體。
4. 大陸用語 → 台灣用語對照（必改）：
   数据/資料（統計語境下「數據」可用，但預設「資料」）、软件/軟體、硬件/硬體、信息/資訊、质量/品質、优化/最佳化、项目/專案或計畫、反馈/回饋、用户/使用者、程序/程式、代码/程式碼、字段/欄位、文件夹/資料夾、网络/網路、视频/影片、打印/列印、缺省/預設、返修/修改稿或修訂、返修邮件/退修信或審查意見信、组会/實驗室會議、开题报告/計畫書（口試）、导师/指導教授、答辩/口試、课题/研究主題、论文投稿/期刊投稿、审稿人/審稿人或審查委員（兩者皆可）、修回/修訂後再審、大修/主要修訂（major revision）、小修/次要修訂（minor revision）、支撑文献/支持文獻、他引/他人引用、院士·杰青·长江学者/（刪除，台灣無此制度；改為「領域重要學者」）、飞书·微信·抖音·知识星球·CNKI·万方/（全部刪除；台灣用 LINE、Notion、Google Drive、華藝 Airiti、臺灣博碩士論文知識加值系統）。
5. 標點：中文段落用全形標點；英文段落照英文規則。SKILL.md 說明文字避免破折號當連接詞。

## 3. 架構規範（沿用上游的靜態／動態分層）

- 保留上游的 **router 模式**：`SKILL.md`（短 router）+ `manifest.yaml`（axes、always_load、references.on_demand）+ `static/`（core 與 fragments）+ `references/`（深度資料，按需載入）。
- 所有 `../nature-shared/` 路徑改為 `../bob-shared/`；bob-shared 的檔案清單見第 5 節，只能引用該清單中存在的檔案。
- 每個 skill 目錄必須有：`SKILL.md`、`manifest.yaml`、`README.md`（繁中，含：用途、觸發語、3 個範例提示詞、與既有 skill 的分工表）、`UPSTREAM.md`（上游來源路徑、commit、逐項列出「保留／改寫／新增／刪除」的檔案）。
- 刪除上游的 `agents/openai.yaml`、`README_EN.md`（不需要）。
- 不要保留任何指向 `nature-*` 名稱的觸發或路由；上游 skill 名稱只在 `UPSTREAM.md` 出現。
- 不憑記憶捏造期刊字數、圖表上限等硬數字。凡寫到具體期刊規定，必須標「以期刊官網為準，查核日期 YYYY-MM-DD」或標為「示例」。
- 每個 skill 的 SKILL.md 控制在 250 行以內；深度內容放 references。

## 4. 與使用者「既有 skill」的分工（必須寫進每個 skill 的 README 與 SKILL.md 的「分工邊界」段）

使用者的 Claude 環境已內建下列 skill（呼叫名稱以 `anthropic-skills:` 為前綴，或直接用名稱），**bob-\* 不得重複其核心功能，而是在需要時把工作交接過去**：

| 既有 skill | 負責 | bob-* 的關係 |
|---|---|---|
| `academic-writing` | 醫藥領域論文全章節撰寫、APA 內文引用、AI 痕跡消除、輸出 .docx | bob-writing 負責「論證架構、段落任務、證據鏈、主文精簡」；要輸出整章 .docx 或整合多篇文獻成段時，交給 academic-writing |
| `apa7-master` | APA 7 參考文獻格式產生與稽核 | 所有 reference list 格式一律交給它；bob-citation 只負責「找到、驗證、匯出 RIS」 |
| `citation-verifier` | 引文真實性查證 | bob-citation 的驗證步驟可呼叫它；bob-citation 額外提供 DOI 解析與欄位比對表 |
| `scoping-review-master` / `prisma-2020-master` / `consort-2025-master` / `strobe-v4-master` / `equator-guideline-finder` | 各報告準則 | bob-writing、bob-reviewer、bob-statistics 遇到對應研究設計時，先呼叫 equator-guideline-finder 決定準則，再套用 |
| `concept-analysis-master` | Walker & Avant 概念分析 | bob-writing 的 paper_type 不含概念分析；直接轉交 |
| `academic-peer-reviewer` | 單一資深審稿人深度批判（含 Minerva 批判思考） | bob-reviewer 提供「3 位互盲審稿人 + 綜合」；使用者要單一深度審查時交給 academic-peer-reviewer |
| `paper-analysis` | 單篇論文閱讀與整理 | 本集不做 reader；直接轉交 |
| `mixed-methods-research` | 混合方法研究設計 | bob-writing 的 mixed-methods fragment 只管「怎麼寫」，設計問題轉交 |
| `pubmed-daily-bundle` | 文獻搜尋排程 | bob-citation 不做排程 |
| `speak-human-tw` | 台灣口語化／去 AI 腔 | bob-polishing 處理學術英文與學術中文；要「講人話」版本時轉交 |
| `docx` / `pptx` / `xlsx` / `pdf` | 檔案輸出 | bob-* 產生文字後，需要檔案時呼叫 |
| `grad-lecture-to-slides` | 簡報 | 本集不做 paper2ppt |
| `critical-thinking-coach` | 密涅瓦思考訓練 | bob-reviewer 綜合段可建議使用 |
| `np-case-report` / `twna-ebhc-report` / `nursing-project-reviewer` | 護理專用報告 | 不重疊 |

可用的 MCP 工具（bob-citation、bob-reviewer 可直接使用，不要假設有 Scopus／ScienceDirect／CNKI）：
- PubMed：`mcp__plugin_bio-research_pubmed__search_articles`、`get_article_metadata`、`get_full_text_article`、`find_related_articles`、`convert_article_ids`、`lookup_article_by_citation`
- Consensus：`mcp__plugin_bio-research_consensus__search`
- ClinicalTrials.gov：`mcp__plugin_bio-research_c-trials__*`
- 一般網路：`WebSearch`、`WebFetch`（Crossref API `https://api.crossref.org/works/<DOI>` 可用 WebFetch 或 Python requests）
- Notion、Google Drive、Gmail、Google Calendar MCP 存在但與本集無關。

## 5. bob-shared 檔案清單（其他 skill 只能引用這些路徑）

```
skills/bob-shared/
  SKILL.md                      （說明：僅供其他 bob-* 依賴，不單獨觸發）
  manifest.yaml
  README.md
  UPSTREAM.md
  core/reader-workflow.md               ← 上游保留（可繁中化）
  core/paper-type-taxonomy.md           ← 改寫：新增 qualitative / mixed-methods / dbr / scoping-review / quality-improvement 五型，保留 research / methods / hypothesis / algorithmic / review
  core/ethics.md                        ← 改寫：改為「APA／ICMJE／台灣 IRB／期刊 AI 揭露」語境，刪除 Nature Portfolio 政策段，保留紅黃綠燈框架
  core/terminology-ledger.md            ← 改寫：表格新增「中文定名」欄，規定中英對照一致
  core/consistency-sweep.md             ← 保留
  core/main-text-discipline.md          ← 保留（SI 改稱「附錄／補充資料」）
  core/discussion-argument-language.md  ← 保留
  core/introduction-funnel.md           ← 由上游 nature-introduction.md 改寫：去 Nature 專屬語境，改為健康科學／護理研究的問題漏斗（背景→重要性→缺口→目的）
  core/abstract-evidence-chain.md       ← 由上游 nature-abstract.md 改寫：支援結構式摘要（Background/Aim/Design/Methods/Results/Conclusion）與非結構式
  core/results-discussion-escalation.md ← 由上游 nature-results-discussion.md 改寫：去 Nature 專屬語境
  core/health-research-compliance.md    ← 由上游 research-compliance.md 改寫：IRB／知情同意／個資法／EQUATOR 準則路由表（CONSORT、STROBE、PRISMA-ScR、COREQ、SRQR、CHERRIES、TRIPOD+AI、DBR 報告要素）／生成式 AI 使用揭露
  core/zh-tw-academic-conventions.md    ← 新增：台灣學術中文慣例（全形標點、數字與單位、量表名稱、統計符號斜體、圖表編號、標楷體、APA 中文參考文獻慣例、常見大陸用語對照表）
  journal-formats/generic-health.md     ← 新增：健康科學期刊通用預設（IMRaD、結構式摘要、關鍵字、報告準則清單、資料可用性、利益衝突）
  journal-formats/nursing-journals.md   ← 新增：JAN、IJNS、NET、NEP、JNR、CIN 等的「投稿前必查項目清單」，不寫死數字，附官網連結欄位
  journal-formats/jmir.md               ← 新增：JMIR 系列特有（結構式摘要五段、Trial registration、Multimedia appendix、CHERRIES／CONSORT-EHEALTH）
  journal-formats/taiwan-nursing.md     ← 新增：護理雜誌、護理研究、台灣專科護理師學刊的中文投稿慣例（中英摘要並列、APA 中文格式）
  journal-formats/ndmc-thesis.md        ← 新增：國防醫學院碩士論文格式慣例（第一章至第五章結構、全形標點、標楷體、表 3-1 式編號、圖說樣式、目錄更新 F9），未確定處標「以所辦最新規範為準」
  scripts/check_consistency.py          ← 上游保留
  tests/test_check_consistency.py       ← 上游保留
```

## 6. 各 skill 改造要點

### bob-writing（來源 nature-writing）
- axes：`task`（manuscript / submission-package / **thesis-chapter**）、`paper_type`（research / methods / hypothesis / algorithmic / review / **qualitative / mixed-methods / dbr**）、`section`（abstract / intro / **literature-review** / method / results / discussion / conclusion / title / **thesis-ch1…ch5** 可用 `thesis-chapter` fragment 統一處理）、`language`（en / **zh-tw** / **zh-tw-to-en**）、`journal`（generic-health / nursing / jmir / taiwan-nursing / ndmc-thesis / nature-family〔保留但非預設〕）。
- 新增 fragments：`paper_type/qualitative.md`、`paper_type/mixed-methods.md`、`paper_type/dbr.md`、`section/literature-review.md`、`section/results.md`（上游叫 experiments，改名並保留檔）、`task/thesis-chapter.md`、`language/zh-tw.md`、`language/zh-tw-to-en.md`（由 zh-to-en 改寫）、`journal/generic-health.md`、`journal/nursing.md`、`journal/jmir.md`、`journal/taiwan-nursing.md`、`journal/ndmc-thesis.md`。
- 保留 references 全部；`references/submission-package.md` 與 templates 改為 Word／純文字 cover letter（LaTeX 模板可保留但標為選用）。
- 交接規則：整章 .docx → academic-writing；文獻回顧含系統性檢索 → scoping-review-master；概念分析 → concept-analysis-master。

### bob-polishing（來源 nature-polishing）
- axes 同上游，但 `language` 增 `zh-tw`（潤飾學術中文本身：去贅字、被動句、翻譯腔、統一術語、全形標點）與 `zh-tw-to-en`；`journal` 改為 generic-health / nursing / jmir / taiwan-nursing / ndmc-thesis。
- 保留 `references/latex-layout.md` 但新增 `references/word-layout.md`（Word 排版：表格跨頁、圖說、標楷體、目錄更新、段落間距）。
- 新增 `references/ai-trace-reduction.md`：學術文本去 AI 腔清單（英文與中文各一份），與 speak-human-tw 的分工說明。

### bob-reviewer（來源 nature-reviewer）
- 評審軸改為健康科學期刊常用：originality、clinical or educational significance、methodological rigour（依研究設計對應 EQUATOR 準則）、ethics and reporting transparency、clarity for interdisciplinary readers。
- 保留「3 位互盲審稿人 + 1 綜合」與凍結規則；`references/domain-specific-review-gates.md` 改寫為 `references/health-research-review-gates.md`：量性（RCT／類實驗／橫斷／世代）、質性（COREQ／SRQR、可信賴性四準則）、混合方法、系統性與範疇性回顧、教育介入與 DBR、AI／LLM 應用研究（TRIPOD+AI、CHART、評估集與洩漏風險）、問卷與量表發展（信效度、CVI、因素分析）。
- `references/editorial criteria and processes.md`（Nature 原文）刪除；`references/source-basis.md` 改為引用 ICMJE、COPE、EQUATOR 與典型護理期刊審稿表的公開原則。
- 輸出格式保留，加「中文核對」區塊（審稿人報告英文，綜合段附繁中摘要）。

### bob-response（來源 nature-response）
- 保留完整 workflow、interactive decision-type gate、互盲隱私過濾、accretion 控制。
- `references/chinese-author-alignment.md` 改為繁中、台灣語境；`references/latex-templates.md` 保留但新增 `templates/response-letter.md`（Word／Markdown 版逐點回覆表格：Comment / Response / Location of change）。
- 新增 `references/taiwan-journal-norms.md`：台灣中文期刊的修訂回覆慣例（回覆表、修改處以底線或色字標示、修訂說明書）。

### bob-citation（合併 nature-citation + nature-ref-verifier + nature-academic-search 的 wf2 引文驗證）
- 三個 workflow：`find-support`（把段落切成可引用句，用 PubMed MCP 找支持文獻，保守評級 direct / partial / background，匯出 RIS）、`verify`（DOI 解析→Crossref 欄位比對→嚴重度三級→報告；含 PMID 反查）、`export`（RIS／BibTeX／nbib 轉換，交 apa7-master 產 APA 7）。
- 期刊範圍：**不限 CNS**；預設 PubMed／MEDLINE 收錄之同儕審查期刊，可加條件「近 5 年」「護理／醫學教育／數位健康」；不做 CNS 白名單。
- 新增 `scripts/verify_dois.py`（純 Python，requests 或 urllib 查 Crossref，輸出 JSON／Markdown 比對表；含 `--pmid` 以 PubMed E-utilities 反查）與 `scripts/ris_tools.py`（RIS↔BibTeX↔nbib 轉換，可由上游 converters 改寫）。上游依賴 Scopus／ScienceDirect／CNKI／Zotero 寫入的部分全部刪除；Zotero 只保留「匯出 RIS 讓使用者手動匯入」。
- 輸出用繁中報告；示例改為護理文獻。

### bob-statistics（來源 nature-statistics）
- 去 Nature／NMI 專屬要求；改為 **APA 7 統計報告格式**（t(df) = x.xx, p = .xxx, d = x.xx；F、χ²、r、β、95% CI、η²）與護理研究常見分析：描述統計、t 檢定、ANOVA、卡方、相關、迴歸、信度（Cronbach's α）、效度（CVI、EFA／CFA）、GEE／混合模型、無母數、樣本數（G*Power）、SUS 計分與詮釋、質性資料的量化呈現。
- 新增 `references/apa7-statistics-format.md`、`references/nursing-instruments-reporting.md`、`references/spss-output-to-apa-table.md`（SPSS 輸出→APA 表格的對應與常見錯誤）、`references/sample-size-and-power.md`。
- 保留 `common-failure-modes.md`、`statistical-reporting.md`、`figure-statistics.md`、`reviewer-checklist.md`（繁中化或保留英文皆可，但去掉 Nature 專屬句）。

### bob-figure（來源 nature-figure，126 檔）
- 整目錄複製，只改：`SKILL.md`（繁中 router、觸發詞繁中、去 Nature／NMI 預設，改為「期刊投稿級 + 碩論 Word 插圖」）、`manifest.yaml`、新增 `static/fragments/target/thesis-word.md`（300 dpi PNG／TIFF、寬度 16 cm 內、中文字型標楷體或 Noto Sans TC、圖說在下、表題在上）與 `static/fragments/target/journal.md`。
- 保留 OpenRouter AI 示意圖路徑，但預設關閉，標為選用。
- 腳本一律不改；只把 `nature_figure_backend.py` 內的狀態檔路徑（若寫死 nature 名稱）改為 bob 名稱並確認能執行。

### bob-research-log（來源 nature-experiment-log）
- 改為「研究日誌」：適用 DBR 迭代紀錄、系統版本（V1–V7 這類）、使用者測試場次、IRB 進度、指導教授會議紀錄；輸出 Markdown 含 YAML frontmatter，路徑由使用者指定；刪除飛書；Obsidian 保留為選用。
- templates：`iteration-log.md`（DBR 迭代）、`meeting-log.md`（指導教授會議）、`test-session-log.md`（使用者測試）、`anomaly-log.md`、`index.md`。

## 7. 每個 skill 的驗收清單（改造者自檢，完成後在 UPSTREAM.md 末尾附上結果）

1. `SKILL.md` frontmatter：`name` 等於目錄名；`description` 含繁中觸發詞；無 `nature-` 字樣。
2. `manifest.yaml` 中每一個路徑都真實存在（含 `../bob-shared/...`）。
3. `python tools/s2twp.py --check <skill 內所有 .md .yaml>` 回傳 0。
4. `grep -r "nature-shared\|nature-writing\|nature-polishing\|nature-reviewer\|nature-response\|nature-citation\|nature-figure\|nature-statistics\|飞书\|微信\|抖音\|CNKI\|万方\|知识星球" skills/<name>` 只允許出現在 `UPSTREAM.md`。
5. README.md 的三個範例提示詞用台灣情境（例如：專科護理師、臨床推理、SUS、IRB、護理雜誌）。
6. 不新增任何硬編碼的期刊數字而未標註查核日期。
