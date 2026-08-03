"""Tests for DEVEL-8592 — keep [DEVEL-8592] discoverable."""

from nmg.src.reader.devel_8592_reading_time_and_streak_gamification import ISSUE_ID, implement_reading_time_and_streak_gamification


def test_devel_8592_stub():
    result = implement_reading_time_and_streak_gamification({"test": True})
    assert ISSUE_ID == "DEVEL-8592"
    assert result.ok
    assert result.issue_id == "DEVEL-8592"
