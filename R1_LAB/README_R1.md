# 🧪 R1 LOCAL LAB (EXPERIMENTAL)

**Statut :** EXPERIMENTAL / SANDBOX
**Autorité :** Amadeus (A0)
**Promotion :** Sunday Uplink uniquement
**Cycle :** Rapide, Jetable, Sans Gilet

---

## 🎯 MISSION

> "Tout peut casser ici. Rien n'est critique."

Le Labo R1 est l'espace de créativité chaotique d'Amadeus. C'est ici que naissent les prototypes avant de demander leur *Citoyenneté* (Promotion vers R2) lors du **Sunday Uplink**.

---

## 🏗️ STRUCTURE

```text
R1_LAB/
├── workflows_experimental/  (Les brouillons n8n .json)
├── payloads/               (Les JSON de test A0→A"1)
├── logs/                   (Trace locale d'exécution)
└── README_R1.md            (Ce fichier)
```

---

## 📜 RÈGLES D'OR

1. **Zéro Prod :** On ne connecte JAMAIS R1 à la base de production S2.
2. **Local First :** Tout tourne sur la machine locale ou le container dev.
3. **Pas de Secrets :** Aucun mot de passe réel dans ces fichiers.
4. **Jetable :** Si on supprime ce dossier, le vaisseau A'Space doit continuer à voler.

---

## 🚀 CYCLE DE VIE D'UN ARTEFACT

1. **Incubation (Lundi-Samedi) :** Amadeus code, teste, casse en R1.
2. **Frozen (Dimanche matin) :** On fige une version candidate.
3. **Sunday Uplink :**
   - Amadeus présente le JSON au 13ème Doctor.
   - Le 13ème Doctor valide l'Idempotence et la Sécurité.
   - Si Valide -> Promotion vers `.agent/workflows/` (R2).
