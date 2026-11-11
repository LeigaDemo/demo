"""Tests for DEVEL-10651 — keep [DEVEL-10651] discoverable."""

from nmg.src.reader.devel_10651_2611_reader_breaking_news_push_quiet_hours import ISSUE_ID, implement_2611_reader_breaking_news_push_quiet_hou


def test_devel_10651_stub():
    result = implement_2611_reader_breaking_news_push_quiet_hou({"test": True})
    assert ISSUE_ID == "DEVEL-10651"
    assert result.ok
    assert result.issue_id == "DEVEL-10651"
