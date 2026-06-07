from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import Reserva
from app.database import get_connection

app = FastAPI(title="Iekrena Trips API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def inicio():
    return {"mensaje": "Backend de Iekrena Trips funcionando correctamente"}


@app.post("/reservas")
def crear_reserva(reserva: Reserva):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO reservas 
    (nombre_completo, email, telefono, pais, destino, fecha_viaje, cantidad_personas, metodo_pago, total)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        reserva.nombre_completo,
        reserva.email,
        reserva.telefono,
        reserva.pais,
        reserva.destino,
        reserva.fecha_viaje,
        reserva.cantidad_personas,
        reserva.metodo_pago,
        reserva.total,
    )

    cursor.execute(sql, valores)
    conn.commit()

    reserva_id = cursor.lastrowid

    cursor.close()
    conn.close()

    return {
        "mensaje": "Reserva guardada correctamente en MySQL",
        "id": reserva_id,
        "reserva": reserva
    }


@app.get("/reservas")
def obtener_reservas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM reservas ORDER BY id DESC")
    reservas = cursor.fetchall()

    cursor.close()
    conn.close()

    return reservas