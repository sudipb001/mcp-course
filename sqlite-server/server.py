"""
server.py

The MCP layer for the SQLite Server. Exposes tools for listing,
searching, and inserting customer records.
"""

from mcp.server.fastmcp import FastMCP

from database import (
    get_all_customers,
    get_customers_by_city,
    add_customer,
)

mcp = FastMCP("SQLite Server")


@mcp.tool()
def list_customers():
    """Return all customers."""
    return get_all_customers()


@mcp.tool()
def find_customers(city: str):
    """Find customers belonging to a city."""
    return get_customers_by_city(city)


@mcp.tool()
def create_customer(name: str, city: str):
    """Create a new customer."""
    return add_customer(name, city)


if __name__ == "__main__":
    mcp.run()
