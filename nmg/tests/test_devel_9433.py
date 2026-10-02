"""Tests for DEVEL-9433 — keep [DEVEL-9433] discoverable."""

from nmg.src.subscription.devel_9433_2610_sub_entitlement_webhook_replay_for_failed_r import ISSUE_ID, implement_2610_sub_entitlement_webhook_replay_for


def test_devel_9433_stub():
    result = implement_2610_sub_entitlement_webhook_replay_for({"test": True})
    assert ISSUE_ID == "DEVEL-9433"
    assert result.ok
    assert result.issue_id == "DEVEL-9433"
