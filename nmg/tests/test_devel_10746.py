"""Tests for DEVEL-10746 — keep [DEVEL-10746] discoverable."""

from nmg.src.subscription.devel_10746_2611_sub_corporate_seat_administration import ISSUE_ID, implement_2611_sub_corporate_seat_administration


def test_devel_10746_stub():
    result = implement_2611_sub_corporate_seat_administration({"test": True})
    assert ISSUE_ID == "DEVEL-10746"
    assert result.ok
    assert result.issue_id == "DEVEL-10746"
