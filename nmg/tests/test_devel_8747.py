"""Tests for DEVEL-8747 — keep [DEVEL-8747] discoverable."""

from nmg.src.subscription.devel_8747_topic_subscription_and_keyword_alert_preferences import ISSUE_ID, implement_topic_subscription_and_keyword_alert_pre


def test_devel_8747_stub():
    result = implement_topic_subscription_and_keyword_alert_pre({"test": True})
    assert ISSUE_ID == "DEVEL-8747"
    assert result.ok
    assert result.issue_id == "DEVEL-8747"
