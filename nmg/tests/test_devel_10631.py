"""Tests for DEVEL-10631 — keep [DEVEL-10631] discoverable."""

from nmg.src.reader.devel_10631_2611_reader_reader_font_and_theme_persistence_ac import ISSUE_ID, implement_2611_reader_reader_font_and_theme_persis


def test_devel_10631_stub():
    result = implement_2611_reader_reader_font_and_theme_persis({"test": True})
    assert ISSUE_ID == "DEVEL-10631"
    assert result.ok
    assert result.issue_id == "DEVEL-10631"
