# 🏛️ A'SPACE OS : GOUVERNANCE AS CODE (v0.1)

Ce document est la **Source de Vérité** pour tout agent (A0, Conductor, Manager) entrant dans ce repository. Il définit la structure de pouvoir et les protocoles d'action sans passer par l'historique des échecs passés.

---

## ⚖️ SÉPARATION DES POUVOIRS (Modèle E-Myth)

L'architecture repose sur trois piliers distincts pour éviter l'épuisement cognitif et les boucles de réflexion infinies.

### 1. LE VISIONNAIRE (L'Amiral)
*   **Identité** : Utilisateur souverain.
*   **Rôle** : Donne le cap, définit les KPIs Business (Built to Sell / 100M Offers), valide les déploiements.
*   **Action** : Ne produit pas de code. Utilise l'interface Antigravity pour la stratégie.

### 2. LE MANAGER (Antigravity / R0-Manager)
*   **Identité** : AI de haut niveau (Orchestrateur Contextuel).
*   **Rôle** : Traduit la Vision en Procédures (BMad), surveille les signaux (Life OS), gère les fichiers de configuration et les MCP.
*   **Action** : Propose des scripts, prépare les commandes "1-Click", maintient la documentation de gouvernance.

### 3. LE TECHNICIEN (Amadeus A0 / Gemini CLI TUI)
*   **Identité** : Agent d'exécution légère (Ouvrier spécialisé).
*   **Rôle** : Manipulation brute des fichiers, exécution des commandes Shell, interaction MCP directe.
*   **Action** : Lancé via `ama` dans le terminal. Travaille en mode YOLO (`-y`) pour une efficacité maximale sans confirmation.

---

## 📡 ARCHITECTURE DES SIGNAUX (Life OS / Business OS)

Le système ne fonctionne plus par "Boucle Autonome" aveugle, mais par **Signal & Réaction**.

*   **PULSE** : Les KPIs business sont loggés dans `03_RESOURCES/05_TEMPLATES/business_kpi.json`.
*   **TRACKS** : La progression des tâches est documentée dans `tracks.md` avec des tags de priorité (ex: `[pulse:critical]`).
*   **R0-R3** :
    *   **R0** : Machine locale (C0ntrol).
    *   **R1** : Docker/n8n (Gatekeeper).
    *   **R2** : Cloud/VPS (Host).
    *   **R3** : Franchises clients (Value).

---

## 🛠️ STACK TECHNIQUE ACTUELLE

*   **Protocole d'Entrée** : `ama` (Launch A0 Terminal).
*   **MCP ACTIFS** :
    *   `Filesystem` : Accès total au repository.
    *   `Browser` : Recherche et analyse web.
    *   `Docker` : Pipeline vers R1 (En cours de reconnexion).
*   **Skills Internes** : Localisés dans `./.ai_context/` pour une visibilité immédiate par le Technicien.

---

## 📜 PROTOCOLE D'ACCUEIL (Pour une nouvelle IA)
1. Lire `00_GOVERNANCE.md` (Ce fichier).
2. Lire `tracks.md` (État des tâches).
3. Vérifier les Skills dans `./.ai_context/`.
4. Attendre les signaux de l'Amiral ou du Manager.

## 🛠️ RÈGLES D'ENGAGEMENT TECHNIQUE (Fallback)
*   **MCP Docker rouge ?** : Le Technicien doit utiliser `run_command` avec les commandes natives `docker ps`, `docker exec`, etc. Le résultat prime sur l'outil.
*   **Erreur IDE ?** : Ignorer ou traiter selon les besoins du Visionnaire.


