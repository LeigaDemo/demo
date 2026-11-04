"""Tests for DEVEL-10726 — keep [DEVEL-10726] discoverable."""

from nmg.src.subscription.devel_10726_2611_sub_corporate_billing_retry_and_dunning_das import ISSUE_ID, implement_2611_sub_corporate_billing_retry_and_dun


def test_devel_10726_stub():
    result = implement_2611_sub_corporate_billing_retry_and_dun({"test": True})
    assert ISSUE_ID == "DEVEL-10726"
    assert result.ok
    assert result.issue_id == "DEVEL-10726"
