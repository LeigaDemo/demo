"""Tests for DEVEL-10921 — keep [DEVEL-10921] discoverable."""

from nmg.src.location.devel_10921_2611_lbs_delivery_fee_boundary_rules import ISSUE_ID, implement_2611_lbs_delivery_fee_boundary_rules


def test_devel_10921_stub():
    result = implement_2611_lbs_delivery_fee_boundary_rules({"test": True})
    assert ISSUE_ID == "DEVEL-10921"
    assert result.ok
    assert result.issue_id == "DEVEL-10921"
