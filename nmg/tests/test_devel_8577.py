"""Tests for DEVEL-8577 — keep [DEVEL-8577] discoverable."""

from nmg.src.location.devel_8577_location_based_breaking_news_radius_filter import ISSUE_ID, implement_location_based_breaking_news_radius_filt


def test_devel_8577_stub():
    result = implement_location_based_breaking_news_radius_filt({"test": True})
    assert ISSUE_ID == "DEVEL-8577"
    assert result.ok
    assert result.issue_id == "DEVEL-8577"
