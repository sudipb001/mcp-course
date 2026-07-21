from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("Company Prompt Server")


@mcp.prompt()
def review_code(code: str, language: str = "python", strictness: str = "normal") -> str:
    """Creates a code review instruction, customized by language and strictness."""
    return f"""You are reviewing {language} code with {strictness} strictness.
 
Check for:
- Correctness
- Security issues
- Readability
- Idiomatic {language} style
 
Code:
{code}
"""


@mcp.prompt()
def summarize_meeting(transcript: str, focus_area: str = "action items") -> str:
    """Creates an instruction to summarize a meeting transcript."""
    return f"""Summarize the following meeting transcript.
 
Focus specifically on: {focus_area}
 
Transcript:
{transcript}
"""


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    """Starts a guided debugging conversation for the given error."""
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]


if __name__ == "__main__":
    mcp.run()
