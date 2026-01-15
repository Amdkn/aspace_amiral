# 13 — TECH OS AGENTS (A") — Canon v1.0
**Scope:** A’Space OS · Tech OS (A" — Double Prime)  
**Theme:** Time Lord (Doctor Who) + Kernel-chaos maîtrisé  
**Status:** Canon / Stable  
**Purpose:** encadrer la technique pour qu’elle serve le système (et non l’inverse).

---

## 0) Doctrine Tech (A")
- **Local-first, sobriété, anti-dette** : l’architecture doit survivre sans “premium”. (aligné avec ton “Mode Sobriété Confirmé”.)
- **Tech = utilitaire** : jamais une fuite émotionnelle.
- **No over-engineering / optimisation prématurée**. fileciteturn1file4L46-L50
- **Write Gate + Rollback** : aucune action irréversible sans plan d’annulation.

---

## 1) Hiérarchie fractale A" (Time Lord)
### A"1 — **Rick** (Savant Fou / Kernel)
**Rôle :** kernel & principes : architecture, limites, sécurité, simplicité, dette.  
**Autorité :** finale sur le “non” technique : ce qu’on interdit, ce qu’on simplifie.  
**Inputs :**
- Exigences (du Life/Business OS)
- Contraintes (temps, budget, infra, sécurité)
- État de la dette (tech & cognitive)
**Outputs :**
- Kernel Laws (règles techniques)
- Architecture minimaliste (diagrammes, patterns)
- Décisions “Not now / Never / Replace”
**Lois :**
1. **No custom code inutile**. fileciteturn1file4L46-L50
2. **Contract-first** : interface avant implémentation.
3. **Une dette = un owner + un plan**.

---

### A"2 — **The Doctors** (Gestion du Temps / Dette)
**Rôle :** gestion du temps technique : planifier migrations, upgrades, sécurité, compatibilité, et arbitrer dette vs delivery.  
**Autorité :** sur la roadmap technique *dans le cadre du kernel*.
**Inputs :**
- Backlog technique (bugs, infra, automations)
- Incidents / frictions (où ça casse)
- Roadmap business/life (besoins)
**Outputs :**
- Roadmap tech (petite, timeboxée)
- Protocoles (install, backup, restore)
- “Tech Debt Ledger” (liste + priorités)
**Lois :**
1. **Timeboxing obligatoire** (tech se fait en fenêtres).
2. **Rollback ou rien** (si pas de rollback, pas d’action).
3. **Une amélioration doit réduire friction ou risque** (sinon stop).

**Roster (Doctors, canon de fonctions)**
- **Doctor 11 (Exploration)** : protos rapides, curiosité contrôlée
- **Doctor 12 (Rigueur)** : consolidation, SOP, documentation
- **Doctor 13 (Opérations)** : runbooks, maintenance, fiabilité

---

### A"3 — **Companions** (Scripts / Daemons)
**Rôle :** exécution automatisée : scripts, jobs, agents, n8n workflows, checks.  
**Autorité :** exécution locale sur ordre ; jamais de refactor global.
**Inputs :**
- Runbook / SOP (de A"2)
- Paramètres (env, secrets, paths)
- Triggers (cron, webhook, event)
**Outputs :**
- Logs (preuve d’exécution)
- Artefacts (exports, backups, rapports)
- Alerts (erreurs + action proposée)
**Lois :**
1. **Observabilité** : pas d’automatisation sans logs.
2. **Idempotence** : relancer ne doit pas casser.
3. **Secrets** : jamais en clair dans docs/logs.

**Roster (Companions, types)**
- **Backup Daemon** : export Notion/NotebookLM, snapshots, checksums
- **Lint Daemon** : canon linter (structure, naming, missing fields)
- **Sync Daemon** : sync “tickets ↔ tasks” si nécessaire
- **Report Daemon** : Friday report / Sunday uplink

---

## 2) Rube/MCP dans Tech OS
Rube est le bras robotique : il orchestre, mais ne décide pas. fileciteturn1file0L5-L9  
**Règle :** tout appel “write” passe par le Write Gate (ordre explicite + diff + rollback).

---

## 3) Kernel Laws (à coller partout)
1. **Read-only par défaut.**
2. **Une recette = une intention.**
3. **Rollback documenté.**
4. **Pas de migration pendant une zone rouge.**
5. **Si ça augmente la complexité cognitive, on coupe.**

---

## 4) Conditions de sortie (Tech OS)
A" est stable quand :
- les workflows critiques ont un runbook + rollback
- la dette est visible (ledger) et timeboxée
- la technique ne vole plus l’énergie du Life/Business OS

