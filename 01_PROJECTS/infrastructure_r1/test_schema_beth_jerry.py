import subprocess
import unittest
import sys

# Helper function to run SQL commands (adapted from test_db.py)
def run_sql(sql):
    try:
        result = subprocess.run(
            ["docker", "exec", "-i", "r1-supabase-db", "psql", "-U", "supabase_admin", "-d", "postgres", "-t", "-c", sql],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print(f"SQL Error: {result.stderr}")
            return None
        return result.stdout.strip()
    except Exception as e:
        print(f"Exception running SQL: {e}")
        return None

class TestBethJerrySchema(unittest.TestCase):
    
    def test_01_tables_exist(self):
        """Test that the required tables exist in the database."""
        tables = ["agent_signals", "kpi_metrics", "governance_state"]
        for table in tables:
            sql = f"SELECT to_regclass('public.{table}');"
            result = run_sql(sql)
            self.assertEqual(result, table, f"Table {table} does not exist.")

    def test_02_governance_state_columns(self):
        """Test governance_state columns specifically."""
        sql = "SELECT column_name FROM information_schema.columns WHERE table_name = 'governance_state';"
        output = run_sql(sql)
        # Check for key columns
        self.assertIn("status", output)
        self.assertIn("reason", output)
        self.assertIn("active", output)

if __name__ == '__main__':
    unittest.main()
