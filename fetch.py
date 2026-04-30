import requests

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=30.2672&longitude=-97.7431&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return data["current_weather"]