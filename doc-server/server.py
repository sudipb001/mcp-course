from mcp.server.fastmcp import FastMCP
from docs import DOCUMENTS

mcp = FastMCP("Documentation Server")


@mcp.resource("docs://{page}")
def read_document(page: str):
    """Returns the requested documentation page, or a not-found message."""
    return DOCUMENTS.get(page, "Document not found.")


@mcp.tool()
def get_documentation(page: str) -> str:
    """Look up a documentation page by name (tools, resources, prompts, getting-started)."""
    return DOCUMENTS.get(page, "Document not found.")


@mcp.resource("company://welcome")
def welcome():
    return """
# Welcome
 
This is our company handbook.
 
## Contents
 
- Leave Policy
- Security
- Benefits
- Travel
"""


@mcp.resource("company://contact")
def company_contact():
    return {
        "company": "ABC Technologies",
        "email": "support@abc.com",
        "phone": "+91-9000000000",
    }


if __name__ == "__main__":
    mcp.run()
