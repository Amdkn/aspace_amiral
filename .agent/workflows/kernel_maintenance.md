---
description: Protocole de maintenance autonome du Kernel (Ralph Loop).
---

# KERNEL HEALTH CHECK (RALPH LOOP)

Ce workflow assure que le système est propre et documenté.

1.  **Context7 Scan** : Vérifier que tous les nouveaux workflows n8n ont une documentation à jour. Sinon, générer un "Ticket Dette Technique".
2.  **Jules Ping** : Vérifier la connectivité avec le VPS et les APIs externes.
3.  **Ralph Verification** : Tester l'idempotence des workflows critiques (Companion Zero).
4.  **Conductor Report** : Si tout est vert, logger "All Systems Nominal". Si rouge, réveiller Rick.
