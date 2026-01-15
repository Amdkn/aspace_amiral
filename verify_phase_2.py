import subprocess
import json
import os
import sys

# Ensure we use the correct python executable
python_exe = sys.executable
cli_path = "01_PROJECTS/pulse.py"
kpi_file = "03_RESOURCES/05_TEMPLATES/business_kpi.json"

print("--- PULSE CLI VERIFICATION ---")

# 1. Log a pulse via CLI
metric = "manual_cli_test"
value = "123.45"
print(f"Logging pulse via CLI: {metric} = {value}...")

result = subprocess.run(
    [python_exe, cli_path, "--metric", metric, "--value", value],
    capture_output=True,
    text=True
)

if result.returncode == 0 and "SUCCESS" in result.stdout:
    print(f"CLI Success: {result.stdout.strip()}")
else:
    print(f"CLI FAILED: {result.stderr}")
    sys.exit(1)

# 2. Verify in JSON
with open(kpi_file, "r") as f:
    data = json.load(f)
    last_pulse = data["pulses"][-1]
    if last_pulse["metric"] == metric and float(last_pulse["value"]) == float(value):
        print(f"SUCCESS: Verified pulse in {kpi_file}!")
        print(f"Entry: {last_pulse}")
    else:
        print("FAILED: Could not find the pulse in JSON file.")
        sys.exit(1)
