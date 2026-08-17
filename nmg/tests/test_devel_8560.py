"""Tests for DEVEL-8560 — keep [DEVEL-8560] discoverable."""

from nmg.fixes.devel_8560_fix_corporate_seat_invite_email import ISSUE_ID, fix_fix_corporate_seat_invite_email


def test_devel_8560_stub():
    result = fix_fix_corporate_seat_invite_email({"test": True})
    assert ISSUE_ID == "DEVEL-8560"
    assert result.ok
    assert result.issue_id == "DEVEL-8560"
