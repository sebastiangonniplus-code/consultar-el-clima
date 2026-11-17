from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from services.weather_client import WeatherClient
from schemas import ClimaRespuesta

load_dotenv() #Carga los datos del .env
app = FastAPI() #Crea la app.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite peticiones desde cualquier origen (ideal para desarrollo local)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],


api_cliente = os.getenv("WEATHER_API_KEY")

cliente = WeatherClient(api_cliente)

@app.get("/api/weather/{city}", response_model= ClimaRespuesta)
def obtener_clima(city:str):
    #Obtiene el clima de la ciudad ingresada por el usuario.
    
    try:
        data = cliente.get_weather(city)

        return{
            "ciudad": data["name"],
            "temperatura": data["main"]["temp"],
            "sensacion_termica": data["main"]["feels_like"],
            "humedad": data["main"]["humidity"],
            "descripcion": data["weather"][0]["description"]
        }

    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))