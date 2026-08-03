"""Tests for DEVEL-8642 — keep [DEVEL-8642] discoverable."""

from nmg.src.subscription.devel_8642_subscription_receipt_and_tax_invoice_pdf_generat import ISSUE_ID, implement_subscription_receipt_and_tax_invoice_pdf


def test_devel_8642_stub():
    result = implement_subscription_receipt_and_tax_invoice_pdf({"test": True})
    assert ISSUE_ID == "DEVEL-8642"
    assert result.ok
    assert result.issue_id == "DEVEL-8642"
