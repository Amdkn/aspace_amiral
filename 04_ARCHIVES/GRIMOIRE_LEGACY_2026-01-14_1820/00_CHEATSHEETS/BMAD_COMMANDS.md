# 🧠 BMAD COMMANDS - Cheatsheet

> **Usage :** Ces commandes sont à taper dans Gemini CLI pour piloter le workflow BMad.

---

## 🚀 LES 5 COMMANDES ESSENTIELLES

| Commande | Description | Exemple |
|----------|-------------|---------|
| `*workflow-init` | Démarre une nouvelle track de projet. | `*workflow-init "GENESIS_LOCAL"` |
| `*status-check` | Vérifie l'état des agents et des serveurs MCP. | `*status-check` |
| `*veto-override` | Force une action bloquée par Beth Veto (demande > 4h). | `*veto-override "deploy-prod"` |
| `*build-run` | Lance une compilation/génération Rick. | `*build-run "./output/workflow.json"` |
| `*mcp-list` | Liste tous les outils MCP connectés à R0. | `*mcp-list` |

---

## 🛠️ COMMANDES AVANCÉES

| Commande | Description |
|----------|-------------|
| `*conductor-assign <agent> <task>` | Assigne une tâche à un agent spécifique via Conductor. |
| `*skill-load <skill_name>` | Charge dynamiquement un skill depuis le Grimoire. |
| `*rick-mode` | Passe en mode Architecte (ignore Life/Business OS). |
| `*rollback <step_id>` | Annule la dernière action d'un step ID donné. |

---

## 📋 SYNTAXE DES PROMPTS CLI

Pour exécuter un ordre "one-shot" sans entrer en mode interactif :

```bash
gemini run --skill "Rick_Build" --prompt "Génère le JSON n8n pour le projet X"
```

Pour lancer le TUI Ralph :
```bash
gemini tui --config ./ralph_config.json
```

---

## 🔗 RÉFÉRENCES

- **BMad Method Repo :** `bmad-code-org/BMAD-METHOD`
- **Conductor Extension :** `gemini-cli-extensions/conductor`
- **Skill Porter :** `AcidicSoil/skill-porter`

---

*Wubba Lubba Dub Dub ! 🧪*
