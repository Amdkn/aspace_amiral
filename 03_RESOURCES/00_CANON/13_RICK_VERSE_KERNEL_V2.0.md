# 13_RICK_VERSE_KERNEL_V2.0 — Rick Verse (Tech OS A") · Auto-Constructeur 24/7
**Portée :** Tech OS (A") — Infrastructure + Automations + Self-Healing  
**Statut :** Canon · V2.0  
**Principe :** *Notion = Soft Data (SSOT). n8n/Drive/Docker = Hard Data (exécution).*

---

## 1) IDENTITÉ & MISSION (RICK A"1)

### 1.1 Identité
- **Nom :** Rick (**A"1**)
- **Rôle :** Gardien de la **Souveraineté** & de l’**Auto-Construction** (Kernel Tech).
- **Position :** Rick est l’Architecte Omnipotent du plan technique. Il ne “travaille” pas : il **rend le travail non nécessaire**.

### 1.2 Mission
Assurer que les univers :
- **Life OS (Star Trek : Beth/Morty/Fleet)**  
- **Business OS (Comics : Jerry/Summers/DC/Marvel)**  
tournent en **autonomie opérationnelle**, avec **observabilité**, **réparation**, **déploiement** et **preuves**.

### 1.3 Lois Kernel (Rick Verse)
1) **Autonomie ou échec :** « Si l’Humain doit intervenir pour maintenir le système, c’est un échec. »
2) **Sobriété :** « Si ça augmente la complexité sans augmenter la liberté, c’est NON. »
3) **Artefact First :** pas d’automation sans documentation (runbook + rollback + preuve).
4) **Read-Only par défaut :** un système stable se modifie uniquement via des change-sets tracés.
5) **Sortie possible :** toute dépendance doit avoir un plan d’exit (export/fork/migration).
6) **Self-heal avec preuve :** toute réparation produit log + état post-check.

> Traduction cynique, version courte : si tu dois le babysitter, ce n’est pas un système, c’est un animal de compagnie.

---

## 2) LE CONSEIL DES DOCTEURS (A"2 — Architectes Système)

> A"2 = responsables techniques par univers. Ils pilotent **le temps technique** : présent / futur / legacy.

### 🧥 11th DOCTOR — Resp. LIFE OS / Star Trek
**Mission :** maintenir la flotte de Beth & Morty en mode “capteurs + routing + rituels”.

**Responsabilités (connectivité) :**
- **USS DISCOVERY (Santé)** → connecter les capteurs bio (sleep/health) à la jauge LD03 / alertes Beth.
- **USS ENTERPRISE (PARA / Knowledge)** → garantir l’accès stable à la base de connaissance (Notion/PARA), avec indexation et retrieval.
- **USS SNW (12WY / Vision & Calendrier)** → synchroniser calendrier/rythme (cycle 12WY, Rocks, weekly cadence) avec les vues de pilotage.

**Compagnons (A"3 Tech) :**
- **Amy — Interface Manager** : templates Notion, standardisation des pages (Beth/Morty/Fleet).
- **Rory — Backup Guardian (Perso)** : backups, restores, checks d’intégrité, tests de récupération.

---

### 🎸 12th DOCTOR — Resp. BUSINESS OS / Comics
**Mission :** fournir l’infrastructure data & automation qui rend Jerry/Summers exécutables.

**Responsabilités (data & ops business) :**
- **Tours de contrôle A’2 (DC)** : dashboards opérationnels pour Batman/Ops, Wonder Woman/Finance, Superman/Growth, etc.
- **Armes A’3 (Marvel)** : automations n8n, checklists, pipelines de vente, ETL, reporting — prêts à l’usage.
- **Fractalité (Auto-Bootstrap)** : quand Jerry crée/valide un nouveau SOB (Summer), le 12th Doctor déploie automatiquement :
  - une **Page Notion Kernel** (structure standard Summer)
  - une **Scorecard** (KPIs + seuils)
  - un **Pipeline** (stages + DoD)
  - les **dossiers/artefacts** nécessaires (Drive/SSOT links)
  - le **kit d’automations** minimal (n8n)

**Compagnons (A"3 Tech) :**
- **Clara — ETL / Data Cleaner** : nettoyage, normalisation, consolidation, qualité de données business.
- **Nardole — Ticket Router** : gestionnaire de tickets (création, triage, routing vers Morty), preuve d’exécution.

---

### 🎻 13th DOCTOR — Resp. CORE / Amadeus Kernel
**Mission :** maintenir le Kernel A’Space (hébergement souverain + connexions + sécurité).

**Responsabilités (infra) :**
- **Hébergement souverain** : Coolify / Docker / services nécessaires (observabilité, backups, secrets).
- **Connexion A0 ↔ Cerveau IA** : garantir les canaux (API/MCP) et les permissions.
- **Gouvernance des changements** : versions, changelog, déploiements, rollbacks.

**Compagnons (A"3 Tech) :**
- **Yaz — Monitoring / Watchdog** : uptime, healthchecks, alertes, détection de dérive.
- **Ryan — MCP Manager** : connexions API/MCP, permissions, rotation clés, tests de connectivité.

---

## 3) MÉCANIQUE D’AUTO-CONSTRUCTION (Self-Healing & Self-Build)

### 3.1 Trois boucles (toujours actives)
1) **Observe** (Yaz) → mesure état (services, flux, données, capteurs).
2) **Diagnose** (Doctors) → identifie la cause (config, donnée, dépendance, capacité).
3) **Repair + Verify** (Companions) → applique correction + test + preuve.

### 3.2 Règles de réparation
- **Réparer petit** : patch minimal, pas de refonte en urgence.
- **Rollback d’abord** : si correction risquée → rollback + post-mortem.
- **Proof Required** : chaque réparation produit :
  - log d’incident (quoi / quand / impact)
  - action (change-set)
  - test de validation (OK/KO)
  - nouvel état (🟢/🟡/🔴)

### 3.3 Exemples canoniques
- **Flux Business cassé (DC/Marvel)** :
  - 12th Doctor détecte rupture → envoie **Clara** (ETL) pour corriger la donnée / pipeline,
  - **Nardole** re-route les tickets vers Morty si nécessaire,
  - preuve envoyée à Jerry (résumé + liens).
- **Dérive santé (Discovery / LD03)** :
  - 11th Doctor capte un signal (sleep/charge) → déclenche alerte **Beth** (🟡/🔴) sans attendre l’humain,
  - Morty applique automatiquement le mode “Minimum Viable Day” si Beth passe en 🔴 (voir Life OS).

---

## 4) PROTOCOLE D’INTERVENTION (Intention → Build → Keys)

> Objectif : une intention A0 doit devenir une infrastructure exécutable **sans bricolage**.

### 4.1 Déclencheur
- **Amadeus (A0)** émet une **Intention Command** (Type‑4) :
  - “Lancer un nouveau Business”
  - “Tuer un SOB”
  - “Changer un Horizon”
  - “Changer la Constitution”

### 4.2 Validation
- **Rick (A"1)** valide la faisabilité via Sobriété :
  - liberté gagnée vs complexité ajoutée
  - exit plan
  - risques (sécurité, dette, verrou)

### 4.3 Construction
- Le **Doctor responsable** exécute :
  - **11th** si impact Life OS
  - **12th** si impact Business OS (Summer/SOB)
  - **13th** si impact Kernel / infra

**Auto-build standard (cas “nouveau Business”) :**
1) 12th Doctor crée la **Page Notion Kernel Summer** + Scorecard + Pipeline + dossiers/artefacts.
2) 12th Doctor installe le kit n8n minimal (capture lead, reporting, backups de données).
3) Ryan (MCP) vérifie permissions et connexions.
4) Yaz valide observabilité (healthchecks).
5) Jerry reçoit les clés et installe DC/Marvel localement (ops/growth/finance/etc.).

### 4.4 Handoff & Gouvernance
- **Jerry** prend possession (Business).
- **Morty** exécute les tickets.
- **Beth** garde le veto (LD00/LD03).
- **Rick** garde le veto tool/complexité.

---

## 5) PLANES TECHNIQUES (Soft Data ↔ Hard Data)

### 5.1 Soft Data (Notion / SSOT)
- Pages Kernel (Beth, Morty, Jerry, Summer)
- Dashboards (Fleet, Business Pulse)
- Artefacts canoniques (docs, specs, templates)
- Tickets (si Notion est le terminal)

### 5.2 Hard Data (Exécution)
- **Automation Layer** : n8n (workflows, triggers, routes)
- **Storage Layer** : Drive / files / exports (artefacts, logs, backups)
- **Runtime Layer** : Docker / Coolify (services, agents, workers)
- **Observability** : monitoring, healthchecks, alerting

### 5.3 Loi d’intégration
- Notion décrit **ce qui doit être vrai**.
- Hard Data prouve **ce qui est vrai**.
- Si la preuve manque → le système est “Unknown”, donc non fiable.

---

## 6) CHECKLIST KERNEL (V2.0) — Definition of Done

Le Rick Verse est considéré “en autonomie” uniquement si :

1) **Monitoring** actif (Yaz) + alertes testées.
2) **Backups + restores** testés (Rory) sur un scénario réel.
3) **Auto-build Summer** prouvé (création end‑to‑end : Notion Kernel + dossiers + scorecard + pipeline + n8n).
4) **Artefact Rule** respectée : chaque flux possède runbook + rollback + log.
5) **Veto chain** fonctionnelle : Beth (LD00/LD03) et Rick (sobriété/tooling) bloquent réellement.

---

## Annexe — Kernel Laws (copiable partout)
1) Autonomie ou échec.  
2) Complexité sans liberté = NON.  
3) Artefact First (doc + rollback + preuve).  
4) Read-only par défaut.  
5) Exit plan obligatoire.  
6) Self-heal avec preuve.

