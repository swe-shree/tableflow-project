"""
Table - The core engine of TableFlow.
"""

from __future__ import annotations
from typing import Any, Callable, List, Optional
from tableflow.operations.search import search
from tableflow.operations.sort import sort
from tableflow.operations.paginate import paginate
from tableflow.operations.select import select
from tableflow.operations.aggregate import aggregate


class Table:
    """
    A lightweight in-memory table that supports search, sort,
    pagination, column selection, and aggregation.
    """

    def __init__(self, data: List[dict]):
        if not isinstance(data, list) or not all(isinstance(r, dict) for r in data):
            raise TypeError("data must be a list of dicts")
        self._data = data

    # ------------------------------------------------------------------ #
    #  Properties                                                          #
    # ------------------------------------------------------------------ #

    @property
    def rows(self) -> List[dict]:
        return list(self._data)

    @property
    def columns(self) -> List[str]:
        if not self._data:
            return []
        return list(self._data[0].keys())

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return f"Table(rows={len(self._data)}, columns={self.columns})"

    # ------------------------------------------------------------------ #
    #  Operations                                                          #
    # ------------------------------------------------------------------ #

    def search(self, query: str, columns: Optional[List[str]] = None) -> "Table":
        """Return a new Table with rows matching *query* (case-insensitive substring)."""
        return Table(search(self._data, query, columns))

    def sort(self, column: str, reverse: bool = False) -> "Table":
        """Return a new Table sorted by *column*."""
        return Table(sort(self._data, column, reverse))

    def paginate(self, page: int = 1, page_size: int = 10) -> "Table":
        """Return a new Table containing only the requested page of rows."""
        return Table(paginate(self._data, page, page_size))

    def select(self, columns: List[str]) -> "Table":
        """Return a new Table with only the specified columns."""
        return Table(select(self._data, columns))

    def aggregate(self, column: str, func: str = "sum") -> Any:
        """
        Compute an aggregate over *column*.

        func: 'sum' | 'avg' | 'min' | 'max' | 'count'
        """
        return aggregate(self._data, column, func)

    # ------------------------------------------------------------------ #
    #  Helpers                                                             #
    # ------------------------------------------------------------------ #

    def to_list(self) -> List[dict]:
        return list(self._data)

    @classmethod
    def from_list(cls, data: List[dict]) -> "Table":
        return cls(data)
