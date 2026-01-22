---
name: airtable_mcp
description: Sober Mastery Skill for Airtable KPI and habit tracking.
---

# Airtable MCP Skill

## 📡 SOURCE
Data Hub: Airtable Base (OS Metrics & Habits)

## 🛠️ TOOLS
- `log_kpi`: Records a numeric value into the 'System Metrics' table (e.g., focus minutes, lines of code).
- `fetch_habits`: Retrieves the habit compliance status for the current week.
- `update_inventory`: Modifies the stock or status of a physical resource in the 'Logistics' table.

## 📜 INSTRUCTIONS
1. `log_kpi` is the primary tool for the `loop` command to report success metrics.
2. `fetch_habits` provides context for the 11th Doctor's Vitality Dashboard.
3. Ensure the `AIRTABLE_BASE_ID` and `AIRTABLE_API_KEY` are configured.
