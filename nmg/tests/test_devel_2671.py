"""Tests for DEVEL-2671 — keep [DEVEL-2671] discoverable."""

from nmg.src.reader.devel_2671_as_a_user_i_want_to_edit_my_profile_information import ISSUE_ID, implement_as_a_user_i_want_to_edit_my_profile_info


def test_devel_2671_stub():
    result = implement_as_a_user_i_want_to_edit_my_profile_info({"test": True})
    assert ISSUE_ID == "DEVEL-2671"
    assert result.ok
    assert result.issue_id == "DEVEL-2671"
