import sqlite3
from typing import Optional

from config.settings import settings
from models.customer import Customer


class CustomerRepository:
    """Reads and writes customer records in SQLite."""

    def __init__(self, db_name: Optional[str] = None):
        self.db_name = db_name or settings.DATABASE_NAME
        self._create_table()

    def _get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_name)

    def _create_table(self) -> None:
        with self._get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    customer_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    city TEXT NOT NULL
                )
                """)

    def get_by_id(self, customer_id: int) -> Optional[Customer]:
        with self._get_connection() as conn:
            row = conn.execute(
                "SELECT customer_id, name, city FROM customers WHERE customer_id = ?",
                (customer_id,),
            ).fetchone()

        if row is None:
            return None

        return Customer(customer_id=row[0], name=row[1], city=row[2])

    def add(self, customer: Customer) -> None:
        with self._get_connection() as conn:
            conn.execute(
                "INSERT INTO customers (customer_id, name, city) VALUES (?, ?, ?)",
                (customer.customer_id, customer.name, customer.city),
            )
