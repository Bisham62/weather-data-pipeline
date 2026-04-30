import pandas as pd
import os

def save_data(df):
    file_exists = os.path.isfile("weather_data.csv")

    if file_exists:
        existing_df = pd.read_csv("weather_data.csv")

        if df["time"][0] in existing_df["time"].values:
            print("\nData already exists. Skipping duplicate entry.")
        else:
            df.to_csv("weather_data.csv", mode='a', header=False, index=False)
            print("\nNew data appended.")
    else:
        df.to_csv("weather_data.csv", index=False)
        print("\nFile created and data saved.")