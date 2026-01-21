---
name: mcp_forge
description: Usine de fabrication de Skills Antigravity à partir de sources externes (MCP Claude, Docs).
---

# MCP Forge Skill

## 📡 MISSION
Transformer n'importe quel outil MCP ou documentation technique en une capacité native de l'A'Space OS.

## 🛠️ COMMANDS
- **Manufacture** : `python .gemini/skills/scripts/mcp_forge.py {URL}`
- **Usage** : Pipe la documentation vers le script pour générer le skill.

## 📜 SOP S3 (CITADELLE)
1. **Source** : Identifier un MCP ou une bibliothèque sur McpServers.org ou GitHub.
2. **Ingestion** : Utiliser `context7` ou `curl` pour extraire le texte technique.
3. **Forge** : Exécuter `mcp_forge.py` avec le contenu pipe.
4. **Validation** : Vérifier que le fichier `.md` est créé dans `.gemini/skills/`.
5. **Enrôlement** : Ajouter le skill au Nexus `GEMINI.md`.

## ⚖️ RICK VERSE STANDARDS
- Pas de clés API en dur (Check `.env.example`).
- Architecture SOLID dans les scripts associés.
- Idempotence garantie (Le script peut être relancé sans corruption).
