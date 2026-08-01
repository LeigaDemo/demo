"""Tests for DEVEL-8647 — keep [DEVEL-8647] discoverable."""

from nmg.src.subscription.devel_8647_apple_in_app_purchase_server_side_validation import ISSUE_ID, implement_apple_in_app_purchase_server_side_valida


def test_devel_8647_stub():
    result = implement_apple_in_app_purchase_server_side_valida({"test": True})
    assert ISSUE_ID == "DEVEL-8647"
    assert result.ok
    assert result.issue_id == "DEVEL-8647"
