"""Tests for DEVEL-8562 — keep [DEVEL-8562] discoverable."""

from nmg.src.location.devel_8562_indoor_venue_mapping_for_malls_and_mtr import ISSUE_ID, implement_indoor_venue_mapping_for_malls_and_mtr


def test_devel_8562_stub():
    result = implement_indoor_venue_mapping_for_malls_and_mtr({"test": True})
    assert ISSUE_ID == "DEVEL-8562"
    assert result.ok
    assert result.issue_id == "DEVEL-8562"
