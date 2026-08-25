import sqlite3
import json
import time
from pathlib import Path

# Load skills export
with open('/tmp/openwebui_skills_export.json', 'r', encoding='utf-8') as f:
    skills_data = json.load(f)

db_path = '/var/lib/docker/volumes/open-webui/_data/webui.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

admin_user_id = '33a21871-719a-42cb-9176-6fced144fbaa'
now = int(time.time())

inserted = 0
updated = 0

for item in skills_data:
    skill_id = item['id']
    name = item['name']
    description = item['description']
    content = item['content']
    meta = json.dumps({"manifest": {"name": name, "description": description}}, ensure_ascii=False)
    
    # Check if skill exists by id or name
    c.execute("SELECT id FROM skill WHERE id = ? OR name = ?", (skill_id, name))
    row = c.fetchone()
    
    if row:
        existing_id = row[0]
        c.execute("""
            UPDATE skill 
            SET name = ?, description = ?, content = ?, meta = ?, is_active = 1, updated_at = ?
            WHERE id = ?
        """, (name, description, content, meta, now, existing_id))
        updated += 1
        print(f"🔄 Updated skill: {name} (id: {existing_id})")
    else:
        c.execute("""
            INSERT INTO skill (id, user_id, name, description, content, meta, is_active, updated_at, created_at)
            VALUES (?, ?, ?, ?, ?, ?, 1, ?, ?)
        """, (skill_id, admin_user_id, name, description, content, meta, now, now))
        inserted += 1
        print(f"✅ Inserted skill: {name} (id: {skill_id})")

conn.commit()

# Verify
c.execute("SELECT id, name, is_active FROM skill ORDER BY name")
all_skills = c.fetchall()
print(f"\n📊 Total active skills in Open WebUI: {len(all_skills)}")
for s in all_skills:
    print(f" • [{s[0]}] {s[1]} (active: {s[2]})")

conn.close()
