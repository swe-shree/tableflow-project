"""Simple numeric aggregations over a single column."""

from typing import Any, List

_SUPPORTED = {"sum", "avg", "min", "max", "count"}


def aggregate(data: List[dict], column: str, func: str = "sum") -> Any:
    """
    Compute *func* over *column* values (non-numeric rows skipped).

    Supported: sum | avg | min | max | count
    """
    if func not in _SUPPORTED:
        raise ValueError(f"Unsupported aggregation '{func}'. Choose from {_SUPPORTED}.")

    values = []
    for row in data:
        val = row.get(column)
        try:
            values.append(float(val))
        except (TypeError, ValueError):
            pass

    if func == "count":
        return len(values)
    if not values:
        return None

    if func == "sum":
        return sum(values)
    if func == "avg":
        return sum(values) / len(values)
    if func == "min":
        return min(values)
    if func == "max":
        return max(values)
