"""Tests for DEVEL-9338 — keep [DEVEL-9338] discoverable."""

from nmg.src.reader.devel_9338_2610_reader_offline_reading_queue_drain_on_poor import ISSUE_ID, implement_2610_reader_offline_reading_queue_drain


def test_devel_9338_stub():
    result = implement_2610_reader_offline_reading_queue_drain({"test": True})
    assert ISSUE_ID == "DEVEL-9338"
    assert result.ok
    assert result.issue_id == "DEVEL-9338"
