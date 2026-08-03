"""Tests for DEVEL-8583 — keep [DEVEL-8583] discoverable."""

from nmg.src.location.devel_8583_geofence_analytics_and_engagement_metrics import ISSUE_ID, implement_geofence_analytics_and_engagement_metric


def test_devel_8583_stub():
    result = implement_geofence_analytics_and_engagement_metric({"test": True})
    assert ISSUE_ID == "DEVEL-8583"
    assert result.ok
    assert result.issue_id == "DEVEL-8583"
