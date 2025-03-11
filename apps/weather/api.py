import os
import requests

WEATHER_API_URL = "http://api.weatherapi.com/v1/forecast.json"
OPEN_WEATHER_KEY = os.getenv("OPEN_WEATHER_KEY")


def fetch_historical_weather(city_name, days = 7):
        params = {
            "key": OPEN_WEATHER_KEY,
            "q": city_name,
            "days": days,
            "aqi": "no",
            "alerts": "no"
        }

        response = requests.get(WEATHER_API_URL, params)

        if response.status_code == 200:
            return response.json()

        return None
