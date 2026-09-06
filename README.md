# bob-research-skills

游明勳（Bob）的個人科研 skill 集。以 [nature-skills](https://github.com/Yuan1z0825/nature-skills) 的「短 router + manifest + 靜態片段 + 按需參考」架構為底，
全面改寫成 **台灣繁體中文、護理／健康科學、APA 第七版、國防醫學院碩士論文** 的語境，
並與 Claude 環境裡既有的 `academic-writing`、`apa7-master`、`scoping-review-master`、`academic-peer-reviewer` 等 skill 分工，不重複造輪子。

## 技能索引

| Skill | 用途 | 典型提示詞 |
|---|---|---|
| `bob-shared` | 共用參考層（研究類型分類、術語帳、主文精簡、討論論證、健康研究合規與 EQUATOR 路由、台灣學術中文慣例、期刊與碩論格式），僅供其他 bob-* 載入 | 不直接呼叫 |
| `bob-writing` | 論證架構與段落任務：摘要、緒論、文獻探討、方法、結果、討論、結論、投稿信；碩論五章；DBR／質性／混合方法 | 「幫我用這些結果起草討論段」「第三章研究方法的段落怎麼排」 |
| `bob-polishing` | 學術英文與學術中文潤飾、中翻英、去 AI 腔、結果段精簡、Word／LaTeX 排版 | 「把這段改成投稿級英文，術語不要變」「這段中文太翻譯腔，幫我順」 |
| `bob-reviewer` | 三位互盲審稿人模擬 + 綜合報告，依研究設計套用 EQUATOR 準則的審查關卡 | 「用三位審稿人的角度審這篇，先各自寫完再綜合」 |
| `bob-response` | 審稿意見逐點回覆、修訂 cover letter、修改處標示、口試委員意見回覆表 | 「這是退修信，幫我分審稿人寫逐點回覆」 |
| `bob-citation` | 用 PubMed 為段落找支持文獻、DOI／欄位查證、RIS／BibTeX 匯出（APA 格式交 apa7-master） | 「幫這段配文獻，近五年、護理教育」「核對這 30 條參考文獻的 DOI」 |
| `bob-statistics` | 統計報告審查與撰寫：APA 統計格式、SPSS 報表轉表格、信效度、SUS、樣本數與檢定力 | 「把這份 SPSS 輸出整理成 APA 表」「審稿人說樣本數不夠，怎麼回」 |
| `bob-figure` | 投稿級與碩論用科研圖（Python／R），多面板對齊與碰撞稽核，中文字型設定 | 「用 matplotlib 畫 SUS 前後測比較圖，碩論用 300 dpi」 |
| `bob-research-log` | 研究日誌：DBR 迭代、指導教授會議、使用者測試場次、IRB 進度 | 「幫我把今天第 4 輪測試的紀錄整理成研究日誌」 |

## 安裝

```powershell
.\install.ps1          # 複製到 %USERPROFILE%\.claude\skills，開新對話後生效
.\install.ps1 -Check   # 只比對差異
```

macOS／Linux：`./install.sh`（`--dest ~/.codex/skills` 可裝到 Codex）。

## 驗證

```bash
python tools/validate.py
```

檢查 frontmatter 名稱、manifest 路徑、禁用字串、殘留簡體字。`tools/s2twp.py` 可把簡體檔轉成台灣繁體。

## 與既有 skill 的分工

| 既有 skill | 負責 | bob-* 交接時機 |
|---|---|---|
| `academic-writing` | 整章撰寫、APA 內文引用、輸出 .docx | bob-writing 定好論證與段落後，要出整章 Word 時 |
| `apa7-master` | APA 7 參考文獻格式 | bob-citation 找到並驗證文獻後 |
| `citation-verifier` | 引文真實性 | bob-citation verify 之外的深查 |
| `scoping-review-master` 等報告準則 skill | JBI／PRISMA／CONSORT／STROBE | bob-writing、bob-reviewer 遇到對應設計時 |
| `academic-peer-reviewer` | 單一資深審稿人深度批判 | 不需要三位互盲時 |
| `speak-human-tw` | 講人話 | 非學術文本 |
| `docx` / `pptx` / `xlsx` / `pdf` | 檔案輸出 | 任何需要檔案時 |

完整分工表見 [ADAPTATION-SPEC.md](ADAPTATION-SPEC.md) 第 4 節。

## 上游與授權

衍生自 nature-skills（Apache-2.0），上游版本 `28150f30`（2026-09-06）。每個 skill 的 `UPSTREAM.md` 逐檔記錄保留、改寫、新增、刪除，方便日後對照上游更新。
上游穩定副本放在 `~/ai-skills/nature-skills`；要看上游新功能時 `git pull` 後對照 UPSTREAM.md 手動搬。

未納入的上游 skill（可直接從上游副本用）：`nature-reader`（本地已有 `paper-analysis`）、`nature-paper2ppt`／`nature-image2ppt`（已有 `grad-lecture-to-slides`）、`nature-paper-card`、`nature-paper-to-patent`、`nature-downloader`、`nature-literature-pipeline`（已有 `pubmed-daily-bundle`）、`nature-proposal-writer`、`nature-data`。
