"""DEVEL-8559: Fix membership badge not updating

Leiga Sprint 2608 · Developer Center
Type: Bug (bugfix)
Status at codegen: Done
Assignee: Evelyn (Dev)
Epic: Digital Subscription - Membership Growth
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-8559].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8559"
ISSUE_NUMERIC_ID = 185586297
SUMMARY = '[NMG] Fix membership badge not updating'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_fix_membership_badge_not_updating(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8559.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8559] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Fix membership badge not updating",
        metrics={
            "domain": DOMAIN,
            "priority": 'Medium',
            "estimate_point": 2,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_fix_membership_badge_not_updating({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()

# leiga_plugins_refresh: DEVEL-8559 @ 2026-08-04T02:20Z
