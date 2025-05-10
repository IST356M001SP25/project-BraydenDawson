import json
from code.extract import get_weather_data

def test_get_weather_data_from_cache(tmp_path):
    # Create a fake cached JSON file
    city = "testcity"
    api_key = "fakekey"
    cache_file = tmp_path / f"weather_{city}.json"
    sample_data = {"cod": "200", "list": [{"dt_txt": "2024-01-01 00:00:00", "main": {"temp": 10, "humidity": 90}, "weather": [{"icon": "01d", "description": "clear sky"}]}]}

    cache_file.write_text(json.dumps(sample_data))

    # Monkey patch cache path
    import code.extract
    original_os_path = code.extract.os.path
    code.extract.os.path.exists = lambda path: True
    code.extract.open = lambda path, mode='r': open(cache_file, mode)

    result = get_weather_data(city, api_key, use_cache=True)
    assert result["cod"] == "200"
    assert "list" in result

    # Restore patched os.path
    code.extract.os.path = original_os_path
