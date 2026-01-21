# 🏗️ Architecture de Solution Structurelle : Foundation Technique

## Vue d'ensemble

Ce document définit l'architecture technique favorisant l'antifragilité par la redondance, l'isolation, et l'automatisation.

## 1. Isolation des Composants

### 1.1 Principes d'Architecture Modulaire

#### Séparation des Responsabilités
```
┌─────────────────────────────────────────────────────────┐
│                  APPLICATION LAYERS                      │
├─────────────────────────────────────────────────────────┤
│  Presentation Layer    │  User Interface / API          │
│  ─────────────────────┼────────────────────────────────┤
│  Application Layer     │  Business Logic / Orchestration│
│  ─────────────────────┼────────────────────────────────┤
│  Domain Layer          │  Core Business Rules           │
│  ─────────────────────┼────────────────────────────────┤
│  Infrastructure Layer  │  Data Access / External Services│
└─────────────────────────────────────────────────────────┘
```

#### Règles de Dépendance
1. **Unidirectionnalité** : Les dépendances vont toujours vers l'intérieur
2. **Indépendance du Domaine** : La couche domaine n'a aucune dépendance externe
3. **Injection de Dépendances** : Utilisation systématique de DI pour l'inversion de contrôle
4. **Interfaces Claires** : Chaque couche expose des contrats stables

### 1.2 Stratégies de Modularisation

#### Micro-Services (Pour projets complexes)
**Quand Utiliser** :
- Équipes multiples travaillant en parallèle
- Besoins de scalabilité différenciés
- Technologies hétérogènes justifiées
- Déploiements indépendants nécessaires

**Structure Type** :
```
services/
├── auth-service/          # Authentification & autorisation
│   ├── src/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
├── api-gateway/           # Point d'entrée unique
│   ├── src/
│   ├── tests/
│   └── config/
├── business-service/      # Logique métier principale
│   ├── src/
│   ├── tests/
│   └── migrations/
└── notification-service/  # Emails, SMS, push notifications
    ├── src/
    ├── tests/
    └── templates/
```

**Communication** :
- **Synchrone** : REST API, gRPC pour les appels critiques
- **Asynchrone** : Message queues (RabbitMQ, Kafka) pour les événements
- **Service Discovery** : Consul, Eureka pour l'enregistrement dynamique

#### Modular Monolith (Pour projets moyens)
**Quand Utiliser** :
- Équipe unique ou petite
- Complexité modérée
- Déploiement unifié acceptable
- Réduction de la complexité opérationnelle souhaitée

**Structure Type** :
```
src/
├── modules/
│   ├── auth/              # Module d'authentification
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── services.py
│   │   ├── repositories.py
│   │   └── tests/
│   ├── users/             # Gestion des utilisateurs
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── services.py
│   │   └── tests/
│   ├── billing/           # Facturation
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── services.py
│   │   └── tests/
│   └── shared/            # Code partagé
│       ├── exceptions.py
│       ├── validators.py
│       └── utils.py
└── core/
    ├── config.py
    ├── database.py
    └── logging.py
```

**Règles d'Interaction** :
- Modules communiquent via interfaces publiques uniquement
- Pas d'import direct des internals d'un autre module
- Événements pour les communications asynchrones
- Dépendances explicites dans les fichiers de config

### 1.3 Isolation des Dépendances Externes

#### Pattern Adapter
```python
# Interface stable (ne change jamais)
class EmailServiceInterface:
    def send_email(self, to: str, subject: str, body: str) -> bool:
        pass

# Implémentation pour SendGrid
class SendGridAdapter(EmailServiceInterface):
    def __init__(self, api_key: str):
        self.client = sendgrid.SendGridAPIClient(api_key)
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        # Implémentation spécifique SendGrid
        pass

# Implémentation pour AWS SES
class SESAdapter(EmailServiceInterface):
    def __init__(self, region: str):
        self.client = boto3.client('ses', region_name=region)
    
    def send_email(self, to: str, subject: str, body: str) -> bool:
        # Implémentation spécifique SES
        pass

# Configuration (facile à changer)
EMAIL_SERVICE = SendGridAdapter(api_key=settings.SENDGRID_KEY)
# EMAIL_SERVICE = SESAdapter(region='us-east-1')  # Changement simple
```

#### Avantages
- **Remplacement Transparent** : Changer de fournisseur sans toucher au code métier
- **Tests Facilités** : Mock de l'interface plutôt que du service réel
- **Migration Progressive** : Tester le nouveau provider en parallèle
- **Résilience** : Fallback vers un provider alternatif en cas d'échec

## 2. Tests Automatisés

### 2.1 Pyramide de Tests

```
              ┌─────────┐
             /  E2E      \       5%  - Tests de bout en bout
            /   Tests     \
           /───────────────\
          /  Integration   \     25% - Tests d'intégration
         /     Tests        \
        /───────────────────\
       /    Unit Tests       \   70% - Tests unitaires
      /─────────────────────\
```

### 2.2 Tests Unitaires

**Objectif** : Tester les composants isolés

**Caractéristiques** :
- Exécution rapide (< 100ms par test)
- Pas d'I/O (base de données, réseau, filesystem)
- Utilisation extensive de mocks
- Couverture élevée (> 80%)

**Exemple** :
```python
import pytest
from unittest.mock import Mock, patch

def test_user_service_create_user():
    # Arrange
    mock_repo = Mock()
    mock_repo.save.return_value = User(id=1, email="test@example.com")
    service = UserService(repository=mock_repo)
    
    # Act
    user = service.create_user(email="test@example.com", password="secure123")
    
    # Assert
    assert user.id == 1
    assert user.email == "test@example.com"
    mock_repo.save.assert_called_once()

def test_user_service_create_user_duplicate_email():
    # Arrange
    mock_repo = Mock()
    mock_repo.exists.return_value = True
    service = UserService(repository=mock_repo)
    
    # Act & Assert
    with pytest.raises(DuplicateEmailError):
        service.create_user(email="existing@example.com", password="secure123")
```

**Outils** :
- **Python** : pytest, unittest, nose2
- **JavaScript** : Jest, Mocha, Jasmine
- **Java** : JUnit, TestNG
- **Coverage** : coverage.py, Istanbul, JaCoCo

### 2.3 Tests d'Intégration

**Objectif** : Tester les interactions entre composants

**Caractéristiques** :
- Exécution plus lente (< 5s par test)
- Utilisation de bases de données de test
- Appels à des services réels (en test)
- Focus sur les interfaces et contrats

**Exemple** :
```python
import pytest

@pytest.fixture
def test_db():
    """Fixture pour base de données de test"""
    db = create_test_database()
    yield db
    db.cleanup()

def test_user_repository_save_and_retrieve(test_db):
    # Arrange
    repo = UserRepository(database=test_db)
    user_data = {"email": "test@example.com", "password": "hashed_pwd"}
    
    # Act
    saved_user = repo.save(user_data)
    retrieved_user = repo.get_by_id(saved_user.id)
    
    # Assert
    assert retrieved_user.id == saved_user.id
    assert retrieved_user.email == "test@example.com"

def test_api_endpoint_create_user(test_client, test_db):
    # Arrange
    payload = {"email": "api@example.com", "password": "secure123"}
    
    # Act
    response = test_client.post("/api/users", json=payload)
    
    # Assert
    assert response.status_code == 201
    assert "id" in response.json()
    
    # Vérifier la persistance
    user = test_db.query(User).filter_by(email="api@example.com").first()
    assert user is not None
```

**Outils** :
- **Databases** : SQLite pour tests, Docker pour PostgreSQL/MySQL
- **API Testing** : TestClient (FastAPI), Supertest (Express)
- **Containers** : Testcontainers pour services complexes

### 2.4 Tests de Résilience (Chaos Engineering)

**Objectif** : Valider le comportement en conditions dégradées

**Scénarios à Tester** :
1. **Latence Réseau** : Délais importants dans les appels API
2. **Timeouts** : Services qui ne répondent pas
3. **Erreurs Intermittentes** : Échecs aléatoires (50% taux d'erreur)
4. **Charge Élevée** : Stress test avec trafic x10
5. **Panne Partielle** : Un micro-service down
6. **Corruption de Données** : Données invalides en input

**Exemple avec Chaos Toolkit** :
```yaml
# chaos-experiment.yaml
version: 1.0.0
title: "Test de résilience du service de paiement"
description: "Valider le fallback sur le provider secondaire"

steady-state-hypothesis:
  title: "Le système accepte les paiements"
  probes:
    - type: probe
      name: "payment-endpoint-responds"
      provider:
        type: http
        url: "http://localhost:8000/api/payment"
        method: GET
        timeout: 3
      tolerance: 200

method:
  - type: action
    name: "simulate-primary-payment-provider-down"
    provider:
      type: process
      path: "docker"
      arguments: "stop payment-provider-primary"
  
  - type: probe
    name: "verify-fallback-to-secondary"
    provider:
      type: http
      url: "http://localhost:8000/api/payment"
      method: POST
      headers:
        Content-Type: "application/json"
      body: '{"amount": 100, "currency": "USD"}'
      timeout: 5
    tolerance: 200

rollbacks:
  - type: action
    name: "restore-primary-provider"
    provider:
      type: process
      path: "docker"
      arguments: "start payment-provider-primary"
```

**Outils** :
- **Chaos Toolkit** : Framework de chaos engineering
- **Toxiproxy** : Simulation de conditions réseau dégradées
- **Pumba** : Chaos testing pour Docker
- **Gremlin** : Plateforme chaos engineering entreprise

### 2.5 Tests de Performance

**Objectif** : Garantir les performances attendues

**Types de Tests** :
1. **Load Testing** : Comportement sous charge normale
2. **Stress Testing** : Limites du système
3. **Spike Testing** : Pics de trafic soudains
4. **Endurance Testing** : Stabilité sur la durée

**Exemple avec Locust** :
```python
from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Attente entre requêtes
    
    @task(3)  # Poids: exécuté 3x plus souvent
    def view_homepage(self):
        self.client.get("/")
    
    @task(2)
    def view_product(self):
        product_id = random.randint(1, 1000)
        self.client.get(f"/products/{product_id}")
    
    @task(1)
    def create_order(self):
        self.client.post("/orders", json={
            "product_id": random.randint(1, 100),
            "quantity": random.randint(1, 5)
        })
    
    def on_start(self):
        # Authentification au démarrage
        self.client.post("/login", json={
            "username": "test_user",
            "password": "test_pass"
        })
```

**Critères d'Acceptation** :
- **Latence p95** : < 500ms pour les endpoints critiques
- **Throughput** : > 1000 req/s pour l'API principale
- **Taux d'Erreur** : < 0.1% sous charge normale
- **Temps de Réponse** : Stable sur 1h de test en continu

## 3. Orchestration de Failover

### 3.1 Stratégies de Haute Disponibilité

#### Load Balancing
```
                    ┌──────────────┐
                    │ Load Balancer│
                    │  (HAProxy)   │
                    └──────┬───────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    ┌────▼────┐      ┌────▼────┐      ┌────▼────┐
    │ Server 1│      │ Server 2│      │ Server 3│
    │ (Active)│      │ (Active)│      │ (Active)│
    └─────────┘      └─────────┘      └─────────┘
```

**Configuration HAProxy** :
```haproxy
frontend http_front
    bind *:80
    mode http
    default_backend http_back

backend http_back
    mode http
    balance roundrobin
    option httpchk GET /health
    http-check expect status 200
    
    server server1 10.0.0.1:8000 check inter 5s fall 3 rise 2
    server server2 10.0.0.2:8000 check inter 5s fall 3 rise 2
    server server3 10.0.0.3:8000 check inter 5s fall 3 rise 2
```

#### Circuit Breaker Pattern
```python
from functools import wraps
import time
from typing import Callable
from enum import Enum

class CircuitState(Enum):
    CLOSED = "closed"      # Fonctionnement normal
    OPEN = "open"          # Service considéré down
    HALF_OPEN = "half_open"  # Test de récupération

class CircuitBreaker:
    def __init__(self, failure_threshold: int = 5, 
                 timeout: int = 60, 
                 expected_exception: type = Exception):
        self.failure_threshold = failure_threshold
        self.timeout = timeout
        self.expected_exception = expected_exception
        self.failure_count = 0
        self.last_failure_time = None
        self.state = CircuitState.CLOSED
    
    def call(self, func: Callable, *args, **kwargs):
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.timeout:
                self.state = CircuitState.HALF_OPEN
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = func(*args, **kwargs)
            self._on_success()
            return result
        except self.expected_exception as e:
            self._on_failure()
            raise
    
    def _on_success(self):
        self.failure_count = 0
        self.state = CircuitState.CLOSED
    
    def _on_failure(self):
        self.failure_count += 1
        self.last_failure_time = time.time()
        
        if self.failure_count >= self.failure_threshold:
            self.state = CircuitState.OPEN

# Usage
payment_circuit = CircuitBreaker(failure_threshold=5, timeout=60)

def process_payment(amount: float):
    return payment_circuit.call(
        external_payment_api.charge,
        amount=amount
    )
```

### 3.2 Rollback Automatique

#### CI/CD avec Détection d'Anomalies
```yaml
# .github/workflows/deploy-with-rollback.yml
name: Deploy with Auto-Rollback

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
      
      - name: Deploy to Production
        id: deploy
        run: |
          ./scripts/deploy.sh
          echo "deployment_id=$(date +%s)" >> $GITHUB_OUTPUT
      
      - name: Health Check
        id: health
        run: |
          for i in {1..10}; do
            if curl -f http://production.example.com/health; then
              echo "Health check passed"
              exit 0
            fi
            sleep 10
          done
          echo "Health check failed"
          exit 1
      
      - name: Monitor Metrics (5 minutes)
        if: success()
        run: |
          python scripts/monitor_deployment.py \
            --duration 300 \
            --error-rate-threshold 1.0 \
            --latency-threshold 1000
      
      - name: Rollback on Failure
        if: failure()
        run: |
          echo "Deployment failed, initiating rollback"
          ./scripts/rollback.sh ${{ steps.deploy.outputs.deployment_id }}
          
      - name: Notify Team
        if: always()
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          text: |
            Deployment ${{ job.status }}
            Commit: ${{ github.sha }}
            Author: ${{ github.actor }}
```

#### Script de Monitoring
```python
# scripts/monitor_deployment.py
import time
import requests
import sys
from dataclasses import dataclass
from typing import List

@dataclass
class Metrics:
    error_rate: float
    latency_p95: float
    requests_per_second: float

def fetch_metrics(prometheus_url: str) -> Metrics:
    """Récupère les métriques depuis Prometheus"""
    # Requêtes Prometheus pour error rate
    error_rate_query = 'rate(http_requests_total{status=~"5.."}[1m])'
    error_rate = requests.get(
        f"{prometheus_url}/api/v1/query",
        params={"query": error_rate_query}
    ).json()['data']['result'][0]['value'][1]
    
    # Latence p95
    latency_query = 'histogram_quantile(0.95, http_request_duration_seconds_bucket[1m])'
    latency_p95 = requests.get(
        f"{prometheus_url}/api/v1/query",
        params={"query": latency_query}
    ).json()['data']['result'][0]['value'][1]
    
    return Metrics(
        error_rate=float(error_rate),
        latency_p95=float(latency_p95) * 1000,  # Conversion en ms
        requests_per_second=0  # À implémenter
    )

def monitor_deployment(duration: int, 
                       error_rate_threshold: float,
                       latency_threshold: float) -> bool:
    """
    Surveille le déploiement pendant une durée donnée.
    Retourne True si tout est OK, False sinon.
    """
    prometheus_url = "http://prometheus.internal:9090"
    start_time = time.time()
    
    while time.time() - start_time < duration:
        metrics = fetch_metrics(prometheus_url)
        
        print(f"Error Rate: {metrics.error_rate}% | "
              f"Latency p95: {metrics.latency_p95}ms")
        
        # Vérification des seuils
        if metrics.error_rate > error_rate_threshold:
            print(f"ERROR: Error rate {metrics.error_rate}% exceeds threshold")
            return False
        
        if metrics.latency_p95 > latency_threshold:
            print(f"ERROR: Latency {metrics.latency_p95}ms exceeds threshold")
            return False
        
        time.sleep(30)  # Check toutes les 30 secondes
    
    print("Deployment monitoring completed successfully")
    return True

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=int, required=True)
    parser.add_argument("--error-rate-threshold", type=float, required=True)
    parser.add_argument("--latency-threshold", type=float, required=True)
    args = parser.parse_args()
    
    success = monitor_deployment(
        duration=args.duration,
        error_rate_threshold=args.error_rate_threshold,
        latency_threshold=args.latency_threshold
    )
    
    sys.exit(0 if success else 1)
```

### 3.3 Blue-Green Deployment

```
┌─────────────────────────────────────────────────────────┐
│               BLUE-GREEN DEPLOYMENT                      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Phase 1: Déploiement Green                             │
│  ┌────────────┐              ┌────────────┐            │
│  │   Blue     │◄─── 100% ────┤   Router   │            │
│  │ (Current)  │              └────────────┘            │
│  └────────────┘                                         │
│  ┌────────────┐                                         │
│  │   Green    │ (Déploiement en cours)                 │
│  │   (New)    │                                         │
│  └────────────┘                                         │
│                                                          │
│  Phase 2: Tests Green                                   │
│  ┌────────────┐              ┌────────────┐            │
│  │   Blue     │◄─── 100% ────┤   Router   │            │
│  │ (Current)  │              └────────────┘            │
│  └────────────┘                     │                   │
│  ┌────────────┐                     │                   │
│  │   Green    │◄──── Tests ─────────┘                   │
│  │   (New)    │                                         │
│  └────────────┘                                         │
│                                                          │
│  Phase 3: Switch                                        │
│  ┌────────────┐              ┌────────────┐            │
│  │   Blue     │              │   Router   │            │
│  │   (Old)    │              └──────┬─────┘            │
│  └────────────┘                     │                   │
│  ┌────────────┐                     │                   │
│  │   Green    │◄─── 100% ───────────┘                   │
│  │ (Current)  │                                         │
│  └────────────┘                                         │
└─────────────────────────────────────────────────────────┘
```

**Script de Déploiement** :
```bash
#!/bin/bash
# scripts/blue-green-deploy.sh

set -e

CURRENT_ENV=$(cat /var/app/current_environment)
NEW_ENV="green"

if [ "$CURRENT_ENV" = "green" ]; then
    NEW_ENV="blue"
fi

echo "Current environment: $CURRENT_ENV"
echo "Deploying to: $NEW_ENV"

# 1. Déployer sur le nouvel environnement
echo "Deploying application to $NEW_ENV..."
docker-compose -f docker-compose.$NEW_ENV.yml up -d

# 2. Attendre que l'application soit prête
echo "Waiting for $NEW_ENV to be healthy..."
for i in {1..30}; do
    if curl -f http://$NEW_ENV.internal:8000/health; then
        echo "$NEW_ENV is healthy"
        break
    fi
    sleep 10
done

# 3. Tests de smoke
echo "Running smoke tests on $NEW_ENV..."
python tests/smoke_tests.py --env $NEW_ENV

# 4. Switch du router
echo "Switching router to $NEW_ENV..."
cp /etc/nginx/sites-available/$NEW_ENV /etc/nginx/sites-enabled/default
nginx -s reload

# 5. Monitoring post-switch
echo "Monitoring $NEW_ENV for 5 minutes..."
python scripts/monitor_deployment.py --duration 300

# 6. Si tout va bien, arrêter l'ancien environnement
echo "Stopping old environment $CURRENT_ENV..."
docker-compose -f docker-compose.$CURRENT_ENV.yml down

# 7. Mettre à jour l'environnement courant
echo $NEW_ENV > /var/app/current_environment

echo "Deployment completed successfully!"
```

---

**Version** : 1.0.0  
**Date de création** : 2026-01-21  
**Statut** : Actif  
**Révision** : Trimestrielle
