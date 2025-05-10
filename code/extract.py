import requests
import os
import json

def get_weather_data(city: str, api_key: str, use_cache=True) -> dict:
    cache_dir = "cache"
    os.makedirs(cache_dir, exist_ok=True)

    cache_path = os.path.join(cache_dir, f"weather_{city.lower()}.json")

    # Load from cache
    if use_cache and os.path.exists(cache_path):
        with open(cache_path, 'r') as f:
            return json.load(f)

    # Fetch from API
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()

    # Save to cache
    with open(cache_path, 'w') as f:
        json.dump(data, f)

    return data
