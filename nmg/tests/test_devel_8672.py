"""Tests for DEVEL-8672 — keep [DEVEL-8672] discoverable."""

from nmg.src.location.devel_8672_augmented_reality_street_view_overlay_for_landma import ISSUE_ID, implement_augmented_reality_street_view_overlay_fo


def test_devel_8672_stub():
    result = implement_augmented_reality_street_view_overlay_fo({"test": True})
    assert ISSUE_ID == "DEVEL-8672"
    assert result.ok
    assert result.issue_id == "DEVEL-8672"
