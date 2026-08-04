"""DEVEL-8621: Fix broken deep link to saved articles

Leiga Sprint 2608 · Developer Center
Type: Bug (bugfix)
Status at codegen: Done
Assignee: Mia (OS)
Epic: Mobile Apps - Reader Engagement
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-8621].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8621"
ISSUE_NUMERIC_ID = 185586784
SUMMARY = '[NMG] Fix broken deep link to saved articles'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_fix_broken_deep_link_to_saved_articles(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8621.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8621] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Fix broken deep link to saved articles",
        metrics={
            "domain": DOMAIN,
            "priority": 'Medium',
            "estimate_point": 1,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_fix_broken_deep_link_to_saved_articles({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()

# leiga_plugins_refresh: DEVEL-8621 @ 2026-08-04T02:20Z
