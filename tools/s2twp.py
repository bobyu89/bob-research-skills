#!/usr/bin/env python
"""Convert simplified Chinese text files to Taiwan traditional (OpenCC s2twp).
Usage: python tools/s2twp.py FILE [FILE ...]   (in-place)
       python tools/s2twp.py --check FILE ...  (report files containing simplified-only chars, exit 1 if any)
"""
import sys, io, re, pathlib
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
try:
    import opencc
except ImportError:
    sys.exit("pip install opencc-python-reimplemented")
cc = opencc.OpenCC('s2twp')
# common simplified-only characters (never valid in Taiwan traditional text)
SIMP = "数论审软质优项络频视馈户开组题义认识说读书长关检验术见观电计设结经统学时间实现应该变为从与这们过还没这样问题发现发展样种统计确认议论谈话调节报导资讯数据网络编写"
SIMP = "".join(sorted(set(c for c in SIMP if cc.convert(c) != c)))
pat = re.compile("[" + re.escape(SIMP) + "]")
check = sys.argv[1] == "--check"
files = sys.argv[2:] if check else sys.argv[1:]
bad = 0
for f in files:
    p = pathlib.Path(f)
    txt = p.read_text(encoding="utf-8")
    if check:
        hits = pat.findall(txt)
        if hits:
            bad += 1
            print(f"{f}: {len(hits)} simplified chars, e.g. {''.join(sorted(set(hits))[:12])}")
    else:
        new = cc.convert(txt)
        if new != txt:
            p.write_text(new, encoding="utf-8")
            print(f"converted: {f}")
sys.exit(1 if bad else 0)
