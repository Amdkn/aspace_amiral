# SKILL — RYAN SINCLAIR (BUILD & DEPLOY)

## 1. AGENT CONSTRUCTION
The core tools for building the Rick's Verse hierarchy.

```markdown
### `spawn_agent_structure`
**Description:** Creates the directory, PROMPT.md, and SKILL.md for a new agent.
**Parameters:**
- `agent_id`: e.g., "08_AMY_A3"
- `archetype`: e.g., "Memory Guardian"
- `os_target`: "Life" or "Business"
**Action:** Generates standard boilerplate files.
```

```markdown
### `deploy_skill_update`
**Description:** Appends a new tool definition to an existing agent's SKILL.md.
**Parameters:**
- `target_filepath`: Path to SKILL.md
- `new_skill_block`: The markdown code block for the tool.
```

## 2. INFRASTRUCTURE MAINTENANCE
Tools to keep the file system clean.

```markdown
### `clean_orphaned_files`
**Description:** Scans for files that are not linked in the Protocol or Index.
```
