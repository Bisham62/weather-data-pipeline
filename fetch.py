import requests

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=30.2672&longitude=-97.7431&current_weather=true"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.Timeout:
        raise RuntimeError("The weather API did not respond within 10 seconds.")
    except requests.exceptions.RequestException as error:
        raise RuntimeError(f"Could not fetch weather data: {error}")
    
    if "current_weather" not in data:
        raise RuntimeError("The weather API response is missing current weather data.")

    return data["current_weather"]
