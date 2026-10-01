"""Tests for DEVEL-9518 — keep [DEVEL-9518] discoverable."""

from nmg.src.subscription.devel_9518_2610_sub_subscription_pause_and_resume import ISSUE_ID, implement_2610_sub_subscription_pause_and_resume


def test_devel_9518_stub():
    result = implement_2610_sub_subscription_pause_and_resume({"test": True})
    assert ISSUE_ID == "DEVEL-9518"
    assert result.ok
    assert result.issue_id == "DEVEL-9518"
