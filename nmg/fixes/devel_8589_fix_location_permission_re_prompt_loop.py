"""DEVEL-8589: Fix location permission re-prompt loop

Leiga Sprint 2608 · Developer Center
Type: Bug (bugfix)
Status at codegen: In Fix
Assignee: Lucas (R&D)
Epic: Location-Based Service - Local Discovery
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-8589].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8589"
ISSUE_NUMERIC_ID = 185586545
SUMMARY = '[NMG] Fix location permission re-prompt loop'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_fix_location_permission_re_prompt_loop(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8589.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8589] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Fix location permission re-prompt loop",
        metrics={
            "domain": DOMAIN,
            "priority": 'Medium',
            "estimate_point": 2,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_fix_location_permission_re_prompt_loop({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()

# leiga_plugins_refresh: DEVEL-8589 @ 2026-08-04T02:20Z
