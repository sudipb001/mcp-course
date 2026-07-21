# server.py
from mcp.server.fastmcp import FastMCP
from resources.hr import HR_DATA
from prompts.hr_prompts import build_explain_policy_prompt
from tools.leave_tools import apply_leave
 
mcp = FastMCP("Company Assistant Server")
 
 
# --- Resource: read-only information ---
@mcp.resource("company://hr/{topic}")
def hr_resource(topic: str):
    """Returns HR information for the requested topic."""
    return HR_DATA.get(topic, "Topic not found.")
 
 
# --- Prompt: reusable instruction template ---
@mcp.prompt()
def explain_policy(topic: str) -> str:
    """Creates an instruction asking the AI to explain a policy simply."""
    return build_explain_policy_prompt(topic)
 
 
# --- Tool: performs an action ---
@mcp.tool()
def apply_for_leave(start_date: str, days: int) -> str:
    """Submits a leave request for the given start date and number of days."""
    return apply_leave(start_date, days)
 
 
if __name__ == "__main__":
    mcp.run()
