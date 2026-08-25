import sqlite3
import json
import time
import uuid
from pathlib import Path

# Load prompts export
with open('/tmp/openwebui_prompts_export.json', 'r', encoding='utf-8') as f:
    prompts_data = json.load(f)

db_path = '/var/lib/docker/volumes/open-webui/_data/webui.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

admin_user_id = '33a21871-719a-42cb-9176-6fced144fbaa'
now = int(time.time())

inserted = 0
updated = 0

for item in prompts_data:
    raw_cmd = item['command'].lstrip('/')
    name = item['title']
    content = item['content']
    
    # Check if prompt with command already exists
    c.execute("SELECT id FROM prompt WHERE command = ?", (raw_cmd,))
    row = c.fetchone()
    
    if row:
        prompt_id = row[0]
        c.execute("""
            UPDATE prompt 
            SET name = ?, content = ?, updated_at = ?, is_active = 1, version_id = ?
            WHERE id = ?
        """, (name, content, now, str(uuid.uuid4()), prompt_id))
        updated += 1
        print(f"🔄 Updated prompt: /{raw_cmd} ({name})")
    else:
        new_id = str(uuid.uuid4())
        version_id = str(uuid.uuid4())
        c.execute("""
            INSERT INTO prompt (id, command, user_id, name, content, data, meta, is_active, version_id, tags, created_at, updated_at)
            VALUES (?, ?, ?, ?, ?, '{}', '{}', 1, ?, '[]', ?, ?)
        """, (new_id, raw_cmd, admin_user_id, name, content, version_id, now, now))
        inserted += 1
        print(f"✅ Inserted prompt: /{raw_cmd} ({name})")

conn.commit()

# Verify
c.execute("SELECT command, name FROM prompt ORDER BY command")
all_prompts = c.fetchall()
print(f"\n📊 Total active prompts in Open WebUI: {len(all_prompts)}")
for p in all_prompts:
    print(f" • /{p[0]} -> {p[1]}")

conn.close()
