"""Tests for DEVEL-8702 — keep [DEVEL-8702] discoverable."""

from nmg.src.location.devel_8702_district_popularity_heatmap_and_trending_areas import ISSUE_ID, implement_district_popularity_heatmap_and_trending


def test_devel_8702_stub():
    result = implement_district_popularity_heatmap_and_trending({"test": True})
    assert ISSUE_ID == "DEVEL-8702"
    assert result.ok
    assert result.issue_id == "DEVEL-8702"
