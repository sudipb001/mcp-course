from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Calculator")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract the second integer from the first."""
    return a - b


if __name__ == "__main__":
    mcp.run()
