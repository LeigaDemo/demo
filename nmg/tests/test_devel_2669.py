"""Tests for DEVEL-2669 — keep [DEVEL-2669] discoverable."""

from nmg.src.reader.devel_2669_as_a_new_visitor_i_need_to_sign_up_with_my_email import ISSUE_ID, implement_as_a_new_visitor_i_need_to_sign_up_with


def test_devel_2669_stub():
    result = implement_as_a_new_visitor_i_need_to_sign_up_with({"test": True})
    assert ISSUE_ID == "DEVEL-2669"
    assert result.ok
    assert result.issue_id == "DEVEL-2669"
