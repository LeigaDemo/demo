"""Tests for DEVEL-10706 — keep [DEVEL-10706] discoverable."""

from nmg.src.location.devel_10706_2611_lbs_district_popularity_heatmap import ISSUE_ID, implement_2611_lbs_district_popularity_heatmap


def test_devel_10706_stub():
    result = implement_2611_lbs_district_popularity_heatmap({"test": True})
    assert ISSUE_ID == "DEVEL-10706"
    assert result.ok
    assert result.issue_id == "DEVEL-10706"
