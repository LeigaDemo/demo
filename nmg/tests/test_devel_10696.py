"""Tests for DEVEL-10696 — keep [DEVEL-10696] discoverable."""

from nmg.src.location.devel_10696_2611_lbs_gps_consent_retention_and_user_control import ISSUE_ID, implement_2611_lbs_gps_consent_retention_and_user


def test_devel_10696_stub():
    result = implement_2611_lbs_gps_consent_retention_and_user({"test": True})
    assert ISSUE_ID == "DEVEL-10696"
    assert result.ok
    assert result.issue_id == "DEVEL-10696"
