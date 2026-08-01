"""Tests for DEVEL-8727 — keep [DEVEL-8727] discoverable."""

from nmg.src.reader.devel_8727_live_blog_real_time_update_with_websocket import ISSUE_ID, implement_live_blog_real_time_update_with_websocke


def test_devel_8727_stub():
    result = implement_live_blog_real_time_update_with_websocke({"test": True})
    assert ISSUE_ID == "DEVEL-8727"
    assert result.ok
    assert result.issue_id == "DEVEL-8727"
