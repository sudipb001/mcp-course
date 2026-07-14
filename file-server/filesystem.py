"""
filesystem.py

Pure business logic for the File System MCP Server.

For safety, every operation is restricted to the local
"workspace" folder rather than the whole file system. This
follows the "Making File Operations Safer" guidance from the
tutorial: an AI assistant should never be able to read or write
arbitrary files on the host machine.
"""

from pathlib import Path

WORKSPACE = Path(__file__).parent / "workspace"
WORKSPACE.mkdir(exist_ok=True)


def _resolve(path: str) -> Path:
    """Resolve a user-supplied path safely inside the workspace."""
    target = (WORKSPACE / path).resolve()
    if not str(target).startswith(str(WORKSPACE.resolve())):
        raise PermissionError("Access outside the workspace is not allowed.")
    return target


def read_file(path: str) -> str:
    try:
        return _resolve(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return "The requested file was not found."
    except PermissionError as error:
        return f"Permission error: {error}"


def write_file(path: str, content: str) -> str:
    try:
        target = _resolve(path)
        target.write_text(content, encoding="utf-8")
        return "File written successfully."
    except PermissionError as error:
        return f"Permission error: {error}"


def list_files(directory: str = ".") -> list:
    try:
        folder = _resolve(directory)
        return [file.name for file in folder.iterdir()]
    except FileNotFoundError:
        return []
    except PermissionError as error:
        return [f"Permission error: {error}"]
