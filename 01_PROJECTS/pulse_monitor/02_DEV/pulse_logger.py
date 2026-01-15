import json
import os
from datetime import datetime

KPI_FILE = "03_RESOURCES/05_TEMPLATES/business_kpi.json"

def log_pulse(metric, value):
    """
    Logs a business KPI pulse to business_kpi.json.
    """
    if not os.path.exists(KPI_FILE):
        data = {}
    else:
        with open(KPI_FILE, 'r') as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {}

    if "pulses" not in data:
        data["pulses"] = []

    new_pulse = {
        "timestamp": datetime.now().isoformat(),
        "metric": metric,
        "value": value
    }
    
    data["pulses"].append(new_pulse)
    
    with open(KPI_FILE, 'w') as f:
        json.dump(data, f, indent=4)
