from mcp.server.fastmcp import FastMCP
from prompts import (
    build_code_review_prompt,
    build_meeting_summary_prompt,
    build_risk_analysis_prompt,
)

mcp = FastMCP("Team Prompt Server")


@mcp.prompt()
def review_code(code: str, language: str = "python", strictness: str = "normal") -> str:
    """Creates a code review instruction."""
    return build_code_review_prompt(code, language, strictness)


@mcp.prompt()
def summarize_meeting(transcript: str, focus_area: str = "action items") -> str:
    """Creates a meeting summary instruction."""
    return build_meeting_summary_prompt(transcript, focus_area)


@mcp.prompt()
def analyze_risk(proposal: str) -> str:
    """Creates a risk analysis instruction."""
    return build_risk_analysis_prompt(proposal)


if __name__ == "__main__":
    mcp.run()
