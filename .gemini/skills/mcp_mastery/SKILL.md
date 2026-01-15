---
name: mcp_mastery
description: Maîtrise des serveurs MCP (Filesystem, Docker, Browser) pour les agents A'Space OS.
---

# MCP Mastery Skill

## 📡 PROTOCOLE DE CONNEXION
1.  **Vérification** : Toujours lancer `/mcp list` au début de la session.
2.  **Diagnostic** : Si un serveur est rouge (🔴), utiliser les commandes Shell natives (`docker ps`, `ls`) via `run_command`.
3.  **Permissions** : En cas d'erreur de permission, demander l'activation du flag YOLO (`-y`).

## 🛠️ OUTILLAGE PRIORITAIRE
*   **Filesystem** : Utiliser `edit_file` pour la création/modification atomique.
*   **Docker** : Privilégier la gestion des containers pour le déploiement de R1 (n8n).
*   **Browser** : Analyser les documentations externes (BMad Github, YouTube summaries).

## ⚖️ GOUVERNANCE
*   L'agent ne doit jamais inventer d'outils. 
*   Si l'outil MCP échoue, le Technicien reporte l'erreur exacte au Manager (Antigravity).
