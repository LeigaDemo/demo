"""Tests for DEVEL-10871 — keep [DEVEL-10871] discoverable."""

from nmg.src.location.devel_10871_2611_lbs_public_facility_finder import ISSUE_ID, implement_2611_lbs_public_facility_finder


def test_devel_10871_stub():
    result = implement_2611_lbs_public_facility_finder({"test": True})
    assert ISSUE_ID == "DEVEL-10871"
    assert result.ok
    assert result.issue_id == "DEVEL-10871"
