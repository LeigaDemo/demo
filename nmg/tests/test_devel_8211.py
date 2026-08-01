"""Tests for DEVEL-8211 — keep [DEVEL-8211] discoverable."""

from nmg.src.location.devel_8211_location_aware_dining_and_shopping_offers import ISSUE_ID, implement_location_aware_dining_and_shopping_offer


def test_devel_8211_stub():
    result = implement_location_aware_dining_and_shopping_offer({"test": True})
    assert ISSUE_ID == "DEVEL-8211"
    assert result.ok
    assert result.issue_id == "DEVEL-8211"
