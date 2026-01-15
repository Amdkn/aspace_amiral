import subprocess
import json
import sys

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

def test_pulses_table():
    print("Testing pulses table...")
    # 1. Insert
    metric = "db_test_metric"
    value = 99.9
    run_sql(f"INSERT INTO pulses (metric, value) VALUES ('{metric}', {value});")
    
    # 2. Select
    res = run_sql(f"SELECT value FROM pulses WHERE metric = '{metric}' ORDER BY timestamp DESC LIMIT 1;")
    if res and float(res) == value:
        print("✅ Pulse Insert/Select: SUCCESS")
        return True
    else:
        print(f"❌ Pulse Insert/Select: FAILED (Got {res})")
        return False

def test_system_state_table():
    print("Testing system_state table...")
    key = "os_version"
    val = json.dumps({"version": "1.0.0", "codename": "Amiral"})
    run_sql(f"INSERT INTO system_state (key, value) VALUES ('{key}', '{val}') ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value;")
    
    res = run_sql(f"SELECT value FROM system_state WHERE key = '{key}';")
    if res:
        data = json.loads(res)
        if data["version"] == "1.0.0":
            print("✅ System State Insert/Select: SUCCESS")
            return True
    
    print(f"❌ System State Insert/Select: FAILED (Got {res})")
    return False

if __name__ == "__main__":
    s1 = test_pulses_table()
    s2 = test_system_state_table()
    
    if s1 and s2:
        print("✅ Database Schema and Connectivity VERIFIED")
        sys.exit(0)
    else:
        print("❌ Database Verification FAILED")
        sys.exit(1)
