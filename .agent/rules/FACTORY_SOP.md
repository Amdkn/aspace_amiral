# 🏭 FACTORY SOP - PROTOCOLE DE FABRICATION S3

Ce protocole définit comment le Rick Verse auto-construit ses propres capacités (Skills).

## 1. GOUVERNANCE SÉQUENTIELLE
Tout nouveau Skill (Capability) doit passer par la "Factory of Factories" :
1. **CONDUCTOR** : Créer une Track dédiée pour la traçabilité.
2. **BMAD** : Découper l'implémentation en phases (B -> M -> A -> D).
3. **RALPH** : Utiliser des boucles de feedback pour valider le code jusqu'à la perfection technique.

## 2. STANDARDS DE SORTIE (ARTIFACTS)
Un Skill n'est considéré comme "LIVRÉ" que s'il contient :
- `SKILL.md` : Documentation exhaustive et interactive.
- `scripts/` : Outils d'exécution associés (le cas échéant).
- `tests/` : Validation Rick Verse de bon fonctionnement.

## 3. RÈGLE D'OR (ANTI-DETTE)
Il est strictement interdit de créer des Skills "ad-hoc" ou manuels sans passer par le processus Track. Ralph doit vérifier l'idempotence et la propreté du code avant l'indexation finale dans le Nexus.
