"""DEVEL-8211: Location-aware dining and shopping offers

Leiga Sprint 2608 · Developer Center
Type: Story (feature)
Status at codegen: To By Deploy
Assignee: Lucas (R&D)
Epic: Location-Based Service - Local Discovery
Domain: location

Synced to Leiga via commit/PR messages containing [DEVEL-8211].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8211"
ISSUE_NUMERIC_ID = 181704205
SUMMARY = '[NMG] Location-aware dining and shopping offers'
DOMAIN = 'location'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def implement_location_aware_dining_and_shopping_offer(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8211.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8211] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied feature stub for Location-aware dining and shopping offers",
        metrics={
            "domain": DOMAIN,
            "priority": 'High',
            "estimate_point": 5,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = implement_location_aware_dining_and_shopping_offer({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()
