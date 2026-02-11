import requests
from .base import WeatherAbstract

class OpenWeatherProvider(WeatherAbstract):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    
    def __init__(self, api_key):
        self.api_key = api_key
    
    def get_current_weather(self, lat, lon):
        params = {"lat": lat, "lon": lon, "appid": self.api_key}
        response = requests.get(self.base_url, params=params)
        data = response.json()
        return {
            "temp": data["main"]["temp"] - 273.15,
            "humidity": data["main"]["humidity"]
        }