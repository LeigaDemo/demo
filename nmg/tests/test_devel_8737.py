"""Tests for DEVEL-8737 — keep [DEVEL-8737] discoverable."""

from nmg.src.reader.devel_8737_article_reading_progress_sync_across_devices import ISSUE_ID, implement_article_reading_progress_sync_across_dev


def test_devel_8737_stub():
    result = implement_article_reading_progress_sync_across_dev({"test": True})
    assert ISSUE_ID == "DEVEL-8737"
    assert result.ok
    assert result.issue_id == "DEVEL-8737"
