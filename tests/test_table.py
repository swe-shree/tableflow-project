"""Basic tests for TableFlow."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from tableflow import Table

SAMPLE = [
    {"id": 1, "name": "Alice",   "dept": "Engineering", "salary": 90000},
    {"id": 2, "name": "Bob",     "dept": "Marketing",   "salary": 72000},
    {"id": 3, "name": "Carol",   "dept": "Engineering", "salary": 95000},
    {"id": 4, "name": "Dave",    "dept": "HR",          "salary": 60000},
    {"id": 5, "name": "Eve",     "dept": "Marketing",   "salary": 78000},
]


def test_search():
    t = Table(SAMPLE)
    result = t.search("engineering")
    assert len(result) == 2, f"Expected 2, got {len(result)}"
    print("  search        ✓")


def test_sort():
    t = Table(SAMPLE)
    result = t.sort("salary", reverse=True)
    assert result.rows[0]["name"] == "Carol", "Highest salary should be Carol"
    print("  sort          ✓")


def test_paginate():
    t = Table(SAMPLE)
    page1 = t.paginate(page=1, page_size=2)
    page2 = t.paginate(page=2, page_size=2)
    assert len(page1) == 2
    assert len(page2) == 2
    assert page1.rows[0]["id"] != page2.rows[0]["id"]
    print("  paginate      ✓")


def test_select():
    t = Table(SAMPLE)
    result = t.select(["name", "dept"])
    assert list(result.rows[0].keys()) == ["name", "dept"]
    print("  select        ✓")


def test_aggregate():
    t = Table(SAMPLE)
    assert t.aggregate("salary", "sum") == 395000
    assert t.aggregate("salary", "count") == 5
    assert t.aggregate("salary", "min") == 60000
    assert t.aggregate("salary", "max") == 95000
    print("  aggregate     ✓")


def test_chaining():
    t = Table(SAMPLE)
    result = (
        t.search("engineering")
         .sort("salary", reverse=True)
         .select(["name", "salary"])
    )
    assert len(result) == 2
    assert result.rows[0]["name"] == "Carol"
    print("  chaining      ✓")


if __name__ == "__main__":
    print("Running TableFlow tests...\n")
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            fn()
    print("\nAll tests passed!")
