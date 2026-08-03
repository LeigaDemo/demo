"""DEVEL-8588: Fix map tile loading on slow networks

Leiga Sprint 2608 · Developer Center
Type: Bug (bugfix)
Status at codegen: Done
Assignee: Evelyn (Dev)
Epic: Location-Based Service - Local Discovery
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-8588].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8588"
ISSUE_NUMERIC_ID = 185586532
SUMMARY = '[NMG] Fix map tile loading on slow networks'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_fix_map_tile_loading_on_slow_networks(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8588.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8588] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Fix map tile loading on slow networks",
        metrics={
            "domain": DOMAIN,
            "priority": 'High',
            "estimate_point": 2,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_fix_map_tile_loading_on_slow_networks({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()
