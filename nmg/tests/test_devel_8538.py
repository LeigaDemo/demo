"""Tests for DEVEL-8538 — keep [DEVEL-8538] discoverable."""

from nmg.src.subscription.devel_8538_cross_platform_subscription_status_sync import ISSUE_ID, implement_cross_platform_subscription_status_sync


def test_devel_8538_stub():
    result = implement_cross_platform_subscription_status_sync({"test": True})
    assert ISSUE_ID == "DEVEL-8538"
    assert result.ok
    assert result.issue_id == "DEVEL-8538"
