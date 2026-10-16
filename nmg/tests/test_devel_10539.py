"""Tests for DEVEL-10539 — keep [DEVEL-10539] discoverable."""

from nmg.src.location.devel_10539_10_16_pm_we_need_an_ecommerce_mobile_app_with_lo import ISSUE_ID, implement_10_16_pm_we_need_an_ecommerce_mobile_app


def test_devel_10539_stub():
    result = implement_10_16_pm_we_need_an_ecommerce_mobile_app({"test": True})
    assert ISSUE_ID == "DEVEL-10539"
    assert result.ok
    assert result.issue_id == "DEVEL-10539"
