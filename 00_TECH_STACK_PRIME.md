# 00_TECH_STACK_PRIME.md — ARCHITECTURE TECHNIQUE "GOLDEN STACK"

> **STATUT :** VALIDÉ
> **ARCHITECTE :** 13th Doctor (A"2)
> **OPÉRATEUR :** Jules (R'0)
> **OBJECTIF :** Une stack décentralisée mais orchestrée, où chaque OS utilise le "Best in Class" pour sa fonction.

---

## 1. LE CŒUR D'ORCHESTRATION (THE BRIDGE)

C'est la couche qui relie les silos. Sans elle, le système est fragmenté.

*   **Intelligence Active :** **Jules (Moi)**
    *   *Rôle :* Opérateur Terminal, Scripteur, Maintenance.
    *   *Outil :* **Gemini CLI** (Sur VPS Hostinger) + **MCP** (Model Context Protocol).
    *   *Mission :* "Je suis le code qui connecte les API."
*   **Flux Automatisés :** **n8n**
    *   *Rôle :* Le système nerveux. Déplace la donnée de A vers B sans intervention humaine.
    *   *Hébergement :* Self-hosted sur Hostinger VPS (Docker).

---

## 2. KERNEL OS (13ÈME DOCTEUR — INFRA & CONTEXTE)

Le domaine de la structure, de la mémoire et de la souveraineté.

*   **Interface de Commandement :** **Archon OS**
    *   *Fonction :* Hub de Contexte & Documentation.
    *   *Rôle :* "Le Cerveau Externe". Centralise les docs, les snippets, et l'état du système.
*   **Infrastructure Physique :** **Hostinger VPS**
    *   *Fonction :* La "Salle des Machines" (R").
    *   *Contenu :* Docker (n8n, Archon, Supabase local ou proxy).

---

## 3. LIFE OS (11ÈME DOCTEUR — VIE & HARMONIE)

Le domaine de l'individu (Beth/Morty). Optimisé pour la fluidité et la clarté mentale.

*   **Moteur d'Exécution (GTD) :** **Dart**
    *   *Pourquoi ?* IA-Native, rapide, clavier-first.
    *   *Utilisateur :* Morty (A1 Execution).
    *   *Flux :* Tâches quotidiennes, Inbox, Next Actions.
*   **Base de Connaissance (PARA) :** **Notion**
    *   *Pourquoi ?* Flexible, document-oriented.
    *   *Utilisateur :* Beth (A1 Core).
    *   *Flux :* Projets longs, Archives, Ressources, Identité.
*   **Stratégie & Métriques (12WY) :** **Airtable**
    *   *Pourquoi ?* Base de données relationnelle visuelle, calculs.
    *   *Utilisateur :* Rick (A1 Audit).
    *   *Flux :* Tracking d'habitudes, Scores hebdos, Objectifs Trimestriels.

---

## 4. BUSINESS OS (12ÈME DOCTEUR — VALEUR & PROJETS)

Le domaine de la production et de l'argent (Jerry/Summers). Optimisé pour le débit et la collaboration.

*   **Business Pulse (Management) :** **ClickUp**
    *   *Pourquoi ?* Hiérarchie puissante (Space/Folder/List), Vues multiples.
    *   *Utilisateur :* Jerry (A'1 Stratège) + Justice League (A'2).
    *   *Flux :* Roadmaps Produits, Sprints, Tickets A'3.
*   **Muse de SOB (Data & Backend) :** **Supabase**
    *   *Pourquoi ?* SQL Open Source, Auth, Realtime.
    *   *Utilisateur :* Les Summers (A'1 Micro-CEO) + Apps clients.
    *   *Flux :* Données utilisateurs, Contenu "Muse" (Inspiration stockée), Backends des SOBs.

---

## 5. SCÉNARIO D'INTÉGRATION (EXEMPLE "MCP")

Si je (Jules) maîtrise les MCP, voici comment je pilote le tout depuis le Terminal :

1.  **Commande :** `jules run --context=life "Check weekly goals"`
2.  **Action MCP :**
    *   Je requête **Airtable** (via MCP-Airtable) pour lire les scores 12WY.
    *   Je requête **Dart** (via MCP-Dart) pour voir les tâches bloquantes.
    *   Je croise les données dans **Archon** (Mémoire).
3.  **Résultat :** Je génère un rapport dans **Notion** et je ping **Beth** si un objectif est rouge.

> **Validation de Capacité :** OUI. En tant qu'IA Ingénieur, je peux configurer des serveurs MCP pour chacune de ces briques (ou utiliser ceux existants) et les piloter via le Terminal ou n8n.

---
*Stack verrouillée pour l'initialisation R'0.*
