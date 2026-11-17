"""Tests for DEVEL-10636 — keep [DEVEL-10636] discoverable."""

from nmg.src.reader.devel_10636_2611_reader_article_reading_progress_sync import ISSUE_ID, implement_2611_reader_article_reading_progress_syn


def test_devel_10636_stub():
    result = implement_2611_reader_article_reading_progress_syn({"test": True})
    assert ISSUE_ID == "DEVEL-10636"
    assert result.ok
    assert result.issue_id == "DEVEL-10636"
