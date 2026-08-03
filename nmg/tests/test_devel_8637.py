"""Tests for DEVEL-8637 — keep [DEVEL-8637] discoverable."""

from nmg.src.subscription.devel_8637_uat_sign_off_for_corporate_subscription_flow import ISSUE_ID, implement_uat_sign_off_for_corporate_subscription


def test_devel_8637_stub():
    result = implement_uat_sign_off_for_corporate_subscription({"test": True})
    assert ISSUE_ID == "DEVEL-8637"
    assert result.ok
    assert result.issue_id == "DEVEL-8637"
