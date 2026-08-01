"""Tests for DEVEL-8186 — keep [DEVEL-8186] discoverable."""

from nmg.src.reader.devel_8186_topic_following_and_personalised_alerts import ISSUE_ID, implement_topic_following_and_personalised_alerts


def test_devel_8186_stub():
    result = implement_topic_following_and_personalised_alerts({"test": True})
    assert ISSUE_ID == "DEVEL-8186"
    assert result.ok
    assert result.issue_id == "DEVEL-8186"
