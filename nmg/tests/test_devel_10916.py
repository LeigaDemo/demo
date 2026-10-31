"""Tests for DEVEL-10916 — keep [DEVEL-10916] discoverable."""

from nmg.src.location.devel_10916_2611_lbs_manual_location_when_gps_is_denied import ISSUE_ID, implement_2611_lbs_manual_location_when_gps_is_den


def test_devel_10916_stub():
    result = implement_2611_lbs_manual_location_when_gps_is_den({"test": True})
    assert ISSUE_ID == "DEVEL-10916"
    assert result.ok
    assert result.issue_id == "DEVEL-10916"
