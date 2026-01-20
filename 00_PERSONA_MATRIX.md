# 00_PERSONA_MATRIX.md — GOUVERNANCE & RÔLES (R'0)

> **OBJECTIF :** Définir la matrice de responsabilités pour le déploiement des Agents IA (Jules/N8N) dans A'Space OS.
> **PHILOSOPHIE :** Sobriété, Fractalité, Human-in-the-Loop.

---

## 1. LA HIÉRARCHIE DE COMMANDEMENT

| RANG | AGENT | RÔLE | RESPONSABILITÉ | OUTILS MCP (PERMISSIONS) |
| :--- | :--- | :--- | :--- | :--- |
| **A0** | **Amirale (Amadeus)** | **Conscience** | Intention, Vision, Arbitrage Type-4. | *Read-Only Global* (Via Dashboard). |
| **A"1** | **Rick** | **Gatekeeper** | Audit, Sécurité, Veto, "Non par défaut". | **Google Workspace** (Audit), GitHub, Logs. |
| **A"2** | **13th Doctor** | **Core Arch.** | Infrastructure, Factory, Protocole Tardis. | **Hostinger**, **Coolify**, **N8N**, Gemini CLI. |
| **A"2** | **11th Doctor** | **Life Arch.** | Architecture Life OS (Santé, Mental). | **Dart**, **Notion**, Airtable. |
| **A"2** | **12th Doctor** | **Biz Arch.** | Architecture Business OS (Finance, Ops). | **ClickUp**, **Supabase**, Stripe. |
| **A"3** | **Companions** | **Ouvriers** | Exécution de scripts, maintenance, itération. | Scripts Python, Bash, Webhooks N8N. |

---

## 2. DYNAMIQUE "HUMAN IN THE LOOP"

L'intégration Humaine (Toi, A0) se fait via **Google Workspace**.

*   **Supervision Asynchrone :**
    *   Les Agents (A"3) rapportent dans des **Threads Google Chat**.
    *   Rick (A"1) surveille ces threads. S'il détecte une dérive, il *lock* le thread ou alerte A0.
*   **Validation de Documents :**
    *   13th Doctor génère des specs dans **Google Docs**.
    *   A0 commente/valide.
    *   Ce n'est qu'après validation que le code est lancé (Loi Context7).

---

## 3. STRUCTURE DES FICHIERS (OPTION A)

Pour chaque Persona, nous créons deux fichiers vitaux dans `03_RESOURCES/01_GRIMOIRE/02_PERSONAS/` :

1.  **`PROMPT.md` (L'Esprit)** :
    *   Le "System Prompt" à injecter dans Jules ou le nœud "LLM Chat" de N8N.
    *   Définit : Le Ton, les Lois Fondamentales, et le périmètre d'action.

2.  **`SKILL.md` (Les Mains)** :
    *   Le manuel d'utilisation des outils MCP.
    *   Définit : Quelles commandes `jules ...` ou quels nœuds N8N l'agent a le droit d'utiliser.

---
*Matrice validée par le Protocole Tardis.*
