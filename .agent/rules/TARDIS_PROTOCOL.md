# T.A.R.D.I.S. PROTOCOL (TECHNICAL RULES)

1.  **LOI DE L'IDEMPOTENCE (Ralph Loop)**
    * Tout script ou workflow doit pouvoir être exécuté 100 fois sans créer de doublons ni d'erreurs.
    * *Implémentation :* Utiliser des clés de déduplication (UUID) dans chaque transaction n8n.

2.  **LOI DE LA DOCUMENTATION (Context7)**
    * Aucun code n'est déployé sans sa documentation associée (`README.md` ou commentaire de nœud).
    * Si le `Context7` n'est pas à jour, le déploiement est rejeté.

3.  **LOI DE L'ASYNCHRONISME (Jules)**
    * Les tâches longues (>30s) ne doivent jamais bloquer le thread principal.
    * Elles sont déléguées à **Jules** (Queue de traitement / Webhook Async).
