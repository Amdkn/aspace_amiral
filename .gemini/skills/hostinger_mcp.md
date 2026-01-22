---
name: hostinger_mcp
description: Sober Mastery Skill for Hostinger VPS & Coolify management.
---

# Hostinger MCP Skill

## 📡 SOURCE
Infrastructure: Hostinger Global VPS
Control Layer: Coolify / SSH

## 🛠️ TOOLS
- `vps_pulse`: Checks the CPU, RAM, and Disk usage of the primary Hostinger VPS.
- `coolify_deploy`: Triggers a deployment for a specific service ID in the Coolify panel.
- `ssh_exec`: Executes a safe, non-destructive command on the R1 server via SSH.

## 📜 INSTRUCTIONS
1. Use `vps_pulse` daily to ensure the R1 environment is not under heavy load.
2. `ssh_exec` must only be used for read-only operations (e.g., `docker ps`, `ls -la`) unless a specific "Correction" track is active.
3. Validate all service IDs before running `coolify_deploy`.
