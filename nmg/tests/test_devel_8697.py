"""Tests for DEVEL-8697 — keep [DEVEL-8697] discoverable."""

from nmg.src.location.devel_8697_geo_fenced_push_notification_scheduling_and_freq import ISSUE_ID, implement_geo_fenced_push_notification_scheduling


def test_devel_8697_stub():
    result = implement_geo_fenced_push_notification_scheduling({"test": True})
    assert ISSUE_ID == "DEVEL-8697"
    assert result.ok
    assert result.issue_id == "DEVEL-8697"
