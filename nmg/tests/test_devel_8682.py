"""Tests for DEVEL-8682 — keep [DEVEL-8682] discoverable."""

from nmg.src.location.devel_8682_uat_sign_off_for_geofence_content_delivery import ISSUE_ID, implement_uat_sign_off_for_geofence_content_delive


def test_devel_8682_stub():
    result = implement_uat_sign_off_for_geofence_content_delive({"test": True})
    assert ISSUE_ID == "DEVEL-8682"
    assert result.ok
    assert result.issue_id == "DEVEL-8682"
