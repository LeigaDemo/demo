"""DEVEL-8560: Fix corporate seat invite email

Leiga Sprint 2608 · Developer Center
Type: Bug (bugfix)
Status at codegen: Not Started
Assignee: JING (Marketing)
Epic: Digital Subscription - Membership Growth
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-8560].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8560"
ISSUE_NUMERIC_ID = 185586307
SUMMARY = '[NMG] Fix corporate seat invite email'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_fix_corporate_seat_invite_email(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8560.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8560] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Fix corporate seat invite email",
        metrics={
            "domain": DOMAIN,
            "priority": 'Low',
            "estimate_point": 1,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_fix_corporate_seat_invite_email({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()

# leiga_plugins_refresh: DEVEL-8560 @ 2026-08-04T02:20Z
