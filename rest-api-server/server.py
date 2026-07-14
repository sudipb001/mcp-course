"""
server.py

The MCP layer for the REST API Server. Exposes tools that call
an external web service (JSONPlaceholder) over HTTP.
"""

from mcp.server.fastmcp import FastMCP
from api import get_posts, get_post

mcp = FastMCP("REST API Server")


@mcp.tool()
def list_posts():
    """Retrieve all posts."""
    return get_posts()


@mcp.tool()
def get_post_by_id(post_id: int):
    """Retrieve a single post by its ID."""
    return get_post(post_id)


if __name__ == "__main__":
    mcp.run()
