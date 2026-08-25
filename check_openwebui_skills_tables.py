import sqlite3

db_path = '/var/lib/docker/volumes/open-webui/_data/webui.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = [row[0] for row in c.fetchall()]
print("All tables in Open WebUI DB:")
for t in sorted(tables):
    print(f" - {t}")

print("\nSpecific schemas for function / tool / skill / filter:")
c.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND (name LIKE '%tool%' OR name LIKE '%func%' OR name LIKE '%skill%' OR name LIKE '%pipe%' OR name LIKE '%filter%')")
for name, sql in c.fetchall():
    print(f"--- Table: {name} ---")
    print(sql)

conn.close()
