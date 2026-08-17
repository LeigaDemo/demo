"""DEVEL-8707: Public transport arrival time with MTR API integration

Leiga Sprint 2608 · Developer Center
Type: Story (feature)
Status at codegen: To Do
Assignee: Richard (R&D)
Epic: Location-Based Service - Local Discovery
Domain: location

Synced to Leiga via commit/PR messages containing [DEVEL-8707].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8707"
ISSUE_NUMERIC_ID = 185587374
SUMMARY = '[NMG] Public transport arrival time with MTR API integration'
DOMAIN = 'location'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def implement_public_transport_arrival_time_with_mtr_a(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8707.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8707] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied feature stub for Public transport arrival time with MTR API integration",
        metrics={
            "domain": DOMAIN,
            "priority": 'Medium',
            "estimate_point": 3,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = implement_public_transport_arrival_time_with_mtr_a({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()
