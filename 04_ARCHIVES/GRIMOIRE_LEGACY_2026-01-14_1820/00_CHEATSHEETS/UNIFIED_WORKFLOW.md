# ⚡ A'SPACE UNIFIED WORKFLOW (GOLDEN STACK)

> "BMad pense, Conductor dirige, Ralph travaille, Skillz exécute."

## 1. PHASE DE PENSÉE (BMAD)
*On ne code pas sans ticket.*
* `*workflow-init` : Lancer l'analyse du projet et choisir la Track.
* `*plan` : Générer le plan d'action détaillé.

## 2. PHASE D'ORCHESTRATION (CONDUCTOR)
*On prépare le terrain.*
* `*conductor-setup` : Initialise le contexte du projet (si nouveau).
* `*conductor-track "Feature Name"` : Démarre une session de travail spécifique.
* `*conductor-status` : Où en sommes-nous ?

## 3. PHASE D'ITÉRATION (RALPH LOOP)
*On laisse la machine suer.*
* `/ralph-loop "Implémente le Step 1 du plan Conductor" --max-iterations 10`
    * *Note :* Ralph va lire le plan, coder, tester, corriger, recommencer.
    * *Note :* Si Ralph bloque, il utilise les tools dans `~/.skillz`.

## 4. PHASE DE VALIDATION
* `*conductor-implement` : Marquer la tâche comme faite.
* `git commit` : Ancrer dans le réel.

---
**EXEMPLE DE COMMANDE COMBO :**
`*conductor-track "Setup N8N" && /ralph-loop "Installe n8n via Docker MCP et vérifie le port 5678" --max-iterations 5`
