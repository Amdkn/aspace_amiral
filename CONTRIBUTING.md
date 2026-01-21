# 🤝 Contributing to A'Space OS - Amiral

Bienvenue ! Ce guide décrit comment contribuer efficacement à ce dépôt.

> 🛡️ **Nouveau** : Ce projet suit maintenant un **Framework Antifragilité** pour transformer les contraintes en opportunités d'amélioration. Consultez [03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/](./03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/) pour plus de détails.

## 🚀 Quick Start

1. **Fork** le dépôt
2. **Clone** votre fork localement
3. Créez une **branche** pour votre travail
4. **Committez** vos changements
5. **Push** vers votre fork
6. Ouvrez une **Pull Request** (utilisez le template antifragile pour les PRs critiques)

## 📋 Pull Request Process

### 1. Branches

**Structure des branches :**
- `main` : Production (locked, merges from develop only)
- `develop` : Development (default branch for PRs)
- `feature/*` : New features
- `fix/*` : Bug fixes
- `hotfix/*` : Urgent production fixes
- `docs/*` : Documentation updates
- `copilot/*` : AI agent contributions

**Règles :**
- ❌ **Pas de PR directe vers `main`** (sauf hotfix/release)
- ✅ **Toutes les PRs doivent cibler `develop`**
- ✅ Utilisez des noms de branches descriptifs

### 2. Commit Messages

Suivez le format **Conventional Commits** :

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

**Types autorisés :**
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bug
- `docs`: Documentation uniquement
- `style`: Formatage (pas de changement de code)
- `refactor`: Refactoring (ni fix ni feature)
- `test`: Ajout ou modification de tests
- `chore`: Tâches de maintenance
- `perf`: Amélioration de performance
- `ci`: Changements CI/CD
- `build`: Changements système de build
- `revert`: Annulation d'un commit précédent

**Exemples :**
```
feat(pulse): add new KPI tracking feature
fix(kernel): resolve file locking issue on Windows
docs(readme): update installation instructions
test(pulse): add unit tests for logger
```

### 3. Code Style

#### Python
- **Style Guide** : Google Python Style Guide (voir `conductor/code_styleguides/python.md`)
- **Linting** : pylint, flake8
- **Formatting** : black (line length: 88)
- **Imports** : isort
- **Type hints** : Encouragés pour les APIs publiques
- **Docstrings** : Obligatoires pour fonctions/classes publiques

**Exemple :**
```python
def calculate_pulse_score(data: dict) -> float:
    """Calculate the pulse score based on KPI data.
    
    Args:
        data: Dictionary containing KPI metrics
        
    Returns:
        float: Calculated pulse score (0.0 to 1.0)
        
    Raises:
        ValueError: If data is invalid
    """
    pass
```

#### JavaScript/TypeScript
- **Linting** : ESLint (si configuré dans le projet)
- **Formatting** : Prettier (si configuré)
- **Style** : Suivre les conventions du projet

#### SQL (PL/pgSQL)
- **Conventions** :
  - Mots-clés en MAJUSCULES
  - Noms de tables/colonnes en snake_case
  - Indentation cohérente (2 ou 4 espaces)
  - Commentaires pour la logique complexe

**Exemple :**
```sql
-- Create pulse tracking table
CREATE TABLE IF NOT EXISTS pulse_events (
    id SERIAL PRIMARY KEY,
    event_type VARCHAR(50) NOT NULL,
    recorded_at TIMESTAMP DEFAULT NOW(),
    metadata JSONB
);

CREATE INDEX idx_pulse_events_type ON pulse_events(event_type);
```

### 4. Tests

- ✅ **Ajoutez des tests** pour toute nouvelle fonctionnalité
- ✅ **Corrigez les tests cassés** avant de soumettre
- ✅ **Exécutez la suite de tests localement** :

```bash
# Python tests
python verify_phase_1.py
python verify_phase_2.py
pytest

# JavaScript tests (si applicable)
npm test
```

### 5. Documentation

- Mettez à jour la documentation si nécessaire
- Ajoutez des docstrings/comments pour le code complexe
- Mettez à jour README.md si vous changez l'installation/utilisation

## 🤖 PR Integration Agent

Un agent automatisé vérifiera votre PR :

### Vérifications automatiques

1. **Validation des règles** :
   - ✅ Branche cible correcte
   - ✅ Format des commits
   - ✅ Pas de conflits de merge

2. **Qualité du code** :
   - ✅ Linting Python (pylint, flake8)
   - ✅ Formatage (black, isort)
   - ✅ Linting JavaScript (ESLint)
   - ✅ Validation SQL (syntax basique)

3. **Tests et couverture** :
   - ✅ Tous les tests passent
   - ✅ Rapport de couverture de code
   - ✅ Scripts de vérification

4. **Labeling automatique** :
   - 🏷️ `size/XS|S|M|L|XL` : Taille de la PR
   - 🏷️ `ready-for-review` : Prêt pour revue
   - 🏷️ `needs-fixes` : Corrections nécessaires
   - 🏷️ `quality-checked` : Qualité vérifiée

### Résultats

L'agent postera un rapport automatique sur votre PR avec :
- ✅ Statut de chaque vérification
- 📊 Rapport de couverture de tests
- 📋 Prochaines étapes suggérées

## 🔧 Configuration locale

### Python

```bash
# Installer les outils de développement
pip install pylint flake8 black isort pytest pytest-cov

# Linting
pylint your_file.py
flake8 your_file.py

# Formatage
black .
isort .

# Tests
pytest --cov=. --cov-report=html
```

### JavaScript

```bash
# Installer les dépendances
npm install

# Linting
npm run lint

# Tests
npm test
```

## 📝 Checklist avant PR

Avant de soumettre votre Pull Request :

- [ ] Code suit le style guide du projet
- [ ] Tous les tests passent localement
- [ ] Ajout de tests pour les nouvelles fonctionnalités
- [ ] Documentation mise à jour si nécessaire
- [ ] Commits suivent le format Conventional Commits
- [ ] Branche cible correcte (develop pour la plupart des cas)
- [ ] Pas de conflits avec la branche cible
- [ ] Code reviewé personnellement

### 🛡️ Checklist Antifragilité (PRs Critiques)

Pour les PRs de **niveau Critique ou Important**, consultez également :
- [ ] [Matrice d'Acceptation des PRs](./03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/02_STRATEGIE_GESTION_PROJET.md#11-checklist-obligatoire-pour-toute-pr)
- [ ] [Template PR Antifragile](./.github/PULL_REQUEST_TEMPLATE/antifragile_pr_template.md)
- [ ] Analyse des risques et plans de mitigation documentés
- [ ] Plan de rollback défini
- [ ] Métriques et monitoring configurés

## 🆘 Besoin d'aide ?

- Consultez les [Issues](../../issues) existantes
- Référez-vous à la [documentation](./README.md)
- Consultez la [gouvernance](./00_GOVERNANCE.md)
- 🆕 Découvrez le [Framework Antifragilité](./03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/)

## 📚 Ressources Additionnelles

### Framework Antifragilité
Ce projet intègre un framework complet pour transformer les contraintes en opportunités :

1. **[Brainstorming Antifragile](./03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/01_BRAINSTORMING_ANTIFRAGILE.md)** : Identification des risques et opportunités
2. **[Stratégie de Gestion](./03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/02_STRATEGIE_GESTION_PROJET.md)** : Processus et rôles pour les PRs
3. **[Architecture de Solution](./03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/03_ARCHITECTURE_SOLUTION.md)** : Patterns de résilience technique
4. **[Guide d'Implémentation](./03_RESOURCES/ANTIFRAGILITY_FRAMEWORK/04_IMPLEMENTATION_GUIDE.md)** : Templates et outils pratiques

**Recommandé pour** :
- 🔴 PRs critiques (hotfix, sécurité)
- 🟡 Changements architecturaux majeurs
- 🟢 Nouvelles fonctionnalités importantes

## 📜 License & Droits

En contribuant, vous acceptez que vos contributions soient sous la même license que le projet.

---

**Merci de contribuer à A'Space OS ! 🚀**
