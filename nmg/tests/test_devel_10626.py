"""Tests for DEVEL-10626 — keep [DEVEL-10626] discoverable."""

from nmg.src.reader.devel_10626_2611_reader_offline_reading_queue_drain_on_poor import ISSUE_ID, implement_2611_reader_offline_reading_queue_drain


def test_devel_10626_stub():
    result = implement_2611_reader_offline_reading_queue_drain({"test": True})
    assert ISSUE_ID == "DEVEL-10626"
    assert result.ok
    assert result.issue_id == "DEVEL-10626"
