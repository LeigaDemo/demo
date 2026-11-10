"""Tests for DEVEL-10671 — keep [DEVEL-10671] discoverable."""

from nmg.src.reader.devel_10671_2611_reader_share_to_social_with_utm_tracking import ISSUE_ID, implement_2611_reader_share_to_social_with_utm_tra


def test_devel_10671_stub():
    result = implement_2611_reader_share_to_social_with_utm_tra({"test": True})
    assert ISSUE_ID == "DEVEL-10671"
    assert result.ok
    assert result.issue_id == "DEVEL-10671"
