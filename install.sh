#!/usr/bin/env bash
# 把 skills/ 下的每個 bob-* skill 複製到 Claude Code 的技能目錄（預設 ~/.claude/skills）。
# 用法：
#   ./install.sh                 # 安裝或更新全部
#   ./install.sh --check         # 只比對差異，不寫入
#   ./install.sh --dest ~/.codex/skills
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEST="$HOME/.claude/skills"
CHECK=0
while [ $# -gt 0 ]; do
  case "$1" in
    --dest) DEST="$2"; shift 2 ;;
    --check) CHECK=1; shift ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done
mkdir -p "$DEST"
n=0
for d in "$HERE"/skills/*/; do
  name="$(basename "$d")"
  if [ "$CHECK" = 1 ]; then
    if [ ! -d "$DEST/$name" ]; then echo "[缺少] $name"; n=$((n+1)); continue; fi
    if diff -rq --exclude=__pycache__ "$d" "$DEST/$name" >/dev/null; then echo "[一致] $name"; else echo "[有差異] $name"; n=$((n+1)); fi
  else
    rm -rf "$DEST/$name"
    cp -R "$d" "$DEST/$name"
    find "$DEST/$name" -name __pycache__ -type d -prune -exec rm -rf {} + 2>/dev/null || true
    echo "[已安裝] $name -> $DEST/$name"; n=$((n+1))
  fi
done
if [ "$CHECK" = 1 ]; then echo; echo "比對完成：$n 個 skill 需要更新"; else echo; echo "完成：$n 個 skill 已同步到 $DEST（開新對話後生效）"; fi
