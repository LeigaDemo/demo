"""Tests for DEVEL-8632 — keep [DEVEL-8632] discoverable."""

from nmg.src.subscription.devel_8632_subscription_cancellation_and_reactivation_flow import ISSUE_ID, implement_subscription_cancellation_and_reactivati


def test_devel_8632_stub():
    result = implement_subscription_cancellation_and_reactivati({"test": True})
    assert ISSUE_ID == "DEVEL-8632"
    assert result.ok
    assert result.issue_id == "DEVEL-8632"
