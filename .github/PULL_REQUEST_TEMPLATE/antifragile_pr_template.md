## 📝 Description

<!-- Décrivez clairement les changements apportés -->

## 🎯 Type de changement

<!-- Cochez les cases appropriées -->

- [ ] 🐛 Bug fix (correction non-breaking)
- [ ] ✨ New feature (ajout de fonctionnalité non-breaking)
- [ ] 💥 Breaking change (changement qui casse la compatibilité)
- [ ] 📚 Documentation
- [ ] 🎨 Style (formatting, renaming)
- [ ] ♻️ Refactoring
- [ ] ⚡ Performance
- [ ] ✅ Tests
- [ ] 🔧 Chore (maintenance, CI, etc.)
- [ ] 🔒 Security fix (correctif de sécurité)

## 🔗 Issue lié

<!-- Si applicable, référencez l'issue : Fixes #123 -->

Fixes #

## 🛡️ Checklist Antifragilité

### Tests et Qualité
- [ ] Tests unitaires ajoutés/mis à jour (couverture > 80% pour le nouveau code)
- [ ] Tests d'intégration ajoutés/mis à jour (si applicable)
- [ ] Tests de régression pour les bugs corrigés
- [ ] Tests de performance (si changement critique)
- [ ] Tous les tests passent localement

### Sécurité
- [ ] Scan de sécurité effectué (pas de vulnérabilités critiques)
- [ ] Pas de secrets hardcodés
- [ ] Validation des inputs utilisateur
- [ ] Protection contre les injections SQL/XSS/CSRF (si applicable)
- [ ] Audit des nouvelles dépendances

### Résilience
- [ ] Gestion des erreurs appropriée (try/catch, error handling)
- [ ] Timeouts configurés pour les appels externes
- [ ] Retry logic implémentée (si pertinent)
- [ ] Logging adéquat pour le debugging
- [ ] Métriques ajoutées pour le monitoring

### Documentation
- [ ] README mis à jour (si changement d'API/usage)
- [ ] Docstrings/JSDoc ajoutés pour les nouvelles fonctions
- [ ] CHANGELOG.md mis à jour
- [ ] ADR créé (si décision architecturale majeure)
- [ ] Diagrammes mis à jour (si changement d'architecture)

### Déploiement
- [ ] Feature flag ajouté (si > 500 lignes ou fonctionnalité risquée)
- [ ] Plan de rollback documenté
- [ ] Migration de données testée (si applicable)
- [ ] Configuration d'environnement documentée
- [ ] Impact sur les autres services évalué

## 📊 Analyse d'Antifragilité

### Risques Identifiés et Mitigations
1. **[Risque 1]** : [Description]
   - **Mitigation** : [Plan]
2. **[Risque 2]** : [Description]
   - **Mitigation** : [Plan]

### Points de Défaillance Potentiels
- **[Point 1]** : [Description et stratégie de résilience]
- **[Point 2]** : [Description et stratégie de résilience]

### Impact sur les Dépendances
- [ ] Aucune nouvelle dépendance externe
- [ ] Nouvelles dépendances documentées avec alternatives identifiées
- [ ] Wrappers/adapters créés pour les dépendances critiques

## 📊 Métriques

### Avant/Après (si applicable)
| Métrique | Avant | Après | Objectif | Statut |
|----------|-------|-------|----------|--------|
| Temps de réponse (ms) | - | - | < 500 | - |
| Couverture de tests (%) | - | - | > 80% | - |
| Complexité cyclomatique | - | - | < 10 | - |

### Taille de la PR
- Lignes ajoutées : 
- Lignes supprimées : 
- Fichiers modifiés : 

**Note** : Les PRs de > 500 lignes sont découragées. Considérez de diviser en mini-PRs.

## 🧪 Plan de Test

### Comment tester cette PR
1. [Étape 1]
2. [Étape 2]
3. [Résultat attendu]

### Scénarios de Test Couverts
- [ ] Cas nominal (happy path)
- [ ] Cas d'erreur (error handling)
- [ ] Cas limites (edge cases)
- [ ] Test de charge (si critique)

### Commandes de Test Exécutées
```bash
# Linting
pylint <files>
flake8 .

# Tests
pytest --cov=. --cov-report=html
python verify_phase_1.py
python verify_phase_2.py

# Sécurité (si applicable)
bandit -r .
safety check
```

## 📋 Checklist Standard

- [ ] Mon code suit le style guide du projet
- [ ] J'ai effectué un self-review de mon code
- [ ] J'ai commenté le code, particulièrement dans les zones complexes
- [ ] J'ai mis à jour la documentation correspondante
- [ ] Mes changements ne génèrent pas de nouveaux warnings
- [ ] Mes commits suivent le format Conventional Commits
- [ ] J'ai vérifié qu'il n'y a pas de conflits avec la branche cible

## 📸 Screenshots (si applicable)

<!-- Ajoutez des captures d'écran si votre changement affecte l'UI -->

## 🔗 Contexte et Références

### Documentation Liée
- [Lien vers ADR si applicable]
- [Lien vers documentation technique]
- [Lien vers benchmark/POC]

### PRs/Issues Liées
- Dépend de #
- Bloque #
- Relate à #

## 💬 Notes pour les Reviewers

<!-- Ajoutez toute information supplémentaire pour les reviewers -->

**Points spécifiques à examiner attentivement :**
- [ ] [Point 1]
- [ ] [Point 2]

## 🚦 Niveau de Criticité

<!-- Cochez le niveau approprié selon 03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/02_STRATEGIE_GESTION_PROJET.md -->

- [ ] **Niveau 1 - Critique (Hotfix)** : Bug bloquant en production, vulnérabilité critique
- [ ] **Niveau 2 - Important (Feature/Fix)** : Nouvelle fonctionnalité majeure, refactoring significatif
- [ ] **Niveau 3 - Normal (Improvement)** : Amélioration incrémentale, optimisation
- [ ] **Niveau 4 - Mineur (Chore/Docs)** : Documentation, refactoring cosmétique

**Estimation du risque** : [Faible / Moyen / Élevé]  
**Temps de rollback estimé** : [X minutes]

## 🚦 Checklist Post-Merge

**À faire après le merge :**
- [ ] Surveiller les logs pendant 1h
- [ ] Vérifier les métriques (erreurs, latence)
- [ ] Confirmer que les alertes fonctionnent
- [ ] Documenter les leçons apprises (si applicable)

---

## 🤖 Pour les Reviewers

**Points à vérifier :**
- [ ] Le code est clair et maintenable
- [ ] Les tests sont appropriés et suffisants
- [ ] La documentation est à jour
- [ ] Pas de problèmes de sécurité évidents
- [ ] Les performances ne sont pas dégradées
- [ ] La checklist antifragilité est complète
- [ ] Le niveau de criticité est approprié

**Questions/Préoccupations :**
<!-- Notez vos questions ou préoccupations ici -->

---

📚 **Référence** : Pour plus de détails sur le processus antifragile, consultez [03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/](../../../03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/)
