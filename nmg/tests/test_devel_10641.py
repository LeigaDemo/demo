"""Tests for DEVEL-10641 — keep [DEVEL-10641] discoverable."""

from nmg.src.reader.devel_10641_2611_reader_bookmark_folders_and_cross_device_sy import ISSUE_ID, implement_2611_reader_bookmark_folders_and_cross_d


def test_devel_10641_stub():
    result = implement_2611_reader_bookmark_folders_and_cross_d({"test": True})
    assert ISSUE_ID == "DEVEL-10641"
    assert result.ok
    assert result.issue_id == "DEVEL-10641"
