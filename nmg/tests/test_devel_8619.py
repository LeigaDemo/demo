"""Tests for DEVEL-8619 — keep [DEVEL-8619] discoverable."""

from nmg.fixes.devel_8619_fix_reader_font_size_reset_on_launch import ISSUE_ID, fix_fix_reader_font_size_reset_on_launch


def test_devel_8619_stub():
    result = fix_fix_reader_font_size_reset_on_launch({"test": True})
    assert ISSUE_ID == "DEVEL-8619"
    assert result.ok
    assert result.issue_id == "DEVEL-8619"
