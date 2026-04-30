from fetch import fetch_weather
from process import process_weather
from storage import save_data
from db import init_db, insert_weather
from db import init_db, insert_weather, log_pipeline_run


init_db()

weather = fetch_weather()
df = process_weather(weather)

print("\n---Weather Analytics ---")

avg_temp = df["temperature"].mean()
max_temp = df["temperature"].max()
min_temp = df["temperature"].min()
avg_wind = df["windspeed"].mean()

print(f"Average Temperature: {avg_temp:.2f} °C")
print(f"Max Temperature: {max_temp:.2f} °C")
print(f"Min Temperature: {min_temp:.2f} °C")
print(f"Average Wind Speed: {avg_wind:.2f} km/h")

print("\nDataFrame:\n")
print(df)

print("\nWeather Insights:")
if df["temperature"][0] > 25:
    print("Hot weather")
elif df["temperature"][0] < 15:
    print("Cold weather")
else:
    print("Moderate weather")

save_data(df)

rows = insert_weather(df)
log_pipeline_run("SUCCESS", rows)