# TableFlow

A lightweight in-memory table processing library for Python.

## Features

- **Search** – case-insensitive substring search across columns
- **Sort** – sort rows by any column, ascending or descending
- **Paginate** – slice data into pages
- **Select** – project specific columns
- **Aggregate** – sum, avg, min, max, count over a column
- **Chainable API** – operations return new `Table` instances

## Quick Start

```python
from tableflow import Table

data = [
    {"name": "Alice", "dept": "Engineering", "salary": 90000},
    {"name": "Bob",   "dept": "Marketing",   "salary": 72000},
    {"name": "Carol", "dept": "Engineering", "salary": 95000},
]

table = Table(data)

result = (
    table
    .search("engineering")
    .sort("salary", reverse=True)
    .select(["name", "salary"])
    .paginate(page=1, page_size=10)
)

print(result.rows)
```

## Install

```bash
pip install -e .
```

## Running Tests

```bash
python tests/test_table.py
```
