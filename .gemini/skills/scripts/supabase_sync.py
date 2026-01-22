import os
import json
import subprocess
from pathlib import Path

# Paths
ROOT_DIR = Path("c:/Users/amado/Documents/A'Space OS/00_Amiral")
OS_DEFS_FILE = ROOT_DIR / "01_PROJECTS/aspace-os-v1/src/data/osDefinitions.js"
DB_CONTAINER = "r1-supabase-db"
DB_USER = "supabase_admin"
DB_NAME = "postgres"

def extract_json_from_js(file_path):
    """
    Roughly extracts the object literal from a JS file.
    In a real scenario, we'd use a JS parser, but for A'Space V1, 
    we look for the 'osData' constant.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        # Find everything between 'export const osData = {' and the last '};'
        start_marker = "export const osData = "
        start_idx = content.find(start_marker) + len(start_marker)
        # Assuming the object ends at the last };
        end_idx = content.rfind("};") + 1
        json_str = content[start_idx:end_idx]
        
        # Clean up JS-isms (trailing commas, etc.) for basic JSON parsing
        # This is high-risk if objects are complex, but keeping it simple for now
        return json_str

def sync_to_supabase(data_str):
    """
    Syncs the telemetry data to Supabase using docker exec and psql.
    """
    # Create temporary SQL file
    sql_file = ROOT_DIR / "01_PROJECTS/infrastructure_r1/temp_sync.sql"
    
    # Example: Update entity status from telemetry
    # For MVP: We just log the sync event
    sql = f"""
    INSERT INTO pulses (metric, value, metadata)
    VALUES ('os_sync_event', 100, '{data_str.replace("'", "''")}'::jsonb);
    """
    
    with open(sql_file, "w", encoding="utf-8") as f:
        f.write(sql)
    
    # Execute SQL
    cmd = f'cat "{sql_file}" | docker exec -i {DB_CONTAINER} psql -U {DB_USER} -d {DB_NAME}'
    subprocess.run(cmd, shell=True, check=True)
    
    # Cleanup
    # os.remove(sql_file)

if __name__ == "__main__":
    print("[*] Starting Sovereign Sync: R0 -> R1")
    try:
        # data = extract_json_from_js(OS_DEFS_FILE)
        # sync_to_supabase(data)
        print("[+] Sync Logic Drafted. Awaiting full JS-to-JSON parser verification.")
    except Exception as e:
        print(f"[!] Sync Failed: {e}")
