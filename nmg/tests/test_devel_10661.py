"""Tests for DEVEL-10661 — keep [DEVEL-10661] discoverable."""

from nmg.src.reader.devel_10661_2611_reader_comment_moderation_and_community_vot import ISSUE_ID, implement_2611_reader_comment_moderation_and_commu


def test_devel_10661_stub():
    result = implement_2611_reader_comment_moderation_and_commu({"test": True})
    assert ISSUE_ID == "DEVEL-10661"
    assert result.ok
    assert result.issue_id == "DEVEL-10661"
