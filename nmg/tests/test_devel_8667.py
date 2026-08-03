"""Tests for DEVEL-8667 — keep [DEVEL-8667] discoverable."""

from nmg.src.location.devel_8667_real_time_traffic_incident_alerts_with_rerouting import ISSUE_ID, implement_real_time_traffic_incident_alerts_with_r


def test_devel_8667_stub():
    result = implement_real_time_traffic_incident_alerts_with_r({"test": True})
    assert ISSUE_ID == "DEVEL-8667"
    assert result.ok
    assert result.issue_id == "DEVEL-8667"
