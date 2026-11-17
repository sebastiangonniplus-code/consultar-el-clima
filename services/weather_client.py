import httpx

class WeatherClient:
    def __init__(self,api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"


    def get_weather(self, ciudad: str):
        #Obtiene el clima en la ciudad actual.

         params = {
             "q": ciudad,
             "units": "metric",
             "lang": "es",
             "appid": self.api_key
         }

         respuesta = httpx.get(self.base_url, params=params)
         if respuesta.status_code == 404:
             raise ValueError("No se encontro la ciudad")

         elif respuesta.status_code != 200:
             raise RuntimeError(f"Error de OpenWeatherMap: {respuesta.status_code} - {respuesta.text}")
         else:
             return respuesta.json()     
