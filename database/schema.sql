CREATE TABLE IF NOT EXISTS ofertas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    ubicacion VARCHAR(150) NOT NULL,
    categoria VARCHAR(100) NOT NULL,
    imagen VARCHAR(255),
    precio DECIMAL(10,2) NOT NULL,
    duracion VARCHAR(100),
    calificacion DECIMAL(2,1),
    descripcion TEXT
);

CREATE TABLE IF NOT EXISTS reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_completo VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL,
    telefono VARCHAR(50) NOT NULL,
    pais VARCHAR(100) NOT NULL,
    destino VARCHAR(150) NOT NULL,
    fecha_viaje DATE,
    cantidad_personas INT NOT NULL,
    metodo_pago VARCHAR(100) NOT NULL,
    total VARCHAR(50),
    fecha_reserva TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);