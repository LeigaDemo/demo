"""DEVEL-8561: Fix promo code stacking issue

Leiga Sprint 2608 · Developer Center
Type: Bug (bugfix)
Status at codegen: To Be Deploy
Assignee: Richard (R&D)
Epic: Digital Subscription - Membership Growth
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-8561].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8561"
ISSUE_NUMERIC_ID = 185586318
SUMMARY = '[NMG] Fix promo code stacking issue'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_fix_promo_code_stacking_issue(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8561.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8561] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Fix promo code stacking issue",
        metrics={
            "domain": DOMAIN,
            "priority": 'Medium',
            "estimate_point": 2,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_fix_promo_code_stacking_issue({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()

# leiga_plugins_refresh: DEVEL-8561 @ 2026-08-04T02:20Z
