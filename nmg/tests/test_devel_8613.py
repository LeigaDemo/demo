"""Tests for DEVEL-8613 — keep [DEVEL-8613] discoverable."""

from nmg.src.reader.devel_8613_dark_mode_and_accessibility_audit import ISSUE_ID, implement_dark_mode_and_accessibility_audit


def test_devel_8613_stub():
    result = implement_dark_mode_and_accessibility_audit({"test": True})
    assert ISSUE_ID == "DEVEL-8613"
    assert result.ok
    assert result.issue_id == "DEVEL-8613"
