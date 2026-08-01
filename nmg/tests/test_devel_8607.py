"""Tests for DEVEL-8607 — keep [DEVEL-8607] discoverable."""

from nmg.fixes.devel_8607_fix_article_image_crop_on_ipad import ISSUE_ID, fix_fix_article_image_crop_on_ipad


def test_devel_8607_stub():
    result = fix_fix_article_image_crop_on_ipad({"test": True})
    assert ISSUE_ID == "DEVEL-8607"
    assert result.ok
    assert result.issue_id == "DEVEL-8607"
