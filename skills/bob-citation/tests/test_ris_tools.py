# -*- coding: utf-8 -*-
"""離線單元測試：ris_tools 解析、轉檔、去重、完整性檢查；verify_dois 的欄位比對。不連網。"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "scripts"))

import ris_tools as rt  # noqa: E402
import verify_dois as vd  # noqa: E402

SAMPLES = os.path.join(HERE, "samples")


def test_parse_nbib_sample():
    recs = rt.read_records(os.path.join(SAMPLES, "pubmed-35696315.nbib"))
    assert len(recs) == 1
    r = recs[0]
    assert r["pmid"] == "35696315"
    assert r["doi"] == "10.1111/jan.15321"
    assert r["authors"][0] == "Lyu, Meng-Meng"
    assert r["year"] == "2022" and r["volume"] == "78" and r["issue"] == "10"
    assert (r["start_page"], r["end_page"]) == ("3069", "3082")


def test_roundtrip_ris_bib_nbib():
    recs = rt.read_records(os.path.join(SAMPLES, "pubmed-35696315.nbib"))
    ris = rt.records_to_ris(recs)
    bib = rt.records_to_bib(recs)
    nbib = rt.records_to_nbib(recs)
    for text, parser in ((ris, rt.parse_ris), (bib, rt.parse_bibtex), (nbib, rt.parse_medline)):
        back = parser(text)
        assert len(back) == 1
        assert back[0]["doi"] == "10.1111/jan.15321"
        assert back[0]["authors"][0].startswith("Lyu")
        assert back[0]["start_page"] == "3069"


def test_author_normalization():
    assert rt.author_to_family_given("Lyu MM") == "Lyu, MM"
    assert rt.author_to_family_given("Meng-Meng Lyu") == "Lyu, Meng-Meng"
    assert rt.author_to_family_given("Lyu, Meng-Meng") == "Lyu, Meng-Meng"
    assert rt.author_to_family_given("Taiwan Nurses Association,") == "Taiwan Nurses Association,"
    assert rt.author_incomplete("Chaudhuri")
    assert not rt.author_incomplete("Chaudhuri, K Ray")


def test_dedupe_mixed_sources():
    recs = rt.read_records(os.path.join(SAMPLES, "dedupe-mix.bib")) + rt.read_records(os.path.join(SAMPLES, "pubmed-35696315.nbib"))
    assert len(recs) == 6
    kept, notes = rt.dedupe_records(recs)
    assert len(kept) == 3
    assert len(notes) == 3
    lyu = [r for r in kept if r["doi"] == "10.1111/jan.15321"][0]
    assert lyu["pmid"] == "35696315"  # 合併後保留較完整的 PubMed 紀錄
    tanner = [r for r in kept if "tanner" in rt.normalize_surname(rt.first_author_surname(r))][0]
    assert tanner["doi"] == "10.3928/01484834-20060601-04" and tanner["start_page"] == "204"


def test_check_flags_surname_only():
    recs = rt.read_records(os.path.join(SAMPLES, "dedupe-mix.bib"))
    report = rt.check_records(recs)
    bad = [x for x in report if any("只有姓氏" in i for i in x["issues"])]
    assert len(bad) == 1


def test_parse_apa7_line():
    line = "[2] Lyu, M.-M., Siah, R. C.-J., Lam, A. S. L., & Cheng, K. K. F. (2021). The effect of psychological interventions on fear of cancer recurrence in breast cancer survivors. J Adv Nurs, 78(10), 3069–3080. https://doi.org/10.1111/jan.15321"
    rec = vd.parse_text_line(line)
    assert rec["label"] == "[2]" and rec["doi"] == "10.1111/jan.15321" and rec["year"] == "2021"
    assert rec["authors"][0].startswith("Lyu")
    assert rec["journal"] == "J Adv Nurs" and rec["volume"] == "78" and rec["issue"] == "10"
    assert (rec["start_page"], rec["end_page"]) == ("3069", "3080")


def _found():
    return {
        "title": "The effect of psychological interventions on fear of cancer recurrence in breast cancer survivors: A systematic review and meta‐analysis",
        "authors": ["Lyu, Meng‐Meng", "Siah, Rosalind Chiew‐Jiat", "Lam, Alekzendr Sheen Loong", "Cheng, Karis Kin Fong"],
        "journal": "Journal of Advanced Nursing", "journal_abbrev": "", "year": "2022", "online_year": "2022", "print_year": "2022",
        "volume": "78", "issue": "10", "start_page": "3069", "end_page": "3082", "article_number": "",
    }


def test_compare_levels():
    given = vd.parse_text_line("[1] Lyu, M.-M., Siah, R. C.-J., Lam, A. S. L., & Cheng, K. K. F. (2022). The effect of psychological interventions on fear of cancer recurrence in breast cancer survivors: A systematic review and meta-analysis. Journal of Advanced Nursing, 78(10), 3069–3082.")
    checks = vd.compare(given, _found())
    assert vd.overall_status(checks) == "verified"

    wrong = vd.parse_text_line("[3] Wang, H., & Chen, L. (2022). Clinical reasoning of nurse practitioners: A meta-analysis. Journal of Advanced Nursing, 78(10), 3069–3082.")
    checks = vd.compare(wrong, _found())
    levels = {c["field"]: c["level"] for c in checks}
    assert levels["title"] == "crit" and levels["first_author"] == "crit"
    assert vd.overall_status(checks) == "fix"

    drift = vd.parse_text_line("[2] Lyu, M.-M., Siah, R. C.-J., Lam, A. S. L., & Cheng, K. K. F. (2021). The effect of psychological interventions on fear of cancer recurrence in breast cancer survivors. J Adv Nurs, 78(10), 3069–3080.")
    checks = vd.compare(drift, _found())
    levels = {c["field"]: c["level"] for c in checks}
    assert levels["year"] == "warn" and levels["pages"] == "warn" and levels["journal"] == "info"
    assert vd.overall_status(checks) == "check"


if __name__ == "__main__":
    # 沒裝 pytest 也能跑：依序執行所有 test_* 函式
    failed = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"PASS {name}")
            except AssertionError as e:
                failed += 1
                print(f"FAIL {name}: {e}")
    print(f"{failed} failed")
    sys.exit(1 if failed else 0)
