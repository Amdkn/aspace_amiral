"""
📡 SIGNAL PULSE: LE CŒUR DE LIFE OS
-----------------------------------
Ce script est le capteur principal de R0. Il remplace la boucle infinie "stupide" par une écoute active.
Il détecte les "Pulsations" (Business KPIs) et les "Signaux de Vie" (État du système/Agent).

ARCHITECTURE:
1. LISTEN (Écoute) : Vérifie les sources (Fichiers, APIs, Docker R1).
2. DECIDE (Décision) : Applique les règles de gestion (E-Myth / Who Not How).
3. ACT (Action) : Déclenche R0 (Antigravity) ou délègue à R1 (n8n).
"""

import os
import json
import time
from datetime import datetime

# CONFIGURATION
SIGNAL_FILE = "tracks.md"
BUSINESS_PULSE_FILE = "03_RESOURCES/05_TEMPLATES/business_kpi.json"
AGENT_STATE_FILE = ".agent_state.json"

class SignalPulse:
    def __init__(self):
        self.last_check = datetime.now()
        print("✅ Signal Pulse Activé. En attente de signaux...")

    def check_life_os(self):
        """Vérifie l'état de santé du système (Life OS)"""
        # Simulation d'un check de santé (ex: est-ce que Docker R1 tourne ?)
        # TODO: Connecter au MCP Docker ici plus tard
        print(f"[{datetime.now().strftime('%H:%M:%S')}] 🩺 Life OS Scan: OPTIMAL")
        return True

    def check_business_pulse(self):
        """Vérifie les KPIs Business (Business OS)"""
        # Lit les objectifs actifs pour voir si on est en retard
        if os.path.exists(SIGNAL_FILE):
            with open(SIGNAL_FILE, 'r', encoding='utf-8') as f:
                content = f.read()
                if "[pulse:critical]" in content:
                    print("🚨 ALERTE BUSINESS: Tâche critique détectée !")
                    return "CRITICAL_TASK"
        return "NORMAL"

    def run_cycle(self):
        """Cycle d'exécution unique (Pas de boucle infinie bloquante)"""
        life_status = self.check_life_os()
        business_status = self.check_business_pulse()

        if business_status == "CRITICAL_TASK":
            self.trigger_antigravity()
        else:
            print("💤 Pas de signal critique. R0 en veille.")

    def trigger_antigravity(self):
        """Réveille l'Architecte (Toi/Moi)"""
        print("🚀 ACTIVATION ANTIGRAVITY demandée par le Business Pulse.")
        # Ici, on pourrait lancer une commande CLI via subprocess si nécessaire
        # subprocess.run(["gemini", "run", "conductor", "Alerte critique..."])

if __name__ == "__main__":
    # Exécution simple pour test (pas de loop infini ici pour l'instant)
    pulse = SignalPulse()
    pulse.run_cycle()
