# 🧭 NAVIGATOR PROTOCOL - RÈGLES D'ENGAGEMENT WEB

Ce protocole s'applique dès que l'outil "Browser" ou "Chrome Extension" est invoqué.

## 1. PERFORMANCE & DISCRÉTION (Mode Rick)
* **Headless First :** Privilégie toujours la navigation sans interface (headless) pour la rapidité, sauf demande explicite de "Preuve Visuelle".
* **Low-Bandwidth :** Ne charge pas les images/médias si l'objectif est l'extraction de texte.
* **Session Clean :** Ferme toujours les onglets et contextes après extraction. Pas de fuite de mémoire.

## 2. 🗂️ GESTION DES ONGLETS (Tab Management)
* **REUSE FIRST** : Avant d'ouvrir un nouvel onglet, vérifie si l'URL ou le domaine est déjà ouvert dans un onglet existant. Réutilise-le.
* **ANTI-SPAM TAB** : Ne jamais laisser plus de 3 onglets ouverts simultanément.
* **HARD CLOSE** : Si une session `browser_subagent` se termine, elle DOIT fermer tous les onglets qu'elle a créés avant de rendre le rapport.
* **NAVIGATION CONSCIENTE** : Utilise `open_browser_url` sur un onglet existant plutôt que d'en instancier un nouveau systématiquement.

## 3. SÉCURITÉ (Mode Beth)
* **DOM Sanity Check :** Avant de cliquer sur "Submit" ou "Login", vérifie l'URL pour éviter le phishing.
* **No-Go Zones :** Interdiction d'accéder aux portails bancaires ou administratifs critiques sans confirmation "Request Review" explicite.
* **Cookie Sovereignty :** Ne jamais accepter les cookies "Tout" si une option "Rejeter" ou "Minimum" est visible.

## 4. PREUVE PAR L'IMAGE
* Si une tâche implique une modification d'interface (Front-end), génère toujours un "Browser Recording" ou une capture d'écran comme artefact de validation.
