from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
from services.weather_client import WeatherClient

load_dotenv() #Carga los datos del .env
app = FastAPI() #Crea la app.
api_cliente = os.getenv("WEATHER_API_KEY")

cliente = WeatherClient(api_cliente)

@app.get("/api/weather/{city}")
def obtener_clima(city:str):
    #Obtiene el clima de la ciudad ingresada por el usuario.
    try:
        return cliente.get_weather(city)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

