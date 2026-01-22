---
name: supabase_mcp
description: Sober Mastery Skill for Supabase persistence and audit.
---

# Supabase MCP Skill

## 📡 SOURCE
Database: Supabase PostgreSQL (Managed)

## 🛠️ TOOLS
- `audit_query`: Retrieves the last 10 log entries from the `system_audit` table.
- `pulse_write`: Writes a new health record to the `telemetry_pulse` table.
- `fetch_directive`: Retrieves the current active governance directive for the 12th Doctor.

## 📜 INSTRUCTIONS
1. Always use `audit_query` before making significant database migrations.
2. `pulse_write` should be triggered automatically by the `loop` command every 3 hours.
3. Ensure the `SUPABASE_KEY` is present in the `.env` before calling these tools.
