"""Tests for DEVEL-8597 — keep [DEVEL-8597] discoverable."""

from nmg.src.reader.devel_8597_comment_moderation_and_community_voting import ISSUE_ID, implement_comment_moderation_and_community_voting


def test_devel_8597_stub():
    result = implement_comment_moderation_and_community_voting({"test": True})
    assert ISSUE_ID == "DEVEL-8597"
    assert result.ok
    assert result.issue_id == "DEVEL-8597"
