"""DEVEL-10916: 2611 lbs: Manual location when GPS is denied

Leiga Sprint 2611 · Developer Center
Type: Story (feature)
Status at codegen: In Product Design
Assignee: Saddie (HB)
Epic: Location-Based Service - Local Discovery
Domain: location

Synced to Leiga via commit/PR messages containing [DEVEL-10916].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-10916"
ISSUE_NUMERIC_ID = 211642727
SUMMARY = '[NMG] 2611 lbs: Manual location when GPS is denied'
DOMAIN = 'location'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def implement_2611_lbs_manual_location_when_gps_is_den(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-10916.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-10916] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied feature stub for 2611 lbs: Manual location when GPS is denied",
        metrics={
            "domain": DOMAIN,
            "priority": 'Highest',
            "estimate_point": 3,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = implement_2611_lbs_manual_location_when_gps_is_den({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()
