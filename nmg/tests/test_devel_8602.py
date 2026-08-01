"""Tests for DEVEL-8602 — keep [DEVEL-8602] discoverable."""

from nmg.src.reader.devel_8602_bookmark_folders_and_sync_across_devices import ISSUE_ID, implement_bookmark_folders_and_sync_across_devices


def test_devel_8602_stub():
    result = implement_bookmark_folders_and_sync_across_devices({"test": True})
    assert ISSUE_ID == "DEVEL-8602"
    assert result.ok
    assert result.issue_id == "DEVEL-8602"
