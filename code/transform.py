# code/transform.py
import pandas as pd

def process_weather_data(raw_data: dict) -> pd.DataFrame:
    data = raw_data['list']
    df = pd.DataFrame([{
        "datetime": entry["dt_txt"],
        "temperature": entry["main"]["temp"],
        "humidity": entry["main"]["humidity"]
    } for entry in data])
    df["datetime"] = pd.to_datetime(df["datetime"])
    return df
