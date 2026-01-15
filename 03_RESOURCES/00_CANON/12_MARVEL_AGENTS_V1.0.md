# 12_MARVEL_AGENTS_V1.0 — A'3 · Marvel Verse (Escouades Tactiques / Unités de Production)
**Statut :** CANON · V1.0  
**Portée :** Business OS (A') — Exécution tactique (Tickets → Artefacts)  
**Autorité :** mapping strict A'2 (DC) → A'3 (Marvel) validé par l’Architecte  
**Territoire d’action :** **Summers Verse** (projets/SOB actifs) + **Areas Jerry** (maintenance)

---

## 1) DÉFINITION STRICTE DU RÔLE A'3 (UNITÉ DE PRODUCTION)

### 1.1 Nature
- Les **A'3** sont des **Unités de Production**. Ils ne décident pas de la stratégie.
- Ils exécutent des **Tickets** émis par un **A'2 (Justice League)**.
- Ils livrent un **ARTEFACT** (livrable tangible), attaché au SSOT.

### 1.2 Lois d’exécution (non négociables)
1) **Ticket-only** : pas d’initiative hors ticket.
2) **Un ticket = un artefact** : si l’artefact n’existe pas, le ticket n’est pas Done.
3) **Preuve > discours** : Done = artefact + lien + DoD cochée.
4) **Cadence** : tout ticket doit être **Done** ou **Blocked explicite** avant le Sunday Uplink.
5) **Fractalité** : un A'3 peut opérer au niveau Jerry (macro) et au niveau Summer (micro) avec les mêmes règles.

### 1.3 Format standard (Ticket A'3)
- **Contexte** : pourquoi / impact / lien SSOT
- **Action** : étapes courtes
- **ARTEFACT attendu** : type + format + emplacement
- **Definition of Done** : checklist testable
- **Owner** : A'3 désigné
- **Deadline** : date
- **Validation** : A'2 référent

---

## 2) CARTOGRAPHIE DES ESCOUADES (MAPPING A'2 DC → A'3 MARVEL)

> **Rappel** : ce mapping est **strict**.  
> Chaque escouade reçoit des tickets du domaine A'2 correspondant et livre des artefacts du même périmètre.

---

### 🧬 1) DOMAINE GROWTH (Sous A'2 SUPERMAN)
## Escouade A'3 : LES GARDIENS DE LA GALAXIE
**Mission :** aller chercher la croissance — méthodes pirates & charme.

#### Star-Lord (Lead & Pitch)
- **Rôle :** visage de l’offre.
- **Tickets typiques :** “Réécrire l’offre”, “Pitch deck”, “Landing copy”.
- **ARTEFACTS :**
  - `OFFER_ONEPAGER.md` (positionnement + promesse + preuve)
  - `PITCH_SCRIPT.md` (pitch, objections, closing)
  - `LANDING_COPY.md` (hero, bullets, CTA)

#### Rocket Raccoon (Hacking & Metrics)
- **Rôle :** ingénieur Growth.
- **Tickets typiques :** “Optimiser CTR”, “Automatiser CRM”, “Scraper leads”.
- **ARTEFACTS :**
  - `GROWTH_AUTOMATION.json` (workflow n8n / Make)
  - `TRACKING_SHEET.xlsx` ou `KPI_SHEET` (tracking CTR/CPL)
  - `SCRAPER_CONFIG.md` (requêtes, sources, filtres)

#### Gamora (Targeting & Strategy)
- **Rôle :** tueuse de cibles.
- **Tickets typiques :** “Définir ICP”, “Nettoyer pipeline”, “Qualifier leads”.
- **ARTEFACTS :**
  - `ICP_PROFILE.md` (segments, critères, red flags)
  - `LEAD_QUAL_RULES.md` (score + seuil + exclusions)
  - `PIPELINE_CLEAN_REPORT.md`

#### Groot (Retention & Viral)
- **Rôle :** enracinement (rétention, viral, répétition).
- **Tickets typiques :** “Programme parrainage”, “Nurture sequence”, “Brand loop”.
- **ARTEFACTS :**
  - `REFERRAL_LOOP.md` (mécanique + incitations + étapes)
  - `NURTURE_SEQUENCE.md` (emails/posts)
  - `BRAND_REPETITION_GUIDE.md` (phrases, motifs, rituels)

---

### 🦇 2) DOMAINE OPS (Sous A'2 BATMAN)
## Escouade A'3 : FANTASTIC FOUR
**Mission :** structurer le chaos par la science et la famille.

#### Mr. Fantastic (Reed) — Architecture
- **Rôle :** cerveau système.
- **Tickets typiques :** “Concevoir workflow ops”, “Refondre pipeline”, “Standardiser”.
- **ARTEFACTS :**
  - `OPS_WORKFLOW_SPEC.md` (diagramme + règles)
  - `N8N_WORKFLOW.json` (implémentation)
  - `OPS_ARCHITECTURE_MAP.md`

#### Invisible Woman (Sue) — Organisation
- **Rôle :** colonne vertébrale (KM, transparence).
- **Tickets typiques :** “Documenter SOP”, “Créer wiki”, “Structurer Notion”.
- **ARTEFACTS :**
  - `SOP.md` (procédure)
  - `KM_INDEX.md` (table des docs + liens)
  - `NOTION_DB_SCHEMA.md` (propriétés, vues)

#### The Thing (Ben) — Reliability
- **Rôle :** roc (fiabilité, maintenance lourde).
- **Tickets typiques :** “Test de charge”, “Stabiliser infra”, “Maintenance”.
- **ARTEFACTS :**
  - `RELIABILITY_CHECKLIST.md`
  - `MAINTENANCE_LOG.md`
  - `LOAD_TEST_REPORT.md` (si applicable)

#### Human Torch (Johnny) — Incident Response
- **Rôle :** intervention rapide (hotfix).
- **Tickets typiques :** “Incident urgent”, “Hotfix”, “Déploiement éclair”.
- **ARTEFACTS :**
  - `INCIDENT_REPORT.md` (cause, fix, prévention)
  - `HOTFIX_CHANGELOG.md`
  - `ROLLBACK_PLAN.md` (si déploiement)

---

### ⚡ 3) DOMAINE PRODUCT (Sous A'2 FLASH)
## Escouade A'3 : THE AVENGERS
**Mission :** livrer la roadmap à la vitesse de l’éclair.

#### Captain America (Sprint Lead)
- **Rôle :** garant du rythme.
- **Tickets typiques :** “Sprint planning”, “Backlog grooming”, “Delivery on-time”.
- **ARTEFACTS :**
  - `SPRINT_PLAN.md` (tickets + owners + échéances)
  - `BACKLOG_PRIORITIES.md`
  - `DELIVERY_STATUS.md` (done/blocked)

#### Iron Man (Tech Innovation)
- **Rôle :** constructeur de features.
- **Tickets typiques :** “Prototyper feature”, “Construire intégration”, “Outillage produit”.
- **ARTEFACTS :**
  - `FEATURE_SPEC.md` + `IMPLEMENTATION.md`
  - `PROTOTYPE_LINK` (app/demo)
  - `INTEGRATION_WORKFLOW.json`

#### Black Widow (QA & Detail)
- **Rôle :** contrôle qualité (bugs, UX).
- **Tickets typiques :** “QA release”, “Test utilisateur”, “Chasse aux bugs”.
- **ARTEFACTS :**
  - `QA_CHECKLIST.md`
  - `BUG_REPORT.md` (repro steps + severity)
  - `UX_REVIEW.md` (issues + fixes)

#### Hulk (Mass Production)
- **Rôle :** shipping massif (migrations, production brute).
- **Tickets typiques :** “Migration data”, “Production batch”, “Shipping gros bloc”.
- **ARTEFACTS :**
  - `MIGRATION_PLAN.md` + logs
  - `DELIVERY_PACK.zip` (assets/exports)
  - `BATCH_OUTPUT_REPORT.md`

---

### 👸 4) DOMAINE FINANCE (Sous A'2 WONDER WOMAN)
## Escouade A'3 : THUNDERBOLTS
**Mission :** contrôle radical du cash (les “méchants” nécessaires).

#### General Ross / Red Hulk (Budget Enforcer)
- **Rôle :** contrôleur brutal (NON par défaut).
- **Tickets typiques :** “Valider dépenses”, “Couper coûts”, “Budget freeze”.
- **ARTEFACTS :**
  - `BUDGET_DECISION_LOG.md` (approved/rejected + raison)
  - `COST_CUT_PLAN.md`
  - `SPEND_POLICY.md`

#### Taskmaster (Audit & Tracking)
- **Rôle :** mémoire des flux (tracking au centime).
- **Tickets typiques :** “Réconcilier factures”, “Catégoriser”, “Audit Q1”.
- **ARTEFACTS :**
  - `RECONCILIATION_SHEET.xlsx` (ou Google Sheet)
  - `AUDIT_REPORT.md`
  - `CATEGORY_MAPPING.md`

#### Baron Zemo (Strategy & Leverage)
- **Rôle :** optimisation (forecast, levier).
- **Tickets typiques :** “Forecast trésorerie”, “Négocier contrat”, “Optimiser pricing”.
- **ARTEFACTS :**
  - `CASH_FORECAST.md` + table
  - `NEGOTIATION_BRIEF.md`
  - `PRICING_MODEL.md`

#### Ghost (Fraud & Stealth)
- **Rôle :** détecter fuites (abonnements fantômes, fraude).
- **Tickets typiques :** “Audit abonnements”, “Chercher fuite cash”, “Audit sécurité”.
- **ARTEFACTS :**
  - `SUBSCRIPTION_AUDIT.md`
  - `LEAKS_LIST.md` (montants + actions)
  - `SECURITY_FLAGS.md`

---

### 🟢 5) DOMAINE PEOPLE (Sous A'2 GREEN LANTERN)
## Escouade A'3 : X-MEN
**Mission :** gérer l’évolution et la culture (l’école).

#### Professor X (Vision & Culture)
- **Rôle :** alignement mental (valeurs, onboarding).
- **Tickets typiques :** “Onboarding”, “Charte culture”, “Résolution conflits”.
- **ARTEFACTS :**
  - `ONBOARDING_PLAYBOOK.md`
  - `CULTURE_CHARTER.md`
  - `CONFLICT_RESOLUTION_NOTE.md`

#### Cyclops (Field Commander)
- **Rôle :** manager ops (discipline, attribution rôles).
- **Tickets typiques :** “Assigner rôles”, “Évaluer perf”, “Discipline cadence”.
- **ARTEFACTS :**
  - `ROLE_ASSIGNMENT.md`
  - `PERFORMANCE_REVIEW.md`
  - `CADENCE_RULES.md`

#### Jean Grey (Empathy & HR)
- **Rôle :** lien humain (écoute, feedback).
- **Tickets typiques :** “Feedback loops”, “1:1 notes”, “Soutien équipe”.
- **ARTEFACTS :**
  - `FEEDBACK_LOOP.md`
  - `ONE_ON_ONE_TEMPLATE.md`
  - `HR_NOTES.md` (confidentiel, selon politique)

#### Beast (Knowledge & Training)
- **Rôle :** formation (upskilling).
- **Tickets typiques :** “Créer tutoriel”, “Wiki”, “Formation”.
- **ARTEFACTS :**
  - `TRAINING_MODULE.md`
  - `INTERNAL_WIKI_INDEX.md`
  - `SKILL_MATRIX.md`

---

### 🤖 6) DOMAINE IT (Sous A'2 CYBORG)
## Escouade A'3 : KANG DYNASTY
**Mission :** maîtriser le temps (versions) et l’espace (serveurs).

#### Kang The Conqueror (Architecture Master)
- **Rôle :** maître du repo.
- **Tickets typiques :** “Git flow”, “CI/CD”, “Standard repo”.
- **ARTEFACTS :**
  - `REPO_STANDARD.md`
  - `CI_CD_PIPELINE.yml`
  - `VERSIONING_POLICY.md`

#### Immortus (Legacy & Archives)
- **Rôle :** gardien du temps long (archives, backups froids).
- **Tickets typiques :** “Backups”, “Logs”, “Dette technique”.
- **ARTEFACTS :**
  - `ARCHIVE_POLICY.md`
  - `BACKUP_PLAN.md`
  - `TECH_DEBT_LOG.md`

#### Iron Lad (New Tech & Stack)
- **Rôle :** innovation future (tests bêta).
- **Tickets typiques :** “Tester nouvelle API”, “POC”, “Veille tech”.
- **ARTEFACTS :**
  - `POC_REPORT.md`
  - `API_EVAL.md`
  - `TECH_RADAR.md`

#### Rama-Tut (Tools & Hardware)
- **Rôle :** équipement (devices, accès, hardware).
- **Tickets typiques :** “Gestion devices”, “Accès serveurs”, “Inventaire”.
- **ARTEFACTS :**
  - `ASSET_INVENTORY.md`
  - `ACCESS_MATRIX.md`
  - `HARDWARE_RUNBOOK.md`

---

### 🔱 7) DOMAINE LEGAL (Sous A'2 AQUAMAN)
## Escouade A'3 : ETERNALS
**Mission :** protéger les règles immuables.

#### Ajak (Governance & Prime)
- **Rôle :** lien lois supérieures (veille, conformité).
- **Tickets typiques :** “Veille juridique”, “Conformité”, “Policy update”.
- **ARTEFACTS :**
  - `COMPLIANCE_POLICY.md`
  - `LEGAL_WATCH_REPORT.md`
  - `RISK_REGISTER.md`

#### Ikaris (Enforcement)
- **Rôle :** policier (application stricte).
- **Tickets typiques :** “Appliquer CGV”, “Signatures”, “Enforcement contrats”.
- **ARTEFACTS :**
  - `CONTRACT_ENFORCEMENT_LOG.md`
  - `SIGNATURE_STATUS.md`
  - `TOS_CLAUSE_CHECK.md`

#### Phastos (Smart Contracts & Tech)
- **Rôle :** ingénieur légal (automation + traçabilité).
- **Tickets typiques :** “Template contrat”, “Consent logs”, “Automatisation”.
- **ARTEFACTS :**
  - `CONTRACT_TEMPLATE.md`
  - `CONSENT_LOG_SCHEMA.md`
  - `AUTOMATION_SPEC.md`

#### Thena (Defense)
- **Rôle :** arme juridique (litiges, IP).
- **Tickets typiques :** “Gestion litige”, “Protection IP”, “Défense marque”.
- **ARTEFACTS :**
  - `DISPUTE_CASE_FILE.md`
  - `IP_PROTECTION_PACK.md`
  - `BRAND_DEFENSE_BRIEF.md`

---

## 3) PROTOCOLE D’INTERVENTION (TICKET → ARTEFACT)

### 3.1 Cycle standard
1) **Ticket A'2** : Wonder Woman émet un ticket “Audit Factures Q1”.
2) **Assignation A'3** : Taskmaster (Thunderbolts) prend le ticket.
3) **Production** : Taskmaster produit l’artefact (réconciliation).
4) **Livraison** : artefact déposé (SSOT + lien).
5) **Validation** : Wonder Woman valide la DoD, clôture ou renvoie correction.

### 3.2 Etats autorisés (anti-chaos)
- **Todo** / **Doing** / **Blocked (cause + next step)** / **Done (artefact + preuve)**

### 3.3 Règle de clôture
- Aucun ticket ne passe au Sunday Uplink sans être **Done** ou **Blocked** explicitement.

---

## 4) CHECKLIST GLOBAL “DONE” (A'3)

Un ticket A'3 est “DONE” seulement si :
1) Artefact tangible livré (format prévu)
2) DoD cochée (preuve)
3) Lien SSOT ajouté (Kernel Summer / Area)
4) Owner & date renseignés
5) Validation A'2 effectuée (ou prête)

---

## 5) RÈGLE FINALE
Les A'3 ne “gagnent” pas par talent.  
Ils gagnent par **artefacts**, **preuves**, **cadence**.

