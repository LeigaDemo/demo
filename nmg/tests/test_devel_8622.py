"""Tests for DEVEL-8622 — keep [DEVEL-8622] discoverable."""

from nmg.src.subscription.devel_8622_student_discount_verification_with_valid_edu_ema import ISSUE_ID, implement_student_discount_verification_with_valid


def test_devel_8622_stub():
    result = implement_student_discount_verification_with_valid({"test": True})
    assert ISSUE_ID == "DEVEL-8622"
    assert result.ok
    assert result.issue_id == "DEVEL-8622"
