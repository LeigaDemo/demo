"""Tests for DEVEL-8232 — keep [DEVEL-8232] discoverable."""

from nmg.src.subscription.devel_8232_corporate_subscription_seat_administration import ISSUE_ID, implement_corporate_subscription_seat_administrati


def test_devel_8232_stub():
    result = implement_corporate_subscription_seat_administrati({"test": True})
    assert ISSUE_ID == "DEVEL-8232"
    assert result.ok
    assert result.issue_id == "DEVEL-8232"
