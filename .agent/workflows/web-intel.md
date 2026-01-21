---
description: Workflow BMad pour l'Intelligence Web et le Scraping Autonome (TOOL NEUTRE).
---

# MISSION : WEB INTEL (BMad Loop)
Objectif : Récupérer des données ou agir sur le web.
STATUT : Outil Infra (S3). Toujours disponible.

## 🔵 PHASE 1 : BRAINSTORM (Définition de Cible)
1. Analyse la demande de l'Amiral.
2. Identifie l'URL cible et le sélecteur CSS/XPath probable.

## 🟣 PHASE 2 : MODEL (Cartographie)
1. Lance l'agent Chrome sur l'URL (Mode Headless par défaut selon `@.agent/rules/NAVIGATOR_PROTOCOL.md`).
2. **Action :** Scan la structure de la page (DOM).

## 🟠 PHASE 3 : ACT (Exécution)
1. Exécute la séquence d'actions.
2. **Sécurité Technique :** Vérifie l'URL (Phishing Check) mais NE BLOQUE PAS sur le statut Beth.

## 🟢 PHASE 4 : DELIVER (Extraction)
1. Formate la donnée.
2. Rapporte : "Cible acquise."
