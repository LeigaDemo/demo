"""Tests for DEVEL-8608 — keep [DEVEL-8608] discoverable."""

from nmg.src.reader.devel_8608_share_to_social_with_utm_tracking import ISSUE_ID, implement_share_to_social_with_utm_tracking


def test_devel_8608_stub():
    result = implement_share_to_social_with_utm_tracking({"test": True})
    assert ISSUE_ID == "DEVEL-8608"
    assert result.ok
    assert result.issue_id == "DEVEL-8608"
