"""DEVEL-10538: Test Case Failed: [Demo] Create new Lead and Verify - Negative

Leiga Sprint 2610 · Developer Center
Type: Bug (bugfix)
Status at codegen: In Fix
Assignee: JING (Marketing)
Epic: —
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-10538].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-10538"
ISSUE_NUMERIC_ID = 207370174
SUMMARY = 'Test Case Failed: [Demo] Create new Lead and Verify - Negative'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_test_case_failed_demo_create_new_lead_an(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-10538.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-10538] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Test Case Failed: [Demo] Create new Lead and Verify - Negative",
        metrics={
            "domain": DOMAIN,
            "priority": 'Medium',
            "estimate_point": None,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_test_case_failed_demo_create_new_lead_an({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()
