"""Tests for DEVEL-8567 — keep [DEVEL-8567] discoverable."""

from nmg.src.location.devel_8567_walking_direction_with_ar_overlay import ISSUE_ID, implement_walking_direction_with_ar_overlay


def test_devel_8567_stub():
    result = implement_walking_direction_with_ar_overlay({"test": True})
    assert ISSUE_ID == "DEVEL-8567"
    assert result.ok
    assert result.issue_id == "DEVEL-8567"
