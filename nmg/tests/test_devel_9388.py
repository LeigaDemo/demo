"""Tests for DEVEL-9388 — keep [DEVEL-9388] discoverable."""

from nmg.src.reader.devel_9388_2610_reader_live_blog_updates_over_websocket import ISSUE_ID, implement_2610_reader_live_blog_updates_over_webso


def test_devel_9388_stub():
    result = implement_2610_reader_live_blog_updates_over_webso({"test": True})
    assert ISSUE_ID == "DEVEL-9388"
    assert result.ok
    assert result.issue_id == "DEVEL-9388"
