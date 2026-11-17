# 🌦️ Weather API con FastAPI, OpenWeatherMap y Frontend Web

Aplicación web full-stack ligera, modular y moderna desarrollada en Python (**FastAPI**) y un cliente web con **HTML, JavaScript y Bootstrap 5** para consultar el estado del clima en tiempo real de cualquier ciudad mediante la integración con la API de **OpenWeatherMap**.

---

## 🚀 Características principales
- **Arquitectura Modular (Backend):** Separación clara entre el punto de entrada (`main.py`), la lógica de cliente HTTP (`services/weather_client.py`), los esquemas de validación con **Pydantic** (`schemas.py`) y la interfaz visual.
- **Frontend Interactivo:** Interfaz web moderna con Bootstrap 5 que consume la API de forma asíncrona mediante JavaScript (`fetch`) sin recargar la página.
- **Soporte CORS:** Configurado con `CORSMiddleware` en FastAPI para permitir la comunicación fluida entre el servidor y el cliente web.
- **Manejo Seguro de Credenciales:** Uso de variables de entorno mediante `python-dotenv` para proteger la API Key.
- **Control Robusto de Excepciones:** Conversión de errores externos en respuestas HTTP claras (`404` para ciudades no encontradas, `500` para fallos del servidor).
- **Documentación Interactiva Automática:** Swagger UI y ReDoc nativos de FastAPI.

---

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python 3.10+, FastAPI, Uvicorn, HTTPX, Pydantic, Python-dotenv.
* **Frontend:** HTML5, CSS3, JavaScript (Async/Await, Fetch API), Bootstrap 5.

---

## 📁 Estructura del Proyecto

```text
segundo-proyecto/
│
├── services/
│   └── weather_client.py   # Lógica de cliente HTTP y consumo de OpenWeatherMap
├── frontend/ (o raíz)      # Archivos de la interfaz visual
│   ├── index.html          # Estructura y diseño con Bootstrap
│   └── script.js           # Lógica de consumo de la API con Fetch
├── .env                    # Variables de entorno privadas (No se sube a Git)
├── .env.example            # Plantilla pública de configuración
├── .gitignore              # Archivos y carpetas ignorados por Git
├── main.py                 # Servidor FastAPI, rutas y configuración de CORS
├── schemas.py              # Modelos de validación con Pydantic
└── requirements.txt        # Dependencias de Python




⚙️ Instalación y Configuración Local

Sigue estos pasos para clonar y poner en marcha el proyecto en tu máquina local:
1. Clonar el repositorio
Bash

git clone [https://github.com/tu-usuario/nombre-del-repositorio.git](https://github.com/tu-usuario/nombre-del-repositorio.git)
cd nombre-del-repositorio

2. Crear y activar el entorno virtual

    En Windows (Git Bash / Terminal):
    Bash

    python -m venv venv
    source venv/Scripts/activate

    En macOS / Linux:
    Bash

    python3 -m venv venv
    source venv/bin/activate

3. Instalar las dependencias de Python
Bash

pip install -r requirements.txt

4. Configurar las variables de entorno

Crea un archivo llamado .env en la raíz del proyecto y añade tu clave de OpenWeatherMap:
Fragmento de código

WEATHER_API_KEY=tu_api_key_real_aqui

(Puedes guiarte del archivo .env.example).
🏃‍♂️ Ejecución de la Aplicación
1. Iniciar el servidor backend (FastAPI)

Ejecuta Uvicorn en tu terminal:
Bash

uvicorn main:app --reload

El servidor backend quedará activo en: http://127.0.0.1:8000
2. Abrir la interfaz web (Frontend)

    Haz doble clic en el archivo index.html para abrirlo en tu navegador web.

    Escribe una ciudad en el buscador y presiona Buscar para ver los datos meteorológicos en tiempo real.

📖 Documentación de la API (Swagger UI)

Si deseas probar los endpoints directamente desde la documentación técnica, puedes ingresar a:

    Swagger UI: http://127.0.0.1:8000/docs

    Endpoint principal: GET /api/weather/{city}

🛡️ Buenas Prácticas de Seguridad

El repositorio incluye un archivo .gitignore optimizado para excluir entornos virtuales (venv/), archivos de caché (__pycache__/) y credenciales sensibles (.env).


---

Una vez que lo actualices en tu archivo `README.md`, recuerda hacer los clásicos comandos de Git para dejar tu repositorio en GitHub al día:
```bash
git add README.md
git commit -m "docs: actualizar README con detalles del frontend y CORS"
git push origin main