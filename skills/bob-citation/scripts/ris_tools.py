#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ris_tools.py：RIS、BibTeX、nbib（MEDLINE）三種書目格式互轉、去重與完整性檢查。
只用 Python 標準函式庫（urllib、json、re、argparse），不需要安裝任何套件。

用法：
  python ris_tools.py convert INPUT [INPUT ...] --to ris|bib|nbib [-o OUT] [--dedupe]
  python ris_tools.py dedupe  INPUT [INPUT ...] [--to ris|bib|nbib] [-o OUT]
  python ris_tools.py check   INPUT [INPUT ...]
  python ris_tools.py fetch   [--pmid 35696315,12345678] [--doi 10.1111/jan.15321] --to ris [-o OUT]
                              [--ncbi-email you@example.com] [--mailto you@example.com]

  輸入格式依副檔名（.ris / .bib / .nbib / .txt）或內容自動判斷；多個輸入可混合格式，合併後輸出。
  --dedupe 以 DOI → PMID → 標題正規化 + 第一作者姓氏（Jaccard ≥ 0.90）三層鍵去重。
  --no-abstract 匯出時省略摘要，讓 EndNote／Zotero 匯入檔更精簡。

範例：
  python ris_tools.py convert refs.bib --to ris -o refs.ris
  python ris_tools.py convert pubmed-a.nbib pubmed-b.nbib zotero.ris --to bib --dedupe -o merged.bib
  python ris_tools.py fetch --pmid 35696315 --to ris -o jan15321.ris
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import textwrap
import time
import unicodedata
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

__version__ = "1.0.0"

EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
CROSSREF_BASE = "https://api.crossref.org/works"
REQUEST_DELAY = 0.35
STOPWORDS = {"a", "an", "the", "in", "of", "for", "on", "to", "and", "with", "by", "et", "al", "at", "from", "or"}

# ---------------------------------------------------------------------------
# 共用工具
# ---------------------------------------------------------------------------


def _configure_stdout() -> None:
    """Windows 主控台預設 cp950，遇到全形連字號或重音字母會炸；統一改成 UTF-8。"""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass


def clean_text(text: str | None) -> str:
    """去 HTML 標籤、統一空白。"""
    text = re.sub(r"<[^>]+>", " ", text or "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def normalize_doi(doi: str | None) -> str:
    doi = (doi or "").strip()
    doi = re.sub(r"^(?:https?://)?(?:dx\.)?doi\.org/", "", doi, flags=re.I)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.I)
    doi = doi.rstrip(".,;)")
    return doi.lower()


def normalize_title(title: str | None) -> str:
    """小寫、去重音、統一各種連字號、去標點與停用詞，供去重與相似度比對。"""
    text = unicodedata.normalize("NFKD", title or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = text.lower()
    text = re.sub(r"[‐-―−]", "-", text)
    text = re.sub(r"[^a-z0-9\s-]", " ", text)
    text = text.replace("-", " ")
    tokens = [t for t in text.split() if t not in STOPWORDS]
    return " ".join(tokens)


def normalize_surname(name: str | None) -> str:
    text = unicodedata.normalize("NFKD", name or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^a-z]", "", text.lower())


def first_author_surname(record: dict) -> str:
    authors = record.get("authors") or []
    if not authors:
        return ""
    first = authors[0]
    if "," in first:
        return first.split(",", 1)[0].strip()
    parts = first.split()
    return parts[0] if parts else ""


def jaccard(a: str, b: str) -> float:
    sa, sb = set(a.split()), set(b.split())
    if not sa or not sb:
        return 0.0
    return len(sa & sb) / len(sa | sb)


def author_to_family_given(name: str) -> str:
    """把各種作者寫法統一成「Family, Given」。

    - "Lyu, Meng-Meng"  → 原樣
    - "Lyu MM"（MEDLINE AU）→ "Lyu, MM"
    - "Meng-Meng Lyu"（BibTeX 自然序）→ "Lyu, Meng-Meng"
    - 團體作者（含 trailing comma 或多個大寫單字且無縮寫）→ 原樣
    """
    name = clean_text(name)
    if not name:
        return ""
    if name.endswith(","):
        return name  # 團體作者慣例
    if "," in name:
        family, given = name.split(",", 1)
        return f"{family.strip()}, {given.strip()}".rstrip(", ").rstrip()
    parts = name.split()
    if len(parts) == 1:
        return name
    last = parts[-1]
    if re.fullmatch(r"[A-Z]{1,4}", last) or re.fullmatch(r"(?:[A-Z]\.){1,4}", last):
        # MEDLINE 式「姓 縮寫」，可能還帶 Jr/2nd 等後綴
        return f"{' '.join(parts[:-1])}, {last}"
    if len(parts) >= 3 and re.fullmatch(r"(Jr|Sr|II|III|IV|2nd|3rd)\.?", last, flags=re.I):
        return f"{parts[-2]}, {' '.join(parts[:-2])}, {last}"
    return f"{last}, {' '.join(parts[:-1])}"


def author_incomplete(name: str) -> bool:
    """姓氏後沒有名字或縮寫（例如只有 "Chaudhuri"）視為不完整；團體作者不算。"""
    if not name or name.endswith(","):
        return False
    if "," not in name:
        return True
    family, given = name.split(",", 1)
    return not given.strip()


# ---------------------------------------------------------------------------
# 紀錄模型：內部一律用同一個 dict 結構
# ---------------------------------------------------------------------------


def new_record() -> dict:
    return {
        "type": "JOUR",
        "authors": [],  # ["Family, Given", ...]
        "title": "",
        "journal": "",
        "journal_abbrev": "",
        "year": "",
        "date": "",  # 原始日期字串（例如 2022 Oct）
        "volume": "",
        "issue": "",
        "start_page": "",
        "end_page": "",
        "doi": "",
        "pmid": "",
        "issn": "",
        "url": "",
        "abstract": "",
        "keywords": [],
        "source": "",  # PubMed / Crossref / 檔案來源
    }


def split_pages(pages: str) -> tuple[str, str]:
    pages = (pages or "").strip().replace("--", "-")
    pages = re.sub(r"[‐-―−]", "-", pages)
    if "-" in pages:
        sp, ep = pages.split("-", 1)
        return sp.strip(), ep.strip()
    return pages, ""


def pages_text(record: dict, sep: str = "-") -> str:
    if record.get("start_page") and record.get("end_page"):
        return f"{record['start_page']}{sep}{record['end_page']}"
    return record.get("start_page", "")


# ---------------------------------------------------------------------------
# 解析：nbib（MEDLINE）
# ---------------------------------------------------------------------------


def parse_medline_fields(nbib_text: str) -> dict:
    """把一筆 MEDLINE 文字拆成 tag -> [values]（沿用上游解析法，支援續行）。"""
    fields: dict = {}
    current_tag = None
    current_value: list = []
    for line in nbib_text.split("\n"):
        if len(line) >= 6 and line[0:4] != "    " and line[4:6] == "- ":
            if current_tag:
                fields.setdefault(current_tag, []).append(" ".join(current_value))
            current_tag = line[0:4].strip()
            current_value = [line[6:].strip()]
        elif line.startswith("      ") and current_tag:
            current_value.append(line[6:].strip())
        elif not line.strip():
            if current_tag:
                fields.setdefault(current_tag, []).append(" ".join(current_value))
            current_tag = None
            current_value = []
    if current_tag:
        fields.setdefault(current_tag, []).append(" ".join(current_value))
    return fields


def _first(fields: dict, tag: str) -> str:
    vals = fields.get(tag, [])
    return vals[0] if vals else ""


def _medline_doi(fields: dict) -> str:
    # LID / AID 可能先出現 [pii] 再出現 [doi]，要掃全部
    for tag in ("LID", "AID"):
        for val in fields.get(tag, []):
            if val and "[doi]" in val:
                return val.replace("[doi]", "").strip()
    return ""


def medline_fields_to_record(fields: dict) -> dict:
    rec = new_record()
    fau = fields.get("FAU", [])
    au = fields.get("AU", [])
    cn = fields.get("CN", [])  # 團體作者
    authors = fau if fau else au
    rec["authors"] = [author_to_family_given(a) for a in authors if a]
    rec["authors"] += [f"{clean_text(c)}," for c in cn if c]
    rec["title"] = clean_text(_first(fields, "TI")).rstrip(".")
    rec["journal"] = clean_text(_first(fields, "JT"))
    rec["journal_abbrev"] = clean_text(_first(fields, "TA"))
    dp = _first(fields, "DP")
    rec["date"] = dp
    rec["year"] = dp[:4] if dp[:4].isdigit() else ""
    rec["volume"] = _first(fields, "VI")
    rec["issue"] = _first(fields, "IP")
    rec["start_page"], rec["end_page"] = split_pages(_first(fields, "PG"))
    rec["doi"] = _medline_doi(fields)
    rec["pmid"] = _first(fields, "PMID")
    issn = [v for v in fields.get("IS", []) if "Linking" in v] or fields.get("IS", [])
    rec["issn"] = issn[0].split(" ")[0] if issn else ""
    rec["abstract"] = clean_text(_first(fields, "AB"))
    rec["keywords"] = [clean_text(m) for m in fields.get("MH", [])] + [clean_text(k) for k in fields.get("OT", [])]
    if rec["doi"]:
        rec["url"] = f"https://doi.org/{rec['doi']}"
    rec["source"] = "PubMed"
    return rec


def parse_medline(text: str) -> list[dict]:
    """一個 .nbib 檔可能含多筆紀錄（以空白行 + PMID- 分隔）。"""
    chunks = re.split(r"\n(?=PMID- )", "\n" + text.strip())
    records = []
    for chunk in chunks:
        chunk = chunk.strip("\n")
        if not chunk.strip():
            continue
        fields = parse_medline_fields(chunk)
        if fields:
            records.append(medline_fields_to_record(fields))
    return records


# ---------------------------------------------------------------------------
# 解析：RIS
# ---------------------------------------------------------------------------

RIS_LINE = re.compile(r"^([A-Z][A-Z0-9])  - ?(.*)$")


def parse_ris(text: str) -> list[dict]:
    records: list[dict] = []
    tags: list[tuple[str, str]] = []
    for raw in text.splitlines():
        line = raw.rstrip("\r")
        m = RIS_LINE.match(line)
        if m:
            tag, value = m.group(1), m.group(2).strip()
            if tag == "ER":
                if tags:
                    records.append(ris_tags_to_record(tags))
                tags = []
            else:
                tags.append((tag, value))
        elif line.strip() and tags:
            # 續行：接到前一個值
            tag, value = tags[-1]
            tags[-1] = (tag, f"{value} {line.strip()}")
    if tags:
        records.append(ris_tags_to_record(tags))
    return records


def ris_tags_to_record(tags: list[tuple[str, str]]) -> dict:
    rec = new_record()
    for tag, value in tags:
        if tag == "TY":
            rec["type"] = value or "JOUR"
        elif tag in ("AU", "A1", "A2"):
            rec["authors"].append(author_to_family_given(value))
        elif tag in ("TI", "T1") and not rec["title"]:
            rec["title"] = clean_text(value)
        elif tag in ("JO", "JF", "T2") and not rec["journal"]:
            rec["journal"] = clean_text(value)
        elif tag in ("JA", "J2") and not rec["journal_abbrev"]:
            rec["journal_abbrev"] = clean_text(value)
        elif tag in ("PY", "Y1", "DA") and not rec["year"]:
            m = re.search(r"(19|20)\d{2}", value)
            rec["year"] = m.group(0) if m else ""
            rec["date"] = value
        elif tag == "VL":
            rec["volume"] = value
        elif tag == "IS":
            rec["issue"] = value
        elif tag == "SP":
            sp, ep = split_pages(value)
            rec["start_page"] = sp
            if ep and not rec["end_page"]:
                rec["end_page"] = ep
        elif tag == "EP":
            rec["end_page"] = value
        elif tag == "DO":
            rec["doi"] = normalize_doi(value)
        elif tag == "AN" and "PMID" in value.upper():
            rec["pmid"] = re.sub(r"\D", "", value)
        elif tag == "UR" and not rec["url"]:
            rec["url"] = value
        elif tag in ("N2", "AB") and not rec["abstract"]:
            rec["abstract"] = clean_text(value)
        elif tag == "KW":
            rec["keywords"].append(clean_text(value))
        elif tag == "SN" and not rec["issn"]:
            rec["issn"] = value
        elif tag == "DB":
            rec["source"] = value
    if not rec["doi"] and rec["url"]:
        m = re.search(r"10\.\d{4,9}/[^\s]+", rec["url"])
        if m:
            rec["doi"] = normalize_doi(m.group(0))
    return rec


# ---------------------------------------------------------------------------
# 解析：BibTeX
# ---------------------------------------------------------------------------


def _split_bib_entries(text: str) -> list[tuple[str, str, str]]:
    """回傳 (entry_type, key, body)。用大括號配對切割，容忍巢狀大括號。"""
    entries = []
    for m in re.finditer(r"@(\w+)\s*\{", text):
        etype = m.group(1).lower()
        if etype in ("comment", "preamble", "string"):
            continue
        i = m.end()
        depth = 1
        j = i
        while j < len(text) and depth:
            if text[j] == "{":
                depth += 1
            elif text[j] == "}":
                depth -= 1
            j += 1
        body = text[i : j - 1]
        key, _, rest = body.partition(",")
        entries.append((etype, key.strip(), rest))
    return entries


def _parse_bib_fields(body: str) -> dict:
    fields: dict = {}
    i = 0
    n = len(body)
    while i < n:
        m = re.compile(r"\s*([\w\-]+)\s*=\s*", re.S).match(body, i)
        if not m:
            break
        name = m.group(1).lower()
        i = m.end()
        if i >= n:
            break
        if body[i] == "{":
            depth = 1
            j = i + 1
            while j < n and depth:
                if body[j] == "{":
                    depth += 1
                elif body[j] == "}":
                    depth -= 1
                j += 1
            value = body[i + 1 : j - 1]
            i = j
        elif body[i] == '"':
            j = i + 1
            while j < n and body[j] != '"':
                j += 1
            value = body[i + 1 : j]
            i = j + 1
        else:
            m2 = re.compile(r"[^,\n]+").match(body, i)
            value = m2.group(0) if m2 else ""
            i = m2.end() if m2 else n
        fields[name] = re.sub(r"\s+", " ", value).strip()
        m3 = re.compile(r"\s*,?\s*").match(body, i)
        i = m3.end() if m3 else i
    return fields


def _strip_braces(value: str) -> str:
    value = value.strip()
    while value.startswith("{") and value.endswith("}"):
        value = value[1:-1].strip()
    return value.replace("{", "").replace("}", "").replace("\\&", "&")


def parse_bibtex(text: str) -> list[dict]:
    records = []
    for etype, key, body in _split_bib_entries(text):
        f = _parse_bib_fields(body)
        rec = new_record()
        rec["type"] = "JOUR" if etype == "article" else etype.upper()
        rec["bib_key"] = key
        authors = _strip_braces(f.get("author", ""))
        rec["authors"] = [author_to_family_given(a) for a in re.split(r"\s+and\s+", authors) if a.strip()]
        rec["title"] = clean_text(_strip_braces(f.get("title", "")))
        rec["journal"] = clean_text(_strip_braces(f.get("journal", "") or f.get("journaltitle", "")))
        rec["journal_abbrev"] = clean_text(_strip_braces(f.get("shortjournal", "")))
        year = _strip_braces(f.get("year", "") or f.get("date", ""))
        m = re.search(r"(19|20)\d{2}", year)
        rec["year"] = m.group(0) if m else ""
        rec["volume"] = _strip_braces(f.get("volume", ""))
        rec["issue"] = _strip_braces(f.get("number", "") or f.get("issue", ""))
        rec["start_page"], rec["end_page"] = split_pages(_strip_braces(f.get("pages", "")))
        rec["doi"] = normalize_doi(_strip_braces(f.get("doi", "")))
        rec["pmid"] = re.sub(r"\D", "", _strip_braces(f.get("pmid", "")))
        rec["url"] = _strip_braces(f.get("url", ""))
        rec["abstract"] = clean_text(_strip_braces(f.get("abstract", "")))
        kw = _strip_braces(f.get("keywords", ""))
        rec["keywords"] = [k.strip() for k in re.split(r"[;,]", kw) if k.strip()]
        rec["issn"] = _strip_braces(f.get("issn", ""))
        rec["source"] = "BibTeX"
        if not rec["doi"] and rec["url"]:
            m = re.search(r"10\.\d{4,9}/[^\s]+", rec["url"])
            if m:
                rec["doi"] = normalize_doi(m.group(0))
        records.append(rec)
    return records


# ---------------------------------------------------------------------------
# 格式偵測與統一讀取
# ---------------------------------------------------------------------------


def detect_format(path: str, text: str) -> str:
    ext = os.path.splitext(path)[1].lower()
    if ext in (".nbib", ".medline"):
        return "nbib"
    if ext == ".ris":
        return "ris"
    if ext in (".bib", ".bibtex"):
        return "bib"
    head = text[:4000]
    if re.search(r"^PMID- ", head, flags=re.M):
        return "nbib"
    if re.search(r"^TY  - ", head, flags=re.M):
        return "ris"
    if re.search(r"@\w+\s*\{", head):
        return "bib"
    raise ValueError(f"無法判斷格式：{path}（請用 .ris / .bib / .nbib 副檔名）")


def read_records(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8-sig") as fh:
        text = fh.read()
    fmt = detect_format(path, text)
    if fmt == "nbib":
        return parse_medline(text)
    if fmt == "ris":
        return parse_ris(text)
    return parse_bibtex(text)


# ---------------------------------------------------------------------------
# 輸出：RIS
# ---------------------------------------------------------------------------


def record_to_ris(rec: dict, with_abstract: bool = True) -> str:
    lines = [f"TY  - {rec.get('type') or 'JOUR'}"]
    for au in rec.get("authors", []):
        lines.append(f"AU  - {au}")
    if rec.get("title"):
        lines.append(f"TI  - {rec['title']}")
    if rec.get("journal"):
        lines.append(f"JO  - {rec['journal']}")
        lines.append(f"T2  - {rec['journal']}")
    if rec.get("journal_abbrev"):
        lines.append(f"JA  - {rec['journal_abbrev']}")
    if rec.get("year"):
        lines.append(f"PY  - {rec['year']}")
    if rec.get("volume"):
        lines.append(f"VL  - {rec['volume']}")
    if rec.get("issue"):
        lines.append(f"IS  - {rec['issue']}")
    if rec.get("start_page"):
        lines.append(f"SP  - {rec['start_page']}")
    if rec.get("end_page"):
        lines.append(f"EP  - {rec['end_page']}")
    if rec.get("doi"):
        lines.append(f"DO  - {rec['doi']}")
        lines.append(f"UR  - https://doi.org/{rec['doi']}")
    elif rec.get("url"):
        lines.append(f"UR  - {rec['url']}")
    if rec.get("issn"):
        lines.append(f"SN  - {rec['issn']}")
    if with_abstract and rec.get("abstract"):
        lines.append(f"N2  - {rec['abstract']}")
    for kw in rec.get("keywords", []):
        lines.append(f"KW  - {kw}")
    if rec.get("pmid"):
        lines.append(f"AN  - PMID:{rec['pmid']}")
    if rec.get("source"):
        lines.append(f"DB  - {rec['source']}")
    lines.append("ER  - ")
    return "\n".join(lines) + "\n"


def records_to_ris(records: list[dict], with_abstract: bool = True) -> str:
    return "\n".join(record_to_ris(r, with_abstract) for r in records)


# ---------------------------------------------------------------------------
# 輸出：BibTeX
# ---------------------------------------------------------------------------


def _bib_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("&", "\\&") if value else ""


def make_bib_key(rec: dict, used: set) -> str:
    if rec.get("bib_key"):
        base = rec["bib_key"]
    elif rec.get("pmid"):
        base = f"pmid{rec['pmid']}"
    else:
        surname = normalize_surname(first_author_surname(rec)) or "anon"
        base = f"{surname}{rec.get('year') or 'nd'}"
    key = base
    suffix = ord("a")
    while key in used:
        key = f"{base}{chr(suffix)}"
        suffix += 1
    used.add(key)
    return key


def record_to_bib(rec: dict, key: str, with_abstract: bool = True) -> str:
    etype = "article" if (rec.get("type") or "JOUR").upper() == "JOUR" else rec["type"].lower()
    lines = [f"@{etype}{{{key},"]
    if rec.get("authors"):
        lines.append(f"  author   = {{{_bib_escape(' and '.join(rec['authors']))}}},")
    if rec.get("title"):
        lines.append(f"  title    = {{{{{_bib_escape(rec['title'])}}}}},")
    if rec.get("journal"):
        lines.append(f"  journal  = {{{_bib_escape(rec['journal'])}}},")
    if rec.get("year"):
        lines.append(f"  year     = {{{rec['year']}}},")
    if rec.get("volume"):
        lines.append(f"  volume   = {{{rec['volume']}}},")
    if rec.get("issue"):
        lines.append(f"  number   = {{{rec['issue']}}},")
    if rec.get("start_page"):
        lines.append(f"  pages    = {{{pages_text(rec, '--')}}},")
    if rec.get("doi"):
        lines.append(f"  doi      = {{{rec['doi']}}},")
        lines.append(f"  url      = {{https://doi.org/{rec['doi']}}},")
    elif rec.get("url"):
        lines.append(f"  url      = {{{rec['url']}}},")
    if rec.get("issn"):
        lines.append(f"  issn     = {{{rec['issn']}}},")
    if rec.get("pmid"):
        lines.append(f"  pmid     = {{{rec['pmid']}}},")
    if rec.get("keywords"):
        lines.append(f"  keywords = {{{_bib_escape('; '.join(rec['keywords']))}}},")
    if with_abstract and rec.get("abstract"):
        lines.append(f"  abstract = {{{_bib_escape(rec['abstract'])}}},")
    lines.append("}")
    return "\n".join(lines) + "\n"


def records_to_bib(records: list[dict], with_abstract: bool = True) -> str:
    used: set = set()
    return "\n".join(record_to_bib(r, make_bib_key(r, used), with_abstract) for r in records)


# ---------------------------------------------------------------------------
# 輸出：nbib（MEDLINE 風格，best-effort）
# ---------------------------------------------------------------------------


def _medline_line(tag: str, value: str) -> str:
    """MEDLINE 每行約 80 字元，續行縮排 6 格。"""
    prefix = f"{tag:<4}- "
    wrapped = textwrap.wrap(value, width=80, initial_indent=prefix, subsequent_indent="      ", break_long_words=False, break_on_hyphens=False)
    return "\n".join(wrapped) if wrapped else prefix


def _medline_au(name: str) -> str:
    """"Lyu, Meng-Meng" -> "Lyu MM"。"""
    if name.endswith(","):
        return name.rstrip(",")
    if "," not in name:
        return name
    family, given = name.split(",", 1)
    initials = "".join(part[0].upper() for part in re.split(r"[\s\-\.]+", given.strip()) if part)
    return f"{family.strip()} {initials}".strip()


def record_to_nbib(rec: dict, with_abstract: bool = True) -> str:
    lines = []
    if rec.get("pmid"):
        lines.append(_medline_line("PMID", rec["pmid"]))
    if rec.get("issn"):
        lines.append(_medline_line("IS", f"{rec['issn']} (Linking)"))
    if rec.get("volume"):
        lines.append(_medline_line("VI", rec["volume"]))
    if rec.get("issue"):
        lines.append(_medline_line("IP", rec["issue"]))
    if rec.get("date") or rec.get("year"):
        lines.append(_medline_line("DP", rec.get("date") or rec["year"]))
    if rec.get("title"):
        title = rec["title"] if rec["title"].endswith(".") else rec["title"] + "."
        lines.append(_medline_line("TI", title))
    if rec.get("start_page"):
        lines.append(_medline_line("PG", pages_text(rec)))
    if rec.get("doi"):
        lines.append(_medline_line("LID", f"{rec['doi']} [doi]"))
    if with_abstract and rec.get("abstract"):
        lines.append(_medline_line("AB", rec["abstract"]))
    for au in rec.get("authors", []):
        if au.endswith(","):
            lines.append(_medline_line("CN", au.rstrip(",")))
        else:
            lines.append(_medline_line("FAU", au))
            lines.append(_medline_line("AU", _medline_au(au)))
    if rec.get("journal_abbrev"):
        lines.append(_medline_line("TA", rec["journal_abbrev"]))
    if rec.get("journal"):
        lines.append(_medline_line("JT", rec["journal"]))
    for kw in rec.get("keywords", []):
        lines.append(_medline_line("OT", kw))
    if rec.get("doi"):
        lines.append(_medline_line("AID", f"{rec['doi']} [doi]"))
    return "\n".join(lines) + "\n"


def records_to_nbib(records: list[dict], with_abstract: bool = True) -> str:
    return "\n".join(record_to_nbib(r, with_abstract) for r in records)


WRITERS = {"ris": records_to_ris, "bib": records_to_bib, "nbib": records_to_nbib}
EXTENSIONS = {"ris": ".ris", "bib": ".bib", "nbib": ".nbib"}


# ---------------------------------------------------------------------------
# 去重（DOI → PMID → 標題 + 第一作者）
# ---------------------------------------------------------------------------

COMPLETENESS_FIELDS = ("doi", "pmid", "volume", "issue", "start_page", "end_page", "abstract", "journal", "year")


def completeness(rec: dict) -> int:
    return sum(1 for f in COMPLETENESS_FIELDS if rec.get(f)) + len(rec.get("authors", []))


def merge_records(keep: dict, other: dict) -> dict:
    """保留較完整的一筆，缺的欄位從另一筆補上。"""
    if completeness(other) > completeness(keep):
        keep, other = other, keep
    merged = dict(keep)
    for k, v in other.items():
        if k == "keywords":
            seen = set(merged.get("keywords", []))
            merged["keywords"] = merged.get("keywords", []) + [x for x in v if x not in seen]
        elif not merged.get(k) and v:
            merged[k] = v
    return merged


def is_same_record(a: dict, b: dict, title_threshold: float = 0.90) -> bool:
    if a.get("doi") and b.get("doi"):
        return normalize_doi(a["doi"]) == normalize_doi(b["doi"])
    if a.get("pmid") and b.get("pmid"):
        return a["pmid"] == b["pmid"]
    ta, tb = normalize_title(a.get("title")), normalize_title(b.get("title"))
    if not ta or not tb:
        return False
    sa, sb = normalize_surname(first_author_surname(a)), normalize_surname(first_author_surname(b))
    if sa and sb and sa != sb:
        return False
    return jaccard(ta, tb) >= title_threshold


def dedupe_records(records: list[dict]) -> tuple[list[dict], list[str]]:
    kept: list[dict] = []
    notes: list[str] = []
    for rec in records:
        for i, existing in enumerate(kept):
            if is_same_record(existing, rec):
                kept[i] = merge_records(existing, rec)
                label = rec.get("doi") or rec.get("pmid") or (rec.get("title") or "")[:60]
                notes.append(f"重複合併：{label}")
                break
        else:
            kept.append(rec)
    return kept, notes


# ---------------------------------------------------------------------------
# 完整性檢查（作者、關鍵欄位）
# ---------------------------------------------------------------------------


def check_records(records: list[dict]) -> list[dict]:
    report = []
    for idx, rec in enumerate(records, 1):
        issues = []
        if not rec.get("authors"):
            issues.append("沒有作者")
        else:
            bad = [a for a in rec["authors"] if author_incomplete(a)]
            if bad:
                issues.append("作者只有姓氏：" + "; ".join(bad))
        for field, label in (("title", "標題"), ("journal", "期刊"), ("year", "年份"), ("doi", "DOI")):
            if not rec.get(field):
                issues.append(f"缺 {label}")
        if not rec.get("volume"):
            issues.append("缺卷號")
        if not rec.get("start_page"):
            issues.append("缺頁碼或文章號")
        report.append({"index": idx, "label": rec.get("doi") or rec.get("pmid") or (rec.get("title") or "")[:60], "issues": issues})
    return report


# ---------------------------------------------------------------------------
# 線上取得：PubMed efetch、Crossref
# ---------------------------------------------------------------------------


def _http_get(url: str, headers: dict | None = None, retries: int = 2) -> bytes:
    last_err: Exception | None = None
    for attempt in range(retries + 1):
        try:
            req = Request(url, headers=headers or {"User-Agent": f"bob-citation-ris-tools/{__version__}"})
            with urlopen(req, timeout=30) as resp:
                return resp.read()
        except HTTPError as e:
            if e.code in (404, 400):
                raise
            last_err = e
        except URLError as e:
            last_err = e
        time.sleep(REQUEST_DELAY * (attempt + 1) * 2)
    raise last_err  # type: ignore[misc]


def fetch_pubmed_records(pmids: list[str], email: str | None = None) -> list[dict]:
    params = {"db": "pubmed", "id": ",".join(pmids), "rettype": "medline", "retmode": "text", "tool": "bob-citation"}
    if email:
        params["email"] = email
    time.sleep(REQUEST_DELAY)
    text = _http_get(f"{EUTILS_BASE}/efetch.fcgi?{urlencode(params)}").decode("utf-8")
    return parse_medline(text)


def crossref_to_record(msg: dict) -> dict:
    rec = new_record()
    for a in msg.get("author", []):
        if a.get("family"):
            rec["authors"].append(f"{clean_text(a['family'])}, {clean_text(a.get('given', ''))}".rstrip(", "))
        elif a.get("name"):
            rec["authors"].append(f"{clean_text(a['name'])},")
    rec["title"] = clean_text((msg.get("title") or [""])[0])
    rec["journal"] = clean_text((msg.get("container-title") or [""])[0])
    short = msg.get("short-container-title") or []
    rec["journal_abbrev"] = clean_text(short[0]) if short and short[0] != rec["journal"] else ""
    for key in ("published-print", "issued", "published-online"):
        parts = (msg.get(key) or {}).get("date-parts") or [[None]]
        if parts and parts[0] and parts[0][0]:
            rec["year"] = str(parts[0][0])
            rec["date"] = "-".join(str(p) for p in parts[0])
            break
    rec["volume"] = msg.get("volume", "") or ""
    rec["issue"] = msg.get("issue", "") or ""
    page = msg.get("page") or msg.get("article-number") or ""
    rec["start_page"], rec["end_page"] = split_pages(page)
    rec["doi"] = normalize_doi(msg.get("DOI", ""))
    issn = msg.get("ISSN") or []
    rec["issn"] = issn[0] if issn else ""
    rec["abstract"] = clean_text(msg.get("abstract", ""))
    rec["url"] = f"https://doi.org/{rec['doi']}" if rec["doi"] else ""
    rec["source"] = "Crossref"
    return rec


def fetch_crossref_record(doi: str, mailto: str | None = None) -> dict:
    doi = normalize_doi(doi)
    ua = f"bob-citation-ris-tools/{__version__}" + (f" (mailto:{mailto})" if mailto else "")
    url = f"{CROSSREF_BASE}/{doi}" + (f"?mailto={mailto}" if mailto else "")
    time.sleep(REQUEST_DELAY)
    data = json.loads(_http_get(url, headers={"User-Agent": ua}).decode("utf-8"))
    return crossref_to_record(data.get("message", data))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _write_output(text: str, output: str | None) -> None:
    if output:
        with open(output, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        print(f"已寫入：{os.path.abspath(output)}", file=sys.stderr)
    else:
        sys.stdout.write(text)


def _load_inputs(paths: list[str]) -> list[dict]:
    records: list[dict] = []
    for p in paths:
        recs = read_records(p)
        print(f"讀取 {p}：{len(recs)} 筆", file=sys.stderr)
        records.extend(recs)
    return records


def cmd_convert(args: argparse.Namespace) -> int:
    records = _load_inputs(args.inputs)
    if args.dedupe:
        records, notes = dedupe_records(records)
        for n in notes:
            print(n, file=sys.stderr)
        print(f"去重後：{len(records)} 筆", file=sys.stderr)
    _write_output(WRITERS[args.to](records, not args.no_abstract), args.output)
    return 0


def cmd_dedupe(args: argparse.Namespace) -> int:
    records = _load_inputs(args.inputs)
    before = len(records)
    records, notes = dedupe_records(records)
    for n in notes:
        print(n, file=sys.stderr)
    print(f"去重：{before} → {len(records)} 筆", file=sys.stderr)
    fmt = args.to
    if not fmt:
        with open(args.inputs[0], "r", encoding="utf-8-sig") as fh:
            fmt = detect_format(args.inputs[0], fh.read())
    _write_output(WRITERS[fmt](records, not args.no_abstract), args.output)
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    records = _load_inputs(args.inputs)
    report = check_records(records)
    problems = 0
    for item in report:
        if item["issues"]:
            problems += 1
            print(f"[{item['index']}] {item['label']}")
            for issue in item["issues"]:
                print(f"    - {issue}")
    print(f"共 {len(records)} 筆，{problems} 筆有待補欄位或作者不完整。")
    return 1 if problems else 0


def cmd_fetch(args: argparse.Namespace) -> int:
    records: list[dict] = []
    errors: list[str] = []
    pmids = [p.strip() for p in (args.pmid or "").split(",") if p.strip()]
    dois = [d.strip() for d in (args.doi or "").split(",") if d.strip()]
    if pmids:
        try:
            got = fetch_pubmed_records(pmids, args.ncbi_email)
            records.extend(got)
            print(f"PubMed：取得 {len(got)} 筆", file=sys.stderr)
        except Exception as e:  # noqa: BLE001
            errors.append(f"PubMed 取得失敗：{e}")
    for doi in dois:
        try:
            records.append(fetch_crossref_record(doi, args.mailto))
            print(f"Crossref：{doi} 取得", file=sys.stderr)
        except Exception as e:  # noqa: BLE001
            errors.append(f"Crossref {doi} 失敗：{e}")
    if args.dedupe:
        records, _ = dedupe_records(records)
    if records:
        _write_output(WRITERS[args.to](records, not args.no_abstract), args.output)
    for e in errors:
        print(e, file=sys.stderr)
    if not records:
        print("沒有取得任何紀錄。", file=sys.stderr)
        return 1
    return 0 if not errors else 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ris_tools.py", description="RIS / BibTeX / nbib 互轉、去重與檢查（bob-citation）")
    parser.add_argument("--version", action="version", version=f"ris_tools {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("-o", "--output", help="輸出檔；省略則印到標準輸出")
    common.add_argument("--no-abstract", action="store_true", help="輸出時省略摘要")

    p = sub.add_parser("convert", parents=[common], help="轉換格式（可多檔合併）")
    p.add_argument("inputs", nargs="+")
    p.add_argument("--to", choices=WRITERS, required=True)
    p.add_argument("--dedupe", action="store_true", help="合併時以 DOI／PMID／標題去重")
    p.set_defaults(func=cmd_convert)

    p = sub.add_parser("dedupe", parents=[common], help="去重（輸出格式預設同第一個輸入）")
    p.add_argument("inputs", nargs="+")
    p.add_argument("--to", choices=WRITERS)
    p.set_defaults(func=cmd_dedupe)

    p = sub.add_parser("check", help="檢查作者完整性與缺欄位")
    p.add_argument("inputs", nargs="+")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("fetch", parents=[common], help="由 PMID（PubMed）或 DOI（Crossref）取得書目並輸出")
    p.add_argument("--pmid", help="PMID，逗號分隔")
    p.add_argument("--doi", help="DOI，逗號分隔")
    p.add_argument("--to", choices=WRITERS, default="ris")
    p.add_argument("--dedupe", action="store_true")
    p.add_argument("--ncbi-email", help="E-utilities 的 email 參數（建議填）")
    p.add_argument("--mailto", help="Crossref polite pool 的 email")
    p.set_defaults(func=cmd_fetch)
    return parser


def main(argv: list[str] | None = None) -> int:
    _configure_stdout()
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
