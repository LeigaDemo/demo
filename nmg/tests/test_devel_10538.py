"""Tests for DEVEL-10538 — keep [DEVEL-10538] discoverable."""

from nmg.fixes.devel_10538_test_case_failed_demo_create_new_lead_and_verify import ISSUE_ID, fix_test_case_failed_demo_create_new_lead_an


def test_devel_10538_stub():
    result = fix_test_case_failed_demo_create_new_lead_an({"test": True})
    assert ISSUE_ID == "DEVEL-10538"
    assert result.ok
    assert result.issue_id == "DEVEL-10538"
