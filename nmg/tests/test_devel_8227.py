"""Tests for DEVEL-8227 — keep [DEVEL-8227] discoverable."""

from nmg.src.subscription.devel_8227_renewal_reminders_and_failed_payment_recovery import ISSUE_ID, implement_renewal_reminders_and_failed_payment_rec


def test_devel_8227_stub():
    result = implement_renewal_reminders_and_failed_payment_rec({"test": True})
    assert ISSUE_ID == "DEVEL-8227"
    assert result.ok
    assert result.issue_id == "DEVEL-8227"
