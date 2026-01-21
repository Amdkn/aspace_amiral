# [[L003]] : Gemini CLI - Skills Alignment Protocol

- **Date**: 2026-01-15
- **Pattern**: Standard AI operations tend to drift towards "one-off scripts" (Technician mode), losing the benefit of iterative learning and reuse.
- **Principle**: The Gemini CLI is not just a tool; it is the **Host of the OS Identity**. Every command run via Gemini CLI must be contextually anchored by the `kernel_os_identity` skill.
- **Manager Guideline**: 
    1. Always use `gemini run "Utilise <skill_name> pour..."`.
    2. Before starting a complex task, ask: "Est-ce une compétence qui doit être usinée dans la Factory ?".
    3. The `knowledge` pane in the UI is a mirror of the `00_CORE/KERNEL/KNOWLEDGE` directory.
