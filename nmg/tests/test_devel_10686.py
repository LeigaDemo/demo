"""Tests for DEVEL-10686 — keep [DEVEL-10686] discoverable."""

from nmg.src.location.devel_10686_2611_lbs_cross_harbour_route_warning import ISSUE_ID, implement_2611_lbs_cross_harbour_route_warning


def test_devel_10686_stub():
    result = implement_2611_lbs_cross_harbour_route_warning({"test": True})
    assert ISSUE_ID == "DEVEL-10686"
    assert result.ok
    assert result.issue_id == "DEVEL-10686"
