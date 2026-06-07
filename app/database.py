import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        port=int(os.getenv("MYSQL_PORT")),
        database=os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
    )

if __name__ == "__main__":
    try:
        conn = get_connection()
        print("Conexión exitosa con Aiven MySQL")
        conn.close()
    except Exception as e:
        print("Error:", e)