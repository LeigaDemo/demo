"""Tests for DEVEL-8657 — keep [DEVEL-8657] discoverable."""

from nmg.src.subscription.devel_8657_subscription_plan_comparison_and_upgrade_prompt import ISSUE_ID, implement_subscription_plan_comparison_and_upgrade


def test_devel_8657_stub():
    result = implement_subscription_plan_comparison_and_upgrade({"test": True})
    assert ISSUE_ID == "DEVEL-8657"
    assert result.ok
    assert result.issue_id == "DEVEL-8657"
