# SKILL — GRAHAM O'BRIEN (UX & STABILITY)

## 1. SYSTEM HEALTH
Tools to monitor the stability and "vibe" of the OS.

```markdown
### `report_system_stability`
**Description:** Scans the active agents (Life & Business) and reports on their "Stress" (load/error rate).
**Output:** A simple "Traffic Light" report (Green/Amber/Red) with human-readable advice.
```

## 2. UX INTERVENTION
Tools to fix interaction problems.

```markdown
### `simplify_agent_output`
**Description:** Takes a complex technical output from Ryan or the 12th Doctor and rewrites it for A0.
**Parameters:**
- `raw_text`: The complex text.
- `tone`: "Reassuring", "Simple", "Brief".
```

```markdown
### `suggest_break`
**Description:** Triggers a "Pause" protocol if the session count exceeds safety limits (100 free sessions).
**Action:** Reminds A0 to log off or switch contexts.
```
