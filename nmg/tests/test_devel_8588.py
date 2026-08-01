"""Tests for DEVEL-8588 — keep [DEVEL-8588] discoverable."""

from nmg.fixes.devel_8588_fix_map_tile_loading_on_slow_networks import ISSUE_ID, fix_fix_map_tile_loading_on_slow_networks


def test_devel_8588_stub():
    result = fix_fix_map_tile_loading_on_slow_networks({"test": True})
    assert ISSUE_ID == "DEVEL-8588"
    assert result.ok
    assert result.issue_id == "DEVEL-8588"
