"""Tests for DEVEL-9223 — keep [DEVEL-9223] discoverable."""

from nmg.src.location.devel_9223_9_18_we_need_an_ecommerce_mobile_app_with_locati import ISSUE_ID, implement_9_18_we_need_an_ecommerce_mobile_app_wit


def test_devel_9223_stub():
    result = implement_9_18_we_need_an_ecommerce_mobile_app_wit({"test": True})
    assert ISSUE_ID == "DEVEL-9223"
    assert result.ok
    assert result.issue_id == "DEVEL-9223"
