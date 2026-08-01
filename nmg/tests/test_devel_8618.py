"""Tests for DEVEL-8618 — keep [DEVEL-8618] discoverable."""

from nmg.fixes.devel_8618_fix_push_notification_double_tap_trigger import ISSUE_ID, fix_fix_push_notification_double_tap_trigger


def test_devel_8618_stub():
    result = fix_fix_push_notification_double_tap_trigger({"test": True})
    assert ISSUE_ID == "DEVEL-8618"
    assert result.ok
    assert result.issue_id == "DEVEL-8618"
