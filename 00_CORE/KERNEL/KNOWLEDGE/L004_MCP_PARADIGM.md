# [[L004]] : The Death of the Webhook (MCP Shift)
- **Date**: 2026-01-15
- **Pattern**: Traditional REST/Webhook integrations are opaque, hard to debug (encoding issues, route mismatches), and require managing endpoints.
- **Principle**: MCP (Model Context Protocol) is the "Sovereign Bridge". It allows direct tool-calling without the overhead of HTTP route registration.
- **Manager Guideline**: 
    1. Prefer `mcp-server-n8n` or native n8n MCP tools over Webhook triggers.
    2. Shift from "Pushing Data" (Webhook) to "Executing Capability" (MCP Tool).
    3. Use the `n8n-gatekeeper` MCP server to orchestrate R1 workflows directly from the Kernel.
