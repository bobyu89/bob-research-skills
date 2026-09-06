#!/usr/bin/env python
"""Validate every skill under skills/ against ADAPTATION-SPEC section 7.

Checks per skill directory:
  1. SKILL.md exists, has frontmatter with name == directory name
  2. manifest.yaml (if present) parses; every path it references exists
  3. relative paths mentioned in SKILL.md / manifest.yaml (../bob-shared/... or local) exist
  4. forbidden strings (upstream names, mainland-only services) only appear in UPSTREAM.md
  5. no simplified-only Chinese characters in .md / .yaml (uses tools/s2twp.py logic)
  6. README.md and UPSTREAM.md exist
Exit 1 on any failure.
"""
import re, sys, pathlib, subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
FORBIDDEN = [
    "nature-shared", "nature-writing", "nature-polishing", "nature-reviewer",
    "nature-response", "nature-citation", "nature-figure", "nature-statistics",
    "nature-ref-verifier", "nature-academic-search", "nature-experiment-log",
    "飞书", "微信", "抖音", "CNKI", "万方", "知识星球", "萬方", "知識星球",
]
PATH_RE = re.compile(r"(?<![\w/])((?:\.\./|\./)?[\w./-]+?\.(?:md|yaml|yml|py|tex|R|json|txt))(?![\w/])")
SKIP_PATH_PREFIX = ("http", "figure.pdf", "figure.")

def frontmatter_name(text):
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if not m:
        return None
    n = re.search(r"^name:\s*(\S+)", m.group(1), re.M)
    return n.group(1).strip("'\"") if n else None

def yaml_paths(manifest_path):
    import yaml
    data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    out = []
    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in ("path", "consistency_script", "tests", "preference_script") and isinstance(v, str):
                    out.append(v)
                elif k in ("path", "tests") and isinstance(v, list):
                    out.extend(x for x in v if isinstance(x, str))
                else:
                    walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    walk(data)
    return out

def main():
    failures = []
    skills = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for sk in skills:
        name = sk.name
        skill_md = sk / "SKILL.md"
        if not skill_md.exists():
            failures.append(f"{name}: SKILL.md missing"); continue
        text = skill_md.read_text(encoding="utf-8")
        fm = frontmatter_name(text)
        if fm != name:
            failures.append(f"{name}: frontmatter name '{fm}' != dir name")
        for req in ("README.md", "UPSTREAM.md"):
            if not (sk / req).exists():
                failures.append(f"{name}: {req} missing")
        # paths in manifest
        manifest = sk / "manifest.yaml"
        refs = []
        if manifest.exists():
            try:
                refs += [(manifest, p) for p in yaml_paths(manifest)]
            except Exception as e:
                failures.append(f"{name}: manifest.yaml parse error: {e}")
        # paths in SKILL.md prose (only those that look like repo-relative)
        for m in PATH_RE.finditer(text):
            p = m.group(1)
            if p.startswith(SKIP_PATH_PREFIX) or p.count("/") == 0:
                continue
            refs.append((skill_md, p))
        for src, p in refs:
            if ".config/" in p:
                continue
            candidates = [sk / p, sk / "static" / p, ROOT / p]
            if not any(c.exists() for c in candidates):
                failures.append(f"{name}: {src.name} references missing path {p}")
        # forbidden strings and simplified chars
        for f in sk.rglob("*"):
            if not f.is_file() or f.suffix.lower() not in (".md", ".yaml", ".yml", ".py", ".json", ".txt", ".tex", ".r"):
                continue
            try:
                t = f.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            rel = f.relative_to(sk).as_posix()
            if f.name not in ("UPSTREAM.md", "zh-tw-academic-conventions.md"):
                for s in FORBIDDEN:
                    if s in t:
                        failures.append(f"{name}: forbidden '{s}' in {rel}")
                        break
    # simplified-character scan via s2twp --check
    mdfiles = [str(p) for p in SKILLS.rglob("*") if p.suffix in (".md", ".yaml", ".yml")]
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "s2twp.py"), "--check", *mdfiles],
                       capture_output=True, text=True, encoding="utf-8")
    if r.returncode != 0:
        for line in r.stdout.strip().splitlines():
            failures.append("simplified: " + line.replace(str(SKILLS) + "\\", "").replace(str(SKILLS) + "/", ""))
    print(f"skills checked: {', '.join(s.name for s in skills)}")
    if failures:
        print(f"\n{len(failures)} problem(s):")
        for f in failures:
            print(" -", f)
        sys.exit(1)
    print("all checks passed")

if __name__ == "__main__":
    main()
