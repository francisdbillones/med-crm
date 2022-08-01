from __future__ import annotations


def all_is_digit(s: str) -> bool:
    return all(c.isdigit() for c in s)
