def build_code_review_prompt(code: str, language: str = "python", strictness: str = "normal") -> str:
    return f"""You are reviewing {language} code with {strictness} strictness.
 
Check for:
- Correctness
- Security issues
- Readability
- Idiomatic {language} style
 
Code:
{code}
"""
 
 
def build_meeting_summary_prompt(transcript: str, focus_area: str = "action items") -> str:
    return f"""Summarize the following meeting transcript.
 
Focus specifically on: {focus_area}
 
Transcript:
{transcript}
"""
 
 
def build_risk_analysis_prompt(proposal: str) -> str:
    return f"""Analyze the following proposal for risk.
 
Identify:
- Financial risk
- Operational risk
- Reputational risk
 
Provide a short mitigation plan for each risk identified.
 
Proposal:
{proposal}
"""
