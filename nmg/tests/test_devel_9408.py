"""Tests for DEVEL-9408 — keep [DEVEL-9408] discoverable."""

from nmg.src.location.devel_9408_2610_lbs_gps_consent_retention_and_user_control import ISSUE_ID, implement_2610_lbs_gps_consent_retention_and_user


def test_devel_9408_stub():
    result = implement_2610_lbs_gps_consent_retention_and_user({"test": True})
    assert ISSUE_ID == "DEVEL-9408"
    assert result.ok
    assert result.issue_id == "DEVEL-9408"
