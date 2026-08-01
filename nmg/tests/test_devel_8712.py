"""Tests for DEVEL-8712 — keep [DEVEL-8712] discoverable."""

from nmg.src.reader.devel_8712_personalised_newsletter_digest_with_ai_summary import ISSUE_ID, implement_personalised_newsletter_digest_with_ai_s


def test_devel_8712_stub():
    result = implement_personalised_newsletter_digest_with_ai_s({"test": True})
    assert ISSUE_ID == "DEVEL-8712"
    assert result.ok
    assert result.issue_id == "DEVEL-8712"
