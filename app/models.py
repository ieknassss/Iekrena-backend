from pydantic import BaseModel


class Reserva(BaseModel):
    nombre_completo: str
    email: str
    telefono: str
    pais: str
    destino: str
    fecha_viaje: str
    cantidad_personas: int
    metodo_pago: str
    total: str