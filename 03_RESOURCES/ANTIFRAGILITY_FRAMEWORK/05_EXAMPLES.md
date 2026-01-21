# 🎯 Guide d'Exemple : Implémentation Antifragile

## Vue d'ensemble

Ce guide fournit des exemples concrets d'application du framework antifragilité dans différents scénarios courants.

## Exemple 1 : Ajout d'une Nouvelle API Externe

### Contexte
L'équipe doit intégrer un service de paiement externe (ex: Stripe) dans l'application.

### Approche Antifragile

#### 1. Découpage en Mini-PRs
```
Fonctionnalité Complète : Intégration Stripe
│
├── PR #1 : Abstraction du service de paiement (100 lignes)
│   └── Créer l'interface PaymentService
│       └── Définir les contrats (charge, refund, verify)
│
├── PR #2 : Implémentation Stripe avec isolation (150 lignes)
│   ├── Créer StripeAdapter implements PaymentService
│   ├── Ajouter configuration + secrets management
│   └── Tests unitaires avec mocks
│
├── PR #3 : Résilience et error handling (100 lignes)
│   ├── Circuit breaker pour appels Stripe
│   ├── Retry logic avec backoff exponentiel
│   ├── Timeouts configurables
│   └── Tests de chaos (simulations d'échecs)
│
├── PR #4 : Monitoring et observabilité (80 lignes)
│   ├── Métriques (succès/échec, latence)
│   ├── Logs structurés
│   ├── Alertes sur taux d'erreur
│   └── Dashboard Grafana
│
└── PR #5 : Feature flag + déploiement progressif (50 lignes)
    ├── Feature flag ENABLE_STRIPE
    ├── Rollout 5% → 25% → 50% → 100%
    └── Documentation de rollback
```

#### 2. Code Exemple : Interface Abstraite

```python
# payment/interfaces.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional
from decimal import Decimal

@dataclass
class PaymentResult:
    success: bool
    transaction_id: Optional[str]
    error_message: Optional[str] = None
    provider: str = ""

class PaymentServiceInterface(ABC):
    """
    Interface pour les services de paiement.
    Permet de changer de provider sans impacter le code métier.
    """
    
    @abstractmethod
    def charge(self, amount: Decimal, currency: str, 
               customer_id: str, **kwargs) -> PaymentResult:
        """Charge un paiement"""
        pass
    
    @abstractmethod
    def refund(self, transaction_id: str, 
               amount: Optional[Decimal] = None) -> PaymentResult:
        """Rembourse un paiement"""
        pass
    
    @abstractmethod
    def verify_transaction(self, transaction_id: str) -> PaymentResult:
        """Vérifie le statut d'une transaction"""
        pass
```

#### 3. Code Exemple : Adapter avec Résilience

```python
# payment/stripe_adapter.py
import stripe
import time
from typing import Optional
from decimal import Decimal
from .interfaces import PaymentServiceInterface, PaymentResult
from .circuit_breaker import CircuitBreaker
from .logging import get_logger

logger = get_logger(__name__)

class StripeAdapter(PaymentServiceInterface):
    """
    Adapter pour Stripe avec résilience intégrée.
    """
    
    def __init__(self, api_key: str, timeout: int = 10):
        stripe.api_key = api_key
        self.timeout = timeout
        self.circuit_breaker = CircuitBreaker(
            failure_threshold=5,
            recovery_timeout=60,
            expected_exception=stripe.error.StripeError
        )
    
    def charge(self, amount: Decimal, currency: str, 
               customer_id: str, **kwargs) -> PaymentResult:
        """
        Charge avec retry automatique et circuit breaker.
        """
        try:
            result = self._retry_with_backoff(
                self._charge_internal,
                amount, currency, customer_id, **kwargs
            )
            
            logger.info(
                "Payment successful",
                extra={
                    "transaction_id": result.transaction_id,
                    "amount": float(amount),
                    "currency": currency,
                    "customer_id": customer_id
                }
            )
            
            return result
            
        except Exception as e:
            logger.error(
                "Payment failed",
                extra={
                    "amount": float(amount),
                    "currency": currency,
                    "customer_id": customer_id,
                    "error": str(e)
                },
                exc_info=True
            )
            return PaymentResult(
                success=False,
                transaction_id=None,
                error_message=str(e),
                provider="stripe"
            )
    
    def _charge_internal(self, amount: Decimal, currency: str,
                        customer_id: str, **kwargs):
        """Appel interne avec circuit breaker"""
        return self.circuit_breaker.call(
            stripe.PaymentIntent.create,
            amount=int(amount * 100),  # Stripe utilise les centimes
            currency=currency.lower(),
            customer=customer_id,
            confirm=True,
            **kwargs
        )
    
    def _retry_with_backoff(self, func, *args, max_retries=3, **kwargs):
        """
        Retry avec backoff exponentiel.
        """
        for attempt in range(max_retries):
            try:
                result = func(*args, **kwargs)
                
                return PaymentResult(
                    success=True,
                    transaction_id=result.id,
                    provider="stripe"
                )
                
            except stripe.error.RateLimitError as e:
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt) + (random.random() * 0.1)
                    logger.warning(
                        f"Rate limited, retrying in {wait_time}s",
                        extra={"attempt": attempt + 1}
                    )
                    time.sleep(wait_time)
                else:
                    raise
            
            except stripe.error.APIConnectionError as e:
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt)
                    logger.warning(
                        f"Connection error, retrying in {wait_time}s",
                        extra={"attempt": attempt + 1}
                    )
                    time.sleep(wait_time)
                else:
                    raise
    
    def refund(self, transaction_id: str, 
               amount: Optional[Decimal] = None) -> PaymentResult:
        """Rembourse avec gestion d'erreurs"""
        try:
            refund_params = {"payment_intent": transaction_id}
            if amount:
                refund_params["amount"] = int(amount * 100)
            
            result = self.circuit_breaker.call(
                stripe.Refund.create,
                **refund_params
            )
            
            return PaymentResult(
                success=True,
                transaction_id=result.id,
                provider="stripe"
            )
            
        except Exception as e:
            logger.error(f"Refund failed: {e}", exc_info=True)
            return PaymentResult(
                success=False,
                transaction_id=None,
                error_message=str(e),
                provider="stripe"
            )
    
    def verify_transaction(self, transaction_id: str) -> PaymentResult:
        """Vérifie le statut avec timeout"""
        try:
            payment_intent = stripe.PaymentIntent.retrieve(
                transaction_id,
                timeout=self.timeout
            )
            
            return PaymentResult(
                success=payment_intent.status == "succeeded",
                transaction_id=payment_intent.id,
                provider="stripe"
            )
            
        except Exception as e:
            logger.error(f"Verification failed: {e}", exc_info=True)
            return PaymentResult(
                success=False,
                transaction_id=None,
                error_message=str(e),
                provider="stripe"
            )
```

#### 4. Tests de Résilience

```python
# tests/test_stripe_adapter_resilience.py
import pytest
from unittest.mock import Mock, patch
from decimal import Decimal
import stripe

from payment.stripe_adapter import StripeAdapter

def test_charge_with_rate_limiting():
    """Test du retry automatique en cas de rate limiting"""
    adapter = StripeAdapter(api_key="test_key")
    
    # Simuler 2 échecs puis succès
    with patch('stripe.PaymentIntent.create') as mock_create:
        mock_create.side_effect = [
            stripe.error.RateLimitError("Too many requests"),
            stripe.error.RateLimitError("Too many requests"),
            Mock(id="pi_123", status="succeeded")
        ]
        
        result = adapter.charge(
            amount=Decimal("100.00"),
            currency="USD",
            customer_id="cus_123"
        )
        
        assert result.success is True
        assert result.transaction_id == "pi_123"
        assert mock_create.call_count == 3

def test_charge_with_circuit_breaker_open():
    """Test du circuit breaker en état ouvert"""
    adapter = StripeAdapter(api_key="test_key")
    
    # Déclencher l'ouverture du circuit breaker
    with patch('stripe.PaymentIntent.create') as mock_create:
        mock_create.side_effect = stripe.error.APIConnectionError("Connection failed")
        
        # Faire échouer 5 fois pour ouvrir le circuit
        for _ in range(5):
            try:
                adapter.charge(Decimal("100.00"), "USD", "cus_123")
            except:
                pass
        
        # Le circuit doit être ouvert maintenant
        assert adapter.circuit_breaker.state.value == "open"
        
        # Les appels suivants doivent échouer immédiatement
        result = adapter.charge(Decimal("100.00"), "USD", "cus_123")
        assert result.success is False
        assert "Circuit breaker is OPEN" in result.error_message

def test_charge_with_timeout():
    """Test du timeout sur les appels Stripe"""
    adapter = StripeAdapter(api_key="test_key", timeout=1)
    
    with patch('stripe.PaymentIntent.create') as mock_create:
        # Simuler un timeout
        mock_create.side_effect = stripe.error.Timeout("Request timed out")
        
        result = adapter.charge(
            amount=Decimal("100.00"),
            currency="USD",
            customer_id="cus_123"
        )
        
        assert result.success is False
        assert "timed out" in result.error_message.lower()
```

#### 5. Feature Flag Implementation

```python
# config/feature_flags.py
import os
from enum import Enum

class Feature(Enum):
    ENABLE_STRIPE = "enable_stripe"

class FeatureFlags:
    def __init__(self):
        self._flags = {
            Feature.ENABLE_STRIPE.value: self._get_env_bool("FF_ENABLE_STRIPE", False)
        }
    
    def is_enabled(self, feature: Feature, user_id: str = None) -> bool:
        if not self._flags.get(feature.value, False):
            return False
        
        # Rollout progressif basé sur user_id
        if user_id and feature == Feature.ENABLE_STRIPE:
            rollout_percentage = int(os.getenv("STRIPE_ROLLOUT_PERCENT", "0"))
            return (hash(user_id) % 100) < rollout_percentage
        
        return True
    
    def _get_env_bool(self, key: str, default: bool) -> bool:
        value = os.getenv(key, str(default))
        return value.lower() in ('true', '1', 'yes')

# Usage dans le code
flags = FeatureFlags()

def process_payment(user_id: str, amount: Decimal, currency: str):
    if flags.is_enabled(Feature.ENABLE_STRIPE, user_id):
        return stripe_adapter.charge(amount, currency, user_id)
    else:
        return legacy_payment_service.charge(amount, currency, user_id)
```

#### 6. Monitoring et Métriques

```python
# monitoring/payment_metrics.py
from prometheus_client import Counter, Histogram, Gauge

# Métriques Prometheus
payment_attempts = Counter(
    'payment_attempts_total',
    'Total payment attempts',
    ['provider', 'currency', 'status']
)

payment_duration = Histogram(
    'payment_duration_seconds',
    'Payment processing duration',
    ['provider']
)

circuit_breaker_state = Gauge(
    'circuit_breaker_state',
    'Circuit breaker state (0=closed, 1=open, 2=half_open)',
    ['service']
)

# Dans StripeAdapter
def charge(self, amount, currency, customer_id, **kwargs):
    with payment_duration.labels(provider='stripe').time():
        try:
            result = self._charge_internal(amount, currency, customer_id, **kwargs)
            
            payment_attempts.labels(
                provider='stripe',
                currency=currency,
                status='success'
            ).inc()
            
            return result
            
        except Exception as e:
            payment_attempts.labels(
                provider='stripe',
                currency=currency,
                status='failure'
            ).inc()
            raise
```

#### 7. Documentation : ADR

```markdown
# ADR-001 : Intégration de Stripe avec Pattern Adapter

**Status** : Accepté  
**Date** : 2026-01-21  
**Décideurs** : Tech Lead, Architecte, Product Owner

## Contexte et Problématique

L'application nécessite un système de paiement robuste. Stripe est choisi comme
provider principal, mais nous devons éviter un couplage fort qui rendrait difficile
un changement de provider futur.

## Options Considérées

### Option 1 : Intégration Directe de Stripe
**Avantages** :
- ✅ Implémentation rapide
- ✅ Accès à toutes les fonctionnalités Stripe

**Inconvénients** :
- ❌ Couplage fort avec Stripe
- ❌ Migration difficile vers un autre provider
- ❌ Tests complexes (dépendance externe)

### Option 2 : Pattern Adapter avec Interface Abstraite
**Avantages** :
- ✅ Découplage du code métier
- ✅ Facilité de changer de provider
- ✅ Tests simplifiés (mock de l'interface)
- ✅ Possibilité d'avoir plusieurs providers en parallèle

**Inconvénients** :
- ❌ Légèrement plus de code initial
- ❌ Abstraction qui peut masquer certaines fonctionnalités spécifiques

## Décision

**Option choisie** : Pattern Adapter (Option 2)

**Justification** :
- L'antifragilité nécessite de pouvoir changer de provider rapidement si Stripe
  devient indisponible ou change ses conditions.
- Les tests sont critiques pour la fiabilité des paiements.
- Le coût additionnel de l'abstraction est négligeable comparé aux bénéfices.

## Conséquences

### Positives
- Code métier indépendant de Stripe
- Tests unitaires rapides sans appels réseau
- Migration future simplifiée
- Possibilité de A/B tester plusieurs providers

### Négatives
- Temps de développement initial légèrement plus long
- Nécessité de maintenir l'interface si ajout de fonctionnalités

### Risques et Mitigation
| Risque | Mitigation |
|--------|------------|
| Abstraction trop complexe | Garder l'interface simple avec les opérations essentielles |
| Performance impactée | Profiling et benchmarks réguliers |

## Plan d'Implémentation

### Phase 1 : Interface et Abstraction (Semaine 1)
- Créer PaymentServiceInterface
- Tests unitaires de l'interface

### Phase 2 : StripeAdapter (Semaine 2)
- Implémenter StripeAdapter
- Ajouter résilience (circuit breaker, retry)
- Tests avec mocks Stripe

### Phase 3 : Integration (Semaine 3)
- Feature flag pour rollout progressif
- Monitoring et alertes
- Documentation

## Validation

**Critères de Succès** :
- [ ] 100% des tests passent
- [ ] Couverture > 90% sur le code payment
- [ ] Temps de réponse < 500ms (p95)
- [ ] Taux d'erreur < 0.5%

**Date de Révision** : 2026-04-21 (3 mois)
```

## Exemple 2 : Gestion d'un Incident de Production

### Scénario
Une mise à jour a causé une augmentation du taux d'erreur de 0.1% à 5% en production.

### Réponse Antifragile

#### 1. Détection Immédiate (Automatique)
```yaml
# Alerte Prometheus
- alert: HighErrorRate
  expr: rate(http_requests_total{status=~"5.."}[5m]) > 0.01
  for: 2m
  labels:
    severity: critical
  annotations:
    summary: "High error rate detected: {{ $value }}%"
    runbook: "https://wiki.internal/runbooks/high-error-rate"
```

#### 2. Rollback Automatique
```bash
# Script de rollback automatisé
#!/bin/bash
set -e

PREVIOUS_VERSION=$(cat /var/app/previous_version)
echo "Rolling back to version: $PREVIOUS_VERSION"

# Blue-Green switch
kubectl set image deployment/app app=myapp:$PREVIOUS_VERSION

# Attendre le rollback
kubectl rollout status deployment/app

# Vérifier la santé
for i in {1..10}; do
  if curl -f http://app/health; then
    echo "Rollback successful"
    exit 0
  fi
  sleep 5
done

echo "Rollback failed"
exit 1
```

#### 3. Post-Mortem Structuré

```markdown
# Post-Mortem : Taux d'Erreur Élevé (2026-01-21)

## Résumé Exécutif
Déploiement de v2.3.0 a causé 5% d'erreurs pendant 18 minutes avant rollback.
Impact : 2500 utilisateurs, 0 perte de données.

## Chronologie
| Heure | Événement |
|-------|-----------|
| 14:00 | Déploiement v2.3.0 commence |
| 14:05 | Alerte "HighErrorRate" déclenchée |
| 14:06 | Équipe DevOps notifiée |
| 14:08 | Investigation démarrée |
| 14:12 | Décision de rollback |
| 14:15 | Rollback automatique exécuté |
| 14:18 | Service rétabli, taux d'erreur normal |

## Cause Racine (5 Why's)
1. **Pourquoi des erreurs ?** → Timeout sur appels à la DB
2. **Pourquoi des timeouts ?** → Query SQL inefficace introduite
3. **Pourquoi query inefficace ?** → Index manquant sur nouvelle colonne
4. **Pourquoi index manquant ?** → Pas de test de performance en CI
5. **Pourquoi pas de test ?** → Tests de performance non automatisés

**Cause Racine** : Absence de tests de performance automatisés en CI

## Actions Correctives

### Immédiates (J+1 à J+7)
| Action | Responsable | Échéance | Statut |
|--------|-------------|----------|--------|
| Ajouter index manquant | DevOps | J+1 | [x] |
| Redéployer v2.3.1 avec fix | DevOps | J+2 | [x] |
| Ajouter test de performance pour cette query | Dev | J+5 | [x] |

### Court Terme (1-4 semaines)
| Action | Responsable | Échéance | Statut |
|--------|-------------|----------|--------|
| Intégrer tests de performance en CI | DevOps | S+2 | [ ] |
| Créer benchmarks de référence | Dev | S+2 | [ ] |
| Documenter runbook pour ce type d'incident | Tech Lead | S+3 | [ ] |

## Améliorations d'Antifragilité

### Ce qui nous rend plus forts
1. **Tests de Performance Automatisés** : Tous les PRs critiques auront des benchmarks
2. **Monitoring Amélioré** : Dashboard avec temps de query par endpoint
3. **Rollback Plus Rapide** : Réduction de 18min → objectif < 5min
4. **Documentation** : Runbook créé pour ce type d'incident

### Tests Ajoutés
- [ ] Test de régression pour cette query SQL
- [ ] Benchmark de performance en CI
- [ ] Test de charge simulant 2x le trafic normal
```

## Exemple 3 : Refactoring Majeur avec Antifragilité

### Contexte
Refactoring d'un module legacy de 5000 lignes en architecture modulaire.

### Approche Antifragile : Strangler Fig Pattern

```
┌─────────────────────────────────────────────────────┐
│          STRANGLER FIG PATTERN                       │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Phase 1: Façade                                     │
│  ┌──────────────┐                                   │
│  │   Façade     │────┐                              │
│  └──────────────┘    │                              │
│         │             ↓                              │
│         └──────→ Legacy Module                       │
│                                                      │
│  Phase 2: Migration Progressive                     │
│  ┌──────────────┐                                   │
│  │   Façade     │────┬──→ New Module (20%)          │
│  └──────────────┘    │                              │
│                      └──→ Legacy Module (80%)        │
│                                                      │
│  Phase 3: Completion                                │
│  ┌──────────────┐                                   │
│  │   Façade     │────────→ New Module (100%)        │
│  └──────────────┘                                   │
│                                                      │
│  Phase 4: Cleanup                                   │
│  New Module (direct calls, no façade)               │
│                                                      │
└─────────────────────────────────────────────────────┘
```

#### Découpage en PRs

```
Refactoring Module Legacy
│
├── PR #1 : Créer la façade (50 lignes)
│   └── Interface stable qui délègue au legacy
│
├── PR #2-10 : Migration progressive (300 lignes/PR)
│   ├── Migrer fonction par fonction
│   ├── Feature flag par fonction
│   └── A/B testing legacy vs new
│
└── PR #11 : Suppression du legacy (supprimer 4500 lignes)
    └── Après validation 100% sur new module
```

---

**Version** : 1.0.0  
**Date** : 2026-01-21  
**Statut** : Prêt à l'emploi
