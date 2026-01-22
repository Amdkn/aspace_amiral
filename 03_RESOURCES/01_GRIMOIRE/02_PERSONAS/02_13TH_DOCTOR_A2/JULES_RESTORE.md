# 📜 TECHNICAL ORDER: JULES_RESTORE (A0-REK-v1.0)

> **ORCHESTRATOR:** Conductor (Antigravity)
> **EXECUTOR:** Ralph Loop
> **SUPERVISOR:** Amy Pond (E-Myh Extension)
> **PRIORITY:** CRITICAL (System Restoration)

---

## 1. OBJECTIVE
Resolve the `🔴 TOTAL HALT` status by performing a deep structural audit and self-healing cycle on the A'Space R0 environment.

## 2. INSTRUCTIONS FOR JULES
Use the `doctor-toolkit` to perform the following sequence:

### [PHASE: ANALYSIS] — PARA SCAN
1. **Action:** `ralph_verify_state("PARA_Root")`
2. **Criteria:** Check for required directories: `01_PROJECTS`, `02_AREAS`, `03_RESOURCES`, `04_ARCHIVES`.
3. **Criteria:** Verify existence of `manifest.yaml` in the root.

### [PHASE: DESIGN] — RECOVERY BLUEPRINT
1. If deviations are found, Conductor must generate a fix blueprint in `03_RESOURCES/00_CANON/recovery_blueprint.md`.
2. **Amy's Extension:** The recovery must not just "fix" but "enhance" (Antifragility). Add missing `.antigravityignore` rules to protect against future "dumb" scripts.

### [PHASE: DEV] — RALPH EXECUTION
1. **Action:** `run_command("mkdir ...")` or `write_to_file(...)` as specified in the blueprint.
2. **Idempotency:** Ralph must loop until the scans return `GREEN`.

### [PHASE: TEST] — VERIFICATION
1. Verify the `aspace-os-v1` dev server is still running.
2. Verify Dashboard telemetry reflects the updated status.

---

## 3. REPORTING (JULES_NOTIFY)
Upon completion, notify the Amiral via the **Kernel Operator Console** with:
`[SUCCESS] Antifragility Loop Complete. Status: OPERATIONAL. PARA Integrity: 100%. - Come along, Pond!`

---
*Signed by the Conductor, under Authority type-4.*
