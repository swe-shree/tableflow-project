"""Column projection – keep only the requested columns."""

from typing import List


def select(data: List[dict], columns: List[str]) -> List[dict]:
    """
    Return *data* with only *columns* retained in each row.
    Missing columns are silently omitted.
    """
    return [{col: row[col] for col in columns if col in row} for row in data]
