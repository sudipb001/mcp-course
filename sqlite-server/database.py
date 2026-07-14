"""
database.py

Pure business logic for the SQLite MCP Server.

All SQL lives in this one module. Every query uses parameterized
placeholders (?) rather than string concatenation, to avoid SQL
injection.
"""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "company.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def _row_to_dict(row) -> dict:
    return {"id": row[0], "name": row[1], "city": row[2]}


def get_all_customers():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, city FROM customers")
        rows = cursor.fetchall()
        connection.close()
        return [_row_to_dict(row) for row in rows]
    except sqlite3.Error as error:
        return f"Database error: {error}"


def get_customers_by_city(city: str):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            SELECT id, name, city
            FROM customers
            WHERE city = ?
            """,
            (city,),
        )
        rows = cursor.fetchall()
        connection.close()
        return [_row_to_dict(row) for row in rows]
    except sqlite3.Error as error:
        return f"Database error: {error}"


def add_customer(name: str, city: str):
    if not name or not city:
        return "Both name and city are required."
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO customers (name, city)
            VALUES (?, ?)
            """,
            (name, city),
        )
        connection.commit()
        connection.close()
        return "Customer added successfully."
    except sqlite3.Error as error:
        return f"Database error: {error}"
