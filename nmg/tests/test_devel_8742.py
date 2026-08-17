"""Tests for DEVEL-8742 — keep [DEVEL-8742] discoverable."""

from nmg.src.reader.devel_8742_article_font_family_and_line_spacing_customisati import ISSUE_ID, implement_article_font_family_and_line_spacing_cus


def test_devel_8742_stub():
    result = implement_article_font_family_and_line_spacing_cus({"test": True})
    assert ISSUE_ID == "DEVEL-8742"
    assert result.ok
    assert result.issue_id == "DEVEL-8742"
