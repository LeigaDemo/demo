"""Tests for DEVEL-8206 — keep [DEVEL-8206] discoverable."""

from nmg.src.location.devel_8206_district_news_and_events_map import ISSUE_ID, implement_district_news_and_events_map


def test_devel_8206_stub():
    result = implement_district_news_and_events_map({"test": True})
    assert ISSUE_ID == "DEVEL-8206"
    assert result.ok
    assert result.issue_id == "DEVEL-8206"
