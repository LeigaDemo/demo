"""Tests for DEVEL-8572 — keep [DEVEL-8572] discoverable."""

from nmg.src.location.devel_8572_district_weather_and_air_quality_widget import ISSUE_ID, implement_district_weather_and_air_quality_widget


def test_devel_8572_stub():
    result = implement_district_weather_and_air_quality_widget({"test": True})
    assert ISSUE_ID == "DEVEL-8572"
    assert result.ok
    assert result.issue_id == "DEVEL-8572"
