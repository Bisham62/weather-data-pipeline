import pandas as pd

def process_weather(weather):
    df = pd.DataFrame([{
        "time": weather["time"],
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"]
    }])
    return df