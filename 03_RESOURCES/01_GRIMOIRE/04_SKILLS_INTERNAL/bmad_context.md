# 📘 BMAD CONTEXT (INTERNAL)

## 1. PARA STRUCTURE
*   `01_PROJECTS` / `02_AREAS` / `03_RESOURCES` / `04_ARCHIVES`

## 2. PHASES & HOOKS
*   `[phase:analysis]` -> Document "Why" in `03_RESOURCES/00_CANON/analysis.md`.
*   `[phase:design]` -> Create skeletons/templates. Don't write logic.
*   `[phase:dev]` -> Implementation. Follow design precisely.
*   `[phase:test]` -> Run verification and auditing.

## 3. ANTI-FRAGILE RULES (THE AUDIT)
*   **Tool Verification** : Always check for `write_file` before attempting creation.
*   **Pathing**: Use relative paths. Never assume a folder is already there (use `create_directory` if needed).
*   **Atomic Actions**: One change per turn. Update `tracks.md` immediately.
*   **Failure Audit**: If a tool fails, document the exact error message in `tracks.md` under a `## 🕵️ FAILURE LOG` section. Stop and wait for the Amiral.

