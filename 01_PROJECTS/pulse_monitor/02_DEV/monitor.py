import os
import json

def check_pulse():
    paths = ["01_PROJECTS", "02_AREAS", "03_RESOURCES", "04_ARCHIVES"]
    status = {}
    
    for path in paths:
        exists = os.path.exists(path)
        status[path] = "OK" if exists else "MISSING"
    
    return status

if __name__ == "__main__":
    pulse = check_pulse()
    print(json.dumps(pulse, indent=4))
