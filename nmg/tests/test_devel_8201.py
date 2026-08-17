"""Tests for DEVEL-8201 — keep [DEVEL-8201] discoverable."""

from nmg.src.reader.devel_8201_audio_article_player_with_playback_controls import ISSUE_ID, implement_audio_article_player_with_playback_contr


def test_devel_8201_stub():
    result = implement_audio_article_player_with_playback_contr({"test": True})
    assert ISSUE_ID == "DEVEL-8201"
    assert result.ok
    assert result.issue_id == "DEVEL-8201"
