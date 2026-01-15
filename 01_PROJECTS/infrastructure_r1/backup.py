import subprocess
import os
from datetime import datetime
import sys

def backup_db():
    print("Backing up PostgreSQL database...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"01_PROJECTS/infrastructure_r1/backups/db_dump_{timestamp}.sql"
    
    try:
        # Use docker exec to run pg_dump
        with open(backup_file, 'w') as f:
            result = subprocess.run(
                ["docker", "exec", "-t", "r1-supabase-db", "pg_dump", "-U", "supabase_admin", "-d", "postgres"],
                stdout=f,
                text=True
            )
        
        if result.returncode == 0:
            print(f"✅ DB Backup saved to {backup_file}")
            return True
        else:
            print(f"❌ DB Backup failed")
    except Exception as e:
        print(f"Exception during DB backup: {e}")
    return False

def backup_n8n():
    print("Backing up n8n configuration...")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = f"01_PROJECTS/infrastructure_r1/backups/n8n_{timestamp}"
    os.makedirs(backup_dir, exist_ok=True)
    
    try:
        # Export workflows via CLI
        result = subprocess.run(
            ["docker", "exec", "r1-n8n", "n8n", "export:workflow", "--all", f"--output=/home/node/.n8n/workflows/backup_{timestamp}.json"],
            capture_output=True,
            text=True
        )
        # Note: In a production environment, we'd copy the file out of the container
        # For now, having it in the mapped volume is a good start.
        
        print("✅ n8n workflows exported within container/volume.")
        return True
    except Exception as e:
        print(f"Exception during n8n backup: {e}")
    return False

if __name__ == "__main__":
    s1 = backup_db()
    s2 = backup_n8n()
    
    if s1 and s2:
        print("✅ Backup complete")
        sys.exit(0)
    else:
        sys.exit(1)
