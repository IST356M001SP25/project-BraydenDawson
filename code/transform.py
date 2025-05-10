import pandas as pd

def process_weather_data(raw_data: dict) -> pd.DataFrame:
    data = raw_data['list']
    df = pd.DataFrame([{
        "datetime": entry["dt_txt"],
        "temperature": entry["main"]["temp"],
        "humidity": entry["main"]["humidity"],
        "icon": entry["weather"][0]["icon"],
        "description": entry["weather"][0]["description"]
    } for entry in data])
    df["datetime"] = pd.to_datetime(df["datetime"])
    return df
