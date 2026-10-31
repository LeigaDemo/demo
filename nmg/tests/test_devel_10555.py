"""Tests for DEVEL-10555 — keep [DEVEL-10555] discoverable."""

from nmg.fixes.devel_10555_test_case_failed_demo_create_new_lead_and_verify import ISSUE_ID, fix_test_case_failed_demo_create_new_lead_an


def test_devel_10555_stub():
    result = fix_test_case_failed_demo_create_new_lead_an({"test": True})
    assert ISSUE_ID == "DEVEL-10555"
    assert result.ok
    assert result.issue_id == "DEVEL-10555"
