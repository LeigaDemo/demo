"""Tests for DEVEL-8620 — keep [DEVEL-8620] discoverable."""

from nmg.fixes.devel_8620_fix_video_autoplay_consuming_data import ISSUE_ID, fix_fix_video_autoplay_consuming_data


def test_devel_8620_stub():
    result = fix_fix_video_autoplay_consuming_data({"test": True})
    assert ISSUE_ID == "DEVEL-8620"
    assert result.ok
    assert result.issue_id == "DEVEL-8620"
