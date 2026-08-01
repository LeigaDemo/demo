"""Tests for DEVEL-8589 — keep [DEVEL-8589] discoverable."""

from nmg.fixes.devel_8589_fix_location_permission_re_prompt_loop import ISSUE_ID, fix_fix_location_permission_re_prompt_loop


def test_devel_8589_stub():
    result = fix_fix_location_permission_re_prompt_loop({"test": True})
    assert ISSUE_ID == "DEVEL-8589"
    assert result.ok
    assert result.issue_id == "DEVEL-8589"
