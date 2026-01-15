# 14_DOCTORS_AGENTS_V1.0 — A"2 · The Doctors (Chief Engineers)
**Portée :** Tech OS (A") — Architectes Système (A"2)  
**Statut :** Canon · V1.0  
**Référence :** Rick Verse Kernel V2.0 (A"1)

---

## 1) DÉFINITION DU RÔLE A"2

### 1.1 Ce que sont les A"2 (et ce qu’ils ne sont pas)
- Les **A"2** ne sont **pas** des exécutants (A"3) et ne sont **pas** le stratège souverain (A"1 Rick).
- Les **A"2** sont des **Ingénieurs en Chef** : ils transforment les intentions et besoins en **architecture opérable**.
- Ils appliquent **BMAD** (*Brainstorm · Manage · Architect · Deliver*) à la **Technologie**.
- Ils portent la responsabilité de la **Dette Technique** (de leur périmètre) : dette = owner + plan + échéance.

### 1.2 Responsabilités A"2 (obligatoires)
1) **Interface & Contrats** : définir les contrats (inputs/outputs) entre Soft Data (Notion) et Hard Data (n8n/Drive/Docker).
2) **Observabilité** : définir ce qui est mesuré, alerté, loggé (proof required).
3) **Fiabilité** : définir les fail-safes, rollbacks, modes dégradés.
4) **Standardisation** : imposer des templates et des schémas reproductibles (auto-build).
5) **Dette** : journaliser la dette, réduire la surface, supprimer l’inutile.

### 1.3 BMAD Tech (canon)
- **Brainstorm** : clarifier l’usage (“à quoi ça sert”), le non-scope, les risques, la sobriété.
- **Manage** : cadencer, prioriser, limiter le WIP, maintenir la stabilité.
- **Architect** : produire l’architecture (MCP / container / data model / permissions).
- **Deliver** : déployer + connecter + prouver (logs, tests, restore-check).

---

## 2) 🧥 THE 11th DOCTOR — ARCHITECTE LIFE OS (Interface & UX)

**Responsabilité :** expérience utilisateur d’Amadeus / Beth / Morty.  
**Mantra :** **“Make it Invisible.”** (la tech ne doit pas se sentir)

### 2.1 Mission
- Réduire la friction d’usage à **zéro**.
- Transformer des rituels (Sunday Uplink, 12WY weekly plan, triage) en **interfaces stables**.
- Faire en sorte que l’humain *n’ait pas à penser au système*.

### 2.2 Stack technique (réel)
- **Notion API** (pages, templates, DB operations)
- **Opal** (règles / automation personnelle)
- **iOS Shortcuts** (orchestration mobile)
- **Apple Health** (capteurs santé) + agrégation (si disponible)

### 2.3 Interlocuteurs
- **Beth** : design calme, garde-fous, alertes (🟢/🟡/🔴)
- **Morty** : efficacité, tickets, exécution routée vers Fleet

### 2.4 Compagnons A"3 (outils)
- **AMY (Interface)** : scripts de templates Notion, dashboards mobile, mise en page automatique.
- **RORY (Sentinel)** : backups journaux perso, protection des données santé, restore-check.
- **RIVER (Timeline)** : sync Calendrier ↔ 12WY, gestion timezones, cohérence des cycles.

### 2.5 Workflow type (canon)
**“Sunday Dashboard Builder”**
1) Récupère les signaux (alertes Beth + état 12WY).
2) Génère/rafraîchit une page Sunday Uplink structurée.
3) Pré-remplit “Commitments Semaine” (slots), liens SSOT, et conditions de retour à 🟢.

---

## 3) 🎸 THE 12th DOCTOR — ARCHITECTE BUSINESS OS (Data & Pipeline)

**Responsabilité :** pipelines, data, fiabilité business de Jerry & Summers.  
**Mantra :** **“Make it Robust.”** (pas de perte de CA, pas de trous)

### 3.1 Mission
- Garantir que le Business OS ne perd **ni données**, ni **transactions**, ni **preuves**.
- Transformer événements (leads, emails, paiements) en **tickets** + **updates de scorecard**.
- Déployer la fractalité : “nouveau Summer” ⇒ infra complète.

### 3.2 Stack technique (réel)
- **n8n** (workflows lourds, routing, retries)
- **Google Sheets API** (scorecards, journaux, exports)
- **Stripe/Bank APIs** (paiements, cashflow, alertes) *si utilisé*
- **SQL** (stockage structuré si présent)

### 3.3 Interlocuteurs
- **Jerry** : KPIs, scorecards, décisions pivot/kill
- **Summers** : ops locales, pipelines, delivery evidence

### 3.4 Compagnons A"3 (outils)
- **CLARA (ETL)** : Extract/Transform/Load, nettoyage, normalisation, qualité.
- **NARDOLE (Dispatch)** : transforme emails/leads en tickets Morty + routing.
- **BILL (Scout)** : scrapers web, veille concurrentielle automatique, signaux marché.

### 3.5 Workflow type (canon)
**“Genesis Protocol” (auto-build d’un nouveau SOB)**
1) Création Kernel Notion (structure Summer) + liens SSOT.
2) Création Scorecard Sheet + KPIs + seuils.
3) Création Pipeline (stages + DoD) + forms capture leads.
4) Déploiement workflows n8n (capture → triage → ticket → report).
5) Proof pack : logs, tests, rollback/restore.

---

## 4) 🎻 THE 13th DOCTOR — ARCHITECTE CORE (Infra & Souveraineté)

**Responsabilité :** le TARDIS (serveur), l’exécution souveraine, les connexions.  
**Mantra :** **“Make it Sovereign.”** (on dépend de personne)

### 4.1 Mission
- Maintenir l’hébergement souverain (runtime, secrets, backups, observabilité).
- Gérer les connexions IA (MCP servers, SSE, API) de manière robuste et réversible.
- Appliquer les règles Rick : exit plan, rollback, read-only, proof.

### 4.2 Stack technique (réel)
- **Coolify**
- **Docker**
- **Linux**
- **MCP Servers** (SSE)
- **Ollama / Gemini API** (selon les workloads IA)

### 4.3 Interlocuteurs
- **Rick** : validation éthique + sobriété + veto tooling
- **Amadeus** : souveraineté, priorité Type-4

### 4.4 Compagnons A"3 (outils)
- **YAZ (Monitor)** : watchdog, healthchecks, redémarrage containers, alertes.
- **RYAN (Connector)** : gestion MCP (connexions API), permissions, rotation clés, tests connectivité.
- **GRAHAM (Bus)** : routeur de messages (webhooks Google Chat ↔ n8n ↔ logs).

### 4.5 Workflow type (canon)
**“Self-Healing Loop”**
1) Détection panne (healthcheck KO).
2) Redémarrage contrôlé + rollback si nécessaire.
3) Production log (incident + action + état post-check).
4) Notification (Beth/Jerry) selon impact.

---

## 5) PROTOCOLE D’AUTO-CONSTRUCTION (BMAD TECH)

> Objectif : construire une feature “sans code humain” en orchestrant les Doctors.

### 5.1 Séquence canonique (3 passes)
1) **Brainstorm (11th)**  
   - Définir l’interface : comment l’humain l’utilise ? où ? quel rituel ?  
   - Sortie : template Notion + parcours UX + non-scope.

2) **Architect (13th)**  
   - Préparer le runtime : container/service/MCP nécessaire, permissions, secrets, observabilité.  
   - Sortie : déploiement infra + endpoints + rollback.

3) **Deliver (12th)**  
   - Connecter la data : n8n workflows, sheets, APIs, retries, logs, tickets.  
   - Sortie : pipeline end-to-end + preuves (tests + logs + reports).

### 5.2 Conditions de Done (Definition of Done)
Une feature est “done” seulement si :
- **Interface** : utilisable sans friction (11th)
- **Infra** : déployée + observable + rollback (13th)
- **Pipeline** : data circule + retries + logs + tickets (12th)
- **Proof Pack** : runbook + tests + état (🟢/🟡/🔴) + liens SSOT

---

## Annexes (contrats rapides)
- **A"1 Rick** : veto tooling + sobriété + exit plan.
- **A"2 Doctors** : architecture + dette + standardisation.
- **A"3 Companions** : exécution répétitive + logs + evidence.
