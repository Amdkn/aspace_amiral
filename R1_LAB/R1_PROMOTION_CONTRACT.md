# 📜 R1 → R2 PROMOTION CONTRACT

**Source :** R1 (Labo Local)
**Promoteur :** Amadeus (A0)
**Destinataire :** 13th Doctor (A"1) - Kernel Guardian
**Canal :** Sunday Uplink uniquement

---

## 🏁 CRITÈRES D'ACCEPTATION (DEFINITION OF DONE)

Pour qu'un artefact (Workflow n8n, Script, Agent) puisse passer de **R1 (Experimental)** à **R2 (Canonical)**, il doit valider **100%** de ces points :

### 1. IDEMPOTENCE 🔄
- [ ] Le script peut être lancé 10 fois de suite sans créer 10 doublons.
- [ ] Il gère le cas "Déjà existant".

### 2. SÉCURITÉ & SECRETS 🔒
- [ ] AUCUN secret hardcodé dans le JSON/Code.
- [ ] Utilise exclusivement les variables d'env ou les Credentials n8n.
- [ ] Pas d'accès root nécessaire.

### 3. OBSERVABILITÉ 👁️
- [ ] Loggue son démarrage.
- [ ] Loggue sa fin (Succès/Échec).
- [ ] Utilise le format de log standard du Kernel.

### 4. ISOLATION 🧱
- [ ] Ne brise pas les frontières Life/Business/Kernel.
- [ ] Si c'est un outil Business, il ne touche pas au Kernel.

---

## 📝 TEMPLATE DE DEMANDE DE PROMOTION

*(À remplir lors du Sunday Uplink)*

```markdown
**Artefact :** `nom_du_fichier.json`
**Type :** Workflow / Agent / Script
**Intention :** (Pourquoi on ajoute ça ?)
**Preuve de Test R1 :** (Lien vers le log de succès local)
**Risque estimé :** Faible / Moyen / Critique
```

---

> "Si le Kernel devient visible, il est déjà trop tard."
> -- Rick (R0)
