"""Tests for DEVEL-8591 — keep [DEVEL-8591] discoverable."""

from nmg.fixes.devel_8591_fix_nearby_offers_not_refreshing import ISSUE_ID, fix_fix_nearby_offers_not_refreshing


def test_devel_8591_stub():
    result = fix_fix_nearby_offers_not_refreshing({"test": True})
    assert ISSUE_ID == "DEVEL-8591"
    assert result.ok
    assert result.issue_id == "DEVEL-8591"
