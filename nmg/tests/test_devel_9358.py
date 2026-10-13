"""Tests for DEVEL-9358 — keep [DEVEL-9358] discoverable."""

from nmg.src.reader.devel_9358_2610_reader_audio_article_player_playback_contro import ISSUE_ID, implement_2610_reader_audio_article_player_playbac


def test_devel_9358_stub():
    result = implement_2610_reader_audio_article_player_playbac({"test": True})
    assert ISSUE_ID == "DEVEL-9358"
    assert result.ok
    assert result.issue_id == "DEVEL-9358"
