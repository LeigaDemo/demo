"""Tests for DEVEL-9393 — keep [DEVEL-9393] discoverable."""

from nmg.src.location.devel_9393_2610_lbs_store_hour_pins_on_the_district_map import ISSUE_ID, implement_2610_lbs_store_hour_pins_on_the_district


def test_devel_9393_stub():
    result = implement_2610_lbs_store_hour_pins_on_the_district({"test": True})
    assert ISSUE_ID == "DEVEL-9393"
    assert result.ok
    assert result.issue_id == "DEVEL-9393"
