import pandas as pd
from code.transform import process_weather_data

def test_process_weather_data():
    raw_data = {
        "list": [
            {
                "dt_txt": "2024-01-01 00:00:00",
                "main": {"temp": 5.0, "humidity": 70},
                "weather": [{"icon": "04d", "description": "cloudy"}]
            }
        ]
    }

    df = process_weather_data(raw_data)
    assert isinstance(df, pd.DataFrame)
    assert "temperature" in df.columns
    assert "humidity" in df.columns
    assert "icon" in df.columns
    assert "description" in df.columns
    assert df["temperature"].iloc[0] == 5.0
    assert df["humidity"].iloc[0] == 70
