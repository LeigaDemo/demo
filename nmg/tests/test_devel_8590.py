"""Tests for DEVEL-8590 — keep [DEVEL-8590] discoverable."""

from nmg.fixes.devel_8590_fix_district_boundary_overlap_for_sheung_wan import ISSUE_ID, fix_fix_district_boundary_overlap_for_sheung


def test_devel_8590_stub():
    result = fix_fix_district_boundary_overlap_for_sheung({"test": True})
    assert ISSUE_ID == "DEVEL-8590"
    assert result.ok
    assert result.issue_id == "DEVEL-8590"
