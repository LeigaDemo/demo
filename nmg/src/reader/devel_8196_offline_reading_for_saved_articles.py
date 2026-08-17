"""DEVEL-8196: Offline reading for saved articles

Leiga Sprint 2608 · Developer Center
Type: Story (feature)
Status at codegen: To Do
Assignee: Evelyn (Dev)
Epic: Mobile Apps - Reader Engagement
Domain: reader

Synced to Leiga via commit/PR messages containing [DEVEL-8196].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8196"
ISSUE_NUMERIC_ID = 181704024
SUMMARY = '[NMG] Offline reading for saved articles'
DOMAIN = 'reader'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def implement_offline_reading_for_saved_articles(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8196.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8196] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied feature stub for Offline reading for saved articles",
        metrics={
            "domain": DOMAIN,
            "priority": 'Medium',
            "estimate_point": 5,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = implement_offline_reading_for_saved_articles({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()
