"""Demo / manual testing entry point for TableFlow."""

from tableflow import Table
from tableflow.utils import pretty_print, total_pages

EMPLOYEES = [
    {"id": 1, "name": "Alice",   "dept": "Engineering", "salary": 90000},
    {"id": 2, "name": "Bob",     "dept": "Marketing",   "salary": 72000},
    {"id": 3, "name": "Carol",   "dept": "Engineering", "salary": 95000},
    {"id": 4, "name": "Dave",    "dept": "HR",          "salary": 60000},
    {"id": 5, "name": "Eve",     "dept": "Marketing",   "salary": 78000},
    {"id": 6, "name": "Frank",   "dept": "Engineering", "salary": 85000},
    {"id": 7, "name": "Grace",   "dept": "HR",          "salary": 63000},
]


def main():
    table = Table(EMPLOYEES)

    print("=== All rows ===")
    pretty_print(table.rows)

    print("\n=== Search: 'engineering' ===")
    pretty_print(table.search("engineering").rows)

    print("\n=== Sorted by salary (desc) ===")
    pretty_print(table.sort("salary", reverse=True).rows)

    print("\n=== Page 1 (page_size=3) ===")
    page = table.paginate(page=1, page_size=3)
    pretty_print(page.rows)
    print(f"Total pages: {total_pages(len(table), 3)}")

    print("\n=== Select [name, dept] ===")
    pretty_print(table.select(["name", "dept"]).rows)

    print("\n=== Aggregations on salary ===")
    for func in ("sum", "avg", "min", "max", "count"):
        print(f"  {func:6s}: {table.aggregate('salary', func)}")

    print("\n=== Chained: Engineering, sorted by salary desc, name+salary only ===")
    result = (
        table
        .search("engineering")
        .sort("salary", reverse=True)
        .select(["name", "salary"])
    )
    pretty_print(result.rows)


if __name__ == "__main__":
    main()
