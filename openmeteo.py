import requests
from .base import WeatherAbstract

class OpenMeteoProvider(WeatherAbstract):
    base_url = "https://api.open-meteo.com/v1/forecast"
    
    def get_current_weather(self, lat, lon):
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,relative_humidity_2m"
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        return {
            "temp": data["current"]["temperature_2m"],
            "humidity": data["current"]["relative_humidity_2m"]
        }