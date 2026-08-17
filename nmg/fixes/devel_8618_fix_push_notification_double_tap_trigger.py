"""DEVEL-8618: Fix push notification double-tap trigger

Leiga Sprint 2608 · Developer Center
Type: Bug (bugfix)
Status at codegen: Done
Assignee: Evelyn (Dev)
Epic: Mobile Apps - Reader Engagement
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-8618].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8618"
ISSUE_NUMERIC_ID = 185586748
SUMMARY = '[NMG] Fix push notification double-tap trigger'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_fix_push_notification_double_tap_trigger(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8618.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8618] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Fix push notification double-tap trigger",
        metrics={
            "domain": DOMAIN,
            "priority": 'Medium',
            "estimate_point": 1,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_fix_push_notification_double_tap_trigger({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()
