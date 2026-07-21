from mcp.server.fastmcp import FastMCP
 
# Create the MCP server instance. The name shown here is what
# Claude Desktop will display when it lists connected servers.
mcp = FastMCP("Company Resource Server")
 
 
@mcp.resource("company://policies/leave")
def leave_policy():
    """Returns the company's leave policy as plain text."""
    return """
Company Leave Policy
 
Casual Leave : 12 Days
Sick Leave   : 10 Days
Earned Leave : 15 Days
"""
 
 
if __name__ == "__main__":
    mcp.run()
