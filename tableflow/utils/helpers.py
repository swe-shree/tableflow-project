"""Miscellaneous helper utilities."""

from typing import List
import math


def pretty_print(data: List[dict], max_col_width: int = 20) -> None:
    """Print *data* as a formatted ASCII table."""
    if not data:
        print("(empty table)")
        return

    columns = list(data[0].keys())
    widths = {col: min(max_col_width, max(len(col), *(len(str(row.get(col, ""))) for row in data)))
              for col in columns}

    def fmt_row(row: dict) -> str:
        return " | ".join(str(row.get(col, ""))[:widths[col]].ljust(widths[col]) for col in columns)

    header = " | ".join(col.ljust(widths[col]) for col in columns)
    separator = "-+-".join("-" * widths[col] for col in columns)

    print(header)
    print(separator)
    for row in data:
        print(fmt_row(row))


def total_pages(total_rows: int, page_size: int) -> int:
    """Return the number of pages needed to display *total_rows* at *page_size* rows per page."""
    if page_size < 1:
        raise ValueError("page_size must be >= 1")
    return math.ceil(total_rows / page_size)
