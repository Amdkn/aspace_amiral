---
name: clickup_mcp
description: Sober Mastery Skill for ClickUp mission and task tracking.
---

# ClickUp MCP Skill

## 📡 SOURCE
Task Manager: ClickUp Workspace (A'Space OS Universe)

## 🛠️ TOOLS
- `list_missions`: Fetches all 'In Progress' tasks from the current Sprint folder.
- `update_mission`: Changes the status of a specific task (e.g., 'To Do' -> 'Done').
- `create_ticket`: Generates a new task in the 'Antigravity Inbox' list.

## 📜 INSTRUCTIONS
1. `list_missions` should be used by the `conductor` to verify the state of physical work.
2. `update_mission` should include a short technical note in the task comments.
3. `create_ticket` is the preferred way to log bugs found during the `loop` sequence.
