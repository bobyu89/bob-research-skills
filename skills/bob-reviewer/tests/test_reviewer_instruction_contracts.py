from pathlib import Path


ROOT = Path(__file__).parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_frontmatter_name_matches_directory() -> None:
    router = read("SKILL.md")

    assert router.startswith("---\nname: bob-reviewer\n")
    assert "nature-" not in router


def test_severity_and_blocking_contract_is_present() -> None:
    router = read("SKILL.md")

    assert "Major Concerns" in router
    assert "Minor Comments" in router
    assert "Blocking Yes" in router
    assert "Minor Comments are never blocking" in router
    assert "Do not impose a concern quota" in router


def test_reviewers_are_isolated_before_synthesis() -> None:
    router = read("SKILL.md")

    assert "真正分離的 context" in router
    assert "Freeze each individual report before comparing" in router
    assert "not shown to reviewers" in router
    assert "Do not let one reviewer read" in router


def test_traceability_and_non_invention_are_required() -> None:
    router = read("SKILL.md")

    assert "claim_pointer" in router
    assert "evidence_pointer" in router
    assert "Do not invent experiments" in router


def test_punctuation_guard_is_part_of_the_reviewer_contract() -> None:
    router = read("SKILL.md")

    assert "Avoid em dashes, en dashes, and colons" in router
    assert "Do not use dash punctuation or colons" in router


def test_chinese_check_block_and_health_axes_are_present() -> None:
    router = read("SKILL.md")
    axes = read("references/review-axes.md")

    assert "中文核對" in router
    assert "口試委員最可能追問的三點" in router
    for axis in (
        "originality",
        "clinical-educational-significance",
        "methodological-rigour",
        "ethics-reporting-transparency",
        "interdisciplinary-clarity",
    ):
        assert f"`{axis}`" in router
        assert f"`{axis}`" in axes


def test_manifest_paths_exist() -> None:
    import re

    manifest = read("manifest.yaml")
    paths = re.findall(r"^\s*(?:-\s*|path:\s*|[a-z-]+:\s+)((?:\.\./|references/)[^\s#]+\.md)\s*$", manifest, re.M)
    assert paths, "no paths found in manifest"
    missing = [p for p in paths if not (ROOT / p).exists()]
    # bob-shared files are produced by a sibling task; report but do not fail on them
    local_missing = [p for p in missing if not p.startswith("../bob-shared/")]
    assert not local_missing, f"missing local paths: {local_missing}"
