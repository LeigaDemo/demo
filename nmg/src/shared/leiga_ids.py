"""Helpers for Leiga work-id formatting in git messages."""

from __future__ import annotations

import re

_DEVEL_RE = re.compile(r"DEVEL-\d+", re.I)


def bracket_id(issue_number: str) -> str:
    num = issue_number.strip().upper()
    if not num.startswith("DEVEL-"):
        raise ValueError(issue_number)
    return f"[{num}]"


def extract_ids(text: str) -> list[str]:
    return [m.group(0).upper() for m in _DEVEL_RE.finditer(text or "")]
