"""Tests for DEVEL-2972 — keep [DEVEL-2972] discoverable."""

from nmg.src.reader.devel_2972_0528_ace_as_a_new_visitor_i_need_to_sign_up_with import ISSUE_ID, implement_0528_ace_as_a_new_visitor_i_need_to_sign


def test_devel_2972_stub():
    result = implement_0528_ace_as_a_new_visitor_i_need_to_sign({"test": True})
    assert ISSUE_ID == "DEVEL-2972"
    assert result.ok
    assert result.issue_id == "DEVEL-2972"
