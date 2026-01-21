# 00_Amiral: Cockpit de Commandement A'Space OS

**Orchestration fractale Life/Business/Kernel.**

Ce dépôt contient la "Vérité Source" (R0) de l'univers A'Space.
Il héberge les Blueprints, la Constitution, et les protocoles validés par l'Architecte et l'Amiral.

## Structure
*   `00_CORE/` : Blueprints et Manifestes.
*   `.agent/rules/` : La Constitution (Lois L0, L1, L2).
*   `00_ARCHITECT_R0_BLUEPRINT.md` : Le Plan de la Trinité R0/R'0/R".

**Statut :** R0 Locked.
**Gouvernance :** Voir `.agent/rules/00_ASPACE_CONSTITUTION_V2.md`.

## 🤖 PR Integration Agent

Ce dépôt utilise un **Agent d'implémentation de PR** automatisé pour gérer la qualité et l'intégration des Pull Requests.

### Fonctionnalités
- ✅ **Validation automatique** : Tests, linting multi-langages (Python, JS, SQL)
- ✅ **Règles de contribution** : Vérification des commits et branches
- ✅ **Détection de conflits** : Simulation de merge avant intégration
- ✅ **Labels dynamiques** : Classification automatique des PRs
- ✅ **Déploiement** : Validation Docker et préparation VPS

### 🛡️ Framework Antifragilité

Le projet intègre maintenant un **Framework Antifragilité** complet pour transformer les contraintes et perturbations en opportunités d'amélioration.

**Ressources disponibles :**
- 📚 [Documentation Complète](./03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/)
- 📋 [Template PR Antifragile](./.github/PULL_REQUEST_TEMPLATE/antifragile_pr_template.md)
- 🎯 [Exemples Pratiques](./03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/05_EXAMPLES.md)

**Principes clés :**
- Découpage en mini-PRs (< 300 lignes)
- Feature flags pour déploiements progressifs
- Tests de résilience (chaos engineering)
- Monitoring et rollback automatiques

### Pour contribuer
1. Consultez [CONTRIBUTING.md](./CONTRIBUTING.md) pour les conventions
2. Créez votre branche depuis `develop`
3. Suivez le format **Conventional Commits**
4. Pour les PRs critiques, utilisez le [Template Antifragile](./.github/PULL_REQUEST_TEMPLATE/antifragile_pr_template.md)
5. L'agent validera automatiquement votre PR

📚 **Documentation complète** : [.github/PR_INTEGRATION_AGENT.md](./.github/PR_INTEGRATION_AGENT.md)
