"""Tests for DEVEL-10666 — keep [DEVEL-10666] discoverable."""

from nmg.src.reader.devel_10666_2611_reader_dark_mode_and_accessibility_audit import ISSUE_ID, implement_2611_reader_dark_mode_and_accessibility


def test_devel_10666_stub():
    result = implement_2611_reader_dark_mode_and_accessibility({"test": True})
    assert ISSUE_ID == "DEVEL-10666"
    assert result.ok
    assert result.issue_id == "DEVEL-10666"
