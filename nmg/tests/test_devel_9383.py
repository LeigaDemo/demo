"""Tests for DEVEL-9383 — keep [DEVEL-9383] discoverable."""

from nmg.src.reader.devel_9383_2610_reader_share_to_social_with_utm_tracking import ISSUE_ID, implement_2610_reader_share_to_social_with_utm_tra


def test_devel_9383_stub():
    result = implement_2610_reader_share_to_social_with_utm_tra({"test": True})
    assert ISSUE_ID == "DEVEL-9383"
    assert result.ok
    assert result.issue_id == "DEVEL-9383"
