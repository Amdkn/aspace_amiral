# 🛠️ SKILL: MCP Mastery - A'Space OS Native Integration (V2.0)

## 🚩 Concept: Sovereign Tool Orchestration
This skill establishes the Model Context Protocol (MCP) as the "Universal Language" of A'Space OS. It replaces brittle Webhooks with a transparent, schema-validated tool ecosystem centered around the **n8n Gatekeeper (R1)**.

## 🏗️ Architecture: The Triptych MCP Bridge
A'Space OS uses a dual-role configuration for n8n:
1. **Server Mode**: n8n exposes its workflows as tools for Gemini/Antigravity.
2. **Client Mode**: n8n calls other MCP servers (Supabase, GitHub, local skills) as tools within workflows.

---

## 📡 Part 1: n8n Gatekeeper (Server Mode)
To expose workflows to Gemini/Antigravity:

### ⚙️ Infrastructure Setup
- **Version**: n8n v2.2.0+ required (Current: 2.3.5 stable).
- **Endpoint**: `http://localhost:5678/mcp/sse` (Standard SSE Transport).
- **Authentication**: `Bearer <N8N_MCP_ACCESS_TOKEN>` (Generated in n8n UI under Settings > Instance-level MCP).

### 📖 Workflow Eligibility Rules
For a workflow to appear as a tool:
1. **Published**: The workflow must be active (Production mode).
2. **Trigger**: Must contain a `Webhook`, `Schedule`, `Chat`, or `Form` trigger.
3. **MCP Flag**: Go to `Workflow Settings` (...) -> `Settings` -> Toggle `Available in MCP` to **ON**.
4. **Description**: The tool's name and schema are derived from the workflow's name and input trigger parameters.

### 🧪 Validation Protocol
`gemini mcp list` -> Check if the workflow name appears in the tools list.

---

## 🛰️ Part 2: n8n Conductor (Client Mode)
To allow n8n to control other parts of the OS:
- **Node**: Use the `MCP Client Tool` node.
- **Connection**: Connect it to an SSE or Stdio MCP server (e.g., a local Python MCP script).
- **Orchestration**: Create "Multi-Agent" workflows where n8n acts as the manager delegating specialized tasks to MCP servers.

---

## 📜 Standard Operating Procedures (SOP)

### 1. Discovery Loop (BMad)
- **Measure**: Check link status. `curl.exe -I http://localhost:5678/mcp/sse`.
- **Analyze**: If 404, check if "Instance-level MCP" is enabled in UI.
- **Decide**: If enabled but missing tool, check "Available in MCP" toggle in workflow settings.

### 2. Execution (Direct Mode)
- Use `gemini run "Execute the 'Pulse Auditor' workflow with data { ... }"`
- Do NOT use `run_command` with `curl` unless the MCP link is down (Fallback mode).

---

## ⚠️ Security Guardrails
- **Token Isolation**: The `N8N_MCP_ACCESS_TOKEN` must be stored ONLY in `.gemini/settings.json` or `.env`.
- **Public Exposure**: Never expose `5678` to the open web. Use local loopback or SSH tunneling.
- **Veto Logic**: Any MCP tool that writes to the `governance_state` must have a manual confirmation step (S1 Safety).
