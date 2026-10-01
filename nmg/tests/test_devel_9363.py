"""Tests for DEVEL-9363 — keep [DEVEL-9363] discoverable."""

from nmg.src.reader.devel_9363_2610_reader_breaking_news_push_quiet_hours import ISSUE_ID, implement_2610_reader_breaking_news_push_quiet_hou


def test_devel_9363_stub():
    result = implement_2610_reader_breaking_news_push_quiet_hou({"test": True})
    assert ISSUE_ID == "DEVEL-9363"
    assert result.ok
    assert result.issue_id == "DEVEL-9363"
