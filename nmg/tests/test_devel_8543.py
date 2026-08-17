"""Tests for DEVEL-8543 — keep [DEVEL-8543] discoverable."""

from nmg.src.subscription.devel_8543_subscription_pause_and_resume_flow import ISSUE_ID, implement_subscription_pause_and_resume_flow


def test_devel_8543_stub():
    result = implement_subscription_pause_and_resume_flow({"test": True})
    assert ISSUE_ID == "DEVEL-8543"
    assert result.ok
    assert result.issue_id == "DEVEL-8543"
