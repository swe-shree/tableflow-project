"""Sorting rows by a single column."""

from typing import List


def sort(data: List[dict], column: str, reverse: bool = False) -> List[dict]:
    """
    Return *data* sorted by *column*.  Rows missing the column are placed last.
    """
    missing = [row for row in data if column not in row]
    present = [row for row in data if column in row]
    sorted_rows = sorted(present, key=lambda r: r[column], reverse=reverse)
    return sorted_rows + missing
