"""Tests for DEVEL-8662 — keep [DEVEL-8662] discoverable."""

from nmg.src.subscription.devel_8662_membership_referral_program_and_reward_tracking import ISSUE_ID, implement_membership_referral_program_and_reward_t


def test_devel_8662_stub():
    result = implement_membership_referral_program_and_reward_t({"test": True})
    assert ISSUE_ID == "DEVEL-8662"
    assert result.ok
    assert result.issue_id == "DEVEL-8662"
