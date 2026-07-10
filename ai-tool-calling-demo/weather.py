def get_weather(city: str):
    weather = {
        "kolkata": {"temperature": 34, "condition": "Sunny"},
        "london": {"temperature": 18, "condition": "Cloudy"},
    }

    return weather.get(city.lower(), {"temperature": "Unknown", "condition": "Unknown"})
