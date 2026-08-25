import sqlite3
import json

db_path = '/var/lib/docker/volumes/open-webui/_data/webui.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

print("=== EXISTING SKILLS IN DB ===")
c.execute("SELECT id, name, description, is_active, meta FROM skill")
skills = c.fetchall()
print(f"Total skills: {len(skills)}")
for s in skills:
    print(f" - [{s[0]}] Name: {s[1]} | Desc: {s[2]} | Active: {s[3]} | Meta: {s[4]}")

print("\n=== EXISTING TOOLS IN DB ===")
c.execute("SELECT id, name, meta FROM tool")
tools = c.fetchall()
print(f"Total tools: {len(tools)}")
for t in tools:
    print(f" - [{t[0]}] Name: {t[1]}")

print("\n=== EXISTING FUNCTIONS IN DB ===")
c.execute("SELECT id, name, type, is_active FROM function")
funcs = c.fetchall()
print(f"Total functions: {len(funcs)}")
for f in funcs:
    print(f" - [{f[0]}] Name: {f[1]} | Type: {f[2]} | Active: {f[3]}")

conn.close()
