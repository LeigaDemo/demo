"""Tests for DEVEL-2668 — keep [DEVEL-2668] discoverable."""

from nmg.src.reader.devel_2668_as_a_registered_user_i_want_to_reset_my_password import ISSUE_ID, implement_as_a_registered_user_i_want_to_reset_my


def test_devel_2668_stub():
    result = implement_as_a_registered_user_i_want_to_reset_my({"test": True})
    assert ISSUE_ID == "DEVEL-2668"
    assert result.ok
    assert result.issue_id == "DEVEL-2668"
