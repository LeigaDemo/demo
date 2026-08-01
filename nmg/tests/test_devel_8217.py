"""Tests for DEVEL-8217 — keep [DEVEL-8217] discoverable."""

from nmg.src.location.devel_8217_geofence_engagement_performance_dashboard import ISSUE_ID, implement_geofence_engagement_performance_dashboar


def test_devel_8217_stub():
    result = implement_geofence_engagement_performance_dashboar({"test": True})
    assert ISSUE_ID == "DEVEL-8217"
    assert result.ok
    assert result.issue_id == "DEVEL-8217"
