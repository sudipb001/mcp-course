"""
search.py

Pure business logic for the Documentation Search MCP Server.

Performs a simple case-insensitive keyword search across every
Markdown file in the docs/ folder. This is intentionally simple —
real systems would add fuzzy matching, ranking, or embeddings —
but the MCP architecture around it stays the same.
"""

from pathlib import Path

DOCS_FOLDER = Path(__file__).parent / "docs"


def search_documents(keyword: str):
    results = []
    for file in DOCS_FOLDER.glob("*.md"):
        content = file.read_text(encoding="utf-8")
        if keyword.lower() in content.lower():
            results.append(file.name)
    return results
