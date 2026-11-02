"""Tests for DEVEL-10751 — keep [DEVEL-10751] discoverable."""

from nmg.src.subscription.devel_10751_2611_sub_apple_in_app_purchase_server_side_valid import ISSUE_ID, implement_2611_sub_apple_in_app_purchase_server_si


def test_devel_10751_stub():
    result = implement_2611_sub_apple_in_app_purchase_server_si({"test": True})
    assert ISSUE_ID == "DEVEL-10751"
    assert result.ok
    assert result.issue_id == "DEVEL-10751"
