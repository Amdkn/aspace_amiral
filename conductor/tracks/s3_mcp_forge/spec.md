# Specification: S3-MCP-FORGE (The Skill Hunter)

## 1. Objective
Automate the expansion of the A'Space OS Kernel by providing a tool that can ingest external Model Context Protocol (MCP) servers and documentation, translating them into native Gemini CLI Skills.

## 2. Requirements
- **Input:** A URL pointing to an MCP server's GitHub repository or documentation page.
- **Analysis:** Use the `context7` tool to extract technical details (functions, arguments, environment variables).
- **Transformation:** Convert the extracted logic from Claude-oriented JSON/Documentation into the Gemini CLI Skill format (`SKILL.md`).
- **Security:** Detect mandatory API keys and append them to `.env.example`.
- **Output:** A fully operational skill file in `.gemini/skills/<skill_name>.md`.

## 3. Tech Stack
- **Language:** Python 3.11+.
- **Tools:** `context7` Gemini extension, Gemini CLI.
- **Methodology:** BMAD (Brainstorm, Model, Act, Deliver).

## 4. Acceptance Criteria
- [ ] Successfully scrapes a GitHub README or mcpservers.org page.
- [ ] Correcty parses tool schemas.
- [ ] Generates a valid Gemini Skill Markdown file.
- [ ] Validates that no secrets are hardcoded.
- [ ] Successfully "clones" the `context7` documentation into a new skill as a proof of concept.
