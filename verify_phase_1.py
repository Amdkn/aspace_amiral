import sys
import os
import json

# DEV folder path
dev_path = os.path.abspath(os.path.join(os.getcwd(), "01_PROJECTS", "pulse_monitor", "02_DEV"))

# Inject dev path
sys.path.append(dev_path)

try:
    import pulse_logger
    
    print("--- PULSE TEST STARTED ---")
    pulse_logger.log_pulse("manual_verification", 100)
    
    # Check JSON file
    kpi_file = "03_RESOURCES/05_TEMPLATES/business_kpi.json"
    with open(kpi_file, "r") as f:
        data = json.load(f)
        last_pulse = data["pulses"][-1]
        print(f"SUCCESS: Last pulse found: {last_pulse}")
        
except Exception as e:
    print(f"FAILURE: Verification failed: {e}")
