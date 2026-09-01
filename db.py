import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        time TEXT PRIMARY KEY,
        temperature REAL,
        windspeed REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pipeline_runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_time TEXT,
        status TEXT,
        rows_inserted INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_weather(df):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    time = str(df["time"][0])
    temperature = df["temperature"][0]
    windspeed = df["windspeed"][0]

    try:
        cursor.execute("""
        INSERT INTO weather (time, temperature, windspeed)
        VALUES (?, ?, ?)
        """, (time, temperature, windspeed))

        conn.commit()
        print("Data inserted into database.")
        return 1  # Indicate one row inserted

    except sqlite3.IntegrityError:
        print("Duplicate entry in database. Skipping.")
        return 0  # Indicate no rows inserted due to duplicate

    finally:
        conn.close()


def log_pipeline_run(status, rows_inserted):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    run_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO pipeline_runs (run_time, status, rows_inserted)
    VALUES (?, ?, ?)
    """, (run_time, status, rows_inserted))

    conn.commit()
    conn.close()
