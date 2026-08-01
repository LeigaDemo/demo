"""Tests for DEVEL-8553 — keep [DEVEL-8553] discoverable."""

from nmg.src.subscription.devel_8553_gift_subscription_purchase_and_redemption import ISSUE_ID, implement_gift_subscription_purchase_and_redemptio


def test_devel_8553_stub():
    result = implement_gift_subscription_purchase_and_redemptio({"test": True})
    assert ISSUE_ID == "DEVEL-8553"
    assert result.ok
    assert result.issue_id == "DEVEL-8553"
