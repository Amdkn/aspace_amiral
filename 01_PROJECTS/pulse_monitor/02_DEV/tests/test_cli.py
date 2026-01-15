import unittest
import subprocess
import json
import os
import sys

class TestPulseCLI(unittest.TestCase):
    def setUp(self):
        self.test_file = "03_RESOURCES/05_TEMPLATES/business_kpi.json"
        self.backup_content = None
        if os.path.exists(self.test_file):
            with open(self.test_file, 'r') as f:
                self.backup_content = f.read()

    def tearDown(self):
        if self.backup_content is not None:
            with open(self.test_file, 'w') as f:
                f.write(self.backup_content)

    def test_cli_log_pulse(self):
        # Path to pulse.py from project root
        cli_path = "01_PROJECTS/pulse.py"
        metric = "cli_metric"
        value = "50"
        
        # Run CLI command
        result = subprocess.run(
            [sys.executable, cli_path, "--metric", metric, "--value", value],
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"CLI STDOUT: {result.stdout}")
            print(f"CLI STDERR: {result.stderr}")
            
        self.assertEqual(result.returncode, 0)
        self.assertIn("SUCCESS: Successfully logged pulse", result.stdout)
        
        # Verify file content
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        
        last_pulse = data["pulses"][-1]
        self.assertEqual(last_pulse["metric"], metric)
        self.assertEqual(float(last_pulse["value"]), float(value))

if __name__ == "__main__":
    unittest.main()

