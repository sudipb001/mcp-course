# Introduction to MCP

The Model Context Protocol (MCP) is a standard way to connect AI
models to external systems such as files, databases, and web
services.

An MCP server exposes **tools**, **resources**, and **prompts**
that an AI client — such as Claude Desktop — can use during a
conversation.

## Why MCP?

Before MCP, every integration between an AI model and an external
system had to be built from scratch, in a different way, for every
provider. MCP standardizes this connection so that:

- Servers can be reused across different AI clients.
- Clients can discover tools automatically, without custom code.
- Business logic stays separate from AI-specific plumbing.

## Core Building Blocks

- **Tools** — functions the AI model can call to take an action or
  fetch information (for example, running a calculation or querying
  a database).
- **Resources** — structured data the AI model can read without
  executing a tool.
- **Prompts** — reusable templates that guide how the AI model
  approaches a task.

This documentation set accompanies the "Building Practical MCP
Servers" tutorial, which builds five example servers: a calculator,
a file system server, a SQLite server, a REST API server, and this
documentation search server.
