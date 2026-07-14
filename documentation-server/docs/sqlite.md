# Using SQLite with MCP

SQLite is a lightweight, serverless, embedded database that ships
with Python's standard library. It's an ideal choice for demos and
small applications because it requires no separate database server
to install or configure.

## The customers Table

The SQLite Server project in this tutorial uses a demo database
named `company.db`, containing a single `customers` table:

| Column | Type | Description |
| --- | --- | --- |
| id | INTEGER | Primary key, auto-incremented |
| name | TEXT | Customer's full name |
| city | TEXT | Customer's city |

## Parameterized Queries

Always use `?` placeholders instead of building SQL strings with
f-strings or concatenation:

```python
cursor.execute(
    "SELECT id, name, city FROM customers WHERE city = ?",
    (city,)
)
```

This protects the database server against SQL injection attacks,
where malicious input is crafted to alter the meaning of a query.

## Closing Connections

Every connection opened with `sqlite3.connect()` should eventually
be closed with `connection.close()`. Leaving connections open
wastes resources and can eventually lock the database file.

## From SQLite to Production Databases

The same tool-calling pattern used for SQLite — open a connection,
run a parameterized query, return structured data, close the
connection — applies almost unchanged to PostgreSQL, MySQL, SQL
Server, and other production databases, once you swap in the
appropriate driver.
