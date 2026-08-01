"""Tests for DEVEL-8191 — keep [DEVEL-8191] discoverable."""

from nmg.src.reader.devel_8191_breaking_news_push_with_smart_quiet_hours import ISSUE_ID, implement_breaking_news_push_with_smart_quiet_hour


def test_devel_8191_stub():
    result = implement_breaking_news_push_with_smart_quiet_hour({"test": True})
    assert ISSUE_ID == "DEVEL-8191"
    assert result.ok
    assert result.issue_id == "DEVEL-8191"
