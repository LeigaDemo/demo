"""Tests for DEVEL-10816 — keep [DEVEL-10816] discoverable."""

from nmg.src.subscription.devel_10816_2611_sub_subscription_pause_and_resume import ISSUE_ID, implement_2611_sub_subscription_pause_and_resume


def test_devel_10816_stub():
    result = implement_2611_sub_subscription_pause_and_resume({"test": True})
    assert ISSUE_ID == "DEVEL-10816"
    assert result.ok
    assert result.issue_id == "DEVEL-10816"
