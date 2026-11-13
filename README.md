# 🌦️ Weather API con FastAPI y OpenWeatherMap

API REST ligera, modular y segura desarrollada en Python utilizando **FastAPI** para consultar el estado del clima en tiempo real de cualquier ciudad mediante la integración con la API de **OpenWeatherMap**.

---

## 🚀 Características principales
- **Arquitectura Modular:** Separación clara de responsabilidades entre el punto de entrada de la aplicación (`main.py`) y la lógica de negocio de consumo externo (`services/weather_client.py`).
- **Manejo Seguro de Credenciales:** Uso de variables de entorno mediante `python-dotenv` para proteger la API Key.
- **Control Robusto de Excepciones:** Conversión de errores externos y códigos de estado en respuestas HTTP claras (`404` para ciudades no encontradas, `500` para fallos del servidor).
- **Documentación Interactiva Automática:** Incorporación nativa de Swagger UI y ReDoc a través de FastAPI.

---

## 🛠️ Tecnologías y Dependencias
* **Python 3.10+**
* **FastAPI** (Framework web asíncrono)
* **Uvicorn** (Servidor ASGI de alto rendimiento)
* **HTTPX** (Cliente HTTP moderno para peticiones asíncronas/síncronas)
* **Python-dotenv** (Gestión de variables de entorno)

---

## 📁 Estructura del Proyecto

```text
segundo-proyecto/
│
├── services/
│   └── weather_client.py   # Lógica de cliente HTTP y consumo de OpenWeatherMap
├── .env                    # Variables de entorno privadas (No se sube a Git)
├── .env.example            # Plantilla pública de configuración
├── .gitignore              # Archivos y carpetas ignorados por Git
├── main.py                 # Punto de entrada de la aplicación FastAPI y rutas
└── requirements.txt        # Dependencias del proyecto
