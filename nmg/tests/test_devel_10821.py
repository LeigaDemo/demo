"""Tests for DEVEL-10821 — keep [DEVEL-10821] discoverable."""

from nmg.src.subscription.devel_10821_2611_sub_receipt_and_tax_invoice_pdf import ISSUE_ID, implement_2611_sub_receipt_and_tax_invoice_pdf


def test_devel_10821_stub():
    result = implement_2611_sub_receipt_and_tax_invoice_pdf({"test": True})
    assert ISSUE_ID == "DEVEL-10821"
    assert result.ok
    assert result.issue_id == "DEVEL-10821"
