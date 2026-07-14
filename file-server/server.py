"""
server.py

The MCP layer for the File System Server. Exposes read, write,
and list operations, all scoped to the local workspace/ folder.
"""

from mcp.server.fastmcp import FastMCP

from filesystem import (
    read_file,
    write_file,
    list_files,
)

mcp = FastMCP("File Server")


@mcp.tool()
def read_text_file(path: str):
    """Read a text file from the workspace."""
    return read_file(path)


@mcp.tool()
def write_text_file(path: str, content: str):
    """Write text to a file in the workspace."""
    return write_file(path, content)


@mcp.tool()
def list_directory(directory: str = "."):
    """List all files in a workspace directory."""
    return list_files(directory)


if __name__ == "__main__":
    mcp.run()
