from app.database import get_connection

conn = get_connection()
cursor = conn.cursor()

cursor.execute("SHOW TABLES")

tablas = cursor.fetchall()

for tabla in tablas:
    print(tabla[0])

cursor.close()
conn.close()