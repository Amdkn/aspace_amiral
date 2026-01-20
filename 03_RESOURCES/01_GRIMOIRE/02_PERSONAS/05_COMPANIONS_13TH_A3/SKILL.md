# SKILL — COMPANIONS (A"3) META-TOOLS

The **Companions of the 13th** use these skills to build, maintain, and audit the *other* agents in the Rick's Verse.

## 1. AGENT SPAWNING (RYAN)
Tools for initializing new agent structures.

```markdown
### `spawn_agent_crew`
**Description:** Initializes the file structure for a new Agent Team.
**Parameters:**
- `os_type`: "Life" or "Business" or "Kernel"
- `doctor_version`: "11th" or "12th" or "13th"
- `agent_names`: List of names (e.g., ["Amy", "Rory"])
**Action:**
1. Creates directory `03_RESOURCES/01_GRIMOIRE/02_PERSONAS/[NEW_DIR]`
2. Generates template `PROMPT.md` based on OS Type.
3. Generates empty `SKILL.md`.
```

## 2. COMPLIANCE AUDIT (YAZ)
Tools for verifying agent alignment with Kernel Laws.

```markdown
### `audit_agent_alignment`
**Description:** Reads an agent's PROMPT.md and checks for violations of the Solarpunk/Kernel Manifesto.
**Parameters:**
- `target_agent_path`: Path to the agent's directory.
**Checklist:**
1. Does it reference the correct Doctor (11th/12th)?
2. Does it respect the A0 hierarchy?
3. Is the tone consistent with the defined Archetype?
4. Are there "Jailbreak" vulnerabilities?
```

## 3. SKILL EVOLUTION (RYAN & GRAHAM)
Tools for upgrading agent capabilities while maintaining usability.

```markdown
### `evolve_agent_skill`
**Description:** Adds a new tool definition to an agent's SKILL.md.
**Parameters:**
- `target_agent`: Name of the agent.
- `skill_name`: Name of the new tool.
- `skill_logic`: Pseudo-code or description of the tool.
**Process:**
1. **Graham Check:** Is this skill too complex for the user?
2. **Ryan Action:** Append the skill block to `SKILL.md`.
```

## 4. SYSTEM STABILITY (GRAHAM)
Tools for reporting on the health of the verse.

```markdown
### `report_system_health`
**Description:** Scans the `02_PERSONAS` directory and reports on missing files or broken links.
**Output:** A "Scorecard" of the Agent Fleet's readiness.
```
