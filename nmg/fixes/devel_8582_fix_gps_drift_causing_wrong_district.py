"""DEVEL-8582: Fix GPS drift causing wrong district

Leiga Sprint 2608 · Developer Center
Type: Bug (bugfix)
Status at codegen: Done
Assignee: Richard (R&D)
Epic: Location-Based Service - Local Discovery
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-8582].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8582"
ISSUE_NUMERIC_ID = 185586477
SUMMARY = '[NMG] Fix GPS drift causing wrong district'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_fix_gps_drift_causing_wrong_district(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8582.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8582] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Fix GPS drift causing wrong district",
        metrics={
            "domain": DOMAIN,
            "priority": 'High',
            "estimate_point": 3,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_fix_gps_drift_causing_wrong_district({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()
