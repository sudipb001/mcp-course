def build_explain_policy_prompt(topic: str) -> str:
    """Builds an instruction asking the AI to explain a company policy simply."""
    return f"""Explain the company's {topic} policy in simple,
friendly language suitable for a new employee.
"""
