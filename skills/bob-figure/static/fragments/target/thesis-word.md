# 交付目標：碩論 Word 插圖（thesis-word）

適用於碩士論文、計畫書、口試附圖，以及任何最終要貼進 Word 的中文圖。本片段覆蓋後端片段中的字型與匯出預設；其餘（對齊閘門、碰撞稽核、資料完整性）照常。

## 匯出契約

| 項目 | 規格 |
|---|---|
| 檔案格式 | **PNG 或 TIFF，300 dpi**（PNG 檔案小、Word 相容性好；有多層灰階或影像時用 TIFF）。同時保留一份向量 PDF 供稽核與日後改投期刊。 |
| 圖寬 | **不超過 16 cm**（A4 直式、左右 2.5 cm 邊界的可用寬度約 16 cm；實際以所辦規範為準）。常用寬度：單圖 12 到 14 cm，多面板 15 到 16 cm。 |
| 圖高 | 不超過 20 cm，避免圖說被推到下一頁；超過時拆成兩張圖或減少面板。 |
| 插入後不縮放 | 以最終尺寸匯出，插入 Word 後**不再拖曳縮放**；縮放會讓字級失控、線寬變細。若 Word 顯示的尺寸不對，回頭改匯出尺寸。 |
| 中文字型 | **標楷體（DFKai-SB）** 與論文正文一致；跨平台或無標楷體時用 **Noto Sans TC**。英文與數字可用 Times New Roman 或與正文相同字型。同一張圖只用一種中文字型。 |
| 字級 | 圖內文字以最終尺寸量測 9 到 11 pt（與正文 12 pt 相比略小），最小不低於 8 pt；面板標籤（a、b、c 或（a）、（b））粗體 11 到 12 pt。 |
| 顏色 | **單色列印可讀**：不同組別用線型、標記形狀或灰階區分，顏色只是輔助；配色同時要色盲友善。口試委員常拿黑白列印稿。 |
| 背景 | 白底、無外框、去除多餘格線；圖內不放標題（標題在圖說）。 |

## 圖說與編號慣例

- **圖說在圖下方，表題在表上方**。圖說格式「圖 3-1　研究架構圖」：章號連字號流水號，圖號後空一個全形空格再接題名，題名末尾不加句號；表題同理「表 4-2　受試者基本資料（N = 30）」。
- 圖說文字由 Word 的標題樣式或所辦範本控制，**不要把圖說畫進圖片裡**；本 skill 只交付圖檔與圖說文字。
- 圖說內的統計符號斜體（*n*、*p*、*M*、*SD*）、誤差線定義（平均值 ± 標準差或 95% CI）、樣本數，都寫進圖說文字，交由 `docx` 插入時套樣式。
- 圖內文字用全形標點與台灣用語（「使用者」「資料」「回饋」）；座標軸標題含單位，例如「反應時間（秒）」。
- 圖號在正文中的引用寫「如圖 3-1 所示」，圖說編號與正文引用一致；需要國防醫學院碩論細節時載入 `../bob-shared/journal-formats/ndmc-thesis.md`，一般台灣學術中文慣例載入 `../bob-shared/core/zh-tw-academic-conventions.md`。未確定處以所辦最新規範為準。

## 交付清單

1. `figure-3-1.png`（或 `.tiff`）：300 dpi、寬度不超過 16 cm、白底。
2. `figure-3-1.pdf`：同一後端匯出的向量版，供稽核與改投期刊。
3. 圖說文字（純文字，含圖號、題名、統計註記）。
4. 資料來源與排除紀錄（若有）。
5. 對齊 JSON 與碰撞稽核 JSON（多面板圖必附）。

## Python（matplotlib）中文字型與負號設定

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 依序嘗試標楷體與 Noto Sans TC；都沒有時回報缺字型，不要用預設字型交付
CANDIDATES = ["DFKai-SB", "標楷體", "Noto Sans TC", "Microsoft JhengHei"]
available = {f.name for f in font_manager.fontManager.ttflist}
zh_font = next((name for name in CANDIDATES if name in available), None)
if zh_font is None:
    raise SystemExit("找不到標楷體或 Noto Sans TC，請先安裝字型再匯出碩論插圖")

mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": [zh_font, "Times New Roman", "DejaVu Sans"],
    "axes.unicode_minus": False,   # 讓負號正常顯示，避免出現方框
    "font.size": 10,
    "axes.titlesize": 10,
    "axes.labelsize": 10,
    "legend.fontsize": 9,
    "xtick.labelsize": 9,
    "ytick.labelsize": 9,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "legend.frameon": False,
    "pdf.fonttype": 42,            # PDF 內嵌可編輯字型
    "savefig.dpi": 300,
})

CM = 1 / 2.54

def save_thesis(fig, stem, width_cm=15.0, height_cm=9.0):
    """以最終尺寸匯出 300 dpi PNG 與向量 PDF；插入 Word 後不再縮放。"""
    fig.set_size_inches(width_cm * CM, height_cm * CM)
    fig.savefig(f"{stem}.png", dpi=300, bbox_inches="tight", facecolor="white")
    fig.savefig(f"{stem}.pdf", bbox_inches="tight", facecolor="white")
```

字型名稱在不同系統可能不同（Windows 內建標楷體多為 `DFKai-SB`），先用 `font_manager` 列出實際名稱再填。若使用 `bbox_inches="tight"`，匯出後用影像尺寸換算確認寬度仍在 16 cm 以內。

## R（ggplot2）對應設定

```r
library(ggplot2)
library(showtext)
font_add("DFKai-SB", regular = "kaiu.ttf")   # Windows 標楷體；macOS／Linux 改用 Noto Sans TC 檔案路徑
showtext_auto()
theme_set(theme_classic(base_size = 10, base_family = "DFKai-SB") +
  theme(legend.position = "bottom", plot.title = element_blank()))
ggsave("figure-3-1.png", plot, width = 15, height = 9, units = "cm", dpi = 300, bg = "white")
ggsave("figure-3-1.pdf", plot, width = 15, height = 9, units = "cm", device = cairo_pdf)
```

## 常見錯誤

- 圖內出現方框或問號：中文字型或負號沒設定。
- 插入 Word 後文字糊掉：匯出解析度低於 300 dpi，或插入後被拖曳放大。
- 圖說寫在圖裡：口試修訂時無法改字，且與所辦樣式不一致。
- 彩色列印才能區分組別：加線型或標記形狀，改成單色可讀。
- 圖寬超過版面被 Word 自動縮小：字級跟著變小，重新以 16 cm 內匯出。
