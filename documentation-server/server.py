"""
server.py

The MCP layer for the Documentation Search Server. Exposes a
single tool for keyword-searching the local docs/ folder.
"""

from mcp.server.fastmcp import FastMCP

from search import search_documents

mcp = FastMCP("Documentation Server")


@mcp.tool()
def search_docs(keyword: str):
    """Search all documentation for a keyword."""
    return search_documents(keyword)


if __name__ == "__main__":
    mcp.run()
