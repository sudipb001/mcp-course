"""
server.py

The MCP layer for the Calculator Server.

This file stays thin: its only responsibility is exposing the
functions in calculator.py as MCP tools. All real business logic
lives in calculator.py.
"""

from mcp.server.fastmcp import FastMCP

from calculator import (
    add,
    subtract,
    multiply,
    divide,
)

mcp = FastMCP("Calculator Server")


@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    """Add two integers."""
    return add(a, b)


@mcp.tool()
def subtract_numbers(a: int, b: int) -> int:
    """Subtract the second integer from the first."""
    return subtract(a, b)


@mcp.tool()
def multiply_numbers(a: int, b: int) -> int:
    """Multiply two integers."""
    return multiply(a, b)


@mcp.tool()
def divide_numbers(a: int, b: int) -> float:
    """Divide one number by another."""
    try:
        return divide(a, b)
    except ValueError as error:
        return f"Error: {error}"


if __name__ == "__main__":
    mcp.run()
