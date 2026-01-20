# ANTIGRAVITY CONSTRUCTION PROTOCOL (B.L.A.S.T.)

Tout nouveau système ou agent doit être construit selon la méthode B.L.A.S.T. définie par l'Architecte (Jack Roberts).

## 1. BLUEPRINT (Vision & Logic)
* **North Star** : Quel est l'objectif unique ?
* **Source of Truth** : Où vit la donnée (Notion, Supabase) ?
* **Behavior** : Règles strictes de comportement.
* *Action :* Toujours initialiser un fichier `gemini.md` à la racine du projet.

## 2. LINK (Connections)
* Utiliser le **MCP (Model Context Protocol)** pour connecter les outils.
* Ne jamais coder d'API wrapper manuel si un serveur MCP existe (ex: Fireflies, Notion, Slack).

## 3. ARCHITECT (The A.N.T. Layers)
* **Architecture** : Les SOPs techniques en Markdown.
* **Navigation** : Le routage logique.
* **Tools** : Les scripts déterministes (Python/Bash).
* *Règle d'Or :* Séparer la logique business (Code) de l'inférence (LLM).

## 4. STYLIZE (UX/UI)
* La fonctionnalité ne suffit pas. Le résultat doit être "Gorgeous".
* Utiliser les blocs Slack, les mises en page Notion, ou des composants UI riches.

## 5. TRIGGER (Deployment)
* Déploiement sur **Modal** ou **n8n** pour l'exécution asynchrone.
* L'agent ne doit pas dépendre de l'IDE ouvert pour tourner (Souveraineté).
