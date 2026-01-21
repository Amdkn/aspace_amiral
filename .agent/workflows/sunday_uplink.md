---
description: Exécute le rituel de gouvernance hebdomadaire (Audit R1 -> Promotion R2).
---

# RITUEL SUNDAY UPLINK

Cet agent va guider la promotion du code du Labo (R1) vers la Citadelle (R2).

## Étape 1 : Audit du Labo (R1)
1.  Scanner le dossier `R1_LAB/workflows_experimental/`.
2.  Pour chaque fichier modifié cette semaine :
    * Vérifier s'il respecte la **Loi d'Idempotence**.
    * Demander à l'utilisateur : "Ce workflow est-il prêt pour la Citadelle ?"

## Étape 2 : Promotion Vers la Citadelle (R2)
1.  Si validé, copier le fichier vers `R2_CITADEL/workflows_stable/`.
2.  Ajouter une entrée dans `CHANGELOG.md` avec le tag `[UPLINK-PROMOTION]`.
3.  Générer un hash SHA-256 du fichier pour sceller la version.

## Étape 3 : Rapport du 13ème Docteur
1.  Analyser l'état de santé des services critiques (n8n, VPS).
2.  Générer un résumé : "État du Kernel : [STABLE/INSTABLE]".
3.  Demander la fermeture de la session : "Rick, publie le Sunday Uplink."
