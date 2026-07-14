"""
calculator.py

Pure business logic for the Calculator MCP Server.

Nothing in this file is MCP-specific. These are ordinary Python
functions that could be reused in a Flask app, a CLI tool, a
Django app, or unit tests without any modification.
"""


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def multiply(a: int, b: int) -> int:
    return a * b


def divide(a: int, b: int) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
