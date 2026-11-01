"""Tests for DEVEL-10646 — keep [DEVEL-10646] discoverable."""

from nmg.src.reader.devel_10646_2611_reader_audio_article_player_playback_contro import ISSUE_ID, implement_2611_reader_audio_article_player_playbac


def test_devel_10646_stub():
    result = implement_2611_reader_audio_article_player_playbac({"test": True})
    assert ISSUE_ID == "DEVEL-10646"
    assert result.ok
    assert result.issue_id == "DEVEL-10646"
