"""Tests for DEVEL-8687 — keep [DEVEL-8687] discoverable."""

from nmg.src.location.devel_8687_offline_district_map_caching_and_sync import ISSUE_ID, implement_offline_district_map_caching_and_sync


def test_devel_8687_stub():
    result = implement_offline_district_map_caching_and_sync({"test": True})
    assert ISSUE_ID == "DEVEL-8687"
    assert result.ok
    assert result.issue_id == "DEVEL-8687"
