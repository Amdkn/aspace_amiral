import json
import os
import sys
from datetime import datetime

# Cross-platform file locking
if sys.platform == 'win32':
    import msvcrt
else:
    import fcntl

KPI_FILE = "03_RESOURCES/05_TEMPLATES/business_kpi.json"

def log_pulse(metric, value):
    """
    Logs a business KPI pulse to business_kpi.json with cross-platform file locking.
    
    Uses msvcrt on Windows and fcntl on Unix-like systems.
    """
    if not os.path.exists(KPI_FILE):
        # Create file if it doesn't exist
        with open(KPI_FILE, 'w') as f:
            json.dump({"pulses": []}, f)

    with open(KPI_FILE, 'r+') as f:
        # Cross-platform file locking
        if sys.platform == 'win32':
            # Windows: Lock the first 10MB of the file (plenty for this JSON)
            lock_size = 10 * 1024 * 1024
            # LK_LOCK: Locks the specified bytes. If the bytes cannot be locked, 
            # the program immediately tries again after 1 second and continues 
            # to try until the bytes can be locked.
            msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, lock_size)
        else:
            # Unix/Linux/macOS: Use fcntl for file locking
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        
        try:
            f.seek(0)
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = {"pulses": []}

            if "pulses" not in data:
                data["pulses"] = []

            new_pulse = {
                "timestamp": datetime.now().isoformat(),
                "metric": metric,
                "value": value
            }
            
            data["pulses"].append(new_pulse)
            
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            
        finally:
            # Unlock the file
            if sys.platform == 'win32':
                f.seek(0)
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, lock_size)
            else:
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
