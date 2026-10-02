"""Tests for DEVEL-9378 — keep [DEVEL-9378] discoverable."""

from nmg.src.reader.devel_9378_2610_reader_dark_mode_and_accessibility_audit import ISSUE_ID, implement_2610_reader_dark_mode_and_accessibility


def test_devel_9378_stub():
    result = implement_2610_reader_dark_mode_and_accessibility({"test": True})
    assert ISSUE_ID == "DEVEL-9378"
    assert result.ok
    assert result.issue_id == "DEVEL-9378"
