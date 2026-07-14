# MCP Transport Layers

MCP servers communicate with clients over a **transport**. The
transport is responsible for moving messages back and forth; it
does not know anything about tools, resources, or prompts.

## STDIO Transport

The most common transport for local development is **STDIO**
(standard input/output). When Claude Desktop launches your server
as a subprocess, it talks to it by writing to the server's stdin
and reading from its stdout.

This is the transport used by every server built in this tutorial:

```python
if __name__ == "__main__":
    mcp.run()
```

Calling `mcp.run()` with no arguments starts the server on STDIO
by default.

## HTTP / SSE Transport

For servers that run remotely — for example, a company-wide MCP
server shared by an entire team — MCP also supports HTTP-based
transports, including Server-Sent Events (SSE) and streamable HTTP.
These allow a single running server process to be reached over the
network by multiple clients at once, instead of being started fresh
as a subprocess for each user.

## Choosing a Transport

| Scenario | Recommended Transport |
| --- | --- |
| Local desktop tool, single user | STDIO |
| Shared team or enterprise server | HTTP / SSE |
| Server embedded in another app | STDIO or in-process |

Regardless of transport, the tools you register with `@mcp.tool()`
do not need to change. The transport is purely a communication
detail handled by FastMCP.
