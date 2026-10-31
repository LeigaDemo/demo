"""Tests for DEVEL-10806 — keep [DEVEL-10806] discoverable."""

from nmg.src.reader.devel_10806_2611_reader_reading_streak_that_survives_offline import ISSUE_ID, implement_2611_reader_reading_streak_that_survives


def test_devel_10806_stub():
    result = implement_2611_reader_reading_streak_that_survives({"test": True})
    assert ISSUE_ID == "DEVEL-10806"
    assert result.ok
    assert result.issue_id == "DEVEL-10806"
