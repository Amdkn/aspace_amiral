import subprocess
import json
import time
import urllib.request
import sys

def check_containers():
    print("Checking Docker containers...")
    try:
        result = subprocess.run(
            ["docker", "compose", "ps", "--format", "json"],
            capture_output=True,
            text=True,
            cwd="01_PROJECTS/infrastructure_r1"
        )
        if result.returncode != 0:
            print(f"Error running docker compose ps: {result.stderr}")
            return False
        
        # Parse JSON output (docker compose ps can return a list of JSON objects or one JSON list)
        try:
            containers = json.loads(result.stdout)
            if not isinstance(containers, list):
                containers = [containers]
        except json.JSONDecodeError:
            # Handle non-list output from older docker compose versions
            lines = result.stdout.strip().split('\n')
            containers = [json.loads(line) for line in lines if line]

        all_running = True
        for container in containers:
            name = container.get("Name") or container.get("Service")
            status = container.get("Status") or container.get("State")
            print(f"Container {name}: {status}")
            if "running" not in status.lower() and "up" not in status.lower():
                all_running = False
        
        return all_running
    except Exception as e:
        print(f"Exception during container check: {e}")
        return False

def check_n8n():
    print("Checking n8n endpoint...")
    url = "http://127.0.0.1:5678/healthz"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            if response.getcode() == 200:
                print("n8n health check: OK")
                return True
    except Exception as e:
        print(f"n8n health check failed: {e}")
    return False

if __name__ == "__main__":
    if check_containers() and check_n8n():
        print("✅ R1 Infrastructure is HEALTHY")
        sys.exit(0)
    else:
        print("❌ R1 Infrastructure health check FAILED")
        sys.exit(1)
