"""Tests for DEVEL-8196 — keep [DEVEL-8196] discoverable."""

from nmg.src.reader.devel_8196_offline_reading_for_saved_articles import ISSUE_ID, implement_offline_reading_for_saved_articles


def test_devel_8196_stub():
    result = implement_offline_reading_for_saved_articles({"test": True})
    assert ISSUE_ID == "DEVEL-8196"
    assert result.ok
    assert result.issue_id == "DEVEL-8196"
