"""Tests for DEVEL-10656 — keep [DEVEL-10656] discoverable."""

from nmg.src.reader.devel_10656_2611_reader_personalised_newsletter_digest import ISSUE_ID, implement_2611_reader_personalised_newsletter_dige


def test_devel_10656_stub():
    result = implement_2611_reader_personalised_newsletter_dige({"test": True})
    assert ISSUE_ID == "DEVEL-10656"
    assert result.ok
    assert result.issue_id == "DEVEL-10656"
