import pandas as pd


def process_weather(weather):
    required_fields = ["time", "temperature", "windspeed"]
    
    for field in required_fields:
        if field not in weather or weather[field] is None:
            raise ValueError(f"Weather data is missing required field: {field}")

    df = pd.DataFrame([{
        "time": weather["time"],
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"]
    }])
    return df
