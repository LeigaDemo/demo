"""DEVEL-8567: Walking direction with AR overlay

Leiga Sprint 2608 · Developer Center
Type: Story (feature)
Status at codegen: In Product Design
Assignee: Lucas (R&D)
Epic: Location-Based Service - Local Discovery
Domain: location

Synced to Leiga via commit/PR messages containing [DEVEL-8567].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8567"
ISSUE_NUMERIC_ID = 185586373
SUMMARY = '[NMG] Walking direction with AR overlay'
DOMAIN = 'location'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def implement_walking_direction_with_ar_overlay(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8567.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8567] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied feature stub for Walking direction with AR overlay",
        metrics={
            "domain": DOMAIN,
            "priority": 'High',
            "estimate_point": 5,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = implement_walking_direction_with_ar_overlay({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()

# leiga_plugins_refresh: DEVEL-8567 @ 2026-08-04T02:20Z
