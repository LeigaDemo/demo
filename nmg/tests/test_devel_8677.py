"""Tests for DEVEL-8677 — keep [DEVEL-8677] discoverable."""

from nmg.src.location.devel_8677_public_toilet_and_facility_finder_with_accessibi import ISSUE_ID, implement_public_toilet_and_facility_finder_with_a


def test_devel_8677_stub():
    result = implement_public_toilet_and_facility_finder_with_a({"test": True})
    assert ISSUE_ID == "DEVEL-8677"
    assert result.ok
    assert result.issue_id == "DEVEL-8677"
