"""Tests for DEVEL-9177 — keep [DEVEL-9177] discoverable."""

from nmg.src.location.devel_9177_9_10_pm_we_need_to_build_a_duty_free_ecommerce_m import ISSUE_ID, implement_9_10_pm_we_need_to_build_a_duty_free_eco


def test_devel_9177_stub():
    result = implement_9_10_pm_we_need_to_build_a_duty_free_eco({"test": True})
    assert ISSUE_ID == "DEVEL-9177"
    assert result.ok
    assert result.issue_id == "DEVEL-9177"
