import pandas as pd
import os


def save_data(df):
    file_path = "weather_data.csv"
    new_time = str(df["time"][0])

    if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
        existing_df = pd.read_csv(file_path)
        existing_times = existing_df["time"].astype(str)

        if new_time in existing_times.values:
            print("\nData already exists. Skipping duplicate entry.")
            return

        df.to_csv(file_path, mode="a", header=False, index=False)
        print("\nNew data appended.")
    else:
        df.to_csv(file_path, index=False)
        print("\nFile created and data saved.")
