"""Slice a list of rows into pages."""

from typing import List


def paginate(data: List[dict], page: int = 1, page_size: int = 10) -> List[dict]:
    """
    Return the slice of *data* that corresponds to the requested 1-indexed *page*.
    """
    if page < 1:
        raise ValueError(f"page must be >= 1, got {page}")
    if page_size < 1:
        raise ValueError(f"page_size must be >= 1, got {page_size}")

    start = (page - 1) * page_size
    end = start + page_size
    return data[start:end]
