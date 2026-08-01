"""Tests for DEVEL-8621 — keep [DEVEL-8621] discoverable."""

from nmg.fixes.devel_8621_fix_broken_deep_link_to_saved_articles import ISSUE_ID, fix_fix_broken_deep_link_to_saved_articles


def test_devel_8621_stub():
    result = fix_fix_broken_deep_link_to_saved_articles({"test": True})
    assert ISSUE_ID == "DEVEL-8621"
    assert result.ok
    assert result.issue_id == "DEVEL-8621"
