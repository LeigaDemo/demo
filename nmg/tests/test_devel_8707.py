"""Tests for DEVEL-8707 — keep [DEVEL-8707] discoverable."""

from nmg.src.location.devel_8707_public_transport_arrival_time_with_mtr_api_integ import ISSUE_ID, implement_public_transport_arrival_time_with_mtr_a


def test_devel_8707_stub():
    result = implement_public_transport_arrival_time_with_mtr_a({"test": True})
    assert ISSUE_ID == "DEVEL-8707"
    assert result.ok
    assert result.issue_id == "DEVEL-8707"
