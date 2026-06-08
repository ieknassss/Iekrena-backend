# IEKRENA TRIPS - Backend

## Descripción del Proyecto

Este backend forma parte del sistema web **IEKRENA TRIPS**, una plataforma turística creada para gestionar reservas de viajes y conectar el formulario del frontend con una base de datos MySQL en la nube.

El servidor permite guardar reservas realizadas por los usuarios, consultar las reservas desde el panel administrativo y mantener la comunicación entre el frontend desarrollado en Reflex y la base de datos alojada en Aiven.

---

## Tecnologías Utilizadas

* Python
* FastAPI
* MySQL
* Aiven MySQL
* Uvicorn
* Python-dotenv
* Git y GitHub

---

## Funcionalidades Implementadas

* Conexión con base de datos MySQL en Aiven.
* Creación de reservas desde el frontend.
* Consulta de reservas guardadas.
* API documentada automáticamente con Swagger.
* Integración con el panel administrativo.
* Uso de variables de entorno para proteger datos sensibles.

---

## Estructura de Carpetas

```text
Iekrena-backend/
│
├── app/
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── database/
│   └── schema.sql
│
├── .env
├── requirements.txt
└── README.md
```

---

## Cómo instalar y ejecutar

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/iekrena-backend.git
```

### 2. Entrar a la carpeta del proyecto

```bash
cd Iekrena-backend
```

### 3. Crear entorno virtual

```bash
python -m venv venv
```

### 4. Activar entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

### 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 6. Configurar variables de entorno

Crear un archivo `.env` con los datos de conexión:

```env
MYSQL_HOST=tu_host
MYSQL_PORT=tu_puerto
MYSQL_DATABASE=defaultdb
MYSQL_USER=tu_usuario
MYSQL_PASSWORD=tu_contraseña
```

### 7. Ejecutar el servidor

```bash
uvicorn app.main:app --reload --port 8001
```

### 8. Abrir Swagger

```text
http://127.0.0.1:8001/docs
```

---

## Endpoints Principales

### Crear reserva

```http
POST /reservas
```

Guarda una nueva reserva en la base de datos.

### Obtener reservas

```http
GET /reservas
```

Devuelve todas las reservas guardadas.

---

## Créditos y Enlaces Útiles

Proyecto desarrollado como parte del proyecto académico **IEKRENA TRIPS** del área de Técnico en Informática.

**Integrantes:**
Lorena Duran Reyes
Iekna Frank

**Colegio:** CAFAM
**Área:** Técnico en Informática

### Enlaces útiles

* FastAPI: https://fastapi.tiangolo.com/
* Aiven: https://aiven.io/
* MySQL: https://www.mysql.com/
* Render: https://render.com/
* GitHub: https://github.com/
