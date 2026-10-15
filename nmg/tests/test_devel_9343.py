"""Tests for DEVEL-9343 — keep [DEVEL-9343] discoverable."""

from nmg.src.reader.devel_9343_2610_reader_reader_font_and_theme_persistence_ac import ISSUE_ID, implement_2610_reader_reader_font_and_theme_persis


def test_devel_9343_stub():
    result = implement_2610_reader_reader_font_and_theme_persis({"test": True})
    assert ISSUE_ID == "DEVEL-9343"
    assert result.ok
    assert result.issue_id == "DEVEL-9343"
