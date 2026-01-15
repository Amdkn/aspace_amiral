# 15_COMPANIONS_AGENTS_V1.0 — A"3 · The Companions (Executants)
**Portée :** Tech OS (A") · Exécution logicielle (n8n / scripts / daemons)  
**Statut :** Canon · V1.0  
**But :** rendre l’infrastructure **exécutable 24/7** sans intervention humaine.

---

## 1) DÉFINITION DU RÔLE A"3 (L’OUVRIER)

### 1.1 Nature
Un **A"3** est un **exécutant** : workflow n8n, script, daemon, healthcheck, worker.

### 1.2 Lois (non négociables)
1) **Zéro autonomie décisionnelle**  
   - Un A"3 exécute un plan défini par un **A"2 Doctor**.
   - Toute ambiguïté ⇒ **Error** (pas “d’interprétation”).

2) **Idempotence** (relance-safe)  
   - L’A"3 **vérifie avant d’écrire** (existence, checksum, last_updated, version, hash).
   - Il utilise un **Idempotency Key** (ex: `source_id + event_type + date_bucket`).

3) **Silence opérationnel**  
   - Il ne “parle” que sur **Done** (succès prouvé) ou **Error** (échec explicite).
   - Les logs sont complets, mais la notification est minimale.

4) **Artefact Rule**  
   - Pas d’automatisation sans documentation : **runbook + rollback + preuve**.

5) **Sécurité**  
   - Secrets via vault / env variables, jamais en clair.
   - Permissions minimales (principle of least privilege).

### 1.3 Contrat Standard (tous les A"3)
Chaque Compagnon doit fournir :
- **Owner (Doctor)** : 11th / 12th / 13th  
- **Nature** : n8n / script / daemon  
- **Trigger** : webhook / schedule / event  
- **Inputs** : payload + sources  
- **Outputs** : artefacts + logs + notifications  
- **Idempotency Key** : règle explicite  
- **Retries** : politique (max / backoff)  
- **Fail-safe** : mode dégradé + DLQ (Donna)  
- **Proof** : “Done evidence” (lien + log + état)

---

## 2) CLUSTER LIFE TECH (Sous le 11th Doctor)
**Objectif :** *Fluidité Invisible.*  
**Périmètre :** Beth/Morty/Fleet, Notion UX, santé, calendrier.

---

### 👱‍♀️ AMY — Interface & Templates
- **Owner (A"2) :** 11th Doctor
- **Nature :** **n8n workflow** + **Notion API**
- **Triggers :**
  - **Webhook** (bouton Notion / request “Build Sunday Dashboard”)
  - **Schedule** (Dimanche matin, horaire local)
- **Fonction :**
  1) Générer / rafraîchir les pages “Dashboard” (Beth / Sunday Uplink / Weekly Plan placeholders)
  2) Appliquer des **templates** (properties, sections, liens SSOT)
  3) Préparer les **vues** (filters/sorts) si gérées via DB
- **Inputs :**
  - `request_type` (ex: `SUNDAY_DASHBOARD`)
  - `week_id` (ex: `Q1-2026-W03`)
  - `notion_page_id` / `db_id`
- **Outputs (artefacts) :**
  - Page Notion créée/mise à jour
  - Log d’exécution + liens des pages
- **Idempotence :**
  - Key = `week_id + request_type`
  - Si page existe → update **diff-only** (pas de duplication)
- **Retries / backoff :**
  - 3 retries, backoff exponentiel (ex: 5s / 20s / 60s)
- **Fail-safe :**
  - Si Notion API timeout → retries puis **Error** (DLQ Donna) sans bloquer le reste du système
- **Done evidence :**
  - Lien page + timestamp + diff summary (champs modifiés)

---

### 🛡️ RORY — The Sentinel (Backups & Privacy)
- **Owner (A"2) :** 11th Doctor
- **Nature :** **Script Bash** + **Restic** + **Docker volumes**
- **Trigger :** **Cron** quotidien 04:00 (timezone serveur)
- **Fonction :**
  1) Backup incrémental des bases critiques (exports Notion, logs, fichiers kernel, dumps SQL si présent)
  2) Chiffrement (repos Restic) + rotation
  3) Test de restauration (échantillon) 1×/semaine
- **Inputs :**
  - chemins volumes (`/srv/aspace/...`)
  - credentials Restic (env)
  - policy rotation (daily/weekly/monthly)
- **Outputs :**
  - Snapshot Restic + rapport “backup status”
  - Hash / taille / durée / erreurs
- **Idempotence :**
  - Restic est incrémental → relance-safe
  - Key = `backup_job + date_bucket`
- **Fail-safe :**
  - Si backup échoue → tentative 1 relance + **Error** + DLQ Donna
  - Si restore-check échoue → alerte **critique** (risque souveraineté)
- **Mantra :** **« Le Centurion attend. »**
- **Done evidence :**
  - Snapshot ID + restore-check result (OK/KO)

---

### 🌀 RIVER — Time & Sync (Calendar ↔ 12WY)
- **Owner (A"2) :** 11th Doctor
- **Nature :** **n8n workflow** (Google Calendar ↔ Notion 12WY)
- **Triggers :**
  - Event Calendar create/update
  - Notion update (Rocks / weekly commitments)
- **Fonction :**
  1) Vérifier que chaque Rock 12WY a des créneaux dans l’agenda
  2) Détecter conflits (overbooking, timezone mismatch, absence de blocs)
  3) Proposer/Créer des blocs “Focus” (si autorisé) ou remonter une alerte
- **Inputs :**
  - `rock_id`, `week_id`, `timezone`
  - événements Calendar (start/end/title)
- **Outputs :**
  - Alignement “Rock → Time Blocks”
  - Rapport de conflit + lien vers l’événement
- **Idempotence :**
  - Key = `rock_id + week_id`
  - Ne crée pas de doublons : compare `event_tag` + time range
- **Fail-safe :**
  - Si API Calendar rate-limit → backoff + DLQ Donna si dépassement
- **Done evidence :**
  - Table “Rocks scheduled %” + conflits listés

---

## 3) CLUSTER BUSINESS TECH (Sous le 12th Doctor)
**Objectif :** *Robustesse Data.*  
**Périmètre :** pipelines business, scorecards Jerry, tickets, veille.

---

### 🍪 CLARA — The Impossible ETL
- **Owner (A"2) :** 12th Doctor
- **Nature :** **n8n workflow complexe** (Data Transformation)
- **Triggers :**
  - Arrivée de donnée brute : email Stripe, CSV, webform, webhook
  - Schedule (reconcile daily)
- **Fonction :**
  1) Extraire la donnée brute
  2) Nettoyer / normaliser (dates, devises, noms, IDs)
  3) Calculer métriques (sommes, MRR, ARPA, churn si applicable)
  4) Injecter dans la **Scorecard** (Google Sheet / SQL)
  5) Réconcilier les “splinters” (fragments dispersés) → unifier
- **Inputs :**
  - `source_system` (stripe/bank/form/csv)
  - payload brut
  - mapping rules (versionnées)
- **Outputs :**
  - lignes propres dans Sheet/DB
  - rapport “ETL batch”
- **Idempotence :**
  - Key = `source_id (txn_id/email_id) + normalized_date`
  - Write en mode **upsert** (pas insert aveugle)
- **Fail-safe :**
  - Si payload invalide → DLQ Donna (payload + cause)
  - Si injection échoue → rollback logique (mark as pending) + retry
- **Done evidence :**
  - Nombre d’enregistrements traités + erreurs + lien vers batch log

---

### 🤖 NARDOLE — Dispatch & Ticketing
- **Owner (A"2) :** 12th Doctor
- **Nature :** **n8n logic router**
- **Trigger :** décision Jerry/Summer (nouveau Rock, nouveau besoin, incident)
- **Fonction :**
  1) Transformer une “intention opérationnelle” en **tickets atomiques** pour Morty
  2) Vérifier un ticket : owner + deadline + DoD + lien SSOT
  3) Router vers le bon canal (Notion DB tickets / email / chat)
- **Inputs :**
  - `initiative_id` / `rock_id`
  - contexte (SSOT links)
  - exigences DoD
- **Outputs :**
  - ticket(s) créés + lien(s)
  - résumé dispatch “N tickets created”
- **Idempotence :**
  - Key = `initiative_id + ticket_type + week_id`
  - Dédoublonnage sur title + DoD hash
- **Fail-safe :**
  - Si ticket incomplet → Error + DLQ Donna (reason: missing fields)
  - Ne crée rien si validations KO
- **Done evidence :**
  - Liste liens tickets + champs validés (owner/deadline/DoD)

---

### 🎓 BILL — The Explorer (Research & Scout)
- **Owner (A"2) :** 12th Doctor
- **Nature :** **MCP Brave Search** / **Scraper (Puppeteer)** (selon autorisations)
- **Trigger :**
  - demande de veille (Jerry/Summer)
  - phase Brainstorm (BMAD)
- **Fonction :**
  1) Collecter infos web (concurrence, prix, tendances, opportunités)
  2) Résumer en “Research Pack” (sources + points clés + risques)
  3) Déposer dans “Resources” du projet (Drive/Notion) + lien
- **Inputs :**
  - requêtes, mots clés, contraintes (geo, industrie)
  - “what to decide” (question à trancher)
- **Outputs :**
  - Research Pack (doc) + citations/URLs (si autorisé)
- **Idempotence :**
  - Key = `query_hash + date_bucket`
  - Ne republie pas si même pack existe dans la fenêtre
- **Fail-safe :**
  - Si scraping bloqué → fallback search-only + note limitation
  - Si sources insuffisantes → Error + DLQ Donna (reason: low confidence)
- **Done evidence :**
  - Lien du pack + date + sources count

---

## 4) CLUSTER CORE INFRA (Sous le 13th Doctor)
**Objectif :** *Souveraineté & TARDIS.*  
**Périmètre :** runtime, monitoring, MCP, message bus.

---

### 👮‍♀️ YAZ — System Monitor
- **Owner (A"2) :** 13th Doctor
- **Nature :** **Docker healthchecks** + **Uptime Kuma** (ou équivalent) + webhooks
- **Trigger :** continu (polling / event)
- **Fonction :**
  1) Vérifier disponibilité (Coolify, containers critiques, endpoints MCP)
  2) Si KO → tentative restart contrôlée
  3) Si échec → escalade (notification urgente) + log incident
- **Inputs :**
  - liste services + endpoints + SLA
- **Outputs :**
  - statut (🟢/🟡/🔴) + incident log
- **Idempotence :**
  - restart protégé : lock “restart_in_progress”
  - Key = `service_id + incident_window`
- **Fail-safe :**
  - Si redémarrages répétitifs → stop loop + alerte critique (risque de thrash)
- **Done evidence :**
  - uptime report + incident timeline + action taken

---

### 🔧 RYAN — The Mechanic (MCP)
- **Owner (A"2) :** 13th Doctor
- **Nature :** **MCP Server(s)** (Model Context Protocol) + connecteurs locaux
- **Trigger :** appel d’Amadeus/Rick/Doctors
- **Fonction :**
  1) Fournir les “mains” à l’IA : filesystem, Drive, APIs locales
  2) Gérer permissions, tokens, rotation clés
  3) Exécuter des actions outillées (dans les limites de policy)
- **Inputs :**
  - requêtes MCP
  - scopes autorisés
- **Outputs :**
  - résultat d’action + logs
- **Idempotence :**
  - opérations “write” exigent pre-check (exists/hash/version)
  - Key = `action_id + target_id`
- **Fail-safe :**
  - si permission insuffisante → refuse (Error) + trace claire
  - si dépendance KO → renvoie status “degraded”
- **Done evidence :**
  - action result + target snapshot (before/after hash)

---

### 🚌 GRAHAM — The Driver (Bus)
- **Owner (A"2) :** 13th Doctor
- **Nature :** **Webhook dispatcher** / **Queue** (Redis ou équivalent)
- **Trigger :** tout message interne (events)
- **Fonction :**
  1) transporter messages entre modules (n8n ↔ chat ↔ logs ↔ Notion)
  2) garantir livraison (ack/retry)
  3) journaliser le trajet (trace)
- **Inputs :**
  - payload + destination + priority
- **Outputs :**
  - message livré + trace ID
- **Idempotence :**
  - Key = `message_id`
  - dédoublonnage si replay
- **Fail-safe :**
  - si destination indisponible → DLQ Donna + retry schedule
- **Done evidence :**
  - trace ID + ack destination + latency

---

## 5) PROTOCOLE D’ERREUR (DEAD LETTER QUEUE — DONNA)

> Donna = table / base d’erreurs. **Tout crash doit atterrir dans Donna** avec le payload.

### 5.1 Règles DLQ
Si un Compagnon plante (erreur fatale) :
1) Il **n’éteint pas** le système (pas de cascade).
2) Il envoie le payload + contexte + cause à **Donna** (DLQ).
3) Il se met en **pause** (ou “degraded”) et **notifie** le Doctor référent.

### 5.2 Schéma minimal Donna (recommandé)
- `error_id` (uuid)
- `companion_name`
- `owner_doctor`
- `timestamp`
- `severity` (warn/error/critical)
- `idempotency_key`
- `payload_raw` (ou pointer vers stockage)
- `cause`
- `retry_count`
- `next_action` (human/doctor/auto)

### 5.3 Politique de reprise
- **Auto-retry** si cause transitoire (timeout, rate limit) : max 3
- **Pause + escalade** si cause structurelle (schema mismatch, permission denied, corruption)

---

## Annexes — Format n8n (prêt à traduire)
Pour chaque workflow n8n, mapper :
- **Trigger Node** : webhook / schedule / event
- **Idempotency Guard** : lookup (Notion/Sheet/DB) + hash compare
- **Core Logic** : transform / route / create
- **Error Branch** : push → Donna + notify Doctor
- **Done Branch** : proof pack + minimal notify

