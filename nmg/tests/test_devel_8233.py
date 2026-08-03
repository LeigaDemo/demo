"""Tests for DEVEL-8233 — keep [DEVEL-8233] discoverable."""

from nmg.src.subscription.devel_8233_entitlement_synchronisation_across_app_and_web import ISSUE_ID, implement_entitlement_synchronisation_across_app_a


def test_devel_8233_stub():
    result = implement_entitlement_synchronisation_across_app_a({"test": True})
    assert ISSUE_ID == "DEVEL-8233"
    assert result.ok
    assert result.issue_id == "DEVEL-8233"
