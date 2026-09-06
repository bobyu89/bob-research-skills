# 把 skills/ 下的每個 bob-* skill 複製到 Claude Code 的技能目錄（預設 ~/.claude/skills）。
# 用法：
#   .\install.ps1            # 安裝或更新全部
#   .\install.ps1 -Check     # 只比對差異，不寫入
#   .\install.ps1 -Dest "C:\path\to\skills"
param(
    [string]$Dest = (Join-Path $HOME ".claude\skills"),
    [switch]$Check
)
$ErrorActionPreference = "Stop"
$src = Join-Path $PSScriptRoot "skills"
if (-not (Test-Path $src)) { throw "找不到 $src" }
if (-not (Test-Path $Dest)) { New-Item -ItemType Directory -Force $Dest | Out-Null }

$changed = 0
Get-ChildItem $src -Directory | ForEach-Object {
    $name = $_.Name
    $target = Join-Path $Dest $name
    if ($Check) {
        if (-not (Test-Path $target)) { Write-Host "[缺少] $name"; $script:changed++; return }
        $a = Get-ChildItem $_.FullName -Recurse -File | ForEach-Object { $_.FullName.Substring($_.FullName.IndexOf($name)) + "|" + (Get-FileHash $_.FullName -Algorithm MD5).Hash }
        $b = Get-ChildItem $target -Recurse -File | ForEach-Object { $_.FullName.Substring($_.FullName.IndexOf($name)) + "|" + (Get-FileHash $_.FullName -Algorithm MD5).Hash }
        $diff = Compare-Object $a $b
        if ($diff) { Write-Host "[有差異] $name ($($diff.Count) 處)"; $script:changed++ } else { Write-Host "[一致] $name" }
    } else {
        if (Test-Path $target) { Remove-Item $target -Recurse -Force }
        Copy-Item $_.FullName $target -Recurse
        Get-ChildItem $target -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "[已安裝] $name -> $target"
        $script:changed++
    }
}
if ($Check) { Write-Host "`n比對完成：$changed 個 skill 需要更新" } else { Write-Host "`n完成：$changed 個 skill 已同步到 $Dest（開新對話後生效）" }
