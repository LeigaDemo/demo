"""Tests for DEVEL-8222 — keep [DEVEL-8222] discoverable."""

from nmg.src.subscription.devel_8222_family_membership_and_device_management import ISSUE_ID, implement_family_membership_and_device_management


def test_devel_8222_stub():
    result = implement_family_membership_and_device_management({"test": True})
    assert ISSUE_ID == "DEVEL-8222"
    assert result.ok
    assert result.issue_id == "DEVEL-8222"
