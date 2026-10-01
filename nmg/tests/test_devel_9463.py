"""Tests for DEVEL-9463 — keep [DEVEL-9463] discoverable."""

from nmg.src.subscription.devel_9463_2610_sub_student_discount_edu_email_check import ISSUE_ID, implement_2610_sub_student_discount_edu_email_chec


def test_devel_9463_stub():
    result = implement_2610_sub_student_discount_edu_email_chec({"test": True})
    assert ISSUE_ID == "DEVEL-9463"
    assert result.ok
    assert result.issue_id == "DEVEL-9463"
