from app.database import get_connection

with open("database/schema.sql", "r", encoding="utf-8") as file:
    sql_script = file.read()

conn = get_connection()
cursor = conn.cursor()

for query in sql_script.split(";"):
    if query.strip():
        cursor.execute(query)

conn.commit()
cursor.close()
conn.close()

print("Tablas creadas correctamente en Aiven MySQL")