"""Tests for DEVEL-8627 — keep [DEVEL-8627] discoverable."""

from nmg.src.subscription.devel_8627_senior_citizen_digital_subscription_plan import ISSUE_ID, implement_senior_citizen_digital_subscription_plan


def test_devel_8627_stub():
    result = implement_senior_citizen_digital_subscription_plan({"test": True})
    assert ISSUE_ID == "DEVEL-8627"
    assert result.ok
    assert result.issue_id == "DEVEL-8627"
