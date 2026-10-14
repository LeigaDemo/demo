"""Tests for DEVEL-10522 — keep [DEVEL-10522] discoverable."""

from nmg.src.location.devel_10522_10_14_am_we_need_an_ecommerce_mobile_app_with_lo import ISSUE_ID, implement_10_14_am_we_need_an_ecommerce_mobile_app


def test_devel_10522_stub():
    result = implement_10_14_am_we_need_an_ecommerce_mobile_app({"test": True})
    assert ISSUE_ID == "DEVEL-10522"
    assert result.ok
    assert result.issue_id == "DEVEL-10522"
