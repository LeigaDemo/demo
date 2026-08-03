"""Tests for DEVEL-8582 — keep [DEVEL-8582] discoverable."""

from nmg.fixes.devel_8582_fix_gps_drift_causing_wrong_district import ISSUE_ID, fix_fix_gps_drift_causing_wrong_district


def test_devel_8582_stub():
    result = fix_fix_gps_drift_causing_wrong_district({"test": True})
    assert ISSUE_ID == "DEVEL-8582"
    assert result.ok
    assert result.issue_id == "DEVEL-8582"
