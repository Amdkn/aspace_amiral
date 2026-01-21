# SECURITY_R0 — Protocoles de Verrouillage & Souveraineté

Ce document définit les mécanismes d'arrêt d'urgence et de verrouillage du système A'Space OS au niveau R0 (Local).

## 1. LE VETO DE BETH (LIFE OS)
Le Veto est déclenché par l'agent Beth (A1) via les signaux S1.

### 1.1 États de Verrouillage
- **🟢 GREEN (Normal)** : Exécution nominale autorisée.
- **🟡 YELLOW (Slowdown)** : 
    - Interdiction de lancer de nouvelles initiatives (`01_PROJECTS`).
    - Ralentissement des boucles d'exécution.
    - Notification prioritaire à l'Amiral.
- **🔴 RED (Halt)** :
    - Arrêt immédiat de tous les workflows S2 (Jerry/Business).
    - Gel des déploiements R1/R2.
    - Désactivation des accès API non-essentiels.

### 1.2 Protocole d'Arrêt d'Urgence (Emergency Stop)
En cas de signal S1 🔴 :
1. **Detection** : n8n identifie un dépassement de seuil critique (Capacité LD03 ou Ikigai LD00).
2. **Lockdown** : Mise à jour de `governance_state` dans Supabase à `status = 'RED'`.
3. **Notification** : Alerte sonore/visuelle sur R0 et notification chiffrée.
4. **Intervention** : Seul l'Amiral (A0) peut lever le verrou via une commande manuelle.

## 2. GOUVERNANCE DES VARIABLES D'ENVIRONNEMENT
- **Règle de Fer** : Aucune clé secrète ne doit être commitée dans le repo Git.
- **Stockage** : Utilisation exclusive de fichiers `.env` locaux (non-trackés) et du coffre-fort de credentials n8n.
- **Audit** : Tout changement manuel des variables doit être signalé au Conductor.

## 3. PROCÉDURE DE RÉINITIALISATION (RESET)
Pour lever un verrou 🔴 :
1. Analyse de la cause racine via Rick (Audit).
2. Correction du désalignement.
3. Commande : `Update governance_state set status = 'GREEN' where active = true;`
