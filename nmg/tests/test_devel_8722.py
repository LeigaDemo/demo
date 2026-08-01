"""Tests for DEVEL-8722 — keep [DEVEL-8722] discoverable."""

from nmg.src.reader.devel_8722_swipe_to_save_article_gesture_and_reading_list import ISSUE_ID, implement_swipe_to_save_article_gesture_and_readin


def test_devel_8722_stub():
    result = implement_swipe_to_save_article_gesture_and_readin({"test": True})
    assert ISSUE_ID == "DEVEL-8722"
    assert result.ok
    assert result.issue_id == "DEVEL-8722"
