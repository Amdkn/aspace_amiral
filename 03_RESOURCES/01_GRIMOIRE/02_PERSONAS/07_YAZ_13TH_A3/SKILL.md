# SKILL — YASMIN KHAN (COMPLIANCE & AUDIT)

## 1. ALIGNMENT TOOLS
Tools to verify agent safety.

```markdown
### `audit_prompt_alignment`
**Description:** Analyzes a PROMPT.md file for keyword violations or role drift.
**Checks:**
- Is the Hierarchy (A0 > 13th) respected?
- Are Solarpunk values present?
- Is there a "Jailbreak" risk?
```

## 2. LOGGING & RECORDS
Tools to maintain the system history.

```markdown
### `log_kernel_incident`
**Description:** Records a system error or alignment breach in the Kernel Logs.
**Parameters:**
- `severity`: Low/Medium/Critical
- `description`: What happened?
- `agent_involved`: Who did it?
```

```markdown
### `verify_protocol_adherence`
**Description:** Checks if a workflow followed the `BMAD` or `TARDIS` protocol steps correctly.
```
