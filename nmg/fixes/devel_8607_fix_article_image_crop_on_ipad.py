"""DEVEL-8607: Fix article image crop on iPad

Leiga Sprint 2608 · Developer Center
Type: Bug (bugfix)
Status at codegen: To Be Deploy
Assignee: Evelyn (Dev)
Epic: Mobile Apps - Reader Engagement
Domain: fixes

Synced to Leiga via commit/PR messages containing [DEVEL-8607].
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

ISSUE_ID = "DEVEL-8607"
ISSUE_NUMERIC_ID = 185586669
SUMMARY = '[NMG] Fix article image crop on iPad'
DOMAIN = 'fixes'


@dataclass
class WorkResult:
    issue_id: str
    ok: bool
    detail: str
    metrics: dict[str, Any]


def fix_fix_article_image_crop_on_ipad(payload: dict[str, Any] | None = None) -> WorkResult:
    """Stub implementation for DEVEL-8607.

    Real product code would live in the NMG apps; this module exists so
    GitHub history for [DEVEL-8607] is visible inside Leiga Plug-ins.
    """
    payload = payload or {}
    return WorkResult(
        issue_id=ISSUE_ID,
        ok=True,
        detail="Applied bugfix stub for Fix article image crop on iPad",
        metrics={
            "domain": DOMAIN,
            "priority": 'Medium',
            "estimate_point": 2,
            "input_keys": sorted(payload.keys()),
        },
    )


def smoke() -> None:
    result = fix_fix_article_image_crop_on_ipad({"source": "leiga-github-sync"})
    assert result.ok, result
    assert result.issue_id == ISSUE_ID
    print(f"{ISSUE_ID} smoke ok · {result.detail}")


if __name__ == "__main__":
    smoke()
