"""Tests for DEVEL-8558 — keep [DEVEL-8558] discoverable."""

from nmg.fixes.devel_8558_fix_duplicate_charge_on_renewal_retry import ISSUE_ID, fix_fix_duplicate_charge_on_renewal_retry


def test_devel_8558_stub():
    result = fix_fix_duplicate_charge_on_renewal_retry({"test": True})
    assert ISSUE_ID == "DEVEL-8558"
    assert result.ok
    assert result.issue_id == "DEVEL-8558"
