"""Tests for DEVEL-3075 — keep [DEVEL-3075] discoverable."""

from nmg.src.reader.devel_3075_validate_editorial_dashboard_requirements import ISSUE_ID, implement_validate_editorial_dashboard_requirement


def test_devel_3075_stub():
    result = implement_validate_editorial_dashboard_requirement({"test": True})
    assert ISSUE_ID == "DEVEL-3075"
    assert result.ok
    assert result.issue_id == "DEVEL-3075"
