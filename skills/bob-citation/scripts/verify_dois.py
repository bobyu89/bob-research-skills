#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
verify_dois.py：把參考文獻清單逐筆送 Crossref（DOI）或 PubMed（PMID）核對，輸出欄位比對表。
只用 Python 標準函式庫（urllib、json、difflib），不需要安裝任何套件。

用法：
  python verify_dois.py --input refs.bib [--mailto you@example.com] [--json out.json] [--md out.md]
  python verify_dois.py --input refs.ris
  python verify_dois.py --input refs.txt            # 每行「[n] 引用文字 … DOI」或 APA 7 一筆一行
  python verify_dois.py --doi 10.1111/jan.15321 --doi 10.1016/j.nedt.2020.104654
  python verify_dois.py --pmid 35696315             # PMID 反查（E-utilities esummary），列出 DOI 與書目
  python verify_dois.py --input refs.txt --search-missing   # 無 DOI 的條目用 Crossref 書目查詢找候選 DOI

嚴重度（沿用上游 ref-verifier 的三級制）：
  🔴 critical：DOI 無法解析、DOI 指向另一篇、第一作者不符、頁碼差 ≥ 5、年份差 ≥ 2
  🟡 warning ：上線年與卷年不一致、卷期不符、頁碼差 ≤ 4、期刊名不符
  🟢 info    ：僅大小寫、標點、縮寫差異
  狀態：✅ Verified／⚠️ Check suggested／❌ Needs fix／❓ Unverifiable
"""

from __future__ import annotations

import argparse
import difflib
import json
import os
import re
import sys
import time
from datetime import date
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ris_tools as rt  # noqa: E402

__version__ = "1.0.0"
CROSSREF_BASE = "https://api.crossref.org/works"
EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
REQUEST_DELAY = 0.35

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s\"<>]+", re.I)
PMID_RE = re.compile(r"PMID:?\s*(\d{6,9})", re.I)
YEAR_RE = re.compile(r"\((19|20)\d{2}[a-z]?\)")

LEVEL_ICON = {"crit": "🔴", "warn": "🟡", "info": "🟢", "ok": "✅", "na": "－"}
STATUS_ICON = {"verified": "✅ Verified", "check": "⚠️ Check suggested", "fix": "❌ Needs fix", "unverifiable": "❓ Unverifiable"}


# ---------------------------------------------------------------------------
# 網路
# ---------------------------------------------------------------------------


def http_get_json(url: str, user_agent: str, retries: int = 2) -> dict:
    last: Exception | None = None
    for attempt in range(retries + 1):
        try:
            req = Request(url, headers={"User-Agent": user_agent, "Accept": "application/json"})
            with urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except HTTPError as e:
            if e.code == 404:
                raise
            last = e
        except URLError as e:
            last = e
        time.sleep(REQUEST_DELAY * (attempt + 1) * 2)
    raise last  # type: ignore[misc]


def crossref_lookup(doi: str, mailto: str | None) -> dict | None:
    """回傳 Crossref message；404 回傳 None；其他錯誤往上丟。"""
    ua = f"bob-citation-verify/{__version__}" + (f" (mailto:{mailto})" if mailto else "")
    url = f"{CROSSREF_BASE}/{quote(doi, safe='/()')}"
    if mailto:
        url += f"?mailto={mailto}"
    time.sleep(REQUEST_DELAY)
    try:
        return http_get_json(url, ua).get("message")
    except HTTPError as e:
        if e.code == 404:
            return None
        raise


def crossref_search(bibliographic: str, mailto: str | None, rows: int = 3) -> list[dict]:
    ua = f"bob-citation-verify/{__version__}" + (f" (mailto:{mailto})" if mailto else "")
    params = {"query.bibliographic": bibliographic[:400], "rows": rows, "select": "DOI,title,author,issued,container-title,volume,page,score"}
    if mailto:
        params["mailto"] = mailto
    time.sleep(REQUEST_DELAY)
    data = http_get_json(f"{CROSSREF_BASE}?{urlencode(params)}", ua)
    return data.get("message", {}).get("items", [])


def pubmed_esummary(pmids: list[str], email: str | None) -> dict:
    params = {"db": "pubmed", "id": ",".join(pmids), "retmode": "json", "tool": "bob-citation"}
    if email:
        params["email"] = email
    time.sleep(REQUEST_DELAY)
    data = http_get_json(f"{EUTILS_BASE}/esummary.fcgi?{urlencode(params)}", f"bob-citation-verify/{__version__}")
    return data.get("result", {})


def esummary_to_record(doc: dict) -> dict:
    rec = rt.new_record()
    rec["title"] = rt.clean_text(doc.get("title", "")).rstrip(".")
    rec["authors"] = [rt.author_to_family_given(a.get("name", "")) for a in doc.get("authors", []) if a.get("name")]
    rec["journal"] = rt.clean_text(doc.get("fulljournalname", ""))
    rec["journal_abbrev"] = rt.clean_text(doc.get("source", ""))
    pubdate = doc.get("pubdate", "") or doc.get("epubdate", "")
    rec["date"] = pubdate
    rec["year"] = pubdate[:4] if pubdate[:4].isdigit() else ""
    rec["online_year"] = (doc.get("epubdate", "") or "")[:4]
    rec["volume"] = doc.get("volume", "") or ""
    rec["issue"] = doc.get("issue", "") or ""
    rec["start_page"], rec["end_page"] = rt.split_pages(doc.get("pages", "") or "")
    for ident in doc.get("articleids", []):
        if ident.get("idtype") == "doi":
            rec["doi"] = rt.normalize_doi(ident.get("value", ""))
        elif ident.get("idtype") == "pubmed":
            rec["pmid"] = ident.get("value", "")
    rec["source"] = "PubMed"
    return rec


def crossref_message_to_record(msg: dict) -> dict:
    rec = rt.crossref_to_record(msg)
    online = (msg.get("published-online") or {}).get("date-parts") or [[None]]
    printed = (msg.get("published-print") or {}).get("date-parts") or [[None]]
    rec["online_year"] = str(online[0][0]) if online and online[0] and online[0][0] else ""
    rec["print_year"] = str(printed[0][0]) if printed and printed[0] and printed[0][0] else ""
    rec["type"] = msg.get("type", "")
    rec["article_number"] = msg.get("article-number", "") or ""
    return rec


# ---------------------------------------------------------------------------
# 純文字引用行解析（APA 7 或「[n] … DOI」）
# ---------------------------------------------------------------------------


def parse_text_line(line: str) -> dict:
    """盡力從一行引用文字抽出識別碼與可比對欄位；抽不到的欄位留空，不列入比對。"""
    rec = rt.new_record()
    rec["raw"] = line.strip()
    label = re.match(r"^\s*(\[\d+\]|\d+[.)])\s*", line)
    rec["label"] = label.group(1) if label else ""
    body = line[label.end():] if label else line
    body = body.strip()

    m = DOI_RE.search(body)
    if m:
        rec["doi"] = rt.normalize_doi(m.group(0))
    m = PMID_RE.search(body)
    if m:
        rec["pmid"] = m.group(1)

    # APA 7：Family, G. G., Family, G., & Family, G. (Year). Title. Journal, Vol(Issue), pages. https://doi.org/...
    ym = YEAR_RE.search(body)
    if ym:
        rec["year"] = ym.group(0)[1:5]
        authors_part = body[: ym.start()].strip().rstrip(".").rstrip(",")
        rest = body[ym.end():].lstrip(". ").strip()
        # 標題：到第一個「. 」或「? 」為止（但避免在縮寫如 "e.g." 上斷開）
        tm = re.match(r"(.+?[.?!])\s+(?=[A-Z\u4e00-\u9fff])", rest)
        if tm:
            rec["title"] = tm.group(1).rstrip(".?!").strip()
            after = rest[tm.end():]
            jm = re.match(r"([^,]+?),\s*(\d+[A-Za-z]?)(?:\s*\(([^)]+)\))?,?\s*([A-Za-z]?\d+(?:\s*[‐-―−-]\s*[A-Za-z]?\d+)?)?", after)
            if jm:
                rec["journal"] = jm.group(1).strip().rstrip(".")
                rec["volume"] = jm.group(2) or ""
                rec["issue"] = jm.group(3) or ""
                rec["start_page"], rec["end_page"] = rt.split_pages(jm.group(4) or "")
            else:
                jm2 = re.match(r"([^,.]+)", after)
                if jm2 and not rec["journal"]:
                    rec["journal"] = jm2.group(1).strip()
        authors = [a for a in re.split(r",\s*(?=[A-Z][A-Za-z'’\-]+,)|,\s*&\s*|\s*&\s*|,\s*and\s+", authors_part) if a.strip()]
        rec["authors"] = [rt.author_to_family_given(a.strip().rstrip(",")) for a in authors] if authors else []
    else:
        # 非 APA：第一個逗號前當第一作者，找 4 位數年份
        first = re.split(r"[,.]", body, 1)[0].strip()
        if first and len(first.split()) <= 4:
            rec["authors"] = [rt.author_to_family_given(first)]
        y = re.search(r"\b(19|20)\d{2}\b", body)
        rec["year"] = y.group(0) if y else ""
    return rec


def load_input(path: str) -> list[dict]:
    with open(path, "r", encoding="utf-8-sig") as fh:
        text = fh.read()
    ext = os.path.splitext(path)[1].lower()
    if ext in (".bib", ".ris", ".nbib") or re.search(r"^(TY  - |PMID- |@\w+\s*\{)", text[:2000], flags=re.M):
        records = rt.read_records(path)
        for i, r in enumerate(records, 1):
            r.setdefault("label", r.get("bib_key") or f"[{i}]")
            r.setdefault("raw", r.get("title", ""))
        return records
    records = []
    # 換行被折斷的 DOI：把「下一行以小寫或數字開頭且前一行沒有結尾標點」的行接回去
    lines: list[str] = []
    for raw in text.splitlines():
        if lines and raw and not raw[0].isspace() and not re.search(r"[.)\]]\s*$", lines[-1]) and re.match(r"^[a-z0-9_/.\-]", raw):
            lines[-1] += raw.strip()
        elif raw.strip():
            lines.append(raw.rstrip())
    for i, line in enumerate(lines, 1):
        rec = parse_text_line(line)
        if not rec["label"]:
            rec["label"] = f"[{i}]"
        records.append(rec)
    return records


# ---------------------------------------------------------------------------
# 欄位比對
# ---------------------------------------------------------------------------


def title_similarity(a: str, b: str) -> float:
    na, nb = rt.normalize_title(a), rt.normalize_title(b)
    if not na or not nb:
        return 0.0
    ratio = difflib.SequenceMatcher(None, na, nb).ratio()
    jac = rt.jaccard(na, nb)
    # 給定標題是被截短的前綴（常見於文字檔）時，用包含度
    contain = 1.0 if (len(na) >= 25 and (na in nb or nb in na)) else 0.0
    return max(ratio, jac, contain)


def norm_journal(name: str) -> str:
    text = rt.normalize_title(name)
    return re.sub(r"\b(journal|of|the|and|&)\b", " ", text).strip()


def journal_abbrev_match(given: str, found_full: str, found_abbrev: str) -> bool:
    g = [t.rstrip(".") for t in rt.normalize_title(given).split()]
    if not g:
        return False
    for target in (found_abbrev, found_full):
        f = rt.normalize_title(target).split()
        if not f:
            continue
        # 每個給定 token 依序是目標 token 的前綴
        i = 0
        ok = True
        for tok in g:
            while i < len(f) and not f[i].startswith(tok):
                i += 1
            if i >= len(f):
                ok = False
                break
            i += 1
        if ok:
            return True
    return False


def norm_page(p: str) -> str:
    p = (p or "").strip().lower()
    p = re.sub(r"[‐-―−]", "-", p)
    return p


def page_number(p: str) -> int | None:
    m = re.search(r"\d+", p or "")
    return int(m.group(0)) if m else None


def check(field: str, given: str, found: str, level: str, note: str = "", score: float | None = None) -> dict:
    return {"field": field, "given": given, "found": found, "level": level, "note": note, "score": score}


def compare(given: dict, found: dict) -> list[dict]:
    checks: list[dict] = []

    # 標題
    if given.get("title") and found.get("title"):
        s = title_similarity(given["title"], found["title"])
        if s >= 0.90:
            same = rt.normalize_title(given["title"]) == rt.normalize_title(found["title"])
            checks.append(check("title", given["title"], found["title"], "ok" if same else "info", "" if same else "僅標點、大小寫或連字號差異", s))
        elif s >= 0.60:
            checks.append(check("title", given["title"], found["title"], "warn", "標題部分不符，請確認是否為同一篇（可能被截短或副標不同）", s))
        else:
            checks.append(check("title", given["title"], found["title"], "crit", "標題不符：DOI 可能指向另一篇（張冠李戴）", s))
    elif found.get("title"):
        checks.append(check("title", "", found["title"], "na", "輸入未提供標題，僅列出資料庫值"))

    # 第一作者
    g_first = rt.normalize_surname(rt.first_author_surname(given))
    f_first = rt.normalize_surname(rt.first_author_surname(found))
    if g_first and f_first:
        if g_first == f_first or g_first.endswith(f_first) or f_first.endswith(g_first):
            checks.append(check("first_author", given["authors"][0], found["authors"][0], "ok"))
        else:
            all_found = [rt.normalize_surname(a.split(",")[0]) for a in found.get("authors", [])]
            if g_first in all_found:
                pos = all_found.index(g_first) + 1
                checks.append(check("first_author", given["authors"][0], found["authors"][0], "crit", f"作者順序異常：輸入的第一作者在資料庫中排第 {pos} 位"))
            else:
                checks.append(check("first_author", given["authors"][0], found["authors"][0], "crit", "第一作者不符：可能為捏造引用或 DOI 張冠李戴"))
    elif found.get("authors"):
        checks.append(check("first_author", "", found["authors"][0], "na", "輸入未提供作者"))

    # 作者人數（僅在兩邊都有完整列表時比）
    if len(given.get("authors", [])) >= 2 and found.get("authors") and len(given["authors"]) < len(found["authors"]):
        if len(given["authors"]) < 20:  # APA 7 到 20 位才縮寫
            checks.append(check("author_count", str(len(given["authors"])), str(len(found["authors"])), "warn", "輸入作者數少於資料庫（APA 7 需列出至多 20 位；若原文用 et al. 可忽略）"))

    # 年份
    if given.get("year") and found.get("year"):
        gy, fy = int(given["year"]), int(found["year"])
        alt = {y for y in (found.get("online_year"), found.get("print_year")) if y and y.isdigit()}
        if gy == fy:
            checks.append(check("year", given["year"], found["year"], "ok"))
        elif str(gy) in alt:
            checks.append(check("year", given["year"], found["year"], "warn", f"上線年與卷年不一致（資料庫 issued={found['year']}，online/print={sorted(alt)}）；APA 7 以正式卷期年份為準"))
        elif abs(gy - fy) <= 1:
            checks.append(check("year", given["year"], found["year"], "warn", "年份差 1 年，請確認是 Early Access 漂移還是筆誤"))
        else:
            checks.append(check("year", given["year"], found["year"], "crit", "年份差 2 年以上"))
    elif found.get("year"):
        checks.append(check("year", "", found["year"], "na"))

    # 期刊
    if given.get("journal") and found.get("journal"):
        gj, fj = norm_journal(given["journal"]), norm_journal(found["journal"])
        if gj == fj or gj == norm_journal(found.get("journal_abbrev", "")):
            checks.append(check("journal", given["journal"], found["journal"], "ok"))
        elif journal_abbrev_match(given["journal"], found["journal"], found.get("journal_abbrev", "")):
            checks.append(check("journal", given["journal"], found["journal"], "info", "期刊縮寫與全名差異（APA 7 需用全名）"))
        elif difflib.SequenceMatcher(None, gj, fj).ratio() >= 0.80:
            checks.append(check("journal", given["journal"], found["journal"], "info", "期刊名寫法略有差異"))
        else:
            checks.append(check("journal", given["journal"], found["journal"], "warn", "期刊名不符"))
    elif found.get("journal"):
        checks.append(check("journal", "", found["journal"], "na"))

    # 卷、期
    for fld, label in (("volume", "卷"), ("issue", "期")):
        if given.get(fld) and found.get(fld):
            if given[fld].strip().lower() == found[fld].strip().lower():
                checks.append(check(fld, given[fld], found[fld], "ok"))
            else:
                checks.append(check(fld, given[fld], found[fld], "warn", f"{label}不符（可能為 Early Access 轉正式出版後的漂移，以資料庫現值為準）"))
        elif found.get(fld):
            checks.append(check(fld, "", found[fld], "na"))
        elif given.get(fld) and fld == "issue":
            checks.append(check(fld, given[fld], "", "info", "資料庫無期號"))

    # 頁碼／文章號
    g_pages = norm_page(rt.pages_text(given))
    f_pages = norm_page(rt.pages_text(found)) or norm_page(found.get("article_number", ""))
    if g_pages and f_pages:
        if g_pages == f_pages:
            checks.append(check("pages", g_pages, f_pages, "ok"))
        else:
            gs, fs = page_number(given.get("start_page")), page_number(found.get("start_page") or found.get("article_number"))
            ge, fe = page_number(given.get("end_page")), page_number(found.get("end_page"))
            if gs is not None and fs is not None and abs(gs - fs) <= 4 and (ge is None or fe is None or abs(ge - fe) <= 4):
                checks.append(check("pages", g_pages, f_pages, "warn", "頁碼小幅偏差（≤ 4）"))
            elif re.search(r"[a-z]", g_pages) or re.search(r"[a-z]", f_pages):
                checks.append(check("pages", g_pages, f_pages, "crit", "文章號不符（注意字母與數字形近：O/0、l/1）"))
            else:
                checks.append(check("pages", g_pages, f_pages, "crit", "頁碼差 5 以上"))
    elif f_pages:
        checks.append(check("pages", "", f_pages, "na"))

    # 可能的撤稿或更正（Crossref update-to）
    if found.get("retraction_note"):
        checks.append(check("retraction", "", found["retraction_note"], "crit", "資料庫標記有撤稿／更正／關注聲明"))
    return checks


def overall_status(checks: list[dict]) -> str:
    levels = {c["level"] for c in checks}
    if "crit" in levels:
        return "fix"
    if "warn" in levels:
        return "check"
    return "verified"


# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------


def retraction_note(msg: dict) -> str:
    notes = []
    for upd in msg.get("update-to", []) or []:
        notes.append(f"update-to:{upd.get('type')}")
    if (msg.get("type") or "") == "retraction":
        notes.append("type:retraction")
    return "; ".join(notes)


def verify_one(given: dict, mailto: str | None, ncbi_email: str | None, search_missing: bool) -> dict:
    result = {"label": given.get("label", ""), "raw": given.get("raw", given.get("title", "")), "doi": given.get("doi", ""), "pmid": given.get("pmid", ""), "source": "", "status": "unverifiable", "checks": [], "found": None, "note": ""}
    found = None
    try:
        if given.get("doi"):
            msg = crossref_lookup(given["doi"], mailto)
            if msg is None:
                result["note"] = "DOI 在 Crossref 回傳 404：DOI 本身可能錯誤（或為非 Crossref 註冊的 DOI，例如部分台灣期刊由華藝／Airiti 註冊）"
                result["checks"].append(check("doi", given["doi"], "", "crit", result["note"]))
                result["status"] = "fix"
                if given.get("pmid"):
                    docs = pubmed_esummary([given["pmid"]], ncbi_email)
                    doc = docs.get(given["pmid"])
                    if doc and "error" not in doc:
                        found = esummary_to_record(doc)
                        result["source"] = "PubMed"
                        result["note"] += "；改用 PMID 反查比對"
            else:
                found = crossref_message_to_record(msg)
                found["retraction_note"] = retraction_note(msg)
                result["source"] = "Crossref"
        elif given.get("pmid"):
            docs = pubmed_esummary([given["pmid"]], ncbi_email)
            doc = docs.get(given["pmid"])
            if doc and "error" not in doc:
                found = esummary_to_record(doc)
                result["source"] = "PubMed"
                if found.get("doi"):
                    result["doi"] = found["doi"]
                    result["note"] = f"PMID 反查得 DOI {found['doi']}"
            else:
                result["note"] = "PMID 在 PubMed 找不到"
                result["checks"].append(check("pmid", given["pmid"], "", "crit", result["note"]))
                result["status"] = "fix"
        else:
            result["note"] = "沒有 DOI 或 PMID，無法自動核對；請用 PubMed lookup_article_by_citation 或標題檢索人工確認"
            if search_missing and (given.get("title") or given.get("raw")):
                items = crossref_search(given.get("title") or given.get("raw"), mailto)
                cands = []
                for it in items:
                    cand = crossref_message_to_record(it)
                    sim = title_similarity(given.get("title") or given.get("raw"), cand.get("title", ""))
                    cands.append({"doi": cand["doi"], "title": cand["title"], "first_author": (cand["authors"] or [""])[0], "year": cand["year"], "journal": cand["journal"], "similarity": round(sim, 2)})
                result["candidates"] = cands
                if cands:
                    best = cands[0]
                    result["note"] = f"無 DOI；Crossref 書目查詢最佳候選 {best['doi']}（相似度 {best['similarity']}），僅供人工確認，未列為已驗證"
    except (HTTPError, URLError, TimeoutError, OSError) as e:
        result["note"] = f"網路或 API 錯誤：{e}"
        return result

    if found is not None:
        result["found"] = {k: found.get(k, "") for k in ("title", "authors", "journal", "journal_abbrev", "year", "online_year", "print_year", "volume", "issue", "start_page", "end_page", "doi", "pmid", "article_number")}
        cmp_checks = compare(given, found)
        result["checks"].extend(cmp_checks)
        if result["status"] != "fix":
            result["status"] = overall_status(result["checks"])
        else:
            result["status"] = "fix"
        if cmp_checks and all(c["level"] == "na" for c in cmp_checks):
            result["note"] = (result["note"] + "；" if result["note"] else "") + "DOI 可解析；輸入未提供可比對欄位，請以下方資料庫書目為準"
    return result


def pmid_report(pmids: list[str], ncbi_email: str | None) -> list[dict]:
    docs = pubmed_esummary(pmids, ncbi_email)
    out = []
    for pmid in pmids:
        doc = docs.get(pmid)
        if not doc or "error" in doc:
            out.append({"label": pmid, "pmid": pmid, "status": "unverifiable", "note": "PMID 找不到", "checks": [], "found": None, "doi": "", "raw": ""})
            continue
        rec = esummary_to_record(doc)
        out.append({"label": pmid, "pmid": pmid, "doi": rec["doi"], "status": "verified", "note": "PMID 反查（未與輸入欄位比對，僅列出 PubMed 書目）", "source": "PubMed", "checks": [], "raw": "", "found": {k: rec.get(k, "") for k in ("title", "authors", "journal", "journal_abbrev", "year", "online_year", "volume", "issue", "start_page", "end_page", "doi", "pmid")}})
    return out


# ---------------------------------------------------------------------------
# 輸出
# ---------------------------------------------------------------------------


def _cell(text: str, limit: int = 60) -> str:
    text = (text or "").replace("|", "\\|").replace("\n", " ")
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _field_cell(checks: list[dict], field: str) -> str:
    for c in checks:
        if c["field"] == field:
            icon = LEVEL_ICON.get(c["level"], "")
            if c["level"] == "na":
                return f"－ {_cell(c['found'], 30)}"
            if c["level"] == "ok":
                return f"✅ {_cell(c['found'], 30)}"
            score = f" ({c['score']:.2f})" if c.get("score") is not None else ""
            return f"{icon} {_cell(c['given'], 24)} → {_cell(c['found'], 24)}{score}"
    return ""


def render_markdown(results: list[dict], mailto: str | None) -> str:
    counts = {k: 0 for k in STATUS_ICON}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    lines = [f"## 參考文獻核對結果：{len(results)} 筆（查核日期 {date.today().isoformat()}）", ""]
    for key in ("verified", "check", "fix", "unverifiable"):
        lines.append(f"- {STATUS_ICON[key]}: {counts.get(key, 0)}")
    lines += ["", "來源：Crossref REST API（DOI）、PubMed E-utilities esummary（PMID）。標題相似度為正規化後的序列比對／Jaccard 最大值。", ""]
    lines.append("| # | 狀態 | DOI／PMID | 標題相似度 | 第一作者 | 年份 | 期刊 | 卷(期) | 頁碼 | 備註 |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|")
    for r in results:
        ident = r.get("doi") or (f"PMID:{r['pmid']}" if r.get("pmid") else "")
        vol = _field_cell(r["checks"], "volume")
        iss = _field_cell(r["checks"], "issue")
        volcell = vol + (f" ({iss})" if iss else "")
        notes = [c["note"] for c in r["checks"] if c.get("note") and c["level"] in ("crit", "warn", "info")]
        if r.get("note") and r["note"] not in notes:
            notes.insert(0, r["note"])
        lines.append("| " + " | ".join([
            _cell(r.get("label", ""), 12), STATUS_ICON[r["status"]], _cell(ident, 40),
            _field_cell(r["checks"], "title"), _field_cell(r["checks"], "first_author"), _field_cell(r["checks"], "year"),
            _field_cell(r["checks"], "journal"), volcell, _field_cell(r["checks"], "pages"), _cell("；".join(notes), 160),
        ]) + " |")
    fixes = [r for r in results if r["status"] == "fix"]
    if fixes:
        lines += ["", "### ❌ 必須修正", "", "| # | 欄位 | 目前值 | 資料庫值 | 說明 |", "|---|---|---|---|---|"]
        for r in fixes:
            for c in r["checks"]:
                if c["level"] == "crit":
                    lines.append(f"| {_cell(r.get('label',''),12)} | {c['field']} | {_cell(c['given'],50)} | {_cell(c['found'],50)} | {_cell(c['note'],120)} |")
    warns = [r for r in results if r["status"] == "check"]
    if warns:
        lines += ["", "### ⚠️ 建議核對", "", "| # | 欄位 | 目前值 | 資料庫值 | 說明 |", "|---|---|---|---|---|"]
        for r in warns:
            for c in r["checks"]:
                if c["level"] == "warn":
                    lines.append(f"| {_cell(r.get('label',''),12)} | {c['field']} | {_cell(c['given'],50)} | {_cell(c['found'],50)} | {_cell(c['note'],120)} |")
    found_only = [r for r in results if r.get("found") and not [c for c in r["checks"] if c["level"] not in ("na", "ok")] and r["status"] == "verified"]
    if any(r.get("found") for r in results):
        lines += ["", "### 資料庫回傳書目（供 apa7-master 產生 APA 7 格式）", ""]
        for r in results:
            f = r.get("found")
            if not f:
                continue
            authors = "; ".join(f.get("authors", [])[:20])
            pages = f"{f.get('start_page','')}" + (f"-{f['end_page']}" if f.get("end_page") else "")
            lines.append(f"- **{r.get('label','')}** {authors} ({f.get('year','')}). {f.get('title','')}. *{f.get('journal','')}*, {f.get('volume','')}" + (f"({f['issue']})" if f.get("issue") else "") + (f", {pages}" if pages else "") + (f". https://doi.org/{f['doi']}" if f.get("doi") else "") + (f"（PMID {f['pmid']}）" if f.get("pmid") else ""))
    for r in results:
        if r.get("candidates"):
            lines += ["", f"### 無 DOI 條目的候選（{r.get('label','')}）", ""]
            for c in r["candidates"]:
                lines.append(f"- {c['doi']}：{c['title']}（{c['first_author']}，{c['year']}，{c['journal']}；相似度 {c['similarity']}）")
    if not mailto:
        lines += ["", "提示：加 `--mailto you@example.com` 可進入 Crossref polite pool，批次查詢較不易被限速。"]
    return "\n".join(lines) + "\n"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="verify_dois.py", description="以 Crossref／PubMed 核對參考文獻欄位（bob-citation）")
    p.add_argument("--input", "-i", help=".bib / .ris / .nbib / .txt 檔")
    p.add_argument("--doi", action="append", default=[], help="直接指定 DOI（可重複）")
    p.add_argument("--pmid", action="append", default=[], help="PMID 反查（可重複，或逗號分隔）")
    p.add_argument("--mailto", help="Crossref polite pool 用的 email")
    p.add_argument("--ncbi-email", help="E-utilities email 參數；省略時沿用 --mailto")
    p.add_argument("--search-missing", action="store_true", help="無 DOI 的條目用 Crossref 書目查詢找候選")
    p.add_argument("--json", help="輸出 JSON 檔")
    p.add_argument("--md", help="輸出 Markdown 檔（省略則印到標準輸出）")
    p.add_argument("--quiet", action="store_true", help="不在標準輸出印 Markdown")
    p.add_argument("--version", action="version", version=f"verify_dois {__version__}")
    return p


def main(argv: list[str] | None = None) -> int:
    rt._configure_stdout()
    args = build_parser().parse_args(argv)
    ncbi_email = args.ncbi_email or args.mailto
    given_records: list[dict] = []
    if args.input:
        given_records.extend(load_input(args.input))
    for i, doi in enumerate(args.doi, 1):
        rec = rt.new_record()
        rec.update({"doi": rt.normalize_doi(doi), "label": f"doi{i}", "raw": doi})
        given_records.append(rec)
    pmids = [x.strip() for chunk in args.pmid for x in chunk.split(",") if x.strip()]
    if not given_records and not pmids:
        build_parser().error("請提供 --input、--doi 或 --pmid")

    results: list[dict] = []
    for rec in given_records:
        print(f"核對 {rec.get('label','')} {rec.get('doi') or rec.get('pmid') or (rec.get('title') or '')[:50]}", file=sys.stderr)
        results.append(verify_one(rec, args.mailto, ncbi_email, args.search_missing))
    if pmids:
        print(f"PMID 反查：{', '.join(pmids)}", file=sys.stderr)
        results.extend(pmid_report(pmids, ncbi_email))

    md = render_markdown(results, args.mailto)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump({"checked_on": date.today().isoformat(), "tool": f"verify_dois {__version__}", "results": results}, fh, ensure_ascii=False, indent=2)
        print(f"JSON：{os.path.abspath(args.json)}", file=sys.stderr)
    if args.md:
        with open(args.md, "w", encoding="utf-8") as fh:
            fh.write(md)
        print(f"Markdown：{os.path.abspath(args.md)}", file=sys.stderr)
    if not args.quiet and not args.md:
        sys.stdout.write(md)
    return 1 if any(r["status"] == "fix" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
