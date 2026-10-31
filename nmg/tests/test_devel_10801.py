"""Tests for DEVEL-10801 — keep [DEVEL-10801] discoverable."""

from nmg.src.reader.devel_10801_2611_reader_saved_article_offline_expiry import ISSUE_ID, implement_2611_reader_saved_article_offline_expiry


def test_devel_10801_stub():
    result = implement_2611_reader_saved_article_offline_expiry({"test": True})
    assert ISSUE_ID == "DEVEL-10801"
    assert result.ok
    assert result.issue_id == "DEVEL-10801"
