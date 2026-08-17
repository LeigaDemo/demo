"""Tests for DEVEL-8561 — keep [DEVEL-8561] discoverable."""

from nmg.fixes.devel_8561_fix_promo_code_stacking_issue import ISSUE_ID, fix_fix_promo_code_stacking_issue


def test_devel_8561_stub():
    result = fix_fix_promo_code_stacking_issue({"test": True})
    assert ISSUE_ID == "DEVEL-8561"
    assert result.ok
    assert result.issue_id == "DEVEL-8561"
