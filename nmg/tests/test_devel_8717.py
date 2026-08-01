"""Tests for DEVEL-8717 — keep [DEVEL-8717] discoverable."""

from nmg.src.reader.devel_8717_reader_preference_learning_and_content_recommend import ISSUE_ID, implement_reader_preference_learning_and_content_r


def test_devel_8717_stub():
    result = implement_reader_preference_learning_and_content_r({"test": True})
    assert ISSUE_ID == "DEVEL-8717"
    assert result.ok
    assert result.issue_id == "DEVEL-8717"
