# 🧠 GRIMOIRE : LESSONS LEARNED (Manager Knowledge)

## 🚩 Purpose
This is the **Sovereign Memory** of the A'Space OS. 
Unlike a technical log, this base stores **Principles** and **Patterns** derived from failures and successes. It is managed by **Antigravity (Manager)** to inform future loops.

---

## 🏗️ Knowledge Index

### [[L001]] : The "Null Mapping" Trap (n8n Webhook)
- **Date**: 2026-01-15
- **Pattern**: When sending JSON to n8n via shell/PowerShell, encoding and shell interpretation often corrupt the payload, leading to `null` fields in the DB.
- **Principle**: Never assume the pipe is clean. Always use a file-based transfer (`curl -d @file.json`) or a validation node within the loop before the database entry.
- **Manager Guideline**: The Technician must provide a "Proof of Persistence" row count for every signal track.

### [[L002]] : Skills vs Workflows Paradox
- **Date**: 2026-01-15
- **Pattern**: A simple n8n workflow is a "Hope-based" system. A Skill is a "Guarantee-based" system.
- **Principle**: Workflows execute; Skills validate and recurse until success.
- **Manager Guideline**: Any mission-critical automation must be encapsulated in a **Skill Factory** prototype before deployment.

---

## 📜 Update Protocol
1. **Identify**: A recurring error or a breakthrough pattern.
2. **Distill**: Remove the "noise" (specific code) and keep the "signal" (the principle).
3. **Record**: Add to this index with a unique ID `[[Lxxx]]`.
4. **Broadcast**: Inform the Technicien (Amadeus) to update his local rules.
