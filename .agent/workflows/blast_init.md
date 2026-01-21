---
description: Initialise un nouveau projet selon le protocole B.L.A.S.T. (Blueprint, Link, Architect, Stylize, Trigger).
---

# GÉNÉRATEUR DE SYSTÈME B.L.A.S.T.

Ce workflow transforme une idée vague en architecture solide.

## Étape 1 : Blueprint (La Vision)
1.  Demander : "Quelle est la 'North Star' de ce système ?"
2.  Créer le fichier `gemini.md` avec la structure du projet.
3.  Définir la "Source of Truth" (ex: Notion Database).

## Étape 2 : Link & Architect (Le Corps)
1.  Identifier les serveurs MCP nécessaires (ex: `@notion`, `@github`).
2.  Générer l'arborescence A.N.T. (Architecture / Navigation / Tools).
3.  Écrire les pseudo-SOPs dans `docs/architecture.md`.

## Étape 3 : Trigger (Le Déploiement)
1.  Demander : "Quelle est la fréquence d'exécution ?" (Cron).
2.  Générer le script de déploiement (n8n JSON ou Modal Python).
3.  Confirmer : "Système prêt pour le lancement."
