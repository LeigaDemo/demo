"""Tests for DEVEL-8559 — keep [DEVEL-8559] discoverable."""

from nmg.fixes.devel_8559_fix_membership_badge_not_updating import ISSUE_ID, fix_fix_membership_badge_not_updating


def test_devel_8559_stub():
    result = fix_fix_membership_badge_not_updating({"test": True})
    assert ISSUE_ID == "DEVEL-8559"
    assert result.ok
    assert result.issue_id == "DEVEL-8559"
