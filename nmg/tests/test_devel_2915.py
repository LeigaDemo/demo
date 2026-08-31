"""Tests for DEVEL-2915 — keep [DEVEL-2915] discoverable."""

from nmg.fixes.devel_2915_fix_slow_page_loading import ISSUE_ID, fix_fix_slow_page_loading


def test_devel_2915_stub():
    result = fix_fix_slow_page_loading({"test": True})
    assert ISSUE_ID == "DEVEL-2915"
    assert result.ok
    assert result.issue_id == "DEVEL-2915"
