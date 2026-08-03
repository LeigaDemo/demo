"""Tests for DEVEL-8692 — keep [DEVEL-8692] discoverable."""

from nmg.src.location.devel_8692_location_based_poll_and_community_survey_feature import ISSUE_ID, implement_location_based_poll_and_community_survey


def test_devel_8692_stub():
    result = implement_location_based_poll_and_community_survey({"test": True})
    assert ISSUE_ID == "DEVEL-8692"
    assert result.ok
    assert result.issue_id == "DEVEL-8692"
