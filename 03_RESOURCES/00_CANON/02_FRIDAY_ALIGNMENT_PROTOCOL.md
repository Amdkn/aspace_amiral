# 02_FRIDAY_ALIGNMENT_PROTOCOL — Audit de Souveraineté (30 min max)

> **Statut : CANON / Rituel**  
> **But :** Ce rituel ne sert pas à “faire des tâches”. Il sert à **AUDITER LA SOUVERAINETÉ**.  
> **Références :** `00_ASPACE_TRIPTYCH_CORE_V1.0.md` (S1–S3) + `01_AMADEUS_INTERNAL_IPBD.md` (I0–I3).  
> **Principe directeur :** *Construire une citadelle invisible. Zéro course de vitesse.*

---

## Pré‑requis (0 min — setup)
- Téléphone en **mode avion** ou **ne pas déranger**.
- Aucun onglet “travail” ouvert sauf :  
  1) Scorecards / Dashboards,  
  2) Liste des artefacts livrés,  
  3) Logs (si incident technique).
- Chronomètre : **30:00**.

---

# PHASE 1 — SAS DE DÉCOMPRESSION (I0 / IDENTITY) — 5 min

### Action
- Silence complet.
- Respiration lente. Aucune interaction.

### Question I0
> **“Suis‑je resté un Architecte cette semaine, ou ai‑je glissé en mode Technicien ?”**

### Check A0 (Seuil)
- **Si Technicien > 20% du temps** → **ALERTE ROUGE** (dérive de rôle).  
- Note unique : **pourquoi** (1 phrase max).  
  Exemple : “J’ai patché en urgence au lieu de designer.”

**Output Phase 1 :**
- `I0_Status = Architecte | Technicien`
- `Technician_Ratio ≈ __%` (estimation honnête)

---

# PHASE 2 — INSPECTION DES PANNEAUX (SCAN S3 → S2 → S1) — 15 min

> **Ordre non‑négociable :** Fondation d’abord, moteur ensuite, conscience enfin.

---

## 2.1 — SCAN FONDATION (S3 — TECH OS / RICK VERSE) — 5 min

### Question
> **“Le système a‑t‑il tenu la charge ? Y a‑t‑il de la dette technique ?”**

### Checks (A"2 — Doctors)
- **🟢 GREEN :** Tout est **documenté**, stable, idempotent.  
- **🟠 ORANGE :** Un script a planté **ou** une doc critique manque **ou** un contournement manuel a été fait.  
- **🔴 RED :** Intervention manuelle requise pour maintenir le système (échec de souveraineté).

### Indicateurs minimaux (à regarder, pas à discuter)
- Pannes / redémarrages / logs d’erreurs (Yaz / monitoring).  
- Backups : dernier backup OK ? (Rory).  
- Doc : un nouveau flux a‑t‑il été ajouté sans artefact associé ? (Loi de l’artefact).

**Output S3 :**
- `S3_Status = 🟢 | 🟠 | 🔴`
- `S3_Debt = None | Minor | Critical`
- `S3_OneFix = ____` (1 réparation prioritaire max)

---

## 2.2 — SCAN MOTEUR (S2 — BUSINESS PULSE) — 5 min

### Question
> **“Avons‑nous produit des Artefacts ou du Bruit ?”**

### Checks (A’2 — Justice League)
- **🟢 GREEN :** Artefacts livrés (Done) + Scorecard mise à jour.  
- **🟠 ORANGE :** Retard mais sous contrôle + dette visible.  
- **🔴 RED :** Accélération forcée / traction sans fondation (violation) **ou** production sans DoD.

### Critères d’audit (tranchants)
- Nombre d’artefacts **livrés** (pas “en cours”).  
- Scorecard : chiffres à jour (Cyborg).  
- Discipline : tickets clos avant Uplink (Captain / rythme).  
- Dérive : “activité” sans livraison = Bruit.

**Output S2 :**
- `S2_Status = 🟢 | 🟠 | 🔴`
- `Artefacts_Done = __`
- `Noise_Flags = __` (0–3)
- `S2_OneCut = ____` (1 scope cut max)

---

## 2.3 — SCAN CONSCIENCE (S1 — LIFE OS) — 5 min

### Question
> **“Mon niveau d’énergie (LD03) est‑il supérieur à lundi dernier ?”**

### Checks (A1 — Beth)
- **🟢 GREEN :** Alignement Ikigai + énergie stable/haute.  
- **🔴 RED :** Fatigue, rancœur, perte de sens, signaux corporels en baisse.

### Critères simples (sans mentalisation)
- Sommeil, tension, irritabilité, envie d’éviter.  
- Charge mentale : “je porte tout” = alerte.  
- Sens : “pourquoi je fais ça ?” devient flou = alerte.

**Output S1 :**
- `S1_Status = 🟢 | 🔴` (binaire par design)
- `LD03_Energy_Delta = + | = | -`
- `Beth_Veto = Yes | No`

---

# PHASE 3 — VERDICT (BMAD REVIEW) — 7 min

> L’Amiral ne débat pas. Il prononce.

## Conditions de verdict (strictes)

### MODE 🟢 VERT — **CONSTRUCTION**
- `S1 = 🟢` **et** `S3 = 🟢`  
- `S2` peut être 🟢 ou 🟠.

**Autorisation :**
- Jerry (A’1) peut accélérer **dans le cadre** (Rocks, tickets, DoD).

**Règle :**
- Un seul axe d’accélération, pas deux.

---

### MODE 🟠 ORANGE — **CONSOLIDATION**
- `S3 = 🟠` **ou** `S2 = 🟠`  
- `S1` doit rester 🟢.

**Interdictions :**
- Stop **intake**.  
- Pas de nouveaux projets.  
- Priorité : documentation, stabilisation, nettoyage.

**Règle :**
- Réparer la doc **avant** d’automatiser.

---

### MODE 🔴 ROUGE — **MAINTENANCE**
- `S1 = 🔴` **ou** `I0 Technicien > 20%` **ou** `S3 = 🔴`.

**Ordres immédiats :**
- Business en pause (S2 réduit au minimum vital).  
- Rick (S3) prend la main pour réduire la charge mentale et fiabiliser.  
- Morty applique le protocole “Minimum Viable Day”.

**Règle :**
- La souveraineté commence par le biologique.

---

**Output Phase 3 :**
- `Verdict = 🟢 Construction | 🟠 Consolidation | 🔴 Maintenance`
- `PrimaryConstraint = S1 | S2 | S3 | I0`

---

# PHASE 4 — TRANSMISSION (NEXT STEPS) — 3 min

## 4.1 — Ligne d’Intention (UNE SEULE)
L’Amiral écrit **UNE LIGNE** pour la semaine suivante.

**Format :**
- “Semaine __. __. __.”

**Exemples :**
- “Semaine S3. On stabilise n8n + backups. Jerry en pause.”  
- “Semaine S1. On récupère LD03. Zéro expansion.”  
- “Semaine S2. Un seul artefact Growth, DoD strict.”

## 4.2 — Priorité Absolue (North Star)
Cette ligne devient :
- la consigne A0,
- la contrainte de Beth (S1),
- la limitation de Jerry (S2),
- le backlog des Doctors (S3).

**Output Phase 4 :**
- `Weekly_Intention = "__________"`
- `OneDeliverable = ________` (optionnel, 1 artefact max)

---

## Appendix — Règles d’hygiène (non négociables)

1. **Pas de verdict sans scan S3→S2→S1.**  
2. **Pas d’accélération si Batman/Ops est en rouge** (et équivalent en S3).  
3. **Un seul scope cut** par semaine est obligatoire si 🟠 ou 🔴.  
4. **Le rituel est court** : si tu dépasses 30 minutes, tu dérives.

**Fin du canon.**
