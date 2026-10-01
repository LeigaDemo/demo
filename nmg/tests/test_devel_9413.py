"""Tests for DEVEL-9413 — keep [DEVEL-9413] discoverable."""

from nmg.src.location.devel_9413_2610_lbs_geofence_content_delivery import ISSUE_ID, implement_2610_lbs_geofence_content_delivery


def test_devel_9413_stub():
    result = implement_2610_lbs_geofence_content_delivery({"test": True})
    assert ISSUE_ID == "DEVEL-9413"
    assert result.ok
    assert result.issue_id == "DEVEL-9413"
