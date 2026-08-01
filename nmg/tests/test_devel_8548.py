"""Tests for DEVEL-8548 — keep [DEVEL-8548] discoverable."""

from nmg.src.subscription.devel_8548_annual_plan_upgrade_and_proration_logic import ISSUE_ID, implement_annual_plan_upgrade_and_proration_logic


def test_devel_8548_stub():
    result = implement_annual_plan_upgrade_and_proration_logic({"test": True})
    assert ISSUE_ID == "DEVEL-8548"
    assert result.ok
    assert result.issue_id == "DEVEL-8548"
