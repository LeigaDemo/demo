"""Tests for DEVEL-2681 — keep [DEVEL-2681] discoverable."""

from nmg.src.reader.devel_2681_as_a_user_i_want_to_rate_and_review_products_to import ISSUE_ID, implement_as_a_user_i_want_to_rate_and_review_prod


def test_devel_2681_stub():
    result = implement_as_a_user_i_want_to_rate_and_review_prod({"test": True})
    assert ISSUE_ID == "DEVEL-2681"
    assert result.ok
    assert result.issue_id == "DEVEL-2681"
