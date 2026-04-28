"""Case-insensitive substring search across one or more columns."""

from typing import List, Optional


def search(data: List[dict], query: str, columns: Optional[List[str]] = None) -> List[dict]:
    """
    Return rows where *query* appears (case-insensitive) in any of the
    given *columns* (defaults to all columns).
    """
    if not query:
        return list(data)

    q = query.lower()

    def row_matches(row: dict) -> bool:
        cols = columns if columns else list(row.keys())
        return any(q in str(row.get(col, "")).lower() for col in cols)

    return [row for row in data if row_matches(row)]
