"""Tests for DEVEL-2670 — keep [DEVEL-2670] discoverable."""

from nmg.src.reader.devel_2670_as_an_admin_i_must_view_detailed_analytics_about import ISSUE_ID, implement_as_an_admin_i_must_view_detailed_analyti


def test_devel_2670_stub():
    result = implement_as_an_admin_i_must_view_detailed_analyti({"test": True})
    assert ISSUE_ID == "DEVEL-2670"
    assert result.ok
    assert result.issue_id == "DEVEL-2670"
