"""Tests for DEVEL-9353 — keep [DEVEL-9353] discoverable."""

from nmg.src.reader.devel_9353_2610_reader_bookmark_folders_and_cross_device_sy import ISSUE_ID, implement_2610_reader_bookmark_folders_and_cross_d


def test_devel_9353_stub():
    result = implement_2610_reader_bookmark_folders_and_cross_d({"test": True})
    assert ISSUE_ID == "DEVEL-9353"
    assert result.ok
    assert result.issue_id == "DEVEL-9353"
