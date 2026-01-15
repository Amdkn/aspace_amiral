import unittest
import os
import json
from ..pulse_logger import log_pulse

class TestPulseLogger(unittest.TestCase):
    def setUp(self):
        self.test_file = "03_RESOURCES/05_TEMPLATES/business_kpi.json"
        # Backup original file if it exists
        self.backup_content = None
        if os.path.exists(self.test_file):
            with open(self.test_file, 'r') as f:
                self.backup_content = f.read()

    def tearDown(self):
        # Restore original file
        if self.backup_content is not None:
            with open(self.test_file, 'w') as f:
                f.write(self.backup_content)

    def test_log_pulse_appends_data(self):
        metric = "test_metric"
        value = 100
        log_pulse(metric, value)
        
        with open(self.test_file, 'r') as f:
            data = json.load(f)
        
        self.assertIn("pulses", data)
        self.assertTrue(len(data["pulses"]) > 0)
        last_pulse = data["pulses"][-1]
        self.assertEqual(last_pulse["metric"], metric)
        self.assertEqual(last_pulse["value"], value)
        self.assertIn("timestamp", last_pulse)

if __name__ == "__main__":
    unittest.main()
