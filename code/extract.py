# code/extract.py
import requests
import os

def get_weather_data(city: str, api_key: str) -> dict:
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    return response.json()
