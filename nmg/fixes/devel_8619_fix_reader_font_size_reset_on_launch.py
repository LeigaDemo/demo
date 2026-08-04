"""DEVEL-8619: Fix reader font size reset on launch

Leiga Sprint 2608 · Developer Center
Type: Bug (bugfix)
Status at codegen: Not Started
Assignee: Lucas (R&D)
Epic: Mobile Apps - Reader Engagement
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-8619].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8619"
ISSUE_NUMERIC_ID = 185586761
SUMMARY = '[NMG] Fix reader font size reset on launch'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_fix_reader_font_size_reset_on_launch(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8619.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8619] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Fix reader font size reset on launch",
        metrics={
            "domain": DOMAIN,
            "priority": 'Low',
            "estimate_point": 2,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_fix_reader_font_size_reset_on_launch({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()

# leiga_plugins_refresh: DEVEL-8619 @ 2026-08-04T02:20Z
