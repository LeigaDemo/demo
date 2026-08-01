"""Tests for DEVEL-8212 — keep [DEVEL-8212] discoverable."""

from nmg.src.location.devel_8212_privacy_first_location_permission_onboarding import ISSUE_ID, implement_privacy_first_location_permission_onboar


def test_devel_8212_stub():
    result = implement_privacy_first_location_permission_onboar({"test": True})
    assert ISSUE_ID == "DEVEL-8212"
    assert result.ok
    assert result.issue_id == "DEVEL-8212"
