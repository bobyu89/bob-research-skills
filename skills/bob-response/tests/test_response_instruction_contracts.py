from pathlib import Path


ROOT = Path(__file__).parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_decision_type_gate_is_part_of_the_runtime_contract() -> None:
    router = read("SKILL.md")
    workflow = read("static/core/workflow.md")

    assert "Major Revision" in router and "Minor Revision" in router
    assert "主要修訂" in router and "次要修訂" in router
    assert "暫停" in workflow
    assert "不可在未區分主要與次要修訂的情況下產出通用回覆" in workflow


def test_reviewer_isolation_is_required_in_core_and_qa() -> None:
    stance = read("static/core/stance.md")
    qa = read("references/qa-checklist.md")

    assert "預設把各審稿人視為互盲" in stance
    assert "不得透露另一位審稿人的" in stance
    assert "Each reviewer-facing file contains only one reviewer's comments" in qa
    assert "complete standalone answer" in qa


def test_missed_existing_text_is_treated_as_a_clarity_problem() -> None:
    stance = read("static/core/stance.md")
    qa = read("references/qa-checklist.md")

    assert "資訊不夠醒目或不夠清楚" in stance
    assert 'No response says "we already stated this"' in qa


def test_punctuation_guard_is_present_in_core_and_qa() -> None:
    stance = read("static/core/stance.md")
    qa = read("references/qa-checklist.md")

    assert "避免把破折號" in stance
    assert "No avoidable em dash, en dash, or colon" in qa


def test_committee_mode_is_routed() -> None:
    router = read("SKILL.md")
    workflow = read("static/core/workflow.md")
    manifest = read("manifest.yaml")

    assert "committee-response" in router
    assert "口試委員意見回覆模式" in workflow
    assert "references/thesis-committee-response.md" in manifest
    assert "templates/committee-response-table.md" in manifest


def test_manifest_paths_exist() -> None:
    import re

    manifest = read("manifest.yaml")
    paths = re.findall(r"^\s*(?:-\s*|path:\s*)((?:\.\./|static/|references/|templates/|scripts/)[^\s]+)", manifest, re.M)
    assert paths
    for rel in paths:
        assert (ROOT / rel).is_file(), rel


def test_no_upstream_names_outside_upstream_md() -> None:
    # Built from parts so this file itself does not contain the upstream skill names.
    upstream_prefix = "nat" + "ure-"
    banned = [upstream_prefix + suffix for suffix in (
        "shared", "writing", "polishing", "reviewer", "response", "citation", "figure", "statistics")]
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.name == "UPSTREAM.md" or "__pycache__" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for word in banned:
            assert word not in text, f"{word} in {path.relative_to(ROOT)}"
